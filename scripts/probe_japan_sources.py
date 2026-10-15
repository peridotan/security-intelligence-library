#!/usr/bin/env python3
"""Read-only live probe for Japanese first-party collection sources."""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path
import os
import sys

import yaml

from collect_intelligence_candidates import fetch_source, parse_xml_feed
from official_html_sources import parse_html_listing
from official_csv_sources import parse_nco_csv

ROOT = Path(__file__).resolve().parents[1]
SOURCE_IDS = (
    "nict-security-press",
    "ipa-security-alerts",
    "jpcert-alerts-jp",
    "nco-security-news",
)


def probe(config: Path, timeout: int) -> tuple[list[tuple[str, int, str]], bool]:
    registry = yaml.safe_load(config.read_text(encoding="utf-8"))
    by_id = {s["id"]: s for s in registry["sources"]}
    results: list[tuple[str, int, str]] = []
    ok = True

    for source_id in SOURCE_IDS:
        source = by_id.get(source_id)
        if not source or not source.get("enabled"):
            results.append((source_id, 0, "missing or disabled"))
            ok = False
            continue
        try:
            if source["type"] == "csv_yearly":
                now_jst = datetime.now(timezone(timedelta(hours=9)))
                source = dict(source, url=source["url"].replace("{year}", str(now_jst.year)))
            payload = fetch_source(source, timeout)
            if source["type"] == "rss":
                records = parse_xml_feed(payload, source)
            elif source["type"] == "html_listing":
                records = parse_html_listing(payload, source)
            elif source["type"] == "csv_yearly":
                records = parse_nco_csv(payload, source)
            else:
                raise ValueError(f"unsupported type: {source['type']}")
            count = len(records)
            status = "ok" if count else "no items parsed; check source format"
            ok = ok and count > 0
            results.append((source_id, count, status))
            for item in sorted(records, key=lambda x: x.get("published_raw", ""), reverse=True)[:3]:
                print(f"SAMPLE {source_id}: {item['published_raw']} | {item['title'][:90]} | {item['url']}")
            if source_id == "nict-security-press" and not any(
                "/press/2026/10/13-1.html" in str(item["url"]) for item in records
            ):
                print("NICT A2B notice no longer in current listing; verify historical coverage.")
        except Exception as exc:
            results.append((source_id, 0, f"{type(exc).__name__}: {exc}"))
            ok = False

    return results, ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, default=ROOT / "config/intelligence_sources.yml")
    ap.add_argument("--timeout", type=int, default=20)
    args = ap.parse_args()
    results, ok = probe(args.config, args.timeout)
    lines = [
        "### Japanese first-party source live probe",
        "",
        "| Source | Parsed items | Status |",
        "| --- | ---: | --- |",
    ]
    for source, count, status in results:
        lines.append(f"| {source} | {count} | {status.replace('|', '/')} |")
    report = "\n".join(lines) + "\n"
    print(report)
    summary = os.getenv("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(report)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

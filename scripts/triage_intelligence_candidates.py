#!/usr/bin/env python3
"""Enrich and deterministically route collected Security Intelligence candidates.

Routes:
- library: eligible for the future article-drafting phase
- vulnerability: product/CVE-level intelligence better suited to Vulnerability Intelligence
- watch: keep for human attention, but do not draft automatically

This script does not publish content and does not use an LLM.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import json
import re
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "intelligence_triage.yml"

USER_AGENT = (
    "Security-Intelligence-Library/1.0 "
    "(+https://github.com/peridotan/security-intelligence-library)"
)

SSVC_E_RE = re.compile(r"(?:^|/)E:([NPA])(?:/|$)")
EXPLOITATION_LABELS = {"N": "None", "P": "PoC", "A": "Active"}
EXPLOITATION_RANK = {"Unknown": 0, "None": 1, "PoC": 2, "Active": 3}


def fetch_bytes(url: str, timeout: int) -> bytes:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json, */*",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        return response.read()


def github_blob_to_raw(url: str) -> str:
    prefix = "https://github.com/"
    if not url.startswith(prefix) or "/blob/" not in url:
        return url
    rest = url[len(prefix):]
    repo_part, path_part = rest.split("/blob/", 1)
    return f"https://raw.githubusercontent.com/{repo_part}/{path_part}"


def note_text(notes: list[dict], title: str | None = None, category: str | None = None) -> str:
    for note in notes or []:
        if title and str(note.get("title", "")).lower() != title.lower():
            continue
        if category and str(note.get("category", "")).lower() != category.lower():
            continue
        text = str(note.get("text", "")).strip()
        if text:
            return text
    return ""


def extract_exploitation(vulnerabilities: list[dict]) -> str:
    best = "Unknown"
    for vulnerability in vulnerabilities:
        for note in vulnerability.get("notes", []) or []:
            if str(note.get("title", "")).upper() != "SSVC":
                continue
            match = SSVC_E_RE.search(str(note.get("text", "")))
            if not match:
                continue
            label = EXPLOITATION_LABELS.get(match.group(1), "Unknown")
            if EXPLOITATION_RANK[label] > EXPLOITATION_RANK[best]:
                best = label
    return best


def extract_max_cvss(vulnerabilities: list[dict]) -> float | None:
    values: list[float] = []
    for vulnerability in vulnerabilities:
        for score in vulnerability.get("scores", []) or []:
            if not isinstance(score, dict):
                continue
            for key in ("cvss_v4", "cvss_v3", "cvss_v2"):
                metric = score.get(key)
                if not isinstance(metric, dict):
                    continue
                raw = metric.get("baseScore")
                try:
                    values.append(float(raw))
                except (TypeError, ValueError):
                    pass
    return max(values) if values else None


def extract_csaf(candidate: dict, timeout: int) -> dict:
    detail_url = github_blob_to_raw(candidate["url"])
    payload = json.loads(fetch_bytes(detail_url, timeout).decode("utf-8-sig"))

    document = payload.get("document", {}) or {}
    vulnerabilities = payload.get("vulnerabilities", []) or []
    notes = document.get("notes", []) or []

    summary = (
        note_text(notes, title="Risk Evaluation")
        or note_text(notes, category="summary")
        or candidate.get("summary", "")
    )

    cves = sorted(
        {
            str(vulnerability.get("cve")).strip()
            for vulnerability in vulnerabilities
            if vulnerability.get("cve")
        }
    )

    return {
        "detail_type": "csaf",
        "detail_url": detail_url,
        "document_category": document.get("category"),
        "summary": summary,
        "vulnerability_count": len(vulnerabilities),
        "cves": cves,
        "max_cvss": extract_max_cvss(vulnerabilities),
        "exploitation": extract_exploitation(vulnerabilities),
    }


def route_candidate(candidate: dict, enrichment: dict, config: dict) -> tuple[str, list[str]]:
    source_id = candidate.get("source_id", "")
    source_defaults = config.get("source_defaults", {}) or {}
    default_route = source_defaults.get(
        source_id,
        (config.get("defaults", {}) or {}).get("route", "watch"),
    )

    reasons: list[str] = []
    if enrichment.get("detail_type") != "csaf":
        reasons.append(f"source default route: {default_route}")
        return default_route, reasons

    if enrichment.get("enrichment_error"):
        reasons.append("detail enrichment failed; hold for human review")
        return "watch", reasons

    rules = config.get("csaf", {}) or {}
    exploitation = enrichment.get("exploitation", "Unknown")
    max_cvss = enrichment.get("max_cvss")
    vulnerability_count = int(enrichment.get("vulnerability_count") or 0)

    if exploitation == "Active":
        route = rules.get("active_exploitation_route", "library")
        reasons.append("SSVC exploitation is Active")
        return route, reasons

    if exploitation == "PoC":
        route = rules.get("poc_exploitation_route", "watch")
        reasons.append("SSVC exploitation indicates PoC")
        return route, reasons

    min_cvss = float(rules.get("watch_min_cvss", 9.0))
    if max_cvss is not None and float(max_cvss) >= min_cvss:
        reasons.append(f"max CVSS {max_cvss:g} >= watch threshold {min_cvss:g}")
        return "watch", reasons

    min_vulns = int(rules.get("watch_min_vulnerabilities", 3))
    if vulnerability_count >= min_vulns:
        reasons.append(
            f"{vulnerability_count} vulnerabilities >= watch threshold {min_vulns}"
        )
        return "watch", reasons

    reasons.append(
        f"product-specific CSAF advisory; source default route: {default_route}"
    )
    return default_route, reasons


def enrich_and_route(candidate: dict, config: dict, timeout: int) -> dict:
    item = dict(candidate)
    enrichment: dict = {}

    if item.get("source_id") == "cisa-csaf-it":
        try:
            enrichment = extract_csaf(item, timeout)
        except (
            HTTPError,
            URLError,
            TimeoutError,
            json.JSONDecodeError,
            UnicodeDecodeError,
            ValueError,
        ) as exc:
            enrichment = {
                "detail_type": "csaf",
                "detail_url": github_blob_to_raw(item["url"]),
                "enrichment_error": f"{type(exc).__name__}: {exc}",
                "vulnerability_count": None,
                "cves": [],
                "max_cvss": None,
                "exploitation": "Unknown",
            }

    if enrichment.get("summary"):
        item["summary"] = enrichment["summary"]

    route, reasons = route_candidate(item, enrichment, config)
    item["enrichment"] = enrichment
    item["triage"] = {
        "route": route,
        "draft_eligible": route == "library",
        "reasons": reasons,
    }
    return item


def render_markdown(payload: dict) -> str:
    candidates = payload["candidates"]
    route_counts = Counter(
        item.get("triage", {}).get("route", "watch") for item in candidates
    )

    lines = [
        "# Security Intelligence Triage Review",
        "",
        f"- Generated: {payload.get('generated_at')}",
        f"- Collection window: {payload.get('window_days')} day(s)",
        f"- Candidate count: {len(candidates)}",
        f"- Library: {route_counts['library']}",
        f"- Vulnerability: {route_counts['vulnerability']}",
        f"- Watch: {route_counts['watch']}",
        f"- Source errors: {len(payload.get('source_errors', []))}",
        "",
        "Approval of this PR confirms the routing result. It does **not** publish any",
        "Library article. Only candidates routed to **Library** are eligible for the",
        "future article-drafting phase.",
        "",
        "## Routing summary",
        "",
        "| Candidate | Route | Exploitation | Max CVSS | CVEs |",
        "| --- | --- | --- | ---: | ---: |",
    ]

    for item in candidates:
        enrichment = item.get("enrichment", {})
        triage = item.get("triage", {})
        max_cvss = enrichment.get("max_cvss")
        max_cvss_text = f"{max_cvss:g}" if isinstance(max_cvss, (int, float)) else "—"
        lines.append(
            f"| {item['title']} | **{triage.get('route', 'watch')}** | "
            f"{enrichment.get('exploitation', '—')} | {max_cvss_text} | "
            f"{len(enrichment.get('cves', []))} |"
        )

    lines += ["", "## Candidates", ""]

    for index, item in enumerate(candidates, 1):
        enrichment = item.get("enrichment", {})
        triage = item.get("triage", {})
        max_cvss = enrichment.get("max_cvss")
        max_cvss_text = f"{max_cvss:g}" if isinstance(max_cvss, (int, float)) else "—"
        cves = ", ".join(enrichment.get("cves", [])) or "—"
        reasons = "; ".join(triage.get("reasons", [])) or "—"

        lines += [
            f"### {index}. {item['title']}",
            "",
            f"- **Recommended route:** `{triage.get('route', 'watch')}`",
            f"- Draft eligible: `{str(bool(triage.get('draft_eligible'))).lower()}`",
            f"- Source: {item.get('source_name', '—')}",
            f"- Published: {item.get('published_at') or item.get('published_raw') or 'unknown'}",
            f"- Vulnerabilities: {enrichment.get('vulnerability_count', '—')}",
            f"- CVEs: {cves}",
            f"- Max CVSS: {max_cvss_text}",
            f"- SSVC exploitation: {enrichment.get('exploitation', '—')}",
            f"- Reason: {reasons}",
            f"- URL: {item.get('url', '')}",
        ]

        if enrichment.get("enrichment_error"):
            lines.append(f"- Enrichment warning: `{enrichment['enrichment_error']}`")

        if item.get("summary"):
            lines += ["", f"> {item['summary']}"]

        lines += ["", "---", ""]

    if payload.get("source_errors"):
        lines += ["## Source collection warnings", ""]
        for error in payload["source_errors"]:
            lines.append(
                f"- **{error.get('source_name', error.get('source_id', 'unknown'))}**: "
                f"{error.get('error', 'unknown error')}"
            )
        lines.append("")

    return "\n".join(lines)


def write_github_output(path: str | None, output_json: Path, output_md: Path, payload: dict):
    if not path:
        return

    counts = Counter(
        item.get("triage", {}).get("route", "watch")
        for item in payload.get("candidates", [])
    )
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(f"candidate_count={len(payload.get('candidates', []))}\n")
        fh.write(f"library_count={counts['library']}\n")
        fh.write(f"vulnerability_count={counts['vulnerability']}\n")
        fh.write(f"watch_count={counts['watch']}\n")
        fh.write(f"candidate_json={output_json.as_posix()}\n")
        fh.write(f"candidate_md={output_md.as_posix()}\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-json", type=Path, required=True)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-md", type=Path, required=True)
    parser.add_argument("--github-output", default=None)
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()

    source_payload = json.loads(args.input_json.read_text(encoding="utf-8"))
    config = yaml.safe_load(args.config.read_text(encoding="utf-8")) or {}

    candidates = [
        enrich_and_route(item, config, args.timeout)
        for item in source_payload.get("candidates", [])
    ]

    payload = dict(source_payload)
    payload["schema_version"] = 2
    payload["triage_policy_version"] = config.get("version", 1)
    payload["candidates"] = candidates
    payload["route_counts"] = dict(
        Counter(
            item.get("triage", {}).get("route", "watch")
            for item in candidates
        )
    )

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.parent.mkdir(parents=True, exist_ok=True)

    args.output_json.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    args.output_md.write_text(render_markdown(payload), encoding="utf-8")

    write_github_output(args.github_output, args.output_json, args.output_md, payload)

    counts = Counter(
        item.get("triage", {}).get("route", "watch") for item in candidates
    )
    print(
        f"Triaged {len(candidates)} candidate(s): "
        f"library={counts['library']}, "
        f"vulnerability={counts['vulnerability']}, "
        f"watch={counts['watch']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

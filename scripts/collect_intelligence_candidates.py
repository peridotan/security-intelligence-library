#!/usr/bin/env python3
"""Collect recent Security Intelligence candidates from configured feeds.

Phase 2A intentionally stops at candidate collection. It does not publish articles and
does not use an LLM. The generated JSON/Markdown files are submitted through the
existing human review pull-request flow.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path
import json
import re
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import xml.etree.ElementTree as ET

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "intelligence_sources.yml"
DOCS = ROOT / "docs"
AUTOMATION_REVIEW = ROOT / ".automation-review"

USER_AGENT = (
    "Security-Intelligence-Library/1.0 "
    "(+https://github.com/peridotan/security-intelligence-library)"
)
URL_RE = re.compile(r"https?://[^\s)>\]\"']+")
TAG_RE = re.compile(r"<[^>]+>")
SPACE_RE = re.compile(r"\s+")


def clean_text(value: str | None, limit: int = 700) -> str:
    if not value:
        return ""
    value = TAG_RE.sub(" ", unescape(str(value)))
    value = SPACE_RE.sub(" ", value).strip()
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    value = str(value).strip()
    try:
        dt = parsedate_to_datetime(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except (TypeError, ValueError, OverflowError):
        pass

    normalized = value.replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(normalized)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError:
        return None


def get_nested(value, path: str | None, default=None):
    if not path:
        return default
    current = value
    for part in path.split("."):
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return default
    return current


def transform_link(link: str, source: dict) -> str:
    link = (link or "").strip()
    if source.get("link_transform") == "github_raw_to_blob":
        prefix = "https://raw.githubusercontent.com/"
        if link.startswith(prefix):
            rest = link[len(prefix):]
            parts = rest.split("/", 3)
            if len(parts) == 4:
                owner, repo, ref, path = parts
                return f"https://github.com/{owner}/{repo}/blob/{ref}/{path}"
    return link


def child_text(node: ET.Element, names: tuple[str, ...]) -> str:
    for child in list(node):
        local = child.tag.rsplit("}", 1)[-1].lower()
        if local in names and child.text:
            return child.text.strip()
    return ""


def atom_link(node: ET.Element) -> str:
    for child in list(node):
        if child.tag.rsplit("}", 1)[-1].lower() != "link":
            continue
        href = child.attrib.get("href", "").strip()
        rel = child.attrib.get("rel", "alternate")
        if href and rel in ("", "alternate"):
            return href
    return ""


def make_record(
    source: dict,
    title: str,
    link: str,
    summary: str,
    published_raw: str,
) -> dict:
    published = parse_datetime(published_raw)
    return {
        "source_id": source["id"],
        "source_name": source["name"],
        "source_url": source["url"],
        "title": clean_text(title, 500),
        "url": transform_link(link, source),
        "summary": clean_text(summary),
        "published_at": published.isoformat() if published else None,
        "published_raw": published_raw or None,
        "category_hint": source.get("category_hint", ""),
        "trust": source.get("trust", ""),
    }


def parse_xml_feed(xml_bytes: bytes, source: dict) -> list[dict]:
    root = ET.fromstring(xml_bytes)
    root_name = root.tag.rsplit("}", 1)[-1].lower()
    records: list[dict] = []

    if root_name == "rss":
        channel = next(
            (c for c in list(root) if c.tag.rsplit("}", 1)[-1].lower() == "channel"),
            root,
        )
        entries = [
            c for c in list(channel)
            if c.tag.rsplit("}", 1)[-1].lower() == "item"
        ]
        for item in entries:
            title = child_text(item, ("title",))
            link = child_text(item, ("link",))
            summary = child_text(item, ("description", "summary"))
            published_raw = child_text(
                item, ("pubdate", "published", "updated", "date")
            )
            if title and link:
                records.append(
                    make_record(source, title, link, summary, published_raw)
                )

    elif root_name == "feed":
        entries = [
            c for c in list(root)
            if c.tag.rsplit("}", 1)[-1].lower() == "entry"
        ]
        for item in entries:
            title = child_text(item, ("title",))
            link = atom_link(item)
            summary = child_text(item, ("summary", "content"))
            published_raw = child_text(item, ("published", "updated"))
            if title and link:
                records.append(
                    make_record(source, title, link, summary, published_raw)
                )
    else:
        raise ValueError(f"unsupported feed root: {root_name}")

    return records


def parse_json_feed(json_bytes: bytes, source: dict) -> list[dict]:
    data = json.loads(json_bytes.decode("utf-8-sig"))
    entries = get_nested(data, source.get("entry_path", "entries"), [])
    if not isinstance(entries, list):
        raise ValueError("JSON feed entry_path did not resolve to a list")

    field_map = source.get("field_map", {})
    title_path = field_map.get("title", "title")
    link_path = field_map.get("link", "link")
    summary_path = field_map.get("summary")
    published_path = field_map.get("published", "published")
    updated_path = field_map.get("updated", "updated")

    records: list[dict] = []
    for item in entries:
        if not isinstance(item, dict):
            continue
        title = get_nested(item, title_path, "")
        link = get_nested(item, link_path, "")
        summary = get_nested(item, summary_path, "") if summary_path else ""
        published_raw = (
            get_nested(item, published_path, "")
            or get_nested(item, updated_path, "")
            or ""
        )
        if title and link:
            records.append(
                make_record(
                    source,
                    str(title),
                    str(link),
                    str(summary or ""),
                    str(published_raw or ""),
                )
            )
    return records


def fetch_source(source: dict, timeout: int) -> bytes:
    accept = (
        "application/json, application/feed+json, "
        "application/rss+xml, application/atom+xml, application/xml, text/xml, */*"
    )
    request = Request(
        source["url"],
        headers={"User-Agent": USER_AGENT, "Accept": accept},
    )
    with urlopen(request, timeout=timeout) as response:
        return response.read()


def accepted_triage_urls() -> set[str]:
    """Return URLs already accepted by merged schema-v2 triage reviews."""
    urls: set[str] = set()
    if not AUTOMATION_REVIEW.exists():
        return urls

    for path in sorted(AUTOMATION_REVIEW.glob("candidates-*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            continue

        if int(payload.get("schema_version") or 0) < 2:
            continue

        for candidate in payload.get("candidates", []) or []:
            if not isinstance(candidate, dict) or "triage" not in candidate:
                continue
            url = str(candidate.get("url", "") or "").strip()
            if url:
                urls.add(url)

    return urls


def existing_urls() -> set[str]:
    # A merged triage review is a completed human decision even when the route is
    # Vulnerability or Watch. Do not propose the same source again every week.
    urls: set[str] = accepted_triage_urls()
    if not DOCS.exists():
        return urls
    for path in DOCS.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        urls.update(URL_RE.findall(text))
    return urls


def unique_recent(
    records: list[dict],
    cutoff: datetime,
    known_urls: set[str],
) -> list[dict]:
    selected: dict[str, dict] = {}
    for record in records:
        url = record["url"]
        if url in known_urls:
            continue
        published = parse_datetime(record.get("published_at"))
        if published is not None and published < cutoff:
            continue
        selected.setdefault(url, record)

    def sort_key(item: dict):
        dt = parse_datetime(item.get("published_at"))
        return dt or datetime.min.replace(tzinfo=timezone.utc)

    return sorted(selected.values(), key=sort_key, reverse=True)


def render_markdown(
    candidates: list[dict],
    errors: list[dict],
    source_stats: list[dict],
    generated_at: datetime,
    days: int,
) -> str:
    start = (generated_at - timedelta(days=days)).date().isoformat()
    end = generated_at.date().isoformat()
    candidate_counts = Counter(item["source_id"] for item in candidates)

    lines = [
        "# Security Intelligence Candidate Review",
        "",
        f"- Generated: {generated_at.isoformat()}",
        f"- Collection window: {start} – {end}",
        f"- Candidate count: {len(candidates)}",
        f"- Source errors: {len(errors)}",
        "",
        "This file is generated automatically. Approval of this PR means the candidate set",
        "is acceptable for the next drafting phase; it does **not** publish Library articles.",
        "",
        "## Source status",
        "",
        "| Source | Type | Fetched | Candidates | Status |",
        "| --- | --- | ---: | ---: | --- |",
    ]

    error_ids = {item["source_id"] for item in errors}
    for stat in source_stats:
        status = "warning" if stat["source_id"] in error_ids else "ok"
        lines.append(
            f"| {stat['source_name']} | `{stat['source_type']}` | "
            f"{stat['fetched']} | {candidate_counts[stat['source_id']]} | {status} |"
        )
    lines.append("")

    if candidates:
        lines += ["## Candidates", ""]
        for index, item in enumerate(candidates, 1):
            published = item.get("published_at") or item.get("published_raw") or "unknown"
            lines += [
                f"### {index}. {item['title']}",
                "",
                f"- Source: {item['source_name']}",
                f"- Published: {published}",
                f"- Category hint: `{item.get('category_hint') or 'unclassified'}`",
                f"- Trust: `{item.get('trust') or 'unspecified'}`",
                f"- URL: {item['url']}",
            ]
            if item.get("summary"):
                lines += ["", f"> {item['summary']}"]
            lines += ["", "---", ""]
    else:
        lines += ["## Candidates", "", "No new candidates were found.", ""]

    if errors:
        lines += ["## Source collection warnings", ""]
        for error in errors:
            lines.append(
                f"- **{error['source_name']}** (`{error['source_id']}`): {error['error']}"
            )
        lines.append("")

    return "\n".join(lines)


def write_github_output(path: str | None, count: int, json_path: Path, md_path: Path):
    if not path:
        return
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(f"candidate_count={count}\n")
        fh.write(f"candidate_json={json_path.as_posix()}\n")
        fh.write(f"candidate_md={md_path.as_posix()}\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-md", type=Path, required=True)
    parser.add_argument("--github-output", default=None)
    args = parser.parse_args()

    if args.days < 1:
        raise SystemExit("--days must be at least 1")

    config = yaml.safe_load(args.config.read_text(encoding="utf-8")) or {}
    sources = [
        source for source in config.get("sources", [])
        if source.get("enabled", True)
    ]
    if not sources:
        raise SystemExit("no enabled sources configured")

    generated_at = datetime.now(timezone.utc)
    cutoff = generated_at - timedelta(days=args.days)
    collected: list[dict] = []
    errors: list[dict] = []
    source_stats: list[dict] = []

    for source in sources:
        source_type = source.get("type")
        fetched_count = 0
        try:
            payload = fetch_source(source, args.timeout)
            if source_type == "rss":
                records = parse_xml_feed(payload, source)
            elif source_type == "json_feed":
                records = parse_json_feed(payload, source)
            else:
                raise ValueError(f"unsupported source type: {source_type}")
            fetched_count = len(records)
            collected.extend(records)
        except (
            HTTPError,
            URLError,
            TimeoutError,
            ET.ParseError,
            json.JSONDecodeError,
            UnicodeDecodeError,
            ValueError,
        ) as exc:
            errors.append(
                {
                    "source_id": source.get("id", "unknown"),
                    "source_name": source.get("name", source.get("id", "unknown")),
                    "error": f"{type(exc).__name__}: {exc}",
                }
            )
        source_stats.append(
            {
                "source_id": source.get("id", "unknown"),
                "source_name": source.get("name", source.get("id", "unknown")),
                "source_type": source_type or "unknown",
                "fetched": fetched_count,
            }
        )

    candidates = unique_recent(collected, cutoff, existing_urls())

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "schema_version": 1,
        "generated_at": generated_at.isoformat(),
        "window_days": args.days,
        "candidate_count": len(candidates),
        "source_stats": source_stats,
        "source_errors": errors,
        "candidates": candidates,
    }
    args.output_json.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    args.output_md.write_text(
        render_markdown(candidates, errors, source_stats, generated_at, args.days),
        encoding="utf-8",
    )
    write_github_output(
        args.github_output,
        len(candidates),
        args.output_json,
        args.output_md,
    )

    print(
        f"Collected {len(candidates)} new candidate(s) "
        f"from {len(sources)} configured source(s); "
        f"{len(errors)} source warning(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

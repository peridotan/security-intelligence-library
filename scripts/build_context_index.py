#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = DOCS / "assets" / "context-index.json"

CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,}\b", re.IGNORECASE)

# Summary / directory pages are intentionally excluded in Phase 7a.
EXCLUDED_DIRS = {
    "about",
    "monthly",
    "quarterly",
    "topics",
    "tags",
    "assets",
    "javascripts",
    "stylesheets",
}


def split_front_matter(text: str):
    if not text.startswith("---\n"):
        return None, text

    parts = text.split("---\n", 2)
    if len(parts) != 3:
        return None, text

    return yaml.safe_load(parts[1]) or {}, parts[2]


def normalize_cve(value: str) -> str:
    return value.strip().upper()


def normalize_cve_list(values):
    result = []
    seen = set()

    for value in values or []:
        value = normalize_cve(str(value))
        if not CVE_RE.fullmatch(value):
            continue
        if value not in seen:
            result.append(value)
            seen.add(value)

    return sorted(result)


def page_key(path: Path) -> str:
    rel = path.relative_to(DOCS).with_suffix("")
    return rel.as_posix().rstrip("/") + "/"


def article_context(path: Path):
    text = path.read_text(encoding="utf-8")

    try:
        meta, body = split_front_matter(text)
    except yaml.YAMLError:
        return None

    if not meta:
        return None

    if meta.get("status") != "published":
        return None

    if path.name == "index.md" or "sample" in path.name.lower():
        return None

    relative_parts = path.relative_to(DOCS).parts
    if any(part in EXCLUDED_DIRS for part in relative_parts[:-1]):
        return None

    # Optional future/manual override:
    #
    # handoff:
    #   cves:
    #     - CVE-2026-1234
    #   exclude_cves:
    #     - CVE-2026-9999
    #
    handoff = meta.get("handoff") or {}

    explicit_cves = handoff.get("cves")
    if explicit_cves is not None:
        cves = normalize_cve_list(explicit_cves)
        source = "front-matter"
    else:
        found = CVE_RE.findall(text)
        cves = normalize_cve_list(found)
        source = "auto"

    excludes = set(normalize_cve_list(handoff.get("exclude_cves")))
    if excludes:
        cves = [cve for cve in cves if cve not in excludes]

    return {
        "title": str(meta.get("title") or path.stem),
        "source": path.relative_to(ROOT).as_posix(),
        "cves": cves,
        "cve_count": len(cves),
        "detection": source,
    }


def main():
    articles = {}
    scanned = 0

    for path in sorted(DOCS.rglob("*.md")):
        context = article_context(path)
        if context is None:
            continue

        scanned += 1

        # Keep only articles that actually carry CVE context.
        if not context["cves"]:
            continue

        articles[page_key(path)] = context

    unique_cves = sorted({
        cve
        for article in articles.values()
        for cve in article["cves"]
    })

    data = {
        "schema_version": "1.0",
        "articles_scanned": scanned,
        "articles_with_cves": len(articles),
        "unique_cve_count": len(unique_cves),
        "articles": articles,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        "Context index generated: "
        f"{scanned} articles scanned / "
        f"{len(articles)} with CVEs / "
        f"{len(unique_cves)} unique CVEs"
    )
    print(f"Output: {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

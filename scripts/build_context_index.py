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
ACTOR_RE = re.compile(r"\bG\d{4}\b", re.IGNORECASE)
TECHNIQUE_RE = re.compile(r"\bT\d{4}(?:\.\d{3})?\b", re.IGNORECASE)

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


def normalize_list(values, pattern):
    result = []
    seen = set()

    for value in values or []:
        value = str(value).strip().upper()

        if not pattern.fullmatch(value):
            continue

        if value not in seen:
            result.append(value)
            seen.add(value)

    return sorted(result)


def page_key(path: Path) -> str:
    rel = path.relative_to(DOCS).with_suffix("")
    return rel.as_posix().rstrip("/") + "/"


def mapped_techniques(meta):
    result = []

    for row in meta.get("mitre_attack") or []:
        if isinstance(row, dict):
            value = row.get("id")
        else:
            value = row

        if value:
            result.append(value)

    return normalize_list(result, TECHNIQUE_RE)


def article_context(path: Path):
    text = path.read_text(encoding="utf-8")

    try:
        meta, body = split_front_matter(text)
    except yaml.YAMLError:
        return None

    if not meta or meta.get("status") != "published":
        return None

    if path.name == "index.md" or "sample" in path.name.lower():
        return None

    relative_parts = path.relative_to(DOCS).parts

    if any(part in EXCLUDED_DIRS for part in relative_parts[:-1]):
        return None

    handoff = meta.get("handoff") or {}

    # --------------------------------------------------
    # CVE
    # --------------------------------------------------
    explicit_cves = handoff.get("cves")

    if explicit_cves is not None:
        cves = normalize_list(explicit_cves, CVE_RE)
        cve_detection = "front-matter"
    else:
        cves = normalize_list(CVE_RE.findall(text), CVE_RE)
        cve_detection = "auto"

    excluded_cves = set(
        normalize_list(handoff.get("exclude_cves"), CVE_RE)
    )
    cves = [x for x in cves if x not in excluded_cves]

    # --------------------------------------------------
    # Threat Actor / ATT&CK Group
    # --------------------------------------------------
    explicit_actors = handoff.get("actors")

    if explicit_actors is not None:
        actors = normalize_list(explicit_actors, ACTOR_RE)
        actor_detection = "front-matter"
    else:
        actors = normalize_list(ACTOR_RE.findall(text), ACTOR_RE)
        actor_detection = "auto"

    excluded_actors = set(
        normalize_list(handoff.get("exclude_actors"), ACTOR_RE)
    )
    actors = [x for x in actors if x not in excluded_actors]

    # --------------------------------------------------
    # ATT&CK Techniques
    #
    # Existing mitre_attack Front Matter is authoritative.
    # We intentionally do NOT scrape all Txxxx strings from body text.
    # --------------------------------------------------
    explicit_techniques = handoff.get("techniques")

    if explicit_techniques is not None:
        techniques = normalize_list(
            explicit_techniques,
            TECHNIQUE_RE,
        )
        technique_detection = "front-matter"
    else:
        techniques = mapped_techniques(meta)
        technique_detection = "mitre_attack"

    excluded_techniques = set(
        normalize_list(
            handoff.get("exclude_techniques"),
            TECHNIQUE_RE,
        )
    )
    techniques = [
        x for x in techniques
        if x not in excluded_techniques
    ]

    return {
        "title": str(meta.get("title") or path.stem),
        "source": path.relative_to(ROOT).as_posix(),

        "cves": cves,
        "cve_count": len(cves),

        "actors": actors,
        "actor_count": len(actors),

        "techniques": techniques,
        "technique_count": len(techniques),

        "detection": {
            "cves": cve_detection,
            "actors": actor_detection,
            "techniques": technique_detection,
        },
    }


def main():
    articles = {}
    scanned = 0

    for path in sorted(DOCS.rglob("*.md")):
        context = article_context(path)

        if context is None:
            continue

        scanned += 1

        if not (
            context["cves"]
            or context["actors"]
            or context["techniques"]
        ):
            continue

        articles[page_key(path)] = context

    unique_cves = sorted({
        x
        for row in articles.values()
        for x in row["cves"]
    })

    unique_actors = sorted({
        x
        for row in articles.values()
        for x in row["actors"]
    })

    unique_techniques = sorted({
        x
        for row in articles.values()
        for x in row["techniques"]
    })

    data = {
        "schema_version": "1.1",
        "articles_scanned": scanned,
        "articles_with_context": len(articles),

        "articles_with_cves": sum(
            1 for row in articles.values()
            if row["cves"]
        ),
        "articles_with_actors": sum(
            1 for row in articles.values()
            if row["actors"]
        ),
        "articles_with_techniques": sum(
            1 for row in articles.values()
            if row["techniques"]
        ),

        "unique_cve_count": len(unique_cves),
        "unique_actor_count": len(unique_actors),
        "unique_technique_count": len(unique_techniques),

        "articles": articles,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT.write_text(
        json.dumps(
            data,
            ensure_ascii=False,
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )

    print(
        "Context index generated: "
        f"{scanned} articles scanned / "
        f"{len(articles)} with context"
    )

    print(
        f"CVE: {data['articles_with_cves']} articles / "
        f"{data['unique_cve_count']} unique"
    )

    print(
        f"Actors: {data['articles_with_actors']} articles / "
        f"{data['unique_actor_count']} unique"
    )

    print(
        f"Techniques: {data['articles_with_techniques']} articles / "
        f"{data['unique_technique_count']} unique"
    )

    print(f"Output: {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

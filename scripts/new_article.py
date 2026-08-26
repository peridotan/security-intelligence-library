#!/usr/bin/env python3
"""Create a new article from the standard Security Intelligence Library template."""

from __future__ import annotations
import argparse
from datetime import date
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "article-template.md"
DOCS = ROOT / "docs"

CATEGORIES = {
    "cybersecurity": "Cybersecurity",
    "identity-security": "Identity Security",
    "ai-security": "AI Security",
    "regulation": "Regulation",
    "risk-management": "Management View",
}

def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9-]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")

def main():
    parser = argparse.ArgumentParser(description="Create a Security Intelligence Library article")
    parser.add_argument("category", choices=sorted(CATEGORIES))
    parser.add_argument("slug", help="ASCII slug, e.g. frontier-ai-cyber-risk")
    parser.add_argument("title", help="Article title")
    parser.add_argument("--description", default="", help="Short description")
    parser.add_argument(
        "--source-period",
        default=date.today().strftime("%Y-%m"),
        help="Intelligence source period in YYYY-MM format",
    )
    args = parser.parse_args()

    if not re.fullmatch(r"\d{4}-\d{2}", args.source_period):
        raise SystemExit("--source-period must be YYYY-MM")

    slug = slugify(args.slug)
    if not slug:
        raise SystemExit("slug must contain at least one ASCII letter or number")

    output = DOCS / args.category / f"{slug}.md"
    if output.exists():
        raise SystemExit(f"already exists: {output}")

    today = date.today().isoformat()
    text = TEMPLATE.read_text(encoding="utf-8")
    replacements = {
        "{{TITLE}}": args.title,
        "{{DATE}}": today,
        "{{DESCRIPTION}}": args.description,
        "{{CATEGORY}}": CATEGORIES[args.category],
        "{{COLLECTION}}": args.category,
        "{{SOURCE_PERIOD}}": args.source_period,
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    output.write_text(text, encoding="utf-8")
    print(output.relative_to(ROOT))
    print(
        "Next: edit the article, add reliable sources/footnotes, set status: published, "
        "then run `python scripts/update_content.py`. "
        "Home, category, monthly and topic indexes are generated automatically."
    )

if __name__ == "__main__":
    main()

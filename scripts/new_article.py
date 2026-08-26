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
    "risk-management": "Risk Management",
}


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a Security Intelligence Library article")
    parser.add_argument("category", choices=sorted(CATEGORIES))
    parser.add_argument("slug", help="ASCII slug, e.g. frontier-ai-cyber-risk")
    parser.add_argument("title", help="Article title")
    parser.add_argument("--description", default="", help="Short description")
    args = parser.parse_args()

    slug = slugify(args.slug)
    if not slug:
        raise SystemExit("slug must contain at least one ASCII letter or number")

    output = DOCS / args.category / f"{slug}.md"
    if output.exists():
        raise SystemExit(f"already exists: {output}")

    today = date.today().isoformat()
    text = TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("{{TITLE}}", args.title)
    text = text.replace("{{DATE}}", today)
    text = text.replace("{{DESCRIPTION}}", args.description)
    text = text.replace("{{CATEGORY}}", CATEGORIES[args.category])

    output.write_text(text, encoding="utf-8")
    print(output.relative_to(ROOT))
    print("Next: edit the article, add reliable source URLs, then add it to zensical.toml nav when ready to publish.")


if __name__ == "__main__":
    main()

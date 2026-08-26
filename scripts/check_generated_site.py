#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import os
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"
errors = []

if not SITE.exists():
    raise SystemExit("site/ does not exist; run `zensical build --clean --strict` first")

class Checker(HTMLParser):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.article_stack = []
        self.div_stack = []
        self.meta_depth = 0
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = set((attrs.get("class") or "").split())

        if tag == "article":
            is_card = "sil-card" in classes
            if is_card and any(self.article_stack):
                errors.append(f"{self.page}: nested sil-card <article>")
            if is_card and self.meta_depth > 0:
                errors.append(f"{self.page}: sil-card started inside sil-card-meta")
            self.article_stack.append(is_card)

        if tag == "div":
            is_meta = "sil-card-meta" in classes
            self.div_stack.append(is_meta)
            if is_meta:
                self.meta_depth += 1

        if tag == "a" and attrs.get("href"):
            self.hrefs.append(attrs["href"])

    def handle_endtag(self, tag):
        if tag == "article" and self.article_stack:
            self.article_stack.pop()

        if tag == "div" and self.div_stack:
            was_meta = self.div_stack.pop()
            if was_meta and self.meta_depth:
                self.meta_depth -= 1

def resolve_href(page: Path, href: str):
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc or href.startswith(("mailto:", "#", "javascript:")):
        return None
    path = unquote(parsed.path)
    if not path:
        return None

    if path.startswith("/security-intelligence-library/"):
        path = path[len("/security-intelligence-library/"):]
        target = SITE / path
    elif path.startswith("/"):
        return None
    else:
        target = (page.parent / path).resolve()

    if target.is_dir():
        target = target / "index.html"
    elif target.suffix == "":
        if (target / "index.html").exists():
            target = target / "index.html"
        else:
            target = target.with_suffix(".html")
    return target

html_files = list(SITE.rglob("*.html"))
if not html_files:
    errors.append("site: no generated HTML files")

for page in html_files:
    text = page.read_text(encoding="utf-8", errors="replace")

    # Detect the exact v0.6.0 failure mode in rendered HTML.
    if re.search(r'<div class="sil-card-meta">(?:(?!</div>).)*<article\b', text, re.S):
        errors.append(f"{page.relative_to(ROOT)}: article nested inside sil-card-meta")

    parser = Checker(page.relative_to(ROOT))
    parser.feed(text)

    # Validate only our own sil-card elements. Zensical/the theme may add
    # unrelated <article> elements, so global <article> tag counts are not a
    # valid balance check.
    if any(parser.article_stack):
        errors.append(f"{page.relative_to(ROOT)}: unclosed sil-card <article>")

    for href in parser.hrefs:
        target = resolve_href(page, href)
        if target is not None and not target.exists():
            errors.append(
                f"{page.relative_to(ROOT)}: broken generated internal href `{href}`"
            )

# Every published article source must have a generated HTML page.
for src in DOCS.rglob("*.md"):
    text = src.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        continue
    parts = text.split("---\n", 2)
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        continue
    if not (
        meta.get("status") == "published"
        and src.name != "index.md" and "sample" not in src.name
    ):
        continue
    rel = src.relative_to(DOCS).with_suffix("")
    expected = SITE / rel / "index.html"
    if not expected.exists():
        # Some generators may use .html rather than pretty URLs.
        alternate = SITE / rel.with_suffix(".html")
        if not alternate.exists():
            errors.append(f"site: no generated page for {src.relative_to(ROOT)}")

if errors:
    print("Generated site checks failed:")
    for error in sorted(set(errors)):
        print("-", error)
    sys.exit(1)

print(f"Generated site checks passed ({len(html_files)} HTML files).")

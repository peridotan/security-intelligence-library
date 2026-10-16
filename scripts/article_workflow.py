#!/usr/bin/env python3
"""Scaffold and validate a Library article + Evidence Review bundle.

This helper does not call any model/API, approve evidence, create a PR,
change an article to published, merge, or deploy. Those remain human actions.
"""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys

import yaml

import check_evidence_review as evidence

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    "cybersecurity": "Cybersecurity",
    "identity-security": "Identity Security",
    "ai-security": "AI Security",
    "regulation": "Regulation",
    "risk-management": "Management View",
}
SLUG_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
REQUIRED_HEADINGS = (
    "## Executive Summary",
    "## なぜ今なのか",
    "## 何が起きているのか",
    "## 経営インパクト",
    "## 日本企業への示唆",
    "## 推奨アクション",
    "## 用語解説",
    "## 関連記事",
    "## 参考情報",
)
PLACEHOLDERS = (
    "{{", "}}", "https://example.com", "TBD",
    "TODO", "ここに", "[Primary source]",
    "## Attack / Process Flow（必要な場合）",
)


def validate_key(collection: str, slug: str) -> None:
    if collection not in CATEGORIES:
        raise ValueError(f"Unsupported collection: {collection}")
    if not SLUG_RE.fullmatch(slug) or slug in {"index", "sample"}:
        raise ValueError("slug must use lowercase ASCII letters/numbers and hyphens, excluding index/sample")
    if evidence.article_path(f"docs/{collection}/{slug}.md") is None:
        raise ValueError("Unsafe destination article path")


def bundle_paths(root: Path, collection: str, slug: str, staged: bool = False) -> dict[str, Path]:
    validate_key(collection, slug)
    if staged:
        return {
            "article": root / "docs" / collection / f"{slug}.md",
            "evidence": root / "review" / "evidence" / f"{slug}.json",
            "review": root / "review" / "pilots" / f"{slug}.md",
        }
    return {
        "article": root / "drafts" / collection / f"{slug}.md",
        "evidence": root / "drafts" / "evidence" / f"{slug}.json",
        "review": root / "drafts" / "reviews" / f"{slug}.md",
    }


def init_bundle(
    root: Path, collection: str, slug: str, title: str, draft_date: str, source_period: str,
) -> dict[str, Path]:
    draft = bundle_paths(root, collection, slug)
    destination = bundle_paths(root, collection, slug, staged=True)
    if not title.strip() or "\n" in title or "\r" in title:
        raise ValueError("title must be non-empty and single-line")
    if not evidence.valid_date(draft_date):
        raise ValueError("draft-date must be YYYY-MM-DD")
    period_match = re.fullmatch(r"(\d{4})-(\d{2})", source_period)
    if not period_match or not 1 <= int(period_match.group(2)) <= 12:
        raise ValueError("source-period must be YYYY-MM (01-12)")
    if any(p.exists() for p in (*draft.values(), *destination.values())):
        raise FileExistsError("Draft bundle or target files already exist; refusing to overwrite")

    article = (root / "templates" / "article-template.md").read_text(encoding="utf-8")
    substitutions = {
        "{{TITLE}}": json.dumps(title.strip(), ensure_ascii=False),
        "{{DATE}}": draft_date,
        "{{SOURCE_PERIOD}}": source_period,
        "{{DESCRIPTION}}": json.dumps("TODO: 一次情報の内容と経営上の意味を記載", ensure_ascii=False),
        "{{CATEGORY}}": CATEGORIES[collection],
        "{{COLLECTION}}": collection,
    }
    for key, val in substitutions.items():
        article = article.replace(key, val)
    # The Markdown heading is not YAML and must not include quotes.
    article = article.replace("# " + json.dumps(title.strip(), ensure_ascii=False), "# " + title.strip(), 1)
    article = article.replace("review_status: Current", "review_status: Needs Review", 1)
    article = article.replace(f"reviewed: {draft_date}", "reviewed: ''", 1)
    if not article.startswith("---\n") or evidence.status_from_text(article) != "draft":
        raise ValueError("Unexpected article template; only draft mode is allowed")

    dossier = json.loads((root / "templates" / "evidence-review-template.json").read_text(encoding="utf-8"))
    dossier["article_path"] = f"docs/{collection}/{slug}.md"
    dossier["review"] = {
        "status": "pending",
        "reviewed_by": None,
        "reviewed_at": None,
        "notes": "出典・該当箇所を確認してから人間が承認する。AIは承認しない。",
    }
    checklist = (root / "templates" / "article-review-checklist.md").read_text(encoding="utf-8")
    checklist = checklist.replace("{{TITLE}}", title.strip()).replace("{{SLUG}}", slug)
    checklist = checklist.replace("{{COLLECTION}}", collection)
    data = {
        "article": article,
        "evidence": json.dumps(dossier, ensure_ascii=False, indent=2) + "\n",
        "review": checklist,
    }
    created: list[Path] = []
    try:
        for key, path in draft.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("x", encoding="utf-8") as stream:
                stream.write(data[key])
            created.append(path)
    except Exception:
        for path in reversed(created):
            path.unlink(missing_ok=True)
        raise
    return draft


def split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("Article missing front matter")
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        raise ValueError("Article front matter is not terminated")
    parsed = yaml.safe_load(parts[1])
    if not isinstance(parsed, dict):
        raise ValueError("Article front matter must be a YAML object")
    return parsed, parts[2]


def validate_bundle(root: Path, collection: str, slug: str, staged: bool = False) -> list[str]:
    paths = bundle_paths(root, collection, slug, staged=staged)
    failures: list[str] = []
    for role, path in paths.items():
        if not path.is_file():
            failures.append(f"{role}: missing {path.relative_to(root)}")
    if failures:
        return failures
    try:
        content = paths["article"].read_text(encoding="utf-8")
        meta, body = split_frontmatter(content)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [f"article: {exc}"]
    if meta.get("status") != "draft":
        failures.append("article.status must be draft; tool never publishes")
    if meta.get("review_status") != "Needs Review":
        failures.append("article.review_status must be Needs Review until human review")
    if meta.get("collections") is None or collection not in meta["collections"]:
        failures.append("article.collections must include the selected collection")
    if meta.get("category") != CATEGORIES[collection]:
        failures.append("article.category does not match the selected collection")
    if not meta.get("topics") or len(meta["topics"]) > 3:
        failures.append("article.topics must contain 1-3 real taxonomy topics")
    if not meta.get("description") or "TODO" in str(meta["description"]):
        failures.append("article.description must be complete")
    for heading in REQUIRED_HEADINGS:
        if heading not in body:
            failures.append(f"article missing section: {heading}")
    for marker in PLACEHOLDERS:
        if marker in content:
            failures.append(f"article still contains template text: {marker}")

    try:
        dossier = json.loads(paths["evidence"].read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return failures + [f"evidence: invalid JSON: {exc}"]
    if not isinstance(dossier, dict):
        return failures + ["evidence must be an object"]
    expected = f"docs/{collection}/{slug}.md"
    if dossier.get("article_path") != expected:
        failures.append(f"evidence.article_path must be {expected}")
    review = dossier.get("review") or {}
    if not isinstance(review, dict) or review.get("status") != "pending":
        failures.append("evidence.review.status must remain pending during staging")
    elif review.get("reviewed_by") or review.get("reviewed_at"):
        failures.append("Do not pre-fill human reviewer/date in a pending review")
    _, evidence_errors = evidence.validate_dossier(dossier, paths["evidence"].relative_to(root).as_posix())
    failures.extend(evidence_errors)
    for index, claim in enumerate(dossier.get("claims", []), 1):
        if isinstance(claim, dict) and claim.get("section") not in body:
            failures.append(f"claims[{index}] section is absent from draft article")
    return failures


def stage_bundle(root: Path, collection: str, slug: str) -> dict[str, Path]:
    errors = validate_bundle(root, collection, slug, staged=False)
    if errors:
        raise ValueError("Cannot stage incomplete bundle:\n- " + "\n- ".join(errors))
    source = bundle_paths(root, collection, slug)
    target = bundle_paths(root, collection, slug, staged=True)
    if any(p.exists() for p in target.values()):
        raise FileExistsError("Target article/evidence/review exists; refusing to overwrite")
    moved: list[tuple[Path, Path]] = []
    try:
        for kind in ("article", "evidence", "review"):
            dst, src = target[kind], source[kind]
            dst.parent.mkdir(parents=True, exist_ok=True)
            src.rename(dst)
            moved.append((src, dst))
    except Exception:
        for src, dst in reversed(moved):
            dst.rename(src)
        raise
    return target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    for action in ("init", "check", "stage"):
        sub = commands.add_parser(action)
        sub.add_argument("--collection", required=True, choices=sorted(CATEGORIES))
        sub.add_argument("--slug", required=True)
        if action == "init":
            sub.add_argument("--title", required=True)
            sub.add_argument("--draft-date", required=True)
            sub.add_argument("--source-period", required=True)
        if action == "check":
            sub.add_argument("--staged", action="store_true", help="Check docs/ and review/evidence/ instead of drafts/")
    args = parser.parse_args(argv)
    try:
        if args.action == "init":
            files = init_bundle(ROOT, args.collection, args.slug, args.title, args.draft_date, args.source_period)
        elif args.action == "check":
            errors = validate_bundle(ROOT, args.collection, args.slug, staged=args.staged)
            if errors:
                print("Bundle incomplete:", *("- " + e for e in errors), sep="\n")
                return 1
            print("Article Draft + Evidence Review bundle structurally complete (NOT human-approved).")
            return 0
        else:
            files = stage_bundle(ROOT, args.collection, args.slug)
        print(f"{args.action} complete (no PR, no approval, no publication):")
        for key, path in files.items():
            print(f"  {key}: {path.relative_to(ROOT)}")
        return 0
    except (ValueError, FileExistsError, OSError, json.JSONDecodeError) as exc:
        print(f"Article workflow error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

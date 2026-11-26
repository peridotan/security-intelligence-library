#!/usr/bin/env python3
"""Read-only review packet for explicitly selected draft articles."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import article_workflow as workflow
import check_evidence_review as evidence

ROOT = Path(__file__).resolve().parents[1]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def cell(value: object) -> str:
    # Keep untrusted Markdown as plain text inside a table.
    import html
    return html.escape(str(value or ""), quote=False).replace("|", "&#124;").replace("\n", " ").replace("\r", " ").replace("`", "&#96;")


def read_safe(root: Path, path: Path) -> bytes:
    if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"unsafe input: {path}")
    return path.read_bytes()


def build_report(root: Path, articles: list[str]) -> tuple[str, int]:
    if not articles:
        raise ValueError("select at least one article")
    lines = ["# Publication review packet (NOT human approval)", "",
             "Source assertions, Library assessments and recorded verification are distinct.",
             "Hashes identify the reviewed inputs; a changed input requires re-review.", ""]
    targets: set[str] = set()
    total = unresolved = 0
    for name in articles:
        p = Path(name)
        if p.is_absolute() or len(p.parts) != 3 or p.parts[0] != "drafts" or p.suffix != ".md":
            raise ValueError(f"expected drafts/<collection>/<slug>.md: {name}")
        col, slug = p.parts[1], p.stem
        workflow.validate_key(col, slug)
        # A literal -update suffix denotes an existing-article update.
        update = slug.endswith("-update")
        target_slug = slug[:-7] if update else slug
        workflow.validate_key(col, target_slug)
        target = f"docs/{col}/{target_slug}.md"
        if target in targets:
            raise ValueError(f"duplicate publication target: {target}")
        targets.add(target)
        ep = root / "drafts" / "evidence" / f"{slug}.json"
        article_bytes = read_safe(root, root / p)
        evidence_bytes = read_safe(root, ep)
        review_bytes = read_safe(root, root / "drafts" / "reviews" / f"{slug}.md")
        original_evidence_path = root / "review" / "evidence" / f"{target_slug}.json"
        original_evidence = read_safe(root, original_evidence_path) if original_evidence_path.exists() else None
        if not update and original_evidence is not None:
            raise ValueError(f"new evidence target exists: {original_evidence_path}")
        meta, body = workflow.split_frontmatter(article_bytes.decode("utf-8"))
        if meta.get("status") != "draft" or meta.get("review_status") != "Needs Review":
            raise ValueError(f"expected pending draft: {name}")
        dossier = json.loads(evidence_bytes)
        dest, errors = evidence.validate_dossier(dossier, ep.relative_to(root).as_posix(), check_article=False)
        if errors or dest != target:
            raise ValueError(f"invalid dossier {name}: " + "; ".join(errors or ["target mismatch"]))
        review = dossier["review"]
        if review.get("status") != "pending" or review.get("reviewed_by") or review.get("reviewed_at"):
            raise ValueError(f"expected unapproved evidence: {name}")
        if update:
            original = read_safe(root, root / target)
            original_meta, _ = workflow.split_frontmatter(original.decode("utf-8"))
            if original_meta.get("status") != "published" or meta.get("date") != original_meta.get("date"):
                raise ValueError(f"update must preserve original publication date: {name}")
        elif (root / target).exists():
            raise ValueError(f"new article target exists: {target}")
        headings = set(body.splitlines())
        claims = dossier["claims"]
        if any(c["section"] not in headings for c in claims):
            raise ValueError(f"claim section absent from draft: {name}")
        missing = sum(c["verification"] in {"needs_review", "unsupported"} for c in claims)
        total += len(claims)
        unresolved += missing
        lines += [f"## {cell(meta.get('title') or slug)}", "",
                  f"- Target: `{target}` ({'update' if update else 'new'})",
                  f"- Article SHA-256: `{digest(article_bytes)}`",
                  f"- Evidence SHA-256: `{digest(evidence_bytes)}`",
                  f"- Editorial review SHA-256: `{digest(review_bytes)}`",
                  f"- Unresolved claims: {missing}", ""]
        if update:
            lines += [f"- Current original SHA-256: `{digest(original)}`",
                      f"- Current original Evidence SHA-256: `{digest(original_evidence) if original_evidence is not None else 'null'}`", ""]
        else:
            lines += ["- Current original SHA-256: `null`", "- Current original Evidence SHA-256: `null`", ""]
        lines += ["| ID | Claim | Section | Classification / importance | Recorded verification | Source / locator / rationale |",
                  "| --- | --- | --- | --- | --- | --- |"]
        for c in claims:
            source = c.get("source") or {}
            detail = " ; ".join(str(v) for v in (source.get("url"), source.get("locator"),
                     source.get("published_at"), source.get("accessed_at"), c.get("rationale"), c.get("review_note")) if v)
            values = (c["id"], c["statement"], c["section"], c["classification"] + " / " + c["importance"], c["verification"], detail)
            lines.append("| " + " | ".join(cell(v) for v in values) + " |")
        lines.append("")
    lines += [f"Articles: {len(targets)}; claims: {total}; unresolved: {unresolved}.",
              "Human review and explicit publication approval are still required.", ""]
    return "\n".join(lines), unresolved


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article", action="append", required=True)
    args = parser.parse_args()
    try:
        report, unresolved = build_report(ROOT, args.article)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f"Review packet error: {exc}", file=sys.stderr)
        return 1
    print(report)
    return 2 if unresolved else 0


if __name__ == "__main__":
    sys.exit(main())

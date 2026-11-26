#!/usr/bin/env python3
"""Prepare an isolated publication bundle from explicit human approval records.

No approval is inferred. This command never changes the source tree, commits,
pushes, merges, or deploys. A manifest is an assertion by the editor, not a
cryptographic proof of reviewer identity.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

import article_workflow as workflow
import batch_review
import check_evidence_review as evidence

ROOT = Path(__file__).resolve().parents[1]


def replace_meta(text: str, changes: dict[str, str]) -> str:
    _, fm, body = text.split("---\n", 2)
    for key, value in changes.items():
        fm, count = re.subn(r"(?m)^" + re.escape(key) + r":[^\n]*$", key + ": " + value, fm)
        if count != 1:
            raise ValueError(f"expected one scalar metadata field: {key}")
    return "---\n" + fm + "---\n" + body


def verify_base(root: Path, base: str) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", base):
        raise ValueError("base_commit must be a full Git SHA")
    for ref in ("HEAD", "origin/main"):
        actual = subprocess.check_output(["git", "rev-parse", ref], cwd=root, text=True).strip()
        if actual != base:
            raise ValueError(f"{ref} differs from approved base; synchronize and recheck")
    branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=root, text=True).strip()
    if not branch or branch == "main":
        raise ValueError("use a publication work branch, not main or detached HEAD")
    dirty = subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=all", "--", "docs", "review"], cwd=root, text=True)
    if dirty.strip():
        raise ValueError("docs/review must match the base commit before preparation")


def prepare(root: Path, manifest: dict, output: Path) -> list[str]:
    """Preflight all records before writing an isolated, new output directory."""
    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
        raise ValueError("manifest schema_version must be 1")
    base = manifest.get("base_commit", "")
    if not isinstance(base, str) or not re.fullmatch(r"[0-9a-f]{40}", base):
        raise ValueError("invalid base_commit")
    records = manifest.get("articles")
    if not isinstance(records, list) or not records or any(not isinstance(r, dict) for r in records):
        raise ValueError("explicit article approval records are required")
    if output.exists() or output.is_symlink() or output.resolve().is_relative_to(root.resolve()):
        raise ValueError("output must be a new directory outside the repository")
    names = [r["draft"] for r in records]
    _, unresolved = batch_review.build_report(root, names)
    if unresolved:
        raise ValueError("unresolved claims: refusing entire batch")
    files: dict[str, bytes] = {}
    audit = []
    for record in records:
        name = record["draft"]
        reviewer = record.get("reviewed_by")
        day = record.get("reviewed_at")
        published = record.get("publication_date")
        if record.get("decision") != "approved" or not isinstance(reviewer, str) or not reviewer.strip():
            raise ValueError(f"explicit human approval required: {name}")
        if not evidence.valid_date(day) or not evidence.valid_date(published) or published < day:
            raise ValueError(f"invalid approval/publication dates: {name}")
        p = Path(name)
        slug = p.stem
        update = slug.endswith("-update")
        target_slug = slug[:-7] if update else slug
        target = f"docs/{p.parts[1]}/{target_slug}.md"
        ep = root / "drafts" / "evidence" / f"{slug}.json"
        rp = root / "drafts" / "reviews" / f"{slug}.md"
        a = batch_review.read_safe(root, root / p)
        e = batch_review.read_safe(root, ep)
        review_text = batch_review.read_safe(root, rp)
        for key, data in (("article_sha256", a), ("evidence_sha256", e), ("review_sha256", review_text)):
            if record.get(key) != batch_review.digest(data):
                raise ValueError(f"approved hash mismatch: {name} / {key}")
        old = batch_review.read_safe(root, root / target) if update else None
        if record.get("original_sha256") != (batch_review.digest(old) if old is not None else None):
            raise ValueError(f"original article changed: {name}")
        evidence_path = f"review/evidence/{target_slug}.json"
        old_evidence_path = root / evidence_path
        old_evidence = batch_review.read_safe(root, old_evidence_path) if old_evidence_path.exists() else None
        if not update and old_evidence is not None:
            raise ValueError(f"new evidence target exists: {evidence_path}")
        if record.get("original_evidence_sha256") != (batch_review.digest(old_evidence) if old_evidence is not None else None):
            raise ValueError(f"original evidence changed: {name}")
        pilot = f"review/pilots/{slug}.md"
        if (root / pilot).exists():
            raise ValueError(f"review target already exists: {pilot}")
        article = a.decode("utf-8")
        meta, _ = workflow.split_frontmatter(article)
        if any(marker in article for marker in workflow.PLACEHOLDERS):
            raise ValueError(f"template placeholders remain: {name}")
        # Existing articles may have legacy composite category labels.
        # Preserve their category and collection membership rather than forcing
        # the new-article taxonomy onto an approved update.
        collections = meta.get("collections")
        if not isinstance(collections, list) or p.parts[1] not in collections:
            raise ValueError(f"collection mismatch: {name}")
        if update:
            original_meta, _ = workflow.split_frontmatter(old.decode("utf-8"))
            if meta.get("category") != original_meta.get("category") or collections != original_meta.get("collections"):
                raise ValueError(f"existing article category/collections changed: {name}")
        elif meta.get("category") != workflow.CATEGORIES[p.parts[1]]:
            raise ValueError(f"collection mismatch: {name}")
        changes = {"status": "published", "review_status": "Current", "reviewed": day, "updated": published}
        if not update:
            changes["date"] = published
        article_out = replace_meta(article, changes)
        dossier = json.loads(e)
        previous_notes = dossier["review"].get("notes")
        dossier["review"] = {"status": "approved", "reviewed_by": reviewer, "reviewed_at": day,
                             "notes": "Human approval recorded from the explicit batch manifest. See publication audit.",
                             "pre_approval_notes": previous_notes}
        _, errors = evidence.validate_dossier(dossier, evidence_path, check_article=False)
        if errors:
            raise ValueError("; ".join(errors))
        for path, data in ((target, article_out.encode("utf-8")),
                           (evidence_path, (json.dumps(dossier, ensure_ascii=False, indent=2) + "\n").encode("utf-8")),
                           (pilot, review_text)):
            if path in files:
                raise ValueError(f"duplicate output: {path}")
            files[path] = data
        audit.append({**record, "target": target, "prepared_article_sha256": batch_review.digest(files[target]),
                      "prepared_evidence_sha256": batch_review.digest(files[evidence_path])})
    audit_path = "review/publication-batches/" + batch_review.digest(json.dumps(manifest, sort_keys=True, ensure_ascii=False).encode()) + ".json"
    if (root / audit_path).exists():
        raise ValueError("batch audit already exists")
    files[audit_path] = (json.dumps({"schema_version": 1, "base_commit": base, "articles": audit}, ensure_ascii=False, indent=2) + "\n").encode()
    output.parent.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix=".publication-", dir=output.parent))
    try:
        for path, data in files.items():
            dest = tmp / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
        # Refuse any existing output, even an empty directory.
        output.mkdir()
        try:
            for item in tmp.iterdir():
                item.rename(output / item.name)
        except Exception:
            shutil.rmtree(output)
            raise
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
        verify_base(ROOT, manifest["base_commit"])
        files = prepare(ROOT, manifest, args.output)
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print(f"Preparation refused: {exc}", file=sys.stderr)
        return 1
    print("Prepared isolated bundle; no repository changes or publication:")
    print("\n".join(files))
    return 0


if __name__ == "__main__":
    sys.exit(main())

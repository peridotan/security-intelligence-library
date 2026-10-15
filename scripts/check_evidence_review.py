#!/usr/bin/env python3
"""Validate evidence dossiers and require one for newly published articles.

This is a *structural* gate. It cannot independently prove a source statement
is true or that a person really reviewed it. Work drafts remain pending until
a human confirms their evidence and explicitly marks the dossier approved.
"""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DOSSIERS = ROOT / "review" / "evidence"
COLLECTIONS = {
    "cybersecurity", "identity-security", "ai-security",
    "regulation", "risk-management",
}
CLASSES = {"source_fact", "source_claim", "library_assessment"}
IMPORTANCES = {"material", "supporting"}
VERIFY_SOURCE = {"verified", "needs_review", "unsupported"}
REVIEW_STATES = {"pending", "approved", "changes_requested"}


def valid_date(value: object) -> bool:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def valid_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        result = urlparse(value)
    except ValueError:
        return False
    return (
        result.scheme == "https"
        and bool(result.hostname)
        and result.hostname not in {"example.com", "www.example.com", "example.org", "example.net"}
        and not result.hostname.endswith((".invalid", ".test", ".example", ".localhost"))
        and not result.username
        and not result.password
    )


def article_path(value: object) -> str | None:
    if not isinstance(value, str) or "\\" in value:
        return None
    part = PurePosixPath(value)
    if part.is_absolute() or any(p in (".", "..") for p in value.split("/")):
        return None
    chunks = part.parts
    if len(chunks) < 3 or chunks[0] != "docs" or chunks[1] not in COLLECTIONS:
        return None
    if part.suffix != ".md" or part.name == "index.md":
        return None
    return str(part)


def status_from_text(body: str) -> str | None:
    if not body.startswith("---\n"):
        return None
    sections = body.split("---\n", 2)
    if len(sections) < 3:
        return None
    # Only the uncomplicated status key needs inspection; full YAML parsing
    # remains the responsibility of the existing content quality checker.
    match = re.search(r'''(?m)^status:\s*['"]?(published|draft)['"]?\s*$''', sections[1])
    return match.group(1) if match else None


def read_status(path: Path) -> str | None:
    if not path.is_file():
        return None
    return status_from_text(path.read_text(encoding="utf-8"))


def check_source(data: object, name: str, errors: list[str]) -> None:
    if not isinstance(data, dict):
        errors.append(f"{name}: source must be an object")
        return
    if not valid_url(data.get("url")):
        errors.append(f"{name}: source.url must be a real HTTPS URL (not example.com)")
    if len(str(data.get("locator") or "").strip()) < 3:
        errors.append(f"{name}: source.locator must identify the passage/table/section")
    if not valid_date(data.get("accessed_at")):
        errors.append(f"{name}: source.accessed_at must be YYYY-MM-DD")
    if data.get("published_at") is not None and not valid_date(data["published_at"]):
        errors.append(f"{name}: source.published_at must be YYYY-MM-DD or omitted when unknown")


def validate_dossier(payload: object, filename: str) -> tuple[str | None, list[str]]:
    problems: list[str] = []
    if not isinstance(payload, dict):
        return None, [f"{filename}: dossier must be a JSON object"]
    if type(payload.get("schema_version")) is not int or payload["schema_version"] != 1:
        problems.append(f"{filename}: schema_version must equal 1")

    target = article_path(payload.get("article_path"))
    if target is None:
        problems.append(f"{filename}: article_path must be a safe docs/<collection>/*.md path")

    review = payload.get("review")
    if not isinstance(review, dict):
        problems.append(f"{filename}: review must be an object")
        review = {}
    state = review.get("status")
    if state not in REVIEW_STATES:
        problems.append(f"{filename}: review.status must be pending, approved or changes_requested")
    if state == "approved":
        if not str(review.get("reviewed_by") or "").strip():
            problems.append(f"{filename}: approved review requires reviewed_by (human reviewer)")
        if not valid_date(review.get("reviewed_at")):
            problems.append(f"{filename}: approved review requires reviewed_at YYYY-MM-DD")
    elif review.get("reviewed_at") and not valid_date(review["reviewed_at"]):
        problems.append(f"{filename}: review.reviewed_at must be YYYY-MM-DD if supplied")

    claims = payload.get("claims")
    if not isinstance(claims, list) or not claims:
        problems.append(f"{filename}: claims must be a non-empty list")
        claims = []

    used: set[str] = set()
    has_material = False
    for idx, claim in enumerate(claims, 1):
        label = f"{filename}: claims[{idx}]"
        if not isinstance(claim, dict):
            problems.append(f"{label}: must be an object")
            continue
        cid = claim.get("id")
        if not isinstance(cid, str) or not re.fullmatch(r"C\d{2,4}", cid):
            problems.append(f"{label}: id must match C01/C001 etc.")
        elif cid in used:
            problems.append(f"{label}: duplicate claim id {cid}")
        else:
            used.add(cid)
        if len(str(claim.get("statement") or "").strip()) < 10:
            problems.append(f"{label}: statement must summarize a material assertion")
        section = claim.get("section")
        if not isinstance(section, str) or not section.startswith("## "):
            problems.append(f"{label}: section must be a '## ' article heading")
        classification = claim.get("classification")
        if classification not in CLASSES:
            problems.append(f"{label}: invalid classification")
        importance = claim.get("importance")
        if importance not in IMPORTANCES:
            problems.append(f"{label}: importance must be material or supporting")
        if importance == "material":
            has_material = True
        verification = claim.get("verification")
        if classification in ("source_fact", "source_claim"):
            check_source(claim.get("source"), label, problems)
            if verification not in VERIFY_SOURCE:
                problems.append(f"{label}: source-backed claim requires verified, needs_review or unsupported")
            if state == "approved" and verification != "verified":
                problems.append(f"{label}: approved dossier still contains unresolved source-backed claim")
        elif classification == "library_assessment":
            if len(str(claim.get("rationale") or "").strip()) < 10:
                problems.append(f"{label}: library_assessment requires rationale (not a sourced fact)")
            if verification != "not_applicable":
                problems.append(f"{label}: library_assessment verification must be not_applicable")
            if "source" in claim and claim["source"] is not None:
                check_source(claim["source"], label, problems)
    if not has_material:
        problems.append(f"{filename}: at least one material claim must be recorded")

    if target:
        article = ROOT / target
        status = read_status(article)
        if status == "published" and state != "approved":
            problems.append(f"{filename}: published article requires an approved human review")
        if state == "approved" and status is None:
            problems.append(f"{filename}: cannot approve a dossier for a missing/non-article path")
        if status == "published":
            text = article.read_text(encoding="utf-8")
            for idx, claim in enumerate(claims, 1):
                if not isinstance(claim, dict):
                    continue
                section = claim.get("section")
                if isinstance(section, str) and section not in text:
                    problems.append(f"{filename}: claims[{idx}] section is absent from published article")
    return target, problems


def new_published_articles(base_ref: str) -> set[str]:
    """Detect added articles AND existing drafts transitioning to published.

    Compare against the PR merge base so older published articles edited in a
    PR do not require retrospective dossiers. Renamed-in article paths are
    treated as new until supported by a dossier.
    """
    base = subprocess.run(
        ["git", "merge-base", base_ref, "HEAD"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    if base.returncode or not base.stdout.strip():
        raise RuntimeError(f"could not find PR merge-base: {base.stderr.strip()}")
    baseline = base.stdout.strip()
    changes = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=AMR",
         f"{baseline}...HEAD", "--", "docs"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    if changes.returncode:
        raise RuntimeError(f"could not inspect changed articles: {changes.stderr.strip()}")
    result: set[str] = set()
    for candidate in changes.stdout.splitlines():
        target = article_path(candidate)
        if not target or read_status(ROOT / target) != "published":
            continue
        previous = subprocess.run(
            ["git", "show", f"{baseline}:{target}"],
            cwd=ROOT, text=True, capture_output=True, check=False,
        )
        previous_status = status_from_text(previous.stdout) if previous.returncode == 0 else None
        if previous_status != "published":
            result.add(target)
    return result


def validate_all(root: Path = DOSSIERS, base_ref: str | None = None) -> tuple[int, list[str]]:
    errors: list[str] = []
    article_to_file: dict[str, str] = {}
    count = 0
    for filename in sorted(root.glob("*.json")):
        count += 1
        try:
            data = json.loads(filename.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            display = filename.relative_to(ROOT) if filename.is_relative_to(ROOT) else filename
            errors.append(f"{display}: invalid JSON: {exc}")
            continue
        display = filename.relative_to(ROOT) if filename.is_relative_to(ROOT) else filename
        target, problems = validate_dossier(data, display.as_posix())
        errors.extend(problems)
        if target:
            if target in article_to_file:
                errors.append(f"{target}: duplicate evidence dossiers: {article_to_file[target]} and {filename.name}")
            article_to_file[target] = filename.name

    if base_ref is not None:
        try:
            added = new_published_articles(base_ref)
        except RuntimeError as exc:
            errors.append(str(exc))
            added = set()
        for target in sorted(added):
            if target not in article_to_file:
                errors.append(f"{target}: newly published article requires a review/evidence/*.json dossier")
    return count, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-ref", help="Git base ref; require evidence for newly published articles")
    args = parser.parse_args()
    count, problems = validate_all(base_ref=args.base_ref)
    if problems:
        print("Evidence Review checks FAILED:")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print(f"Evidence Review checks passed ({count} dossier(s) validated).")
    if args.base_ref:
        print("Newly published article coverage checked against:", args.base_ref)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import urlparse
from datetime import date, datetime
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TOPIC_CONFIG = ROOT / "config" / "topics.yml"
ATTACK_CONFIG = ROOT / "config" / "mitre_attack.yml"

REQ_META = [
    "title", "date", "updated", "reviewed", "review_status", "source_period",
    "description", "category", "collections", "topics", "tags", "audience",
    "management_impact", "impact_types", "urgency", "evidence", "status",
    "pptx", "media_rights"
]
REQ_SEC = [
    "## Executive Summary", "## なぜ今なのか", "## 経営インパクト",
    "## 日本企業への示唆", "## 推奨アクション", "## 参考情報"
]
URGENCY = {"Immediate", "Near-term", "Strategic"}
EVIDENCE = {"Confirmed", "Observed", "Mixed", "Assessment"}
REVIEW_STATUS = {"Current", "Needs Review", "Superseded", "Archived"}
MANAGEMENT_IMPACT = {"High", "Medium", "Low"}
COLLECTIONS = {
    "cybersecurity", "identity-security", "ai-security", "regulation", "risk-management"
}

_topic_data = yaml.safe_load(TOPIC_CONFIG.read_text(encoding="utf-8")) or {}
TOPICS = {
    str(topic["name"])
    for group in (_topic_data.get("groups") or [])
    for topic in (group.get("topics") or [])
}
_attack_data = yaml.safe_load(ATTACK_CONFIG.read_text(encoding="utf-8")) or {}
ATTACK_TECHNIQUES = _attack_data.get("techniques") or {}
ATTACK_BASIS = {"Source-labeled", "Analyst-mapped"}
errors = []

def split_fm(text):
    if not text.startswith("---\n"):
        return None, text
    parts = text.split("---\n", 2)
    return yaml.safe_load(parts[1]) or {}, parts[2]

def as_iso(v):
    if isinstance(v, (date, datetime)):
        return v.isoformat()
    return str(v)

def is_article(path, meta):
    return bool(
        meta and meta.get("status") == "published"
        and path.name != "index.md"
        and "sample" not in path.name
        and "about" not in path.parts
    )

for path in sorted(DOCS.rglob("*.md")):
    if "about" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    try:
        meta, body = split_fm(text)
    except yaml.YAMLError as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid YAML: {exc}")
        continue
    if not is_article(path, meta):
        continue

    rel = path.relative_to(ROOT)
    for key in REQ_META:
        if key not in meta:
            errors.append(f"{rel}: missing `{key}`")

    if meta.get("urgency") not in URGENCY:
        errors.append(f"{rel}: invalid urgency `{meta.get('urgency')}`")
    if meta.get("evidence") not in EVIDENCE:
        errors.append(f"{rel}: invalid evidence `{meta.get('evidence')}`")
    if meta.get("review_status") not in REVIEW_STATUS:
        errors.append(f"{rel}: invalid review_status `{meta.get('review_status')}`")

    if meta.get("review_status") == "Superseded":
        successor = str(meta.get("superseded_by", "") or "").strip()
        if not successor:
            errors.append(f"{rel}: Superseded article requires `superseded_by`")
        elif successor.startswith(("http://", "https://")):
            if not urlparse(successor).netloc:
                errors.append(f"{rel}: malformed superseded_by URL `{successor}`")
        else:
            successor_path = (path.parent / successor.split("#", 1)[0]).resolve()
            if successor_path.suffix == "":
                successor_path = successor_path.with_suffix(".md")
            if not successor_path.exists():
                errors.append(f"{rel}: broken superseded_by `{successor}`")

    if meta.get("management_impact") not in MANAGEMENT_IMPACT:
        errors.append(f"{rel}: invalid management_impact `{meta.get('management_impact')}`")

    if not re.fullmatch(r"\d{4}-\d{2}", str(meta.get("source_period", ""))):
        errors.append(f"{rel}: source_period must be YYYY-MM")

    for field in ("date", "updated", "reviewed"):
        try:
            date.fromisoformat(as_iso(meta.get(field)))
        except Exception:
            errors.append(f"{rel}: `{field}` must be YYYY-MM-DD")

    collections = meta.get("collections")
    if not isinstance(collections, list) or not collections:
        errors.append(f"{rel}: collections must be a non-empty list")
    else:
        bad = [c for c in collections if c not in COLLECTIONS]
        if bad:
            errors.append(f"{rel}: unsupported collections: {', '.join(map(str, bad))}")

    topics = meta.get("topics")
    if not isinstance(topics, list) or not topics:
        errors.append(f"{rel}: topics must be a non-empty list")
    else:
        unknown_topics = [t for t in topics if t not in TOPICS]
        if unknown_topics:
            errors.append(
                f"{rel}: unsupported topics: {', '.join(map(str, unknown_topics))}"
            )
        if len(topics) > 3:
            errors.append(f"{rel}: use at most 3 curated topics")

    tags = meta.get("tags")
    if not isinstance(tags, list) or not tags:
        errors.append(f"{rel}: tags must be a non-empty list")

    mitre = meta.get("mitre_attack")
    if mitre is not None:
        if not isinstance(mitre, list) or not mitre:
            errors.append(f"{rel}: mitre_attack must be a non-empty list when present")
        else:
            if len(mitre) > 8:
                errors.append(f"{rel}: use at most 8 MITRE ATT&CK mappings")
            seen_attack_ids = set()
            for item in mitre:
                if not isinstance(item, dict):
                    errors.append(f"{rel}: each mitre_attack entry must be an object")
                    continue
                tid = str(item.get("id", "") or "").strip()
                basis = str(item.get("basis", "") or "").strip()
                note = str(item.get("note", "") or "").strip()
                if tid not in ATTACK_TECHNIQUES:
                    errors.append(f"{rel}: unsupported MITRE ATT&CK id `{tid}`")
                if tid in seen_attack_ids:
                    errors.append(f"{rel}: duplicate MITRE ATT&CK id `{tid}`")
                seen_attack_ids.add(tid)
                if basis not in ATTACK_BASIS:
                    errors.append(f"{rel}: invalid MITRE ATT&CK basis `{basis}`")
                if len(note) < 8:
                    errors.append(f"{rel}: MITRE ATT&CK mapping `{tid}` requires a context note")

    impact_types = meta.get("impact_types")
    if not isinstance(impact_types, list) or not impact_types:
        errors.append(f"{rel}: impact_types must be a non-empty list")

    for section in REQ_SEC:
        if section not in body:
            errors.append(f"{rel}: missing `{section}`")

    if '<div class="sil-article-meta">' not in body:
        errors.append(f"{rel}: metadata block missing")
    for label in ("Source Period", "Last Reviewed", "Review Status", "Topics", "Impact Areas"):
        if f"<span class=\"sil-meta-label\">{label}</span>" not in body:
            errors.append(f"{rel}: generated metadata missing `{label}`")

    if meta.get("review_status") == "Superseded":
        if '<div class="sil-superseded-banner"' not in body:
            errors.append(f"{rel}: Superseded article banner missing")
        if "Historical Snapshot" not in body:
            errors.append(f"{rel}: Superseded article banner label missing")

    if meta.get("mitre_attack"):
        if body.count("<!-- AUTO:MITRE:START -->") != 1:
            errors.append(f"{rel}: generated MITRE ATT&CK mapping block missing or duplicated")
        if "## MITRE ATT&CK® Mapping" not in body:
            errors.append(f"{rel}: MITRE ATT&CK mapping heading missing")
        if "© 2026 The MITRE Corporation." not in body:
            errors.append(f"{rel}: MITRE ATT&CK copyright notice missing")
    elif "<!-- AUTO:MITRE:START -->" in body:
        errors.append(f"{rel}: MITRE ATT&CK block exists without mitre_attack metadata")

    if not str(meta.get("pptx", "") or "").strip() and "## PowerPoint" in body:
        errors.append(f"{rel}: PowerPoint placeholder must be hidden")

    # Internal Markdown links.
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        raw = target.split("#", 1)[0]
        if not raw:
            continue
        tp = (path.parent / raw).resolve()
        if tp.suffix == "":
            tp = tp.with_suffix(".md")
        if not tp.exists():
            errors.append(f"{rel}: broken internal link `{target}`")

    # Source section must contain at least one syntactically valid URL.
    if "## 参考情報" in body:
        refs = body.split("## 参考情報", 1)[1]
        urls = re.findall(r"https?://[^\s)]+", refs)
        if not urls:
            errors.append(f"{rel}: no source URL")
        for url in urls:
            if not urlparse(url).netloc:
                errors.append(f"{rel}: malformed URL `{url}`")

    # Rights guardrails.
    has_media = bool(
        re.search(r"!\[[^\]]*\]\([^)]+\)", body)
        or re.search(r"<(?:img|video|audio|iframe|embed|object)\b", body, flags=re.I)
    )
    media_rights = str(meta.get("media_rights", "none")).lower()
    allowed_media = {"original", "licensed", "permission", "public-domain"}
    if has_media and media_rights not in allowed_media:
        errors.append(
            f"{rel}: embedded media requires `media_rights` "
            f"({', '.join(sorted(allowed_media))})"
        )

    has_quote = bool(
        re.search(r"(?m)^\s*>\s+\S", body)
        or re.search(r"<blockquote\b", body, flags=re.I)
    )
    if has_quote and meta.get("quotation_reviewed") is not True:
        errors.append(f"{rel}: direct quotation requires `quotation_reviewed: true`")
    if re.search(r"<script\b", body, flags=re.I):
        errors.append(f"{rel}: executable script is not allowed")

    for block in re.findall(r"```text\s*\n(.*?)\n```", body, flags=re.S):
        if "↓" in block or "→" in block or "▼" in block:
            errors.append(
                f"{rel}: flow-like text code block found; use `.sil-flow` markup instead"
            )


# Quarterly review pages are synthesis pages, not production articles.
quarterly_dir = DOCS / "quarterly"
if quarterly_dir.exists():
    for path in sorted(quarterly_dir.glob("20??-q?.md")):
        text = path.read_text(encoding="utf-8")
        try:
            meta, body = split_fm(text)
        except yaml.YAMLError as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid YAML: {exc}")
            continue
        rel = path.relative_to(ROOT)
        if not meta or meta.get("review_type") != "quarterly":
            errors.append(f"{rel}: quarterly review requires `review_type: quarterly`")
            continue
        if not re.fullmatch(r"\d{4}-Q[1-4]", str(meta.get("period", ""))):
            errors.append(f"{rel}: quarterly period must be YYYY-QN")
        months = meta.get("months")
        prelude_month = str(meta.get("prelude_month", "") or "").strip()
        if prelude_month:
            if not re.fullmatch(r"\d{4}-\d{2}", prelude_month):
                errors.append(f"{rel}: invalid prelude_month `{prelude_month}`")
            elif not (DOCS / "monthly" / f"{prelude_month}.md").exists():
                errors.append(f"{rel}: missing prelude monthly source `{prelude_month}`")
            if "sil-prequarter" not in body:
                errors.append(f"{rel}: prelude_month is set but Pre-quarter Signals block is missing")
        if not isinstance(months, list) or len(months) != 3:
            errors.append(f"{rel}: quarterly review requires exactly 3 months")
        else:
            for month in months:
                if not re.fullmatch(r"\d{4}-\d{2}", str(month)):
                    errors.append(f"{rel}: invalid quarterly month `{month}`")
                monthly_path = DOCS / "monthly" / f"{month}.md"
                if not monthly_path.exists():
                    errors.append(f"{rel}: missing monthly source `{month}`")
        for key in ("title", "description", "summary", "reviewed"):
            if not meta.get(key):
                errors.append(f"{rel}: missing `{key}`")
        try:
            date.fromisoformat(as_iso(meta.get("reviewed")))
        except Exception:
            errors.append(f"{rel}: `reviewed` must be YYYY-MM-DD")
        quarter = str(meta.get("period", "")).split("-", 1)[-1]
        required_quarter_sections = (
            "## Executive Summary",
            f"## {quarter}の7つの構造変化",
            "## Management Priorities",
            "## Evidence Basis",
        )
        for section in required_quarter_sections:
            if section not in body:
                errors.append(f"{rel}: missing `{section}`")

        # Internal links for quarterly review pages.
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            raw = target.split("#", 1)[0]
            if not raw:
                continue
            tp = (path.parent / raw).resolve()
            if tp.suffix == "":
                tp = tp.with_suffix(".md")
            if not tp.exists():
                errors.append(f"{rel}: broken internal link `{target}`")

# Generated-source blocks must exist and must not contain the v0.6.0 nesting bug.
generated_pages = [
    DOCS / "index.md",
    DOCS / "monthly/index.md",
    DOCS / "quarterly/index.md",
    DOCS / "topics/index.md",
    DOCS / "tags/index.md",
    DOCS / "cybersecurity/index.md",
    DOCS / "identity-security/index.md",
    DOCS / "ai-security/index.md",
    DOCS / "regulation/index.md",
    DOCS / "risk-management/index.md",
]
for page in generated_pages:
    text = page.read_text(encoding="utf-8")
    if '<div class="sil-card-meta">' in text:
        # A card may never begin before the current metadata div is closed.
        if re.search(r'<div class="sil-card-meta">(?:(?!</div>).)*<article\b', text, re.S):
            errors.append(f"{page.relative_to(ROOT)}: nested article inside sil-card-meta")
    if text.count('<article class="sil-card">') != text.count("</article>"):
        errors.append(f"{page.relative_to(ROOT)}: unbalanced generated article cards")

# Repository governance / rights consistency.
for required_file in [
    "LICENSE", "LICENSE-CODE.txt", "COPYRIGHT.md", "THIRD_PARTY_NOTICES.md",
    "RIGHTS_REVIEW.md", "CONTRIBUTING.md", ".github/SECURITY.md",
    "config/topics.yml", "config/mitre_attack.yml"
]:
    if not (ROOT / required_file).exists():
        errors.append(f"repository: missing `{required_file}`")

home_text = (DOCS / "index.md").read_text(encoding="utf-8")
if "<!-- AUTO:HOME_QUARTERLY:START -->" not in home_text:
    errors.append("docs/index.md: quarterly Home block missing")
quarterly_index_text = (DOCS / "quarterly/index.md").read_text(encoding="utf-8")
if "<!-- AUTO:QUARTERLY_INDEX:START -->" not in quarterly_index_text:
    errors.append("docs/quarterly/index.md: quarterly index block missing")

config_text = (ROOT / "zensical.toml").read_text(encoding="utf-8")
if '{ "Quarterly Review" = "quarterly/index.md" },' not in config_text:
    errors.append("repository: Quarterly Review navigation entry missing")
if "&copy; 2026 peridotan. All rights reserved." not in config_text:
    errors.append("repository: footer copyright notice is not standardized")
if 'font = false' not in config_text:
    errors.append("repository: Google Fonts autoload must remain disabled")
if '"content.action.edit"' in config_text:
    errors.append("repository: editorial edit action should remain disabled")

about_text = (DOCS / "about/index.md").read_text(encoding="utf-8")
for section in [
    "## AI利用方針", "## 引用・画像・商標の扱い",
    "## Privacy / 外部通信", "## Copyright and Licensing"
]:
    if section not in about_text:
        errors.append(f"docs/about/index.md: missing `{section}`")
if "生成AIを利用しています" not in about_text:
    errors.append("docs/about/index.md: AI usage must be stated affirmatively")

requirements = (ROOT / "requirements.txt").read_text(encoding="utf-8").splitlines()
for req in [r for r in requirements if r.strip() and not r.lstrip().startswith("#")]:
    if "==" not in req:
        errors.append(f"requirements.txt: dependency must be pinned exactly: `{req}`")

if errors:
    print("Content checks failed:")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("Content checks passed.")

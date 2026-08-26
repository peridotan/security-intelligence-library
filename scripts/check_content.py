#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import urlparse
import re, sys, yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REQ_META = ["title","date","updated","description","category","tags","audience",
            "management_impact","urgency","evidence","status","pptx"]
REQ_SEC = ["## Executive Summary","## なぜ今なのか","## 経営インパクト",
           "## 日本企業への示唆","## 推奨アクション","## 参考情報"]
URGENCY = {"Immediate","Near-term","Strategic"}
EVIDENCE = {"Confirmed","Observed","Mixed","Assessment"}
errors=[]

def split_fm(text):
    if not text.startswith("---\n"): return None,text
    p=text.split("---\n",2)
    return yaml.safe_load(p[1]) or {},p[2]

for path in sorted(DOCS.rglob("*.md")):
    if "about" in path.parts: continue
    text=path.read_text(encoding="utf-8")
    try: meta,body=split_fm(text)
    except yaml.YAMLError: continue
    if not (meta and meta.get("status")=="published" and path.name!="index.md" and "sample" not in path.name):
        continue
    rel=path.relative_to(ROOT)
    for k in REQ_META:
        if k not in meta: errors.append(f"{rel}: missing `{k}`")
    if meta.get("urgency") not in URGENCY: errors.append(f"{rel}: invalid urgency")
    if meta.get("evidence") not in EVIDENCE: errors.append(f"{rel}: invalid evidence")
    for s in REQ_SEC:
        if s not in body: errors.append(f"{rel}: missing `{s}`")
    if '<div class="sil-article-meta">' not in body: errors.append(f"{rel}: metadata block missing")
    if not str(meta.get("pptx","") or "").strip() and "## PowerPoint" in body:
        errors.append(f"{rel}: PowerPoint placeholder must be hidden")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
        if target.startswith(("http://","https://","mailto:","#")): continue
        raw=target.split("#",1)[0]
        if not raw: continue
        tp=(path.parent/raw).resolve()
        if tp.suffix=="": tp=tp.with_suffix(".md")
        if not tp.exists(): errors.append(f"{rel}: broken internal link `{target}`")
    if "## 参考情報" in body:
        refs=body.split("## 参考情報",1)[1]
        urls=re.findall(r"https?://[^\s)]+",refs)
        if not urls: errors.append(f"{rel}: no source URL")
        for u in urls:
            if not urlparse(u).netloc: errors.append(f"{rel}: malformed URL `{u}`")


# Repository governance / rights consistency checks.
for required_file in [
    "LICENSE", "LICENSE-CODE.txt", "COPYRIGHT.md", "THIRD_PARTY_NOTICES.md",
    "RIGHTS_REVIEW.md", "CONTRIBUTING.md", ".github/SECURITY.md"
]:
    if not (ROOT / required_file).exists():
        errors.append(f"repository: missing `{required_file}`")

config_text = (ROOT / "zensical.toml").read_text(encoding="utf-8")
if "&copy; 2026 peridotan. All rights reserved." not in config_text:
    errors.append("repository: footer copyright notice is not standardized")
if 'font = false' not in config_text:
    errors.append("repository: Google Fonts autoload must remain disabled for privacy")
if '"content.action.edit"' in config_text:
    errors.append("repository: editorial edit action should remain disabled")

about_text = (DOCS / "about/index.md").read_text(encoding="utf-8")
for section in [
    "## AI利用方針",
    "## 引用・画像・商標の扱い",
    "## Privacy / 外部通信",
    "## Copyright and Licensing",
]:
    if section not in about_text:
        errors.append(f"docs/about/index.md: missing `{section}`")
if "生成AIを利用しています" not in about_text:
    errors.append("docs/about/index.md: AI usage must be stated in affirmative form")

requirements = (ROOT / "requirements.txt").read_text(encoding="utf-8").splitlines()
for req in [r for r in requirements if r.strip() and not r.lstrip().startswith("#")]:
    if "==" not in req:
        errors.append(f"requirements.txt: dependency must be pinned exactly: `{req}`")

# Published-content rights guardrails.
for path in sorted(DOCS.rglob("*.md")):
    if "about" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    try:
        meta, body = split_fm(text)
    except yaml.YAMLError:
        continue
    if not (meta and meta.get("status") == "published" and path.name != "index.md" and "sample" not in path.name):
        continue

    rel = path.relative_to(ROOT)
    has_media = bool(
        re.search(r"!\[[^\]]*\]\([^)]+\)", body)
        or re.search(r"<(?:img|video|audio|iframe|embed|object)\b", body, flags=re.I)
    )
    media_rights = str(meta.get("media_rights", "none")).lower()
    allowed_media = {"original", "licensed", "permission", "public-domain"}
    if has_media and media_rights not in allowed_media:
        errors.append(
            f"{rel}: embedded media requires front matter `media_rights` "
            f"({', '.join(sorted(allowed_media))})"
        )

    # Direct blockquotes require an explicit manual review marker.
    has_quote = bool(re.search(r"(?m)^\s*>\s+\S", body) or re.search(r"<blockquote\b", body, flags=re.I))
    if has_quote and meta.get("quotation_reviewed") is not True:
        errors.append(f"{rel}: direct quotation requires `quotation_reviewed: true`")

    # Published articles should never contain executable inline scripts.
    if re.search(r"<script\b", body, flags=re.I):
        errors.append(f"{rel}: executable script is not allowed in published editorial content")

if errors:
    print("Content checks failed:")
    for e in errors: print("-",e)
    sys.exit(1)
print("Content checks passed.")

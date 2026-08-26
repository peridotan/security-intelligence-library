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

if errors:
    print("Content checks failed:")
    for e in errors: print("-",e)
    sys.exit(1)
print("Content checks passed.")

#!/usr/bin/env python3
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REQUIRED = ["title","date","updated","description","category","tags","audience",
            "management_impact","urgency","evidence","status","pptx"]

def split_fm(text):
    if not text.startswith("---\n"):
        return None, text
    parts = text.split("---\n", 2)
    return yaml.safe_load(parts[1]) or {}, parts[2]

def dump_fm(data):
    order = ["title","date","updated","description","category","tags","audience",
             "management_impact","urgency","evidence","status","pptx","hide"]
    out = {k:data[k] for k in order if k in data}
    out.update({k:v for k,v in data.items() if k not in out})
    return "---\n" + yaml.safe_dump(out, allow_unicode=True, sort_keys=False).strip() + "\n---\n"

def esc(v):
    return (str(v).replace("&","&amp;").replace("<","&lt;")
            .replace(">","&gt;").replace('"',"&quot;"))

def article(path, meta):
    return bool(meta and meta.get("status") == "published"
                and path.name != "index.md" and "sample" not in path.name
                and "about" not in path.parts)

def meta_block(meta):
    audience = " / ".join(str(x) for x in meta.get("audience", []))
    impact = str(meta.get("management_impact",""))
    iclass = re.sub(r"[^a-z]","",impact.lower()) or "medium"
    items = [
        ("Published",meta.get("date","")), ("Updated",meta.get("updated","")),
        ("Category",meta.get("category","")), ("Audience",audience),
        ("Management Impact",impact), ("Urgency",meta.get("urgency","")),
        ("Evidence",meta.get("evidence",""))
    ]
    rows = ['<div class="sil-article-meta">']
    for label,value in items:
        if label == "Management Impact":
            rows.append(f'  <div class="sil-meta-item"><span class="sil-meta-label">{label}</span><span class="sil-impact-{iclass}">{esc(value)}</span></div>')
        else:
            rows.append(f'  <div class="sil-meta-item"><span class="sil-meta-label">{label}</span><span class="sil-meta-value">{esc(value)}</span></div>')
    rows.append("</div>")
    pptx = str(meta.get("pptx","") or "").strip()
    if pptx:
        rows += ['<div class="sil-ppt-link">', f'  <a href="{esc(pptx)}">PowerPoint版を開く →</a>', '</div>']
    return "\n".join(rows) + "\n\n"

for path in sorted(DOCS.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    if "about" in path.parts:
        continue
    try:
        meta, body = split_fm(text)
    except yaml.YAMLError:
        continue
    if not article(path, meta):
        continue
    missing = [k for k in REQUIRED if k not in meta]
    if missing:
        raise SystemExit(f"{path}: missing front matter: {', '.join(missing)}")
    body = re.sub(r"\n## PowerPoint\n.*?(?=\n## |\Z)", "\n", body, flags=re.S)
    h1 = re.search(r"(?m)^# .+$", body)
    summary = body.find('<div class="sil-executive-summary"')
    if not h1 or summary < 0:
        raise SystemExit(f"{path}: H1 or Executive Summary wrapper missing")
    body = body[:h1.end()] + "\n\n" + meta_block(meta) + body[summary:].lstrip()
    path.write_text(dump_fm(meta) + body, encoding="utf-8")
print("Article metadata synchronized.")

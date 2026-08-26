#!/usr/bin/env python3
from pathlib import Path
from datetime import date, datetime
import calendar
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REQUIRED = [
    "title", "date", "updated", "reviewed", "review_status", "source_period",
    "description", "category", "collections", "tags", "audience",
    "management_impact", "impact_types", "urgency", "evidence", "status",
    "pptx", "media_rights"
]

def split_fm(text):
    if not text.startswith("---\n"):
        return None, text
    parts = text.split("---\n", 2)
    return yaml.safe_load(parts[1]) or {}, parts[2]

def dump_fm(data):
    order = [
        "title", "date", "updated", "reviewed", "review_status",
        "source_period", "event_date", "description", "category", "collections",
        "tags", "audience", "management_impact", "impact_types",
        "urgency", "evidence", "status", "monthly_include",
        "pptx", "media_rights", "quotation_reviewed", "hide", "search"
    ]
    out = {k: data[k] for k in order if k in data}
    out.update({k: v for k, v in data.items() if k not in out})
    return "---\n" + yaml.safe_dump(out, allow_unicode=True, sort_keys=False).strip() + "\n---\n"

def esc(v):
    return (str(v).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))

def fmt_date(v):
    if isinstance(v, (date, datetime)):
        return v.isoformat()
    return str(v)

def fmt_period(v):
    s = str(v)
    m = re.fullmatch(r"(\d{4})-(\d{2})", s)
    if not m:
        return s
    year, month = int(m.group(1)), int(m.group(2))
    return f"{calendar.month_name[month]} {year}"

def article(path, meta):
    return bool(
        meta and meta.get("status") == "published"
        and path.name != "index.md"
        and "sample" not in path.name
        and "about" not in path.parts
    )

def meta_block(meta):
    audience = " / ".join(str(x) for x in meta.get("audience", []))
    impact = str(meta.get("management_impact", ""))
    impact_types = " / ".join(str(x) for x in meta.get("impact_types", []))
    iclass = re.sub(r"[^a-z]", "", impact.lower()) or "medium"
    review = str(meta.get("review_status", ""))
    rclass = re.sub(r"[^a-z]", "-", review.lower()).strip("-") or "current"

    items = [
        ("Published", fmt_date(meta.get("date", "")), None),
        ("Source Period", fmt_period(meta.get("source_period", "")), None),
        ("Updated", fmt_date(meta.get("updated", "")), None),
        ("Last Reviewed", fmt_date(meta.get("reviewed", "")), None),
        ("Review Status", review, f"sil-review-{rclass}"),
        ("Category", meta.get("category", ""), None),
        ("Audience", audience, None),
        ("Impact Areas", impact_types, None),
        ("Management Impact", impact, f"sil-impact-{iclass}"),
        ("Urgency", meta.get("urgency", ""), None),
        ("Evidence", meta.get("evidence", ""), None),
    ]
    rows = ['<div class="sil-article-meta">']
    for label, value, css in items:
        cls = css or "sil-meta-value"
        rows.append(
            f'  <div class="sil-meta-item"><span class="sil-meta-label">{label}</span>'
            f'<span class="{cls}">{esc(value)}</span></div>'
        )
    rows.append("</div>")

    pptx = str(meta.get("pptx", "") or "").strip()
    if pptx:
        rows += [
            '<div class="sil-ppt-link">',
            f'  <a href="{esc(pptx)}">PowerPoint版を開く →</a>',
            '</div>'
        ]
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
    # Remove any previously generated metadata block before recreating it.
    body = re.sub(
        r'\n<div class="sil-article-meta">.*?</div>\s*</div>\s*',
        "\n",
        body,
        count=1,
        flags=re.S
    )
    body = re.sub(
        r'\n<div class="sil-ppt-link">.*?</div>\s*',
        "\n",
        body,
        count=1,
        flags=re.S
    )

    h1 = re.search(r"(?m)^# .+$", body)
    summary = body.find('<div class="sil-executive-summary"')
    if not h1 or summary < 0:
        raise SystemExit(f"{path}: H1 or Executive Summary wrapper missing")

    body = body[:h1.end()] + "\n\n" + meta_block(meta) + body[summary:].lstrip()
    path.write_text(dump_fm(meta) + body, encoding="utf-8")

print("Article metadata synchronized.")

#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from datetime import date, datetime
import calendar
import html
import os
import re
from collections import Counter, defaultdict
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TOPIC_CONFIG = ROOT / "config" / "topics.yml"


def load_topic_taxonomy():
    data = yaml.safe_load(TOPIC_CONFIG.read_text(encoding="utf-8")) or {}
    groups = data.get("groups") or []
    by_name = {}
    for group in groups:
        for topic in group.get("topics") or []:
            by_name[str(topic["name"])] = topic
    return groups, by_name

TOPIC_GROUPS, TOPIC_BY_NAME = load_topic_taxonomy()

CATEGORY_INFO = {
    "cybersecurity": ("Cybersecurity", "cybersecurity/index.md"),
    "identity-security": ("Identity Security", "identity-security/index.md"),
    "ai-security": ("AI Security", "ai-security/index.md"),
    "regulation": ("Regulation", "regulation/index.md"),
    "risk-management": ("Management View", "risk-management/index.md"),
}
URGENCY_ORDER = {"Immediate": 0, "Near-term": 1, "Strategic": 2}

def split_fm(text):
    if not text.startswith("---\n"):
        return None, text
    parts = text.split("---\n", 2)
    return yaml.safe_load(parts[1]) or {}, parts[2]

def fmt_date(v):
    if isinstance(v, (date, datetime)):
        return v.isoformat()
    return str(v)

def fmt_period(v):
    s = str(v)
    m = re.fullmatch(r"(\d{4})-(\d{2})", s)
    if not m:
        return s
    y, mo = int(m.group(1)), int(m.group(2))
    return f"{calendar.month_name[mo]} {y}"

def period_key(v):
    s = str(v or "")
    m = re.fullmatch(r"(\d{4})-(\d{2})", s)
    return (int(m.group(1)), int(m.group(2))) if m else (0, 0)

def article_sort(a):
    meta = a["meta"]
    return (
        -period_key(meta.get("source_period"))[0],
        -period_key(meta.get("source_period"))[1],
        URGENCY_ORDER.get(str(meta.get("urgency")), 9),
        -int(fmt_date(meta.get("updated", "0000-00-00")).replace("-", "") or 0),
        str(meta.get("title", "")),
    )

def iter_articles():
    rows = []
    for path in sorted(DOCS.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        try:
            meta, body = split_fm(text)
        except yaml.YAMLError:
            continue
        if not (
            meta and meta.get("status") == "published"
            and path.name != "index.md"
            and "sample" not in path.name
            and "about" not in path.parts
        ):
            continue
        rows.append({"path": path, "meta": meta, "body": body})
    return sorted(rows, key=article_sort)

def rel_link(from_page: Path, to_page: Path):
    return os.path.relpath(to_page, start=from_page.parent).replace(os.sep, "/")

def esc(v):
    return html.escape(str(v), quote=True)

def shorten(text, n=122):
    value = re.sub(r"\s+", " ", str(text or "")).strip()
    return value if len(value) <= n else value[:n-1].rstrip() + "…"

def primary_collection(meta):
    collections = meta.get("collections") or []
    if collections:
        return str(collections[0])
    return ""

def card(article, page, mode="category", more=False):
    meta, path = article["meta"], article["path"]
    title = esc(meta.get("title", ""))
    href = esc(rel_link(page, path))
    desc = esc(shorten(meta.get("description", "")))
    period = fmt_period(meta.get("source_period", ""))
    urgency = str(meta.get("urgency", ""))
    evidence = str(meta.get("evidence", ""))
    primary = primary_collection(meta)
    category = CATEGORY_INFO.get(primary, (str(meta.get("category", "")), ""))[0]
    areas = " / ".join(str(x) for x in (meta.get("impact_types") or [])[:2])

    if mode == "home":
        meta_line = f"{period} · {category} · Urgency: {urgency}"
    elif mode == "monthly":
        meta_line = f"{category} · {urgency} · {evidence}"
    else:
        meta_line = f"{period} · {urgency} · {evidence}"
        if areas:
            meta_line += f" · {areas}"

    out = [
        '  <article class="sil-card">',
        f'    <a class="sil-card-title" href="{href}">{title}</a>',
        f'    <div class="sil-card-meta">{esc(meta_line)}</div>',
        f'    <p>{desc}</p>',
    ]
    if more:
        out.append(f'    <a class="sil-card-more" href="{href}">記事を読む →</a>')
    out.append("  </article>")
    return "\n".join(out)

def replace_block(path: Path, name: str, content: str):
    text = path.read_text(encoding="utf-8")
    start = f"<!-- AUTO:{name}:START -->"
    end = f"<!-- AUTO:{name}:END -->"
    pattern = re.escape(start) + r".*?" + re.escape(end)
    replacement = start + "\n" + content.rstrip() + "\n" + end
    new, count = re.subn(pattern, replacement, text, flags=re.S)
    if count != 1:
        raise SystemExit(f"{path}: expected exactly one auto block `{name}`, found {count}")
    path.write_text(new, encoding="utf-8")

articles = iter_articles()

# Home: latest six, prioritizing the current source period and urgency.
home = DOCS / "index.md"
latest = articles[:6]
latest_html = '<div class="sil-cards sil-cards-2">\n' + "\n".join(
    card(a, home, mode="home", more=True) for a in latest
) + "\n</div>"
replace_block(home, "HOME_LATEST", latest_html)

# Monthly metadata and monthly-page article blocks.
monthly_pages = []
for page in sorted((DOCS / "monthly").glob("20??-??.md")):
    meta, body = split_fm(page.read_text(encoding="utf-8"))
    period = str(meta.get("period") or page.stem)
    month_articles = [
        a for a in articles
        if str(a["meta"].get("source_period")) == period
        and a["meta"].get("monthly_include", True) is not False
    ]
    if "<!-- AUTO:MONTH_ARTICLES:START -->" in page.read_text(encoding="utf-8"):
        block = (
            f"## Core {len(month_articles)} Themes\n\n"
            '<div class="sil-cards sil-cards-2">\n'
            + "\n".join(card(a, page, mode="monthly") for a in month_articles)
            + "\n</div>"
        )
        replace_block(page, "MONTH_ARTICLES", block)
    monthly_pages.append({
        "path": page,
        "meta": meta,
        "period": period,
        "count": len(month_articles),
    })

monthly_pages.sort(key=lambda m: period_key(m["period"]), reverse=True)

def month_card(m, page):
    meta = m["meta"]
    href = esc(rel_link(page, m["path"]))
    title = esc(meta.get("title") or f"{fmt_period(m['period'])} Intelligence")
    summary = esc(shorten(meta.get("summary") or meta.get("description") or "", 145))
    reviewed = fmt_date(
        meta.get("reviewed") or meta.get("as_of") or meta.get("updated") or ""
    )
    reviewed_part = f" · Reviewed {reviewed}" if reviewed else ""
    return "\n".join([
        '  <article class="sil-card">',
        f'    <a class="sil-card-title" href="{href}">{title}</a>',
        f'    <div class="sil-card-meta">{m["count"]} Core Themes{esc(reviewed_part)}</div>',
        f'    <p>{summary}</p>',
        f'    <a class="sil-card-more" href="{href}">月次サマリーを見る →</a>',
        '  </article>',
    ])

monthly_index = DOCS / "monthly/index.md"
monthly_html = '<div class="sil-cards">\n' + "\n".join(
    month_card(m, monthly_index) for m in monthly_pages
) + "\n</div>"
replace_block(monthly_index, "MONTHLY_INDEX", monthly_html)

home_monthly = '<div class="sil-cards">\n' + "\n".join(
    month_card(m, home) for m in monthly_pages[:3]
) + "\n</div>"
replace_block(home, "HOME_MONTHLY", home_monthly)

# Category indexes from article collections.
for collection, (_, rel_index) in CATEGORY_INFO.items():
    page = DOCS / rel_index
    selected = [a for a in articles if collection in (a["meta"].get("collections") or [])]
    html_cards = '<div class="sil-cards sil-cards-2">\n' + "\n".join(
        card(a, page, mode="category") for a in selected
    ) + "\n</div>"
    replace_block(page, "CATEGORY_ARTICLES", html_cards)

# Topics: controlled editorial taxonomy. Tags are kept separately as granular keywords.
topic_page = DOCS / "topics/index.md"
topic_articles = defaultdict(list)
for a in articles:
    for topic in a["meta"].get("topics") or []:
        topic_articles[str(topic)].append(a)

def topic_anchor(name):
    item = TOPIC_BY_NAME.get(name)
    if item and item.get("id"):
        return str(item["id"])
    value = name.casefold()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")

topic_parts = [
    "## Topic Directory",
    "",
    '<div class="sil-topic-groups">',
]
for group in TOPIC_GROUPS:
    topic_parts += [
        '<section class="sil-topic-group">',
        f'<div class="sil-topic-group-title">{esc(group["name"])}</div>',
        '<div class="sil-topic-directory">',
    ]
    for topic in group.get("topics") or []:
        name = str(topic["name"])
        count = len(topic_articles.get(name, []))
        topic_parts.append(
            f'<a class="sil-topic" href="#{esc(topic_anchor(name))}">'
            f'{esc(name)} <span class="sil-topic-count">{count}</span></a>'
        )
    topic_parts += ["</div>", "</section>"]
topic_parts += ["</div>", ""]

for group in TOPIC_GROUPS:
    topic_parts += [f'## {group["name"]}', ""]
    for topic in group.get("topics") or []:
        name = str(topic["name"])
        desc = str(topic.get("description") or "")
        rows = sorted(topic_articles.get(name, []), key=article_sort)
        topic_parts += [
            f'### {name} {{#{topic_anchor(name)}}}',
            "",
            desc,
            "",
        ]
        if rows:
            for a in rows:
                m = a["meta"]
                href = rel_link(topic_page, a["path"])
                topic_parts.append(
                    f'- [{m["title"]}]({href}) '
                    f'— {fmt_period(m.get("source_period"))} · '
                    f'{m.get("urgency")} · {m.get("evidence")}'
                )
        else:
            topic_parts.append("_該当記事はまだありません。_")
        topic_parts.append("")

replace_block(topic_page, "TOPICS", "\n".join(topic_parts))

# Tags: detailed keywords remain searchable/discoverable, but are not editorial Topics.
tags_page = DOCS / "tags/index.md"
tag_articles = defaultdict(list)
for a in articles:
    for tag in a["meta"].get("tags") or []:
        tag_articles[str(tag)].append(a)

def tag_sort(item):
    tag, rows = item
    return (-len(rows), tag.casefold())

multi_tags = [(tag, rows) for tag, rows in tag_articles.items() if len(rows) >= 2]
single_tags = [(tag, rows) for tag, rows in tag_articles.items() if len(rows) == 1]
multi_tags.sort(key=tag_sort)
single_tags.sort(key=lambda x: x[0].casefold())

def tag_anchor(tag):
    value = tag.casefold()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    if value:
        return value
    import hashlib
    return "tag-" + hashlib.sha1(tag.encode("utf-8")).hexdigest()[:10]

tag_parts = [
    "## Frequently Used Tags",
    "",
    '<div class="sil-topic-directory">',
]
for tag, rows in multi_tags:
    tag_parts.append(
        f'<a class="sil-topic" href="#{esc(tag_anchor(tag))}">'
        f'{esc(tag)} <span class="sil-topic-count">{len(rows)}</span></a>'
    )
tag_parts += ["</div>", ""]

for tag, rows in multi_tags:
    tag_parts += [f'## {tag} {{#{tag_anchor(tag)}}}', ""]
    for a in sorted(rows, key=article_sort):
        m = a["meta"]
        href = rel_link(tags_page, a["path"])
        tag_parts.append(
            f'- [{m["title"]}]({href}) '
            f'— {fmt_period(m.get("source_period"))} · {m.get("urgency")}'
        )
    tag_parts.append("")

if single_tags:
    tag_parts += [
        "## One-article Tags",
        "",
        "現時点で1記事だけに付いている詳細キーワードです。",
        "",
        '<div class="sil-topic-directory">',
    ]
    for tag, rows in single_tags:
        href = rel_link(tags_page, rows[0]["path"])
        tag_parts.append(
            f'<a class="sil-topic" href="{esc(href)}">{esc(tag)} '
            f'<span class="sil-topic-count">1</span></a>'
        )
    tag_parts += ["</div>", ""]

replace_block(tags_page, "TAGS", "\n".join(tag_parts))

# Home Featured Topics = most-used curated Topics only.
topic_rank = []
for group_index, group in enumerate(TOPIC_GROUPS):
    for topic_index, topic in enumerate(group.get("topics") or []):
        name = str(topic["name"])
        topic_rank.append(
            (name, len(topic_articles.get(name, [])), group_index, topic_index)
        )
topic_rank.sort(key=lambda x: (-x[1], x[2], x[3]))
featured = [item for item in topic_rank if item[1] > 0][:8]
featured_html = '<div class="sil-topics">\n' + "\n".join(
    f'<a class="sil-topic" href="topics/index.md#{topic_anchor(name)}">'
    f'{esc(name)} <span class="sil-topic-count">{count}</span></a>'
    for name, count, _, _ in featured
) + "\n</div>"
replace_block(home, "HOME_TOPICS", featured_html)

used_topic_count = sum(
    1 for name in TOPIC_BY_NAME if topic_articles.get(name)
)
print(
    f"Indexes generated: {len(articles)} articles, "
    f"{len(monthly_pages)} monthly pages, "
    f"{used_topic_count} curated topics, {len(tag_articles)} tags."
)

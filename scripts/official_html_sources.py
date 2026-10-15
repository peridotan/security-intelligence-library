"""Conservative HTML listing adapters for official Japanese security sources.

Parse public, dated first-party links only. No linked-page crawling or JavaScript.
Unsupported HTML structures should not fabricate publication dates or URLs.
"""
from __future__ import annotations

from datetime import date
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
import re

NICT_PRESS_PATH = re.compile(r"^/press/(20\d\d)/(\d{2})/(\d{2})-[0-9]+\.html$")
NICT_SECURITY = re.compile(
    r"サイバー|セキュリティ|脆弱|不正アクセス|情報漏|攻撃|マルウェア|"
    r"暗号|ランサム|フィッシング|認証|インシデント|MITRE|PQC|AI安全", re.I
)

class Links(HTMLParser):
    def __init__(self, html: str):
        super().__init__(convert_charrefs=True)
        self.line_offsets = [0] + [m.end() for m in re.finditer(r"\n", html)]
        self.open_links: list[dict] = []
        self.links: list[dict] = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        attrs = dict(attrs)
        line, col = self.getpos()
        position = self.line_offsets[line - 1] + col
        self.open_links.append({"href": attrs.get("href", ""), "text": [], "position": position})

    def handle_data(self, data):
        if self.open_links:
            self.open_links[-1]["text"].append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.open_links:
            node = self.open_links.pop()
            node["text"] = re.sub(r"\s+", " ", " ".join(node["text"])).strip()
            self.links.append(node)


def valid_day(year: str, month: str, day: str) -> str | None:
    try:
        return date(int(year), int(month), int(day)).isoformat()
    except ValueError:
        return None


def nict_press(html: str, source: dict) -> list[dict]:
    records = []
    for link in Links(html).links:
        url = urljoin(source["url"], link["href"])
        parts = urlparse(url)
        if parts.hostname not in ("www.nict.go.jp", "www1.nict.go.jp"):
            continue
        match = NICT_PRESS_PATH.fullmatch(parts.path)
        title = link["text"]
        if not match or not title or not NICT_SECURITY.search(title):
            continue
        published = valid_day(*match.groups())
        if published:
            records.append({"title": title, "url": url, "published_raw": published, "summary": ""})
    return records


def parse_html_listing(html_bytes: bytes, source: dict) -> list[dict]:
    html = html_bytes.decode("utf-8-sig", errors="replace")
    strategy = source.get("html_strategy")
    if strategy == "nict_press":
        return nict_press(html, source)
    raise ValueError(f"unsupported HTML listing strategy: {strategy}")

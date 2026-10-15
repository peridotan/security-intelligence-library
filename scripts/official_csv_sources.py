"""Read the NCO's published annual CSV, used by its official news page."""
from __future__ import annotations

import csv
from datetime import date
from io import StringIO
from urllib.parse import urljoin, urlparse


def official_nco_link(href: str) -> str:
    if not href or href.strip() in ("#", "-"):
        return ""
    url = urljoin("https://www.cyber.go.jp/", href.strip())
    part = urlparse(url)
    host = part.hostname or ""
    if part.scheme != "https" or not (host == "cyber.go.jp" or host.endswith(".cyber.go.jp")):
        return ""
    return url


def parse_nco_csv(payload: bytes, source: dict) -> list[dict]:
    rows = csv.DictReader(StringIO(payload.decode("utf-8-sig")))
    if not rows.fieldnames or not {"date", "name", "path", "pdf"}.issubset(rows.fieldnames):
        raise ValueError("NCO CSV missing expected columns")
    items = []
    for row in rows:
        raw_date = (row.get("date") or "").strip()
        try:
            year, month, day = [int(v) for v in raw_date.split("/")]
            published = date(year, month, day).isoformat()
        except (ValueError, TypeError):
            continue
        title = (row.get("name") or "").strip()
        if not title:
            continue
        url = official_nco_link(row.get("path") or "")
        if not url:
            for pdf in (row.get("pdf") or "").split(";"):
                path = pdf.rsplit("|", 1)[-1].strip()
                url = official_nco_link(path)
                if url:
                    break
        if not url:
            continue
        items.append({"title": title, "url": url, "published_raw": published,
                      "summary": ""})
    return items

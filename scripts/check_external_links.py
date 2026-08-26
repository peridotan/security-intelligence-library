#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from urllib import request, error
from urllib.parse import urlparse
from datetime import date
import argparse
import re
import socket
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

parser = argparse.ArgumentParser()
parser.add_argument("--output", help="Write Markdown report")
parser.add_argument("--timeout", type=float, default=12.0)
parser.add_argument("--delay", type=float, default=0.05)
args = parser.parse_args()

url_sources = {}
for path in DOCS.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    for url in re.findall(r"https?://[^\s)>\]\"']+", text):
        url = url.rstrip(".,;:")
        url_sources.setdefault(url, set()).add(path.relative_to(ROOT).as_posix())

hard = []
warnings = []
ok = 0

headers = {
    "User-Agent": "Security-Intelligence-Library-LinkChecker/1.0 (+https://github.com/peridotan/security-intelligence-library)"
}

for i, url in enumerate(sorted(url_sources), 1):
    status = None
    note = ""
    try:
        req = request.Request(url, headers=headers, method="HEAD")
        try:
            with request.urlopen(req, timeout=args.timeout) as resp:
                status = resp.status
        except error.HTTPError as exc:
            status = exc.code
            # Some sites reject HEAD while GET works.
            if status in {400, 405, 501}:
                req = request.Request(url, headers={**headers, "Range": "bytes=0-0"}, method="GET")
                with request.urlopen(req, timeout=args.timeout) as resp:
                    status = resp.status
    except error.HTTPError as exc:
        status = exc.code
    except (error.URLError, socket.timeout, TimeoutError, OSError) as exc:
        note = type(exc).__name__

    sources = ", ".join(sorted(url_sources[url]))
    if status in {404, 410}:
        hard.append((url, status, sources))
    elif status is None:
        warnings.append((url, note or "network error", sources))
    elif status in {401, 403, 429} or status >= 500:
        # Authentication, bot protection, rate limiting and temporary server
        # failures are warnings to avoid false-positive maintenance issues.
        warnings.append((url, f"HTTP {status}", sources))
    else:
        ok += 1

    if args.delay:
        time.sleep(args.delay)

lines = [
    "# External Link Report", "",
    f"Generated: {date.today().isoformat()}",
    f"Checked: {len(url_sources)} · OK/redirect: {ok} · Hard broken: {len(hard)} · Warnings: {len(warnings)}",
    "",
]
if hard:
    lines += ["## Hard broken links", ""]
    for url, status, sources in hard:
        lines.append(f"- HTTP {status}: {url} — {sources}")
    lines.append("")
if warnings:
    lines += ["## Warnings / inconclusive", ""]
    for url, reason, sources in warnings:
        lines.append(f"- {reason}: {url} — {sources}")
    lines.append("")
if not hard and not warnings:
    lines += ["No link problems detected.", ""]

report = "\n".join(lines)
print(report)
if args.output:
    Path(args.output).write_text(report, encoding="utf-8")
sys.exit(1 if hard else 0)

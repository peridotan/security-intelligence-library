#!/usr/bin/env python3
from pathlib import Path
from datetime import date, datetime
import argparse
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

THRESHOLDS = {
    "regulation": 90,
    "identity-security": 120,
    "ai-security": 120,
    "cybersecurity": 120,
    "risk-management": 180,
}

def split_fm(text):
    if not text.startswith("---\n"):
        return None, text
    p = text.split("---\n", 2)
    return yaml.safe_load(p[1]) or {}, p[2]

def parse_date(v):
    if isinstance(v, datetime):
        return v.date()
    if isinstance(v, date):
        return v
    return date.fromisoformat(str(v))

parser = argparse.ArgumentParser()
parser.add_argument("--output", help="Write Markdown report")
args = parser.parse_args()

today = date.today()
due = []
for path in sorted(DOCS.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        continue
    meta, _ = split_fm(text)
    if not (
        meta and meta.get("status") == "published"
        and path.name != "index.md" and "sample" not in path.name
    ):
        continue
    if meta.get("review_status") in {"Superseded", "Archived"}:
        continue

    collections = meta.get("collections") or []
    thresholds = [THRESHOLDS[c] for c in collections if c in THRESHOLDS]
    threshold = min(thresholds) if thresholds else 120
    reviewed = parse_date(meta["reviewed"])
    age = (today - reviewed).days
    if age > threshold or meta.get("review_status") == "Needs Review":
        due.append((path.relative_to(ROOT), meta.get("title"), reviewed, age, threshold))

lines = ["# Review Freshness Report", "", f"Generated: {today.isoformat()}", ""]
if due:
    lines += ["## Review required", ""]
    for path, title, reviewed, age, threshold in due:
        lines.append(
            f"- **{title}** — `{path}` — reviewed {reviewed.isoformat()} "
            f"({age} days ago; threshold {threshold})"
        )
else:
    lines += ["No published articles are currently due for review."]

report = "\n".join(lines) + "\n"
print(report, end="")
if args.output:
    Path(args.output).write_text(report, encoding="utf-8")
sys.exit(1 if due else 0)

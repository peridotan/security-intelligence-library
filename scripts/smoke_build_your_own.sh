#!/usr/bin/env bash
set -euo pipefail

# Isolated reproduction check for docs/about/build-your-own.md.
# No user repository is created, no GitHub Pages deployment, and no PR is opened.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
cd "$WORK"

echo "::group::Step 1 - bootstrap a clean Zensical site"
zensical new .
test -f zensical.toml
test -f docs/index.md
test -f .github/workflows/docs.yml
printf 'site/\n.venv/\n__pycache__/\n' > .gitignore
zensical build --clean --strict
test -f site/index.html
echo "::endgroup::"

echo "::group::Step 2 - selective MIT software import from source repository"
git init -b main
git config user.name "Repro Smoke Test"
git config user.email "repro-smoke@example.invalid"
git add .
git commit -qm "Initial independent site"

git remote add sil-source https://github.com/peridotan/security-intelligence-library.git
git fetch --depth=1 sil-source main
echo "Source ref: $(git rev-parse FETCH_HEAD)"
git restore --source=FETCH_HEAD --staged --worktree -- \
  requirements.txt \
  config/intelligence_sources.yml \
  config/intelligence_triage.yml \
  scripts/collect_intelligence_candidates.py \
  scripts/triage_intelligence_candidates.py \
  scripts/official_html_sources.py \
  scripts/official_csv_sources.py \
  scripts/open_review_pr.sh \
  scripts/request_pr_review.sh \
  .github/workflows/collect-intelligence-candidates.yml \
  LICENSE-CODE.txt
git remote remove sil-source

test -f LICENSE-CODE.txt
test -f scripts/collect_intelligence_candidates.py
test -f scripts/triage_intelligence_candidates.py
bash -n scripts/open_review_pr.sh scripts/request_pr_review.sh
test ! -d docs/cybersecurity  # no published articles from the source repository
test -f docs/index.md
echo "::endgroup::"

echo "::group::Step 3 - fixture-based collection and deterministic Triage"
mkdir -p .automation-review .repro-fixture
python - <<'PY'
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape
import yaml

feed = Path(".repro-fixture/feed.xml").resolve()
now = format_datetime(datetime.now(timezone.utc))
feed.write_text(
    '<rss version="2.0"><channel>'
    '<item><title>Reproduction test security advisory</title>'
    '<link>https://example.invalid/build-your-own-fixture</link>'
    '<description>Fixture-only advisory for isolated smoke testing</description>'
    f'<pubDate>{escape(now)}</pubDate></item>'
    '</channel></rss>',
    encoding="utf-8",
)
config = {
    "version": 1,
    "sources": [{
        "id": "fixture-rss",
        "name": "Local Fixture",
        "type": "rss",
        "url": feed.as_uri(),
        "enabled": True,
        "category_hint": "cybersecurity",
        "trust": "primary",
    }],
}
Path(".repro-fixture/sources.yml").write_text(
    yaml.safe_dump(config, sort_keys=False), encoding="utf-8"
)
PY
python scripts/collect_intelligence_candidates.py \
  --config .repro-fixture/sources.yml \
  --days 7 \
  --output-json .automation-review/raw-local.json \
  --output-md .automation-review/raw-local.md
python scripts/triage_intelligence_candidates.py \
  --input-json .automation-review/raw-local.json \
  --output-json .automation-review/triage-local.json \
  --output-md .automation-review/triage-local.md
python - <<'PY'
from pathlib import Path
import json
raw = json.loads(Path(".automation-review/raw-local.json").read_text(encoding="utf-8"))
triage = json.loads(Path(".automation-review/triage-local.json").read_text(encoding="utf-8"))
assert raw["candidate_count"] == 1, raw
assert triage["candidate_count"] == 1, triage
assert triage["candidates"][0]["triage"]["route"] == "watch", triage
assert triage["candidates"][0]["triage"]["draft_eligible"] is False, triage
assert not (Path("docs")/"cybersecurity").exists(), "Editorial content was copied"
print("PASS: a newly created site, selective code import, RSS fixture, and Watch triage")
PY
echo "::endgroup::"

# Build remains valid after installing the collector files.
zensical build --clean --strict
test -f site/index.html
echo "Build Your Own smoke test passed; no external repo created or published."

#!/usr/bin/env python3
"""Regenerate derived content, synchronize article metadata, and run quality checks."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

for script in [
    "scripts/build_indexes.py",
    "scripts/sync_article_metadata.py",
    "scripts/check_content.py",
]:
    subprocess.run([sys.executable, script], cwd=ROOT, check=True)

print("Content update completed.")

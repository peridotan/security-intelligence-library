#!/usr/bin/env python3
"""Compare deployed Pages content with the exact built artifact (read-only HTTP)."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import sys
import time
import urllib.request
from urllib.parse import quote

BASE = "https://peridotan.github.io/security-intelligence-library/"
ROOT = Path(__file__).resolve().parents[1]


def targets(site: Path) -> list[Path]:
    result = sorted(p.relative_to(site) for p in site.rglob("*.html") if p.name != "404.html")
    context = Path("assets/context-index.json")
    if Path("index.html") not in result or not (site / context).is_file():
        raise ValueError("built site lacks home or context index")
    return result + [context]


def fetch(path: Path, revision: str) -> bytes:
    relative = path.as_posix()
    if relative.endswith("index.html"):
        relative = relative[:-len("index.html")]
    url = BASE + quote(relative, safe="/") + "?sil_revision=" + quote(revision, safe="")
    request = urllib.request.Request(url, headers={"Cache-Control": "no-cache", "Accept-Encoding": "identity", "User-Agent": "SIL-deployment-verifier/1"})
    with urllib.request.urlopen(request, timeout=15) as response:
        if response.status != 200 or not response.geturl().startswith(BASE):
            raise ValueError(f"unexpected response: {response.status}")
        return response.read()


def verify(site: Path, revision: str, getter=fetch, attempts: int = 4, delay: float = 10) -> list[str]:
    pending = {p: hashlib.sha256((site / p).read_bytes()).digest() for p in targets(site)}
    errors = {}
    for attempt in range(attempts):
        for p, expected in list(pending.items()):
            try:
                if hashlib.sha256(getter(p, revision)).digest() != expected:
                    raise ValueError("deployed content differs from built artifact")
            except (OSError, ValueError) as exc:
                errors[p] = str(exc)
            else:
                del pending[p]
                errors.pop(p, None)
        if not pending:
            break
        if attempt + 1 < attempts:
            time.sleep(delay)
    return [f"{p.as_posix()}: {errors[p]}" for p in pending]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", required=True)
    args = parser.parse_args()
    try:
        errors = verify(ROOT / "site", args.revision)
    except (OSError, ValueError) as exc:
        print(f"Deployment verification failed: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("Deployment verification failed:\n" + "\n".join(errors), file=sys.stderr)
        return 1
    print(f"Verified {len(targets(ROOT / 'site'))} deployed HTML/JSON files against built artifact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Build an allowlisted MIT Agent Kit ZIP without editorial content.

The archive is NOT a deployable SIL clone. It contains only project guidance,
task skills and a bootstrap prompt. The strict allowlist prevents accidental
distribution of article text, datasets, credentials, or generated site files.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = (
    "article-drafting",
    "evidence-review",
    "intelligence-discovery",
    "intelligence-triage",
    "monthly-review",
    "quarterly-review",
)
SOURCES = {
    "AGENTS.md": "AGENTS.md",
    "agent-kit/README.md": "README.md",
    "agent-kit/STARTER_PROMPT.md": "STARTER_PROMPT.md",
    "agent-kit/NOTICE.md": "NOTICE.md",
    "LICENSE-CODE.txt": "LICENSE.txt",
}
PREFIX = "sil-agent-kit/"


def validate_skill(path: Path, name: str) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    split = text.split("\n---\n", 1)
    if len(split) != 2:
        raise ValueError(f"{path}: unterminated YAML frontmatter")
    frontmatter = split[0][4:].splitlines()
    fields = {}
    for line in frontmatter:
        if ":" not in line:
            raise ValueError(f"{path}: malformed frontmatter")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    if fields.get("name") != name:
        raise ValueError(f"{path}: name must match directory")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError(f"{path}: invalid skill name")
    if len(fields.get("description", "")) < 20:
        raise ValueError(f"{path}: description missing or too short")
    if fields.get("license") != "MIT":
        raise ValueError(f"{path}: distributed skill license must be MIT")
    if not split[1].strip():
        raise ValueError(f"{path}: skill instructions are empty")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="dist/sil-agent-kit.zip")
    args = parser.parse_args()

    mapped = dict(SOURCES)
    actual_skills = {
        path.parent.name
        for path in (ROOT / ".agents" / "skills").glob("*/SKILL.md")
    }
    if actual_skills != set(EXPECTED_SKILLS):
        raise SystemExit(
            "Skill allowlist does not match repository skills: "
            f"{sorted(actual_skills)}"
        )
    for name in EXPECTED_SKILLS:
        relative = f".agents/skills/{name}/SKILL.md"
        mapped[relative] = relative

    for source in mapped:
        path = ROOT / source
        if not path.is_file() or path.is_symlink():
            raise SystemExit(f"Missing/unsafe allowed input: {source}")
        if source.endswith("/SKILL.md"):
            validate_skill(path, path.parent.name)

    archive = Path(args.output).resolve()
    archive.parent.mkdir(parents=True, exist_ok=True)
    if archive in {ROOT / path for path in mapped}:
        raise SystemExit("Output would overwrite a source file")

    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for source, target in sorted(mapped.items(), key=lambda item: item[1]):
            data = (ROOT / source).read_bytes()
            entry = zipfile.ZipInfo(PREFIX + target, (2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = (0o100644 << 16)
            zf.writestr(entry, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    with zipfile.ZipFile(archive) as zf:
        expected = {PREFIX + target for target in mapped.values()}
        actual = set(zf.namelist())
        if actual != expected or zf.testzip() is not None:
            raise SystemExit("ZIP validation failed")
        if any(name.startswith(PREFIX + "docs/") for name in actual):
            raise SystemExit("Unexpected editorial content in ZIP")
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    print(f"Agent kit ZIP verified: {len(mapped)} allowlisted files")
    print(f"Output: {archive} ({archive.stat().st_size} bytes)")
    print(f"SHA256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

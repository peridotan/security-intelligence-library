#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse
import json
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CONTEXT_INDEX = DOCS / "assets" / "context-index.json"
ATTACK_CONFIG = ROOT / "config" / "mitre_attack.yml"

CVE_RE = re.compile(r"CVE-\d{4}-\d{4,}", re.IGNORECASE)
ACTOR_RE = re.compile(r"G\d{4}", re.IGNORECASE)
TECHNIQUE_RE = re.compile(r"T\d{4}(?:\.\d{3})?", re.IGNORECASE)

HANDOFF_KEYS = {
    "cves",
    "exclude_cves",
    "actors",
    "exclude_actors",
    "techniques",
    "exclude_techniques",
}

errors = []
warnings = []


def split_fm(text):
    if not text.startswith("---\n"):
        return None, text

    parts = text.split("---\n", 2)
    if len(parts) != 3:
        return None, text

    return yaml.safe_load(parts[1]) or {}, parts[2]


def normalize(value):
    return str(value or "").strip().upper()


def validate_list(rel, handoff, key, pattern, known=None):
    if key not in handoff:
        return []

    values = handoff[key]

    if not isinstance(values, list):
        errors.append(f"{rel}: handoff.{key} must be a list")
        return []

    normalized = []
    seen = set()

    for raw in values:
        value = normalize(raw)

        if not pattern.fullmatch(value):
            errors.append(
                f"{rel}: invalid handoff.{key} value `{raw}`"
            )
            continue

        if value in seen:
            errors.append(
                f"{rel}: duplicate handoff.{key} value `{value}`"
            )
            continue

        seen.add(value)
        normalized.append(value)

        if known is not None and value not in known:
            errors.append(
                f"{rel}: unknown handoff.{key} value `{value}`"
            )

    return normalized


def load_attack_techniques():
    data = yaml.safe_load(
        ATTACK_CONFIG.read_text(encoding="utf-8")
    ) or {}

    return {
        normalize(key)
        for key in (data.get("techniques") or {}).keys()
    }


def resolve_threat_data(explicit):
    if explicit:
        return Path(explicit).resolve()

    sibling = (
        ROOT.parent
        / "threat-investigation-dashboard"
        / "data"
        / "dashboard.json"
    )

    if sibling.exists():
        return sibling

    return None


def load_actor_ids(path):
    if path is None:
        return None

    if not path.exists():
        errors.append(
            f"Threat dashboard data not found: {path}"
        )
        return None

    try:
        data = json.loads(
            path.read_text(encoding="utf-8")
        )
    except Exception as exc:
        errors.append(
            f"Failed to read Threat dashboard data: {exc}"
        )
        return None

    return {
        normalize(actor.get("external_id"))
        for actor in (data.get("actors") or [])
        if actor.get("external_id")
    }


def validate_front_matter(technique_ids, actor_ids):
    pages = 0

    for path in sorted(DOCS.rglob("*.md")):
        text = path.read_text(encoding="utf-8")

        try:
            meta, _ = split_fm(text)
        except yaml.YAMLError as exc:
            errors.append(
                f"{path.relative_to(ROOT)}: invalid YAML: {exc}"
            )
            continue

        if not meta or "handoff" not in meta:
            continue

        pages += 1
        rel = path.relative_to(ROOT)
        handoff = meta.get("handoff")

        if not isinstance(handoff, dict):
            errors.append(
                f"{rel}: handoff must be an object"
            )
            continue

        unknown = sorted(
            set(handoff.keys()) - HANDOFF_KEYS
        )

        if unknown:
            errors.append(
                f"{rel}: unsupported handoff keys: "
                + ", ".join(unknown)
            )

        cves = validate_list(
            rel,
            handoff,
            "cves",
            CVE_RE,
        )
        excluded_cves = validate_list(
            rel,
            handoff,
            "exclude_cves",
            CVE_RE,
        )

        actors = validate_list(
            rel,
            handoff,
            "actors",
            ACTOR_RE,
            actor_ids,
        )
        excluded_actors = validate_list(
            rel,
            handoff,
            "exclude_actors",
            ACTOR_RE,
            actor_ids,
        )

        techniques = validate_list(
            rel,
            handoff,
            "techniques",
            TECHNIQUE_RE,
            technique_ids,
        )
        excluded_techniques = validate_list(
            rel,
            handoff,
            "exclude_techniques",
            TECHNIQUE_RE,
            technique_ids,
        )

        for name, included, excluded in [
            ("CVE", cves, excluded_cves),
            ("Actor", actors, excluded_actors),
            ("Technique", techniques, excluded_techniques),
        ]:
            overlap = sorted(
                set(included) & set(excluded)
            )

            if overlap:
                errors.append(
                    f"{rel}: {name} appears in both include "
                    f"and exclude: {', '.join(overlap)}"
                )

    return pages


def validate_context_index(technique_ids, actor_ids):
    if not CONTEXT_INDEX.exists():
        errors.append(
            "docs/assets/context-index.json is missing"
        )
        return (0, 0, 0)

    try:
        data = json.loads(
            CONTEXT_INDEX.read_text(encoding="utf-8")
        )
    except Exception as exc:
        errors.append(
            f"Failed to read context index: {exc}"
        )
        return (0, 0, 0)

    cve_count = 0
    actor_count = 0
    technique_count = 0

    for page, row in (data.get("articles") or {}).items():
        for raw in row.get("cves") or []:
            value = normalize(raw)
            cve_count += 1

            if not CVE_RE.fullmatch(value):
                errors.append(
                    f"{page}: invalid indexed CVE `{raw}`"
                )

        for raw in row.get("actors") or []:
            value = normalize(raw)
            actor_count += 1

            if not ACTOR_RE.fullmatch(value):
                errors.append(
                    f"{page}: invalid indexed Actor `{raw}`"
                )
            elif actor_ids is not None and value not in actor_ids:
                errors.append(
                    f"{page}: Actor `{value}` not found "
                    "in Threat Investigation data"
                )

        for raw in row.get("techniques") or []:
            value = normalize(raw)
            technique_count += 1

            if not TECHNIQUE_RE.fullmatch(value):
                errors.append(
                    f"{page}: invalid indexed Technique `{raw}`"
                )
            elif value not in technique_ids:
                errors.append(
                    f"{page}: Technique `{value}` not found "
                    "in Library ATT&CK catalog"
                )

    return cve_count, actor_count, technique_count


def main():
    parser = argparse.ArgumentParser(
        description="Validate Security Intelligence Suite handoff contracts."
    )
    parser.add_argument(
        "--threat-data",
        help=(
            "Path to Threat Investigation data/dashboard.json. "
            "Defaults to sibling repository when available."
        ),
    )
    args = parser.parse_args()

    technique_ids = load_attack_techniques()

    threat_data = resolve_threat_data(args.threat_data)
    actor_ids = load_actor_ids(threat_data)

    if actor_ids is None:
        warnings.append(
            "Threat Actor existence validation skipped: "
            "Threat Investigation dashboard.json not available."
        )

    pages = validate_front_matter(
        technique_ids,
        actor_ids,
    )

    cves, actors, techniques = validate_context_index(
        technique_ids,
        actor_ids,
    )

    if warnings:
        for message in warnings:
            print(f"WARNING: {message}")

    if errors:
        print()
        print("Suite handoff checks FAILED:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print(
        "Suite handoff checks passed: "
        f"{pages} explicit handoff page(s) / "
        f"{cves} CVE ref(s) / "
        f"{actors} Actor ref(s) / "
        f"{techniques} Technique ref(s)"
    )

    if threat_data:
        print(f"Threat data: {threat_data}")


if __name__ == "__main__":
    main()

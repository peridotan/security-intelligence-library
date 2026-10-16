#!/usr/bin/env python3
"""Check standalone Incident Trend Brief evidence (structure, not source truth).

Never infer a shared actor, causal chain or national incidence rate from
sampled incident disclosures. Advisory material is not an incident record.
"""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "incident-trends"
ID_RE = re.compile(r"\d{4}-\d{2}-h[12]\Z")
KEY_RE = re.compile(r"[A-Z][A-Z0-9_-]{2,63}\Z")
CATEGORIES = {"unauthorized_access", "ransomware", "other_cyber_incident"}
IMPACT = {"confirmed_disruption", "possible_data_exposure", "investigating", "confirmed_data_exposure"}
VERACITY = {"source_fact", "source_claim"}
CONFIDENCE = {"low", "medium", "high"}


def valid_date(value: object) -> bool:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def safe_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = urlparse(value)
    except ValueError:
        return False
    return (parsed.scheme == "https" and bool(parsed.hostname)
            and not parsed.username and not parsed.password
            and parsed.hostname not in {"example.com", "www.example.com", "example.org"}
            and not parsed.hostname.endswith((".invalid", ".test", ".localhost")))


def _text(obj: dict, field: str, where: str, errors: list[str], minimum: int = 4):
    v = obj.get(field)
    if not isinstance(v, str) or len(v.strip()) < minimum:
        errors.append(f"{where}.{field}: non-empty explanatory text required")


def _references(value: object, valid_ids: set[str], where: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not value:
        errors.append(f"{where}: at least one source reference required")
        return
    for ref in value:
        if not isinstance(ref, str) or ref not in valid_ids:
            errors.append(f"{where}: unknown source {ref!r}")


def validate(data: object, filename: str) -> list[str]:
    e: list[str] = []
    if not isinstance(data, dict):
        return [f"{filename}: expected JSON object"]
    ident = data.get("brief_id")
    if data.get("schema_version") != 1 or type(data.get("schema_version")) is not int:
        e.append("schema_version must be integer 1")
    if not isinstance(ident, str) or not ID_RE.fullmatch(ident) or ident + ".json" != filename:
        e.append("brief_id must match YYYY-MM-h1/h2 and filename")
    p = data.get("period")
    if not isinstance(p, dict):
        return e + ["period: object required"]
    a, b, asof = p.get("start"), p.get("end"), p.get("as_of")
    if not all(map(valid_date, (a, b, asof))):
        e.append("period: start/end/as_of must be valid YYYY-MM-DD dates")
        return e
    if not a <= b <= asof:
        e.append("period: require start <= end <= as_of")
    if ident and isinstance(ident, str) and ID_RE.fullmatch(ident):
        year, month, half = ident.split("-")
        expected_start = f"{year}-{month}-" + ("01" if half == "h1" else "16")
        if a != expected_start:
            e.append("period start does not match the stated half-month")
        if half == "h1" and b != f"{year}-{month}-15":
            e.append("h1 period must end on day 15")
        if half == "h2":
            from calendar import monthrange
            if b != f"{year}-{month}-{monthrange(int(year), int(month))[1]:02d}":
                e.append("h2 period must end on the month's final day")
    coverage = data.get("coverage")
    if not isinstance(coverage, dict) or coverage.get("sampling") != "curated_non_exhaustive" or coverage.get("counting_unit") != "incident_group":
        e.append("coverage must state curated_non_exhaustive and incident_group counting")
    elif not isinstance(coverage.get("limitations"), str) or len(coverage["limitations"].strip()) < 25:
        e.append("coverage.limitations must explain sample bias and non-national nature")
    sources = data.get("sources")
    source_ids: set[str] = set()
    if not isinstance(sources, list) or not sources:
        e.append("sources: non-empty array required")
        sources = []
    for i, s in enumerate(sources, 1):
        loc = f"sources[{i}]"
        if not isinstance(s, dict):
            e.append(f"{loc}: object required")
            continue
        sid = s.get("id")
        if not isinstance(sid, str) or not KEY_RE.fullmatch(sid) or sid in source_ids:
            e.append(f"{loc}: unique uppercase source id required")
        else:
            source_ids.add(sid)
        if not safe_https(s.get("url")):
            e.append(f"{loc}: real https source URL required")
        _text(s, "publisher", loc, e)
        _text(s, "locator", loc, e, minimum=8)
        if not valid_date(s.get("published_at")) or s["published_at"] > asof:
            e.append(f"{loc}: published_at must not be after as_of")
        if not valid_date(s.get("accessed_at")) or s["accessed_at"] > asof:
            e.append(f"{loc}: accessed_at must not be after as_of")

    incidents = data.get("incidents")
    if not isinstance(incidents, list) or not incidents:
        e.append("incidents: non-empty array required")
        incidents = []
    event_ids: set[str] = set()
    groups: set[str] = set()
    for i, ev in enumerate(incidents, 1):
        loc = f"incidents[{i}]"
        if not isinstance(ev, dict):
            e.append(f"{loc}: object required")
            continue
        eid, grp = ev.get("id"), ev.get("event_group")
        if not isinstance(eid, str) or not KEY_RE.fullmatch(eid) or eid in event_ids:
            e.append(f"{loc}: incident id must be unique")
        else:
            event_ids.add(eid)
        if not isinstance(grp, str) or not KEY_RE.fullmatch(grp) or grp in groups:
            e.append(f"{loc}: unique event_group required; duplicate disclosures must be linked")
        else:
            groups.add(grp)
        if not valid_date(ev.get("disclosed_at")) or not a <= ev["disclosed_at"] <= b:
            e.append(f"{loc}: disclosed_at must be inside the reporting window")
        if ev.get("category") not in CATEGORIES or ev.get("impact") not in IMPACT:
            e.append(f"{loc}: invalid category/impact")
        _text(ev, "organization", loc, e)
        _text(ev, "title", loc, e)
        _text(ev, "uncertainty", loc, e, minimum=20)
        facts = ev.get("facts")
        if not isinstance(facts, list) or not facts:
            e.append(f"{loc}.facts: non-empty array required")
            facts = []
        for j, fact in enumerate(facts, 1):
            f_loc = f"{loc}.facts[{j}]"
            if not isinstance(fact, dict):
                e.append(f"{f_loc}: object required")
                continue
            _text(fact, "text", f_loc, e, minimum=15)
            if fact.get("classification") not in VERACITY:
                e.append(f"{f_loc}: classification must be source_fact or source_claim")
            _references(fact.get("source_ids"), source_ids, f_loc + ".source_ids", e)
        related = ev.get("related_disclosures", [])
        if not isinstance(related, list):
            e.append(f"{loc}.related_disclosures: array required")
            related = []
        for j, rel in enumerate(related, 1):
            rel_loc = f"{loc}.related_disclosures[{j}]"
            if not isinstance(rel, dict):
                e.append(f"{rel_loc}: object required")
                continue
            _text(rel, "organization", rel_loc, e)
            if not valid_date(rel.get("disclosed_at")) or not a <= rel["disclosed_at"] <= b:
                e.append(f"{rel_loc}: date outside reporting window")
            _references(rel.get("source_ids"), source_ids, rel_loc + ".source_ids", e)

    advisories = data.get("advisories")
    if not isinstance(advisories, list):
        e.append("advisories: array required")
        advisories = []
    advisory_ids: set[str] = set()
    for i, adv in enumerate(advisories, 1):
        loc = f"advisories[{i}]"
        if not isinstance(adv, dict):
            e.append(f"{loc}: object required")
            continue
        aid = adv.get("id")
        if not isinstance(aid, str) or not KEY_RE.fullmatch(aid) or aid in advisory_ids:
            e.append(f"{loc}: unique advisory id required")
        else:
            advisory_ids.add(aid)
        _text(adv, "summary", loc, e, minimum=15)
        _references(adv.get("source_ids"), source_ids, loc + ".source_ids", e)
    signals = data.get("trend_signals")
    if not isinstance(signals, list) or not signals:
        e.append("trend_signals: at least one analyst assessment required")
        signals = []
    signal_ids: set[str] = set()
    for i, sig in enumerate(signals, 1):
        loc = f"trend_signals[{i}]"
        if not isinstance(sig, dict):
            e.append(f"{loc}: object required")
            continue
        sid = sig.get("id")
        if not isinstance(sid, str) or not KEY_RE.fullmatch(sid) or sid in signal_ids:
            e.append(f"{loc}: unique trend id required")
        else:
            signal_ids.add(sid)
        _text(sig, "assessment", loc, e, minimum=35)
        _text(sig, "limitation", loc, e, minimum=25)
        if sig.get("confidence") not in CONFIDENCE:
            e.append(f"{loc}: invalid confidence")
        events, advis = sig.get("incident_ids"), sig.get("advisory_ids")
        if not isinstance(events, list) or not isinstance(advis, list) or not events + advis:
            e.append(f"{loc}: at least one incident/advisory reference required")
            continue
        for event in events:
            if event not in event_ids:
                e.append(f"{loc}: unknown incident {event!r}")
        for advisory in advis:
            if advisory not in advisory_ids:
                e.append(f"{loc}: unknown advisory {advisory!r}")
    return e


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Optional specific data files; defaults to data/incident-trends/*.json")
    args = parser.parse_args()
    files = [Path(p) for p in args.paths] if args.paths else sorted(INPUT.glob("*.json"))
    if not files:
        print("No Incident Trend data files found.", file=sys.stderr)
        return 1
    failures = []
    for path in files:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            failures.append(f"{path}: {exc}")
            continue
        errors = validate(payload, path.name)
        # Validate Draft article and pending claim dossier when present. Do not
        # require an old Draft after a human has staged and published the issue.
        if not errors:
            draft_slug = "incident-trend-brief-" + payload["brief_id"]
            draft = ROOT / "drafts" / "cybersecurity" / (draft_slug + ".md")
            if draft.is_file():
                import article_workflow
                errors.extend(article_workflow.validate_bundle(ROOT, "cybersecurity", draft_slug))
        failures.extend(f"{path}: {err}" for err in errors)
        if not errors:
            print(f"Validated {path}: {len(payload['incidents'])} distinct curated incident groups; "
                  f"{len(payload['advisories'])} separately tracked advisories; "
                  f"{len(payload['trend_signals'])} analyst trend hypotheses.")
    if failures:
        print("Incident Trend evidence validation FAILED:")
        for err in failures:
            print("- " + err)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

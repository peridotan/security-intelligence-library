# Security Intelligence Candidate Collection

This is Phase 2A of the Security Intelligence Library automation.

## Goal

Collect recent items from trusted primary-source feeds and route them through the
existing pull-request review flow:

Source feed → candidate normalization → duplicate filtering → review PR → email → human approval

This phase deliberately does **not** generate or publish article prose.

## Run manually

GitHub:

1. Actions
2. Collect Security Intelligence Candidates
3. Run workflow
4. Choose the lookback window (default: 7 days)

If new candidates are found, the workflow creates a review PR and requests review
from the repository owner. GitHub sends the normal review-request notification.

## Source registry

Sources are configured in:

`config/intelligence_sources.yml`

Initial sources are intentionally limited to:

- NIST Cybersecurity RSS
- CISA Cybersecurity Advisories RSS

A source failure is recorded as a warning and does not prevent other sources from
being collected.

## Duplicate filtering

The collector scans existing `docs/**/*.md` files and excludes candidate URLs that
already appear in Library content.

## Generated review files

The PR contains:

- `.automation-review/candidates-<run-id>.json`
- `.automation-review/candidates-<run-id>.md`

The JSON file is intentionally machine-readable so the next phase can consume
approved candidate sets and generate article drafts.

## Review meaning

For Phase 2A:

- Approve + merge: candidate set is accepted for the future drafting phase.
- Request changes: candidate selection needs adjustment.
- Close without merge: discard this candidate set.

Merging this PR does not publish any Library article because generated review files
are outside `docs/`.

## Next phase

Phase 2B will consume approved candidate JSON and generate Library article drafts.
Those drafts will be sent through a second human-review PR before publication.

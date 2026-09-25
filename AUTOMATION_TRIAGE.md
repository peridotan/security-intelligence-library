# Security Intelligence Triage

Phase 2A.5 adds deterministic routing between source collection and human review.

## Routes

- `library`: eligible for the future Security Intelligence Library article-drafting phase
- `vulnerability`: product/CVE-level intelligence better suited to Vulnerability Intelligence
- `watch`: potentially important, but held for human review before drafting

A route is a workflow recommendation, not a publication decision.

## Current deterministic policy

### NIST Cybersecurity

Default route: `library`

NIST guidance and standards are treated as Library candidates, still subject to human review.

### CISA CSAF IT

Default route: `vulnerability`

The CSAF detail document is fetched and enriched with:

- CVE count and IDs
- maximum CVSS base score found
- SSVC Exploitation (`None`, `PoC`, `Active`)
- CISA Risk Evaluation / summary text

Overrides:

- SSVC `Active` → `library`
- SSVC `PoC` → `watch`
- max CVSS >= 9.0 → `watch`
- 3 or more vulnerabilities in one advisory → `watch`
- otherwise → `vulnerability`

These thresholds are intentionally conservative and configurable in
`config/intelligence_triage.yml`.

## Human approval meaning

Approve + merge confirms the candidate metadata and recommended routing.

It does **not** publish an article.

The next phase will consume only merged candidates with:

`triage.draft_eligible: true`

to generate article drafts for a second human review.

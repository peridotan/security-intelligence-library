# Source Registry v2 — Japanese Primary Sources Pilot

Status: **Draft PR — do not merge before live probe and human review.**

## Goal

Extend discovery to Japanese primary sources without automatic publication.
Regression example: https://www.nict.go.jp/press/2026/10/13-1.html

## Sources and methods

| Source ID | Official URL | Method | Caveat |
| --- | --- | --- | --- |
| nict-security-press | https://www.nict.go.jp/press/ | HTML listing | Filter security-related press titles; uses dated official press URLs. This covers the A2B warning, not every CYNEX report. |
| ipa-security-alerts | https://www.ipa.go.jp/security/rss/alert.rdf | RSS/RDF | Product-specific notices may belong in Vulnerability Intelligence. |
| jpcert-alerts-jp | https://www.jpcert.or.jp/rss/jpcert.rdf | RSS/RDF | Supplements existing English source; avoid high-volume combined JVN feed. |
| nco-security-news | https://www.cyber.go.jp/news/list/index.html | HTML listing | Provisional adapter. Validate site access and markup from GitHub Actions. |

All new sources use the existing default Watch route. No new articles
are published without human review.

## Safety and known limitations

- The HTML collectors do not execute JavaScript, follow linked pages,
  or guess publication dates. First-party hosts are enforced.
- NICT non-press CYNEX reports are not comprehensively covered.
- NCO parsing is provisional; if the site blocks CI or markup differs,
  correct the parser or split NCO into a later PR before merging.
- Exact URL deduplication remains; semantic deduplication is a future task.
- Scheduled collection currently logs source errors but does not create an
  error-only PR when there are no candidates.

## Validation

Offline: run Python unittest discovery against scripts/test_official_html_sources.py
and Python compileall for the three changed collection scripts.

Online: run Python scripts/probe_japan_sources.py from the GitHub Actions runner.
The PR workflow validate-japan-sources.yml performs both checks, fails for
unreachable or zero-item sources, and reports counts and source errors.

## Acceptance criteria

1. All four live-source probes complete successfully.
2. Check representative official titles, dates, and URLs, including NICT A2B.
3. Review expected noise, duplicate candidates, and Watch routing.
4. Keep the PR as Draft until review. If NCO fails, fix or defer NCO separately.

After approval, run the usual seven-day collection and monitor source utility
for four weeks before expanding the registry further.

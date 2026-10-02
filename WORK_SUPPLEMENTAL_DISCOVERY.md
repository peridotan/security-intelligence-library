# ChatGPT Work Supplemental Discovery

This document is the source-of-truth instruction for public-web discovery that supplements
`config/intelligence_sources.yml`. Its purpose is to find high-signal developments missed by
configured feeds without creating duplicate Library articles or repeating accepted triage.

## Scope

Search only for recent developments in:

- Cybersecurity
- Identity Security
- AI Security
- Regulation
- Risk Management

Prefer primary sources, regulators, national CERTs, standards bodies, security research teams,
and first-party vendor research. Supplemental discovery is not a replacement for configured
feeds.

## Required pre-checks

Before searching the public web:

1. Read `config/intelligence_sources.yml` and treat enabled feeds as already-covered discovery
   channels.
2. Inspect `docs/` for existing published or draft articles related to the same event, report,
   regulation, vulnerability, actor, campaign, standard, or management theme.
3. Inspect merged `.automation-review/candidates-*.json` and promotion records. A candidate
   already accepted as `library`, `vulnerability`, or `watch` is not a new discovery.
4. Search the public web only after these repository checks.

Exact URL matching is necessary but not sufficient. Compare title, organization, publication,
report/advisory name, CVE identifiers, regulation/standard identifiers, affected technology,
and the substantive event or finding.

## Content relation

Every discovered item must receive exactly one `content_relation` value:

- `new` — materially new intelligence not represented in docs or accepted triage.
- `update-existing` — new facts, final guidance, changed status, new exploitation evidence, or
  another meaningful development that belongs in an existing Library article. Record the
  existing article path.
- `duplicate` — substantially the same source/event/finding is already represented. Do not
  propose a new article.
- `watch` — potentially relevant but not yet strong enough for Library or Vulnerability action.
- `vulnerability` — product/CVE-level intelligence better handled by Vulnerability Intelligence.

When uncertain between `new` and `update-existing`, prefer `update-existing` and surface the
existing article for human review. Do not silently suppress a candidate solely because keywords
look similar.

## Route decision

After the content-relation check, suggest one route:

- `library` for durable security-management intelligence with broader organizational value.
- `vulnerability` for CVE/product/exploitation-centered intelligence.
- `watch` for emerging, narrow, vendor-specific, or insufficiently mature signals.

A route does not override `content_relation`. In particular, `update-existing + library` means
update the identified Library article rather than create a new one.

## Output gate

Return at most five high-signal candidates. Exclude `duplicate` items from the candidate list,
but mention material duplicates in a short exclusion note when that explains why an obvious
source was not selected.

For each retained candidate include:

- title
- source
- publication date
- URL
- category
- why it matters for Japanese companies or security management
- `content_relation`
- existing article path when `update-existing`
- suggested route: `library`, `vulnerability`, or `watch`
- short rationale

Do not modify GitHub, publish an article, or merge anything during discovery. Human review remains
the publication gate.

If no worthwhile non-duplicate discoveries remain, report:

`No supplemental candidates were found.`

## Example

If a newly found ENISA page discusses ENISA Threat Landscape 2026 and
`docs/cybersecurity/enisa-threat-landscape-2026-dependencies.md` already covers that report, the
candidate is not `new`. Classify it as `update-existing` only if it adds material new information;
otherwise exclude it as `duplicate`.

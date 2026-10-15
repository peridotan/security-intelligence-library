# Evidence Review v1 — claim-level traceability and publication gate

## Goal and limitations

Every **new** published Security Intelligence Library article must have a
machine-readable, **human-approved** Evidence Review record for material claims.
This separates verified source facts, first-party/vendor assertions, and
Library interpretation so the editor can focus on substantive exceptions.

A passing validation **does not prove a statement is true or that a named
person actually reviewed it**. CI validates structure, traceability and the
recorded approval state, not remote source content or reviewer identity.
The human editor must open primary sources and inspect the cited passages.

## Work-to-GitHub workflow

1. After an eligible Triage PR merges, ChatGPT Work drafts the article under
   the requirements of WORK_AI_DRAFTING.md.
2. For each article draft, Work also produces an Evidence Review JSON artifact
   based on templates/evidence-review-template.json. The reviewer summary
   must identify material claims and unresolved items.
3. Keep review.status = pending while preparing the draft; Work never sets
   approved, and never invents a human reviewer or date.
4. A human inspects each material source claim against the actual primary
   source, corrects/removes unsupported assertions, and then records
   review.status = approved, reviewed_by and reviewed_at.
5. When submitting a new published article at docs/<collection>/<slug>.md,
   commit its matching dossier under review/evidence/<slug>.json in the same
   PR. Evidence sidecars live outside docs/ and are not rendered on the site.
6. Pull-request CI validates the dossier before the existing required
   quality gate passes. Merge and publication remain separate human choices.

## Schema v1

| Field | Values / purpose |
| --- | --- |
| schema_version | Integer 1 |
| article_path | Repository-relative docs/<collection>/<slug>.md |
| review.status | pending, changes_requested, approved |
| review.reviewed_by | Human reviewer handle, required for approved |
| review.reviewed_at | Real YYYY-MM-DD date, required for approved |
| claims[].id | Stable C01, C02, etc., unique per dossier |
| claims[].statement | Statement to check against the article |
| claims[].section | Article section heading such as ## 何が起きているのか |
| claims[].importance | material or supporting |
| claims[].classification | source_fact, source_claim, library_assessment |
| claims[].verification | As explained below |
| claims[].source | HTTPS URL, precise locator, accessed_at, optional published_at |
| claims[].rationale | Required for library_assessment |

At least one **material** claim is required. Include all consequential
conclusions, dates, affected systems, obligations and recommendations;
do not list every trivial sentence.

### Classification and verification

- **source_fact**: a concrete statement supported directly by the
  cited first-party source, e.g. the publication date or documented requirement.
  A vendor's product-performance assertion should not be recast as an
  independently confirmed fact.
- **source_claim**: an organization's estimate, assertion, prediction or
  interpretation, even if accurately attributed to its official publication.
- **library_assessment**: Library analysis, recommendation or inference,
  with an explicit rationale and without pretending it was a sourced fact.

Source-backed claims require the real source URL, a precise passage locator,
and the actual date accessed. Use **verified** only after reading the cited
passage; otherwise use **needs_review** or **unsupported**. A verified
source_claim means the attribution is faithful, not that the claim is
independently true. A library_assessment must use **not_applicable** for
verification and carry a substantive rationale.

A draft can have unresolved source-backed claims while review.status is
pending or changes_requested. An approved dossier **cannot** contain any
needs_review or unsupported source-backed claim. The human must correct
or remove those claims rather than automatically reclassifying them.

Do not guess a primary-source publication date: omit published_at when
unknown. Avoid reproducing lengthy source quotations. A locator can be
a document section, page, figure, table or a specific paragraph heading.

The provided template contains placeholders; **replace them with actual
sources/dates before committing it to review/evidence/**.

## CI enforcement and backward compatibility

The validator checks JSON format, path safety, claim IDs, source URL/date
syntax, classifications, review metadata, unresolved claims and article
section references. It also finds **newly added** published Markdown articles
in the five production collections and requires matching approved evidence.

Existing published articles are **not** forced into retroactive dossiers.
Monthly/quarterly syntheses are not covered by this first iteration.
Evidence dossiers added voluntarily for existing articles are validated.
A later phase can expand enforcement to major updates and syntheses.

This is a structural check only, not a semantic or network-based source audit.

## Reproduce locally

From the repository root, with an available origin/main Git ref:

    python -m unittest discover -s scripts -p "test_evidence_review.py" -v
    python scripts/check_evidence_review.py --base-ref origin/main

Without the base-ref flag, the script validates existing dossiers but
does not demand new-article coverage. See PR_QUALITY_GATE.md for full CI.

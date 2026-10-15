# Pull Request Quality Gate

The GitHub Actions workflow at `.github/workflows/pr-quality.yml` validates **every
pull request** to Security Intelligence Library before a human decides whether
to merge it. It complements the existing `docs.yml` workflow, which deploys
GitHub Pages only after a push to `main`.

## What runs

1. Check out the proposed PR (using the regular `pull_request` event), and
   publicly available Threat Investigation reference data.
2. Install the same Python dependencies used by publication.
3. Run offline regression tests for official first-party source adapters
   and Evidence Review dossiers.
4. Validate claim-level Evidence Review records, and require a human-approved
   dossier for **newly published articles**, including Draft-to-published
   transitions (legacy published articles remain exempt).
5. Generate the article/category indexes and intelligence context index.
6. Synchronize article metadata.
7. Validate article fields, sections, evidence metadata, links and media rights.
8. Validate cross-repository Suite handoff contracts.
9. Fail if generated `docs/` changes or untracked generated files have not
   been included in the PR.
10. Build the site with `zensical build --clean --strict`.
11. Check rendered HTML and internal links.

The job is **read-only** (`contents: read`); it cannot merge PRs, deploy
GitHub Pages, publish articles, or push generated files. It uses no application
API key or PR write token.

## Reproduce the checks before submitting a PR

From the repository root, after installing `requirements.txt`:

```bash
python -m unittest discover -s scripts -p 'test_official_*_sources.py' -v
python -m unittest discover -s scripts -p 'test_evidence_review.py' -v
python scripts/check_evidence_review.py --base-ref origin/main
python scripts/build_indexes.py
python scripts/build_context_index.py
python scripts/sync_article_metadata.py
python scripts/check_content.py
python scripts/check_suite_handoff.py --threat-data .suite/threat-investigation-dashboard/data/dashboard.json
git diff --check
zensical build --clean --strict
python scripts/check_generated_site.py
```

The Suite check requires a local checkout of
`peridotan/threat-investigation-dashboard` at
`.suite/threat-investigation-dashboard`; GitHub Actions checks it out
automatically. For a local run, this is the same reference dataset used by
`docs.yml`.

**Important:** after running the generators, commit any intentional
`docs/` changes to the PR branch and rerun the checks. CI intentionally
fails when generated output is missing or stale.

## Handling failures

Inspect the failed step in the PR's `Checks` tab. For example:

- **Evidence Review:** include the reviewed dossier for each new published
  article, fix unresolved material claims and record human approval.
  See `EVIDENCE_REVIEW.md`.
- **Content quality:** fix missing required sections / metadata and rerun.
- **Generated docs:** run the index and metadata generators, commit the
  resulting `docs/` changes, and push again.
- **Suite handoff:** correct actor or MITRE ATT&CK relationships.
- **Strict build / generated HTML:** correct broken links or HTML markup.
- **Source parser regression:** fix the relevant adapter or its fixtures.

Pushing a fix automatically reruns the workflow.

## Enforcing the result

The workflow reports a check named
`Content, indexes, Suite and site` under
`Validate Security Intelligence PR`.

**A successful workflow is not, by itself, a mandatory merge gate.**
To actually block merging on red checks, configure GitHub repository branch
protection or rulesets on `main` to require that status check, after its
first successful run. This requires repository settings access and must be
configured separately.

The existing Japanese-source live validation workflow stays separate: its
network-dependent checks run only for relevant source-code changes, while
this content validation runs for all PRs.

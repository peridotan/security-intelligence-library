# Security Intelligence Library - Review Approval Workflow

This is the first building block for automated article, monthly, and quarterly publishing.

## Goal

Generated content is not published directly. Automation creates a pull request and requests a human review from the repository owner.

Flow:

1. A generator changes one or more files.
2. `scripts/open_review_pr.sh` creates a dedicated branch and pull request.
3. `scripts/request_pr_review.sh` requests a GitHub review from the repository owner.
4. GitHub sends a `review_requested` notification according to the reviewer's notification settings.
5. The reviewer opens the pull request and chooses **Review changes -> Approve** or requests changes.
6. Merge remains a human action for the first phase.

## One-time repository setting

For the smoke test and future automation to create pull requests with `GITHUB_TOKEN`, enable:

`Settings -> Actions -> General -> Workflow permissions -> Allow GitHub Actions to create and approve pull requests`

The workflow itself still grants only the permissions it needs:

- `contents: write`
- `pull-requests: write`

## Smoke test

After this change is on `main`:

1. Open the repository on GitHub.
2. Open **Actions**.
3. Select **Review Request Smoke Test**.
4. Choose **Run workflow**.
5. GitHub Actions creates a test pull request authored by `github-actions[bot]` and requests review from the repository owner.
6. Open the review-request notification, inspect the PR, and choose **Review changes -> Approve**.
7. Close the smoke-test PR without merging it.

The smoke-test file lives outside `docs/`, so it is not part of the published Security Intelligence Library site.

## Reuse from article/monthly/quarterly generators

A future generator only needs to create or update its Markdown files and then run:

```bash
export GH_TOKEN="$GITHUB_TOKEN"
export GITHUB_REPOSITORY="owner/repository"
export GITHUB_REPOSITORY_OWNER="owner"
export REVIEW_TITLE="[Review] September 2026 Security Intelligence"
export REVIEW_BODY="Automated draft. Please review sources, analysis, and publication readiness."
export COMMIT_MESSAGE="Generate September 2026 Security Intelligence draft"

scripts/open_review_pr.sh
```

This keeps the approval path the same for article drafts, monthly reviews, and quarterly reviews.

## Email behavior

The review request itself is sent through GitHub notifications. Whether it also arrives by email depends on the reviewer's GitHub notification settings. A custom SMTP/Zoho notification can be added later as a fallback without changing the PR approval model.

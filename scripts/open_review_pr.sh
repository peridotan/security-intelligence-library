#!/usr/bin/env bash
set -euo pipefail

BASE_BRANCH="${BASE_BRANCH:-main}"
REVIEWER="${REVIEWER:-${GITHUB_REPOSITORY_OWNER:-}}"
REVIEW_TITLE="${REVIEW_TITLE:-Security Intelligence review request}"
REVIEW_BODY="${REVIEW_BODY:-Automated Security Intelligence Library review request.}"
COMMIT_MESSAGE="${COMMIT_MESSAGE:-Prepare Security Intelligence review}"
BRANCH_PREFIX="${BRANCH_PREFIX:-automation/review}"

if [[ -z "${GITHUB_REPOSITORY:-}" ]]; then
  echo "GITHUB_REPOSITORY is required (owner/repo)." >&2
  exit 2
fi

if [[ -z "${GH_TOKEN:-}" ]]; then
  echo "GH_TOKEN is required." >&2
  exit 2
fi

if [[ -z "$REVIEWER" ]]; then
  echo "REVIEWER is required." >&2
  exit 2
fi

if [[ -z "$(git status --porcelain)" ]]; then
  echo "No changes to submit for review." >&2
  exit 3
fi

RUN_SUFFIX="${GITHUB_RUN_ID:-$(date -u +%Y%m%d%H%M%S)}"
RUN_ATTEMPT="${GITHUB_RUN_ATTEMPT:-1}"
BRANCH="${BRANCH_PREFIX}-${RUN_SUFFIX}-${RUN_ATTEMPT}"

if ! git config user.name >/dev/null 2>&1; then
  git config user.name "github-actions[bot]"
fi
if ! git config user.email >/dev/null 2>&1; then
  git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
fi

git checkout -b "$BRANCH"
git add -A
git commit -m "$COMMIT_MESSAGE"
git push --set-upstream origin "$BRANCH"

PR_URL=$(gh pr create \
  --base "$BASE_BRANCH" \
  --head "$BRANCH" \
  --title "$REVIEW_TITLE" \
  --body "$REVIEW_BODY")

PR_NUMBER=$(gh pr view "$BRANCH" --json number --jq '.number')

"$(dirname "$0")/request_pr_review.sh" "$PR_NUMBER" "$REVIEWER"

echo "Created review PR: ${PR_URL}"

if [[ -n "${GITHUB_OUTPUT:-}" ]]; then
  echo "pr_number=${PR_NUMBER}" >> "$GITHUB_OUTPUT"
  echo "pr_url=${PR_URL}" >> "$GITHUB_OUTPUT"
  echo "branch=${BRANCH}" >> "$GITHUB_OUTPUT"
fi

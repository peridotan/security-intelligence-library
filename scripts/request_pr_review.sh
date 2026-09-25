#!/usr/bin/env bash
set -euo pipefail

PR_NUMBER="${1:-}"
REVIEWER="${2:-${REVIEWER:-${GITHUB_REPOSITORY_OWNER:-}}}"
REPOSITORY="${GITHUB_REPOSITORY:-}"

if [[ -z "$PR_NUMBER" ]]; then
  echo "Usage: $0 <pr-number> [reviewer]" >&2
  exit 2
fi

if [[ -z "$REPOSITORY" ]]; then
  echo "GITHUB_REPOSITORY is required (owner/repo)." >&2
  exit 2
fi

if [[ -z "$REVIEWER" ]]; then
  echo "Reviewer is required." >&2
  exit 2
fi

if [[ -z "${GH_TOKEN:-}" ]]; then
  echo "GH_TOKEN is required." >&2
  exit 2
fi

echo "Requesting review from ${REVIEWER} for ${REPOSITORY}#${PR_NUMBER}"

gh api \
  --method POST \
  -H "Accept: application/vnd.github+json" \
  "/repos/${REPOSITORY}/pulls/${PR_NUMBER}/requested_reviewers" \
  -f "reviewers[]=${REVIEWER}" \
  >/dev/null

echo "Review requested: ${REVIEWER}"

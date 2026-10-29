# Draft Review — 初期侵入の主要5類型 ― Unit 42の2026年9月観測から考える防御優先順位

- Status: **Draft / Human review pending**
- Origin: merged triage PR #43 (2026-10-19)
- Article file: `drafts/cybersecurity/unit42-initial-access-vectors-september-2026.md`
- Evidence: `drafts/evidence/unit42-initial-access-vectors-september-2026.json`
- Intended published paths: `docs/cybersecurity/unit42-initial-access-vectors-september-2026.md`, `review/evidence/unit42-initial-access-vectors-september-2026.json`
- Primary source: https://unit42.paloaltonetworks.com/top-5-initial-access-vectors-september-2026/
- Material claims: C01, C02, C03, C04, C05
- Evidence status: `pending` (not approved)

## Human reviewer checklist

- [ ] Open and inspect the primary source passages for each material claim.
- [ ] Unit 42が示す主要5類型の性質と観測範囲を、人間が原文Table 1で再確認する。日本全体の順位と読み替えない。
- [ ] Compare the full article with the latest published Library docs for duplication and link validity.
- [ ] Confirm Japanese implications are Library analysis, not attributed vendor facts.
- [ ] Confirm intended article path, metadata, references, and rendered site preview.
- [ ] Record the real human reviewer and review date only after material-claim review.
- [ ] Do not publish, merge, or change to `approved` during Draft stage.

## Evidence承認意思の記録（2026-10-29 JST）

- **明示的な意思表明**：依頼者はChatGPTの会話で「PR #49のUnit 42 5件とAWS ML-DSA 14件、合計19件のEvidenceを承認します。記事公開・マージはまだ行わないでください。」と明示した。
- **この記事の対象**：Unit 42 — 5件（C01–C05）。PR #49の現行Evidence Claimに対する承認意思として記録する。
- **GitHub接続アカウント**：`peridotan`。接続アカウントと依頼者の同一性を独立検証した記録ではない。
- **操作の境界**：今回の承認は**記事の公開・掲載パスへの移動・PR #49のマージの承認ではない**。 `ARTICLE_WORKFLOW.md` に基づき、正式な公開承認が出るまで `drafts/evidence/` の `review.status: pending`、`reviewed_by: null`、`reviewed_at: null` を維持する。
- **変更時の扱い**：Claimまたは記事本文に実質的な変更が加わった場合、その差分について再確認が必要。
- **承認の意味**：会話上の承認意思を記録したもので、一次情報の独立検証、公開承認、GitHub PRレビューの自動承認を装うものではない。

# Draft Review — ML-DSAでSoftware Supply Chainを守る ― AWSにおける耐量子署名とAlgorithm Governance

- Status: **Draft / Human review pending**
- Origin: merged triage PR #43 (2026-10-19)
- Article file: `drafts/cybersecurity/aws-mldsa-supply-chain-governance.md`
- Evidence: `drafts/evidence/aws-mldsa-supply-chain-governance.json`
- Intended published paths: `docs/cybersecurity/aws-mldsa-supply-chain-governance.md`, `review/evidence/aws-mldsa-supply-chain-governance.json`
- Primary source: https://aws.amazon.com/blogs/security/quantum-resistant-signing-on-aws-part-2-enforce-your-ml-dsa-algorithm-policy-with-scps-and-iam/
- Material claims: C01–C14
- Evidence status: `pending` (not approved)

## Human reviewer checklist

- [ ] Open and inspect the primary source passages for each material claim.
- [ ] AWS KMS・Private CAの指定値、IAM Roles Anywhere適用範囲、SCPがManagement Accountには適用されない点を人間が確認する。
- [ ] AWS Part 2のDeny-listが将来追加されるVariantを自動的にはブロックしない問題、default-denyとのTrade-offを人間が確認する。
- [ ] 米国NSSでCNSA 2.0を適用する場合のML-DSA-87限定を、商用向け65/87の例や日本の一般義務と混同しない。
- [ ] Compare the full article with the latest published Library docs for duplication and link validity.
- [ ] Confirm Japanese implications are Library analysis, not attributed vendor facts.
- [ ] Confirm intended article path, metadata, references, and rendered site preview.
- [ ] Record the real human reviewer and review date only after material-claim review.
- [ ] Do not publish, merge, or change to `approved` during Draft stage.

## Evidence承認意思の記録（2026-10-29 JST）

- **明示的な意思表明**：依頼者はChatGPTの会話で「PR #49のUnit 42 5件とAWS ML-DSA 14件、合計19件のEvidenceを承認します。記事公開・マージはまだ行わないでください。」と明示した。
- **この記事の対象**：AWS ML-DSA — 14件（C01–C14）。PR #49の現行Evidence Claimに対する承認意思として記録する。
- **GitHub接続アカウント**：`peridotan`。接続アカウントと依頼者の同一性を独立検証した記録ではない。
- **操作の境界**：今回の承認は**記事の公開・掲載パスへの移動・PR #49のマージの承認ではない**。 `ARTICLE_WORKFLOW.md` に基づき、正式な公開承認が出るまで `drafts/evidence/` の `review.status: pending`、`reviewed_by: null`、`reviewed_at: null` を維持する。
- **変更時の扱い**：Claimまたは記事本文に実質的な変更が加わった場合、その差分について再確認が必要。
- **承認の意味**：会話上の承認意思を記録したもので、一次情報の独立検証、公開承認、GitHub PRレビューの自動承認を装うものではない。

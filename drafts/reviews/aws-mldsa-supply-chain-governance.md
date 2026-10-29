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

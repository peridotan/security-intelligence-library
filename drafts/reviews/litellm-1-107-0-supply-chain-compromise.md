# Evidence Review／編集レビュー表 — LiteLLM 1.107.0 Supply Chain Compromise

- 出自：2026-10-29にマージされた [Triage PR #46](https://github.com/peridotan/security-intelligence-library/pull/46) の Library新規記事候補
- 記事：`drafts/ai-security/litellm-1-107-0-supply-chain-compromise.md`
- 証拠：`drafts/evidence/litellm-1-107-0-supply-chain-compromise.json`
- 公開予定パス：`docs/ai-security/litellm-1-107-0-supply-chain-compromise.md`
- Evidence公開予定パス：`review/evidence/litellm-1-107-0-supply-chain-compromise.json`
- 重要Claim：C01〜C09
- 状態：**記事Draft、Evidence pending、公開未承認**

## 編集者が確認する事項

- [ ] LiteLLMの[2026-10-23 Canonical RCA](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)と、当時の[Incident Report](https://docs.litellm.ai/blog/security-incident-oct-21-2026)を区別する。Incident Report中の旧仮説をRCAより優先しない
- [ ] PyPIとContainerのTag／Digest／UTC時間帯、Private Enterprise Releaseの扱いを一次情報で確認
- [ ] Microsoftの[Payload解析](https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks/)と、LiteLLMの攻撃者アクセス経路に関する報告を区別
- [ ] Python Startup HooksのT1546.018、T1195.001のMITRE mappingがMicrosoftのSource-labeledと一致することを確認
- [ ] Unix Loaderの追加コード実行が確認されていないことを再確認
- [ ] 感染した環境でPython/pipを実行する検査が危険な理由と、Credential Rotation推奨を確認
- [ ] 既存のLiteLLM Runtime侵害記事との役割分担と関連記事リンクを確認
- [ ] 記事本文、Evidence Claim、出典、すべての編集指摘を確認した人間だけが後工程で承認者・承認日を記録する

**このDraft PRでは公開・マージ・Evidence approved化を行わない。**

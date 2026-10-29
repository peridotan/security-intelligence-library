# Evidence Review／編集レビュー表 — LiteLLM 1.107.0 Supply Chain Compromise

- 出自：2026-10-29にマージされた [Triage PR #46](https://github.com/peridotan/security-intelligence-library/pull/46) の Library新規記事候補
- 記事：`drafts/ai-security/litellm-1-107-0-supply-chain-compromise.md`
- 証拠：`drafts/evidence/litellm-1-107-0-supply-chain-compromise.json`
- 公開予定パス：`docs/ai-security/litellm-1-107-0-supply-chain-compromise.md`
- Evidence公開予定パス：`review/evidence/litellm-1-107-0-supply-chain-compromise.json`
- 重要Claim：C01〜C09
- 状態：**Evidence承認済み・掲載準備中・PR未マージ**

## 編集者が確認する事項

- [ ] LiteLLMの[2026-10-23 Canonical RCA](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)と、当時の[Incident Report](https://docs.litellm.ai/blog/security-incident-oct-21-2026)を区別する。Incident Report中の旧仮説をRCAより優先しない
- [ ] PyPIとContainerのTag／Digest／UTC時間帯、Private Enterprise Releaseの扱いを一次情報で確認
- [ ] Microsoftの[Payload解析](https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks/)と、LiteLLMの攻撃者アクセス経路に関する報告を区別
- [ ] Python Startup HooksのT1546.018、T1195.001のMITRE mappingがMicrosoftのSource-labeledと一致することを確認
- [ ] Unix Loaderの追加コード実行が確認されていないことを再確認
- [ ] 感染した環境でPython/pipを実行する検査が危険な理由と、Credential Rotation推奨を確認
- [ ] 既存のLiteLLM Runtime侵害記事との役割分担と関連記事リンクを確認
- [ ] 記事本文、Evidence Claim、出典、すべての編集指摘を確認した人間だけが後工程で承認者・承認日を記録する

**2026-10-29のEvidence承認および公開承認に基づき、Evidenceと記事を掲載パスに移行しました。マージ・Pagesへの反映はまだ行っていません。**

## Evidence承認意思の記録（2026-10-29 JST）

- **承認意思の表明**：依頼者はChatGPTの会話で「Evidenceも承認」と明示。直前の確認質問は「各Claimを一次情報と照合済みで承認するという意味か」であり、これへの回答として受領した。
- **対象範囲**：この記事のEvidence Claim **9件**（現行Draft PR #50の版）。
- **認証済みGitHub連携アカウント**：`peridotan`。会話内で独立した本人確認を行ったわけではないため、GitHubアカウントと依頼者の同一性を独立検証した記録ではない。
- **変更しない承認ゲート**：この記録は**記事公開、PR #50のマージ、`published`への変更の承認ではない**。リポジトリの`ARTICLE_WORKFLOW.md`に従い、別途正式な公開承認を得るまで`drafts/evidence/`の`review.status = pending`、`reviewed_by = null`、`reviewed_at = null`を維持する。正式な公開段階で承認者として記録するハンドル・日付を確定する。
- **有効範囲**：後から本文やClaimが実質変更された場合、その変更分は再レビュー対象とする。

## 公開用ステージング（2026-10-29）

- 承認者：`peridotan`（GitHub接続の認証済みアカウント）
- 承認記録：ChatGPT会話で全23件のEvidence承認に続き、2記事の公開承認を明示。
- 記事：`docs/ai-security/litellm-1-107-0-supply-chain-compromise.md`（`status: published`、`review_status: Current`）。
- 証拠：`review/evidence/litellm-1-107-0-supply-chain-compromise.json`（`review.status: approved`、`reviewed_by: peridotan`、`reviewed_at: 2026-10-29`）。
- **この変更はPR作業ブランチ内のみ**。マージ前には最新のCI、生成インデックス、サイトプレビューと最終差分を確認。

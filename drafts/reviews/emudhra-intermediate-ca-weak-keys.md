# Evidence Review／編集レビュー表 — eMudhra中間CAの弱鍵問題

- 出自：2026-10-29にマージされた [Triage PR #46](https://github.com/peridotan/security-intelligence-library/pull/46) の Library新規記事候補
- 記事：`drafts/cybersecurity/emudhra-intermediate-ca-weak-keys.md`
- 証拠：`drafts/evidence/emudhra-intermediate-ca-weak-keys.json`
- 公開予定パス：`docs/cybersecurity/emudhra-intermediate-ca-weak-keys.md`
- Evidence公開予定パス：`review/evidence/emudhra-intermediate-ca-weak-keys.json`
- 重要Claim：C01〜C14（C10はCloudflare限定、C12/C13はRootの影響とOkta、C14はApple CLI）
- 状態：**記事Draft、Evidence pending、公開未承認**

## 編集者が確認する事項

- [ ] Google、Mozilla、Apple、Cloudflare、Okta/Auth0によるBlock・Distrustの日時・適用範囲を各一次情報で確認
- [ ] [eMudhraの2026-10-28 Update 6](https://emudhra.com/en/post/certificate-security-incident)の約30,800件という数字は「信頼解除されたRoot配下のG3階層の発行済み証明書」であり、「弱い8 Intermediateからの発行」ではない点を確認（**今回補足した重要点**）
- [ ] eMudhraのKey Wrap/Unwrap原因説明や顧客影響・未悪用評価は、当事者の発言として扱い、最終RCAと断定しない
- [ ] AppleのTLS向け6 Intermediate（Cross-sign含む12証明書）とCode Signing向け2 Intermediateの区別を確認
- [ ] Certificateの誤発行・Server Impersonationの**潜在能力**と、実際に観測された悪用・侵害を区別する
- [ ] AppleのmacOSコマンドラインツール（curl / git / /etc/ssl/cert.pem）の例外と更新状況を一次情報で確認
- [ ] BrowserだけでなくAPI Client、Java/Python、Container、Custom Trust Store、Offline装置の対処要否を確認
- [ ] 正当Certificateの接続障害回避と、安易なTLS検証無効化の禁止を併記
- [ ] 既存PQC/TLS記事等との重複、および外部リンクを確認
- [ ] 14 Claimsの一次情報を人間が再検証した後にのみ、後工程でapprovedとする

**このDraft PRでは公開・マージ・Evidence approved化を行わない。**

## Evidence承認意思の記録（2026-10-29 JST）

- **承認意思の表明**：依頼者はChatGPTの会話で「Evidenceも承認」と明示。直前の確認質問は「各Claimを一次情報と照合済みで承認するという意味か」であり、これへの回答として受領した。
- **対象範囲**：この記事のEvidence Claim **14件**（現行Draft PR #50の版）。
- **認証済みGitHub連携アカウント**：`peridotan`。会話内で独立した本人確認を行ったわけではないため、GitHubアカウントと依頼者の同一性を独立検証した記録ではない。
- **変更しない承認ゲート**：この記録は**記事公開、PR #50のマージ、`published`への変更の承認ではない**。リポジトリの`ARTICLE_WORKFLOW.md`に従い、別途正式な公開承認を得るまで`drafts/evidence/`の`review.status = pending`、`reviewed_by = null`、`reviewed_at = null`を維持する。正式な公開段階で承認者として記録するハンドル・日付を確定する。
- **有効範囲**：後から本文やClaimが実質変更された場合、その変更分は再レビュー対象とする。

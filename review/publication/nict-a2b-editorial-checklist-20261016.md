# NICT A2B攻撃 — 正式掲載の編集レビュー（2026-10-16）

## このPRの位置づけ

記事を `docs/cybersecurity/nict-a2b-backend-api-security.md` に配置した**掲載準備用のDraft PR**です。現時点では次の状態です。

- 記事：`status: draft`、`review_status: Needs Review`。記事は**まだ公開承認されていません**。
- Evidence Review：`review/evidence/nict-a2b-backend-api-security.json` に13件の根拠を記載。全13件のAIによる出典照合状態は記録済みですが、`review.status: pending`、`reviewed_by: null`、`reviewed_at: null` です。
- このPR自体をマージすると、下書きページがビルドされて直接URLで閲覧できる可能性があります。**人間のレビューを終えるまでPRをマージしない**でください。
- この資料とレビューJSONはパブリックGitHubリポジトリで閲覧可能であり、機密・個人情報を含めないようにしています。

## 編集チェックリスト

- [ ] この題材をLibraryのCybersecurity記事として採用することを最終決定した。
- [ ] 出典NICT/LETTICE Rev 1.1（2026年10月13日、7ページ）について重要主張（特にC02、C05、C07、C11、C12）の本文・図・表を自分で確認した。
- [ ] **C02**：国内漏えい事案に関連するという**NICTの報告**であり、個々の被害事案の因果関係をLibraryが独立確認したという意味ではないことを確認した（PDF p.1、p.6）。
- [ ] **C05**：AIを使った解析・攻撃工程は図1（p.2）で示されているが、個別事案のAI使用状況の実証データを記事が捏造・断定していないことを確認した。
- [ ] **C07**：SSRF、RCE、SQLインジェクション、IDORはLETTICEが述べる主要な探索・悪用対象（p.3）。全被害事案で全種類を悪用したという断定がないことを確認した。
- [ ] **C11**：ログ調査の起点が2026年8月以降であること（可能なら過去ログも）を確認した（p.4）。
- [ ] **C12**：IoC3件の転記と**IoC一致のみでは侵害を断定できない**旨を確認した（p.6）。
- [ ] Library独自の管理・開発上の推奨がNICTの一次事実と区別されている。
- [ ] 公開日、最終確認日、記事カテゴリ、関連記事・リンク、画像引用の有無を最終確認した。

## 公開を承認したら実施する作業

1. **人間が確認した後でのみ** `review/evidence/nict-a2b-backend-api-security.json` の `review.status` を `approved` に変更し、実際の担当者のGitHubユーザー名等を `reviewed_by` に、日付を `reviewed_at` に記録する。
2. 記事の `status` を `published`、`review_status` を `Current` に変更し、実際の公開日とレビュー日を反映する。
3. 現行の生成処理を実行して派生ファイルをコミットする。

   ```bash
   python scripts/build_indexes.py
   python scripts/build_context_index.py
   python scripts/sync_article_metadata.py
   ```

4. 必須品質チェック `Content, indexes, Suite and site` の成功を確認する。Draft解除後にもActionsが再実行されるので、その結果も確認する。
5. 人間がGitHub PRの最終差分を確認し、**それからマージ**する。GitHub Pagesへの反映は `main` 更新後の別ワークフローで行われる。

## ソース

- NICT/LETTICE 原資料（Rev 1.1、2026年10月13日）：https://cynex.nict.go.jp/pdf/library/lettice/261013-01.pdf
- NICTプレスリリース：https://www.nict.go.jp/press/2026/10/13-1.html
- CYNEX注意喚起：https://cynex.nict.go.jp/library/261013-01.html

## 履歴

資料収集・原稿作成・出典確認の試験履歴： https://github.com/peridotan/security-intelligence-library/pull/39

このチェックリストの作成とCI通過は、人間のEvidence Review承認には代わりません。

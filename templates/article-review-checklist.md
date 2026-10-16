# {{TITLE}} — Evidence Review / 記事編集チェックリスト

対象Draft: `drafts/{{COLLECTION}}/{{SLUG}}.md`  
根拠JSON: `drafts/evidence/{{SLUG}}.json`  
掲載候補: `docs/{{COLLECTION}}/{{SLUG}}.md`

> これは下書き用テンプレートです。AIの根拠照合結果と、人間の承認は別の行為です。

## Draft / 出典確認

- [ ] Triage候補のroute・draft_eligibleを確認した。手動採用の場合は、その事実と採用理由を記録した
- [ ] 同じ出来事についてLibraryの既存記事・下書き・採用済み候補と重複していない
- [ ] 一次資料の発行元、日付、対象範囲、原文の該当箇所（ページ・節・表）を確認した
- [ ] 事実（source_fact）、発行元の主張（source_claim）、Libraryの評価（library_assessment）を分けた
- [ ] 重要な日付・数値・影響範囲・影響対象・引用、法的要件に推測や未確認の断定がない
- [ ] AI利用・効果・被害事例に関して、資料が裏付ける範囲を超えて一般化していない
- [ ] 未解決の `needs_review` / `unsupported` の項目を記録し、公開前に修正・削除した
- [ ] タイトル、Topics、関連リンク、出典URL、媒体の権利を確認した

## 掲載判断（人間）

- [ ] 人間の編集担当者が重要な主張・根拠・提言を点検し、採用を決定した
- [ ] Evidence Review JSONの `review.status` を `approved` に変更した
- [ ] 実在する担当者本人の `reviewed_by` と実際の `reviewed_at` を記録した
- [ ] 人間が確認していない事項は `approved` として記録せず、理由を残した

## 公開用PR

- [ ] 記事を `docs/{{COLLECTION}}/{{SLUG}}.md` に配置した
- [ ] 日付を確認し `status: published`、`review_status: Current` にした
- [ ] `python scripts/build_indexes.py` を実行した
- [ ] `python scripts/build_context_index.py` を実行した
- [ ] `python scripts/sync_article_metadata.py` を実行した
- [ ] 意図した派生ファイルをPRにコミットし、CIの必須チェックが成功した
- [ ] PRの最終差分を確認し、必要ならDraft解除後の再実行結果も確認した
- [ ] 人間がPRをマージした後、GitHub Pagesと記事・脚注・出典リンクの表示を確認した

## 編集メモ・例外事項

- 出典確認で留保した事項：
- 今回は採用を見送った主張：
- 人間による公開判断の根拠：
- 関連するTriage PR / Evidence Draft PR：

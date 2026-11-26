---
name: article-drafting
description: 採用されたLibrary候補や明示されたテーマから、日本語の記事草稿・根拠JSON・人間用レビュー表をセットで用意する時に使う。公開はしない。
license: MIT
---

# Article Drafting

## 参照
`WORK_AI_DRAFTING.md`、`ARTICLE_WORKFLOW.md`、`EVIDENCE_REVIEW.md`、`templates/`、採用済みTriage結果。

## 手順
1. 新規記事か既存記事更新かを確認する。重複記事を新規作成しない。
2. 原資料を開いて数値、日付、仕様、制度、観測主体の範囲を検証する。未確認事項は残す。
3. 原則としてExecutive Summary、なぜ今なのか、何が起きたか、経営影響、日本企業への示唆、推奨アクション、参考情報を用い、既存のテンプレートを優先する。
4. 重要主張を`source_fact`、`source_claim`、`library_assessment`で分け、出典URLと該当節・ページを紐付ける。
5. `scripts/article_workflow.py`を使える場合、`init`と`check`の仕様・上書き禁止を先に確認し、記事・Evidence JSON・レビュー表を用意する。
6. `status: draft`とEvidenceの`review.status: pending`を維持し、未解決主張と人間確認事項を添える。
7. 関連記事の表示名はリンク先の正式タイトルを確認して使用する。Evidence Reviewへ引き渡し、実際の人間の承認を待つ。一括公開は ARTICLE_WORKFLOW.md に従う。

## 禁止
出典・確認日・レビュー担当者・承認を捏造しない。Work／AIによる直接公開やPRマージを実施しない。

## 成果
記事Markdown、Evidence JSON、編集レビュー表、未解決事項。

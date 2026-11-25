---
name: evidence-review
description: 記事草稿や更新記事の重要主張を一次資料に照合し、事実・情報源の主張・独自分析の区別とEvidence Review記録を監査する時に使う。
license: MIT
---

# Evidence Review

## 参照
`EVIDENCE_REVIEW.md`、`ARTICLE_WORKFLOW.md`、`templates/evidence-review-template.json`、対象記事・既存Evidence台帳。

## 手順
1. 重要な事実、数値、日付、法令、脆弱性の悪用状況、引用、提言を抜き出す。
2. 主張ごとに一次情報の該当節、発行日、観測条件、反証・留保を確認する。
3. `source_fact`、`source_claim`、`library_assessment`を正しく区別し、情報源の観測を普遍的事実としない。
4. Evidence JSONに主張ID、原典URL、確認できた部分、未解決点を対応付ける。
5. 形式・構造チェック（条件が整う場合は`python scripts/check_evidence_review.py --base-ref origin/main`）を実行する。CI成功は真偽や実際の人間承認の証明ではない。
6. 修正案、削除候補、未解決事項を人間のレビュー表へまとめる。利用可能な場合は `scripts/batch_review.py --article <Draftパス>`（複数指定可）を使い、承認対象のハッシュと主張一覧を出力する。公開処理は `ARTICLE_WORKFLOW.md` の一括公開手順に従う。
7. 実際の担当者が確認・承認するまでは`review.status: pending`を維持し、`reviewed_by`・`reviewed_at`は捏造しない。

## 禁止
AIが人間の承認者を代行しない。未確認の根拠をverifiedに変えない。

## 成果
主張別チェック結果、根拠対応、未解決事項と人間の判断事項。

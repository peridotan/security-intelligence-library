---
name: intelligence-triage
description: 収集候補の重複、Library・Vulnerability・Watchルート、5軸の暫定重要度、人間の採用判断案を整理する時に使う。公開・マージはしない。
license: MIT
---

# Intelligence Triage

## 参照
`SECURITY_INTELLIGENCE_SELECTION_POLICY.md`、`AUTOMATION_TRIAGE.md`、`config/intelligence_triage.yml`、既存`docs/`と候補台帳。

## 手順
1. 一次原資料と公開日、何が変わったのかを確認する。未確認主張は未確認のまま残す。
2. 既存記事との関係（`new`、`update-existing`、`duplicate`、`watch`、`vulnerability`）を判定する。
3. 関係とは別に推奨ルート（`library`、`vulnerability`、`watch`）と決定理由を記録する。機械的なルートは記事掲載の承認ではない。
4. Library候補は試行的な5軸（経営30・対策25・新規性20・日本関連15・根拠10）で評価可能。75点以上は積極検討、55〜74点は個別判断。重複・根拠不足・緊急例外はスコアより優先する。
5. 新規作成／更新／保留／除外を提案し、レビュー担当者が決定できる判断理由と残課題を示す。
6. マージ済みTriage PRから記事化へ渡す場合、現行`WORK_AI_DRAFTING.md`の`triage.route=library`かつ`triage.draft_eligible=true`条件を守る。

## 禁止
選定スコアで`config/intelligence_triage.yml`を勝手に変更しない。AIが採用・公開を確定しない。

## 成果
候補とルートの表、関係・評価・根拠、既存記事との照合、担当者への提案。

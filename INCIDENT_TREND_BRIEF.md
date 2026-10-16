# Incident Trend Brief — 隔週インシデント傾向レビュー

## 目的・Library内の位置づけ

本Briefは、公開されたインシデントを単に列挙せず、**攻撃経路・被害傾向・対策の横断的な変化**を経営と実務の両面から整理します。

既存のSecurity Intelligence Libraryとは **公開・閲覧は統合、収集・記録・分析は分離** します。個別記事は一つの事案・攻撃手法を深掘りし、本Briefは2週間の代表事案を比較、Monthlyは月全体の戦略的な変化、Quarterlyは複数月にまたがる構造変化を扱います。**Monthlyの短縮版にはしません**。

初号の構成：
- 事案記録：data/incident-trends/2026-10-h1.json
- 記事草稿：drafts/cybersecurity/incident-trend-brief-2026-10-h1.md
- 根拠JSON：drafts/evidence/incident-trend-brief-2026-10-h1.json
- 人間のレビュー表：drafts/reviews/incident-trend-brief-2026-10-h1.md

## 期間・選定条件

- H1：毎月1〜15日、H2：16日〜月末。**当該期間に公表されたもの**を収集し、攻撃発生・侵害判明・公表・続報を区別します。
- as_of：公表情報を実際に評価した確認基準日。次号以降の更新で以前の判断が変わり得ます。
- curated_non_exhaustive：母集団をすべて捉えた調査ではない、一次情報を優先した代表例の選定。
- incident_group：侵害事案の重複を避けるための編集上の事案単位。利用企業、自治体、取引先の続報は related_disclosures に含め、**別の攻撃発生件数として足しません**。
- advisories：JPCERT/CC、NICT、IPAなどの注意喚起は事案数とは別に管理。注意喚起に記された手法が選定した組織の侵入経路だったことを示すものではありません。

このMVPでは国内の総発生件数、増加率、発生率、業種別被害率などを計算しません。厳密な統計が必要なら、母集団、情報源の捕捉率、重複ルール、追跡・更新ルールを別に設計してから行います。

## データ構造

| 記録 | 主な項目 | 意味 |
| --- | --- | --- |
| Brief | brief_id、period.start/end/as_of | 期末と情報確認時点を区別 |
| 収集条件 | coverage.sampling/counting_unit/limitations | 網羅性の限界と数え方 |
| 出典 | sources の id、publisher、url、published_at、accessed_at、locator | 各事実と一次情報の対応 |
| 事案 | incidents の id、event_group、disclosed_at、category、impact | 同一事案の重複防止 |
| 主張 | facts の text、classification、source_ids | 事実・出典の見解を区別 |
| 留保 | uncertainty | 影響・原因の不明点 |
| 関連公表 | related_disclosures | 利用組織の発表を事案群へ関連付け |
| 注意喚起 | advisories | 攻撃手法・防御策を別管理 |
| 分析 | trend_signals の assessment、confidence、limitation、incident_ids、advisory_ids | 根拠のある分析と限界 |

重要な公表結果は更新履歴を反映します。漏えい「可能性」、確認された不正照会、流出の痕跡なし、サービス停止、バックアップ取り出し可能、業務再開完了はそれぞれ異なる状態です。同じ状況として要約しません。

同一犯・同一攻撃手法・AI悪用の有無が一次資料で確認できない場合、断定しません。IoCとVirusTotalのデータを大量に自動照会・再配布する仕組みも、このMVPには含めません。

## 隔週の制作フロー

1. 各期終了後、国内の公表企業、政府、JPCERT/CC、NICT、IPAなど**一次情報**を確認し、Libraryの記事と既存事案との重複を調べる。
2. 各事案をevent_groupへ整理して、実際の公表日、出典のURL・節・ページ、確認済みの影響、未確認事項、関連する組織の公表をdata/incident-trendsのJSONに記録する。
3. 注意喚起はadvisoriesへ分離し、trend_signalsの各仮説に「根拠の事案・注意喚起」と「まだ確認できていない点」を記載する。
4. 既存のARTICLE_WORKFLOW.mdに従い、Cybersecurityカテゴリ、Incident Trendsタグの記事草稿・根拠JSON・レビュー表を作成する。採用・根拠の最終確認は人間が行う。
5. 下記のチェックを実行する。

~~~bash
python scripts/check_incident_trends.py
python -m unittest discover -s scripts -p "test_incident_trends.py" -v
python scripts/article_workflow.py check --collection cybersecurity --slug incident-trend-brief-2026-10-h1
~~~

6. **Draft PRで人間がレビュー**。3事案群が非網羅サンプルであること、JPCERT/CC等の一般的な手口との混同がないこと、出典の確度、続報による判断変更を確認する。
7. 人間が正式採用・公開を承認した場合にだけ、article_workflow.pyのstageで掲載先をdocs/cybersecurity/へ移し、review/evidenceへ根拠JSONを配置する。実際に確認した人間がreview.status = approved、reviewed_by、reviewed_atを記録する。記事をpublishedへ更新し、生成インデックス・メタデータを更新する。
8. 必須CIの成功、Draft解除後の再チェック、**人間によるマージ**、GitHub Pagesへの配信と表示確認を実施する。

同じDraft PRを更新して公開に進めても構いません。CIの成功は出典の真偽や人間の実確認を証明するものではありません。詳細はARTICLE_WORKFLOW.mdとEVIDENCE_REVIEW.mdを参照してください。

## データのCI検査

scripts/check_incident_trends.py は、期間とファイル名の一致、発表日・確認日、重複事案群ID、ソースURL・参照位置、関連公表と注意喚起の分離、分析への参照とlimitationsを検査します。

この検査は**構造のみ**です。ネットワークを使った原文の取得・真偽の自動判定、データ自動収集、AI推論による事件の断定、GitHubへの公開・マージは行いません。初号ではデータと記事を人間が選定・作成したDraftとして扱います。

## 次の運用改善候補

初号への編集フィードバックを確認した後に、対象ケース数、海外事例の対象化、Monthlyへの相互リンク、候補収集の自動化と毎期の実行頻度を決めます。少なくとも自動化開始時には、一次資料の更新、公表の訂正、事案群の重複、公開の承認を人間が確認できるようにします。

# Security Intelligence Selection Policy
情報収集・選定基準（v1.0 / 評価スコア試行版）

更新日: 2026-11-20

## 1. 目的と適用範囲

Security Intelligence Library（SIL）はセキュリティニュースを網羅する媒体ではない。公開情報から、企業のセキュリティ実務、経営リスク、設計・運用、ガバナンス、投資・優先順位づけの意思決定に寄与する変化を選び、根拠を明示して蓄積する。

本ポリシーは、フィード収集、補完Web調査、手動発見による**候補の編集上の採否**と理由の記録に適用する。候補の収集、ルーティング、記事Draft作成、Evidence Review、公開承認は別工程であり、**高得点でも自動採用・自動公開しない**。Monthly / Quarterlyでは、記事の採用点数をそのままCore Theme順位に流用せず、各期間の構造変化を別途編集判断する。

- 情報源の技術的な登録・有効化: [config/intelligence_sources.yml](config/intelligence_sources.yml)
- 現行の機械的なルート規則: [config/intelligence_triage.yml](config/intelligence_triage.yml)、[AUTOMATION_TRIAGE.md](AUTOMATION_TRIAGE.md)
- 補完調査時の既存記事照合: [WORK_SUPPLEMENTAL_DISCOVERY.md](WORK_SUPPLEMENTAL_DISCOVERY.md)
- 記事化・根拠・人間の公開承認: [ARTICLE_WORKFLOW.md](ARTICLE_WORKFLOW.md)、[EVIDENCE_REVIEW.md](EVIDENCE_REVIEW.md)
- 公開するEditorial Policy: [docs/about/index.md](docs/about/index.md)

本ポリシーは、上記の既存ルールを置き換えたり、CIが強制する新しいスキーマを導入したりするものではない。

## 2. 収集対象・情報源の信頼性

対象領域は Cybersecurity / Identity Security / AI Security / Regulation / Risk Management。特に攻撃・防御の構造変化、Identity / AI / Supply Chain / Resilience、国内外の重要な規制・標準、組織的な対応の変化を重視する。

情報源の優先順位は公開Editorial Policyに従う。

| Tier | 情報源 | 選定時の扱い |
| --- | --- | --- |
| 1 | 政府、規制当局、標準化団体、原著・公式仕様 | 原則優先。適用範囲、施行・公開・更新日の違いを確認する |
| 2 | セキュリティベンダー等の一次調査、観測データ | 観測対象・母集団・推定と確定事実を区別する |
| 3 | 信頼できる専門媒体、第三者分析 | 可能な限り一次資料を追跡し、重要な主張は照合する |
| 4 | SNS、攻撃者の主張、未検証の速報 | 単独では確定事実として採用しない。原則watch・裏付け待ち |

複数の記事が同じ一次調査を引用しているだけなら、独立した裏付けが複数得られたとはみなさない。一次情報でも発行者の主張・予測が独立に検証された事実になるわけではない。

## 3. 判定手順：スコアより先に適格性と重複を確認

1. **対象・安全性**：公開可能な情報か。対象領域・企業意思決定との接点があるか。秘密情報、NDA対象情報、個人情報は扱わない。
2. **出典確認**：原資料URL、発行主体、公開日・更新日（確認可能な場合）、重要な主張の位置を確認する。裏付け不足を推測で補わない。
3. **既存記事・採択済み候補の照合**：URLの一致だけでなく、出来事、調査、規制・標準番号、対象技術、CVE、主張の実質で比較する。採択済みの `.automation-review/candidates-*.json` も確認する。
4. **content_relationを1つ指定**：`new` / `update-existing` / `duplicate` / `watch` / `vulnerability`。この分類は既存の補完調査ルールと同じ意味で用いる。
5. **routeを別に指定**：`library` / `vulnerability` / `watch`。content_relationとrouteを混同しない。例えば `update-existing + library` は既存記事の更新提案であり、新規記事化ではない。
6. **編集評価**：Libraryに入れるか判断する候補について、5軸スコアと理由を記録する。重複などで除外する候補は採点不要だが、除外理由を残す。
7. **人間の判断**：採用、既存記事更新、保留、別システムへ振り分け、除外のいずれかを記録する。Draft・公開には従来の個別承認が必要。

`new` と `update-existing` の区別が不明なら、既存記事を提示して `update-existing` を優先し、人間が確認する。キーワードが似ているだけで黙って除外しない。

## 4. Library候補の5軸評価（試行）

各軸を0〜5の6段階で評価し、`軸の配点 × 評価値 / 5` を合算する（最大100点）。0=関連なし、1=弱い、2=限定的、3=一定、4=高い、5=非常に高い。**これは編集上の比較補助であり、機械的な掲載要件ではない。**

| 評価軸 | 配点 | 高得点の判断例 |
| --- | ---: | --- |
| 経営・事業への影響 | 30 | 事業継続、説明責任、法令対応、投資・優先順位に明確な影響 |
| セキュリティ対策への影響 | 25 | 複数組織で設計・統制・検知・運用の変更が必要 |
| 新規性・変化の大きさ | 20 | 既知情報の焼き直しではなく、新事実・確定した制度・攻撃手法の変化 |
| 日本企業への関連性 | 15 | 国内の企業・制度・サプライチェーン・利用技術への適用可能性が具体的 |
| 根拠の確かさ | 10 | 重要な主張を原資料で追跡でき、事実・発行元の主張・分析を区別できる |
| **合計** | **100** | |

スコアは重大性、緊急性、出典Tier、Evidence分類の代用品ではない。特に「経営影響」と「対策影響」の説明は重複させず、別々の判断理由を記録する。

### 試行上の目安（人間による判断を置き換えない）

| 合計 | 原則の扱い |
| --- | --- |
| 75〜100 | Libraryの採用・更新を積極的に検討 |
| 55〜74 | Watchで継続観測、または追加調査後に採用判断 |
| 0〜54 | Library新規記事は原則見送り。Vulnerabilityへの振り分けやWatch継続は個別判断 |

- `duplicate` は点数に関係なく新規記事にしない。
- `vulnerability` 主体の候補は、高得点でも原則Vulnerabilityへ送る。ただし脆弱性管理全体の構造的変化を示す場合は人間がLibraryへの昇格を検討する。
- 公開された重大インシデント、実悪用、規制期限などは低得点でも人間が優先審査できる。その場合は例外理由を残す。
- 出典不足・重要主張の未検証は、点数にかかわらず公開を保留する。
- 目安は運用実績から見直す。現行GitHub Actionsのルーティング閾値へ**自動反映しない**。

## 5. ルーティングと緊急性の分離

ルートはどのワークフローで扱うかを表す。

- `library`: 組織横断で再利用可能な、長期に価値のある管理・リスク情報。
- `vulnerability`: 個別製品、CVE、深刻度、実悪用状況など脆弱性中心の情報。
- `watch`: 新しいが根拠が弱い、狭すぎる、変化が未確定、追加観測待ちの情報。

機械的ルーティングは現行設定が優先する。例：NISTはLibrary、CISA CSAF ITはVulnerabilityを原則とし、SSVC ActiveはLibrary、PoC・CVSS 9.0以上・脆弱性3件以上等はWatchの規則がある。**ルートは公開決定ではなくレビュー候補の分類**である。設定値を変更する場合は別PRで検討する。

Urgencyも別記する（公開Editorial Policyに準拠）。

- `Immediate`: 現在の露出・侵害、施行済み義務等への早期対応。
- `Near-term`: 数週〜数か月以内の設計・計画・対応。
- `Strategic`: 中長期の戦略、能力、ガバナンス、投資判断。

## 6. 判断記録（最低限）

既存のTriage PR、補完調査結果、編集レビュー記録に、可能な範囲で以下を残す。**既存JSONのスキーマを無断で変更することは求めない**。

| フィールド | 内容 |
| --- | --- |
| candidate | タイトル、原資料URL、発行元、公開・更新日（判明分）、確認日 |
| content_relation | `new` / `update-existing` / `duplicate` / `watch` / `vulnerability` |
| existing_article | `update-existing` の場合の既存記事パス |
| route | `library` / `vulnerability` / `watch` |
| assessment | 5軸の0〜5点と合計点（採点対象の場合） |
| urgency | `Immediate` / `Near-term` / `Strategic` |
| decision | `adopt` / `update` / `watch` / `redirect` / `exclude` |
| rationale | 採用・保留・除外理由、日本企業または経営・運用上の意味、例外の理由 |
| provenance | 判断日、判断担当者、確認済みの根拠URL、未解決事項 |

記載例（試行用の編集レビューMarkdown。自動処理の入力仕様ではない）：

```yaml
candidate:
  title: "例：新たな公的ガイドラインの公表"
  source_url: "https://example.org/official-guidance"
  source_tier: 1
content_relation: new
route: library
assessment_0_to_5:
  business_impact: 4
  security_control_impact: 4
  novelty: 5
  relevance_japan: 3
  evidence_quality: 4
score_total: 81
urgency: Near-term
decision: adopt
rationale: "複数組織の統制設計に影響。国内への適用条件は別途確認する"
unresolved: "国内での適用範囲を確認"
```

上記URL・数値は書式説明の**架空例**であり、実在候補の採否ではない。採用判断の記録はEvidence Reviewの代わりにはならない。記事中の重要主張は `source_fact` / `source_claim` / `library_assessment` として別途検証し、新規記事の公開には人間による承認が必要。

## 7. 典型例

| 候補 | 原則の判断 | 主な理由 |
| --- | --- | --- |
| CVEごとの通常の製品更新情報 | `vulnerability` | まず脆弱性単位で管理。組織横断の示唆があれば再審査 |
| 新たな規制の確定版や施行期限の変更 | `library` / `update-existing` | 経営・統制・対応計画への影響。既存記事との重複を確認 |
| ベンダーによる未検証の宣伝・性能主張 | `watch` または除外 | 裏付け不足、独立性に留意 |
| 既存記事と同じ調査結果の再掲 | `duplicate` | 新規記事を作らず重複として記録 |
| 侵害手口の新たな実証が既存記事を更新 | `update-existing + library` | 実質的な新事実を既存記事へ反映 |

## 8. 人間によるレビューと改善

- 補完調査の候補提示は [WORK_SUPPLEMENTAL_DISCOVERY.md](WORK_SUPPLEMENTAL_DISCOVERY.md) に従い最大5件。重要な除外・重複の理由も簡潔に残す。
- 採用候補のDraft生成は、マージ済みTriageの `triage.route = library` かつ `triage.draft_eligible = true` を原則とする。その他の候補は明示的な人間の昇格判断が必要。
- スコア、理由、例外を記録し、一定期間の運用後に「高得点だが価値が低かった候補」「低得点で重要だった候補」「重複判定の誤り」をレビューする。
- 本文の根拠検証・出典の実質確認・公開は [ARTICLE_WORKFLOW.md](ARTICLE_WORKFLOW.md) に従い、PRの承認とマージを人間が行う。
- 将来スコアを自動化・閾値で強制する場合、誤判定の検証、後方互換、回帰テスト、別PRでの承認を必須とする。

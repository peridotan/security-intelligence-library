---
title: About / Editorial Policy
hide:
  - toc
---

# About / Editorial Policy

Security Intelligence Libraryは、公開情報に基づくサイバーセキュリティ、Identity、AI Security、規制・リスクマネジメントの調査・分析を、Markdownで蓄積する静的ナレッジベースです。

## Editorial Policy

### 情報源の優先順位

| Tier | 主な情報源 | 扱い |
| --- | --- | --- |
| Tier 1 | 政府、規制当局、標準化団体、原著・公式仕様 | 最優先 |
| Tier 2 | セキュリティベンダーの一次調査・Telemetry | 観測範囲を明示 |
| Tier 3 | 信頼できる主要メディア、専門家分析 | 一次情報で可能な限り照合 |
| Tier 4 | SNS、攻撃者主張、未検証情報 | 事実と分離し、未検証であることを明示 |

重要な数字・制度変更・確認済み事実は、**本文中の脚注から根拠へ直接たどれること**を標準とします。記事末尾の「参考情報」には、追加の一次情報・背景資料も掲載します。

### Evidence

- **Confirmed** — 法令・公式発表など、一次情報で確認できる事実
- **Observed** — 政府・ベンダー等の観測・Telemetry・研究結果
- **Mixed** — 確認済み事実と、攻撃者主張など未検証情報を併記
- **Assessment** — 複数情報源を基にした分析・設計上の評価

### Urgency

- **Immediate** — 現在のExposure、Incident、施行済み規制など、早期判断が必要
- **Near-term** — 数週間〜数か月の計画・設計へ反映すべき
- **Strategic** — 中長期の能力・ガバナンス・投資判断へ影響

Management ImpactとUrgencyは別概念です。

## 標準記事構成

1. Executive Summary
2. なぜ今なのか
3. 何が起きているのか / 論点
4. 経営インパクト
5. 日本企業への示唆
6. 推奨アクション
7. 用語解説
8. 関連記事
9. 参考情報

MetadataはFront Matterを**Single Source of Truth**とし、公開日、更新日、カテゴリ、想定読者、Management Impact、Urgency、Evidenceをビルド時に同期します。PowerPointリンクは `pptx` が設定された記事にのみ表示します。

## AI利用方針

調査補助、構成、草稿作成、比較整理などに生成AIを利用する場合があります。ただし、重要な事実、数値、規制内容、引用元については公開情報・一次情報を確認し、AIの出力だけを根拠にはしません。

## 情報管理方針

公開サイトには、公開情報と公開可能な分析のみを掲載します。顧客情報、個人情報、社内限定資料、NDA対象情報、秘密情報、認証情報はコミットしません。

## Correction Policy

公開後に誤り、重要な前提不足、リンク切れ等を確認した場合は、記事本文と `updated` を更新します。重要な訂正では、何を変更したかが分かる形で履歴を残します。

誤りやリンク切れの連絡は [GitHub Issues](https://github.com/peridotan/security-intelligence-library/issues) からお願いします。

## Copyright and Licensing

本サイトのオリジナルな記事・分析・解説・表などのEditorial Contentは、別途明示される場合を除き、

**© 2026 peridotan. All rights reserved.**

です。

記事コンテンツの再配布、転載、商用再利用、二次利用について包括的な許諾は行っていません。引用・参照等は適用法令の範囲で行ってください。

一方、リポジトリ内のスクリプト、GitHub Actions、スタイルシート、設定ファイルなどの**Software部分にはMIT License**を適用します。詳細はリポジトリの `LICENSE` と `COPYRIGHT.md` を参照してください。

第三者の商標、製品名、サービス名、引用元資料、リンク先コンテンツ、フォント、ライブラリ等の権利は、それぞれの権利者に帰属します。既知の第三者コンポーネントは `THIRD_PARTY_NOTICES.md` に整理しています。

本サイトのCopyright表示は、引用・要約・参照している第三者資料そのものの権利を主張するものではありません。

## Disclaimer

本サイトは公開情報を整理した一般的な情報提供を目的とし、法的助言、セキュリティ保証、監査意見、投資助言を提供するものではありません。規制・契約・セキュリティ判断は、対象組織の状況と最新の一次情報を確認したうえで行ってください。

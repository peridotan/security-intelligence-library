# Security Intelligence Library

Cybersecurity / Identity Security / AI Security / Regulation / Management View の公開情報をMarkdownで蓄積し、Zensical + GitHub Pagesで公開するナレッジベースです。

## v0.17.1

- Quarterly Review一覧のReviewed日付を途中改行しない表示へ修正
- Quarterly ReviewのStatsをDesktopで1行表示に調整
- Tablet / Mobileでは従来どおり自然に折り返すResponsive表示を維持
- Content / Evidence / Quarterly analysisの内容変更なし

## v0.17.0

- Q1 2026 Security Intelligence Reviewを追加
- January / February / Marchの30 Core Themesを7つの構造変化へ再分析
- Q1 Evidence Mix（Confirmed 17 / Observed 12 / Assessment 1）を表示
- Q1 → Q2のTrust Architecture進化を整理
- Quarterly CIの必須Section検証をQ1〜Q4共通ロジックへ改善
- Quarterly Review一覧とHomeへQ1 Reviewを自動反映

## v0.16.0

- January 2026 Intelligenceを追加
- January 2026 Executive Summaryと10 Core Themesを追加
- NIST CAISI AI Agent Security RFI記事を追加
- Microsoft AI Agent Runtime Defense記事を追加
- OpenAI AI Agent Link / URL Data Exfiltration記事を追加
- LangGrinch / AI Application Supply Chain記事を追加
- Microsoft Data Security Index 2026記事を追加
- ShinyHunters-branded SaaS Data Theft記事を追加
- Complex Routing / Domain Spoofing記事を追加
- RedVDS Cybercrime Infrastructure記事を追加
- EU Cybersecurity Package 2026記事を追加
- 経済安全保障経営ガイドライン記事を追加
- ShinyHunters記事にSelective MITRE ATT&CK® Mappingを追加

## v0.15.0

- February 2026 Intelligenceを追加
- February 2026 Executive Summaryと10 Core Themesを追加
- Anthropic LLM-discovered Zero-days記事を追加
- OpenAI Trusted Access for Cyber（February）記事を追加
- NIST Agent Identity + Standards記事を追加
- NIST AI 800-3 Evaluation Uncertainty記事を追加
- GTIG AI Threat Tracker（February）記事を追加
- Unit 42 Global Incident Response 2026記事を追加
- Dell RecoverPoint Zero-day / Recovery Infrastructure記事を追加
- NIST SP 1800-39 Data Classification記事を追加
- EU ICT Supply Chain Security Toolbox記事を追加
- IT製品調達セキュリティ要件リスト第2.1版記事を追加

## v0.14.1

- Q2 2026 Quarterly Reviewへ `Pre-Q2 Signals · March 2026` を追加
- MarchのAI / Identity / Supply Chain / Resilienceの4 SignalsをQ2へ接続
- `prelude_month` metadataを追加し、対応するMonthly Sourceの存在をCIで検証
- June trajectory cardの表現を `運用Architectureへ` に簡潔化

## v0.14.0

- March 2026 Intelligenceを追加
- March 2026 Executive Summaryと10 Core Themesを追加
- AI as Tradecraft記事を追加
- Tycoon2FA / AiTM PhaaS記事を追加
- Teams Vishing / Quick Assist記事を追加
- NIST Deployed AI Monitoring記事を追加
- AI事業者ガイドライン第1.2版記事を追加
- NIST SP 1800-42 mDL for Financial Institutions記事を追加
- NIST SP 1308 Cyber Risk / ERM / Workforce記事を追加
- SCS評価制度の制度構築方針記事を追加
- サイバーインフラ事業者ガイドライン記事を追加
- M-Trends 2026記事を追加
- Tycoon2FAとTeams VishingにSelective MITRE ATT&CK® Mappingを追加
- ATT&CK catalogへT1566.004 / T1219.002を追加

## v0.13.0

- `Quarterly Review`を新設
- Q2 2026 Security Intelligence Reviewを追加
- April / May / Juneの30 Core Themesを7つの構造変化へ再分析
- Q2 ReviewにEvidence Mix（Confirmed 20 / Observed 9 / Assessment 1）を表示
- Homeに最新Quarterly Reviewを自動表示
- Quarterly Review一覧をFront Matterから自動生成
- Primary NavigationにQuarterly Reviewを追加
- CIでQuarter metadata、3か月のMonthly Source、必須Section、内部Linkを検証

## v0.12.0

- MITRE ATT&CK® Mappingを全記事ではなくAttack / Campaign記事へ選択的に導入
- 8記事に初期Mappingを追加
- `Source-labeled` と `Analyst-mapped` を明確に区別
- ATT&CK Technique catalogを `config/mitre_attack.yml` で一元管理
- Mapping表をFront Matterから自動生成
- 独自Attack / Process Flowは読者向け図解として維持
- CIでTechnique ID、重複、Mapping Basis、Context Note、Legal Noticeを検証
- MITRE ATT&CK® Terms of Use / Trademark / Copyright noticeをThird-Party Noticesへ追加

## v0.11.2

- 攻撃チェーン／Process Flowを `text` コードブロックから専用Flow UIへ変更
- OT攻撃、Vulnerability Window、Credential Attack、AI Agent Identityの4図を移行
- Branch / Panel / Loopを含むFlow表示を追加
- MobileではBranch / Panelを1列へ自動Stack
- CIで矢印付き `text` コードブロックを検出し、Flow UI利用を促す

## v0.11.1

- Monthly Intelligence一覧をDesktop 3列 / Tablet 2列 / Mobile 1列へ整理
- `review_status: Superseded` 記事にHistorical Snapshot Bannerを自動表示
- Superseded記事から後継・最終版記事へ明示的に誘導
- `superseded_by` metadataを追加
- CIでSuperseded記事の後継リンクとBanner生成を検証

## v0.11.0

- April 2026 Intelligenceを追加
- April 2026 Executive Summaryと10 Core Themesを追加
- Claude Mythos Preview / Project GlasswingのCyber Capability記事を追加
- AIが攻撃Lifecycleへ組み込まれるThreat Landscape記事を追加
- AI-enabled Device Code Phishing記事を追加
- Axios Supply Chain / Code Signing Trust記事を追加
- OpenAI Advanced Account Security記事を追加
- EUDI Wallet Cybersecurity Certification記事を追加
- NIST IR 8259r1 IoT Product Lifecycle Security記事を追加
- NIST SP 800-133r3 PQC Key Generation記事を追加
- 日本のSCS評価制度の実装段階記事を追加
- 重要インフラ統一基準（案）のHistorical Snapshot記事を追加

## v0.10.0

- May 2026 Intelligenceを追加
- May 2026 Executive Summaryと10 Core Themesを追加
- Project YATA-Shield記事を追加
- 金融庁 Frontier AI短期対応記事を追加
- NIST AI Agent Security RFI分析記事を追加
- Singapore Agentic AI Governance v1.5記事を追加
- OpenAI Codex Runtime Security記事を追加
- OpenAI Trusted Access for Cyber記事を追加
- Mini Shai-Hulud / @antv Supply Chain記事を追加
- F5 / Confluence Edge-to-Identity攻撃記事を追加
- AiTM Token Compromise記事を追加
- NIST SP 1800-41 OT Response / Recovery記事を追加
- v0.9系のTopics / Tags / Current Intelligence自動生成をそのまま利用

## v0.9.1

- Home Heroを読者価値中心の説明へ変更
- Home kickerの `Risk` を `Management` に統一
- Current Intelligenceの説明を実装仕様ではなく読者向け表現へ変更
- Topics冒頭に Articles / Curated Topics / Detailed Tags の自動集計を追加
- TopicsからTagsへの明確なCTAを追加
- 各Topic Group末尾にTopic Directoryへ戻る導線を追加
- `AI-enabled Threats` を `AI-Enabled Threats` に表記統一

## v0.9.0

- `Topics`と`Tags`を分離
- Topicsを18個の統制されたEditorial Taxonomyへ整理
- 30記事すべてに1〜3個のcurated `topics`を付与
- 詳細な製品名・技術名・攻撃名は従来どおり`tags`として保持
- Topic taxonomyを `config/topics.yml` で一元管理
- Topicsページを4グループのDirectory + 記事一覧として自動生成
- `docs/tags/index.md` を追加し101個の詳細Tagを別索引へ移行
- Home Featured Topicsをcurated Topicsから自動生成
- 個別記事MetadataにTopicsを表示
- CIで未知Topic・Topic過多（4個以上）を拒否

### Taxonomy rule

- Topics: 横断的な主要論点。1記事1〜3個。
- Tags: 製品名、技術名、攻撃手法、標準、固有名詞等の詳細キーワード。

## v0.8.1

- Homeの `Latest Intelligence` を `Current Intelligence` に変更
- Monthly Intelligenceの `as of` 表示を `Reviewed` に変更
- Monthly metadataを `as_of` から `reviewed` へ移行
- Mastra npm Supply Chain記事の出典をMicrosoft専用一次情報へ変更
- Mastra記事にSocketの独立技術分析を追加

## v0.8.0

- June 2026 Intelligenceを追加
- June 2026 Executive Summaryと10 Core Themesを追加
- AutoJack / localhost Trust Boundary記事を追加
- MCP Tool Poisoning / Agentic Supply Chain記事を追加
- NIST Continuous AI Security記事を追加
- MDASH / AI Vulnerability Discovery記事を追加
- Mastra npm AI Supply Chain記事を追加
- NIST IR 8374r1 Ransomware CSF 2.0記事を追加
- NIST SP 1339 OT Backup記事を追加
- NIST SP 1800-45 OT Remote Access記事を追加
- NIST PIV PQC / Crypto Agility記事を追加
- NIST SP 800-18r2 Integrated System Plans記事を追加
- v0.7.xのFront Matter駆動Index生成によりHome / Category / Monthly / Topicsへ自動反映

## v0.7.1

- Fixed a false positive in `check_generated_site.py`.
- Zensical/theme-generated `<article>` elements are no longer counted against `sil-card` elements.
- Generated HTML validation now tracks only Security Intelligence Library card elements.

## v0.7.0

- Front MatterをSingle Source of TruthとしてHome / Category / Monthly / Topicsを自動生成
- Monthly Intelligence一覧のHTML構造不具合を解消
- PublishedとSource Periodを分離して記事Metadataに表示
- `reviewed` / `review_status` を追加し鮮度管理を導入
- `impact_types` を追加しManagement ImpactがHighに集中しても差分を把握可能に
- Primary Navigationから個別記事を外し、記事数増加に耐える構造へ変更
- `scripts/update_content.py` を追加し記事追加後の更新作業を1コマンド化
- 週次External Link CheckerとReview Freshness Checkを追加
- CIで生成後HTMLの構造・内部リンクを検証
- RedirectやEditorial / Rights Guardrailは継続

### Content workflow

```bash
python scripts/new_article.py ai-security example-slug "記事タイトル" --source-period 2026-09
# 記事を編集して status: published に変更
python scripts/update_content.py
```

個別記事を`zensical.toml`やCategory / Topics / Homeへ手作業で追加する必要はありません。

## v0.6.0

- July 2026 Intelligenceを追加
- July 2026 Executive Summaryと9 Core Themesを追加
- JADEPUFFER / Agentic Ransomware記事を追加
- OpenAI / Hugging Face Cyber評価インシデント記事を追加
- Passkey Enrollment / Recovery Attack記事を追加
- Entra ID Passkey既定化記事を追加
- Kimi K3 Cyber Capability評価記事を追加
- NIST SP 800-239 AI Data Center Security記事を追加
- NIST SP 1326 C-SCRM Due Diligence記事を追加
- EU Cybersecurity & AI Action Plan記事を追加
- AD FS / SharePoint実悪用Zero-day記事を追加
- Category / Topics / Monthly Archive / Navigationを更新

## v0.5.3

- AI利用方針を「利用する場合があります」から「利用しています」へ明確化
- Human Editorial Responsibilityを明文化
- 引用・画像・商標の利用ルールを追加
- Privacy方針を追加し、Google Fonts自動読み込みを無効化
- トップレベルLICENSEの曖昧さを解消し、MIT本文を `LICENSE-CODE.txt` に分離
- AI生成物・事実・第三者資料に対するCopyright表示の限界を明文化
- `RIGHTS_REVIEW.md` を追加
- Editorial Contentの外部PRを原則非受付とし、権利帰属の曖昧さを回避
- `CONTRIBUTING.md` / `.github/SECURITY.md` / Dependabot設定を追加
- Zensical / PyYAML / Pythonを固定し、ビルド再現性を改善
- Google Fontsへの外部通信を停止
- Redirect用旧URLページを検索対象外化
- CIに画像・埋込メディア・直接引用のRights Guardrailを追加

## v0.5.2

- Editorial Contentは `© 2026 peridotan. All rights reserved.` として権利を保持
- Software部分にMIT Licenseを適用
- `COPYRIGHT.md` を追加し、記事とコードの権利関係を明確化
- `THIRD_PARTY_NOTICES.md` を追加
- About / Editorial PolicyにCopyright and Licensingを追加
- FooterのCopyright holderを `peridotan` に統一

## v0.5.1

- 420px以下では記事Metadataを1列表示
- Markdown表を横スクロール可能にし、狭い列への過剰な折返しを抑制
- 狭幅モバイルでは浮動TOCを非表示にして本文との重なりを回避
- 参考情報を生URL表示から「情報源タイトル＝リンク」形式へ整理

## v0.5.0

- HomeをLatest Intelligence 6件に整理
- Monthly Intelligence Archiveを追加
- August 2026 Executive Summaryを追加
- Topicsをクリック可能に変更
- AboutをEditorial Policyへ拡張
- Source Tier / Evidence / Urgency / AI利用 / Correction / Disclaimerを明文化
- Front MatterをMetadataのSingle Source of Truthに変更
- 空のPPT導線を非表示化
- 主要主張にInline Footnoteを追加
- CIでFront Matter、必須章、内部リンク、参考URLを検証

## Local check

```bash
python scripts/sync_article_metadata.py
python scripts/check_content.py
zensical build --clean --strict
```


## Licensing

- Editorial content under `docs/`: © 2026 peridotan. All rights reserved.
- Software/configuration portions: MIT License (`LICENSE-CODE.txt`)
- Third-party materials: subject to their respective licenses and rights

See `COPYRIGHT.md`, `LICENSE`, `LICENSE-CODE.txt`, `RIGHTS_REVIEW.md`, and `THIRD_PARTY_NOTICES.md`.

# Security Intelligence Library

Cybersecurity / Identity Security / AI Security / Regulation / Management View の公開情報をMarkdownで蓄積し、Zensical + GitHub Pagesで公開するナレッジベースです。

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

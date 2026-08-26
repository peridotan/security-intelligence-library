# Security Intelligence Library

Cybersecurity / Identity Security / AI Security / Regulation / Management View の公開情報をMarkdownで蓄積し、Zensical + GitHub Pagesで公開するナレッジベースです。

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
- Software/configuration portions: MIT License
- Third-party materials: subject to their respective licenses and rights

See `COPYRIGHT.md`, `LICENSE`, and `THIRD_PARTY_NOTICES.md`.

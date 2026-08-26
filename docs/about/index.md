---
title: About
hide:
  - toc
---

# About

Security Intelligence Libraryは、公開情報に基づく調査・分析をMarkdownで蓄積する静的ナレッジベースです。

## コンテンツモデル

```text
Public Sources / Research
          ↓
      Markdown
      (Master)
       ↙     ↘
     Web      PowerPoint
  Search       Briefing
  Archive      Presentation
```

**Markdownを原本**とし、Webは検索・閲覧・蓄積、PowerPointは経営説明・プレゼンテーションという役割に分けます。

## 標準記事構成

1. Executive Summary
2. なぜ今なのか
3. 何が起きているのか
4. 経営インパクト
5. 日本企業への示唆
6. 推奨アクション
7. 用語解説
8. PowerPoint
9. 参考情報

記事には公開日、更新日、カテゴリ、想定読者、Management Impactを付与します。

記事テンプレートはリポジトリ内の `templates/article-template.md` と `docs/about/article-template.md` に保持します。一般閲覧用の上部ナビゲーションには表示しません。

## 情報管理方針

公開サイトには、公開情報と公開可能な分析のみを掲載します。以下は公開リポジトリにコミットしません。

- 顧客情報
- 社内限定資料
- NDA対象情報
- APIキー、トークン、パスワード、秘密鍵
- 公開許可のないPowerPoint / PDF

## Source Policy

重要な主張は、可能な限り一次情報、政府機関、規制当局、標準化団体、主要研究機関・セキュリティベンダーの情報で確認します。確認済み事実と第三者の主張・推測は区別します。

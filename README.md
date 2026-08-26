# Security Intelligence Library

Markdownを原本として、サイバーセキュリティ、AI、Identity、規制、リスクマネジメントの調査・分析を蓄積するWebナレッジベースです。

## Architecture

```text
Research / Source Material
          ↓
       Markdown
       (Master)
       ↙     ↘
GitHub Pages  PowerPoint
```

## v0.2.0

- トップページをポータル型レイアウトへ変更
- Latest Intelligence / Category cards / Featured Topics を追加
- `Article Template` を上部ナビゲーションから非表示化
- 記事メタデータを標準化（公開日、更新日、カテゴリ、想定読者、Management Impact）
- Executive Summary / 推奨アクションを視覚的に強調
- カテゴリページをカード形式に改善
- カスタムCSSを追加

## Local preview

Python 3.10+ が必要です。

```bash
python -m venv .venv
source .venv/Scripts/activate   # Git Bash on Windows
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
zensical serve --open
```

ローカルサイトは通常 `http://localhost:8000/` で表示されます。

## Create a new article

```bash
python scripts/new_article.py ai-security frontier-ai-cyber-risk "Frontier AIのサイバー能力と経営リスク" --description "AIサイバー能力の進展を経営視点で整理"
```

利用可能なカテゴリ:

- `cybersecurity`
- `identity-security`
- `ai-security`
- `regulation`
- `risk-management`

作成後、本文と出典を確認し、公開準備ができた記事だけ `zensical.toml` の `nav` に追加します。

## GitHub Pages deployment

Repository **Settings > Pages > Build and deployment > Source** は **GitHub Actions** を使用します。

`main` へのpushごとに `.github/workflows/docs.yml` が自動実行され、成功すると以下へ公開されます。

https://peridotan.github.io/security-intelligence-library/

## Security / publishing rule

このリポジトリは公開情報専用です。以下はコミットしないでください。

- 顧客情報
- 社内限定資料
- NDA対象情報
- APIキー、トークン、パスワード、秘密鍵
- 公開許可のないPowerPoint/PDF

## Version

- v0.2.0: 2026-08-26
- v0.1.0: 2026-08-26

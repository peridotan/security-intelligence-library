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

作成後、`zensical serve` で確認し、必要に応じて `zensical.toml` の `nav` に記事を追加します。

## GitHub Pages deployment

1. GitHubで `security-intelligence-library` リポジトリを作成
2. このディレクトリの内容を `main` ブランチへpush
3. Repository **Settings > Pages > Build and deployment > Source** を **GitHub Actions** に設定
4. Actions の `Publish Security Intelligence Library` が成功することを確認
5. `https://peridotan.github.io/security-intelligence-library/` を開く

以降、`main` へのpushごとに自動ビルド・公開されます。

## Security / publishing rule

このリポジトリは公開情報専用です。以下はコミットしないでください。

- 顧客情報
- 社内限定資料
- NDA対象情報
- APIキー、トークン、パスワード、秘密鍵
- 公開許可のないPowerPoint/PDF

## Version

Initial scaffold: 2026-08-26

---
title: Build Your Own Security Intelligence Library
description: Security Intelligence Libraryの考え方とMITライセンスのソフトウェアを参考に、自分の情報収集・評価・公開基盤を構築する手順。
---

# Build Your Own Security Intelligence Library

**Security Intelligence Library（SIL）の仕組みを参考に、自分のテーマで情報を収集・整理するサイトを作りたい方へ。** このページは、実際の構成に基づく再現ガイドです。まず自分のサイトを公開し、次に情報収集を自動化し、必要に応じて記事レビューや他のダッシュボードとの連携を増やす順番をおすすめします。

> **重要**：このリポジトリは、ソフトウェア・設定と、記事・解説文でライセンスが異なります。**公開されている記事を丸ごと転載してよいわけではありません。** また、元サイトの全機能をワンクリックで複製できる完成済みテンプレートではありません。

詳しい動作の考え方は[How It Works](how-it-works.md)、情報の選定基準は[Selection Policy](https://github.com/peridotan/security-intelligence-library/blob/main/SECURITY_INTELLIGENCE_SELECTION_POLICY.md)をご覧ください。

## 1. 再現できる範囲と前提

| 段階 | できること | このページの扱い |
| --- | --- | --- |
| **Step 1：公開サイト** | Markdownから独自のナレッジサイトを生成し、GitHub Pagesで公開 | 最小構成の手順を記載 |
| **Step 2：情報収集・Triage** | 設定した一次情報の候補収集、重複URLの除外、Library / Vulnerability / Watchの一次振り分け、PRでの人間レビュー | 既存のMITソフトウェアを選択して取り込む手順を記載 |
| **Step 3：記事・Evidence Review** | 自分で書いた記事と根拠を管理し、公開前に確認する | 既存の構成・導入の入口を案内 |
| **Step 4：高度な連携** | Monthly / Quarterly、他のダッシュボード連携、AI支援を組み合わせる | 個別開発が必要。自動で複製されるものではない |

必要なものは、Git、Python 3.14が動く環境、GitHubアカウント、公開用の新しいGitHubリポジトリです。手順のコマンド例はGit Bash等のBash環境を想定しています。WindowsのPowerShellでは仮想環境の有効化コマンドなどを読み替えてください。

### ライセンスの境界

- **再利用できるもの**：原則として scripts、GitHub Actions、構築・検証用の設定、CSSなどのソフトウェア部分。MITライセンスの条件に従い、元の著作権表示と許諾表示を保持してください。
- **自由な転載を認めていないもの**：docs配下の記事・独自解説・独自表現・独自の編集内容。これらには原則として別の著作権条件が適用されます。自分のサイトの文章は自分で用意してください。
- **別途確認が必要なもの**：外部の画像・文章・商標・資料、各サービスの利用規約、コピーしたOSSの依存関係。

詳しくは[Copyright and Licensing](https://github.com/peridotan/security-intelligence-library/blob/main/COPYRIGHT.md)と[MIT License本文](https://github.com/peridotan/security-intelligence-library/blob/main/LICENSE-CODE.txt)を確認してください。GitHub上でForkできることと、元の記事を自分のサイトに再公開できることは同義ではありません。

**おすすめは、記事一式をコピーするのではなく、新規の空リポジトリから始めて、必要なMITソフトウェアのみを取り込む方法です。**

## 2. Step 1：自分のサイトを作って公開する

### 2.1 Zensicalで新規プロジェクトを作る

新しいフォルダで次を実行します。

~~~bash
mkdir my-security-intelligence
cd my-security-intelligence

python -m venv .venv
source .venv/Scripts/activate  # Windows Git Bashの場合
python -m pip install "zensical==0.0.56" "PyYAML==6.0.3"

zensical new .
~~~

macOS / Linuxの仮想環境では通常 `source .venv/bin/activate` を使います。Zensicalの `new` はMarkdown、設定ファイル、GitHub Pages用のGitHub Actionsを新規生成します。元のSILの記事はコピーされません。

作成される `zensical.toml` の `[project]` セクションで、少なくとも `site_name` と `site_url` を自分のものに変更します。例：

~~~toml
[project]
site_name = "My Security Intelligence"
site_url = "https://YOUR_ACCOUNT.github.io/my-security-intelligence/"
~~~

上記は**設定項目の例**です。既存の `zensical.toml` をこの2行だけで置き換える必要はありません。GitHub PagesのURLは実際のアカウント名・リポジトリ名に合わせてください。

`docs/index.md` を、目的、対象テーマ、問い合わせ方法などの**独自の文章**に編集します。最初は記事を1件も持たないサイトでも構いません。

### 2.2 ローカルで確認する

~~~bash
zensical serve
~~~

ブラウザでローカルプレビューを確認し、公開前に次のビルドも行います。

~~~bash
zensical build --clean --strict
~~~

生成される `site/` と仮想環境はGit管理しません。 `.gitignore` に少なくとも `site/`、`.venv/`、`__pycache__/` を追加してください。

### 2.3 GitHub Pagesに公開する

GitHubで空の公開リポジトリ `my-security-intelligence` を作成します（READMEなどによる初期コミットは作らない例）。その後、ローカルからpushします。

~~~bash
git init -b main
git add .
git commit -m "Initial personal intelligence site"
git remote add origin https://github.com/YOUR_ACCOUNT/my-security-intelligence.git
git push -u origin main
~~~

GitHubのリポジトリ設定から **Settings → Pages → Build and deployment → Source: GitHub Actions** を選びます。Zensicalが生成した `.github/workflows/docs.yml` を利用し、必要ならPython・ZensicalのバージョンをStep 1の設定に合わせて固定します。

GitHub Actionsの公開ワークフローが成功したら、自分のURLを開いてタイトル、本文、内部リンク、モバイル表示を確認してください。**Actionsが成功したことだけでは、表示を目視確認したことにはなりません。**

参考：[Zensical新規プロジェクト](https://zensical.org/docs/usage/new/)、[Zensicalの公開手順](https://zensical.org/docs/publish-your-site/)、[GitHub Pagesの設定](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。

## 3. Step 2：候補収集とレビューPRを追加する

ここからはSILの**MITライセンスのソフトウェア部分だけ**を選んで利用します。Step 1で作ったリポジトリのルートから実行してください。

### 3.1 必要なファイルだけを取り込む

~~~bash
git remote add sil-source https://github.com/peridotan/security-intelligence-library.git
git fetch --depth=1 sil-source main

# 取り込み元のコミットを記録しておく
git rev-parse FETCH_HEAD

git restore --source=FETCH_HEAD --staged --worktree --   requirements.txt   config/intelligence_sources.yml   config/intelligence_triage.yml   scripts/collect_intelligence_candidates.py   scripts/triage_intelligence_candidates.py   scripts/official_html_sources.py   scripts/official_csv_sources.py   scripts/open_review_pr.sh   scripts/request_pr_review.sh   .github/workflows/collect-intelligence-candidates.yml   LICENSE-CODE.txt

git remote remove sil-source
~~~

このコマンドは指定したソフトウェアファイルだけを作業ツリーへ展開します。**元サイトの `docs/` や公開済み記事、分析結果を取り込みません。** 将来のリポジトリ更新でファイル間の依存関係が変わる可能性があるため、コピー元のコミットを記録しておいてください。

`LICENSE-CODE.txt` に含まれる元のMIT著作権・許諾表示は維持し、コピーしたコードであることが分かるよう、自分のREADMEにも出典を記載してください。自作記事のライセンスは別途自分で定義します。

### 3.2 最初は少数の情報源にする

`config/intelligence_sources.yml` は元サイト用に多くの取得先が登録されています。最初はその設定を次のような少数の一次情報へ絞ると、結果を確認しやすくなります。

~~~yaml
version: 1
sources:
  - id: nist-cybersecurity
    name: NIST Cybersecurity
    type: rss
    url: https://www.nist.gov/news-events/cybersecurity/rss.xml
    enabled: true
    category_hint: regulation
    trust: primary

  - id: jpcert-alerts
    name: JPCERT/CC Alerts
    type: rss
    url: https://www.jpcert.or.jp/english/rss/jpcert-en.rdf
    enabled: true
    category_hint: cybersecurity
    trust: primary
~~~

URLやRSSの配信状態は将来変わる場合があります。取得に失敗した場合はエラー・警告を確認し、安易に非公式の代替ソースへ切り替えないでください。

`config/intelligence_triage.yml` は既存のルート設定を引き継げます。ただし、**一次振り分けは採用・公開の決定ではありません。** 新しく追加する収集元を自動的にLibrary記事へ昇格させないでください。

また、コピー元の収集・Triageスクリプトにある `USER_AGENT` のGitHubリポジトリURLは、自分のリポジトリのURLに変更してください。

### 3.3 ローカルで収集・Triageを試す

~~~bash
python -m pip install -r requirements.txt
mkdir -p .automation-review

python scripts/collect_intelligence_candidates.py   --days 7   --output-json .automation-review/raw-local.json   --output-md .automation-review/raw-local.md

python scripts/triage_intelligence_candidates.py   --input-json .automation-review/raw-local.json   --output-json .automation-review/triage-local.json   --output-md .automation-review/triage-local.md
~~~

`raw-local.md` と `triage-local.md` を開き、実際に取得した候補や振り分け理由を確認します。対象期間に新しい情報がなければ候補0件になることもあります。**ローカル試験の一時ファイルは、内容を確認してから削除し、不要なままコミットしないでください。**

### 3.4 GitHub ActionsでレビューPRを作る

コピーした `.github/workflows/collect-intelligence-candidates.yml` は、GitHub Actionsから収集とTriageを実行し、候補がある場合にレビューPRを作るワークフローです。元の設定では、毎週月曜08:00 JST相当のスケジュールと手動実行を備えています。GitHubのスケジュール実行には遅延や停止が起こり得ます。

GitHubの **Settings → Actions → General** で、当該リポジトリでActionsを利用できることを確認し、Workflow permissionsの **Allow GitHub Actions to create and approve pull requests** を必要に応じて有効にします。実際の収集ワークフローは `contents: write` と `pull-requests: write` を宣言しています。組織ポリシーによっては変更できない場合があります。

GitHub Actionsの「Collect Security Intelligence Candidates」から、まず **Run workflow** で手動実行してください。PRが作られたら、候補URL、重複、ルート、対象テーマ、取得失敗の警告をレビューします。

- PRをマージしても**記事は自動公開されません**。
- 初期の自動処理には生成AIを呼び出す処理はありません。
- 追加のAI評価・記事下書きは、別途自分で導入・管理する工程です。
- 最初の成功を確認してから、スケジュールと情報源の数を増やしてください。

参考：[GitHub Actionsの権限設定](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository)、[元のTriage運用](https://github.com/peridotan/security-intelligence-library/blob/main/AUTOMATION_TRIAGE.md)。

## 4. Step 3：記事と根拠を管理する

情報を見つけても、そのまま公開するのではなく、採用・保留・既存記事更新・除外の理由を残します。SILの[Selection Policy](https://github.com/peridotan/security-intelligence-library/blob/main/SECURITY_INTELLIGENCE_SELECTION_POLICY.md)では、経営影響、対策への影響、新規性、日本企業への関連性、根拠の確かさを5軸・100点で比較する**試行方式**を定義しています。この点数は自動採否判定には使っていません。

最小構成では、候補を人が確認して、自分で書いたMarkdown記事を `docs/` に追加するだけでも始められます。記事には原資料URL、公開・確認日、確定事実と観測・推測の区別、日本企業への示唆、確認できなかった事項を残してください。

より厳密に管理したい場合は、[ARTICLE_WORKFLOW.md](https://github.com/peridotan/security-intelligence-library/blob/main/ARTICLE_WORKFLOW.md)、[EVIDENCE_REVIEW.md](https://github.com/peridotan/security-intelligence-library/blob/main/EVIDENCE_REVIEW.md)、[記事テンプレート](https://github.com/peridotan/security-intelligence-library/tree/main/templates)を参考に、**自分の内容と分類体系に合わせて**記事・Evidence JSON・人間のレビュー表を導入します。

元の `scripts/article_workflow.py` 等は、特定のカテゴリ、Topics、テンプレート、Evidence構造を前提にしています。**Step 2のファイルをコピーするだけでは、元サイトの完全な記事制作パイプラインは動きません。** 必要な依存ファイルを別途確認し、検証・テストしたうえで段階的に導入してください。AIがドラフトを作る場合も、人間の根拠確認・公開承認は省略しません。

## 5. Step 4：必要なら高度な機能を追加する

元SILでは記事のFront Matterから各一覧を生成し、Monthly / Quarterlyで内容を再編集し、Vulnerability / Threat Investigationダッシュボードとの連携も行っています。ただし、以下は最小構成の対象外です。

| 機能 | 追加で必要なこと |
| --- | --- |
| 自動生成のカテゴリ・月次・Topic一覧 | Front Matter、分類語彙、`scripts/build_indexes.py` 等と表示テンプレートを整合させる |
| Evidence ReviewのCI強制 | 自分のEvidence JSONの構造と承認プロセスを設計する |
| AIによる補完調査・記事Draft | 外部のAI実行基盤、実行権限、レビュー条件を個別に準備する |
| Vulnerability / Threat連携 | 相手側のデータ・URL・API仕様を用意し、Suite専用コードの固定URLや参照先を変更する |
| Suite E2Eテスト | 自分の公開URLや連携先に合わせてシナリオを作り直す |

例えば、元の公開ワークフロー `docs.yml` には、`peridotan/threat-investigation-dashboard` のチェックアウトと `check_suite_handoff.py` が含まれます。**これを無変更で別サイトへ持ち込むと、元のSuiteへの依存が残ります。** Step 1で生成した独立したPagesワークフローを基点に、必要な機能だけ追加してください。

## 6. 公開前の確認リスト

- [ ] サイト名、URL、README、著作権表示を自分のサイト用に設定した
- [ ] 元SILの掲載記事・独自解説・画像を、許諾なく転載していない
- [ ] コピーしたMITソフトウェアには著作権・許諾表示を保持した
- [ ] 情報源の利用規約と取得頻度、失敗時の警告を確認した
- [ ] GitHub Actionsの書き込み権限は必要なWorkflowに限定した
- [ ] 収集した候補の自動採用・自動公開が起こらないことを確認した
- [ ] 記事の根拠を人間が確認できるようにした
- [ ] ローカルビルド、PR差分、公開ページ、モバイル表示を確認した
- [ ] 秘密情報、顧客情報、個人情報、非公開資料を含めていない

## 7. どこまで再現性を確認したのか

本リポジトリでは、[独立した再現テスト](https://github.com/peridotan/security-intelligence-library/blob/main/scripts/smoke_build_your_own.sh)を用意しています。GitHub Actionsの[Build Your Own Reproduction](https://github.com/peridotan/security-intelligence-library/blob/main/.github/workflows/build-your-own-smoke.yml)で、ガイドの変更時に検証します。

このテストは一時ディレクトリに新規Zensicalサイトと独立したGitリポジトリを作成し、**SILのコードだけを選択取得**して、ローカルのRSS試験データを収集・Triageまで流します。テスト完了後は一時ファイルを削除し、元の公開リポジトリや記事を変更しません。

実行コマンド（元のリポジトリを取得した状態で実行）：

~~~bash
python -m pip install -r requirements.txt
bash scripts/smoke_build_your_own.sh
~~~

このテストで確認するのは**最小構成のサイト生成・ビルド、MITコードの選択取得、RSS収集とWatch振り分け**です。実際の新規GitHubリポジトリ作成、Pagesへのデプロイ、GitHub ActionsからのレビューPR作成、記事・Evidenceの本番運用、AIや他ダッシュボードとの連携は検証対象外です。これらは各自の権限・運用条件で別途確認してください。

## 8. 困ったとき・今後の拡張

| 症状 | 確認ポイント |
| --- | --- |
| Pagesが公開されない | PagesのSource、`docs.yml`、workflow実行ログ、`site_url` |
| 候補0件 | 遡及日数、情報源の公開日、既存URLとの重複 |
| 収集の警告 | RSSの形式変更、アクセス制限（403/429）、配信元の一時障害 |
| 自動PRが作られない | ActionsのPR作成権限、`GITHUB_TOKEN`、候補0件、レビュー担当の設定 |
| CIが元のThreat連携で失敗 | 元のSuite専用ワークフローや固定URLを流用していないか |
| 記事生成でエラー | テンプレート、カテゴリ、Topics、Evidence設定との整合 |

**最初の完成形は「自分のサイトが公開され、候補収集のレビューPRを人間が確認できること」です。** 記事生成、AI、月次・四半期、他のダッシュボード連携は、その後で少しずつ増やす方が、出典管理と運用の再現性を保ちやすくなります。

本ガイドは元実装と公式ドキュメントを突き合わせた構築手順であり、すべてのGitHubアカウント設定・OS・外部配信元での動作を保証するものではありません。動かない箇所は実行ログを保存して確認してください。

関連情報：[How It Works](how-it-works.md) / [About / Editorial Policy](index.md) / [元のGitHubリポジトリ](https://github.com/peridotan/security-intelligence-library) / [Zensical公式ドキュメント](https://zensical.org/docs/create-your-site/)。

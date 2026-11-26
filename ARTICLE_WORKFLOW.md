# 記事制作・Evidence Review・公開の標準ワークフロー

この手順は、NICT A2B攻撃の試験運用（[Draft PR #39](https://github.com/peridotan/security-intelligence-library/pull/39) → [公開PR #40](https://github.com/peridotan/security-intelligence-library/pull/40)）で確認した工程を、**通常の記事にも繰り返し適用**するためのものです。

**役割分担**：GitHub Actions＝収集・重複確認補助・形式検証・サイト公開、ChatGPT Work＝一次情報に基づく記事・根拠JSONのDraft、人間＝記事採用・根拠の実質確認・公開承認・PRマージ。

AIの出典照合と**人間の確認・承認は異なる行為**です。CIの成功は情報の真実性や人間の実レビューを保証しません。

候補の編集上の採否、評価スコア（試行）、判断理由の記録基準は [SECURITY_INTELLIGENCE_SELECTION_POLICY.md](SECURITY_INTELLIGENCE_SELECTION_POLICY.md) を参照してください。点数だけで採否や公開を決めるものではなく、従来どおり人間の判断とEvidence Reviewを必要とします。

## 全体像

| Phase | 主担当 | 実施内容 | 完了条件 |
| --- | --- | --- | --- |
| 0. Triage | GitHub Actions＋人間 | route、重複、既存記事との関係を確認 | Library採用対象が明確 |
| 1. Draft | Work＋編集担当者 | 一次資料を確認、記事と根拠JSONを作成 | 未解決事項を区別したDraft |
| 2. Evidence Review | AI補助＋**人間** | 重要主張・根拠のページ/節を照合 | 担当者が判断できる |
| 3. Draft PR | 編集担当者 | Draftと根拠・レビュー表をPR提出 | 未公開・未マージ |
| 4. Publication | 編集担当者 | 人間の承認を記録、公開状態・生成ファイルを反映 | 必須CI成功 |
| 5. Merge / Pages | **人間**＋GitHub Actions | マージ・デプロイ・ブラウザ表示確認 | サイトの目視チェック完了 |

NICT試験では説明のためPRを2本に分けました。今後は**同じDraft PRを更新してPhase 3→5まで進めても構いません**。

## 複数記事の一括公開（標準）

同じ編集サイクルの候補は記事単位でレビューし、承認済みの記事だけを最新mainから作成した1本の公開PRに集約する。単独公開が必要な場合は従来の単一記事手順も利用できる。未承認記事、watch候補、未解決の根拠を含む記事は公開PRから除外する。

### 承認前のレビュー表

```bash
python scripts/batch_review.py --article drafts/ai-security/example-article.md --article drafts/identity-security/example-existing-update.md
```

実際のDraftパスを明示する。対応する `drafts/evidence/<Draftファイル名>.json` と `drafts/reviews/<Draftファイル名>.md` が必要。新規・既存記事更新の両方を扱う。標準出力には本文/Evidence/編集レビュー表と更新元本文・既存EvidenceのSHA-256（原本が存在しない場合はnull）、主張、分類、検証状態、参照箇所、URL、独自評価理由、未解決件数が出る。結果は人間向けレビュー資料であり、承認記録ではない。未解決主張がある場合は表を出力した上で終了コード2を返す。構造不正は終了コード1。

### 承認後の公開ファイル準備（任意CLI）

人間がレビュー表を確認した後、承認記録JSONを作成する。新規記事は original_sha256 と original_evidence_sha256 を null、更新は現行原本のSHA-256（既存Evidenceがなければ後者はnull）にする。レビューMarkdownのSHA-256も記録する。ハッシュは実ファイルから取得し、承認後に再計算して承認済みと見なさない。

~~~json
{
  "schema_version": 1,
  "base_commit": "<実際の40桁のmainコミットSHA>",
  "articles": [
    {
      "draft": "drafts/ai-security/example-article.md",
      "decision": "approved",
      "reviewed_by": "<実際の人間の担当者>",
      "reviewed_at": "YYYY-MM-DD",
      "publication_date": "YYYY-MM-DD",
      "article_sha256": "<承認時のSHA-256>",
      "evidence_sha256": "<承認時のSHA-256>",
      "review_sha256": "<承認時のSHA-256>",
      "original_sha256": null,
      "original_evidence_sha256": null
    }
  ]
}
~~~

上記は記入例であり承認ではない。最新mainをfetchし、そのコミットから作成した公開用ブランチで次を実行する。原本docs/reviewは未変更であること。Draftは別途配置する。

~~~bash
git fetch origin main
python scripts/batch_prepare.py --manifest /path/to/human-approved.json --output /path/to/new-publication-bundle
~~~

出力はリポジトリ外の新規ディレクトリに限定し、原本は変更しない。全件の承認・ハッシュ・未解決主張・更新元の整合性を先に確認し、不一致なら全体を拒否する。出力したdocs、review/evidence、review/pilots、review/publication-batchesを確認して公開用ブランチへ取り込み、第5節の生成・CIを実行する。一括公開のコミットには必ず `git add review/publication-batches/` で監査記録を含める。既存記事の更新は初回公開日を保持する。旧Evidenceの差分レビューでは過去の主張の保持も人間が確認する。承認記録は人間の申告であり、CLIは本人性や実質レビューを証明しない。取り込み直前にmainの変化を確認し、競合時は再レビューする。

### 一括公開の実施

1. 人間が対象記事とレビュー表を確認し、記事ごとに公開を明示承認する。承認者・日付・対象ファイルのハッシュを編集レビュー記録に残す。
2. 最新mainから一つの公開ブランチを作成する。承認時のハッシュと取り込むDraft/Evidenceを照合する。変更があれば再レビューする。
3. 新規記事は既存ファイルへの衝突を確認して掲載パスへ移す。既存記事更新は承認時の元記事と現在のmainを比較し、変更があれば再レビューする。既存URLと初回公開日は保持する。承認済みファイルだけを取り込む。
4. Evidenceをapprovedにし、実際の担当者・日付を記録する。承認前の注意書きは履歴と明示し、現時点の状態と矛盾させない。承認対象の主張・根拠は変更しない。
5. 全記事を取り込んだ後に第5節の生成コマンドを一括で実行する。一つの公開PRにまとめ、最新CI成功・最終差分確認後、人間がマージする。
6. mainが途中で進んだ場合は再同期し、既存記事の競合と承認対象の変更を確認し、生成とCIを再実行する。生成差分の手書きやCIの迂回は不可。
7. 第6節の公開確認を行う。公開PRに取り込まなかったDraftは未公開のまま管理し、公開済みの個別Draft PRは重複マージしない。

この手順は公開PRの作成・承認・マージを自動化するものではない。レビュー表生成は読み取り専用であり、実質的な根拠確認や承認を代行しない。

## 0. 収集・記事採用判断

通常は [WORK_AI_DRAFTING.md](WORK_AI_DRAFTING.md) の条件に従い、マージ済みTriage PRから **triage.route = library** かつ **triage.draft_eligible = true** の候補を選びます。

手動発見の場合は [WORK_SUPPLEMENTAL_DISCOVERY.md](WORK_SUPPLEMENTAL_DISCOVERY.md) に沿って、new / update-existing / duplicate / watch / vulnerability を判断し、採用者・理由・既存記事との関係をレビュー記録に残します。update-existingなら新しい記事を作らず既存記事を更新します。watch・vulnerabilityは人間がLibrary向けに昇格判断するまで記事にしません。

## 1. 記事セットのひな形を作る

ローカルリポジトリで**機能ブランチを作ります**。mainへ直接コミットしません。

~~~powershell
git switch main
git pull --ff-only
git switch -c article/sample-api-risk
python scripts/article_workflow.py init --collection cybersecurity --slug sample-api-risk --title "公開APIのリスクと実務上の示唆" --draft-date 2026-10-16 --source-period 2026-10
~~~

作られるファイルは3つです。

- **drafts/cybersecurity/sample-api-risk.md**：記事ひな形。statusはdraft、review_statusはNeeds Review
- **drafts/evidence/sample-api-risk.json**：根拠JSON。review.statusはpending
- **drafts/reviews/sample-api-risk.md**：人間向け編集レビュー表

テンプレートには **TODO、ダミーURL、未入力日付** が残ります。これは未確認の内容を誤って公開しないためです。必ず実際の出典・原稿で置き換えます。既存ファイルは上書きしません。日付はコマンド実行者が明示するため、システムが勝手に推測しません。

ChatGPT Workを使用する場合は [WORK_AI_DRAFTING.md](WORK_AI_DRAFTING.md) に沿って記事Markdown・根拠JSON・レビューサマリーを生成し、上記3か所に配置します。Work自体はGitHubへのプッシュ・承認・公開を行いません。

## 2. 記事と根拠の対応を確認する

記事は [templates/article-template.md](templates/article-template.md) の構成に従い、Topicsは [config/topics.yml](config/topics.yml) から1〜3個選びます。根拠JSONは [templates/evidence-review-template.json](templates/evidence-review-template.json) と [EVIDENCE_REVIEW.md](EVIDENCE_REVIEW.md) に準拠させます。

- **source_fact**：一次資料から直接確認できる事実
- **source_claim**：発行元の見解・推測・予測など。記載の確認と独立の真実性は別物
- **library_assessment**：Library独自の分析・対応提言。根拠となる推論理由を記録

各重要主張に実際のURL、該当するページ・節・表番号、閲覧日を記載します。未確認事項はneeds_review / unsupportedとし、数値・日付・出典を補いません。

~~~powershell
python scripts/article_workflow.py check --collection cybersecurity --slug sample-api-risk
~~~

コマンドは**記事・根拠JSON・見出し対応とテンプレートの残存**を確認するだけです。出典の実質的な真偽や人間の承認を代行しません。未入力のテンプレートは意図的にチェックに失敗します。

## 3. Draft PRを作る

GitHub CLIを利用できる場合の例です。

~~~powershell
git add drafts/cybersecurity/sample-api-risk.md drafts/evidence/sample-api-risk.json drafts/reviews/sample-api-risk.md
git commit -m "Draft API security article with evidence"
git push -u origin article/sample-api-risk
gh pr create --draft --base main --title "[Article Review] 公開APIのリスクと実務上の示唆" --body-file drafts/reviews/sample-api-risk.md
~~~

GitHub CLIがなければ、GitHub Pull Requests画面から **Create draft pull request** を選びます。レビュー表の内容をPR本文へコピーしてください。

**公開リポジトリのDraft PRはGitHub上では誰でも閲覧できます。** 機密情報・未公開の顧客情報・個人情報は含めないでください。PRはこの時点でマージしません。

## 4. 掲載パスへ移動して人間が承認する

人間のレビューが進んだら、まだ記事がdraft、根拠JSONのレビューがpendingの間に、次のコマンドで掲載場所へ移動します。

~~~powershell
python scripts/article_workflow.py stage --collection cybersecurity --slug sample-api-risk
~~~

移動先は以下のとおりです。

- **docs/cybersecurity/sample-api-risk.md**
- **review/evidence/sample-api-risk.json**
- **review/pilots/sample-api-risk.md**

このコマンドは形式と見出しの整合を確認し、移動先が既存なら中断します。**承認者や承認日、記事のpublished状態、PRを一切自動設定しません**。docs下のDraftが直接URLから閲覧できる場合があるため、内容の公開判断が終わる前にPRをマージしないでください。

人間が実際に重要な主張を確認し、正式に掲載を承認した後に限り、根拠JSONの **review.status = approved / reviewed_by = 実際の担当者 / reviewed_at = 実際の日付** を記録します。未確認の重要主張は出典再確認・修正・削除等で解消します。CI通過だけのためにverifiedへ書き換えてはいけません。

その後、記事を **status: published / review_status: Current** に変更し、日付を確定します。

## 5. 生成ファイルを更新し、PR品質チェックを確認する

~~~powershell
python scripts/build_indexes.py
python scripts/build_context_index.py
python scripts/sync_article_metadata.py
python scripts/check_content.py
python scripts/check_evidence_review.py --base-ref origin/main
git diff --check
git add docs/ review/evidence/ review/pilots/
# 一括公開の場合は監査記録も追加する（単一記事の場合は不要）
# git add review/publication-batches/
git commit -m "Publish reviewed article with Evidence Review"
git push
~~~

必須チェック **Validate Security Intelligence PR / Content, indexes, Suite and site** が、Evidence Review、サイト生成、Suite連携、HTML・内部リンク、インデックスの派生ファイルまで確認します。生成結果が未コミットだと意図的に失敗するため、生成したdocs差分を再コミットして再実行してください。

~~~powershell
gh pr ready
~~~

Draft解除でCIが再実行されます。**最新チェックが成功**し、担当者が最終差分を確認してから、人間がGitHubのPRをマージします。mainへのpush後のGitHub Pages公開は [.github/workflows/docs.yml](.github/workflows/docs.yml) が行います。PR検証の仕組みが公開・マージすることはありません。

## 6. デプロイと公開ページを確認する

Pagesデプロイ後に `scripts/check_deployed_site.py` が生成HTMLとContext Index JSONを公開URLから取得し、ビルド成果物とのSHA-256一致を確認する。キャッシュ・一時的な失敗は限定回数再試行し、継続する不一致はActionsを失敗として記録する。デプロイ自体を取り消す仕組みではない。Actionsの結果を確認した上で、公開ページをブラウザで開き、タイトル、日付・メタデータ、本文、目次、脚注・出典リンク、関連記事、モバイル表示を確認します。**CIの成功は見た目や参照先の正しさまで保証しません**。問題があれば別PRで修正します。

## 単一記事CLI（article_workflow.py）が自動化しないこと

AIやWebへの問い合わせ、記事自動作成、内容の真偽判定、人間のEvidence Review承認、承認日・承認者の記入、PRの自動作成、publishedへの変更、マージ、Pagesへのデプロイ、既存記事の上書き。

CLIの回帰テストは次で実行できます（必須PR CIにも組み込みます）。

~~~powershell
python -m unittest discover -s scripts -p "test_article_workflow.py" -v
~~~

## 例外時の扱い

- 重複を発見：既存記事の更新・watchを優先
- 出典が失効・消失：別ソースを勝手に捏造しない。needs_reviewで保留
- 必須主張の裏付けが弱い：公開前に削除・修正、必要なら公開を延期
- 生成差分が残る：生成・コミット・CI再実行
- botが作成したPRでCIが走らない：GITHUB_TOKEN起点のワークフロー抑制などを確認。必須チェックを迂回してマージしない

関連文書： [WORK_AI_DRAFTING.md](WORK_AI_DRAFTING.md)、[WORK_SUPPLEMENTAL_DISCOVERY.md](WORK_SUPPLEMENTAL_DISCOVERY.md)、[EVIDENCE_REVIEW.md](EVIDENCE_REVIEW.md)、[PR_QUALITY_GATE.md](PR_QUALITY_GATE.md)。

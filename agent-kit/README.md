# Security Intelligence Agent Kit

このZIPは、情報を収集・選定・分析して人間の承認を経て公開する**運用設計のたたき台**です。SILの複製サイト、記事データ、完成済みの自動収集プログラム、実行環境、AI API、GitHub Actionsの設定は含みません。

## 内容
- `STARTER_PROMPT.md` — 新規プロジェクトの初期設計・段階的な開発を依頼するプロンプト
- `AGENTS.md` — リポジトリ単位の継続的な開発・編集原則の例
- `.agents/skills/*/SKILL.md` — Discovery / Triage / Article Drafting / Evidence Review / Monthly / Quarterly の6つの反復ワークフロー
- `LICENSE.txt` — 配布する運用テンプレート・Skill・ソフトウェアのMITライセンス

## 導入手順
1. `STARTER_PROMPT.md`を読み、対象分野・利用者・使用する基盤を自分用に置き換える。
2. 新しいリポジトリを作り、`AGENTS.md`と`.agents/skills/`をコピーする。既存のAGENTSやSkillを上書きする前に差分を確認する。
3. `AGENTS.md`に登場する`SECURITY_INTELLIGENCE_SELECTION_POLICY.md`、`ARTICLE_WORKFLOW.md`などは**元SIL固有の参照先**で、ZIPには含まれない。自分の運用文書・分類体系・スクリプトの実在するパスへ書き換える。存在しない工程を「実行済み」としない。
4. CodexなどSkillを認識するエージェントにはリポジトリ直下の`.agents/skills/<skill-name>/SKILL.md`を使用する。別環境のChatGPT Work等では対象ファイルを明示的に読ませる。ツール・権限・スケジュールは別途接続する。
5. 最初は手動レビュー付きの小さなフローでテストし、権利・秘密情報・根拠・公開前承認を確認する。

## ライセンスと制約
この配布物に含まれる新規のガイド・Skill・ソフトウェアテンプレートはMITライセンスで配布します。著作権表示とライセンス本文を保持してください。元SILの`docs/`掲載記事、独自分析や第三者コンテンツは**配布していません**。事実・アイデアの利用と、記事の原文転載は区別してください。

**人間の判断を機械に置き換えるものではありません。** AI出力、CI成功、スコア値だけで記事採用・根拠承認・公開を自動化しないでください。

元実装（参考）：https://github.com/peridotan/security-intelligence-library
公式Skill形式：https://learn.chatgpt.com/docs/build-skills

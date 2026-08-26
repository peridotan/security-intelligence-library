---
title: 生成AI利活用ガバナンス ― 禁止事項だけでなく「安全に使える仕組み」を作る
date: 2026-08-14
updated: 2026-08-26
description: 生成AI利活用ガバナンスを、利用類型・リスク・統制・教育・モニタリングの観点から企業向けに整理する。
category: AI Security
tags:
  - AI Governance
  - Generative AI
  - Risk Management
  - Security for AI
  - Regulation
audience:
  - Executive
  - CISO
  - Risk Management
management_impact: High
status: published
pptx: ""
---

# 生成AI利活用ガバナンス ― 禁止事項だけでなく「安全に使える仕組み」を作る

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-14</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

生成AIガバナンスは、「機密情報を入力しない」「回答を鵜呑みにしない」という利用規約だけでは機能しません。利用が広がるほど、個人利用、業務組込み、AI Agent、モデル開発などでリスクが異なり、**同じ禁止事項を全ケースに当てはめると、過剰統制か統制不足のどちらか**になります。

企業が作るべきなのは、利用目的とリスクに応じて、使えるサービス、入力できるデータ、必要なレビュー、外部公開、権限、ログ、インシデント対応を決める**リスクベースの利用ガバナンス**です。METIのAI事業者ガイドライン第1.2版、NIST AI RMF / Generative AI Profile、OECDのResponsible AI Due Diligenceなども、AIをライフサイクル全体で継続的に管理する方向性を示しています。

</div>

## なぜ今なのか

生成AIは、単独のチャット利用から、社内データを参照するRAG、業務アプリへの組込み、AI Agentによる操作へ広がっています。利用形態が変わると、入力情報漏えいだけでなく、アクセス権限、誤操作、第三者サービス、著作権、個人情報、説明責任、モデル更新などがリスクになります。

日本ではAI事業者ガイドラインが継続的に更新され、2026年3月31日に第1.2版が公開されています。NIST AI 600-1は生成AI固有・増幅されるリスクを整理し、Govern / Map / Measure / Manageの考え方で継続管理を示しています。

## 「生成AI利活用」を類型で分ける

ガバナンスを実務化するには、まず利用を一括りにしないことが重要です。例えば次の4類型に分けると、必要統制を整理しやすくなります。

| 利活用類型 | 例 | 主なリスク |
| --- | --- | --- |
| ① 生成AIサービス利用 | ChatGPT等を従業員が利用 | 情報入力、誤回答、著作権、Shadow AI |
| ② AIアプリケーション | RAG、Copilot、社内AIアプリ | Data Access、Prompt Injection、出力利用 |
| ③ AI Agent | SaaS操作、コード変更、業務自動化 | Identity、権限、Tool Misuse、誤操作 |
| ④ AIモデル開発・運用 | Fine-tuning、独自モデル | Training Data、Model Security、Supply Chain |

類型は「成熟度」とは別です。同じAI Agentでも、PoC段階と全社基幹業務への本番導入では必要な統制が異なります。したがって、**類型 × 重要度 / 成熟度 × リスク**で管理するのが実務的です。

## ガバナンスで定義すべき10領域

### 1. 利用目的・Use Case分類

- 利用目的とBusiness Owner
- PoC / 本番の区別
- 高リスク用途の定義
- 人の最終判断が必要な業務

### 2. 利用サービス・モデル

- 会社承認済みサービス
- Enterprise契約 / 個人契約の扱い
- 学習利用、保存期間、データ所在
- モデル・機能更新時の再評価

### 3. データ

- 機密、個人情報、顧客情報、知財の入力可否
- RAGデータへのAccess Control
- Data Loss Prevention / AI Gateway等の利用
- ログに機密情報が残るリスク

### 4. Identity / Access

- 誰がどのAIを利用できるか
- Agent / NHIのIdentityと権限
- 最小権限、JIT、短命Credential
- 管理者権限・外部システム操作の承認

### 5. 出力の信頼性

- Hallucinationの許容範囲
- 出力を人がレビューすべき条件
- 根拠・引用・参照元の確認
- 自動実行前のValidation

### 6. Legal / Compliance

- 個人情報保護
- 著作権・ライセンス
- 契約上の守秘義務
- 業法・規制・説明責任

### 7. Security for AI

- Prompt Injection
- Sensitive Information Disclosure
- Supply Chain
- Excessive Agency
- Agent Identity / Privilege Abuse

### 8. Third Party / Procurement

- AI Providerのセキュリティ評価
- Subprocessor / Model Provider
- インシデント通知
- Exit Plan / Vendor Lock-in

### 9. Monitoring / Incident Response

- 利用状況・Shadow AIの可視化
- High-risk操作ログ
- 誤回答、情報漏えい、Agent誤操作の報告窓口
- Credential失効、Agent停止、データ削除の手順

### 10. Education / Change Management

- 利用者向け基本教育
- 開発者・管理者向け専門教育
- 事例共有
- ガイドラインを定期更新する仕組み

## 禁止中心のガバナンスが失敗しやすい理由

「生成AIは禁止」「機密情報は禁止」とだけ規定すると、利用者は業務上便利な非承認サービスへ流れ、Shadow AIが増える可能性があります。一方、全面自由化すると、個人契約や不明なデータ利用条件が混在します。

有効なガバナンスは、**安全な選択肢を用意し、リスクの高い用途だけ統制を強くする**ものです。例えば、一般文書の要約は承認済みEnterprise AIで自由に使える一方、顧客個人情報を使うRAGや外部システムを操作するAgentは追加審査対象とします。

## 経営インパクト

| 観点 | ガバナンス不足 | 過剰統制 |
| --- | --- | --- |
| 生産性 | Shadow AI、バラバラの利用 | 利用が進まず競争力低下 |
| 情報 | 機密・個人情報漏えい | 安全な活用機会を失う |
| 品質 | 誤回答の無検証利用 | 人手レビュー過多でROI低下 |
| Security | Agent権限・Secretの乱立 | PoC止まりで統制知見が蓄積しない |
| Compliance | 説明責任・契約違反 | ルールが複雑化し守られない |

<div class="sil-action-box" markdown>

## 推奨アクション

1. **AI利用台帳を作る** — サービス、Use Case、Owner、データ、外部接続、重要度を記録する。
2. **4つの利活用類型でルールを分ける** — 生成AI利用、AIアプリ、AI Agent、モデル開発を同じ規定で扱わない。
3. **承認済みの安全な利用経路を用意する** — Enterprise契約、SSO、ログ、データ保護を備え、Shadow AIを減らす。
4. **高リスク条件を明示する** — 個人情報、顧客判断、外部公開、コード本番反映、AgentによるWrite操作などを追加審査対象にする。
5. **Human-in-the-Loopをリスクベースにする** — 全出力をレビューするのではなく、影響の大きい判断・操作を重点化する。
6. **Security / Legal / Risk / Businessを同じプロセスにする** — 別々の審査を増やさず、共通のUse Case評価へ統合する。
7. **四半期ごとにルールを見直す** — モデル能力、Provider機能、事故、規制の変化を反映する。

</div>

## 成熟度の見方

| 段階 | 状態 | 次の課題 |
| --- | --- | --- |
| M0 未管理 | 個人判断・Shadow AI | 可視化 |
| M1 可視化 | 利用台帳、承認サービス | 基本ルール |
| M2 統制 | データ・Access・レビュー基準 | 継続監視 |
| M3 継続統制 | ログ、リスク評価、インシデント対応 | 自動化・最適化 |
| M4 最適化 | リスクに応じて統制を動的調整 | 経営指標・継続改善 |

成熟度は「AIをどれだけ高度に使っているか」だけではなく、**その利用をどこまで可視化・統制・改善できているか**という観点も別途評価する必要があります。

## 用語解説

**AI Governance**  
AIの開発・提供・利用について、責任、リスク許容度、ルール、監視、改善を定める仕組み。

**Human-in-the-Loop (HITL)**  
AIの判断・操作の一部に人間の確認や承認を組み込む設計。すべてを人が確認するという意味ではない。

**Shadow AI**  
企業が承認・把握していないAIサービスやAI機能を従業員が業務利用している状態。

## 関連記事

- [AI Agent Identity / NHI ― AI Agentを「操作主体」として統制する](../identity-security/ai-agent-identity-nhi.md)
- [Frontier AIのサイバー能力が「Critical」に近づく意味](frontier-ai-cyber-capabilities.md)

## PowerPoint

対応する公開可能なPowerPoint版は、今後このページからリンクします。

## 参考情報

- 経済産業省 / IPA・AISI, AI事業者ガイドライン 第1.2版 (2026-03-31)  
  https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/20260331_report.html
- NIST, AI Risk Management Framework  
  https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI 600-1, Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile  
  https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- OECD, Due Diligence Guidance for Responsible AI (2026)  
  https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/02/oecd-due-diligence-guidance-for-responsible-ai_7831bb49/41671712-en.pdf
- OWASP Gen AI Security Project, Top 10 for Agentic Applications for 2026  
  https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

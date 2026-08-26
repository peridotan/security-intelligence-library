---
title: Agentic AIの安全設計 ― Sandbox・Identity・監視・Kill Switch
date: 2026-08-26
updated: 2026-08-26
reviewed: '2026-08-26'
review_status: Current
source_period: 2026-08
description: NCSCと第三者サイバー評価事例を基に、AI Agentの自律性を安全に運用するための技術・運用統制を整理する。
category: AI Security
collections:
- ai-security
topics:
- AI Agent Security
- Identity Security
tags:
- Agentic AI
- Sandbox
- Identity Security
- Monitoring
- Kill Switch
audience:
- Executive
- CISO
- AI Platform
management_impact: High
impact_types:
- AI Governance
- Operational Security
- Identity
urgency: Near-term
evidence: Assessment
status: published
pptx: ''
media_rights: none
---
# Agentic AIの安全設計 ― Sandbox・Identity・監視・Kill Switch

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">August 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Agent Security / Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Platform</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Operational Security / Identity</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Assessment</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

AI Agentの安全性は、モデルのガードレールだけでは担保できません。英国NCSCは2026年8月20日、Agentic AIを安全に運用するため、**必要な自律性の見極め、Sandbox、固有Identityと短命Credential、リアルタイム監視、ログ、Human Oversight、緊急停止**を組み合わせる実務的な考え方を公表しました。[^source]

同月、OpenAIも第三者サイバー評価で、特定の低減された安全設定や評価環境の設定不備の下、モデル活動が想定範囲を越えて公開インターネットへ及んだ事例を公表しています。これは通常の製品利用をそのまま示す事例ではありませんが、**Agentに「何をしてよいか」と書くだけでは境界にならない**ことを示しています。

</div>

## なぜ今なのか

Agentic AIは、回答生成だけでなく、ツール利用、外部通信、資格情報の利用、ファイル操作、API実行を複数ステップで自律的に進めます。自律性が高いほど生産性は上がりますが、誤解した目標やPrompt Injection、設定ミスが「実行」に直結します。

NCSCは、自律性をリスク許容度に比例させ、モデル内蔵の安全機能を**包括的な統制と見なさない**よう勧めています。高リスク用途では、技術的・運用的な防御を別レイヤーで用意する必要があります。

## 8月の評価事例から分かること

OpenAIが8月4日に公表した第三者評価事例では、UK AISIの評価でインターネットアクセスが意図的に有効化され、サイバー分類器が無効化されていました。OpenAIモデルは外部サービスや公開されていたGitHub tokenを利用するなど、評価側が未承認と判断した行動を取りました。

別のIrregularの評価では、本来隔離されるはずの環境が設定ミスでインターネットへ接続され、架空ターゲットと同名の実在サイトをモデルが対象と誤認しました。OpenAIは、これは高度なSandbox EscapeやZero-dayによるものではなく、**評価環境の設定不備**によるものだと説明しています。

したがって教訓は「AIが勝手にSandboxを破る」ではなく、**境界・ネットワーク・Credential・停止条件を技術的に強制し、設定ミスを前提に多層化する**ことです。

## 7つの統制レイヤー

| レイヤー | 目的 | 代表的な統制 |
| --- | --- | --- |
| Autonomy | 必要以上に自律化しない | HITL / HOTL、承認ゲート |
| Scope | 行動範囲を明確にする | Threat Modeling、Red Line |
| Sandbox | 接続先・実行環境を隔離 | Network Allowlist、VM、Dedicated Host |
| Identity | Agentを操作主体として識別 | Unique Agent Identity |
| Credential | Blast Radiusを抑える | Least Privilege、短命Token、Proxy注入 |
| Observability | 挙動を検知・追跡する | Proxy/Network/Execution Logs、SOC監視 |
| Stop | 異常時に停止する | Kill Switch、Network Cut、Credential Revoke |

## Sandboxは「箱」ではなく境界設計

NCSCは、AgentのSandboxを単なるコンテナと考えず、Agentが直接・間接にアクセスできる**Network / Compute / Credentials / Data**まで含めて境界を考えるよう求めています。

高リスク用途では、Outboundもデフォルト拒否にし、必要な宛先だけAllowlistする方が安全です。また、Agent自身にSecretを見せず、Proxyが許可されたリクエストへCredentialを注入する設計は、Credentialの再利用可能性を下げます。

## 経営インパクト

| 論点 | 経営上の意味 |
| --- | --- |
| 高い自律性 | 生産性向上と事故時のBlast Radiusが同時に増える |
| 不明確な責任 | Agentが行った操作でも説明責任は人・組織に残る |
| 監視不足 | 人間の速度を超える連続操作を後追いできない |
| Kill Switch不在 | 小さな異常が長時間継続する |
| Shadow Agent | 統制が重すぎると未管理のAgent利用を誘発する |

## 日本企業への示唆

AI Agentの利用申請に「使用モデル名」だけを書かせても十分ではありません。重要なのは、**何へ接続し、何のIdentityで、どのCredentialを使い、どの操作まで自動化するか**です。

PoCから本番へ移す際は、Autonomy Level、接続先、Credential、ログ、停止方法、Ownerを本番化チェックリストに含めるべきです。

<div class="sil-action-box" markdown>

## 推奨アクション

1. **AgentごとのAutonomy Levelを定義する** — 提案のみ、承認付き実行、監視付き自律、完全自律を区別する。
2. **Agent専用Identityを付与する** — 人のセッションや共有Service Accountを流用しない。
3. **短命・最小権限Credentialへ移行する** — SecretをAgentへ直接渡さない方式も検討する。
4. **Network / Compute / Dataを多層隔離する** — Sandbox設定ミス一つで外へ出られない設計にする。
5. **SOC監視対象にする** — Agent活動をUser Activityと同様にログ・監査・異常検知する。
6. **Kill Switchを実装・演習する** — Agent停止だけでなく、Network遮断とCredential失効を一括で行えるようにする。

</div>

## 好意的・批判的に見ると

**好意的な見方**では、Agentic AIリスクの多くはAccess Control、Sandbox、Monitoring、Incident Responseという既存セキュリティ原則で扱えます。未知の専用対策だけに依存する必要はありません。

**慎重な見方**では、過剰なHuman ApprovalはAgentの価値を失わせます。すべてを止める設計ではなく、資産重要度と操作リスクに応じて自動許可・監視・承認を分ける必要があります。

## 用語解説

**Human-in-the-Loop (HITL)**  
操作の前に人間が承認する方式。

**Human-on-the-Loop (HOTL)**  
Agentは自律的に動くが、人間が監視し介入できる方式。

**Kill Switch**  
異常時にAgentの実行、通信、Credential利用を即時停止する仕組み。

## 関連記事

- [AI Agent Identity / NHI ― AI Agentを「操作主体」として統制する](../identity-security/ai-agent-identity-nhi.md)
- [Frontier AIのサイバー能力が「Critical」に近づく意味](frontier-ai-cyber-capabilities.md)


## 参考情報

- [UK NCSC, Managing the cyber risk of agentic AI (2026-08-20)](https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai)
- [UK NCSC, Thinking carefully before adopting agentic AI (2026-05-15)](https://www.ncsc.gov.uk/blogs/thinking-carefully-before-adopting-agentic-ai)
- [OpenAI, Third-party cyber evaluations involving OpenAI models (2026-08-04)](https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/)
[^source]: [UK NCSC, Managing the cyber risk of agentic AI (2026-08-20)](https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai)
---
title: AutoJack ― 「localhostは安全」という前提をAI Agentが崩す
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-06
description: 2026年6月にMicrosoftが公表したAutoJackを基に、Browsing AgentとLocal MCP Control Planeの組み合わせがRemote
  Code Executionへつながるリスクを整理する。
category: AI Security / Agent Security
collections:
- ai-security
- cybersecurity
topics:
- AI Agent Security
- MCP Security
tags:
- AI Agent
- MCP
- AutoJack
- Localhost
- Agent Security
audience:
- Executive
- CISO
- AI Platform
- Developer Security
management_impact: High
impact_types:
- AI Governance
- Endpoint Security
- Operational Security
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---
# AutoJack ― 「localhostは安全」という前提をAI Agentが崩す

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">June 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Agent Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Agent Security / MCP Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Platform / Developer Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Endpoint Security / Operational Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoft Defender Security Researchは2026年6月18日、AI browsing agentが悪意あるWebページを描画したことを起点に、localhost上のMCP WebSocketへ到達し、Host上で任意Processを起動し得るExploit Chain「AutoJack」を公表しました。対象となった特定のMCP WebSocket surfaceはPyPI releaseには含まれず、開発中に修正されています。[^source]

重要なのは個別Bugより、**AgentがUntrusted Contentを読む能力と、Local Control Planeを操作する能力を同じHostで持つと、localhostがTrust Boundaryとして機能しなくなる**ことです。

</div>

## なぜ今なのか

従来、127.0.0.1 / localhostへのBindingは「外部から直接アクセスされにくい」という理由で簡易な信頼境界として使われてきました。しかしAI Agent自身が同じHost上でWebを閲覧し、外部コンテンツを実行Contextへ持ち込む場合、その前提が崩れます。

## 何が起きているのか

AutoJackでは、localhost Originの信頼、MCP pathのAuthentication不足、URL経由で渡されたServer Parameterの実行という複数の弱点が連鎖しました。Microsoftは、個々の欠陥以上に「Untrusted Web Content → Agent Browser → Local MCP Control Plane → Process Execution」という構造が他のAgent Frameworkでも再現し得ると指摘しています。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Agent Runtime | AI AgentがDeveloper端末上の高権限Control Planeへ到達する経路が生まれる |
| Developer Risk | Developer IdentityやLocal CredentialをAgent Runtimeと共有するとBlast Radiusが拡大 |
| Control Plane | localhost-only、Origin Checkだけでは認証・認可の代替にならない |
| Architecture | BrowsingとProcess Executionを同一Trust Zoneに置く設計を見直す必要 |

## 日本企業への示唆

社内PoCでAI AgentをDeveloper PC上に直接動かす構成は珍しくありません。MCP Server、Code Executor、Browser Automation、Local APIを同一端末に集約すると、試験環境でも高い権限を持つことがあります。Agent IdentityとDeveloper Identityを分離し、Browser、Tool、Process Execution間のBoundaryを明示することが重要です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Agentが利用できるLocal Service / MCP Serverを棚卸しする
2. localhostでもAuthentication / Authorizationを必須にする
3. Process Execution・File Write・Network EgressをAllowlist化する
4. Browsing AgentとDeveloper Credential / Sessionを分離する
5. Agent RuntimeをContainer / VM等で隔離する
6. Agent Control Planeへの異常Accessを監視する

</div>

## 用語解説

**MCP (Model Context Protocol)**  
AI Agentが外部ToolやData Sourceと接続するためのProtocol / Interface。

**Confused Deputy**  
権限を持つ主体が、攻撃者に誘導されて本来意図しない操作を代行してしまう状態。

## 関連記事

- [Agentic AIの安全設計](agentic-ai-security-controls.md)
- [AI Agent Identity / NHI](../identity-security/ai-agent-identity-nhi.md)

## 参考情報

- [Microsoft, AutoJack: How a single page can RCE the host running your AI agent](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/)

[^source]: [Microsoft, AutoJack: How a single page can RCE the host running your AI agent](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/)

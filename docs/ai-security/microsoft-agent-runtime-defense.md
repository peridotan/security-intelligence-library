---
title: AI Agent Runtime Defense ― Tool Invocationを「Code Execution」と同じHigh-risk Eventとして守る
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-01
description: Microsoft Defender Security Researchが2026年1月23日に公開したAgent Runtime Securityの研究を基に、Tool
  Invocation、Generative Orchestration、Prompt Injection、Real-time Enforcementを整理する。
category: AI Security / Agent Runtime
collections:
- ai-security
- cybersecurity
topics:
- AI Agent Security
- AI Governance
tags:
- Microsoft
- AI Agent
- Runtime Security
- Tool Invocation
- Generative Orchestration
- Prompt Injection
- Real-time Protection
audience:
- Executive
- CISO
- AI Platform
- SOC
management_impact: High
impact_types:
- AI Governance
- Operational Security
- Data Security
urgency: Near-term
evidence: Assessment
status: published
pptx: ''
media_rights: none
---

# AI Agent Runtime Defense ― Tool Invocationを「Code Execution」と同じHigh-risk Eventとして守る

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">January 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Agent Runtime</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Agent Security / AI Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Platform / SOC</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Operational Security / Data Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Assessment</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoft Defender Security Researchは2026年1月23日、AI AgentのTool InvocationをRuntimeで検査・制御する考え方を公開しました。[^source]

Microsoftの整理では、AgentがToolを呼ぶことは、Dataを読む、Emailを送る、Recordを更新する等の**実世界Actionを実行するCode Executionに近いSecurity Event**です。攻撃者がAgentのPlanをNatural Language経由で操作できると、Systemそのものを侵害せず、Agentに許可された権限の範囲内で不正Actionを実行させる可能性があります。

そのためBuild時のPrompt / Policy Reviewだけではなく、各Tool InvocationのIntent、Destination、ContextをRuntimeで評価し、実行前にAllow / BlockするControlが重要になります。

</div>

## なぜ今なのか

Generative Orchestrationでは、同じInputでもAgentがTool、Knowledge、Topicを動的に組み合わせます。静的なWorkflow Reviewだけでは実行Pathを完全に予測できません。

## Runtime Securityの考え方

<div class="sil-flow" role="group" aria-label="AI agent runtime enforcement flow">
  <div class="sil-flow-step"><strong>User / Event / External Content</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Agent Planning / Generative Orchestration</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Planned Tool Invocation</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Runtime Security Check</strong><span>Intent / Destination / Context</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-branches">
    <div class="sil-flow-step sil-flow-step-action"><strong>Allow</strong></div>
    <div class="sil-flow-step sil-flow-step-impact"><strong>Block / Alert</strong></div>
  </div>
</div>

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| AI Control | Build-time Reviewだけでは不十分 |
| SOC | Agent Actionを新しいTelemetryとして扱う必要 |
| Data | Agent経由のExfiltrationは正規Actionに見える可能性 |
| Approval | Tool単位でRisk-based Enforcementが必要 |

## 日本企業への示唆

Agent Securityでは「禁止Prompt List」より、実際に何を実行しようとしているかを見た方が有効です。Payment、Email送信、権限変更、Code Deployment等はRuntime Enforcement対象として優先できます。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AgentのTool InvocationをLogする
2. High-risk Toolを分類する
3. 実行前Policy Checkを設計する
4. External Content起点のActionを厳格化する
5. Agent ActionをSOCへ通知する
6. Block / Human Approval / Allowの3段階Controlを検討する

</div>

## 用語解説

**Tool Invocation**  
AI AgentがConnector、API、Function、Workflow等を呼び出して外部SystemへActionすること。

## 関連記事

- [NIST CAISI AI Agent Security RFI](nist-caisi-agent-security-rfi-january.md)
- [MCP Tool Poisoning](mcp-tool-poisoning-agent-supply-chain.md)

## 参考情報

- [Microsoft Security Blog, From runtime risk to real-time defense: Securing AI agents](https://www.microsoft.com/en-us/security/blog/2026/01/23/runtime-risk-realtime-defense-securing-ai-agents/)

[^source]: [Microsoft Defender Security Research, Securing AI agents at runtime](https://www.microsoft.com/en-us/security/blog/2026/01/23/runtime-risk-realtime-defense-securing-ai-agents/)

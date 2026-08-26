---
title: Coding Agentをどう守るか ― OpenAIのCodex運用から見るAgent Runtime Security
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-05
description: OpenAIが2026年5月8日に公開したRunning Codex safely at OpenAIを基に、Sandbox、承認、Network
  Access、Credential、Telemetryを統合したCoding Agent Securityを整理する。
category: AI Security / Agent Runtime
collections:
- ai-security
- identity-security
topics:
- AI Agent Security
- Identity Security
tags:
- OpenAI
- Codex
- Coding Agent
- Sandbox
- Network Egress
- Credentials
- Telemetry
audience:
- CISO
- AI Platform
- Developer Security
- DevSecOps
management_impact: High
impact_types:
- AI Governance
- Identity
- Developer Security
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# Coding Agentをどう守るか ― OpenAIのCodex運用から見るAgent Runtime Security

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">May 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Agent Runtime</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Agent Security / Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">CISO / AI Platform / Developer Security / DevSecOps</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Identity / Developer Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

OpenAIは2026年5月8日、社内でCoding AgentであるCodexを実運用する際のSecurity Controlを公開しました。SandboxとApproval、Network Access制御、Identity / Credential、Rule、Admin Configuration、Agent-native Telemetry / Auditを組み合わせ、低Risk Actionは迅速に、高Risk Actionは明示的な境界の中で扱う設計です。[^source]

重要なのは、Coding Agentを「高機能IDE」としてではなく、**Code・Shell・Network・Credentialへ到達可能なPrivileged Workload**として扱っていることです。

</div>

## なぜ今なのか

Coding AgentはRepositoryを読み、Commandを実行し、Fileを変更し、外部Serviceと連携できます。Developer本人の権限をそのまま引き継がせると、Prompt Injectionや誤操作のBlast Radiusが大きくなります。

Agent SafetyはModel GuardrailだけでなくRuntime Architectureで決まります。

## 統制の考え方

- SandboxでHost / File / Processを隔離する
- Riskの高いActionはHuman Approvalを要求する
- Network Accessを必要最小限に制限する
- CredentialをAgentへ常時露出させない
- Organization PolicyをAgent Runtimeへ適用する
- Agent固有のAction Logを保持する

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Developer Productivity | Agent活用を止めずにRiskを限定できる |
| Credential Risk | Developer Token / Cloud Credential流出を防ぐ設計が必要 |
| Audit | 「誰が何をしたか」だけでなく「Agentが何をしたか」を残す |
| Platform Strategy | Coding AgentをManaged Runtimeとして統制する必要 |

## 日本企業への示唆

個人PCで自由にCoding Agentを実行する運用と、企業標準のAgent Runtimeを用意する運用ではRiskが大きく異なります。Coding Agentの全社利用を進めるなら、Sandbox / Network / Credential / Loggingを共通基盤として提供する方が管理しやすくなります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Coding AgentをDeveloper Endpoint Policyの対象にする
2. Default-deny Network EgressとAllowlistを検討する
3. Cloud / Git / Package Credentialを短命化する
4. Production操作やSecret AccessをApproval対象にする
5. Agent Action LogをSIEMへ集約する
6. Sandbox EscapeやPrompt InjectionをRed Team対象にする

</div>

## 用語解説

**Agent-native Telemetry**  
AI AgentがどのToolを呼び、どのCommandを実行し、どのResourceへAccessしたかをAgent単位で記録するTelemetry。

## 関連記事

- [Agentic AIの安全設計](agentic-ai-security-controls.md)
- [AI Agent Identity / NHI](../identity-security/ai-agent-identity-nhi.md)

## 参考情報

- [OpenAI, Running Codex safely at OpenAI](https://openai.com/index/running-codex-safely/)

[^source]: [OpenAI, Running Codex safely at OpenAI](https://openai.com/index/running-codex-safely/)

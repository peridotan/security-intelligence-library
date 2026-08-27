---
title: NIST CAISI AI Agent Security RFI ― Agent Securityを「Model＋Software System」の問題として定義
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-01
description: NIST CAISIが2026年1月12日に公開したAI Agent Security RFIを基に、Indirect Prompt Injection、Data
  Poisoning、Agent Access、Monitoring、Security Measurementの論点を整理する。
category: AI Security / Agent Security
collections:
- ai-security
- risk-management
topics:
- AI Agent Security
- AI Governance
- Security Governance & Risk Management
tags:
- NIST
- CAISI
- AI Agent
- Agent Security
- Indirect Prompt Injection
- Data Poisoning
- Runtime Monitoring
- Security Measurement
audience:
- Executive
- CISO
- AI Governance
- AI Platform
management_impact: High
impact_types:
- AI Governance
- Operational Security
- Architecture
urgency: Strategic
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# NIST CAISI AI Agent Security RFI ― Agent Securityを「Model＋Software System」の問題として定義

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">January 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Agent Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Agent Security / AI Governance / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Governance / AI Platform</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Operational Security / Architecture</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NISTのCenter for AI Standards and Innovation（CAISI）は2026年1月12日、AI Agent Systemの安全な開発・導入に関するRequest for Information（RFI）を公開しました。[^source]

RFIが重要なのは、Agent SecurityをModel単体の問題として扱っていない点です。AI ModelのOutputがSoftware SystemのTool、Data、Credential、APIと結び付くことで、Indirect Prompt Injection、Poisoned Model、Specification Gaming、過剰なAgent Accessといった**Agent固有のSystem Risk**が生まれると整理しています。

この時点でNISTは、Agent Securityを独立したCybersecurity論点として扱い、Development、Deployment、Measurement、Access Constraint、Monitoringまでを今後のGuidance対象として明示しました。

</div>

## なぜ今なのか

AI Agentは回答を生成するだけでなく、外部SystemへActionできます。そのため「Modelが安全か」だけでなく、Model Outputがどの権限でどのToolを動かすかがRiskを決めます。

## RFIが提示した主要論点

- Agent固有のSecurity Threat
- Indirect Prompt Injection
- Poisoned / Insecure Model
- Misaligned Action / Specification Gaming
- Development段階でのSecurity Assessment
- Deployment EnvironmentでのAccess Constraint
- Runtime Monitoring
- Agent SecurityのMeasurement
- 従来Cybersecurity Practiceの適用可能性とGap

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Architecture | AI Agentを通常Appと同じTrust Modelで扱えない |
| IAM | Agent Access Scopeを独立して制御する必要 |
| Governance | Model Reviewだけでは導入審査が不十分 |
| Assurance | Agent Securityを測るMetric / Testが必要 |

## 日本企業への示唆

Agent導入申請では、Model名や利用目的だけでなく、Agentが接続するData、Tool、Credential、Action、Network、Approval Pointを必須項目にした方が安全です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Agent InventoryとOwnerを作成する
2. AgentごとにTool / Data / Action Scopeを記録する
3. High-impact ActionへHuman Approvalを設定する
4. External ContentをUntrusted Inputとして扱う
5. Agent AccessをLeast Privilegeで制約する
6. Runtime LoggingとSecurity Testを導入条件にする

</div>

## 用語解説

**AI Agent System**  
AI Modelの推論をSoftware、Tool、Data Source、Credential、Workflow等と組み合わせ、計画・判断・Actionを実行するSystem。

## 関連記事

- [NIST AI Agent Security分析](nist-ai-agent-security-rfi-analysis.md)
- [AI Agent Identity / NHI](../identity-security/ai-agent-identity-nhi.md)

## 参考情報

- [NIST, CAISI Issues Request for Information About Securing AI Agent Systems](https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems)

[^source]: [NIST CAISI, AI Agent Security RFI](https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems)

---
title: Trusted Access for Cyber ― 高いCyber Capabilityを「IdentityとTrust」で段階開放する
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-02
description: OpenAIが2026年2月5日に発表したTrusted Access for Cyberを基に、Frontier Cyber CapabilityのAccess
  Control、Identity Verification、Enterprise Trust、Monitoringの意味を整理する。
category: AI Security / Capability Access
collections:
- ai-security
- identity-security
- risk-management
topics:
- AI Cyber Capability
- Identity Security
- AI Governance
tags:
- OpenAI
- Trusted Access for Cyber
- GPT-5.3-Codex
- Identity Verification
- Capability-aware Access
- Cyber Safeguards
audience:
- Executive
- CISO
- AI Governance
- Security Research
management_impact: High
impact_types:
- AI Governance
- Identity
- Access Control
urgency: Strategic
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# Trusted Access for Cyber ― 高いCyber Capabilityを「IdentityとTrust」で段階開放する

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">February 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Capability Access</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Cyber Capability / Identity Security / AI Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Governance / Security Research</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Identity / Access Control</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

OpenAIは2026年2月5日、Cybersecurity用途で高いCapabilityを持つModelへのAccessについて、Identity / Trustに基づいて段階的に許可する**Trusted Access for Cyber**を発表しました。[^source]

背景には、同じ「脆弱性を探す」という依頼でも、防御・Responsible Disclosureにも攻撃準備にも使えるというDual-use問題があります。単純なPrompt内容だけでIntentを判定するのではなく、利用者のIdentity、Enterprise Relationship、Monitoring、Usage Policyを組み合わせてRiskを下げる考え方です。

</div>

## なぜ今なのか

Frontier ModelのCyber Capabilityが高くなるほど、「全員に同じCapabilityを同じ条件で提供する」ことが難しくなります。一方、強すぎる制限はSecurity Researchや防御側のAutomationを阻害します。

## Access Modelの考え方

<div class="sil-flow" role="group" aria-label="Capability-aware access flow">
  <div class="sil-flow-step"><strong>Baseline Safeguards</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Identity / Enterprise Verification</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Trusted Access</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Monitoring / Usage Policy / Enforcement</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step sil-flow-step-action"><strong>Higher-risk Defensive Cyber Work</strong></div>
</div>

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| AI Governance | Model AccessをRole / Trust Levelで変える設計が必要 |
| Identity | AI CapabilityとIdentity Assuranceが直接つながる |
| Security Research | Legitimate WorkのFalse Positive拒否を減らす仕組みが必要 |
| Audit | 誰がどのCapabilityを使ったかのTraceabilityが重要 |

## 日本企業への示唆

社内AI AgentやSecurity Copilotでも、全Employeeに同じTool Permissionを与えるのではなく、Role・Identity Assurance・Target System・Business Needに応じてCapabilityを段階化する考え方が有効です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AI CapabilityをRisk Levelで分類する
2. 高Risk CapabilityへPhishing-resistant Authenticationを要求する
3. Human / Agent / Service Identityを区別する
4. Capability利用LogをAudit可能にする
5. Policy違反時のRevoke / Suspension Processを定義する
6. Legitimate Security Research向けException Processを整備する

</div>

## 用語解説

**Capability-aware Access**  
利用者のIdentity、Role、Trust、Use Caseに応じて、AIやToolが実行できる能力・権限の範囲を変える考え方。

## 関連記事

- [Advanced Account Security](../identity-security/openai-advanced-account-security.md)
- [Trusted Access for Cyber](openai-trusted-access-cyber.md)

## 参考情報

- [OpenAI, Introducing Trusted Access for Cyber](https://openai.com/index/trusted-access-for-cyber/)

[^source]: [OpenAI, Trusted Access for Cyber](https://openai.com/index/trusted-access-for-cyber/)

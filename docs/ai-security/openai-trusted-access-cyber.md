---
title: Cyber能力へのAccess Control ― OpenAI Trusted Accessが示す「能力 × Identity」の統制
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-05
description: OpenAIが2026年5月7日に拡張したTrusted Access for Cyberを基に、高度なCyber CapabilityへのAccessをIdentity、Organization
  Verification、利用目的、監視で制御する考え方を整理する。
category: AI Security / Cyber Capability Governance
collections:
- ai-security
- identity-security
- risk-management
topics:
- AI Cyber Capability
- Identity Security
- Security Governance & Risk Management
tags:
- OpenAI
- GPT-5.5-Cyber
- Trusted Access
- Phishing-resistant MFA
- Identity Verification
- Cyber Capability
audience:
- Executive
- CISO
- Security Research
- AI Governance
management_impact: High
impact_types:
- AI Governance
- Identity
- Abuse Prevention
urgency: Strategic
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# Cyber能力へのAccess Control ― OpenAI Trusted Accessが示す「能力 × Identity」の統制

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">May 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Cyber Capability Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Cyber Capability / Identity Security / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Security Research / AI Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Identity / Abuse Prevention</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

OpenAIは2026年5月7日、GPT-5.5およびGPT-5.5-Cyberに合わせてTrusted Access for Cyberを拡張しました。高度なCyber Taskを行う検証済みDefenderに対してSafeguard上の摩擦を下げる一方、Identity / Organization Verification、Authorized Use、Misuse Monitoringを組み合わせてAccessを制御する仕組みです。[^source]

さらに高度なCyber ModelへのAccessでは、2026年6月1日からPhishing-resistantなAdvanced Account Securityを求める方針も示しました。これは、**Model Capabilityが上がるほどAccount Assuranceも上げる「Capability-aware Identity Security」**の一例です。

</div>

## なぜ今なのか

AI ModelのCyber Capabilityが高くなると、同じModel Accessでも利用者のIdentity、所属、目的、対象SystemのAuthorizationによってRiskが変わります。

一律に機能を拒否するか一律に開放するのではなく、Trust Levelに応じて能力Accessを段階化する考え方が重要になります。

## 統制モデル

Trusted Accessの考え方は企業内の高Risk AI Toolにも応用できます。

- User / Organization Verification
- Phishing-resistant Authentication
- Approved Use Case / Scope
- Capability Tier
- Misuse Monitoring
- Periodic Review / Revocation

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| AI Governance | CapabilityごとにAccess Requirementを変える必要 |
| Identity Security | 強いAI Capabilityは強いIdentity Assuranceを要求 |
| Insider Risk | 利用目的・対象System・Authorizationの証跡が重要 |
| Security Research | 防御担当者に必要な能力を適切に提供しやすくなる |

## 日本企業への示唆

社内AI AgentやSecurity Copilotにも、全社員一律ではなく「能力Tier」を設ける考え方が使えます。Code Execution、Exploit Validation、Credential Access等は、より強いIdentity Assuranceと承認を要求する設計が適しています。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AI CapabilityをLow / Elevated / Privileged等にTieringする
2. 高Risk CapabilityにPasskey等のPhishing-resistant MFAを要求する
3. 利用対象SystemとAuthorizationを記録する
4. Capability利用Logを監視する
5. Role変更・退職・Project終了時にAccessをRevocationする
6. Cyber Research用AIと一般業務AIのAccess Policyを分離する

</div>

## 用語解説

**Capability-aware Access Control**  
利用者属性だけでなく、AIが提供する能力のRisk Levelに応じて認証・承認・監視要件を変える考え方。

## 関連記事

- [Frontier AIのサイバー能力が「Critical」に近づく意味](frontier-ai-cyber-capabilities.md)
- [Passkeyは破られたのか](../identity-security/pass-the-passkey.md)

## 参考情報

- [OpenAI, Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/)

[^source]: [OpenAI, Trusted Access for Cyber](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/)

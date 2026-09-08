---
title: Enterprise Frontier Safeguards ― PrivacyとMisuse Detectionを「分離」して両立する
date: 2026-09-08
updated: 2026-09-08
reviewed: 2026-09-08
review_status: Current
source_period: 2026-09
description: Anthropicが2026年9月1日に発表したEnterprise Frontier Safeguardsを基に、Zero Data RetentionとMisuse
  DetectionをCustomer-controlled Cloudで両立するSplit-custody Architectureを整理する。
category: AI Security / Governance
collections:
- ai-security
- risk-management
topics:
- AI Governance
- AI Agent Security
- Security Governance & Risk Management
tags:
- Anthropic
- Enterprise Frontier Safeguards
- Zero Data Retention
- Misuse Detection
- Customer-controlled Cloud
- Privacy
- Regulated AI
- Split Custody
audience:
- Executive
- CISO
- AI Governance
- Privacy
management_impact: High
impact_types:
- AI Governance
- Privacy
- Monitoring
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# Enterprise Frontier Safeguards ― PrivacyとMisuse Detectionを「分離」して両立する

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-09-08</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">September 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-09-08</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-09-08</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Governance / AI Agent Security / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Governance / Privacy</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Privacy / Monitoring</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Anthropicは2026年9月1日、**Enterprise Frontier Safeguards（EFS）**を発表しました。EFSはZero Data Retention（ZDR）のPrivacy要件と、Frontier ModelのMisuse Detectionを両立させるため、Customer-controlled Cloud InfrastructureへData / Logを保持するArchitectureを採用するとしています。[^source]

100社超のCustomerおよびAWS、Google Cloud、Microsoftとの協力で開発され、Claude Code、Claude Enterprise、Claude Platform、主要Cloud Platform等への対応が予定されています。Rolloutは**2026年秋以降に段階的に開始予定**であり、現時点では全Customerへ展開済みの機能ではありません。

重要なのは、PrivacyとSecurity Monitoringを「どちらか一方」とせず、**Data CustodyとDetection Functionを分離するArchitecture Pattern**として考えられる点です。

</div>

## なぜ今なのか

規制産業や機密性の高い企業では、Frontier AIの利用にMisuse DetectionやSecurity Monitoringが必要でも、Provider側へPrompt / Output / Logを長期保持させたくない場合があります。このTrade-offがAI導入の阻害要因になります。

## Architectureの考え方

<div class="sil-flow" role="group" aria-label="Enterprise frontier safeguards split custody">
  <div class="sil-flow-step"><strong>Enterprise AI Workload</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-branches">
    <div class="sil-flow-step"><strong>Customer-controlled Data / Logs</strong><span>Privacy / Residency / Key Control</span></div>
    <div class="sil-flow-step"><strong>Misuse Detection Safeguards</strong><span>Security Signal / Enforcement</span></div>
  </div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step sil-flow-step-action"><strong>Frontier Capability with Enterprise Controls</strong></div>
</div>

## 経営インパクト

| 観点 | 経営上の意味 |
| --- | --- |
| Privacy | Provider Retentionを減らしながらControlを維持する選択肢 |
| AI Governance | MonitoringをPolicyだけでなくArchitectureへ組み込む |
| Cloud Strategy | Data / LogのCustodyとAI Provider責任を分離して設計 |
| Vendor Risk | 「保存しない」だけでなく「どう検知するか」を確認する必要 |

## 日本企業への示唆

金融、医療、製造、公共等では、AI利用可否を「外部送信だから禁止」で止めるのではなく、Data Residency、ZDR、Customer-managed Infrastructure、Monitoring、Incident Accessの役割分担を要件化する方が実務的です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AI ProviderのRetention / Detection / Incident Accessを分けて確認する
2. Customer-controlled Logの保存場所とAccess Ownerを定義する
3. ZDRがSecurity Monitoringへ与える影響を評価する
4. Provider DetectionのSignal / Enforcement範囲を契約前に確認する
5. Data Residency / Key Management RequirementとAI Safeguardを一体化する
6. EFSはRollout予定段階のため、利用可否と実装条件を継続確認する

</div>

## 用語解説

**Zero Data Retention (ZDR)**  
Provider側でPromptやOutput等のCustomer Dataを利用後に保持しない、または極小化するData Handling方式。

**Split Custody**  
Data / Key / Log等の保有主体と、Detection / Controlを提供する主体を分けるArchitectureの考え方。

## 関連記事

- [生成AI利活用ガバナンス](generative-ai-governance.md)
- [NISTが示すContinuous AI Security](continuous-ai-security-nist-proof.md)

## 参考情報

- [Anthropic, Developing Enterprise Frontier Safeguards with our customers (2026-09-01)](https://www.anthropic.com/news/enterprise-frontier-safeguards)

[^source]: [Anthropic, Enterprise Frontier Safeguards (2026-09-01)](https://www.anthropic.com/news/enterprise-frontier-safeguards)

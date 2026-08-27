---
title: Domain Spoofing via Complex Routing ― 「社内ドメインだから安全」というTrustをMail設計が崩す
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-01
description: Microsoft Threat Intelligenceが2026年1月6日に公開したComplex RoutingとSpoof Protection
  Misconfigurationの悪用を基に、DMARC、SPF、Third-party Connector、Internal-looking Phishingを整理する。
category: Identity Security / Email Trust
collections:
- identity-security
- cybersecurity
topics:
- Credential Attacks
- Identity Security
tags:
- Microsoft
- Email Security
- Domain Spoofing
- Complex Routing
- DMARC
- SPF
- Third-party Connector
- Tycoon2FA
audience:
- Executive
- CISO
- Messaging
- SOC
management_impact: High
impact_types:
- Identity
- Email Security
- Financial Fraud
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# Domain Spoofing via Complex Routing ― 「社内ドメインだから安全」というTrustをMail設計が崩す

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">January 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / Email Trust</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Credential Attacks / Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Messaging / SOC</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / Email Security / Financial Fraud</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoft Threat Intelligenceは2026年1月6日、Complex Mail Routingと不十分なSpoof Protectionを悪用し、**自社Domainから内部送信されたように見えるPhishing Message**をDeliveryするCampaignを報告しました。[^source]

Microsoftは、このVectorをDirect Send自体のVulnerabilityではなく、MXがOffice 365を直接指していないComplex Routingや、SPF / DMARC / Third-party Connectorの設定不備を悪用するものと説明しています。

Tycoon2FA等のPhaaSへ誘導するCredential Phishingにも利用されており、問題の本質は「内部に見えるEmailを信頼する」というTrust Assumptionです。

</div>

## なぜ今なのか

Hybrid Mail、Security Gateway、Third-party Relay、Marketing Platform等を組み合わせるほどMail Flowは複雑になり、Authentication ResultをどこでEnforceするかが曖昧になります。

## Riskの構造

<div class="sil-flow" role="group" aria-label="Complex mail routing spoof flow">
  <div class="sil-flow-step"><strong>External Threat Actor</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Complex / Third-party Mail Routing</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Weak SPF / DMARC / Connector Enforcement</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step sil-flow-step-impact"><strong>Message appears internally sent</strong></div>
</div>

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Email Security | Security Productの有無よりRouting Designが重要 |
| Identity | Internal-looking PhishがCredential Theftへつながる |
| BEC | Financial Scamへ悪用される可能性 |
| Architecture | Third-party ConnectorもTrust Boundaryとして管理が必要 |

## 日本企業への示唆

長年継ぎ足したMail Routingは「動いているから安全」とは限りません。M&AやCloud移行後のConnectorを含め、Authentication / Spoof Enforcement Pointを再確認する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. MX / Relay / Connector構成を棚卸しする
2. DMARCを可能な範囲でrejectへ移行する
3. SPF Soft Fail依存を見直す
4. Third-party ConnectorのTrust条件を確認する
5. Internal-looking MessageにもPhishing Detectionを適用する
6. Mail Flow変更をSecurity Review対象にする

</div>

## 用語解説

**Complex Routing**  
Cloud Mail、On-premises Server、Security Gateway、Third-party Service等を複数経由するMail Delivery構成。

## 関連記事

- [Tycoon2FA](tycoon2fa-aitm-phaas.md)
- [ShinyHunters型SaaS Data Theft](shinyhunters-saas-data-theft.md)

## 参考情報

- [Microsoft Security Blog, Phishing actors exploit complex routing and misconfigurations to spoof domains](https://www.microsoft.com/en-us/security/blog/2026/01/06/phishing-actors-exploit-complex-routing-and-misconfigurations-to-spoof-domains/)

[^source]: [Microsoft Threat Intelligence, complex routing and domain spoofing](https://www.microsoft.com/en-us/security/blog/2026/01/06/phishing-actors-exploit-complex-routing-and-misconfigurations-to-spoof-domains/)

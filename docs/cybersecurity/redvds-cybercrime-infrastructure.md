---
title: RedVDS ― CybercrimeのScaleを支える「安価なInfrastructure-as-a-Service」
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-01
description: Microsoft Threat Intelligenceが2026年1月14日に公開したRedVDS調査を基に、VDS InfrastructureがBEC、Mass
  Phishing、Account Takeover、Financial Fraudを支える構造を整理する。
category: Cybersecurity / Cybercrime Infrastructure
collections:
- cybersecurity
- risk-management
topics:
- Credential Attacks
- Security Governance & Risk Management
tags:
- Microsoft
- RedVDS
- VDS
- Cybercrime Infrastructure
- BEC
- Mass Phishing
- Account Takeover
- Financial Fraud
audience:
- Executive
- CISO
- SOC
- Threat Intelligence
management_impact: High
impact_types:
- Threat Landscape
- Financial Fraud
- Identity
urgency: Near-term
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# RedVDS ― CybercrimeのScaleを支える「安価なInfrastructure-as-a-Service」

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">January 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / Cybercrime Infrastructure</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Credential Attacks / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / SOC / Threat Intelligence</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Threat Landscape / Financial Fraud / Identity</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoft Threat Intelligenceは2026年1月14日、複数のFinancially Motivated Actorが利用していたVirtual Dedicated Server Provider **RedVDS**の調査結果を公開しました。[^source]

Microsoftは、RedVDS InfrastructureがBusiness Email Compromise、Mass Phishing、Account Takeover、Financial Fraud等に利用され、Legal、Construction、Manufacturing、Real Estate、Healthcare、Education等の複数Sectorが標的になったと報告しています。

重要なのは特定Malwareより、**安価でDisposableなHosting / Virtual Desktop Infrastructureが犯罪Campaignの再利用可能な共通基盤になっている**ことです。

</div>

## なぜ今なのか

Phishing Kitだけでなく、Hosting、Proxy、Domain、Credential、VDSまでCrime-as-a-Service化すると、攻撃者はInfrastructure構築に時間を使わずCampaignをScaleできます。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Threat Intel | IP単体Blockは短命になりやすい |
| BEC | Infrastructure再利用でCampaignを大量展開可能 |
| Fraud | Identity CompromiseからFinancial Fraudへ直結 |
| Defense | Behavior / Identity / Transaction Signalが重要 |

## 日本企業への示唆

「このIPをBlockしたから終わり」ではなく、同じActor Infrastructureが変化・再生成される前提で、Login Behavior、Mailbox Change、Payment Changeを継続監視する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Threat IntelをIPだけでなくInfrastructure Patternで見る
2. Impossible Travel / New SessionをIdentity側で検知する
3. Mailbox Rule変更を監視する
4. Payment ChangeへOut-of-band Verificationを入れる
5. BEC IncidentをFinanceと共同Exerciseする
6. IOC Expiry / Reuseを考慮してDetectionを更新する

</div>

## 用語解説

**Cybercrime Infrastructure-as-a-Service**  
攻撃に必要なServer、Remote Desktop、Proxy、Domain等を第三者Serviceとして調達し、犯罪Operationを高速・大規模化する構造。

## 関連記事

- [ShinyHunters型SaaS Data Theft](../identity-security/shinyhunters-saas-data-theft.md)
- [AI as Tradecraft](ai-as-tradecraft-march-2026.md)

## 参考情報

- [Microsoft Security Blog, Inside RedVDS: How a single virtual desktop provider fueled worldwide cybercriminal operations](https://www.microsoft.com/en-us/security/blog/2026/01/14/inside-redvds-how-a-single-virtual-desktop-provider-fueled-worldwide-cybercriminal-operations/)

[^source]: [Microsoft Threat Intelligence, RedVDS](https://www.microsoft.com/en-us/security/blog/2026/01/14/inside-redvds-how-a-single-virtual-desktop-provider-fueled-worldwide-cybercriminal-operations/)

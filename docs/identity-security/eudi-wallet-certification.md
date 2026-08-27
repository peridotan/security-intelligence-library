---
title: EUDI Wallet Certification ― Digital Identityを「実装」から「認証・保証」へ
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-04
description: ENISAが2026年4月3日に公開Consultationを開始したEU Digital Identity Wallet向けCybersecurity
  Certification Schemeを基に、Digital IdentityのSecurity AssuranceとCertificationを整理する。
category: Identity Security / Digital Identity
collections:
- identity-security
- regulation
topics:
- Identity Security
- Regulation & Policy
tags:
- ENISA
- EUDI Wallet
- Digital Identity
- Cybersecurity Certification
- eIDAS
- Wallet
audience:
- Executive
- IAM
- Digital Identity
- Compliance
management_impact: High
impact_types:
- Identity
- Regulatory
- Trust
urgency: Strategic
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# EUDI Wallet Certification ― Digital Identityを「実装」から「認証・保証」へ

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">April 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / Digital Identity</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Identity Security / Regulation &amp; Policy</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / IAM / Digital Identity / Compliance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / Regulatory / Trust</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

ENISAは2026年4月3日、European Digital Identity（EUDI）Wallet向けCandidate Cybersecurity Certification SchemeのPublic Consultationを開始しました。EU Digital Identity Frameworkに基づき、Member Stateが提供するWalletのSecurity Requirementを共通のCertification Frameworkで評価する方向です。[^source]

Member Stateは2026年末までに少なくとも1つのCertified EUDI Walletを提供することが求められており、Digital IdentityのTrustが「規格に準拠した実装」だけでなく、**第三者によるSecurity AssuranceとCertification**へ広がっていることを示します。

</div>

## なぜ今なのか

Digital WalletはIdentity Credential、Attribute、Personal Dataを保持し、Physical / Digital Service双方のAuthenticationに使われます。

Wallet自体が侵害されれば影響は広範囲になるため、Authentication Protocolだけでなく、Device、Secure Storage、Lifecycle、Implementation Qualityを含むCertificationが必要になります。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Digital Identity | Wallet SecurityがAuthentication Trustの一部になる |
| Vendor Selection | Wallet / Identity ProviderのCertification Statusが選定条件になり得る |
| Privacy | Identity DataとSecurity Assuranceを同時に扱う必要 |
| Cross-border | 国ごとのWalletを共通FrameworkでTrustする仕組みが必要 |

## 日本企業への示唆

EUDI Walletそのものを導入しない企業でも、社員証、Customer Identity Wallet、Verifiable Credential等を設計する際に参考になります。

Credential Formatだけではなく、Wallet Application、Device、Key Storage、Recovery、Update、CertificationまでEnd-to-Endで評価する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Digital Wallet導入時にSecurity Certification要件を確認する
2. Credential KeyのStorage / Backup / Recovery設計を確認する
3. Wallet UpdateとVulnerability Response責任をVendor契約へ入れる
4. Device Compromise時のCredential Revocationを設計する
5. WalletとIdentity ProviderのTrust Boundaryを明確化する
6. Regulatory CertificationをVendor Due Diligenceへ組み込む

</div>

## 用語解説

**EUDI Wallet**  
EU Digital Identity Frameworkに基づくDigital Identity Wallet。Public / Private ServiceでIdentityやAttributeを提示するために利用される。

## 関連記事

- [NIST PIVのPQC対応](pqc-piv-dual-stack.md)
- [Entra IDがPasskeyを既定へ](entra-passkeys-default.md)

## 参考情報

- [ENISA, ENISA advances the certification of EU Digital Wallets](https://www.enisa.europa.eu/news/enisa-advances-the-certification-of-eu-digital-wallets)

[^source]: [ENISA, EUDI Wallet certification consultation](https://www.enisa.europa.eu/news/enisa-advances-the-certification-of-eu-digital-wallets)

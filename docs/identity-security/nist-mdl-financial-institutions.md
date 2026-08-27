---
title: NIST SP 1800-42 Draft ― Digital Identityを金融の実取引へ持ち込むReference Architecture
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-03
description: NIST NCCoEが2026年3月18日に公開した金融機関向けmDL実装Draftを基に、Verifiable Digital Credential、Threat
  Model、Privacy、Interoperabilityの意味を整理する。
category: Identity Security / Digital Identity
collections:
- identity-security
- risk-management
topics:
- Identity Security
- Security Governance & Risk Management
tags:
- NIST
- SP 1800-42
- mDL
- Mobile Driver License
- Verifiable Credential
- Financial Services
- Digital Identity
audience:
- Executive
- IAM
- Financial Services
- Digital Identity
management_impact: High
impact_types:
- Identity
- Fraud
- Privacy
urgency: Strategic
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# NIST SP 1800-42 Draft ― Digital Identityを金融の実取引へ持ち込むReference Architecture

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">March 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / Digital Identity</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Identity Security / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / IAM / Financial Services / Digital Identity</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / Fraud / Privacy</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NIST NCCoEは2026年3月18日、Financial InstitutionがMobile Driver’s License（mDL）をCustomer Identity Verificationへ利用するためのSP 1800-42 Initial Public Draftを公開しました。[^source]

これはDigital Credentialの概念説明ではなく、Reference Architecture、Threat Model、Usability、Financial Regulatory RequirementとのMappingを含む実装Guideです。**Digital Identity Wallet / Verifiable Credentialが実証段階から業務Architectureへ移る流れ**を示します。

</div>

## なぜ今なのか

Physical IDの画像UploadやKnowledge-based VerificationはFraudやPrivacyの課題を抱えます。mDLのようなDigital Credentialは、必要なAttributeをStandards-basedに提示する新しいIdentity Proofing手段になり得ます。

## Draftが扱う論点

- Online Financial Account Management
- Standards-based Reference Architecture
- Threat Modeling
- Security / Privacy
- Usability
- Interoperability
- Financial Regulatory Requirement Mapping

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Fraud | ID画像だけに頼らないVerificationへ移行可能 |
| Privacy | 必要Attributeだけを提示する設計が重要 |
| Architecture | Wallet / Issuer / Verifier間のTrust設計が必要 |
| Vendor | InteroperabilityとLifecycle Supportが選定条件になる |

## 日本企業への示唆

mDLそのものを使わない場合でも、社員Credential、Customer Identity、本人確認Walletを設計する際のReferenceになります。Wallet導入ではCredential FormatだけでなくIssuer Trust、Revocation、Device / Recoveryを確認すべきです。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Digital Identityの対象Use Caseを整理する
2. Issuer / Wallet / VerifierのTrust Boundaryを定義する
3. Privacy / Selective Disclosure要件を確認する
4. Device Loss / Revocation / Recoveryを設計する
5. Existing KYC / Identity ProofingとのCoexistenceを計画する
6. VendorのInteroperability / Standards対応を確認する

</div>

## 用語解説

**mDL (Mobile Driver’s License)**  
ISO等の標準に基づいてMobile Device上で運転免許情報を安全に提示するDigital Credential。

## 関連記事

- [EUDI Wallet Certification](eudi-wallet-certification.md)
- [NIST PIVのPQC対応](pqc-piv-dual-stack.md)

## 参考情報

- [NIST SP 1800-42, Digital Identities – Mobile Driver’s License](https://csrc.nist.gov/pubs/sp/1800/42/ipd)

[^source]: [NIST SP 1800-42 Initial Public Draft](https://csrc.nist.gov/pubs/sp/1800/42/ipd)

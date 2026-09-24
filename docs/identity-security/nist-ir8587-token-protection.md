---
title: Token Security Becomes Identity Control Plane ― NIST IR 8587 Final
date: 2026-09-24
updated: 2026-09-24
reviewed: 2026-09-24
review_status: Current
source_period: 2026-09
description: NISTとCISAが2026年9月15日にFinal版を公開したNIST IR 8587を基に、Identity / Access TokenとAssertionのSigning
  Key、Verification、Lifecycle、Workload Identity保護を整理する。
category: Identity Security / Token Protection
collections:
- identity-security
- risk-management
topics:
- Identity Security
- Security Governance & Risk Management
tags:
- NIST
- CISA
- NIST IR 8587
- Token Security
- SSO
- Federation
- Signing Key
- Workload Identity
- Token Revocation
audience:
- Executive
- CISO
- IAM
- Cloud
management_impact: High
impact_types:
- Identity
- Cloud
- Cryptographic Key Management
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# Token Security Becomes Identity Control Plane ― NIST IR 8587 Final

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-09-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">September 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-09-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-09-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / Token Protection</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Identity Security / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / IAM / Cloud</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / Cloud / Cryptographic Key Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NISTはCISAと連携し、2026年9月15日に**NIST IR 8587, Protecting Tokens and Assertions from Forgery, Theft, and Misuse**のFinal版を公開しました。Federal AgencyとCloud Service Provider向けのImplementation Guidanceですが、NISTはCommercial Organizationを含めTokenをAccess Managementに利用する組織にも参考になると説明しています。[^source]

IR 8587は、Identity Token、Access Token、Assertionを単なる認証後の一時データではなく、**SSO、Federation、API、Workload Accessを支えるSecurity Control Plane**として扱います。Signing Key Protection、Token Verification、Lifecycle Control、Continuous Monitoringを組み合わせる考え方です。

Final版では、Signing KeyのStorageとUsageを分けたProtection、System Classification / Transaction Sensitivityを踏まえたKey Validity、Workload IdentityでのShort-lived Token、Token RevocationやSignal Sharingに関するStandards Referenceが強化されました。

</div>

## なぜ今なのか

PasswordやMFAを強化しても、発行済みTokenが盗まれたり、Signing Keyが不正利用されたり、Verificationが不十分であれば、ApplicationやAPIへのAccessが成立する可能性があります。

Cloud / SaaS / API / Workload Identityが増えるほど、Identity Securityの中心は「Credentialを守る」だけでなく、**Tokenを安全に発行し、検証し、短命化し、異常時に止める**ところまで広がります。

## Token Protectionの主要Control

| Control | 役割 |
| --- | --- |
| Signing Key Protection | Token / Assertionを正当に発行したと信頼するRootを守る |
| Secure Key Usage | KeyをExportせず、許可されたOperationだけに使う |
| Token Verification | Issuer、Audience、Signature、Validity等を正しく検証する |
| Lifecycle Control | Expiration、Rotation、Revocation、Session Invalidatonを管理する |
| Workload Identity | Static Secret依存を減らしShort-lived Tokenを利用する |
| Monitoring / Signal Sharing | Token RiskやRevocation SignalをService間で共有する |

## 経営インパクト

| 観点 | 経営上の意味 |
| --- | --- |
| SSO / Federation | IdPだけでなくToken Consumer側のVerification品質が重要 |
| Key Management | Signing Key侵害は多数Serviceへ同時Impactを与え得る |
| Cloud / API | Token TheftがCredential Reset後もAccess継続につながる場合がある |
| Workload | Long-lived SecretからShort-lived Identityへの移行が必要 |
| Incident Response | Token / Session失効をContainment Playbookへ組み込む |
| Vendor | CSP / SaaSが提供するKey Protection・Revocation機能の確認が必要 |

## 日本企業への示唆

NIST IR 8587は米国政府向け要素を持ちますが、日本企業でもSSO、Federation、API、Cloud、Workload Identityを利用する限り、設計観点はそのまま有用です。

特にIAMのSecurity Reviewを「MFA方式」「Password Policy」で終わらせず、**Signing Key、Token Lifetime、Audience Restriction、Revocation、Workload Credential**まで広げると、Identity Control Plane全体を評価しやすくなります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. **Token Inventoryを作る** — ID Token、Access Token、Assertion、Workload TokenのIssuer / Consumer / Lifetimeを把握する。
2. **Signing Key Protectionを確認する** — Storage、Usage、Rotation、Access Controlを分けて評価する。
3. **Token VerificationをReviewする** — Issuer / Audience / Signature / Expiration等のValidationを確認する。
4. **Short-lived Tokenを優先する** — WorkloadでStatic Secretや長寿命Tokenへの依存を減らす。
5. **Revocation / Session InvalidatonをTestする** — Identity Incident時にどこまで即時停止できるか演習する。
6. **Provider / Consumer責任分界を明確にする** — IdP、CSP、SaaS、Custom App間のControl Ownerを定める。

</div>

## 用語解説

**Assertion**  
Identity Provider等が、UserやEntityの認証状態・属性等について発行するSecurity Statement。Federationで利用されるSAML Assertionなどが代表例です。

**Signing Key**  
Token / AssertionへDigital Signatureを付与するKey。ConsumerはSignatureを検証することでIssuerとIntegrityを確認します。

## 参考情報

- [NIST CSRC, Protecting Tokens and Assertions - NIST IR 8587 (2026-09-15)](https://csrc.nist.gov/news/2026/protecting-tokens-and-assertions-nist-ir-8587)
- [NIST CSRC, NIST IR 8587 Final](https://csrc.nist.gov/pubs/ir/8587/final)
- [NIST, NIST Finalizes Guidelines on Protecting Online Identity and Access Tokens From Misuse (2026-09-15)](https://www.nist.gov/news-events/news/2026/09/nist-finalizes-guidelines-protecting-online-identity-and-access-tokens)

[^source]: [NIST CSRC, Protecting Tokens and Assertions - NIST IR 8587 (2026-09-15)](https://csrc.nist.gov/news/2026/protecting-tokens-and-assertions-nist-ir-8587)

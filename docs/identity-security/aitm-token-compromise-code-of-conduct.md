---
title: AiTM Token Compromise ― 「MFA済み」のSessionを盗まれるPhishing
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-05
description: Microsoftが2026年5月4日に公表したCode of Conductを装う多段Phishing Campaignを基に、AiTM、Token
  Theft、Phishing-resistant MFAの重要性を整理する。
category: Identity Security / Phishing
collections:
- identity-security
- cybersecurity
topics:
- Credential Attacks
- Passkey & Phishing-resistant MFA
- Identity Security
tags:
- AiTM
- Phishing
- Session Token
- MFA
- Microsoft Entra
- Credential Theft
audience:
- CISO
- IAM
- SOC
- End-user Security
management_impact: High
impact_types:
- Identity
- Financial Fraud
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# AiTM Token Compromise ― 「MFA済み」のSessionを盗まれるPhishing

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">May 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / Phishing</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Credential Attacks / Passkey &amp; Phishing-resistant MFA / Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">CISO / IAM / SOC / End-user Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / Financial Fraud</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoftは2026年5月4日、「Code of Conduct」確認を装う多段Social Engineering Campaignを報告しました。最終的に被害者を正規Sign-inに似たAdversary-in-the-Middle（AiTM）Flowへ誘導し、Authentication TrafficをProxyしてSession Tokenを窃取することでAccount Accessを得る手法です。[^source]

これはPasswordだけを盗む従来型Phishingと異なり、**非Phishing-resistant MFAを通過した後のSessionまで奪う**ため、「MFA導入済み」だけでは十分な対策になりません。

</div>

## なぜ今なのか

OTPやPush型MFAはPassword-onlyより大幅に安全ですが、AiTM Proxyでは利用者本人に正規MFAを実行させ、その結果生成されたSessionを攻撃者がReplayできます。

Identity SecurityはAuthentication Factorだけでなく、Session、Device、Risk Signal、Phishing-resistant Authenticationまで含める必要があります。

## 攻撃Chain

1. Business文脈に沿ったLureを送付
2. 複数段階のRedirectで警戒を回避
3. AiTM Proxy上でSign-inを実施させる
4. Password / MFAを正規IdPへ中継
5. Authentication TokenをCapture
6. Tokenを利用してAccountへAccess

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| MFA Strategy | 「MFA導入率」よりPhishing Resistanceが重要 |
| Session Security | Authentication後のToken監視が必要 |
| Fraud | Mailbox / SaaS侵害からBusiness Email Compromiseへ発展可能 |
| Awareness | 利用者教育だけでは完全に防ぎにくい |

## 日本企業への示唆

MFA導入KPIを「何%がMFAか」から「何%がPhishing-resistantか」へ変えることが重要です。高Risk Userや管理者からPasskey / FIDOへ移行し、Session RiskをConditional AccessやITDRで監視します。

<div class="sil-action-box" markdown>

## 推奨アクション

1. 管理者・財務・HelpdeskからPasskey / FIDOを優先導入する
2. Legacy / Phishable MFA利用者を可視化する
3. Token ReplayやImpossible Travel等のSession Riskを監視する
4. Device ComplianceをConditional Accessへ組み込む
5. Sign-in URLをメールで誘導する運用を減らす
6. Phishing Incident時はPassword変更だけでなくSession Revocationを行う

</div>

## 用語解説

**AiTM (Adversary-in-the-Middle)**  
利用者と正規Serviceの間にProxyを置き、CredentialやAuthentication TokenをReal-timeで中継・窃取するPhishing手法。

## 関連記事

- [Passkey時代の次の攻撃面](passkey-enrollment-recovery-attacks.md)
- [Entra IDがPasskeyを既定へ](entra-passkeys-default.md)

## 参考情報

- [Microsoft, Breaking the code: Multi-stage code of conduct phishing campaign leads to AiTM token compromise](https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/)

[^source]: [Microsoft, AiTM token compromise campaign](https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/)

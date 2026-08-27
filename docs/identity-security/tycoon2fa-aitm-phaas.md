---
title: Tycoon2FA ― MFA突破がPhishing-as-a-Serviceとして「産業化」した
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-03
description: Microsoftが2026年3月4日に公表したTycoon2FA分析を基に、AiTM、Session Cookie Theft、短命Infrastructure、PhaaSによるMFA突破のScale化を整理する。
category: Identity Security / AiTM Phishing
collections:
- identity-security
- cybersecurity
topics:
- Credential Attacks
- Passkey & Phishing-resistant MFA
- Identity Security
tags:
- Tycoon2FA
- Microsoft
- AiTM
- Phishing-as-a-Service
- Session Cookie
- MFA
- Storm-1747
mitre_attack:
- id: T1566.002
  basis: Analyst-mapped
  note: Microsoftが観測したLinkを用いるPhishing Deliveryに対応。Tycoon2FAの全Delivery方式をこのTechniqueだけで表すものではない。
- id: T1557
  basis: Analyst-mapped
  note: 正規Authentication Serviceとの間にAiTM Proxyを置き、認証TrafficをRelayする行動に対応。
- id: T1539
  basis: Analyst-mapped
  note: MFA完了後のSession Cookieを取得し、再認証なしでAccount Accessへ利用する行動に対応。
audience:
- Executive
- CISO
- IAM
- SOC
management_impact: High
impact_types:
- Identity
- Financial Fraud
- SaaS Security
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# Tycoon2FA ― MFA突破がPhishing-as-a-Serviceとして「産業化」した

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">March 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / AiTM Phishing</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Credential Attacks / Passkey &amp; Phishing-resistant MFA / Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / IAM / SOC</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / Financial Fraud / SaaS Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoftは2026年3月4日、Tycoon2FAが世界で毎月50万超の組織に到達するCampaignを可能にし、数千万件規模のPhishing Messageに利用されたと報告しました。[^source]

Tycoon2FAの本質はPasswordを盗むだけではありません。被害者のCredentialとMFAを正規ServiceへReal-time Relayし、その後に発行されるSession Cookieまで取得することで、SMS、OTP、Push等の一般的なMFAを実質的に迂回します。つまり**MFAの存在を前提に設計された犯罪Infrastructure**です。

</div>

## なぜ今なのか

MFA普及は攻撃を止めたのではなく、攻撃者のTargetを「Password」から「Authentication Process / Session」へ移しました。PhaaSによって高度なAiTM Infrastructureを低Skill Actorでも利用できます。

## 攻撃Flow

<div class="sil-flow" role="group" aria-label="Tycoon2FA attack flow">
  <div class="sil-flow-step"><strong>Phishing Email / Link / Attachment</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Redirect / CAPTCHA / Anti-analysis</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>偽Sign-in + AiTM Relay</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>正規MFA Challenge</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Session Cookie Capture</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step sil-flow-step-impact"><strong>Account Access / Mailbox Rule / Authenticator追加</strong></div>
</div>

<!-- AUTO:MITRE:START -->
## MITRE ATT&CK® Mapping

<div class="sil-mitre-note" markdown>

この表は、攻撃・Campaignの理解に有用な場合だけ表示します。`Source-labeled` は一次情報がATT&CK IDを明示したもの、`Analyst-mapped` は一次情報に記載された行動を本LibraryがATT&CKへ対応付けたものです。後者は、元情報の発行者がそのATT&CK IDを明示したことを意味しません。

</div>

| Technique | Tactic | Basis | Article context |
| --- | --- | --- | --- |
| [T1566.002 Spearphishing Link](https://attack.mitre.org/techniques/T1566/002/) | Initial Access | Analyst-mapped | Microsoftが観測したLinkを用いるPhishing Deliveryに対応。Tycoon2FAの全Delivery方式をこのTechniqueだけで表すものではない。 |
| [T1557 Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/) | Credential Access, Collection | Analyst-mapped | 正規Authentication Serviceとの間にAiTM Proxyを置き、認証TrafficをRelayする行動に対応。 |
| [T1539 Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539/) | Credential Access | Analyst-mapped | MFA完了後のSession Cookieを取得し、再認証なしでAccount Accessへ利用する行動に対応。 |

<div class="sil-mitre-legal">
MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation. © 2026 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation.
</div>
<!-- AUTO:MITRE:END -->

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| MFA Strategy | MFA導入率だけではRiskを説明できない |
| Session | Password変更だけでは侵害Sessionが残る可能性 |
| BEC / Fraud | Mailbox RuleやAccount乗っ取りが財務被害へ波及 |
| Detection | 短命Domain・CAPTCHA・ObfuscationでStatic IOC依存が弱くなる |

## 日本企業への示唆

Privileged Userや財務・人事など高Risk Roleでは、Phishing-resistant Authenticationを優先すべきです。Incident ResponseでもPassword ResetだけでなくSession / Token Revoke、MFA Device、Inbox Ruleまで確認する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. 高Risk RoleへPasskey / FIDO2を優先展開する
2. Conditional AccessでAuthentication Strengthを要求する
3. Incident時にActive Session / TokenをRevokeする
4. MFA Device追加とInbox Rule変更を監視する
5. Risky Sign-inとPhishing Clickを相関分析する
6. CAPTCHAや正規Login画面が見えることを「安全の証拠」と教育しない

</div>

## 用語解説

**AiTM (Adversary-in-the-Middle)**  
被害者と正規認証Serviceの間でTrafficをRelayし、Credentialだけでなく認証後のSession Token / Cookieまで取得する攻撃方式。

## 関連記事

- [AiTM Token Compromise](aitm-token-compromise-code-of-conduct.md)
- [Passkey時代の次の攻撃面](passkey-enrollment-recovery-attacks.md)

## 参考情報

- [Microsoft Security Blog, Inside Tycoon2FA: How a leading AiTM phishing kit operated at scale](https://www.microsoft.com/en-us/security/blog/2026/03/04/inside-tycoon2fa-how-a-leading-aitm-phishing-kit-operated-at-scale/)

[^source]: [Microsoft Security Blog, Inside Tycoon2FA](https://www.microsoft.com/en-us/security/blog/2026/03/04/inside-tycoon2fa-how-a-leading-aitm-phishing-kit-operated-at-scale/)

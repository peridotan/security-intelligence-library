---
title: AI-enabled Device Code Phishing ― Passwordを盗まずTokenを取る攻撃がScaleする
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-04
description: Microsoftが2026年4月6日に報告したDevice Code Phishing Campaignを基に、Dynamic Code
  Generation、OAuth Token、MFA、Device Registrationを含む攻撃Chainを整理する。
category: Identity Security / OAuth Abuse
collections:
- identity-security
- cybersecurity
topics:
- Credential Attacks
- Identity Security
tags:
- Microsoft Entra
- Device Code
- OAuth
- EvilTokens
- Phishing-as-a-Service
- Access Token
- Refresh Token
- Device Registration
mitre_attack:
- id: T1566.002
  basis: Analyst-mapped
  note: Phishing LinkからDevice Code認証Flowへ誘導するInitial Accessに対応。
- id: T1528
  basis: Analyst-mapped
  note: 被害者の認証後にAccess / Refresh Tokenを攻撃者側Sessionへ取得する行動に対応。
- id: T1098.005
  basis: Analyst-mapped
  note: 侵害後に新しいDeviceを登録し、長期Accessへつなげた観測に対応。
- id: T1114.003
  basis: Analyst-mapped
  note: 悪意あるInbox RuleによるMail転送・隠蔽・継続Collectionに対応。
audience:
- CISO
- IAM
- SOC
- Microsoft 365
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
# AI-enabled Device Code Phishing ― Passwordを盗まずTokenを取る攻撃がScaleする

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">April 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / OAuth Abuse</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Credential Attacks / Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">CISO / IAM / SOC / Microsoft 365</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / Financial Fraud / SaaS Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoftは2026年4月6日、OAuth 2.0 Device Authorization Flowを悪用して組織Accountを侵害する大規模Phishing Campaignを報告しました。攻撃InfrastructureはAutomationとDynamic Device Code Generationを使い、従来のStatic Code方式で障害となっていた15分のCode有効期限を事実上回避しています。[^source]

この攻撃ではPasswordを直接盗む必要がありません。被害者自身が正規Microsoft Loginで認証し、攻撃者が開始したSessionを承認することで、有効なAccess / Refresh Tokenが攻撃者側へ渡ります。

</div>

## なぜ今なのか

Device Code FlowはSmart TVやCLI等、Keyboard入力が難しいDevice向けの正規OAuth Flowです。その正規性がSocial Engineeringに悪用されます。Dynamic Generationにより、被害者がLinkをClickした時点で新しいDevice Codeを生成できるため、Campaignを大規模化しやすくなりました。

## 攻撃Chain

1. Invoice / RFP / Shared File等のLureを送信
2. Threat Actor-controlled Pageへ誘導
3. BackendがMicrosoft IdPへDevice CodeをReal-timeで要求
4. VictimへCodeと正規`microsoft.com/devicelogin`を提示
5. VictimがPassword / MFAを含む正規認証を実施
6. Attack BackendがAccess Tokenを取得
7. Device Registration、Inbox Rule、Mail Exfiltration等へ展開

<!-- AUTO:MITRE:START -->
## MITRE ATT&CK® Mapping

<div class="sil-mitre-note" markdown>

この表は、攻撃・Campaignの理解に有用な場合だけ表示します。`Source-labeled` は一次情報がATT&CK IDを明示したもの、`Analyst-mapped` は一次情報に記載された行動を本LibraryがATT&CKへ対応付けたものです。後者は、元情報の発行者がそのATT&CK IDを明示したことを意味しません。

</div>

| Technique | Tactic | Basis | Article context |
| --- | --- | --- | --- |
| [T1566.002 Spearphishing Link](https://attack.mitre.org/techniques/T1566/002/) | Initial Access | Analyst-mapped | Phishing LinkからDevice Code認証Flowへ誘導するInitial Accessに対応。 |
| [T1528 Steal Application Access Token](https://attack.mitre.org/techniques/T1528/) | Credential Access | Analyst-mapped | 被害者の認証後にAccess / Refresh Tokenを攻撃者側Sessionへ取得する行動に対応。 |
| [T1098.005 Device Registration](https://attack.mitre.org/techniques/T1098/005/) | Persistence, Privilege Escalation | Analyst-mapped | 侵害後に新しいDeviceを登録し、長期Accessへつなげた観測に対応。 |
| [T1114.003 Email Forwarding Rule](https://attack.mitre.org/techniques/T1114/003/) | Collection | Analyst-mapped | 悪意あるInbox RuleによるMail転送・隠蔽・継続Collectionに対応。 |

<div class="sil-mitre-legal">
MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation. © 2026 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation.
</div>
<!-- AUTO:MITRE:END -->

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| MFA | MFA成功そのものがAttack Session承認に使われ得る |
| OAuth | 正規Authentication FlowのAbuseを監視する必要 |
| SaaS | Endpoint MalwareなしでもMicrosoft 365を侵害可能 |
| Fraud | Mailbox Reconnaissanceから送金詐欺へ発展可能 |

## 日本企業への示唆

Device Code Flowを業務で使わない組織はConditional AccessでBlockすることが有効です。必要な場合もUser / App / Device条件を限定し、Device RegistrationやToken利用を監視します。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Device Code Flowの利用実態を確認する
2. 不要な場合はConditional AccessでBlockする
3. Device Code AuthenticationをSign-in Logで監視する
4. 不審なDevice Registrationを検知する
5. Incident時はPassword変更だけでなくRefresh TokenをRevokeする
6. Mailbox Rule / Graph API AccessをPost-compromise Indicatorとして監視する

</div>

## 用語解説

**Device Code Flow**  
入力能力の限られたDevice等で、別Browserに短いCodeを入力して認証を完了するOAuth 2.0の正規認証方式。

## 関連記事

- [AiTM Token Compromise](aitm-token-compromise-code-of-conduct.md)
- [Large-Scale Credential Attacks](../cybersecurity/large-scale-credential-attacks.md)

## 参考情報

- [Microsoft Security Blog, Inside an AI-enabled device code phishing campaign](https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/)

[^source]: [Microsoft Security Blog, AI-enabled Device Code Phishing](https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/)

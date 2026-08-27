---
title: Advanced Account Security ― 高Risk AI Accountでは「認証」と「回復」を同じ強度で守る
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-04
description: OpenAIが2026年4月30日に公表したAdvanced Account Securityを基に、Passkey、Passwordless、Recovery、Session、High-risk
  Capabilityを統合したIdentity Securityを整理する。
category: Identity Security / Account Protection
collections:
- identity-security
- ai-security
topics:
- Passkey & Phishing-resistant MFA
- Identity Security
- AI Cyber Capability
tags:
- OpenAI
- Advanced Account Security
- Passkey
- Security Key
- Account Recovery
- Session Management
- Trusted Access for Cyber
audience:
- CISO
- IAM
- AI Governance
- High-risk User
management_impact: High
impact_types:
- Identity
- AI Governance
- Account Takeover
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# Advanced Account Security ― 高Risk AI Accountでは「認証」と「回復」を同じ強度で守る

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">April 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / Account Protection</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Passkey &amp; Phishing-resistant MFA / Identity Security / AI Cyber Capability</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">CISO / IAM / AI Governance / High-risk User</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / AI Governance / Account Takeover</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

OpenAIは2026年4月30日、ChatGPT / Codex Account向けにAdvanced Account Securityを公表しました。設定を有効化すると、Password Loginを無効化してPasskeyまたはPhysical Security Keyを要求し、Email / SMS Recoveryも無効化、Session短縮、Login Alert、Active Session管理等を組み合わせます。[^source]

注目すべき点は、**Loginだけを強化してRecoveryを弱いまま残さない**ことです。さらにOpenAIは、最もCyber Capabilityの高いModelへTrusted Accessで接続する個人利用者に対し、2026年6月1日からこのProtectionを必須化するとしました。

</div>

## なぜ今なのか

AI Accountは会話履歴だけでなく、Code、Connected Tool、Organization Context、Developer Workflowへ接続されるようになっています。高Risk AI Capabilityを利用できるAccountが乗っ取られれば、通常のSaaS Account以上のImpactを持つ可能性があります。

## Controlの構成

- Passkey / FIDO Security Key
- Password Login Disable
- Email / SMS Recovery Disable
- Backup Passkey / Recovery Key
- Shorter Session
- Login Alert
- Active Session Visibility
- High-risk Capabilityとの連動

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Identity Governance | User RiskだけでなくCapability RiskでAuthentication Levelを変える |
| Recovery | Helpdesk Recoveryが弱点にならない設計が必要 |
| Session | Strong Authentication後のSession Theftも考慮 |
| AI Governance | Agent / Cyber CapabilityとIdentity Assuranceを接続する必要 |

## 日本企業への示唆

企業内でもAdministrator、Security Researcher、AI Agent Operator等の高Risk Roleでは、Passkey導入だけでなくRecovery、Session、Device、Helpdesk Flowまで同じAssurance Levelに揃える必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. 高Risk Roleを定義しPhishing-resistant MFAを必須化する
2. Email / SMS Recovery依存を減らす
3. Backup Authenticator / Recovery Key運用を設計する
4. HelpdeskによるAuthentication ResetをHigh-risk Processとして管理する
5. Session LifetimeとRisk-based Reauthenticationを見直す
6. 高Risk AI CapabilityへのAccessをIdentity Assuranceと連動させる

</div>

## 用語解説

**Recovery Assurance**  
Account Recovery時にも通常Loginと同等のIdentity確認強度を維持し、Recovery経路がAuthenticationのBypassにならないようにする考え方。

## 関連記事

- [Passkey時代の次の攻撃面](passkey-enrollment-recovery-attacks.md)
- [Cyber能力へのAccess Control](../ai-security/openai-trusted-access-cyber.md)

## 参考情報

- [OpenAI, Introducing Advanced Account Security](https://openai.com/index/advanced-account-security/)

[^source]: [OpenAI, Advanced Account Security](https://openai.com/index/advanced-account-security/)

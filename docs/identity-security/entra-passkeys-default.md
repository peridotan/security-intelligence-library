---
title: Microsoft Entra IDがPasskeyを既定へ ― SMS / Voice MFA終了に向けた移行設計
date: 2026-08-26
updated: 2026-08-26
description: Microsoftが2026年7月に発表したEntra IDのPasskey既定化とMicrosoft提供SMS・音声認証終了のロードマップを企業Identity移行の観点から整理する。
category: Identity Security
tags:
- Microsoft Entra ID
- Passkey
- Phishing-resistant MFA
- Authentication
audience:
- Executive
- CISO
- IAM
- IT Operations
management_impact: High
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
source_period: 2026-07
---

# Microsoft Entra IDがPasskeyを既定へ ― SMS / Voice MFA終了に向けた移行設計

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / IAM / IT Operations</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoftは2026年7月13日、Entra IDでPasskeyを既定のPhishing-resistant Authenticationとして推進し、2026年9月1日からSMS / Voice利用者をPasskey登録対象へ順次移行、2027年2月1日にMicrosoft提供のSMS / Voice Deliveryを終了する方針を発表しました。[^source]

これは単なる認証機能追加ではなく、企業IAMにおける「MFAなら何でもよい」時代から、**Phishing-resistant AuthenticationをDefaultにする移行**です。

</div>

## なぜ今なのか

SMS、Voice、OTP、Push等はMFA導入率を大きく高めましたが、Social Engineering、SIM Swap、Adversary-in-the-Middle等により攻撃可能性が残ります。

MicrosoftはPasskeyを標準経路にし、SMS / Voiceを例外的なOperational / Regulatory Requirementへ位置づけ直しています。

## 何が変わるのか

Microsoftの公表では、Public CloudのEntra IDについて概ね次のTimelineです。

| 時期 | 変更 |
| --- | --- |
| 2026-09-01 | SMS / Voice対象利用者をPasskey有効化・登録Campaign対象へ |
| 2026-09-18 | Telecom Provider情報の提供予定 |
| 2026-10-30 | 必要な組織が外部Telecom Providerを構成可能になる予定 |
| 2027-02-01 | Microsoft提供SMS / Voice Delivery終了 |

組織側は、SMS / Voice利用者の棚卸し、Passkey対応端末、User Communication、Recovery、例外利用を事前に設計する必要があります。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Identity Risk | Phishable MFAへの依存を大幅に減らせる |
| Migration | User Experience、端末、Helpdesk、Recoveryの変更が必要 |
| Compliance | SMSを必要とする特殊要件の確認が必要 |
| Cost | SMS継続時は外部Provider契約・費用が発生する可能性 |

## 日本企業への示唆

「Passkeyを有効にする」だけでは不十分です。既存のSMS利用者、業務用端末、BYOD、Shared Device、海外拠点、Guest、Recovery Scenarioを分類した移行計画が必要です。

特に登録・回復フローを攻撃者が狙い始めているため、Passkey導入と同時にEnrollment Securityを強化する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Entra IDでSMS / Voice有効ユーザーを棚卸しする
2. User Segment別にSynced / Device-bound Passkey方針を決める
3. Pilot → Registration Campaign → 全社展開の順で移行する
4. Helpdesk / RecoveryをPasskey前提で再設計する
5. SMS継続が必要な規制・業務理由を文書化する
6. Conditional Access / ITDRと組み合わせる

</div>

## 用語解説

**Phishing-resistant Authentication**  
Credentialを偽サイトへ入力・Replayさせる典型的なPhishing攻撃に耐性を持つ認証方式。Passkey / FIDO2等が代表例。

## 関連記事

- [Passkey時代の次の攻撃面](passkey-enrollment-recovery-attacks.md)
- [Passkeyは破られたのか](pass-the-passkey.md)

## 参考情報

- [Microsoft Security Blog, Passkeys are the default authentication method in Entra ID](https://www.microsoft.com/en-us/security/blog/2026/07/13/microsoft-entra-id-security-updates-passkeys-are-the-default-authentication-method-in-entra-id/)
- [Microsoft Learn, Passkeys by default and retirement of Microsoft-provided SMS and voice authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement)

[^source]: [Microsoft Security Blog, Passkeys are the default authentication method in Entra ID](https://www.microsoft.com/en-us/security/blog/2026/07/13/microsoft-entra-id-security-updates-passkeys-are-the-default-authentication-method-in-entra-id/)

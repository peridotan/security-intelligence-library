---
title: Passkey時代の次の攻撃面 ― 登録・回復フローを狙うSocial Engineering
date: 2026-08-26
updated: 2026-08-26
description: Okta Threat Intelligenceが2026年7月に報告したPasskey登録・セルフサービス回復フローへの攻撃を基に、フィッシング耐性MFA導入後のIdentity
  Securityを整理する。
category: Identity Security
tags:
- Passkey
- Account Recovery
- MFA Enrollment
- Social Engineering
audience:
- Executive
- CISO
- IAM
- Helpdesk
management_impact: High
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
source_period: 2026-07
---

# Passkey時代の次の攻撃面 ― 登録・回復フローを狙うSocial Engineering

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / IAM / Helpdesk</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Okta Threat Intelligenceは2026年7月、攻撃者が利用者を電話等で誘導し、攻撃者が開始したMFA登録やPassword Resetを被害者自身に承認させる活動が増えていると報告しました。O-UNC-066ではPasskey登録を口実に、攻撃者管理のPasskeyをEntra Accountへ登録させる手法が観測されています。[^source]

これはPasskeyの暗号方式が破られたのではありません。**強固なAuthenticatorを守っても、そのAuthenticatorを追加・再登録するEnrollment / Recovery Processが弱ければAccount Takeoverが成立する**という問題です。

</div>

## なぜ今なのか

Phishing-resistant MFAを導入すると、Password + OTPを盗んでReplayする従来型Attackは難しくなります。

攻撃者はその代わりに、以下の「正規フロー」を狙います。

- Passkey / MFAの追加登録
- Self-Service Password Reset
- HelpdeskによるRecovery
- Device Registration
- MFA Method変更

認証の強度が上がるほど、**LifecycleとRecoveryが新しい最弱点**になります。

## 何が起きているのか

Oktaは、Passkeyを文字列として盗むのではなく、利用者をSocial Engineeringで誘導して「攻撃者側のAuthenticatorを正規登録させる」活動を観測しています。

また別のClusterでは、攻撃者が被害者へ電話しながらForgot Password Flowを同時実行し、Phishing-resistantでないMFA要素を使って本人確認を通す方法が報告されています。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Authentication Strategy | Passkey導入だけでAccount Takeover Riskはゼロにならない |
| Helpdesk Risk | Recovery担当者・本人確認手続きが攻撃対象になる |
| Persistence | 攻撃者Passkeyが登録されると長期的な正規アクセスになり得る |
| Detection | 「成功ログイン」よりAuthentication Method変更の監視が重要 |

## 日本企業への示唆

Passkey導入Projectでは、Login Flowだけでなく、登録、紛失、機種変更、Helpdesk Recovery、退職・異動、Authenticator削除までを設計範囲に含める必要があります。

とくに電話での本人確認や「利用者が操作できるから本人」という前提は見直す必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Passkey / MFA追加登録をHigh-risk Eventとして監視する
2. Authentication Method変更時に既存の強固なFactorで再認証する
3. Helpdesk Recoveryの本人確認を強化し、例外手続きを監査する
4. SSPRでPhishable Factorだけによる回復を避ける
5. 新規Authenticator登録後のRisk-based Restrictionを検討する
6. ITDRでEnrollment / Recovery / Sessionを連続的に監視する

</div>

## 用語解説

**Enrollment Attack**  
AuthenticatorやMFA Methodの追加登録フローを悪用し、攻撃者管理の認証手段を正規登録する攻撃。

**Recovery Attack**  
Password Reset、Account Recovery、Helpdesk等の回復手続きを迂回路として悪用する攻撃。

## 関連記事

- [Passkeyは破られたのか](pass-the-passkey.md)
- [Large-Scale Credential Attacks](../cybersecurity/large-scale-credential-attacks.md)

## 参考情報

- [Okta Threat Intelligence, How to stop attackers from self-serving their way into accounts](https://www.okta.com/blog/threat-intelligence/intrusion-actors-self-serve-their-way-into-accounts/)
- [Okta Threat Intelligence](https://www.okta.com/blog/threat-intelligence/)

[^source]: [Okta Threat Intelligence, How to stop attackers from self-serving their way into accounts](https://www.okta.com/blog/threat-intelligence/intrusion-actors-self-serve-their-way-into-accounts/)

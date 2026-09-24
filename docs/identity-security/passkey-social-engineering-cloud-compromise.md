---
title: Passkey-themed Social Engineering ― 強い認証の「周辺」がCloud侵害へつながる
date: 2026-09-24
updated: 2026-09-24
reviewed: 2026-09-24
review_status: Current
source_period: 2026-09
description: Microsoftが2026年9月9日に報告したPasskey / MFA / SSO更新を口実とするSocial Engineeringから、AiTM・Device
  Code・認証手段追加・Microsoft Graph Recon・Cloud Data Collectionへ進むCampaignを整理する。
category: Identity Security / Social Engineering
collections:
- identity-security
- cybersecurity
- risk-management
topics:
- Identity Security
- Passkey & Phishing-resistant MFA
- Credential Attacks
tags:
- Microsoft
- Passkey
- Device Code
- AiTM
- MFA Enrollment
- Session Token
- Microsoft Graph
- Cloud Identity
- Social Engineering
audience:
- Executive
- CISO
- IAM
- SOC
management_impact: High
impact_types:
- Identity
- Cloud
- Data Exfiltration
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# Passkey-themed Social Engineering ― 強い認証の「周辺」がCloud侵害へつながる

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-09-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">September 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-09-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-09-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / Social Engineering</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Identity Security / Passkey &amp; Phishing-resistant MFA / Credential Attacks</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / IAM / SOC</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / Cloud / Data Exfiltration</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoft Security Researchは2026年9月9日、Passkey、MFA、SSOの設定更新を口実にUserへ接触し、Cloud Identity侵害へつなげるActive Campaignを報告しました。活動は2026年5月以降に観測され、異常Sign-inの後に攻撃者管理の認証手段追加、Microsoft Graphを使ったReconnaissance、SharePoint / OneDrive Download、Exchange経由のMail Collectionへ進む例が確認されています。[^source]

重要なのは、**Passkeyそのものが破られたという報告ではない**点です。PasskeyはUserを誘導するPretextとして使われ、実際のInitial AccessではAiTM PhishingやDevice Code Flowが悪用されました。その後、攻撃者は追加認証手段やToken / Sessionを使ってPersistenceとCloud Data Accessへ進みます。

したがって、Phishing-resistant MFA導入後も、Enrollment、Recovery、Device Code、Session Token、Authentication Method Changeを別のHigh-risk Controlとして扱う必要があります。

</div>

## なぜ今なのか

Passkey導入が進むほど、攻撃者は「Passkeyを突破する」よりも、**Passkey設定を支援するIT担当者を装う、別の認証FlowへUserを誘導する、登録後のSessionを奪う**といった周辺経路へ移る可能性があります。

Microsoftの観測では、攻撃開始時のPhone / SMSがPersonal Device上で行われる場合、Corporate Endpoint Telemetryに痕跡が残りにくく、Userの申告と後続Cloud Signalをつないで復元する必要があります。

## 攻撃Chain

<div class="sil-flow" role="group" aria-label="Passkey themed social engineering cloud compromise flow">
  <div class="sil-flow-step"><strong>Phone / SMS / Trusted Message</strong><span>Passkey / MFA / SSO更新を要求</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>AiTM / Device Code</strong><span>Credential・Session / Access Tokenを取得</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Authentication Method Addition</strong><span>攻撃者管理のMFA手段を追加</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Microsoft Graph Recon</strong><span>User / Group / Role / App / Repositoryを列挙</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step sil-flow-step-impact"><strong>SharePoint / OneDrive / Exchange Collection</strong></div>
</div>

## 経営インパクト

| 観点 | 経営上の意味 |
| --- | --- |
| Passkey | Strong Authentication導入だけでは周辺FlowのRiskは消えない |
| Enrollment | 認証手段追加を通常User操作ではなくHigh-risk Operationとして扱う必要 |
| Device Code | Legitimate Authentication FlowがSocial Engineering経由で悪用され得る |
| Session / Token | Password Resetだけでは継続Sessionを止められない場合がある |
| Cloud Data | Identity侵害がGraph経由でSaaS Data Collectionへ短時間で接続する |
| Detection | Sign-in、認証手段変更、Graph、SharePoint、Exchangeを横断相関する必要 |

## 日本企業への示唆

Passkey導入計画では、Login Ceremonyだけでなく**登録・再登録・回復・Helpdesk・Device Code・Session失効**までを一つのIdentity Lifecycleとして設計することが重要です。

特に「IT部門からPasskey更新の電話が来た」というシナリオは、技術Controlだけでは止めにくいため、正規Support Channelの固定、Out-of-band Verification、Authentication Method Changeの監視を組み合わせる必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. **Authentication Method RegistrationをHigh-risk Operationとして保護する** — Managed Device、Phishing-resistant MFA、Risk条件等を組み合わせる。
2. **Device Code Flowの利用範囲を棚卸しする** — 不要なClient / Scenarioでは制限する。
3. **新規MFA手段追加を監視する** — Risky Sign-inと時間的に近い変更を優先Alertにする。
4. **Incident時にSession / Refresh Tokenを失効する** — Password ResetだけでContainment完了としない。
5. **Graph ReconからData Collectionまで相関する** — Directory / App / SharePoint / OneDrive / Exchangeを横断する。
6. **HelpdeskのPasskey支援手順を固定する** — Phone / SMSだけでUserに登録操作を求めない。

</div>

## 用語解説

**AiTM（Adversary-in-the-Middle）**  
Userと正規Serviceの間に攻撃者のProxy等を介在させ、CredentialやSession Tokenを取得するPhishing手法。

**Device Code Flow**  
入力能力が限られるDevice等でUserが別画面からCodeを入力して認証するOAuth系のFlow。正規機能ですが、攻撃者がUserを誘導すると攻撃者Controlled ClientへのAuthorizationに悪用され得ます。

## 関連記事

- [IT Support Impersonation ― Teamsの「信頼」がRemote SessionからDomain侵入へつながる](teams-it-support-remote-session-intrusion.md)

## 参考情報

- [Microsoft Security Research, Passkey-themed social engineering leads to identity and cloud compromise (2026-09-09)](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/)

[^source]: [Microsoft Security Research, Passkey-themed social engineering leads to identity and cloud compromise (2026-09-09)](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/)

---
title: ShinyHunters型SaaS Data Theft ― VishingでSSOを奪い、Cloud Dataを直接盗む
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-01
description: Mandiant / GTIGが2026年1月30日に公開したShinyHunters-branded SaaS Data Theftを基に、Vishing、SSO
  Credential、MFA Device Enrollment、SaaS Exfiltration、Extortionを整理する。
category: Identity Security / SaaS Identity
collections:
- identity-security
- cybersecurity
topics:
- Credential Attacks
- Identity Security
- Third-party Risk / C-SCRM
tags:
- Mandiant
- GTIG
- ShinyHunters
- Vishing
- SSO
- MFA
- SaaS
- Extortion
mitre_attack:
- id: T1566.004
  basis: Analyst-mapped
  note: Mandiantが観測したVoice PhishingによるSocial EngineeringのInitial Accessに対応。
- id: T1078
  basis: Analyst-mapped
  note: 取得したSSO CredentialとMFAを使い正規AccountとしてSaaSへAccessする行動に対応。
- id: T1098.005
  basis: Analyst-mapped
  note: 攻撃者が被害組織のMFAへUnauthorized Deviceを登録する観測に対応。
audience:
- Executive
- CISO
- IAM
- SOC
management_impact: High
impact_types:
- Identity
- SaaS Security
- Extortion
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# ShinyHunters型SaaS Data Theft ― VishingでSSOを奪い、Cloud Dataを直接盗む

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">January 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / SaaS Identity</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Credential Attacks / Identity Security / Third-party Risk / C-SCRM</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / IAM / SOC</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / SaaS Security / Extortion</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Mandiant / Google Threat Intelligence Groupは2026年1月30日、ShinyHunters-branded Extortionに関連する複数Threat Clusterが、Voice PhishingとVictim-branded Credential Harvestingを使ってSSO CredentialとMFA Codeを取得し、Cloud SaaSからDataを窃取する活動を拡大していると報告しました。[^source]

Compromise後はSaaS Application内のSensitive DataやInternal CommunicationをExfiltrateし、そのDataをExtortionへ利用します。MandiantはUnauthorized DeviceのMFA Enrollmentも観測しています。

この攻撃はProduct Vulnerabilityではなく、**Identity TrustとSaaS Accessを直接狙う攻撃**です。

</div>

## なぜ今なのか

企業Dataの多くがSaaSへ移ると、EndpointへMalwareを入れなくても、SSO Identityを奪えば直接Business Dataへ到達できます。

## 攻撃Flow

<div class="sil-flow" role="group" aria-label="ShinyHunters SaaS data theft flow">
  <div class="sil-flow-step"><strong>Vishing / Victim-branded Credential Site</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>SSO Credential + MFA Code</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Unauthorized MFA Device Enrollment</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>SaaS Access</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Data / Internal Communication Exfiltration</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step sil-flow-step-impact"><strong>Extortion</strong></div>
</div>

<!-- AUTO:MITRE:START -->
## MITRE ATT&CK® Mapping

<div class="sil-mitre-note" markdown>

この表は、攻撃・Campaignの理解に有用な場合だけ表示します。`Source-labeled` は一次情報がATT&CK IDを明示したもの、`Analyst-mapped` は一次情報に記載された行動を本LibraryがATT&CKへ対応付けたものです。後者は、元情報の発行者がそのATT&CK IDを明示したことを意味しません。

</div>

| Technique | Tactic | Basis | Article context |
| --- | --- | --- | --- |
| [T1566.004 Spearphishing Voice](https://attack.mitre.org/techniques/T1566/004/) | Initial Access | Analyst-mapped | Mandiantが観測したVoice PhishingによるSocial EngineeringのInitial Accessに対応。 |
| [T1078 Valid Accounts](https://attack.mitre.org/techniques/T1078/) | Initial Access, Persistence, Privilege Escalation, Defense Evasion | Analyst-mapped | 取得したSSO CredentialとMFAを使い正規AccountとしてSaaSへAccessする行動に対応。 |
| [T1098.005 Device Registration](https://attack.mitre.org/techniques/T1098/005/) | Persistence, Privilege Escalation | Analyst-mapped | 攻撃者が被害組織のMFAへUnauthorized Deviceを登録する観測に対応。 |

<div class="sil-mitre-legal">
MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation. © 2026 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation.
</div>
<!-- AUTO:MITRE:END -->

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Identity | SSOがEnterprise DataへのMaster Keyになる |
| SaaS | Endpoint Securityを通らずData Theftが成立 |
| Helpdesk | Voice Social Engineering対策が必要 |
| Incident | MFA Reset / Device Enrollment / Sessionまで確認する必要 |

## 日本企業への示唆

High-value SaaSへはPasskey / FIDO2等のPhishing-resistant Authenticationを優先し、MFA Device登録やRecovery EventをHigh-risk Eventとして監視すべきです。

<div class="sil-action-box" markdown>

## 推奨アクション

1. High-value SaaSへPhishing-resistant MFAを要求する
2. MFA Device追加をAlert対象にする
3. Helpdeskの本人確認を強化する
4. SSO LoginとSaaS Data Downloadを相関する
5. SaaS Session / Token Revoke手順を整備する
6. VishingをIncident Exerciseへ追加する

</div>

## 用語解説

**SaaS Data Theft**  
EndpointやServerを深く侵害せず、正規SaaS Account / Sessionを悪用してCloud上のDataを直接窃取する攻撃。

## 関連記事

- [Teams Vishing](teams-vishing-quick-assist.md)
- [Tycoon2FA](tycoon2fa-aitm-phaas.md)

## 参考情報

- [Google Cloud / Mandiant, Vishing for Access: Tracking the Expansion of ShinyHunters-Branded SaaS Data Theft](https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft)
- [Google Cloud / Mandiant, Proactive Defense Against ShinyHunters-Branded Data Theft Targeting SaaS](https://cloud.google.com/blog/topics/threat-intelligence/defense-against-shinyhunters-cybercrime-saas)

[^source]: [Mandiant / GTIG, ShinyHunters-branded SaaS data theft](https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft)

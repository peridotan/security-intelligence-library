---
title: Edge ApplianceからIdentity侵害へ ― F5 / Confluence攻撃Chainが示す境界防御の盲点
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-05
description: Microsoftが2026年5月22日に報告したF5 BIG-IPからConfluenceへPivotしたLinux intrusionを基に、Edge
  Device、Legacy、Credential、Identityを一続きで守る必要性を整理する。
category: Cybersecurity / Edge Security
collections:
- cybersecurity
- identity-security
topics:
- Vulnerability Management
- Identity Security
tags:
- F5 BIG-IP
- Confluence
- Linux
- Edge Appliance
- Credential Theft
- EOL
mitre_attack:
- id: T1021.004
  basis: Source-labeled
  note: Microsoftが本CampaignのObserved ATT&CK TechniqueとしてSSH利用を明示。
- id: T1083
  basis: Source-labeled
  note: MicrosoftがLinux Host上のFile EnumerationをObserved ATT&CK Techniqueとして明示。
- id: T1190
  basis: Source-labeled
  note: Microsoftが脆弱なConfluence ServerへのRCEをObserved ATT&CK Techniqueとして明示。
- id: T1505
  basis: Source-labeled
  note: MicrosoftがConfluence Web Server上のWeb ShellによるPersistent AccessをT1505として明示。
- id: T1078.002
  basis: Source-labeled
  note: MicrosoftがConfluence ServerのDomain Credential利用をObserved ATT&CK Techniqueとして明示。
- id: T1187
  basis: Source-labeled
  note: MicrosoftがDomain Controllerを狙うAuthentication Coercion / Relay行動を明示。
- id: T1557
  basis: Source-labeled
  note: MicrosoftがRelay-style Authentication AttackをAdversary-in-the-Middleとして明示。
audience:
- CISO
- Infrastructure
- SOC
- IAM
management_impact: High
impact_types:
- Operational Security
- Identity
- Legacy Risk
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---
# Edge ApplianceからIdentity侵害へ ― F5 / Confluence攻撃Chainが示す境界防御の盲点

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">May 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / Edge Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Vulnerability Management / Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">CISO / Infrastructure / SOC / IAM</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Operational Security / Identity / Legacy Risk</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoftは2026年5月22日、Internet-facing F5 BIG-IP Applianceを起点としてLinux環境へ侵入し、内部のConfluence ServerへPivotしてCredential TheftとIdentity Compromiseへ進んだMulti-stage Attackを報告しました。観測されたBIG-IP Versionは2024年末にEOLとなっていたものです。[^source]

この事例の重要点は、Edge Device侵害を「Network機器の問題」で終わらせず、**Edge → Internal Server → Credential → Identity**というAttack Pathで捉える必要があることです。

</div>

## なぜ今なのか

Firewall、VPN、Load Balancer等のEdge ApplianceはInternetへ公開され、高権限Network位置を持つ一方、Server/Endpointと比べてEDRや通常のAsset Managementが適用しにくい場合があります。

EOL Productや管理不足のVirtual Applianceが残ると、内部侵入の入口になります。

## 攻撃Chain

- Internet-facing Edge Applianceへの侵入
- SSH等によるLinux HostへのAccess
- Internal Reconnaissance
- Confluence等のServerへPivot
- Credential Access
- Identity / Additional Systemへ横展開

Microsoftは特定Incidentだけでなく、Edge DeviceのN-day Vulnerabilityを入口にする高Impact Incidentの増加傾向も指摘しています。

<!-- AUTO:MITRE:START -->
## MITRE ATT&CK® Mapping

<div class="sil-mitre-note" markdown>

この表は、攻撃・Campaignの理解に有用な場合だけ表示します。`Source-labeled` は一次情報がATT&CK IDを明示したもの、`Analyst-mapped` は一次情報に記載された行動を本LibraryがATT&CKへ対応付けたものです。後者は、元情報の発行者がそのATT&CK IDを明示したことを意味しません。

</div>

| Technique | Tactic | Basis | Article context |
| --- | --- | --- | --- |
| [T1021.004 Remote Services: SSH](https://attack.mitre.org/techniques/T1021/004/) | Lateral Movement | Source-labeled | Microsoftが本CampaignのObserved ATT&CK TechniqueとしてSSH利用を明示。 |
| [T1083 File and Directory Discovery](https://attack.mitre.org/techniques/T1083/) | Discovery | Source-labeled | MicrosoftがLinux Host上のFile EnumerationをObserved ATT&CK Techniqueとして明示。 |
| [T1190 Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | Initial Access | Source-labeled | Microsoftが脆弱なConfluence ServerへのRCEをObserved ATT&CK Techniqueとして明示。 |
| [T1505 Server Software Component](https://attack.mitre.org/techniques/T1505/) | Persistence | Source-labeled | MicrosoftがConfluence Web Server上のWeb ShellによるPersistent AccessをT1505として明示。 |
| [T1078.002 Valid Accounts: Domain Accounts](https://attack.mitre.org/techniques/T1078/002/) | Initial Access, Persistence, Privilege Escalation, Defense Evasion | Source-labeled | MicrosoftがConfluence ServerのDomain Credential利用をObserved ATT&CK Techniqueとして明示。 |
| [T1187 Forced Authentication](https://attack.mitre.org/techniques/T1187/) | Credential Access | Source-labeled | MicrosoftがDomain Controllerを狙うAuthentication Coercion / Relay行動を明示。 |
| [T1557 Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/) | Credential Access, Collection | Source-labeled | MicrosoftがRelay-style Authentication AttackをAdversary-in-the-Middleとして明示。 |

<div class="sil-mitre-legal">
MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation. © 2026 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation.
</div>
<!-- AUTO:MITRE:END -->

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Asset Management | Network ApplianceもServer同等のLifecycle管理が必要 |
| Legacy Risk | EOL ApplianceはPatch不能・Detection不足の二重Risk |
| Identity | Edge侵害後の最終TargetがCredentialになる |
| Cloud | Marketplace / Templateから古いImageが残る可能性 |

## 日本企業への示唆

Cloud上のVirtual ApplianceやSIerが導入したGatewayは「Network機器」として別管理されることがあります。Version / EOL / Exposure / Admin AccessをCMDBへ統合し、Identity側の監視とつなげる必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Internet-facing Edge ApplianceをAsset Inventoryで特定する
2. Version / EOL / Security Update状況を継続確認する
3. 管理InterfaceとSSH Accessを制限する
4. Edgeから内部Serverへの通信をSegmentationする
5. Edge侵害後のCredential AccessをITDR / SIEMで監視する
6. Cloud Template / Marketplace Imageの古いVersionを棚卸しする

</div>

## 用語解説

**Edge Appliance**  
Firewall、VPN、Load Balancer、Gateway等、Internetと内部Networkの境界付近で動作するSecurity / Network機器。

## 関連記事

- [Large-Scale Credential Attacks](large-scale-credential-attacks.md)
- [2026年7月の実悪用Zero-day](july-2026-trust-infrastructure-zero-days.md)

## 参考情報

- [Microsoft, From edge appliance to enterprise compromise: Multi-stage Linux intrusion via F5 and Confluence](https://www.microsoft.com/en-us/security/blog/2026/05/22/from-edge-appliance-to-enterprise-compromise-multi-stage-linux-intrusion-via-f5-and-confluence/)

[^source]: [Microsoft, F5 / Confluence multi-stage intrusion](https://www.microsoft.com/en-us/security/blog/2026/05/22/from-edge-appliance-to-enterprise-compromise-multi-stage-linux-intrusion-via-f5-and-confluence/)

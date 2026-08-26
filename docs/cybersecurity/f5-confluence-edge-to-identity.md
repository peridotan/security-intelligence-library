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

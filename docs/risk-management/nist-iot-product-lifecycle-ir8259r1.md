---
title: NIST IR 8259r1 ― IoT Securityは「出荷前」ではなくEnd-of-LifeまでのProduct責任
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-04
description: NISTが2026年4月20日に公開したIR 8259r1を基に、IoT Product SecurityをPre-marketからPost-market、Support、EOLまで管理する考え方を整理する。
category: Risk Management / Product Security
collections:
- risk-management
- cybersecurity
topics:
- Third-party Risk / C-SCRM
- Security Governance & Risk Management
tags:
- NIST
- IR 8259r1
- IoT
- Product Security
- End-of-Life
- Vulnerability Disclosure
- Secure by Design
audience:
- Executive
- CISO
- Product Security
- Procurement
management_impact: High
impact_types:
- Product Security
- Supply Chain
- Lifecycle Risk
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# NIST IR 8259r1 ― IoT Securityは「出荷前」ではなくEnd-of-LifeまでのProduct責任

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">April 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Risk Management / Product Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Third-party Risk / C-SCRM / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Product Security / Procurement</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Product Security / Supply Chain / Lifecycle Risk</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NISTは2026年4月20日、IR 8259 Revision 1「Foundational Cybersecurity Activities for IoT Product Manufacturers」を公開しました。Revision 1はIoT Product全体を対象に広げ、Pre-marketからPost-marketまでのCybersecurity Activity、Customer Communication、Maintenance、Support、End-of-Lifeを強く意識した内容になっています。[^source]

ポイントは、Security FeatureをProductへ実装して出荷すれば終わりではなく、**販売後に脆弱性が見つかり、Updateされ、やがてSupport終了するまでをProduct Security責任として設計する**ことです。

</div>

## なぜ今なのか

IoT / Connected Productは長期間利用される一方、Software Update、Cloud Service、Mobile App、Component Dependency等を持ちます。

ManufacturerがSupport PeriodやVulnerability Responseを明確にしなければ、Customer側がSecurity Riskを管理できません。

## Lifecycleで見るべき項目

- Customer Security Requirementの把握
- Product Cybersecurity Requirementの設計
- Secure Development
- Vulnerability Handling
- Software / Firmware Update
- Customer Communication
- Maintenance / Support
- End-of-Life / End-of-Support

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Product Liability | Security Supportの長さと品質がProduct価値へ影響 |
| Procurement | Purchase時にEOL / Support Period確認が必要 |
| Supply Chain | Component更新不能がProduct全体のRiskになる |
| Cost | 長期SupportをProduct Pricing / Lifecycle Costへ織り込む必要 |

## 日本企業への示唆

製造業・IoT Vendorだけでなく、Connected Deviceを購入・利用する企業にも重要です。調達時に「何年間Patchされるか」「EOL後にどのような移行策があるか」をSecurity Requirementとして確認する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Product / DeviceごとにSupport PeriodをInventory化する
2. Vendor契約へSecurity Update期間を明記する
3. Vulnerability Disclosure / PSIRT能力を確認する
4. EOL前のReplacement Planを作る
5. Component / Firmware Dependencyを把握する
6. Unsupported ProductをException管理ではなくRisk Registerへ載せる

</div>

## 用語解説

**Post-market Cybersecurity**  
Product販売後のVulnerability Handling、Update、Support、Customer Communication、End-of-Life等を含むCybersecurity Activity。

## 関連記事

- [NIST SP 1326 C-SCRM Due Diligence](c-scrm-due-diligence-sp1326.md)
- [SCS評価制度](japan-scs-evaluation-operationalization.md)

## 参考情報

- [NIST, Foundational Cybersecurity Activities for IoT Product Manufacturers](https://csrc.nist.gov/pubs/ir/8259/r1/final)
- [NIST, Foundational Cyber Activities for IoT Product Manufacturers](https://csrc.nist.gov/News/2026/foundational-cyber-activities-for-iot-prod-mfrs)

[^source]: [NIST IR 8259 Revision 1](https://csrc.nist.gov/pubs/ir/8259/r1/final)

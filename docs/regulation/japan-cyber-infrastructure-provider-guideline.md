---
title: サイバーインフラ事業者ガイドライン ― Software Securityを「Vendor責任＋Customer責任」で設計する
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-03
description: 経済産業省と国家サイバー統括室が2026年3月31日に策定したサイバーインフラ事業者向けガイドラインを基に、Software SupplierとCustomerの責務、調達、評価Checklistの意味を整理する。
category: Regulation / Software Supply Chain
collections:
- regulation
- risk-management
- cybersecurity
topics:
- Software Supply Chain
- Third-party Risk / C-SCRM
- Regulation & Policy
tags:
- METI
- NCO
- Cyber Infrastructure Provider
- Software Supply Chain
- Shared Responsibility
- Procurement
- Evaluation Checklist
audience:
- Executive
- CISO
- Procurement
- Product Security
management_impact: High
impact_types:
- Supply Chain
- Product Security
- Procurement
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# サイバーインフラ事業者ガイドライン ― Software Securityを「Vendor責任＋Customer責任」で設計する

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">March 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Regulation / Software Supply Chain</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Software Supply Chain / Third-party Risk / C-SCRM / Regulation &amp; Policy</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Procurement / Product Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Supply Chain / Product Security / Procurement</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

経済産業省と国家サイバー統括室は2026年3月31日、Softwareの開発・供給・運用を行う「サイバーインフラ事業者」とそのCustomerに求められる役割を整理したGuidelineを策定しました。[^source]

重要なのはSoftware Vendorだけへ責任を押し付けるのではなく、**ProviderとCustomerが互いの責務を認識し、調達・運用・評価を通じてSoftware Supply Chain全体のResilienceを高める**考え方です。

</div>

## なぜ今なのか

Modern SoftwareはCloud、Open Source、Managed Service、Library、Update Service等の多層Supply Chainで構成されます。Security Responsibilityが曖昧だと、Incident時にPatch、Notification、SupportのGapが発生します。

## Guidelineの実務的な意味

- Provider / Customer双方の責務を整理
- 6 Categoryで具体的取組を提示
- Evaluation Checklistを用意
- Provider自身のSupply Chainも評価対象
- CustomerのProcurement Risk Managementへ利用可能
- Security ResilienceをSoftware Lifecycleで評価

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Contract | Security Responsibilityを契約前に明確化する必要 |
| Procurement | Product FunctionだけでなくVendor Security Capabilityを評価 |
| Incident | Notification / Patch / Support責任を事前定義 |
| C-SCRM | Direct VendorだけでなくDownstream Dependencyまで視野に入れる |

## 日本企業への示唆

Software調達時に「Security機能があるか」だけでなく、VendorのSecure Development、Vulnerability Handling、Update、Support、Supply Chain管理を確認する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Guideline Checklistと既存Vendor AssessmentをMappingする
2. Software契約のSecurity Responsibilityを確認する
3. Vulnerability Notification SLAを定義する
4. Support / EOL / Update責任を確認する
5. Critical Software VendorをTieringする
6. VendorのThird-party Dependency管理をDue Diligenceへ追加する

</div>

## 用語解説

**サイバーインフラ事業者**  
Softwareを開発・供給・運用し、社会や企業のDigital Infrastructureを支える事業者を広く捉えた概念。

## 関連記事

- [NIST IR 8259r1](../risk-management/nist-iot-product-lifecycle-ir8259r1.md)
- [SCS評価制度「制度構築方針」](japan-scs-policy-march-2026.md)

## 参考情報

- [経済産業省, サイバーインフラ事業者に求められる役割等に関するガイドライン](https://www.meti.go.jp/press/2025/03/20260331001/20260331001.html)
- [国家サイバー統括室, ガイドライン資料](https://www.cyber.go.jp/council/cs/ciip/yakuwari/index.html)

[^source]: [経済産業省, サイバーインフラ事業者ガイドライン](https://www.meti.go.jp/press/2025/03/20260331001/20260331001.html)

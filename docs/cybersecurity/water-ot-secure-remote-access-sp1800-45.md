---
title: NIST SP 1800-45 ― OT Remote Accessを「例外VPN」からReference Architectureへ
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-06
description: 2026年6月にNIST NCCoEが最終公開したWater and Wastewater Sector向けSP 1800-45を基に、重要インフラの安全なOT
  Remote Accessを整理する。
category: Cybersecurity / Critical Infrastructure
collections:
- cybersecurity
- risk-management
tags:
- NIST
- OT Security
- Remote Access
- Critical Infrastructure
- Water
audience:
- Executive
- CISO
- OT Security
- Infrastructure
management_impact: High
impact_types:
- Business Continuity
- OT / Safety
- Identity
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# NIST SP 1800-45 ― OT Remote Accessを「例外VPN」からReference Architectureへ

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">June 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / Critical Infrastructure</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / OT Security / Infrastructure</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Business Continuity / OT / Safety / Identity</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NIST NCCoEは2026年6月24日、SP 1800-45「Cybersecurity for the Water and Wastewater Sector: Build Architecture」を最終公開しました。水道・下水Sectorを対象に、商用Technologyを用いた複数のSecure Remote Access Reference DesignをLabで構築・実証しています。[^source]

重要なのは水道業界固有の話に閉じず、**OT Remote AccessをVendor作業の例外経路ではなく、Authentication・Authorization・Monitoringを備えた正式Architectureとして設計する**ことです。

</div>

## なぜ今なのか

設備VendorのRemote Maintenanceは事業継続に有効ですが、常設VPN、Shared Account、Flat Network、監視不足が残ると重要Infrastructureへの強力な侵入経路になります。Digital TransformationでInternet-connected SensorやAnalyticsが増えるほどBoundaryも複雑になります。

## 何が起きているのか

SP 1800-45はSmallからLarge Utilityを想定したReference Designを示し、Remote AccessをOperational Needに応じて安全に実装する具体例を提供しています。Controlの中心はAccess Authorization、Authentication、Secure Communication、Monitoringであり、「VPNを使う」だけではありません。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Third-party Access | Vendor Account / Remote Maintenanceを正式なIdentity Control対象にする |
| OT Segmentation | Remote Accessの到達範囲を限定する |
| Monitoring | 誰がいつ何へ接続したか追跡できる必要 |
| Availability | 緊急保守を阻害せずSecurityを成立させる設計が必要 |

## 日本企業への示唆

日本の製造・重要インフラでも、Vendor Remote Accessを契約・現場運用・Network設計の3者で統合管理することが重要です。PAM、MFA、Jump Host、Session Recording、Time-bound Accessなどを、現場の保守要件に合わせて組み合わせるべきです。

<div class="sil-action-box" markdown>

## 推奨アクション

1. OT Remote Access経路を全て棚卸しする
2. Shared Accountを個別Identityへ移行する
3. MFA / PAM / Time-bound Accessを適用する
4. Vendorごとに到達可能Assetを限定する
5. Session Logging / Recordingを実装する
6. 緊急保守時のBreak-glass手順を演習する

</div>

## 用語解説

**Remote Access Architecture**  
外部・遠隔利用者がOTへ接続するためのIdentity、Network、Control Point、Monitoringを含む設計。

**Jump Host**  
管理対象Systemへの接続を中継し、Access Controlと監査を集中させるHost。

## 関連記事

- [NIST SP 1339 OT Backup](nist-ot-backup-sp1339.md)
- [重要インフラの統一基準](../regulation/japan-critical-infrastructure-unified-standard.md)

## 参考情報

- [NIST SP 1800-45, Cybersecurity for the Water and Wastewater Sector](https://csrc.nist.gov/News/2026/cyber-for-water-wastewater-sector)

[^source]: [NIST SP 1800-45, Cybersecurity for the Water and Wastewater Sector](https://csrc.nist.gov/News/2026/cyber-for-water-wastewater-sector)

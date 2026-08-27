---
title: NIST SP 800-133r3 Draft ― PQC移行はAlgorithmだけでなくKey Generation / HSMまで変える
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-04
description: NISTが2026年4月17日に公開したSP 800-133 Revision 3 Draftを基に、PQC、KEM、Seed Expansion、Hybrid
  ImplementationがKey Management基盤へ与える影響を整理する。
category: Identity Security / Cryptography
collections:
- identity-security
- risk-management
topics:
- PQC / Crypto Agility
- Identity Security
tags:
- NIST
- SP 800-133r3
- PQC
- ML-KEM
- HSM
- Key Generation
- Hybrid Cryptography
- Crypto Agility
audience:
- CISO
- IAM
- PKI
- Cryptography
management_impact: High
impact_types:
- Cryptography
- Identity
- Technology Lifecycle
urgency: Strategic
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# NIST SP 800-133r3 Draft ― PQC移行はAlgorithmだけでなくKey Generation / HSMまで変える

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">April 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / Cryptography</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">PQC / Crypto Agility / Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">CISO / IAM / PKI / Cryptography</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Cryptography / Identity / Technology Lifecycle</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NISTは2026年4月17日、SP 800-133 Revision 3「Recommendation for Cryptographic Key Generation」のInitial Public Draftを公開しました。Revision 3では、Key Encapsulation Mechanism（KEM）、PQC Signature、Seed Expansion、Hybrid Classical/PQC Implementation等が追加され、PQCをKey Generationの運用レベルへ統合する方向が明確になっています。[^source]

PQC MigrationはAlgorithm名を置き換えるだけではありません。Key Seedをどう保管するか、HSMが新しいKey形式をどう扱うか、ClassicalとPQCをHybrid運用するかなど、**Key Management Infrastructureそのものの更新**が必要になります。

</div>

## なぜ今なのか

Cryptographic MigrationではApplication、Protocol、Certificate、HSM、Key Ceremony、Backup等が複雑に依存しています。

NISTがHSM DesignやML-KEM Seed Storage、Hybrid Implementationについて明示的にFeedbackを求めていることは、PQCが研究段階からOperational Designへ進んでいることを示します。

## 主な変更点

- Asymmetric Key Pair Generationの拡張
- Seed Expansionの利用方法
- KEMをSymmetric Key Establishment Optionとして整理
- PQC Signatureへの参照追加
- Random Number GenerationをSP 800-90Cと整合
- HSM / Seed Storage / Hybrid Implementationの実務論点提示

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| HSM | Firmware / HardwareのPQC対応状況がMigration速度を左右 |
| PKI | CertificateだけでなくKey Lifecycle全体を見直す必要 |
| Procurement | Crypto Agilityを製品選定条件にする必要 |
| Long-lived Data | 長期機密性が必要なDataは早期Migration検討が必要 |

## 日本企業への示唆

PQC Projectを「将来Algorithmを切り替える」といった単純な計画にせず、Cryptographic InventoryからHSM、Key Generation、Certificate、Protocol、Vendor Supportを関連付けて管理する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Cryptographic Inventoryを作成する
2. HSM / KMS / PKIのPQC RoadmapをVendorへ確認する
3. ML-KEM / ML-DSA等のKey Materialの扱いを検証する
4. Hybrid Cryptographyを使うSystem候補を整理する
5. Key Backup / Recovery / Rotation Processへの影響を確認する
6. Crypto AgilityをArchitecture Requirementへ追加する

</div>

## 用語解説

**Seed Expansion**  
短いSeedからAlgorithmで必要なKey Materialを決定的に展開する方式。PQCではKey SizeやStorage Designに関連する重要な論点になる。

## 関連記事

- [NIST PIVのPQC対応](pqc-piv-dual-stack.md)

## 参考情報

- [NIST SP 800-133 Revision 3 Initial Public Draft](https://csrc.nist.gov/pubs/sp/800/133/r3/ipd)
- [NIST, Recommendation for Cryptographic Key Generation](https://csrc.nist.gov/news/2026/recommendation-for-cryptographic-key-generation)

[^source]: [NIST SP 800-133 Revision 3 Initial Public Draft](https://csrc.nist.gov/pubs/sp/800/133/r3/ipd)

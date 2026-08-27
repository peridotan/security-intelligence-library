---
title: IT製品調達セキュリティ要件リスト第2.1版 ― ProcurementをSecurity Controlとして使う
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-02
description: 2026年2月6日に更新されたIT製品の調達におけるセキュリティ要件リスト第2.1版とIPAガイドブックを基に、調達段階でSecurity
  Requirementを定義する意味を整理する。
category: Regulation / Procurement Security
collections:
- regulation
- risk-management
topics:
- Third-party Risk / C-SCRM
- Regulation & Policy
- Security Governance & Risk Management
tags:
- IPA
- METI
- IT Procurement
- Security Requirements
- Product Security
- Government Procurement
- JISEC
audience:
- Executive
- CISO
- Procurement
- Architecture
management_impact: High
impact_types:
- Procurement
- Product Security
- Supply Chain
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# IT製品調達セキュリティ要件リスト第2.1版 ― ProcurementをSecurity Controlとして使う

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">February 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Regulation / Procurement Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Third-party Risk / C-SCRM / Regulation &amp; Policy / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Procurement / Architecture</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Procurement / Product Security / Supply Chain</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

2026年2月6日、経済産業省は「IT製品の調達におけるセキュリティ要件リスト」第2.1版を公開し、IPAも活用Guidebook第2.1版を公開しました。[^source]

このListは政府機関等の調達で参照されるSecurity Requirementを整理するもので、第2.1版では従来11製品分野の要件が更新されています。

企業にとって重要なのは、**Securityを導入後の設定問題だけでなく、製品選定・契約前に要求すべき品質として扱う**考え方です。

</div>

## なぜ今なのか

導入後に「Logが取れない」「Patch Supportが短い」「Strong Authenticationに対応しない」と判明しても、Architectureを変えるCostは高くなります。Security RequirementはProcurement段階で入れる方が効率的です。

## Procurementで見るべき観点

- Authentication / Access Control
- Logging / Audit
- Secure Update
- Vulnerability Handling
- Cryptographic Function
- Management Interface
- Security Certification / Evidence
- Support / Lifecycle

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Procurement | Price / FunctionだけでなくSecurity Requirementを評価 |
| Architecture | 後付けControl Costを下げる |
| Vendor Risk | Product Security Evidenceを契約前に確認 |
| Lifecycle | Support / Update条件をTotal Costへ反映 |

## 日本企業への示唆

政府調達向けListをそのまま適用する必要はありませんが、自社RFP / RFIのSecurity Requirementを作るReferenceとして有用です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Critical Product向けSecurity Requirement Templateを作る
2. RFPへLogging / MFA / Update / Vulnerability要件を入れる
3. Vendor Evidenceの提出条件を決める
4. ExceptionをRisk Acceptance Processへ接続する
5. Support / EOLをCommercial条件と同時に評価する
6. Procurement / Security / Architectureで共同Reviewする

</div>

## 用語解説

**Security by Procurement**  
Security Requirementを製品・Serviceの購入前に明示し、Vendor選定・契約条件を通じてRiskを低減する考え方。

## 関連記事

- [サイバーインフラ事業者ガイドライン](japan-cyber-infrastructure-provider-guideline.md)
- [SCS評価制度](../risk-management/japan-scs-evaluation-operationalization.md)

## 参考情報

- [IPA, IT製品の調達におけるセキュリティ要件リスト](https://www.ipa.go.jp/security/it-product/index.html)

[^source]: [IPA, IT製品の調達におけるセキュリティ要件リスト 第2.1版](https://www.ipa.go.jp/security/it-product/index.html)

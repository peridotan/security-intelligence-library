---
title: NIST SP 1326 ― Supply Chain Securityを「契約後の監査」から「契約前のDue Diligence」へ
date: 2026-08-26
updated: 2026-08-26
description: NISTが2026年7月に最終版を公開したC-SCRM Due Diligence Assessment Quick-Start Guide
  SP 1326を企業調達・Vendor Risk Managementの観点から整理する。
category: Management View / Supply Chain
tags:
- NIST
- C-SCRM
- Supply Chain
- Third-party Risk
audience:
- Executive
- CISO
- Procurement
- Risk Management
management_impact: High
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
source_period: 2026-07
---

# NIST SP 1326 ― Supply Chain Securityを「契約後の監査」から「契約前のDue Diligence」へ

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Management View / Supply Chain</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Procurement / Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NISTは2026年7月8日、Cybersecurity Supply Chain Risk Management（C-SCRM）のDue Diligence Assessment Quick-Start GuideであるSP 1326を最終公開しました。NISTは、SupplierやProductについて利用可能な情報を調査し、調達前または既存利用中のRisk判断に必要な最低限のInvestigative Rigorを実装しやすい形で提示しています。[^source]

重要な変化は、Vendor Securityを「契約後にQuestionnaireを送る活動」から、**契約・更新・重大変更の前にRiskを調べる意思決定Process**へ移すことです。

</div>

## なぜ今なのか

Cloud、SaaS、OSS、Managed Service、AI Serviceの利用拡大により、企業は自社ControlだけではRiskを閉じられません。

一方、全Supplierへ大規模Assessmentを実施するのは現実的ではありません。SP 1326は「最低限どこまで調べれば合理的な判断ができるか」というQuick-Startの考え方を提供します。

## Due Diligenceで見るべきもの

組織の具体的なProcessはRiskに応じて変わりますが、実務上は以下の情報を組み合わせます。

- SupplierのOwnership / Business Stability
- Security Incident / Breach History
- Product Security Practice
- Vulnerability Disclosure / Patch Practice
- Software / Hardware Supply Chain
- Dependency / Subcontractor
- Compliance / Certification
- Data / Service Concentration
- Exit / Replacement Feasibility

ポイントは、チェック項目を埋めることではなく、**調達判断・例外承認・Risk Acceptanceへ接続すること**です。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Procurement | Security Reviewを調達前のGateへ組み込む |
| Concentration | 重要Supplierへの依存を経営Riskとして可視化 |
| Contract | Security RequirementとEvidence要求を契約へ反映 |
| Accountability | 誰が残余Riskを受容したか記録できる |

## 日本企業への示唆

日本企業では、購買、法務、IT、Security、事業部が別々にSupplierを評価することがあります。C-SCRMではこれらを一つのDecision Processへまとめることが重要です。

国内のSCS評価制度等の第三者評価をEvidenceとして活用しつつ、自社固有のData、Service Criticality、Concentration Riskは別途判断する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. SupplierをCriticalityでTieringする
2. 契約前Due Diligenceの最低項目を定義する
3. 外部RatingやCertificationだけで判断しない
4. Incident / Vulnerability / Ownership変更を継続監視する
5. Renewal時にRiskを再評価する
6. Exception / Risk Acceptanceを経営判断として記録する

</div>

## 用語解説

**C-SCRM**  
Cybersecurity Supply Chain Risk Management。Supplier、Product、Service、Dependencyを通じて発生するCyber RiskをLifecycle全体で管理する考え方。

**Due Diligence**  
意思決定前に、相手方・対象製品について合理的な調査を行うこと。

## 関連記事

- [Management View](index.md)
- [重要インフラのサイバーセキュリティが「統一基準」へ](../regulation/japan-critical-infrastructure-unified-standard.md)

## 参考情報

- [NIST SP 1326, Cybersecurity Supply Chain Risk Management: Due Diligence Assessment Quick-Start Guide](https://csrc.nist.gov/pubs/sp/1326/final)
- [NIST C-SCRM Publications](https://csrc.nist.gov/Projects/cyber-supply-chain-risk-management/publications)

[^source]: [NIST SP 1326](https://csrc.nist.gov/pubs/sp/1326/final)

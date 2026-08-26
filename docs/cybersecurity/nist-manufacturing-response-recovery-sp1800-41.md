---
title: NIST SP 1800-41 Draft ― OTでは「防ぐ」だけでなくResponse / Recoveryを設計する
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-05
description: NIST NCCoEが2026年5月21日に公開した製造業向けResponse / Recovery Guide SP 1800-41 Draftを基に、ICS/OTでの復旧設計とOperational
  Resilienceを整理する。
category: Cybersecurity / OT
collections:
- cybersecurity
- risk-management
topics:
- OT / Critical Infrastructure
- Ransomware & Resilience
tags:
- NIST
- SP 1800-41
- Manufacturing
- ICS
- Incident Response
- Recovery
- Operational Resilience
audience:
- Executive
- CISO
- OT Security
- Manufacturing
management_impact: High
impact_types:
- Business Continuity
- OT / Safety
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# NIST SP 1800-41 Draft ― OTでは「防ぐ」だけでなくResponse / Recoveryを設計する

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">May 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / OT</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">OT / Critical Infrastructure / Ransomware &amp; Resilience</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / OT Security / Manufacturing</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Business Continuity / OT / Safety</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NIST NCCoEは2026年5月21日、製造業のICS / OT環境におけるCyber IncidentへのResponseとRecoveryを扱うSP 1800-41 Initial Public Draftを公開しました。11のIndustry CollaboratorとReference ArchitectureやAttack Scenarioを構築し、Cyber Attack後にOperationsを安全に復旧するための実践的な方法を示しています。[^source]

重要なのは、Defense-in-depthでもCyber Riskをゼロにはできないと明示し、**「侵入を防ぐ」Controlと同じレベルで、Response・Restore・Operational Recoveryを設計する**ことです。

</div>

## なぜ今なのか

OT / ICSではSystem停止がProduction、Safety、Quality、Supply Chainへ直接影響します。一方、Patchや復旧をITと同じ手順で行えない設備も多くあります。

そのためIncident Response Planは、Forensicsだけでなく「どの順で設備を戻すか」「安全確認をどう行うか」「代替運転が可能か」を含む必要があります。

## 実務上の論点

- Cyber IncidentがPhysical Processへ与えるImpactの把握
- IT / OT間のIncident Coordination
- Known-good Configuration / Backupの確保
- Restoration順序とDependencyの把握
- Recovery時のSafety Validation
- Vendor / Integratorを含むResponse Exercise

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Production | Recovery時間が直接売上・Supply Chainへ影響 |
| Safety | 復旧を急ぐこと自体がPhysical Safety Riskになり得る |
| Vendor | Equipment Vendor / Integratorの支援可否がRecoveryを左右 |
| BCP | IT Disaster RecoveryだけではOT復旧をカバーできない |

## 日本企業への示唆

製造現場のBackupを「取っている」だけで安心せず、実際にPLC / HMI / Engineering Station / Historian等をどの順序で戻せるかを確認する必要があります。Cyber Exerciseへ工場運用・設備保全・Safety担当を含めることが重要です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Critical OT AssetとDependencyを可視化する
2. Known-good Backup / ConfigurationのRestore Testを行う
3. IT / OT共同Incident Response Planを作る
4. Recovery順序とSafety Checkpointを定義する
5. Vendor / Integratorを含めた復旧Exerciseを実施する
6. RTOだけでなくManual Operation / Production Lossも評価する

</div>

## 用語解説

**Operational Resilience**  
Cyber Incidentや障害が起きても、重要なBusiness / Physical Operationを継続または許容時間内に復旧できる能力。

## 関連記事

- [NIST OT Backup SP 1339](nist-ot-backup-sp1339.md)
- [Water OT Secure Remote Access](water-ot-secure-remote-access-sp1800-45.md)

## 参考情報

- [NIST SP 1800-41 Initial Public Draft](https://csrc.nist.gov/pubs/sp/1800/41/ipd)
- [NIST, SP 1800-41 Released for Public Comment](https://csrc.nist.gov/News/2026/nist-sp-1800-41-released-for-public-comment)

[^source]: [NIST SP 1800-41 Initial Public Draft](https://csrc.nist.gov/pubs/sp/1800/41/ipd)

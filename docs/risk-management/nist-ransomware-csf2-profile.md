---
title: NIST IR 8374r1 ― Ransomware対策を「製品導入」からCSF 2.0の経営Riskへ
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-06
description: 2026年6月にNISTが最終公開したIR 8374 Revision 1を基に、Ransomware Risk ManagementをCSF
  2.0のGovern・Identify・Protect・Detect・Respond・Recoverで整理する。
category: Management View / Ransomware
collections:
- risk-management
- cybersecurity
topics:
- Ransomware & Resilience
- Security Governance & Risk Management
tags:
- NIST
- Ransomware
- CSF 2.0
- Resilience
- Risk Management
audience:
- Executive
- CISO
- Risk Management
- BCP
management_impact: High
impact_types:
- Business Continuity
- Governance
- Operational Security
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---
# NIST IR 8374r1 ― Ransomware対策を「製品導入」からCSF 2.0の経営Riskへ

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">June 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Management View / Ransomware</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Ransomware &amp; Resilience / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Risk Management / BCP</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Business Continuity / Governance / Operational Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NISTは2026年6月11日、IR 8374 Revision 1「Ransomware Risk Management: A Cybersecurity Framework 2.0 Community Profile」を最終公開しました。旧版をCSF 1.1からCSF 2.0へ更新し、RansomwareをGovern、Identify、Protect、Detect、Respond、Recoverの全Functionで管理する実務Profileです。[^source]

これは「Backup製品を入れる」「EDRを導入する」といった個別Controlではなく、**Risk Appetite、Owner、Asset、Detection、Incident Response、Recoveryまでを一つの経営Riskとしてつなぐ**ための枠組みです。

</div>

## なぜ今なのか

Ransomwareは暗号化だけでなくData Theft、Extortion、Service Disruptionを伴うため、単一製品ではRiskを閉じられません。CSF 2.0でGovernが追加されたことで、経営責任、Risk Decision、Third-party、Policyを含む上流管理が明確になっています。

## 何が起きているのか

IR 8374r1は、Ransomware ReadinessをCSF 2.0のOutcomeへMappingし、組織の現在地とPriority Actionを評価できるCommunity Profileです。Playbookや成熟度評価を既存CSF 2.0 Programへ統合しやすくなっています。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Governance | Ransomware RiskをCISOだけでなく経営Riskとして扱う |
| Resilience | Backupの有無ではなくRecovery Timeと復旧演習を重視 |
| Data Extortion | 暗号化されなくてもData Theftで重大Incidentになり得る |
| Third-party | Supplier / Managed Service経由のRiskもProfileへ組み込む |

## 日本企業への示唆

日本企業ではRansomware対策チェックリストが製品導入状況の確認に寄りがちです。CSF 2.0 Profileを使い、Business Service単位で「どこまで止まるか」「誰がRiskを受容するか」「復旧に何時間かかるか」まで確認すると経営会議へつなげやすくなります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. IR 8374r1を既存Ransomware AssessmentへMappingする
2. Critical Business Service単位でRecovery Objectiveを設定する
3. Backup Restoreを定期演習する
4. Data Theft / ExtortionをIncident Scenarioへ追加する
5. Supplier経由のRansomware Scenarioを評価する
6. 残余Riskと追加投資を経営判断として記録する

</div>

## 用語解説

**CSF 2.0 Community Profile**  
特定SectorやRiskに対してNIST CSF 2.0 Outcomeを具体化したProfile。

**Ransomware Resilience**  
侵入防止だけでなく業務継続・復旧・Data Extortion対応まで含む耐性。

## 関連記事

- [脆弱性悪用の猶予は48時間以下へ](../cybersecurity/exploitation-window-48-hours.md)
- [Management View](index.md)

## 参考情報

- [NIST IR 8374r1, Ransomware Risk Management: A Cybersecurity Framework 2.0 Community Profile](https://csrc.nist.gov/News/2026/ransomware-risk-management-ir-8374r1)

[^source]: [NIST IR 8374r1, Ransomware Risk Management: A Cybersecurity Framework 2.0 Community Profile](https://csrc.nist.gov/News/2026/ransomware-risk-management-ir-8374r1)

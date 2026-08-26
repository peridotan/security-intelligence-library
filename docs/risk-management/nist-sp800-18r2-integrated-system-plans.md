---
title: NIST SP 800-18r2 ― Security・Privacy・C-SCRMを別々の計画書にしない
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-06
description: 2026年6月にNISTが最終公開したSP 800-18 Revision 2を基に、System Security Plan、Privacy
  Plan、C-SCRM Planを統合的に管理する意味を整理する。
category: Management View / Governance
collections:
- risk-management
- regulation
topics:
- Security Governance & Risk Management
- Third-party Risk / C-SCRM
tags:
- NIST
- Risk Management
- Privacy
- C-SCRM
- Security Planning
audience:
- Executive
- CISO
- Risk Management
- Privacy
- Procurement
management_impact: High
impact_types:
- Governance
- Regulatory
- Supply Chain
urgency: Strategic
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---
# NIST SP 800-18r2 ― Security・Privacy・C-SCRMを別々の計画書にしない

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">June 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Management View / Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Security Governance &amp; Risk Management / Third-party Risk / C-SCRM</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Risk Management / Privacy / Procurement</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Governance / Regulatory / Supply Chain</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NISTは2026年6月30日、SP 800-18 Revision 2「Developing Security, Privacy, and Cybersecurity Supply Chain Risk Management Plans for Systems」を最終公開しました。約20年ぶりのRevisionで、System Security Plan、System Privacy Plan、C-SCRM Planを相互に関連する「System Plans」として整理します。[^source]

ポイントは文書を増やすことではなく、**Asset、Data Flow、Control、Owner、Risk DecisionをSecurity・Privacy・Supply Chainで共有し、一つのSystem Boundaryを同じ情報から管理する**ことです。

</div>

## なぜ今なのか

Security、Privacy、Procurementが別々に同じSystemを評価すると、Asset、Data、Supplier、Ownerの情報が不一致になり、Control gapや重複作業が生まれます。Cloud / SaaS / AI Serviceの利用拡大で、System Boundaryは自社内だけでは閉じなくなっています。

## 何が起きているのか

SP 800-18r2は3種類のSystem Planに必要なEssential Elementを整理し、NIST RMFのStep / Taskと関連付けます。Systemが扱うData、Responsible Person、Environment、Component、Internal/External Data Flow、Planned/In-place ControlをCentral Referenceとして維持する考え方です。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Governance | Security / Privacy / C-SCRMの責任分界と共通情報を明確化 |
| Evidence | 監査・認可・Risk Reviewで同じ情報を再利用できる |
| Third-party | Supplier / External ServiceをSystem Boundary内のRiskとして扱う |
| AI / Cloud | Data FlowとExternal Dependencyが多いSystemほど効果が大きい |

## 日本企業への示唆

日本企業でもISMS、Privacy、委託先管理、Cloud審査、AI審査が別Formで実施されることがあります。共通のSystem / Service Recordを作り、その上に各専門Controlを重ねる方式へ変えると、利用部門の審査負荷と管理部門の情報不整合を減らせます。

<div class="sil-action-box" markdown>

## 推奨アクション

1. System / Service単位の共通Recordを定義する
2. Asset / Data Flow / Owner / Supplier情報を一元化する
3. Security / Privacy / C-SCRMのControl Mappingを作る
4. System変更時に3領域を同時更新する
5. Risk Acceptanceを一つのDecision Logへ集約する
6. AI / SaaS Reviewにも同じSystem Planを再利用する

</div>

## 用語解説

**System Plan**  
Systemの目的、Boundary、Control、責任、Risk Decision等を記録する計画・管理情報。

**C-SCRM**  
Cybersecurity Supply Chain Risk Management。SupplierやService Dependencyを通じたCyber Riskの管理。

## 関連記事

- [C-SCRM Due Diligence](c-scrm-due-diligence-sp1326.md)
- [生成AI利活用ガバナンス](../ai-security/generative-ai-governance.md)

## 参考情報

- [NIST SP 800-18 Rev. 2](https://csrc.nist.gov/pubs/sp/800/18/r2/final)

[^source]: [NIST SP 800-18 Rev. 2](https://csrc.nist.gov/pubs/sp/800/18/r2/final)

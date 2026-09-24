---
title: EU CRA Reporting Goes Live ― 脆弱性・重大Incident報告が24h / 72h運用へ
date: 2026-09-24
updated: 2026-09-24
reviewed: 2026-09-24
review_status: Current
source_period: 2026-09
description: EU Cyber Resilience ActのReporting Obligationが2026年9月11日に適用開始され、Actively
  Exploited VulnerabilityとSevere Incidentについて24時間Early Warning、72時間Full Notificationが必要になった点を整理する。
category: Regulation
collections:
- regulation
- cybersecurity
- risk-management
topics:
- Regulation & Policy
- Vulnerability Management
- Security Governance & Risk Management
tags:
- EU
- Cyber Resilience Act
- CRA
- ENISA
- Single Reporting Platform
- Vulnerability Reporting
- Incident Reporting
- Product Security
- PSIRT
audience:
- Executive
- CISO
- Legal
- PSIRT
management_impact: High
impact_types:
- Regulatory
- Product Security
- Incident Response
urgency: Immediate
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# EU CRA Reporting Goes Live ― 脆弱性・重大Incident報告が24h / 72h運用へ

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-09-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">September 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-09-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-09-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Regulation</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Regulation &amp; Policy / Vulnerability Management / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Legal / PSIRT</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Regulatory / Product Security / Incident Response</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

2026年9月11日、EU Cyber Resilience Act（CRA）のReporting Obligationが適用開始されました。Manufacturerは、Product with Digital Elementsに影響する**Actively Exploited Vulnerability**と**Severe Incident**を報告する必要があります。[^commission]

基本Timelineは、認知から**24時間以内のEarly Warning**、**72時間以内のFull Notification**です。Actively Exploited VulnerabilityはCorrective Measureが利用可能になってから14日以内、Severe Incidentは72時間Notificationから1か月以内にFinal Reportが必要です。

同日、ENISAのCRA Single Reporting Platform（SRP）が稼働し、Manufacturerは原則として一度のSubmissionで関係当局へ通知できる運用になりました。[^enisa]

CRAは「2027年の製品Security要件」だけではありません。**Reporting Obligationはすでに2026年9月から実運用に入っています。**

</div>

## なぜ今なのか

CRAの主要なCybersecurity Requirementは2027年12月11日から適用されますが、Vulnerability / Incident Reportingはそれより先に始まりました。

これにより、EU市場へDigital Productを提供する企業では、PSIRT / CSIRTが技術的に問題を把握した瞬間から、Legal、Product Owner、Managementを含むReporting Clockを動かす必要があります。

## Reporting Timeline

<div class="sil-flow" role="group" aria-label="CRA reporting timeline">
  <div class="sil-flow-step"><strong>Awareness</strong><span>AEV / Severe Incidentを認知</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Within 24h</strong><span>Early Warning</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Within 72h</strong><span>Full Notification</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step sil-flow-step-impact"><strong>Final Report</strong><span>AEV: Corrective Measure後14日以内 / Severe Incident: 72h通知から1か月以内</span></div>
</div>

## 経営インパクト

| 観点 | 実務への影響 |
| --- | --- |
| Reporting Clock | 技術調査が完了する前から24h / 72hの期限が進む |
| Product Inventory | どのProductがEU市場でCRA対象か把握が必要 |
| PSIRT / CSIRT | VulnerabilityとIncidentをRegulatory Reportingへ接続する |
| Legal | 「報告対象か」の判定を短時間で支援できる体制が必要 |
| Evidence | Awareness時刻、判断、Notification内容、Corrective Measureを記録する |
| Supplier | Third-party Componentの情報が自社Reportingへ波及し得る |

## 日本企業への示唆

EU向けProductを持つ日本企業は、CRA対応をProduct Developmentだけの課題にしないことが重要です。実務上のボトルネックは、**誰がAwareness時刻を確定し、誰がReportabilityを判断し、誰がSRPへSubmissionするか**という組織横断Flowです。

特にSBOM、Vulnerability Management、PSIRT、Incident Response、Legalの情報が分断されている場合、24時間以内のEarly Warningに必要な最低限の情報を揃えられない可能性があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. **CRA対象Product Inventoryを確定する** — EU Market、Product Owner、Manufacturer Roleを紐付ける。
2. **24h / 72h Runbookを作る** — AwarenessからSubmissionまでのOwner、Backup、Escalationを定義する。
3. **AEV / Severe Incident判定を手順化する** — PSIRT、CSIRT、Legalが同じDecision Treeを使う。
4. **SRPの利用準備を確認する** — Account、Contact、代理Submission、休日対応を確認する。
5. **Evidenceを保存する** — Awareness時刻、判断根拠、提出内容、Corrective MeasureをAudit可能にする。
6. **Supplier Notificationと接続する** — Component / SaaS / OSS情報が入った際のCRA影響評価を定める。

</div>

## 用語解説

**Actively Exploited Vulnerability（AEV）**  
CRA上の報告対象となる、悪用が確認されている脆弱性。具体的な法的定義・該当判定はCRA本文およびCommission Guidanceを確認する必要があります。

**Single Reporting Platform（SRP）**  
ENISAが開発・運用するCRA向けの共通Reporting Platform。通知を一度提出し、関係するCSIRT等へ共有する仕組みです。

## 参考情報

- [European Commission, Cyber Resilience Act - Reporting obligations (updated 2026-09-11)](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting)
- [ENISA, The CRA Single Reporting Platform is launched (2026-09-11)](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched)

[^commission]: [European Commission, Cyber Resilience Act - Reporting obligations](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting)
[^enisa]: [ENISA, The CRA Single Reporting Platform is launched (2026-09-11)](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched)

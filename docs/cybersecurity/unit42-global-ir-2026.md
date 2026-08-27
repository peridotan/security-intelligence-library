---
title: Unit 42 Global IR 2026 ― 72分・Identity 90%・SaaS 23%が示す「境界防御の限界」
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-02
description: Palo Alto Networks Unit 42が2026年2月17日に公開したGlobal Incident Response Reportを基に、72分の攻撃速度、Identity、SaaS
  Supply Chain、Multi-surface Attackを整理する。
category: Cybersecurity / Threat Landscape
collections:
- cybersecurity
- identity-security
- risk-management
topics:
- Credential Attacks
- Third-party Risk / C-SCRM
- Security Governance & Risk Management
tags:
- Palo Alto Networks
- Unit 42
- Global Incident Response 2026
- Identity
- SaaS
- Supply Chain
- Attack Speed
- Browser
audience:
- Executive
- CISO
- SOC
- Risk Management
management_impact: High
impact_types:
- Threat Landscape
- Identity
- Supply Chain
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# Unit 42 Global IR 2026 ― 72分・Identity 90%・SaaS 23%が示す「境界防御の限界」

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">February 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / Threat Landscape</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Credential Attacks / Third-party Risk / C-SCRM / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / SOC / Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Threat Landscape / Identity / Supply Chain</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Unit 42は2026年2月17日、750件超のMajor Incidentを分析したGlobal Incident Response Reportを公開しました。最速の事例ではInitial AccessからData Exfiltrationまで**72分**、Identity Weaknessは約90%のInvestigationで重要な役割を持ち、23%のIncidentではThird-party SaaS Applicationが悪用されたと報告しています。[^source]

さらに87%のIntrusionが複数Attack Surfaceにまたがっていました。つまり攻撃はEndpoint、Network、Cloud、SaaS、Identityを横断し、単一ControlだけではContainmentしにくくなっています。

</div>

## なぜ今なのか

Security ProgramがProduct別に分断されていると、攻撃者はControl間のGapを移動します。速度が上がるほど、Team間のTicket RelayやManual InvestigationがBottleneckになります。

## 主要なObservation

| Observation | Unit 42の報告 |
| --- | --- |
| Fastest initial access → exfiltration | 72分 |
| Identity weaknesses | 約90%のInvestigationでMaterial |
| Third-party SaaS abuse | 23%のIncident |
| Multiple attack surfaces | 87%のIntrusion |
| Browser-based activity | 約48%のIncident |

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| SOC | Product別AlertよりCross-surface Correlationが重要 |
| Identity | Credential / TokenをPrimary Attack Vehicleとして扱う |
| SaaS | Trusted IntegrationがSupply Chain Riskになる |
| Response | 72分を前提にDecision / Automationを設計する |

## 日本企業への示唆

SOC、IAM、Network、Cloud、SaaS Teamを分離したままでは、攻撃者の横断速度に追いつきません。High-impact SignalだけでもCross-domainで共有できるDetection / Response Modelが必要です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Identity / Endpoint / SaaS / Network Telemetryを相関する
2. High-confidence Compromiseの自動Containment条件を決める
3. Third-party SaaS IntegrationをInventory化する
4. Browser / Session RiskをSOC Use Caseへ追加する
5. Detection-to-Containment TimeをKPI化する
6. Incident演習を72分Scaleで実施する

</div>

## 用語解説

**Attack Surface Convergence**  
複数のTechnology Domainをまたいで攻撃が連続し、従来別々に管理していたControlが一つのAttack Chainとして狙われる状態。

## 関連記事

- [Large-Scale Credential Attacks](large-scale-credential-attacks.md)
- [M-Trends 2026](m-trends-2026-speed-identity-recovery.md)

## 参考情報

- [Palo Alto Networks, 2026 Unit 42 Global Incident Response Report — Attacks Now 4x Faster](https://www.paloaltonetworks.com/blog/2026/02/unit-42-global-ir-report/)

[^source]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/blog/2026/02/unit-42-global-ir-report/)

---
title: Dell RecoverPoint Zero-day ― 「Recovery製品」自体が長期Persistenceの足場になる
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-02
description: Mandiant / GTIGが2026年2月17日に公表したDell RecoverPoint for Virtual MachinesのCVE-2026-22769悪用を基に、Recovery
  Infrastructure、Default Credential、VMware Pivot、Persistenceを整理する。
category: Cybersecurity / Recovery Infrastructure
collections:
- cybersecurity
- risk-management
topics:
- Ransomware & Resilience
- Vulnerability Management
- Security Governance & Risk Management
tags:
- Dell RecoverPoint
- CVE-2026-22769
- UNC6201
- GRIMBOLT
- BRICKSTORM
- VMware
- Recovery Infrastructure
- Default Credential
audience:
- Executive
- CISO
- Infrastructure
- Incident Response
management_impact: High
impact_types:
- Business Continuity
- Infrastructure
- Vulnerability Risk
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# Dell RecoverPoint Zero-day ― 「Recovery製品」自体が長期Persistenceの足場になる

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">February 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / Recovery Infrastructure</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Ransomware &amp; Resilience / Vulnerability Management / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Infrastructure / Incident Response</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Business Continuity / Infrastructure / Vulnerability Risk</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Mandiant / GTIGは2026年2月17日、Dell RecoverPoint for Virtual MachinesのCVE-2026-22769（CVSS 10.0）がUNC6201によって少なくとも2024年半ばから悪用されていたと報告しました。[^source]

調査では、Appliance内のHard-coded Default Credentialを使ってTomcat ManagerへAuthenticationし、Malicious WARをDeployしてroot権限でCommand Executionできることが判明しました。ActorはBRICKSTORM / GRIMBOLT等をPersistenceに利用し、VMware InfrastructureやSaaSへPivotしています。

重要なのは、**Business Recoveryを支えるInfrastructureそのものがStealthy PersistenceとLateral Movementの足場になった**ことです。

</div>

## なぜ今なのか

Backup / Recovery製品は高い権限と重要Systemへの接続を持つ一方、EDRや通常のEndpoint Monitoringが十分に入らないことがあります。そのため攻撃者にとって価値の高いTrust Planeになります。

## 攻撃Flow

<div class="sil-flow" role="group" aria-label="RecoverPoint compromise flow">
  <div class="sil-flow-step"><strong>RecoverPoint Appliance</strong><span>Hard-coded Default Credential</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Tomcat Manager</strong><span>Malicious WAR Deploy</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Root Command Execution</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>BRICKSTORM / GRIMBOLT Persistence</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step sil-flow-step-impact"><strong>VMware / Internal / SaaS Pivot</strong></div>
</div>

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Recovery | Backup / Recovery製品も攻撃TargetとしてHardeningが必要 |
| Visibility | ApplianceはEDR Coverage外になりやすい |
| Credential | Vendor Default / Embedded CredentialがCritical Riskになる |
| BCP | Recovery Control Plane侵害は復旧能力そのものを損なう |

## 日本企業への示唆

BackupをImmutable化していても、Management / Recovery Applianceが侵害されればOperationを妨害される可能性があります。Recovery InfrastructureをTier-0相当で管理すべきです。

<div class="sil-action-box" markdown>

## 推奨アクション

1. CVE-2026-22769の適用状況を確認する
2. Recovery ApplianceをCritical AssetとしてInventory化する
3. Default / Embedded Credentialを確認する
4. Appliance Web / Auth / Deploy Logを保持する
5. VMware / Backup / Identity間のTrustを最小化する
6. Recovery ExerciseにManagement Plane侵害Scenarioを追加する

</div>

## 用語解説

**Recovery Control Plane**  
Backup、Replication、Virtualization、Restore等を管理し、障害・Incident時の復旧判断や実行を担うManagement Infrastructure。

## 関連記事

- [M-Trends 2026](m-trends-2026-speed-identity-recovery.md)
- [NIST OT Backup SP 1339](nist-ot-backup-sp1339.md)

## 参考情報

- [Google Cloud / Mandiant, UNC6201 Exploiting a Dell RecoverPoint for Virtual Machines Zero-Day](https://cloud.google.com/blog/topics/threat-intelligence/unc6201-exploiting-dell-recoverpoint-zero-day)

[^source]: [Mandiant / GTIG, Dell RecoverPoint Zero-Day](https://cloud.google.com/blog/topics/threat-intelligence/unc6201-exploiting-dell-recoverpoint-zero-day)

---
title: NIST AI 800-4 ― AI Governanceは「導入前審査」よりPost-deployment Monitoringが難しい
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-03
description: NISTが2026年3月9日に公表したDeployed AI SystemsのMonitoring課題を基に、Functionality、Operations、Human
  Factors、Security、Compliance、Large-scale Impactの継続監視を整理する。
category: AI Security / Governance
collections:
- ai-security
- risk-management
topics:
- AI Governance
- Security Governance & Risk Management
tags:
- NIST
- NIST AI 800-4
- Post-deployment Monitoring
- AI Governance
- AI Risk
- Continuous Monitoring
audience:
- Executive
- CISO
- AI Governance
- Risk Management
management_impact: High
impact_types:
- AI Governance
- Compliance
- Operational Risk
urgency: Strategic
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# NIST AI 800-4 ― AI Governanceは「導入前審査」よりPost-deployment Monitoringが難しい

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">March 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Governance / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Governance / Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Compliance / Operational Risk</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NISTは2026年3月9日、Deployed AI SystemsのPost-deployment Monitoringに関する課題を整理したNIST AI 800-4を公表しました。[^source]

AIは導入時の評価だけでは挙動を固定できません。利用者、Data、Environment、Model Update、Attack、社会的影響によってRiskが変化するため、**AI Governanceを継続Monitoringとして運用する必要**があります。

</div>

## なぜ今なのか

企業のAI Governanceは利用申請、禁止事項、Model選定といったPre-deployment Controlから始まりがちです。しかし実運用では、導入後の挙動変化や新しいMisuseを検知しなければGovernanceが形骸化します。

## NISTが整理した6つのMonitoring Category

| Category | 確認する問い |
| --- | --- |
| Functionality | 意図した機能を維持しているか |
| Operational | Infrastructureとして安定して動作しているか |
| Human Factors | Human-AI Interactionが適切か |
| Security | 攻撃・Misuseに対して安全か |
| Compliance | 法令・Standard・Controlへ適合しているか |
| Large-scale Impacts | 広範なDownstream Impactを生んでいないか |

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Governance | 年1回の審査より継続Monitoring Processが重要 |
| Ownership | 誰が何をMonitorし、誰が停止判断するかを明確化する必要 |
| Metrics | AccuracyだけでなくSecurity / Compliance / Human Impactも必要 |
| Incident | AI Incident SharingやEscalation Processが必要 |

## 日本企業への示唆

生成AI利用Guidelineを作った後に、利用状況、Incident、Policy Violation、Data Exposure、Model / Tool変更を観測できる仕組みを追加する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AI System / Agent Inventoryを作成する
2. Monitoring OwnerとEscalation条件を定義する
3. Security / Compliance / Human FactorのMetricを分離する
4. Model / Tool / Data Source変更をChange Managementへ入れる
5. AI Incidentを既存Risk / Incident Processへ統合する
6. 定期ReviewだけでなくEvent-driven Reviewを設計する

</div>

## 用語解説

**Post-deployment Monitoring**  
AI Systemを本番利用した後の挙動、Performance、Security、Compliance、Human Impact等を継続的に観測・評価する活動。

## 関連記事

- [生成AI利活用ガバナンス](generative-ai-governance.md)
- [NISTが示す「AI Securityは一度設定して終わりではない」理由](continuous-ai-security-nist-proof.md)

## 参考情報

- [NIST, Challenges to the Monitoring of Deployed AI Systems](https://www.nist.gov/news-events/news/2026/03/new-report-challenges-monitoring-deployed-ai-systems)

[^source]: [NIST, Challenges to the Monitoring of Deployed AI Systems](https://www.nist.gov/news-events/news/2026/03/new-report-challenges-monitoring-deployed-ai-systems)

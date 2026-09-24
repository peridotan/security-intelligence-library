---
title: Cyber Dependencies Weaken Digital Resilience ― ENISA Threat Landscape 2026
date: 2026-09-24
updated: 2026-09-24
reviewed: 2026-09-24
review_status: Current
source_period: 2026-09
description: ENISAが2026年9月22日に公開したThreat Landscape 2026を基に、2025年観測データからRansomware、DDoS、Vulnerability
  Exploitation、Supply Chain / Third-party Dependency、AIのDual Roleを整理する。
category: Cybersecurity / Threat Landscape
collections:
- cybersecurity
- risk-management
topics:
- Third-party Risk / C-SCRM
- Ransomware & Resilience
- AI-Enabled Threats
tags:
- ENISA
- Threat Landscape
- Cyber Dependency
- Ransomware
- DDoS
- Vulnerability Exploitation
- Supply Chain
- Third-party Risk
- AI-Enabled Threats
audience:
- Executive
- CISO
- Risk Management
- SOC
management_impact: High
impact_types:
- Cyber Resilience
- Third-party
- Threat Landscape
urgency: Strategic
evidence: Assessment
status: published
pptx: ''
media_rights: none
---

# Cyber Dependencies Weaken Digital Resilience ― ENISA Threat Landscape 2026

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-09-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">September 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-09-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-09-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / Threat Landscape</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Third-party Risk / C-SCRM / Ransomware &amp; Resilience / AI-Enabled Threats</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Risk Management / SOC</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Cyber Resilience / Third-party / Threat Landscape</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Assessment</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

ENISAは2026年9月22日、**ENISA Threat Landscape 2026**を公開しました。分析対象は2025年1月1日〜12月31日に観測されたIncident / Eventであり、2026年9月時点のリアルタイムIncident統計ではありません。[^source]

ENISAは、Ransomwareを短期的Impactが最も大きいIncident Typeとし、Public Administrationが最もTargetedなSectorだったと整理しています。また、Cybercrime、State-nexus、HacktivismなどThreat Categoryの境界が曖昧になり、Supply-chain / Third-party Attackを含む**Cyber DependencyがAttack SurfaceとSystemic Impactを拡大する**点を強調しています。

AIについてもDual Roleが示されました。Malicious Operationを支援するToolとしての利用が増える一方、Business環境へAI Systemを統合すること自体が新しいAttack Surfaceを生みます。

</div>

## なぜ今なのか

個別のThreat ActorやMalwareだけを追っても、Business Impactを説明しにくくなっています。Cloud、SaaS、Software Component、Supplier、Identity ProviderなどのDependencyを通じて、一つのIncidentが複数組織へ波及するためです。

ENISA Threat Landscape 2026の価値は、2025年の観測データを使って、**Threatの種類よりも「依存関係を通じてImpactが広がる構造」**を経営Riskへ接続している点にあります。

## 主要Signal

| Signal | ENISAの整理 | Management View |
| --- | --- | --- |
| Ransomware | Short-termで最もImpactが大きいIncident Type | BackupだけでなくBusiness Recoveryを検証する |
| DDoS | 記録Eventの51%を占め、地政学的Eventと連動 | Essential ServiceのAvailability Riskとして扱う |
| Public Administration | Targeted Organizationの32% | 公共・重要ServiceではAvailabilityとDependencyが重要 |
| Vulnerability Exploitation | Intrusion Vectorを特定できたUnauthorized Accessの一部でVulnerability利用が目立つ | KEV / EPSS等でExploit Exposureを短縮する |
| Supply Chain / Third-party | Cyber DependencyがLarge-scale Impactにつながる | Supplier InventoryとConcentration Riskを管理する |
| AI | 攻撃支援と新Attack Surfaceの双方 | AI for Attack / AI as Targetを同時に扱う |

## 経営インパクト

| 観点 | 経営上の意味 |
| --- | --- |
| Dependency | 自社Controlが強くてもProvider / Supplier側Incidentで停止し得る |
| Concentration | 同じCloud / IdP / Softwareへの集中がSystemic Riskになる |
| Resilience | Preventionだけでなく代替手段・Recovery Timeが重要 |
| Threat Convergence | Crime / Hacktivism / State-nexusで共通Techniqueが再利用される |
| Vulnerability | Patch件数よりExploit Exposure Windowの短縮が重要 |
| AI | Security Toolであると同時にAttack Surface / Adversary Toolにもなる |

## 日本企業への示唆

日本企業でも、ENISAのEU向け統計をそのまま国内発生率として読むべきではありません。一方、Cloud / SaaS / Software Supply Chainへの依存、Ransomware、DDoS、Vulnerability Exploitation、AIのDual Roleという構造は、Enterprise RiskのScenarioとして利用できます。

実務ではAsset Inventoryを「自社Asset一覧」で止めず、**Business Service → Critical Dependency → Provider / Software → Recovery Option**までつなぐと、Threat IntelligenceをResilience Planningへ接続しやすくなります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. **Critical Dependency Mapを作る** — Business ServiceからCloud / SaaS / IdP / Supplier / Softwareへ依存関係を追う。
2. **Concentration Riskを確認する** — 単一Provider障害・侵害で止まるServiceを特定する。
3. **Recovery Optionを検証する** — Backupだけでなく代替経路、Manual Operation、Credential Recoveryを演習する。
4. **Exploit Exposure Windowを管理する** — KEV / EPSS / Asset Contextで優先度と残存時間を見る。
5. **DDoS ScenarioをAvailability Riskへ接続する** — Internet-facing / Essential ServiceのCapacityとFailoverを確認する。
6. **AIのDual RoleをRisk Registerへ入れる** — AI-assisted AttackとAI System自体のSecurityを分離せず扱う。

</div>

## 用語解説

**Cyber Dependency**  
Cloud、SaaS、Software、Supplier、Network、Identity Service等、Digital Serviceを成立させる外部・内部依存関係。本記事ではDependencyを通じてIncident Impactが連鎖するRiskを指します。

**Threat Landscape**  
一定期間のIncident、Threat Actor、Technique、Target Sector等を分析し、Threat環境の傾向や構造を整理したもの。

## 参考情報

- [ENISA, ENISA Threat Landscape 2026 (2026-09-22)](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026)
- [ENISA, Exploring the evolution of the cyber threat landscape: How dependencies weaken our digital resilience (2026-09-22)](https://www.enisa.europa.eu/news/exploring-the-evolution-of-the-cyber-threat-landscape-how-dependencies-weaken-our-digital-resilience)

[^source]: [ENISA, ENISA Threat Landscape 2026 (2026-09-22)](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026)

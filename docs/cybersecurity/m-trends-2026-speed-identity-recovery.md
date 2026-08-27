---
title: M-Trends 2026 ― 攻撃の「22秒化」とRecovery Denialが示す次の防御モデル
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-03
description: Mandiantが2026年3月23日に公表したM-Trends 2026を基に、Access Hand-offの高速化、Voice Phishing、SaaS
  Identity、Recovery Denial、Edge Persistenceを経営Riskとして整理する。
category: Cybersecurity / Threat Landscape
collections:
- cybersecurity
- risk-management
- identity-security
topics:
- Credential Attacks
- Ransomware & Resilience
- Security Governance & Risk Management
tags:
- Mandiant
- M-Trends 2026
- Voice Phishing
- Recovery Denial
- Edge Device
- SaaS Identity
- Ransomware
- Initial Access
audience:
- Executive
- CISO
- SOC
- Risk Management
management_impact: High
impact_types:
- Threat Landscape
- Identity
- Business Continuity
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# M-Trends 2026 ― 攻撃の「22秒化」とRecovery Denialが示す次の防御モデル

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">March 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / Threat Landscape</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Credential Attacks / Ransomware &amp; Resilience / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / SOC / Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Threat Landscape / Identity / Business Continuity</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Mandiantは2026年3月23日、2025年のFrontline Incident Investigationを基にM-Trends 2026を公表しました。報告では、Initial Access ActorからSecondary ActorへのMedian Hand-off Windowが2022年の8時間超から2025年には**22秒**まで短縮したとされています。[^source]

同時にVoice Phishingの増加、SaaS Token / Sessionを狙うIdentity Attack、Backup・Identity・Virtualizationを壊すRecovery Denial、EDRが入りにくいEdge Deviceでの長期Persistenceが観測されています。これは個別Threatではなく、**Speed・Identity・Recovery・Visibilityを同時に再設計すべき**ことを示します。

</div>

## なぜ今なのか

従来のIncident Responseは「Alertを確認してからContainment」という時間感覚でした。Access Hand-offがSeconds単位になると、Human Approvalだけに依存するContainmentでは間に合わない場面が増えます。

## M-Trendsが示した主要変化

| Trend | Observation |
| --- | --- |
| Exploit | Initial Infection Vectorの32% |
| Voice Phishing | 11%で2番目のInitial Vector |
| Prior Compromise | Ransomwareでは30%のInitial Vector |
| Hand-off | Median 22秒 |
| Recovery Denial | Backup / Identity / Virtualizationを直接Target |
| Edge Persistence | VPN / Router等のTelemetry Gapを悪用 |
| AI | Attack Lifecycleを加速するが、多くの侵入は依然Human / Systemic Failure起点 |

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| SOC | Low-severity AlertでもSecondary Intrusionの前兆になり得る |
| Identity | Voice / SaaS / Tokenを含むContinuous Verificationが必要 |
| BCP | BackupだけでなくRecovery Control Plane自体を守る必要 |
| Network | Edge DeviceをEDR外のBlind Spotとして扱わない |

## 日本企業への示唆

Ransomware対策をEndpointとBackup製品の導入で完了とせず、AD、Hypervisor、Cloud Backup、SaaS Identity、Edge Deviceを「RecoveryとTrustのControl Plane」として保護すべきです。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Initial Access後の自動Containment条件を見直す
2. SaaS / IdP / Session TokenのBehavior監視を強化する
3. BackupをCorporate ADから分離しImmutable化する
4. Hypervisor / Backup / IdentityをTier-0として扱う
5. VPN / Router等のEdge Log Retentionを延長する
6. Voice PhishingをHelpdesk / Executive向けExerciseへ入れる

</div>

## 用語解説

**Recovery Denial**  
Data暗号化だけでなく、Backup、Identity、Virtualization、Management Plane等を破壊し、組織が自力で復旧する能力そのものを奪う攻撃。

## 関連記事

- [NIST IR 8374r1](../risk-management/nist-ransomware-csf2-profile.md)
- [F5 / Confluence Edge-to-Identity](f5-confluence-edge-to-identity.md)

## 参考情報

- [Google Cloud / Mandiant, M-Trends 2026](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026)
- [Google Cloud / Mandiant, Proactive Preparation and Hardening Against Destructive Attacks: 2026 Edition](https://cloud.google.com/blog/topics/threat-intelligence/preparation-hardening-destructive-attacks)

[^source]: [Google Cloud / Mandiant, M-Trends 2026](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026)

---
title: AI as Tradecraft ― 攻撃者は「自律攻撃」より先にAIを日常の攻撃運用へ組み込んだ
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-03
description: Microsoftが2026年3月6日に公表したThreat Intelligenceを基に、Threat ActorがAIをReconnaissance、Social
  Engineering、Malware、Post-compromiseへ組み込む実態とHuman-in-the-Loopの意味を整理する。
category: Cybersecurity / AI-enabled Threats
collections:
- cybersecurity
- ai-security
topics:
- AI-Enabled Threats
- Security Governance & Risk Management
tags:
- Microsoft
- AI as Tradecraft
- Threat Actor
- Generative AI
- Human-in-the-loop
- Jasper Sleet
- Coral Sleet
audience:
- Executive
- CISO
- SOC
- Threat Intelligence
management_impact: High
impact_types:
- Threat Landscape
- Security Operations
- AI Risk
urgency: Near-term
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# AI as Tradecraft ― 攻撃者は「自律攻撃」より先にAIを日常の攻撃運用へ組み込んだ

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">March 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / AI-enabled Threats</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI-Enabled Threats / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / SOC / Threat Intelligence</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Threat Landscape / Security Operations / AI Risk</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoftは2026年3月6日、Threat ActorがAIを単発の実験ではなく、Reconnaissance、Social Engineering、Tooling、Malware Development、Post-compromise Data Triage等の攻撃工程へ組み込み始めていると報告しました。[^source]

一方で、Microsoftの観測ではTarget選定やDeployment判断などでHuman Operatorが引き続き中心的な役割を持っています。したがって3月時点の重要な変化は、**完全自律AI Attackの一般化ではなく、既存Attack Chainの摩擦と所要時間をAIが下げていること**です。

</div>

## なぜ今なのか

AI Cyber Riskを「AIが勝手に侵入する未来」だけで捉えると、現在の変化を過小評価します。攻撃者にとってAIの価値は、まず調査、文章生成、Code改善、データ整理、意思決定支援を高速化できる点にあります。

## 攻撃工程への組み込み

- Target / Persona Research
- Phishing / Social Engineering Content
- Tool / Scriptの生成・改善
- Malware Development支援
- Compromised DataのTriaging
- Asset Prioritization
- Monetizationや次のAction判断の支援
- Agentic Workflowの実験

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Threat Model | 高度Actorだけでなく一般Actorの作業効率が上がる |
| SOC | IOC更新だけでは追いつきにくくBehavior Detectionが重要 |
| Awareness | 「不自然な文章」を見抜く教育の価値が低下 |
| AI Governance | 自社AIだけでなく外部ActorのAI利用もRisk Scenarioに含める必要 |

## 日本企業への示唆

AI専用対策を急いで増やす前に、Identity、Email、Endpoint、Logging、Patch、Incident Responseの基本Controlが「攻撃速度の上昇」に耐えられるかを確認することが重要です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Attack ChainごとにAIで速度が上がる工程をThreat Modelingする
2. Phishing Detectionを文面特徴からBehavior / Infrastructureへ広げる
3. SOCのTriage自動化とHuman Escalation条件を整備する
4. Credential / Session / Identity異常を優先Monitoringする
5. AI利用の有無よりBusiness ImpactでIncident Priorityを決める

</div>

## 用語解説

**Tradecraft**  
攻撃者が継続的に利用する手法、運用方法、Tool、意思決定の組み合わせ。

## 関連記事

- [AIは「自律攻撃」以前に攻撃工程へ埋め込まれている](ai-embedded-threat-operations.md)
- [AI Enabled Malwareの「現実」](../ai-security/ai-enabled-malware-reality.md)

## 参考情報

- [Microsoft Security Blog, AI as tradecraft: How threat actors operationalize AI](https://www.microsoft.com/en-us/security/blog/2026/03/06/ai-as-tradecraft-how-threat-actors-operationalize-ai/)

[^source]: [Microsoft Security Blog, AI as tradecraft](https://www.microsoft.com/en-us/security/blog/2026/03/06/ai-as-tradecraft-how-threat-actors-operationalize-ai/)

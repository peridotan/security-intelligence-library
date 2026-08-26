---
title: NISTが示す「AI Securityは一度設定して終わりではない」理由
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-06
description: 2026年6月にNISTが公表したRobust AI Securityの数学的議論を基に、固定GuardrailからContinuous
  Red Team / Update / Resilienceへ移行する意味を整理する。
category: AI Security / Governance
collections:
- ai-security
- risk-management
tags:
- NIST
- AI Security
- Red Team
- Guardrails
- Continuous Monitoring
audience:
- Executive
- CISO
- AI Governance
- AI Platform
management_impact: High
impact_types:
- AI Governance
- Strategic Risk
- Operational Security
urgency: Strategic
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# NISTが示す「AI Securityは一度設定して終わりではない」理由

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">June 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Governance / AI Platform</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Strategic Risk / Operational Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NISTは2026年6月9日、有限の固定Guardrailだけでは適応的なAdversarial Promptに対して普遍的なRobustnessを保証できない、という数学的議論を紹介しました。NISTはこれを、AI Securityを「one and done」ではなく、継続的なRed Team、Guardrail更新、Operational Resilienceへ移す根拠として位置づけています。[^source]

経営上の意味は、AI Securityを導入時AssessmentやPolicy策定だけで完了させず、**脆弱性管理と同じContinuous Processとして予算・責任・監視を持つ必要がある**ことです。

</div>

## なぜ今なのか

LLMは自然言語という非常に広いInput Spaceを持ち、攻撃者も新しいJailbreakやPrompt Techniqueを継続的に探索します。固定Ruleや一度のRed Teamで全ての将来Inputをカバーする前提は現実的ではありません。

## 何が起きているのか

NISTは、継続的に弱点を探すRed Team、発見された弱点に応じたGuardrail更新、侵害が起きる前提でImpactを限定し素早く回復するOperational Resilienceの3要素を挙げています。目標は完全無欠ではなく、攻撃Costを上げ続けるSecurity Economicsです。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Governance | AI Security ReviewをRelease前の一回限りのGateにできない |
| Budget | 継続Red Team・Monitoring・Updateの運用費が必要 |
| Residual Risk | Guardrailがあっても残余Riskを経営判断として扱う |
| Resilience | PreventだけでなくDetect / Respond / RecoverをAIにも適用 |

## 日本企業への示唆

生成AI利用Guidelineや禁止事項だけでは継続防御になりません。Model Version、Prompt、Tool、RAG Data、Guardrailの変更を追跡し、定期Red Team、Attack Simulation、Incident対応をLifecycleへ入れる必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AI SystemごとにSecurity Ownerを定める
2. Model / Prompt / Tool変更を継続評価する
3. 定期的なAI Red Team / Adversarial Testingを行う
4. Jailbreak / Prompt AbuseのTelemetryを収集する
5. Guardrail更新をChange Managementへ組み込む
6. AI Incident Response / Kill Switchを整備する

</div>

## 用語解説

**Adversarial Prompt**  
AIの制約を回避したり意図しない挙動を引き出すことを目的とした入力。

**Operational Resilience**  
完全な防止だけに依存せず、障害・侵害時の影響限定と迅速復旧を重視する考え方。

## 関連記事

- [生成AI利活用ガバナンス](generative-ai-governance.md)
- [Agentic AIの安全設計](agentic-ai-security-controls.md)

## 参考情報

- [NIST, Mathematical Proof Supports Transition to a Continuous-Monitor-and-Update Security Model for AI Systems](https://www.nist.gov/news-events/news/2026/06/nist-mathematical-proof-supports-transition-continuous-monitor-and-update)

[^source]: [NIST, Mathematical Proof Supports Transition to a Continuous-Monitor-and-Update Security Model for AI Systems](https://www.nist.gov/news-events/news/2026/06/nist-mathematical-proof-supports-transition-continuous-monitor-and-update)

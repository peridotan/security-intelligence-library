---
title: NIST AI 800-3 ― AI Benchmarkの「1つのScore」を経営判断に使いすぎない
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-02
description: NISTが2026年2月19日に公表したAI 800-3を基に、Benchmark Accuracy、Generalized Accuracy、不確実性、AI
  Capability評価の読み方を整理する。
category: AI Security / Evaluation
collections:
- ai-security
- risk-management
topics:
- AI Governance
- AI Cyber Capability
- Security Governance & Risk Management
tags:
- NIST
- NIST AI 800-3
- AI Evaluation
- Benchmark
- Uncertainty
- GLMM
- Frontier Model
audience:
- Executive
- CISO
- AI Governance
- AI Evaluation
management_impact: High
impact_types:
- AI Governance
- Measurement
- Decision Risk
urgency: Strategic
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# NIST AI 800-3 ― AI Benchmarkの「1つのScore」を経営判断に使いすぎない

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">February 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Evaluation</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Governance / AI Cyber Capability / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Governance / AI Evaluation</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Measurement / Decision Risk</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NISTは2026年2月19日、AI Evaluation結果を統計的により正しく解釈するためのNIST AI 800-3を公表しました。[^source]

NISTは、Benchmarkで得た単一のAccuracy Scoreが、必ずしも「似た問題全般に対する実力」を意味しないこと、Evaluation結果には不確実性があり、Benchmark Itemの選び方や測定方法でInterpretationが変わることを整理しています。

これはCyber Capability評価にも重要です。**「Model Aは何％成功した」という数字だけでCapabilityやRiskを断定せず、何を測った数字なのか、どの程度一般化できるのかを見る必要**があります。

</div>

## なぜ今なのか

Frontier AIのCapability議論ではBenchmark Scoreが経営・Policy判断に使われます。しかしScoreの意味を取り違えると、過大評価・過小評価の両方が起こります。

## NISTが区別する考え方

| 指標 | 意味 |
| --- | --- |
| Benchmark Accuracy | 実際に出題した固定問題群でのPerformance |
| Generalized Accuracy | 類似問題のより広い集合へ一般化したPerformance |
| Uncertainty | 測定結果がどの程度ぶれ得るか |
| Assumptions | 統計Modelが前提にしている条件 |

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Model Selection | Score差だけでVendor選定しない |
| Risk | Cyber / Safety Benchmarkの数字を確率的Evidenceとして扱う |
| Governance | Evaluation MethodとAssumptionを記録する |
| Board Reporting | 「Score」ではなくRange / Limitationも説明する |

## 日本企業への示唆

AI製品比較やPoC評価でも、Benchmarkの順位をそのまま採用理由にせず、自社Use CaseでのEvaluationとUncertaintyを併記する方が安全です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AI Evaluationの目的を明確化する
2. Benchmarkと実Use Caseを区別する
3. ScoreにConfidence / Variationを付ける
4. Vendor公表値のEvaluation Conditionを確認する
5. Cyber Capability評価では再現性とScopeを確認する
6. Board向け資料で数字の限界を明記する

</div>

## 用語解説

**Generalized Accuracy**  
特定Benchmarkの問題だけでなく、それと同種のより広い問題集合に対してどの程度Performanceを発揮すると推定できるかを表す考え方。

## 関連記事

- [Frontier AIのCyber Capability](claude-mythos-preview-cyber-capability.md)
- [Kimi K3 Cyber Capabilities](kimi-k3-cyber-capabilities.md)

## 参考情報

- [NIST, Expanding the AI Evaluation Toolbox with Statistical Models](https://www.nist.gov/news-events/news/2026/02/new-report-expanding-ai-evaluation-toolbox-statistical-models)

[^source]: [NIST AI 800-3](https://www.nist.gov/news-events/news/2026/02/new-report-expanding-ai-evaluation-toolbox-statistical-models)

---
title: GTIG AI Threat Tracker ― AIは攻撃Toolであると同時に「盗まれるAsset」になった
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-02
description: Google Threat Intelligence Groupの2026年2月AI Threat Trackerを基に、Model Extraction
  / Distillation、Threat ActorのAI利用、AI-enabled Malware実験を整理する。
category: Cybersecurity / AI-enabled Threats
collections:
- cybersecurity
- ai-security
topics:
- AI-Enabled Threats
- AI Infrastructure
- AI Cyber Capability
tags:
- Google
- GTIG
- AI Threat Tracker
- Model Extraction
- Distillation
- HONESTCUE
- AI-enabled Malware
audience:
- Executive
- CISO
- AI Security
- Threat Intelligence
management_impact: High
impact_types:
- AI Security
- Intellectual Property
- Threat Landscape
urgency: Near-term
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# GTIG AI Threat Tracker ― AIは攻撃Toolであると同時に「盗まれるAsset」になった

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">February 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / AI-enabled Threats</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI-Enabled Threats / AI Infrastructure / AI Cyber Capability</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Security / Threat Intelligence</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Security / Intellectual Property / Threat Landscape</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Google Threat Intelligence Group（GTIG）は2026年2月12日、AI Threat Trackerの更新を公開し、Threat ActorによるAI活用だけでなく、**Model Extraction / Distillation AttackによってAI Model自体のCapabilityやReasoningを盗もうとする活動**を報告しました。[^source]

Googleは100,000件超のPromptを含むExtraction Campaignを検出した例を挙げています。また、AI-enabled Malwareについては実験が進んでいるものの、「革命的なParadigm Shift」はまだ観測していないとしています。

</div>

## なぜ今なのか

企業が独自ModelやDomain-specific AIを持つようになると、Model WeightだけでなくAPI経由のCapability ExtractionもIP Riskになります。同時に攻撃者はAIをReconnaissance、Vulnerability Research、Malware開発等へ組み込みます。

## 2つのRisk Surface

<div class="sil-flow" role="group" aria-label="Dual AI threat surface">
  <div class="sil-flow-branches">
    <div class="sil-flow-step"><strong>AI as Tool</strong><span>Recon / Scripting / Malware / Lure</span></div>
    <div class="sil-flow-step"><strong>AI as Target</strong><span>Model Extraction / Distillation / Capability Theft</span></div>
  </div>
</div>

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| AI Security | Model API利用そのものをAbuse Detection対象にする |
| IP | Model CapabilityやDomain Knowledgeも保護対象になる |
| Threat Intel | AI使用の有無よりAttack Outcomeを見る必要 |
| Vendor Risk | External Model APIのMisuse Detection能力も評価対象 |

## 日本企業への示唆

自社独自Modelを提供する場合はRate LimitだけでなくPrompt Pattern、Repeated Capability Probe、Suspicious Automationを監視する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AI API AccessをIdentity単位で監視する
2. Extraction / Scraping PatternをUse Caseとして定義する
3. Rate LimitとBehavior Detectionを組み合わせる
4. Proprietary Model / Prompt / Fine-tuneをIP Inventoryへ追加する
5. AI-enabled Malwareを過大評価せずObserved Capabilityで判断する
6. AI VendorへAbuse Detection / Enforcement能力を確認する

</div>

## 用語解説

**Model Extraction**  
API等へ大量のQueryを送り、Modelの出力やCapabilityを収集して別Modelへ移植・再現しようとする行為。

## 関連記事

- [AI Enabled Malwareの「現実」](../ai-security/ai-enabled-malware-reality.md)
- [AI as Tradecraft](ai-as-tradecraft-march-2026.md)

## 参考情報

- [Google Cloud / GTIG, Distillation, Experimentation, and Continued Integration of AI for Adversarial Use](https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use)

[^source]: [GTIG AI Threat Tracker, February 2026](https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use)

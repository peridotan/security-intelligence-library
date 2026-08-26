---
title: Singapore Agentic AI Governance v1.5 ― 「自律性をRisk Tierで制限する」実装例
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-05
description: Singapore IMDAが2026年5月20日に更新したModel AI Governance Framework for Agentic
  AIを基に、Risk Bounding、人の責任、Multi-agent、Third-party Agentの実装を整理する。
category: Regulation / AI Governance
collections:
- regulation
- ai-security
- risk-management
topics:
- AI Governance
- AI Agent Security
- Regulation & Policy
tags:
- Singapore
- IMDA
- Agentic AI
- Human Oversight
- Automation Bias
- Multi-agent
audience:
- Executive
- CISO
- AI Governance
- Business Owner
management_impact: High
impact_types:
- AI Governance
- Regulatory
- Operational Risk
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# Singapore Agentic AI Governance v1.5 ― 「自律性をRisk Tierで制限する」実装例

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">May 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Regulation / AI Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Governance / AI Agent Security / Regulation &amp; Policy</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Governance / Business Owner</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Regulatory / Operational Risk</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Singapore IMDAは2026年5月20日、Model AI Governance Framework for Agentic AIを更新しました。60を超える組織からのFeedbackや10件超の実Deployment Caseを取り込み、Multi-agent System、Third-party Agent、Automation Bias等の新しいBest Practiceを追加しています。[^source]

特に実務的なのは、Agent ActionをImpactやReversibilityに応じてTier分けし、**低Riskは自動化、中RiskはHuman Approval、高RiskはAgentに実行させない**という考え方をCase Studyで示している点です。

</div>

## なぜ今なのか

Agentic AIは、導入可否だけでなく「どこまで自律化してよいか」を決める必要があります。

従来のAI GovernanceがData、説明可能性、Biasを中心に設計されていたのに対し、Agentic AIではAction Scope、Tool Permission、Human Checkpoint、Third-party Agent、Multi-agent Interactionが追加論点になります。

## Frameworkの4つの柱

1. Riskを事前に評価しAgentの権限をBoundする
2. 人をMeaningfully Accountableにする
3. Lifecycle全体でTechnical Control / Processを実装する
4. End UserへTransparencyとTrainingを提供する

更新版では実際のAgent Deployment Caseを通じて、AutonomyをRisk Tierで変える方法が示されています。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Delegation | 人からAgentへ委譲できるActionの上限を定義する必要 |
| Accountability | 「AIが実行した」ではなくOwnerと承認者を残す |
| Third-party Risk | 外部Agentも自社Control Frameworkへ組み込む |
| Human Factors | Automation BiasをRiskとして扱う必要 |

## 日本企業への示唆

全Agentを一律に「Human-in-the-Loop」にすると業務効率が出ず、逆に全面自動化するとRiskが上がります。ActionをTieringし、低Riskだけ自動化する設計が現実的です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Agent ActionをImpact / Reversibility / DetectabilityでTieringする
2. 高Risk ActionはAgent実行禁止またはMandatory Approvalにする
3. Third-party Agentの権限とData Accessを可視化する
4. Multi-agent間のDelegation ChainをAudit可能にする
5. Automation BiasをTraining / UI Designの対象にする
6. Agent変更時にRisk Tierを再評価する

</div>

## 用語解説

**Automation Bias**  
自動化Systemの判断を人が過度に信頼し、誤りを見逃したり自らの判断を弱めたりする傾向。

## 関連記事

- [NIST AI Agent Security分析](../ai-security/nist-ai-agent-security-rfi-analysis.md)
- [Agentic AIの安全設計](../ai-security/agentic-ai-security-controls.md)

## 参考情報

- [Singapore IMDA, Updated Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/factsheets/2026/updated-model-ai-governance-framework-for-agentic-ai)
- [Singapore IMDA, Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf)

[^source]: [Singapore IMDA, Updated Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/factsheets/2026/updated-model-ai-governance-framework-for-agentic-ai)

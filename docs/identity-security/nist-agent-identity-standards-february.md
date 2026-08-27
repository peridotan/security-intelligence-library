---
title: NISTがAI Agentを「Identity＋Standards」の問題として定義し始めた
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-02
description: NISTが2026年2月に公開したAI Agent Identity and Authorization Concept PaperとAI
  Agent Standards Initiativeを基に、識別・認可・監査・Non-repudiation・Interoperabilityの意味を整理する。
category: Identity Security / AI Agent
collections:
- identity-security
- ai-security
topics:
- AI Agent Security
- Identity Security
- AI Governance
tags:
- NIST
- NCCoE
- CAISI
- AI Agent
- Agent Identity
- Authorization
- Non-repudiation
- Interoperability
audience:
- Executive
- CISO
- IAM
- AI Governance
management_impact: High
impact_types:
- Identity
- AI Governance
- Architecture
urgency: Strategic
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# NISTがAI Agentを「Identity＋Standards」の問題として定義し始めた

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">February 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / AI Agent</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Agent Security / Identity Security / AI Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / IAM / AI Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / AI Governance / Architecture</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NISTは2026年2月5日、Software / AI AgentへIdentity StandardとBest Practiceを適用するConcept Paperを公開し、Identification、Authorization、Auditing、Non-repudiation、Prompt Injection対策などを論点として提示しました。さらに2月17日には**AI Agent Standards Initiative**を開始し、AgentのSecurity・Identity・Interoperabilityを標準化の主要課題として位置づけました。[^source1][^source2]

この2つを合わせると、AI Agentは単なるApplication Featureではなく、**独立したAction主体として識別・認可・監査され、他Systemと安全に相互運用する必要がある**という方向が明確になっています。

</div>

## なぜ今なのか

AgentはEmail、Calendar、Code、Data、SaaS等へ接続し、数時間にわたってActionできるようになっています。Human UserのSession内で動く単純Automationとして扱うだけでは、責任と権限を追跡しにくくなります。

## NISTが示した主要論点

- Agent Identification
- Authorization
- Auditing
- Non-repudiation
- Prompt Injection Mitigation
- Secure Interoperability
- Industry-led Standards / Protocol
- Open Source Protocol Development

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| IAM | Agentにも独立IdentityとLifecycleが必要 |
| Authorization | Humanの全権限をAgentへコピーしない設計が必要 |
| Audit | Human → Agent → Tool → Actionを追跡可能にする |
| Standards | Proprietary Agent連携だけに依存するとLock-in Riskが高まる |

## 日本企業への示唆

AI Agent導入時には「誰の代わりに動くか」だけでなく、「Agent自身を何として識別するか」「どのTokenを使うか」「誰が停止できるか」をArchitecture Requirementに含める必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AI AgentをIdentity Inventoryへ追加する
2. Human Credentialの共有を禁止する
3. Short-lived / Scoped Tokenを利用する
4. Agent ActionをHuman Principalと関連付けてLogする
5. Tool / Protocol選定でInteroperabilityを確認する
6. Prompt Injectionによる権限逸脱をThreat Modelへ追加する

</div>

## 用語解説

**Non-repudiation**  
誰が、どのIdentityを使い、どのActionを実行したかを後から否認できない形で証明・追跡できる性質。

## 関連記事

- [AI Agent Identity / NHI](ai-agent-identity-nhi.md)
- [NIST AI Agent Security RFI](../ai-security/nist-ai-agent-security-rfi-analysis.md)

## 参考情報

- [NIST, New Concept Paper on Identity and Authority of Software Agents](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents)
- [NIST, AI Agent Standards Initiative](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure)

[^source1]: [NIST, Agent Identity and Authorization Concept Paper](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents)
[^source2]: [NIST, AI Agent Standards Initiative](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure)

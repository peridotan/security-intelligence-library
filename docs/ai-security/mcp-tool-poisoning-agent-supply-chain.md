---
title: MCP Tool Poisoning ― AI AgentのSupply Chainは「コード」だけではない
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-06
description: 2026年6月のMicrosoft Incident Responseの分析を基に、MCP Tool Descriptionの改変がAI
  Agentの行動を変えるSupply Chain Riskを整理する。
category: AI Security / Supply Chain
collections:
- ai-security
- risk-management
topics:
- AI Agent Security
- MCP Security
- Software Supply Chain
tags:
- AI Agent
- MCP
- Tool Poisoning
- Agentic Supply Chain
- Least Agency
audience:
- Executive
- CISO
- AI Governance
- AI Platform
management_impact: High
impact_types:
- AI Governance
- Supply Chain
- Data / IP
urgency: Immediate
evidence: Assessment
status: published
pptx: ''
media_rights: none
---
# MCP Tool Poisoning ― AI AgentのSupply Chainは「コード」だけではない

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">June 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Supply Chain</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Agent Security / MCP Security / Software Supply Chain</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Governance / AI Platform</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Supply Chain / Data / IP</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Assessment</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoft Incident Responseは2026年6月30日、Enterprise AI Agentが「読む」だけでなく「行動する」段階へ移る中で、MCP ToolのDescription Metadataを悪意ある指示へ変更するTool Poisoning Patternを解説しました。記事では、承認済み第三者Toolの説明が更新され、Agentが本来不要な機密DataをTool Callへ付加して外部送信する例を示しています。[^source]

これは特定のCopilot脆弱性報告ではなく、**Agentic Supply Chainにおける一般的な攻撃Pattern**です。Tool Description自体をSystem Prompt相当のControl Planeとして扱う必要があります。

</div>

## なぜ今なのか

AI AgentはTool名だけでなく自然言語のTool Descriptionを読んで、どのToolをいつ、どのParameterで呼ぶか判断します。そのため、Dependency Codeを変更しなくてもMetadata更新だけでAgent Behaviorを変えられる場合があります。

## 何が起きているのか

Microsoftが示したPatternでは、第三者MCP ServerのTool Descriptionに隠れた指示を混入し、Agentへ追加Data収集と送信を促します。個々の操作は正規権限の範囲内でも、連鎖全体ではData Exfiltrationになります。Microsoftは「Tool DescriptionをSystem Promptとして扱う」「Least PrivilegeだけでなくLeast Agencyを適用する」ことを推奨しています。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Third-party Risk | MCP ServerやConnectorが新しいSoftware Supply Chain Dependencyになる |
| Data Loss | 正規Tool CallのParameterとして機密Dataが流出し得る |
| Change Control | Tool Metadata変更をCode Changeと同じ水準でReviewする必要 |
| Autonomy | 権限が小さくても自律性が高いAgentは大きな影響を出し得る |

## 日本企業への示唆

MCP導入時は「Serverを一度承認したら終わり」ではなく、Publisher、Tool、Description、Endpoint、Permissionの変更を継続監視する必要があります。財務、人事、顧客Dataなどを扱うAgentでは、Tool Call ParameterにDLPを適用し、重要ActionへHuman Approvalを組み合わせるべきです。

<div class="sil-action-box" markdown>

## 推奨アクション

1. MCP Server / PublisherをInventory化する
2. Tool Description更新をSecurity Review対象にする
3. Agentが利用できるToolをAllowlistで限定する
4. 外部ToolへのParameterにDLP / Data Classificationを適用する
5. 高影響ActionへHuman-in-the-Loopを入れる
6. Agent Behavior Baselineと新規Endpointを監視する

</div>

## 用語解説

**Tool Poisoning**  
ToolのMetadataやDescriptionへ悪意ある指示を混入し、AgentのTool選択・実行を誘導する攻撃。

**Least Agency**  
Agentに必要最小限の権限だけでなく、必要最小限の自律性・行動範囲だけを与える考え方。

## 関連記事

- [Agentic AIの安全設計](agentic-ai-security-controls.md)
- [AutoJack](autojack-agent-localhost-rce.md)

## 参考情報

- [Microsoft, Securing AI agents: When AI tools move from reading to acting](https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/)

[^source]: [Microsoft, Securing AI agents: When AI tools move from reading to acting](https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/)

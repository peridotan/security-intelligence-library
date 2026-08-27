---
title: LangGrinch ― AI Application Supply ChainはPromptだけでなくFrameworkも攻撃面になる
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-01
description: Microsoftが2026年1月30日に公開したLangChain Core CVE-2025-68664のCase Studyを基に、AI
  Framework、Serialization Injection、Secret Exposure、Code-to-Runtime Securityを整理する。
category: AI Security / Software Supply Chain
collections:
- ai-security
- cybersecurity
topics:
- Software Supply Chain
- AI Agent Security
- Vulnerability Management
tags:
- Microsoft
- LangChain
- LangGrinch
- CVE-2025-68664
- Serialization Injection
- AI Framework
- Software Supply Chain
- Secret Exposure
audience:
- Executive
- CISO
- Application Security
- AI Platform
management_impact: High
impact_types:
- Software Security
- AI Security
- Supply Chain
urgency: Immediate
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# LangGrinch ― AI Application Supply ChainはPromptだけでなくFrameworkも攻撃面になる

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">January 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Software Supply Chain</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Software Supply Chain / AI Agent Security / Vulnerability Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Application Security / AI Platform</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Software Security / AI Security / Supply Chain</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoft Defender Security Researchは2026年1月30日、LangChain CoreのCVE-2025-68664（LangGrinch、CVSS 9.3）を例に、AI Application Supply ChainのSecurityを解説しました。[^source]

このVulnerabilityはSerialization / Deserialization処理におけるControl DataとUser-controlled Dataの分離不備に起因し、条件次第でEnvironment Variable等のSecret取得や意図しないClass Instantiationにつながります。

重要なのは、AI SecurityがPrompt Injectionだけでは完結しないことです。**Framework、SDK、Orchestrator、Serialization Layerといった通常のSoftware Supply Chain Riskが、AgentのTool / Secret / Runtimeと結び付く**ためです。

</div>

## なぜ今なのか

AI ApplicationはLangChain等のFrameworkへ大きく依存します。Modelが安全でもFramework Vulnerabilityがあれば、Agent EnvironmentやSecretへ到達される可能性があります。

## Attack Surface

<div class="sil-flow" role="group" aria-label="AI application supply chain risk flow">
  <div class="sil-flow-step"><strong>AI Application</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Framework / SDK / Orchestrator</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Serialization / Runtime</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-branches">
    <div class="sil-flow-step"><strong>Secrets</strong></div>
    <div class="sil-flow-step"><strong>Tools / APIs</strong></div>
    <div class="sil-flow-step"><strong>Cloud / Data</strong></div>
  </div>
</div>

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| AI Security | Model / Prompt対策だけでは不十分 |
| SBOM | AI Framework / PackageをInventoryへ含める必要 |
| Secret | Agent RuntimeのEnvironment SecretがHigh-value Target |
| Patch | AI StackのDependency Update Processが必要 |

## 日本企業への示唆

AI PoCからProductionへ移行する際、Framework / SDKを「試作用Library」として放置せず、通常Applicationと同じVulnerability / Dependency Management対象にする必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AI ApplicationのDependency Inventoryを作る
2. LangChain等のVersionを継続監視する
3. SecretをEnvironmentへ過剰配置しない
4. Framework VulnerabilityをCI/CD Gateへ入れる
5. Code / Image / Runtimeの3段階で検出する
6. AI FrameworkをSupplier Risk対象へ含める

</div>

## 用語解説

**Serialization Injection**  
DataをObjectへ復元する際、User-controlled DataがControl Informationとして解釈され、意図しないObjectや処理を生成するVulnerability。

## 関連記事

- [Mastra npm Supply Chain](../cybersecurity/mastra-npm-ai-supply-chain.md)
- [MCP Tool Poisoning](mcp-tool-poisoning-agent-supply-chain.md)

## 参考情報

- [Microsoft Security Blog, Case study: Securing AI application supply chains](https://www.microsoft.com/en-us/security/blog/2026/01/30/case-study-securing-ai-application-supply-chains/)

[^source]: [Microsoft Defender Security Research, AI application supply chains](https://www.microsoft.com/en-us/security/blog/2026/01/30/case-study-securing-ai-application-supply-chains/)

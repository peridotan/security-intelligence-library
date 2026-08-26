---
title: Mastra npm Supply Chain Compromise ― AI Frameworkも「開発者のTrust」を狙われる
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-06
description: 2026年6月にMicrosoftが報告したMastra npm Supply Chain Compromiseを基に、AI開発FrameworkとDeveloper
  CredentialのSupply Chain Riskを整理する。
category: Cybersecurity / Supply Chain
collections:
- cybersecurity
- ai-security
- risk-management
topics:
- Software Supply Chain
- Third-party Risk / C-SCRM
tags:
- Software Supply Chain
- npm
- Mastra
- AI Framework
- Developer Security
audience:
- Executive
- CISO
- AppSec
- Developer Platform
management_impact: High
impact_types:
- Supply Chain
- Credential Risk
- Software Security
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---
# Mastra npm Supply Chain Compromise ― AI Frameworkも「開発者のTrust」を狙われる

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">June 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / Supply Chain</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Software Supply Chain / Third-party Risk / C-SCRM</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AppSec / Developer Platform</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Supply Chain / Credential Risk / Software Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoft Threat Intelligenceは2026年6月17日、AI Agent FrameworkのMastra ecosystemで、npm maintainer accountの侵害を起点に140超のPackageへ悪意あるDependencyが混入したSupply Chain Attackを報告しました。Microsoftの調査では、Install時のpostinstall処理を通じて追加Payloadが実行される構造が確認されています。[^source]

AI FrameworkはCloud Credential、API Key、Model Provider Token等へ近いDeveloper Environmentで使われるため、**AI Supply Chain CompromiseはAI SystemだけでなくCI/CD・Cloud・Developer Identityへ波及する**可能性があります。

</div>

## なぜ今なのか

AI開発は多数のOpen Source Package、Agent Framework、Connector、SDKへ依存します。Popular Frameworkが侵害されれば、一つのMaintainer AccountやPackage Releaseから多数のDownstream Projectへ影響が広がります。

## 何が起きているのか

本件ではMastra関連Package群へ悪意あるDependencyが混入し、Package Install時にPayload実行へつながるSupply Chain Patternが観測されました。重要なのはPackageのNameやPublisherを信頼するだけでなく、Version、Provenance、Maintainer Access、Install Script、Downstream Dependencyまで継続的に検証する必要がある点です。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Developer Identity | Package Publisher / Maintainer Accountが高価値Identityになる |
| CI/CD | Build RunnerのCloud / Repository Credentialへ到達し得る |
| Blast Radius | Popular Frameworkの一度の侵害が多数Projectへ波及 |
| AI Adoption | AI導入速度がDependency追加速度を上げ、審査が追いつかない可能性 |

## 日本企業への示唆

AI Application Teamが独自判断でFrameworkやMCP Packageを追加できる環境では、通常のOSS GovernanceとAI Governanceを分離しない方が安全です。SBOMだけでなくPackage Provenance、Maintainer Risk、Install Script、CI Credential Exposureを確認する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AI / Agent FrameworkをSoftware Inventoryへ含める
2. Package VersionをLockしUnexpected Updateを検知する
3. Maintainer / Publisher Accountへ強いMFAを要求する
4. CI RunnerのCredentialを短命・最小権限化する
5. Install Script実行を制限・監視する
6. Package compromise時のCredential Rotation手順を整備する

</div>

## 用語解説

**Software Supply Chain Attack**  
依存Package、Build Process、Repository、Publisher等の信頼関係を悪用してDownstreamへ侵害を広げる攻撃。

**postinstall**  
npm PackageのInstall後に自動実行されるScript Lifecycle hook。

## 関連記事

- [C-SCRM Due Diligence](../risk-management/c-scrm-due-diligence-sp1326.md)
- [MCP Tool Poisoning](../ai-security/mcp-tool-poisoning-agent-supply-chain.md)

## 参考情報

- [Microsoft Security Blog, From package to postinstall payload: Inside the Mastra npm supply chain compromise by Sapphire Sleet](https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/)
- [Socket, 140+ Mastra npm Packages Compromised in Coordinated Supply Chain Attack](https://socket.dev/blog/mastra-npm-packages-compromised)

[^source]: [Microsoft Security Blog, From package to postinstall payload: Inside the Mastra npm supply chain compromise by Sapphire Sleet](https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/)

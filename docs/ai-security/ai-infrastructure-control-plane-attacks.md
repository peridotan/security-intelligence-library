---
title: AI Infrastructureが攻撃対象へ ― LiteLLM・RAGFlow・Kestraが示すControl Plane Risk
date: 2026-09-03
updated: 2026-09-03
reviewed: '2026-09-03'
review_status: Current
source_period: 2026-08
description: Microsoftが2026年8月26日に報告したLiteLLM、RAGFlow、Kestraへの侵害を基に、AI Gateway・RAG・OrchestratorがCredential・Data・Executionを集中させるControl
  PlaneになるRiskを整理する。
category: AI Security
collections:
- ai-security
- cybersecurity
- risk-management
topics:
- AI Infrastructure
- Vulnerability Management
- Security Governance & Risk Management
tags:
- AI Infrastructure
- LiteLLM
- RAGFlow
- Kestra
- AI Gateway
- RAG
- Orchestration
- Credential Theft
- Control Plane
mitre_attack:
- id: T1190
  basis: Source-labeled
  note: Microsoftが、Internet公開されたAI Workload SurfaceへのInitial AccessとしてExploit Public-Facing
    Applicationを明示。
- id: T1552.001
  basis: Source-labeled
  note: Microsoftが、LiteLLM等のRuntimeや設定からProvider API KeyやDatabase Credentialを取得する活動をCredentials
    in Filesとして明示。
audience:
- Executive
- CISO
- AI Platform
- Cloud Security
management_impact: High
impact_types:
- AI Infrastructure
- Credential Risk
- Cloud Security
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---
# AI Infrastructureが攻撃対象へ ― LiteLLM・RAGFlow・Kestraが示すControl Plane Risk

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-09-03</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">August 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-09-03</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-09-03</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Infrastructure / Vulnerability Management / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Platform / Cloud Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Infrastructure / Credential Risk / Cloud Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoft Security Researchは2026年8月26日、**LiteLLM Gateway、RAGFlow、Kestraという3種類のAI関連Workloadで実際に観測した侵害活動**を公開しました。攻撃経路は異なりますが、Credential窃取、Persistence、Container / Host Access、Cryptominingなど、侵害後の目的には共通性があります。[^source]

重要なのは、これらを単なる「AI製品の脆弱性」として見ないことです。AI Gateway、Retrieval Platform、Workflow Orchestratorは、Model Provider Key、Database Connection、Tenant Configuration、Container、Workflow Execution等を集約しやすく、**AI Stackにおける新しいControl Plane**になっています。

そのためAI Securityは、Prompt InjectionやModel Safetyだけでなく、通常のInternet-facing Application Security、Secret Management、Container Security、Patch / Exposure Managementまで統合して考える必要があります。

</div>

## なぜ今なのか

企業のAI利用がPoCからProductionへ移るにつれ、Modelの周囲にGateway、RAG、Tool Server、Workflow Engine、Vector / Database、Container Runtimeが増えています。

こうしたComponentは「AIを動かす裏方」に見えますが、実際には複数のCredential、Data Source、Execution Pathを集中させます。侵害された場合、単一Applicationより大きなBlast Radiusを持つ可能性があります。

Microsoftは今回の3事例を通じて、AI Workloadを個別Applicationではなく、**Credential・Data Access・Model Connectivity・Execution Privilegeが集中するControl Point**として監視する必要があるとしています。

## 確認された3つの侵害パターン

| AI Workload | 観測された活動 | 主なRisk |
| --- | --- | --- |
| **LiteLLM** | Gateway RuntimeからSecret取得、PostgreSQL Access、Persistence、Miner | Model Provider Key / Proxy Key / DB Credentialの集中 |
| **RAGFlow** | Application Path改変、LLM設定FlowへのHook、Provider Credential取得 | 新規登録されるLLM API Keyの継続窃取 |
| **Kestra** | Workflow経由のShell Execution、Container探索、XMRig展開 | OrchestratorのExecution権限・Container Secretの悪用 |

LiteLLMでは、Microsoftは公開されたGateway Surfaceの悪用を高い確度で評価し、CVE-2026-42271とCVE-2026-48710を関連するPublic Vulnerability Pathとして挙げています。

Kestraについても、CVE-2026-49869によるAuthentication BypassをInitial Accessとして高い確度で評価しています。

RAGFlowでは、SSRF風の探索後にCode ExecutionとApplication改変が観測されていますが、Microsoftは**特定の脆弱性への帰属については低い確度**としており、ここは区別が必要です。

## AI Control Planeとして見る

<div class="sil-flow" role="group" aria-label="AI infrastructure control plane">
  <div class="sil-flow-branches">
    <div class="sil-flow-step"><strong>Users / Apps</strong></div>
    <div class="sil-flow-step"><strong>Enterprise Data</strong></div>
    <div class="sil-flow-step"><strong>Model Providers</strong></div>
  </div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>AI Gateway / RAG / Orchestrator</strong><span>Credential · Routing · Execution · Tenant Configuration</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-branches">
    <div class="sil-flow-step"><strong>API Keys</strong></div>
    <div class="sil-flow-step"><strong>Containers / Hosts</strong></div>
    <div class="sil-flow-step"><strong>Workflow / Tools</strong></div>
  </div>
</div>

この中央層が侵害されると、AI Modelそのものを破らなくても、Model利用権、Data Access、Compute、Downstream Systemへの接続を悪用できます。

<!-- AUTO:MITRE:START -->
## MITRE ATT&CK® Mapping

<div class="sil-mitre-note" markdown>

この表は、攻撃・Campaignの理解に有用な場合だけ表示します。`Source-labeled` は一次情報がATT&CK IDを明示したもの、`Analyst-mapped` は一次情報に記載された行動を本LibraryがATT&CKへ対応付けたものです。後者は、元情報の発行者がそのATT&CK IDを明示したことを意味しません。

</div>

| Technique | Tactic | Basis | Article context |
| --- | --- | --- | --- |
| [T1190 Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | Initial Access | Source-labeled | Microsoftが、Internet公開されたAI Workload SurfaceへのInitial AccessとしてExploit Public-Facing Applicationを明示。 |
| [T1552.001 Credentials In Files](https://attack.mitre.org/techniques/T1552/001/) | Credential Access | Source-labeled | Microsoftが、LiteLLM等のRuntimeや設定からProvider API KeyやDatabase Credentialを取得する活動をCredentials in Filesとして明示。 |

<div class="sil-mitre-legal">
MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation. © 2026 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation.
</div>
<!-- AUTO:MITRE:END -->

## 経営インパクト

| 観点 | 経営上の意味 |
| --- | --- |
| AI Adoption | AI Platformを「新しいSaaS」として軽く扱わない |
| Credential | Model API KeyやCloud Secretが一か所へ集中しやすい |
| Vulnerability | Internet公開AI Management Surfaceを緊急Patch対象へ入れる |
| Cloud / Container | AI PlatformとContainer Runtimeを一体で監視する |
| Incident Response | AI Gateway侵害時はCredential RotationとDownstream影響確認が必要 |

## 日本企業への示唆

AI Platformを導入するときは、Model選定だけでなく、**Gateway / RAG / Orchestrator / MCP / Container / Secret Storeの構成**を一つのSecurity Architectureとして把握する必要があります。

特にPoC環境をそのままInternet公開したり、Environment Variableへ多数のAPI Keyを格納したり、AI Gatewayへ広いNetwork Accessを与えたりすると、便利なControl Planeがそのまま攻撃者のControl Planeになります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. **AI Infrastructure Inventoryを作る** — Gateway、RAG、Orchestrator、MCP、Vector DB、Container Runtimeを棚卸しする。
2. **Internet Exposureを最小化する** — Management / Admin InterfaceをPrivate Accessへ寄せる。
3. **Secretを集中させすぎない** — Environment Variableや設定ファイルの長期Credentialを減らし、短命Credential / Vaultを利用する。
4. **AI Workload起点のShell / Secret Accessを監視する** — GatewayやOrchestrator Processからの異常実行をHigh-signal Eventとして扱う。
5. **Patch PriorityをControl Planeで上げる** — AI InfrastructureのPublic-facing RCE / Auth Bypassは通常Applicationより高く扱う。
6. **侵害時のCredential RotationをRunbook化する** — Model Provider、Cloud、DB、SaaS、Container Secretまで影響範囲を確認する。

</div>

## 好意的・批判的に見ると

**重要な変化**は、AI固有の未知攻撃が必要だったわけではなく、既知のApplication / Credential / Container Securityの原則がAI Stackにもそのまま効くことです。既存Security ProgramをAI Infrastructureへ拡張できます。

一方で、3事例だけから「すべてのAI Platformが大量に侵害されている」と一般化することはできません。Microsoftが観測した具体的Case Studyとして扱い、ExposureとAsset Importanceに応じて優先順位を決めるべきです。

## 用語解説

**AI Gateway**  
Applicationと複数のAI Model Providerの間に入り、Routing、Authentication、Rate Limit、Policy、Key Management等を担うComponent。

**Control Plane**  
System全体の設定、権限、Routing、実行を管理する中枢。侵害されると複数Resourceへ影響が波及しやすい。

## 関連記事

- [AI Agent Identity / NHI](../identity-security/ai-agent-identity-nhi.md)
- [Agentic AIの安全設計](agentic-ai-security-controls.md)
- [脆弱性悪用の猶予は48時間以下へ](../cybersecurity/exploitation-window-48-hours.md)

## 参考情報

- [Microsoft Security Research, When AI infrastructure becomes the target: Securing gateways and control points (2026-08-26)](https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/)

[^source]: [Microsoft Security Research, When AI infrastructure becomes the target (2026-08-26)](https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/)

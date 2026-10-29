---
title: LiteLLM 1.107.0 Supply Chain Compromise ― Python起動だけでCredential Theftが走る
date: 2026-10-29
updated: 2026-10-29
reviewed: 2026-10-29
review_status: Needs Review
source_period: 2026-10
description: LiteLLM 1.107.0のPoisoned Releaseを基に、Python Startup Hook、GitHub Owner Token、Release Pipeline、AI Gateway Credentialの連鎖的Riskを整理する。
category: AI Security
collections:
  - ai-security
  - cybersecurity
topics:
  - Software Supply Chain
  - AI Infrastructure
  - Identity Security
tags:
  - LiteLLM
  - Python
  - PyPI
  - Supply Chain
  - Credential Theft
  - CI/CD
  - AI Gateway
mitre_attack:
  - id: T1195.001
    basis: Source-labeled
    note: MicrosoftがLiteLLM 1.107.0の悪意あるWheelとContainer Image配布をCompromise Software Dependencies and Development Toolsとして明示。
  - id: T1546.018
    basis: Source-labeled
    note: Microsoftがcook.pthとsitecustomize.pyによるPython初期化時の自動実行をPython Startup Hooksとして明示。
audience:
  - Executive
  - CISO
  - AI Platform
  - DevSecOps
management_impact: High
impact_types:
  - AI Infrastructure
  - Software Supply Chain
  - Credential Risk
urgency: Immediate
evidence: Mixed
status: draft
pptx: ""
media_rights: none
---

# LiteLLM 1.107.0 Supply Chain Compromise ― Python起動だけでCredential Theftが走る

<div class="sil-executive-summary" markdown>

## Executive Summary

2026年10月21日、LiteLLMのRelease Pipelineから悪意あるバージョン1.107.0がPyPIと公式Container Registryへ公開されました。LiteLLMの公式Incident Reportによると、PyPI Wheelは約2時間、Docker HubとGHCRの一部Tagも一定時間、侵害されたArtifactを指していました。[^litellm-incident]

Microsoftの解析では、悪意あるPackageがPython Startup Hookを利用したため、ApplicationがLiteLLMを明示的にImportしなくても、影響環境でPythonを起動するだけでCredential Collectorが実行され得ました。標的にはDeveloper Tool、Cloud、Browser、SSH、AI Application、LiteLLM Database内の一部Credential・Model Configurationが含まれます。[^microsoft]

本件は、AI Gatewayの脆弱性というより、**AI Platformが持つCredential、Developer Identity、CI/CD Approval、Package ReleaseのTrustが一つの攻撃Chainで破られたSupply Chain Incident**です。既存のLiteLLM記事がInternet-facing Runtime侵害を扱うのに対し、本稿はPoisoned ReleaseとRelease Governanceを扱います。

</div>

## なぜ今なのか

AI GatewayはModel Provider API Key、Database Connection、Workload Identity、Routing Policy等を集約します。同時に、そのSoftware PackageはDeveloper Workstation、CI/CD Runner、Test Environment、ContainerにもInstallされます。したがって、一つの正規Releaseが侵害されると、AI Runtimeだけでなく開発・配布・CloudのCredentialへ影響が広がります。

さらに本件では、Packageの使用時ではなくPython Interpreterの初期化時にPayloadが起動しました。Incident Responseで確認のためにPythonやpipを実行する行為自体が、Payloadを起動する可能性があります。Microsoftは、疑わしい環境内でPythonやpipを起動して存在確認しないよう注意しています。[^microsoft]

## 何が起きているのか

### 確認された影響Artifact

LiteLLMは次のArtifactを影響対象として公表しました。[^litellm-incident]

| 配布経路 | 影響対象 | 公表された時間帯（UTC） |
| --- | --- | --- |
| PyPI | `litellm==1.107.0`の全7 Wheel | 10月21日 11:39:51～13:23 |
| Docker Hub | `v1.107.0`、`latest`、`main-latest`、`main-stable` | 11:46:56～14:20 |
| GHCR | 同じ4 Tag | 11:46:56～13:51までに利用不能化 |

LiteLLMは、それ以前のVersionとPrivate Enterprise Releaseは影響を受けなかったと説明しています。これはMaintainerの公表内容であり、各組織は自環境のDigest、Cache、Mirror、Build Logで実際の取得状況を確認する必要があります。

### Python Startup Hookによる自動実行

Microsoftは、影響Wheel内で次の2経路を解析しました。[^microsoft]

- `.pth`によるPath Extension処理からCredential Collectorを起動
- `sitecustomize.py`を利用し、Unix系環境で追加Python Codeを取得・実行できるLoaderを常駐

Collectorは、Developer Credential、Cloud Credential、Browser Data、SSH Material、Environment Variable、LiteLLM Database内の一部情報を収集対象とし、暗号化して外部Endpointへ送信する処理を備えていました。MicrosoftはEndpoint上でCollectorの探索、暗号化、外部接続に合致する挙動を観測しています。一方、Unix向けLoaderによる追加Codeの取得・実行は、設計上の機能は確認されたものの、実行自体は確認されていないと区別しています。

### Maintainerが公表した攻撃Chain

LiteLLMの2026年10月23日版Canonical Reportは、次の経路を示しています。[^litellm-rca]

1. 5月27日、Internal Alpha ServiceのAdministrative KeyがPublic Repositoryの履歴へ残り、失効されなかった。
2. 10月10日、攻撃者がそのKeyでAgent Platform APIへAccessし、GitHub Organization OwnerのGitHub CLI OAuth Tokenを取得した。
3. Owner権限でInternal RepositoryにWorkflowを作り、別MaintainerのTokenやCI Secretを外部へ送信した。
4. Release WorkflowのSourceを正規Repositoryから類似名のForkへ変更し、Branch Protectionを無効化・回避した。
5. 盗まれた別Maintainer TokenでProduction Approval Gateを通過し、悪意ある1.107.0を署名・公開した。
6. Release Runの記録を削除し、Workflow HistoryをForce Pushで見えにくくした。

Microsoftは、最初のUpstream AccessとCredential取得経路を独立に確定したわけではないと明記しています。本稿では攻撃ChainをLiteLLM Maintainerの調査結果として扱い、MicrosoftのPayload解析・Endpoint観測と区別します。

## Attack / Process Flow

<div class="sil-flow" role="group" aria-label="LiteLLM supply chain compromise">
  <div class="sil-flow-step"><strong>公開履歴に残ったAgent Platform Admin Key</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>GitHub Organization Owner Token取得</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>CI Secret追加窃取・Release Workflow改変</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>類似名Forkから1.107.0をBuild・Publish</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Python Startup HookでCredential Collector自動実行</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Developer・Cloud・AI Gateway Credentialへ波及</strong></div>
</div>

<!-- AUTO:MITRE:START -->
## MITRE ATT&CK® Mapping

| Technique | Basis | Article context |
| --- | --- | --- |
| T1195.001 Compromise Software Dependencies and Development Tools | Source-labeled | Microsoftが悪意あるLiteLLM WheelとContainer Imageの配布を明示。 |
| T1546.018 Event Triggered Execution: Python Startup Hooks | Source-labeled | Microsoftが`cook.pth`と`sitecustomize.py`による自動実行を明示。 |

<!-- AUTO:MITRE:END -->

## 経営インパクト

| 観点 | 経営上の意味 |
| --- | --- |
| AI Platform | AI Gateway侵害がModel Provider、Database、Tenant Policyへ波及する |
| Developer Identity | Organization Owner TokenがRelease・Branch Protection・Approvalを横断する単一障害点になる |
| CI/CD Governance | Approval Gateが存在しても、承認Identity自体が盗まれると形式的Controlになる |
| Incident Response | Package削除だけでなく、Process、Environment、Credential、Downstream Accessの調査が必要 |
| Evidence | Workflow Log削除やForce Pushを前提に、Organization Audit Logを別経路で保持する必要がある |

## 日本企業への示唆

日本企業がLiteLLMを直接利用していなくても、AI PlatformやDeveloper Toolが同様に多数のSecretとRelease権限へ接続している可能性があります。重要なのは特定PackageのBlockだけでなく、**公開履歴に残るSecret、Owner Token、CI Secret、Production Approval、Artifact Provenance、Runtime Credentialを一つのTrust Chainとして管理すること**です。

特にGitHub Organization Owner等の広範なTokenをAgent PlatformやExperimental Serviceへ格納しないこと、Approvalを別Identity・別Control Planeで成立させること、Release SourceとArtifact Digestを検証することが重要です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. LiteLLM 1.107.0のWheel、Container Tag、Digest、Internal Mirror、Build Cacheの利用履歴を確認する。
2. 疑わしい環境ではPythonやpipを起動せず、隔離した外部手段でFile、Process、Network、Image Layerを調査する。
3. 影響環境をRebuildし、アクセス可能だったModel Provider、Cloud、GitHub、Database、SSH等のCredentialを失効・再発行する。
4. GitHub Organization Owner TokenをAgentやCIへ保存せず、Repository・Operation単位の短命Tokenへ分割する。
5. Release WorkflowのSource Repository、Commit、Artifact Digest、ProvenanceをPolicy Gateで検証する。
6. Production ApprovalをBuild Identityと分離し、承認Identityの盗用を検知する。
7. Organization Audit LogとRelease Evidenceを、削除可能なWorkflow Logとは別の保管先へ転送する。

</div>

## 用語解説

**Python Startup Hook**  
Python Interpreter起動時に読み込まれる`.pth`や`sitecustomize.py`等の仕組み。正当な環境設定にも使われますが、本件ではPayloadの自動起動へ悪用されました。

**Artifact Provenance**  
PackageやContainer Imageが、どのSource、Commit、Workflow、Builderから生成されたかを検証できる情報です。

## 関連記事

- [AI Infrastructureが攻撃対象へ ― LiteLLM・RAGFlow・Kestraが示すControl Plane Risk](https://peridotan.github.io/security-intelligence-library/ai-security/ai-infrastructure-control-plane-attacks/)
- [Mastra npm Supply Chain Compromise](https://peridotan.github.io/security-intelligence-library/cybersecurity/mastra-npm-ai-supply-chain/)
- [Axios Supply Chain Compromise](https://peridotan.github.io/security-intelligence-library/cybersecurity/openai-axios-signing-supply-chain/)
- [LangGrinch](https://peridotan.github.io/security-intelligence-library/ai-security/langgrinch-ai-application-supply-chain/)

## 参考情報

- [Microsoft Security Blog, Inside the LiteLLM 1.107.0 supply chain compromise](https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks/)
- [LiteLLM, The attack chain behind the v1.107.0 release](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)
- [LiteLLM, Contained: Oct 21, 2026 LiteLLM release v1.107.0 compromised](https://docs.litellm.ai/blog/security-incident-oct-21-2026)

[^microsoft]: [Microsoft Security Research, Inside the LiteLLM 1.107.0 supply chain compromise, 2026-10-23](https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks/)
[^litellm-rca]: [LiteLLM, The attack chain behind the v1.107.0 release, 2026-10-23](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)
[^litellm-incident]: [LiteLLM, Contained: Oct 21, 2026 LiteLLM release v1.107.0 compromised, 2026-10-21](https://docs.litellm.ai/blog/security-incident-oct-21-2026)

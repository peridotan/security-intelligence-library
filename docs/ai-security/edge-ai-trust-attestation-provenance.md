---
title: Edge AI Trust Model ― Attestation・Provenance・Deterministic Mediationで境界を作る
date: 2026-09-08
updated: 2026-09-08
reviewed: 2026-09-08
review_status: Current
source_period: 2026-09
description: Microsoft Security Researchが2026年9月4日に示したEdge AI Security Architectureを基に、Runtime
  Attestation、Artifact Provenance、Deterministic Mediation、Credential Releaseを整理する。
category: AI Security / Edge AI
collections:
- ai-security
- cybersecurity
- risk-management
topics:
- AI Infrastructure
- AI Agent Security
- Security Governance & Risk Management
tags:
- Microsoft
- Edge AI
- Runtime Attestation
- Artifact Provenance
- Deterministic Mediation
- Trust Model
- Customer-owned Environment
- OT
audience:
- Executive
- CISO
- AI Platform
- OT Security
management_impact: High
impact_types:
- AI Infrastructure
- OT Security
- Architecture
urgency: Strategic
evidence: Assessment
status: published
pptx: ''
media_rights: none
---

# Edge AI Trust Model ― Attestation・Provenance・Deterministic Mediationで境界を作る

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-09-08</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">September 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-09-08</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-09-08</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Edge AI</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Infrastructure / AI Agent Security / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Platform / OT Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Infrastructure / OT Security / Architecture</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Assessment</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoft Security Researchは2026年9月4日、Customer-owned Environmentで動く**Edge AI**のSecurity Architectureを整理しました。Edge AIではModel、Customer Data、Credential、System AuthorityがCloud Provider管理外のDevice / Local Infrastructureへ移るため、従来Cloud AIとはTrust Modelが変わるとしています。[^source]

提案の中心は、Model OutputをそのままAuthorizationに使わず**Deterministic Mediator**を通すこと、Runtime Attestationで実行環境を検証してからSensitive AssetをReleaseすること、Model / Configuration / Retrieval ArtifactのProvenanceを確認することです。

これはMicrosoftによるArchitecture Guidanceであり、標準や規制ではありません。しかし、Factory、Hospital、Vehicle、Edge Device等でAIがPhysical / Operational SystemへActionする場合の有用な設計Patternです。

</div>

## なぜ今なのか

AIがCloud ChatからEdge / OTへ移ると、LatencyやData Sovereigntyの利点がある一方、ModelとCredentialがPhysical Environmentに近づきます。Prompt Injectionだけでなく、Model Tampering、Malicious Firmware、Configuration Poisoning、Physical Access等を一つのTrust Modelで考える必要があります。

## 4つのTrust Control

| Control | 役割 |
| --- | --- |
| **Deterministic Mediation** | ModelはActionを提案し、Policy Engineが許可・拒否を決める |
| **Runtime Attestation** | Boot / Firmware / Runtimeが期待状態か確認する |
| **Artifact Provenance** | Model、Prompt、Tool、Retrieval Assetの出所・Integrityを確認する |
| **Conditional Asset Release** | Trust Evidenceが成立した時だけKey / Credential / Sensitive Dataを渡す |

## 経営インパクト

| 観点 | 経営上の意味 |
| --- | --- |
| OT / Safety | Model Outputを直接Physical Actionへつなげない |
| Credential | Verified EnvironmentだけへSecretをReleaseする |
| Supply Chain | Model / Firmware / ConfigのProvenanceが必要 |
| Lifecycle | Deploy後もAttestation / Leaseを更新し続ける設計が必要 |

## 日本企業への示唆

製造現場や店舗、医療、公共InfrastructureでEdge AIを使う場合、「Modelが安全か」より**そのModelを動かすDevice / Runtime / Artifact / Credentialを毎回信頼できるか**を設計すべきです。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Edge AIのModel / Device / Firmware / Tool / Data FlowをInventory化する
2. Safety-critical ActionをDeterministic Policy Engine経由にする
3. Credential ReleaseをAttestation Evidenceへ連動する
4. Model / Configuration / Retrieval ArtifactへSignature / Provenanceを要求する
5. Offline / Disconnected時のTrust Expiryを設計する
6. OT / Physical Safety TeamとAI Security Reviewを共同実施する

</div>

## 用語解説

**Runtime Attestation**  
DeviceやRuntimeが期待されたSoftware / Configurationで動いていることをCryptographic Evidence等で検証する仕組み。

**Deterministic Mediation**  
LLMの確率的判断だけでActionを許可せず、明示的なRule / Policy Engineが最終Authorizationを行う設計。

## 関連記事

- [AI生成スクリプトがPLC標的活動に登場](../cybersecurity/ai-generated-plc-attacks.md)
- [AI Infrastructureが攻撃対象へ](ai-infrastructure-control-plane-attacks.md)

## 参考情報

- [Microsoft Security Research, How to secure edge AI in customer-owned environments (2026-09-04)](https://www.microsoft.com/en-us/security/blog/2026/09/04/secure-edge-ai-customer-owned-environments/)

[^source]: [Microsoft Security Research, Secure edge AI (2026-09-04)](https://www.microsoft.com/en-us/security/blog/2026/09/04/secure-edge-ai-customer-owned-environments/)

---
title: Claude Mythos Preview ― AIのExploit Development能力が一段上がった4月
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-04
description: Anthropicが2026年4月7日に公表したClaude Mythos PreviewのCybersecurity評価を基に、Zero-day発見、Exploit
  Development、Project Glasswingと企業防御への意味を整理する。
category: AI Security / Cyber Capability
collections:
- ai-security
- cybersecurity
- risk-management
topics:
- AI Cyber Capability
- Vulnerability Management
- Security Governance & Risk Management
tags:
- Anthropic
- Claude Mythos Preview
- Project Glasswing
- Zero-day
- Exploit Development
- Frontier AI
- Vulnerability Discovery
audience:
- Executive
- CISO
- Product Security
- Vulnerability Management
management_impact: High
impact_types:
- AI Governance
- Vulnerability Risk
- Software Security
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# Claude Mythos Preview ― AIのExploit Development能力が一段上がった4月

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">April 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Cyber Capability</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Cyber Capability / Vulnerability Management / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Product Security / Vulnerability Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Vulnerability Risk / Software Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Anthropicは2026年4月7日、Claude Mythos PreviewのCybersecurity Capability評価を公表しました。同社の内部Testingでは、Zero-day Vulnerabilityの発見だけでなく、複数の脆弱性を組み合わせたExploit、Local Privilege Escalation、Remote Code Execution等を自律的に構築できたと報告しています。[^source]

特に重要なのは、前世代Modelではほぼ成功しなかったAutonomous Exploit Developmentが、Mythos Previewでは明確に進展したとAnthropic自身が評価した点です。一方、公開時点で同社が発見した脆弱性の99%以上は未Patchで、全結果を外部検証できる状態ではありませんでした。このため本Libraryでは、**Anthropicが自社評価で観測したCapability Leap**として扱います。

</div>

## なぜ今なのか

従来、AIによるVulnerability DiscoveryとExploit Developmentの間には大きな能力差があると考えられていました。Mythos Previewの報告は、その差が急速に縮まる可能性を示しています。

AnthropicはFreeBSD、OpenBSD、FFmpeg等について具体例を公表し、Project Glasswingを通じて重要Softwareを保守する組織へ限定的にModelを提供しました。

## 何が変わったのか

- Zero-day Vulnerabilityを自律的に探索
- VulnerabilityからExploit Primitiveを構築
- 複数のPrimitiveをEnd-to-End Exploitへ連結
- N-day VulnerabilityをWorking Exploitへ変換
- Human Expertが数週間必要と見積もる作業をHours単位で実施した例
- 大量Parallel Scanningによる探索Scaleの拡大

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Vulnerability Management | 「公開CVEを待って直す」運用の猶予が縮む可能性 |
| Product Security | Vendor自身がAIで自社Codeを先にScanする必要性が高まる |
| Patch Capacity | 発見速度よりValidation / Disclosure / Patch速度がBottleneckになる |
| AI Governance | 高度なCyber CapabilityへのAccess Controlが重要になる |

## 日本企業への示唆

企業がMythos級Modelを直接利用しなくても、Software Vendorや攻撃者が同等能力を使う前提でExposureを見直す必要があります。

Internet-facing、Identity、Remote Access、Critical Softwareは、脆弱性公開後に対応を始めるのではなく、Asset Inventory、Compensating Control、Emergency Patch Processまで事前に準備する方が安全です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Internet-facing / Identity / Critical Assetを優先Assetとして定義する
2. KEV・EPSS・Exposure・Business CriticalityをPatch Priorityへ統合する
3. Product Security TeamでAI-assisted Code Review / Vulnerability Discoveryを評価する
4. 大量Finding発生時のTriaging Processを準備する
5. Vendorの緊急Patch CapacityとDisclosure Processを確認する
6. Cyber Capabilityの高いAI ModelへAccess Tierを設定する

</div>

## 用語解説

**Exploit Development**  
脆弱性の存在を確認するだけでなく、実際にSecurity Controlを突破して任意Code実行等へつなげる攻撃手法を構築すること。

## 関連記事

- [Frontier AIのサイバー能力が「Critical」に近づく意味](frontier-ai-cyber-capabilities.md)
- [Project YATA-Shield](../regulation/japan-project-yata-shield.md)

## 参考情報

- [Anthropic, Assessing Claude Mythos Preview’s cybersecurity capabilities](https://www.anthropic.com/research/mythos-preview)
- [Anthropic, Project Glasswing](https://www.anthropic.com/project/glasswing)

[^source]: [Anthropic, Assessing Claude Mythos Preview’s cybersecurity capabilities](https://www.anthropic.com/research/mythos-preview)

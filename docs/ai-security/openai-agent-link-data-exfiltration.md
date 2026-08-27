---
title: AI Agent Link Safety ― URLそのものがData Exfiltration Channelになる
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-01
description: OpenAIが2026年1月28日に公開したAI AgentのURL-based Data Exfiltration対策を基に、Prompt
  Injection、Redirect、Public URL Verification、User Confirmationを整理する。
category: AI Security / Agent Security
collections:
- ai-security
- risk-management
topics:
- AI Agent Security
- AI Governance
tags:
- OpenAI
- AI Agent
- Prompt Injection
- URL Exfiltration
- Data Exfiltration
- Redirect
- Defense in Depth
audience:
- Executive
- CISO
- AI Platform
- Application Security
management_impact: High
impact_types:
- AI Governance
- Data Security
- Application Security
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# AI Agent Link Safety ― URLそのものがData Exfiltration Channelになる

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">January 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security / Agent Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI Agent Security / AI Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Platform / Application Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Data Security / Application Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

OpenAIは2026年1月28日、AI AgentがWeb Resourceを自動取得する際の**URL-based Data Exfiltration**対策を公開しました。[^source]

攻撃者はPrompt InjectionによってAgentへURLを生成・取得させ、そのQuery Parameter等へPrivate Dataを埋め込むことで、Chat上に機密情報を表示させなくても外部ServerへDataを送信させる可能性があります。

OpenAIは単純な「Trusted Domain Allowlist」ではRedirect等を悪用できるため不十分とし、**Conversationとは独立したWeb Indexで既にPublicに観測されたExact URLか**を基準にAutomatic Fetchを判断する設計を説明しています。

</div>

## なぜ今なのか

AgentがWeb Page、Image、Link PreviewをUserの代わりに自動取得するようになると、HTTP RequestそのものがData Movementになります。

## 攻撃イメージ

<div class="sil-flow" role="group" aria-label="URL-based data exfiltration flow">
  <div class="sil-flow-step"><strong>Untrusted Web Content</strong><span>Prompt Injection</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Agent creates / fetches URL</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Private Data embedded in URL</strong><span>Query / Path</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step sil-flow-step-impact"><strong>Attacker Server Log receives Data</strong></div>
</div>

## なぜDomain Allowlistだけでは足りないか

- Legitimate SiteでもExternal Redirectを持つ
- First Domainだけ見てもFinal Destinationを保証できない
- 過度なAllowlistはFalse Positiveを増やす
- UserがWarningに慣れて無視するRiskがある
- 「Domainの評判」より「Exact URLがPublicか」の方が強いSecurity Propertyになり得る

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| DLP | Chat Outputだけ監視してもData Leakを見逃す可能性 |
| Browser / Network | AgentのOutbound RequestもSecurity Control対象 |
| UX | User Confirmationをどこで要求するかが重要 |
| Architecture | Prompt Injection対策をNetwork / Product Controlと組み合わせる必要 |

## 日本企業への示唆

自社AgentでURL Fetch、Webhook、Image Load、HTTP Connectorを許可する場合、PayloadだけでなくDestinationとRequest Parameterを監視すべきです。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AgentのOutbound Network PathをInventory化する
2. URL / WebhookへSensitive Dataを埋め込ませない
3. Redirect後のDestinationまで検証する
4. Unverified DestinationにはUser Approvalを要求する
5. Egress LogをAgent Identityと関連付ける
6. Prompt InjectionをDefense-in-depthで扱う

</div>

## 用語解説

**URL-based Data Exfiltration**  
Sensitive DataをURLのPathやQuery Parameterへ埋め込み、そのURLをAgentやBrowserにRequestさせることで外部へ送信する手法。

## 関連記事

- [AutoJack](autojack-agent-localhost-rce.md)
- [AI Agent Runtime Defense](microsoft-agent-runtime-defense.md)

## 参考情報

- [OpenAI, Keeping your data safe when an AI agent clicks a link](https://openai.com/index/ai-agent-link-safety/)

[^source]: [OpenAI, AI agent link safety](https://openai.com/index/ai-agent-link-safety/)

---
title: ASCII Smuggling ― AI Prompt Injectionの技法がPhishing Evasionへ逆流した
date: 2026-09-08
updated: 2026-09-08
reviewed: 2026-09-08
review_status: Current
source_period: 2026-09
description: Microsoftが2026年9月3日に公表した大規模Phishing Campaignを基に、AI Prompt Injection研究で知られたInvisible
  Unicode Tag Characterが従来型Email Filter Evasionへ転用された事例を整理する。
category: Cybersecurity / Phishing
collections:
- cybersecurity
- identity-security
- ai-security
topics:
- Credential Attacks
- AI-Enabled Threats
- Identity Security
tags:
- Microsoft
- ASCII Smuggling
- Unicode Tags
- Phishing
- Prompt Injection
- Email Security
- Evasion
- Normalization
audience:
- Executive
- CISO
- SOC
- Messaging Security
management_impact: High
impact_types:
- Email Security
- Identity
- AI Security
urgency: Near-term
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# ASCII Smuggling ― AI Prompt Injectionの技法がPhishing Evasionへ逆流した

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-09-08</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">September 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-09-08</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-09-08</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / Phishing</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Credential Attacks / AI-Enabled Threats / Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / SOC / Messaging Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Email Security / Identity / AI Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoft Security Researchは2026年9月3日、AI Prompt Injection研究で注目された**ASCII Smuggling**の技法が、従来型PhishingのEmail Filter Evasionへ転用された大規模Campaignを報告しました。[^source]

攻撃者はUnicode Tags Block（U+E0000〜U+E007F）のInvisible Characterを金融系Keywordの途中に挿入し、人間には通常の単語として見せながら、単純なKeyword / Signature Parserには分断された文字列として処理させます。

Microsoft TelemetryではこのSignatureが2月9日から急増し、Peak時には1日200万件超の規模が観測されました。ただしMicrosoft Defenderでは99%以上が他のLayerも含む防御でFlagされており、「この手法でEmail Securityが全面的に回避された」という意味ではありません。

</div>

## なぜ今なのか

AI SecurityとTraditional Securityを別分野として見ると、研究されたEvasion Techniqueの転用を見落とします。ModelにInstructionを隠すために使われたCharacter Encodingが、今度はMail FilterからKeywordを隠す用途に使われました。

## 何が新しいのか

Invisible CharacterによるKeyword Fragmentation自体は新しくありません。今回の特徴は、

- AI Security研究で有名になったUnicode Tags Blockを利用
- Finance-themed Phishingで大規模利用
- Peak時にMulti-million Message / Day
- Weekday中心の規則的なSending Pattern
- Legitimate Marketing PlatformのInfrastructureも悪用

という点です。

## 経営インパクト

| 観点 | 経営上の意味 |
| --- | --- |
| Email Security | Visible TextだけでなくNormalization前後を検査する必要 |
| AI Security | Prompt Injection DetectionとMail Securityが共通Signalを持つ |
| SOC | Character Encodingを単独IOCではなくCampaign Patternと組み合わせる |
| Identity | Filter Evasionの最終目的はUser Action / Credential Theftにつながり得る |

## 日本企業への示唆

AI導入の有無に関係なく、Email / Web / Documentを処理するSecurity PipelineでInvisible UnicodeをどうNormalizeしているか確認する価値があります。同じNormalizationはAI AssistantがEmailやDocumentを読む場合のPrompt Injection対策にも役立ちます。

<div class="sil-action-box" markdown>

## 推奨アクション

1. U+E0000〜U+E007F等のInvisible UnicodeをNormalization対象にする
2. Keyword Match前にZero-width / Non-rendering Characterを処理する
3. Unicode Tag CharacterをAnomaly SignalとしてHuntする
4. Sender / Domain / URL / Volume / Cadenceと組み合わせて判定する
5. AI Ingestion Pipelineでも同じNormalizationを適用する
6. Mail GatewayがInvisible Unicodeをどう扱うかTest Caseを作る

</div>

## 用語解説

**ASCII Smuggling**  
Unicode Tags等のInvisible Characterを使い、人間に見えるTextとSoftwareが処理するRaw Textの差を悪用する手法。名称は研究Communityで広く使われる呼称。

## 関連記事

- [Domain Spoofing via Complex Routing](../identity-security/complex-routing-domain-spoofing.md)
- [AI as Tradecraft](ai-as-tradecraft-march-2026.md)

## 参考情報

- [Microsoft Security Research, ASCII smuggling crosses over from AI prompt injection to phishing evasion (2026-09-03)](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/)

[^source]: [Microsoft Security Research, ASCII smuggling phishing evasion (2026-09-03)](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/)

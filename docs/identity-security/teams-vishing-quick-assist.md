---
title: Teams Vishing ― 「IT Supportを信じる」ことがInitial Accessになる
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-03
description: Microsoft Incident Responseが2026年3月16日に公表したTeams Voice Phishing事例を基に、Quick
  Assist、正規Tool Abuse、Credential Theft、Session Hijackingを整理する。
category: Identity Security / Social Engineering
collections:
- identity-security
- cybersecurity
topics:
- Credential Attacks
- Identity Security
tags:
- Microsoft Teams
- Vishing
- Quick Assist
- Social Engineering
- Remote Access
- Identity-first Attack
mitre_attack:
- id: T1566.004
  basis: Analyst-mapped
  note: Microsoft TeamsのVoice CallでIT Supportを装い、利用者を操作したInitial Accessに対応。
- id: T1219.002
  basis: Analyst-mapped
  note: 被害者にQuick AssistでRemote Interactive Accessを許可させた正規Remote Desktop機能の悪用に対応。
audience:
- Executive
- CISO
- IAM
- SOC
- Helpdesk
management_impact: High
impact_types:
- Identity
- Social Engineering
- Endpoint
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# Teams Vishing ― 「IT Supportを信じる」ことがInitial Accessになる

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">March 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / Social Engineering</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Credential Attacks / Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / IAM / SOC / Helpdesk</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / Social Engineering / Endpoint</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoft Incident Responseは2026年3月16日、Microsoft TeamsのVoice PhishingでIT Supportを装ったThreat Actorが、被害者にQuick Assistを許可させて初期侵入した事例を公表しました。[^source]

この事例の重要点はZero-dayでもMalware Deliveryでもなく、**正規Collaboration Tool、正規Remote Support Tool、利用者のTrustをつないで侵入したこと**です。その後は偽Credential Page、Malicious MSI、C2、Credential Harvesting、Session Hijackingへ展開しました。

</div>

## なぜ今なのか

Email Securityが強くなるほど、攻撃者はTeams、Voice、Helpdesk、Remote Support等の「業務上信頼される経路」へ移ります。Security AwarenessをEmailだけに限定するとBlind Spotになります。

## 攻撃Flow

<div class="sil-flow" role="group" aria-label="Teams vishing attack flow">
  <div class="sil-flow-step"><strong>Teams Voice Call</strong><span>IT Supportを偽装</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Quick Assist許可</strong><span>正規Remote Support Tool</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>偽Credential Page</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>MSI / Loader / C2</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step sil-flow-step-impact"><strong>Credential Harvesting / Session Hijacking</strong></div>
</div>

<!-- AUTO:MITRE:START -->
## MITRE ATT&CK® Mapping

<div class="sil-mitre-note" markdown>

この表は、攻撃・Campaignの理解に有用な場合だけ表示します。`Source-labeled` は一次情報がATT&CK IDを明示したもの、`Analyst-mapped` は一次情報に記載された行動を本LibraryがATT&CKへ対応付けたものです。後者は、元情報の発行者がそのATT&CK IDを明示したことを意味しません。

</div>

| Technique | Tactic | Basis | Article context |
| --- | --- | --- | --- |
| [T1566.004 Spearphishing Voice](https://attack.mitre.org/techniques/T1566/004/) | Initial Access | Analyst-mapped | Microsoft TeamsのVoice CallでIT Supportを装い、利用者を操作したInitial Accessに対応。 |
| [T1219.002 Remote Desktop Software](https://attack.mitre.org/techniques/T1219/002/) | Command and Control | Analyst-mapped | 被害者にQuick AssistでRemote Interactive Accessを許可させた正規Remote Desktop機能の悪用に対応。 |

<div class="sil-mitre-legal">
MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation. © 2026 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation.
</div>
<!-- AUTO:MITRE:END -->

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Helpdesk | Support Process自体がHigh-risk Security Controlになる |
| Collaboration | Teams等をEmail外のPhishing Surfaceとして管理する必要 |
| Remote Tool | 正規ToolはAllowlistされやすくDetectionを回避しやすい |
| Identity | Endpoint侵入後の最終TargetはCredential / Sessionになりやすい |

## 日本企業への示唆

「社内ITから連絡が来たら従う」という業務習慣そのものを設計し直す必要があります。特にRemote Support開始時のIdentity Verificationと、外部Teams AccountからのContact Policyが重要です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. 外部Teams Communicationを必要最小限に制限する
2. Helpdeskの本人確認とCallback Processを標準化する
3. Quick Assist / RMM ToolをInventory化し不要なら無効化する
4. Remote Support開始時に別ChannelでVerificationする
5. Voice PhishingをAwareness / Tabletop Exerciseへ追加する
6. Remote Tool利用とIdentity RiskをSOCで相関する

</div>

## 用語解説

**Vishing**  
Voice（電話・音声Call）を使ったPhishing / Social Engineering。

## 関連記事

- [Large-Scale Credential Attacks](../cybersecurity/large-scale-credential-attacks.md)
- [Tycoon2FA](tycoon2fa-aitm-phaas.md)

## 参考情報

- [Microsoft Security Blog, Help on the line: How a Microsoft Teams support call led to compromise](https://www.microsoft.com/en-us/security/blog/2026/03/16/help-on-the-line-how-a-microsoft-teams-support-call-led-to-compromise/)

[^source]: [Microsoft Incident Response, Teams support call compromise](https://www.microsoft.com/en-us/security/blog/2026/03/16/help-on-the-line-how-a-microsoft-teams-support-call-led-to-compromise/)

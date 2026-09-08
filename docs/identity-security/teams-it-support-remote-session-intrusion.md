---
title: IT Support Impersonation ― Teamsの「信頼」がRemote SessionからDomain侵入へつながる
date: 2026-09-08
updated: 2026-09-08
reviewed: 2026-09-08
review_status: Current
source_period: 2026-09
description: Microsoftが2026年9月2日に報告したHuman-operated Intrusionを基に、Teams外部コラボレーション、IT
  Support偽装、RMM、Node.js Implant、AD Recon、WinRM横展開をIdentity Trustの観点で整理する。
category: Identity Security / Social Engineering
collections:
- identity-security
- cybersecurity
- risk-management
topics:
- Identity Security
- Credential Attacks
- Security Governance & Risk Management
tags:
- Microsoft
- Teams
- IT Support Impersonation
- Social Engineering
- RMM
- Node.js
- Active Directory
- WinRM
- Helpdesk Trust
audience:
- Executive
- CISO
- IAM
- SOC
management_impact: High
impact_types:
- Identity
- Social Engineering
- Lateral Movement
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# IT Support Impersonation ― Teamsの「信頼」がRemote SessionからDomain侵入へつながる

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-09-08</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">September 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-09-08</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-09-08</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / Social Engineering</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Identity Security / Credential Attacks / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / IAM / SOC</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / Social Engineering / Lateral Movement</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoft Threat Intelligenceは2026年9月2日、Microsoft TeamsのExternal Collaborationを悪用してIT / Helpdesk担当者を装い、User自身にInteractive Remote Sessionを許可させるHuman-operated Intrusion Campaignを報告しました。[^source]

Remote Management ToolでControlを得た後、攻撃者はPowerShellからMalicious MSIをInstallし、Portable Node.js RuntimeとObfuscated JavaScript Implantを展開。さらにHost / Active Directory Reconnaissanceを行い、WinRMでDomain Controller等のHigh-value Assetへ横展開を試みています。

これはTeamsの脆弱性ではありません。**正規Collaboration機能・Remote Support Tool・Userの「IT Supportを信じる」判断をつないだTrust Attack**です。

</div>

## なぜ今なのか

Email Phishingへの警戒が高まるほど、攻撃者はTeams、Voice、Remote Supportなど「業務上ふつうに使う信頼Channel」へ移ります。Identity SecurityはLogin画面だけでなく、Userが誰をSupport Personnelとして信頼するかまで広がっています。

## 攻撃Chain

<div class="sil-flow" role="group" aria-label="Teams IT support impersonation attack flow">
  <div class="sil-flow-step"><strong>External Teams Contact</strong><span>IT / Helpdeskを偽装</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>User grants Remote Session</strong><span>Legitimate RMM Tool</span></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>PowerShell → MSI → Node.js Implant</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Host / Active Directory Recon</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step sil-flow-step-impact"><strong>WinRM Lateral Movement → High-value Assets</strong></div>
</div>

## 経営インパクト

| 観点 | 経営上の意味 |
| --- | --- |
| Identity | Authenticatorが強くてもUser-approved Remote Accessで回避され得る |
| Collaboration | Teams External Accessが新しいInitial-contact Surfaceになる |
| Remote Support | RMM Toolを誰が起動・承認できるかがSecurity Controlになる |
| Helpdesk | Support IdentityをUserが検証できる仕組みが必要 |
| SOC | 正規Toolの連鎖をBehaviorで検知する必要 |

## 日本企業への示唆

「社員教育を強化する」だけでは不十分です。正規HelpdeskのContact Methodを固定し、External Teams ContactからRemote Toolを起動するFlowをPolicyで禁止・警告するなど、User判断だけに依存しないControlが必要です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Helpdesk / IT Supportの正規Contact Channelを明文化する
2. External Teams UserのLabel / Warningを教育と連動する
3. Remote Support ToolのAllowlist / Execution Controlを導入する
4. Support Session開始時にOut-of-band Verificationを要求する
5. Node.js / MSI / PowerShellの不自然な連鎖をDetection Use Caseへ追加する
6. Teams → RMM → AD Reconを含むIncident Exerciseを実施する

</div>

## 用語解説

**Trust Attack**  
技術的な認証突破より、正規Channel・正規Tool・組織上の役割への信頼を悪用してAccessやActionを得る攻撃。

## 関連記事

- [Teams Vishing](teams-vishing-quick-assist.md)
- [ShinyHunters型SaaS Data Theft](shinyhunters-saas-data-theft.md)

## 参考情報

- [Microsoft Security Research, Impersonating IT support: how threat actors turn a remote session into enterprise-wide access (2026-09-02)](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)

[^source]: [Microsoft Security Research, IT support impersonation campaign (2026-09-02)](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)

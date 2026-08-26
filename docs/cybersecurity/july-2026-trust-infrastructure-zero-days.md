---
title: 2026年7月の実悪用Zero-day ― AD FS / SharePointから見る「Trust Infrastructure」の守り方
date: 2026-08-26
updated: 2026-08-26
reviewed: '2026-08-26'
review_status: Current
source_period: 2026-07
description: MicrosoftとIPAが2026年7月に確認したAD FSおよびSharePointの実悪用脆弱性を、Patch Tuesdayの件数ではなくTrust
  Infrastructureの優先順位で整理する。
category: Cybersecurity / Identity
collections:
- cybersecurity
- identity-security
topics:
- Vulnerability Management
- Identity Security
tags:
- AD FS
- SharePoint
- Zero-day
- Vulnerability Management
audience:
- Executive
- CISO
- IAM
- Infrastructure
management_impact: High
impact_types:
- Identity
- Business Continuity
urgency: Immediate
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---
# 2026年7月の実悪用Zero-day ― AD FS / SharePointから見る「Trust Infrastructure」の守り方

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">July 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / Identity</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Vulnerability Management / Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / IAM / Infrastructure</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / Business Continuity</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoftは2026年7月のSecurity Updateで、CVE-2026-56155（AD FS）とCVE-2026-56164（SharePoint Server）がPatch公開前から実際に悪用されていたことを公表しました。IPAも日本企業へ至急のUpdate適用を呼びかけています。[^source]

注目すべきはPatch件数の多さではありません。AD FSはToken Signing等のIdentity Trust、SharePointはBusiness Content / Collaborationへ深く接続します。**侵害時のBlast Radiusが大きい基盤を最優先で守る**必要があります。

</div>

## なぜ今なのか

7月Updateでは多数のCVEが公開されましたが、企業がすべてを同じUrgencyで扱うことはできません。

優先順位はCVSSや件数だけでなく、

- Active Exploitation
- Internet Exposure
- Privilege / Trust
- Asset Criticality
- Compensating Control
- Recovery Difficulty

で判断すべきです。

## AD FSで何が問題だったか

MicrosoftのSupport情報では、AD FSがToken Signing / Token Encryption CertificateのPrivate Key保護に利用するDistributed Key Manager（DKM）ContainerのACLが過度に広い場合、DKM Key Materialを読める攻撃者がToken Signing Private Keyを復号できる可能性が説明されています。

Microsoftは7月からAudit Modeを開始し、今後さらにHardeningを進める計画を示しています。

これは単なるServer EoPではなく、**Identity Trust InfrastructureのKey Material保護**として扱うべき問題です。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Identity Trust | Token Signing Key侵害は認証基盤全体の信頼へ影響 |
| Collaboration | SharePoint侵害は情報漏えい・横展開へつながり得る |
| Patch Priority | 「件数」より実悪用 × 重要Assetで優先する必要 |
| Legacy Risk | On-prem Identity / Collaboration基盤の残存Riskが顕在化 |

## 日本企業への示唆

Cloud移行済みでも、AD FSやOn-prem SharePointが例外用途・Legacy System連携のため残っている企業があります。

「主システムではない」ため監視やPatchが弱くなっているLegacy Trust Infrastructureこそ、攻撃者にとって有効な入口になる可能性があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AD FS / SharePointの利用有無とExposureを緊急棚卸しする
2. 7月以降のSecurity Update適用状況を確認する
3. AD FS DKM ACL Audit Eventを確認する
4. Token Signing / Encryption Keyの保護・Rotation手順を確認する
5. Legacy Federationの廃止計画を再評価する
6. Vulnerability PriorityにKEV / Exploitation / Asset Criticalityを組み込む

</div>

## 用語解説

**AD FS (Active Directory Federation Services)**  
MicrosoftのFederation / SSO基盤。Token Signing等のTrust機能を提供します。

**DKM (Distributed Key Manager)**  
AD FS等が秘密情報を保護するためにActive Directory内で利用する仕組み。

## 関連記事

- [脆弱性悪用の猶予は48時間以下へ](exploitation-window-48-hours.md)
- [Large-Scale Credential Attacks](large-scale-credential-attacks.md)

## 参考情報

- [Microsoft, 2026年7月のセキュリティ更新プログラム](https://www.microsoft.com/en-us/msrc/blog/2026/07/202607-security-update)
- [Microsoft Support, CVE-2026-56155 AD FS DKM container ACL hardening](https://support.microsoft.com/ja-JP/servicing/os/windows/docs/2026/07/kb5121391-cve-2026-56155-ad-fs-dkm-container-acl-hardening)
- [IPA, Microsoft製品の脆弱性対策について（2026年7月）](https://www.ipa.go.jp/security/security-alert/2026/0715-ms.html)

[^source]: [Microsoft, 2026年7月のセキュリティ更新プログラム](https://www.microsoft.com/en-us/msrc/blog/2026/07/202607-security-update)

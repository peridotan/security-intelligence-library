---
title: AI生成スクリプトがPLC標的活動に登場 ― OT/ICSセキュリティの転換点
date: 2026-08-26
updated: 2026-08-26
reviewed: '2026-08-26'
review_status: Current
source_period: 2026-08
description: Siemens S7 PLCを狙うAI生成の悪用スクリプトに関する共同警告から、OT/ICS防御への示唆を整理する。
category: Cybersecurity
collections:
- cybersecurity
- risk-management
topics:
- AI-enabled Threats
- OT / Critical Infrastructure
tags:
- OT Security
- ICS
- PLC
- AI
- Critical Infrastructure
audience:
- Executive
- CISO
- OT Security
management_impact: High
impact_types:
- Business Continuity
- OT / Safety
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---
# AI生成スクリプトがPLC標的活動に登場 ― OT/ICSセキュリティの転換点

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">August 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI-enabled Threats / OT / Critical Infrastructure</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / OT Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Business Continuity / OT / Safety</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NSAなどの米政府機関は2026年8月19日、米国内のSiemens S7 Series PLCを対象とした**偵察・能力開発にAI生成の悪用スクリプトが使われている**と警告しました。スクリプトは正規の監視ツールを装う形で利用され、製造、エネルギー、水、化学、食品など複数の重要分野が対象とされています。[^source]

一次情報が示しているのは、AIによる大規模な物理破壊が成功したという話ではありません。重要なのは、従来は専門知識が必要だったPLC向けの探索・スクリプト作成をAIが補助し、**OTを狙う攻撃準備のコストと速度が変わり得る**ことです。

</div>

## なぜ今なのか

OT/ICSは可用性・安全性を優先するため、長寿命機器、更新制約、独自プロトコル、遠隔保守など、ITとは異なる条件を持ちます。ここへAIによるコード生成と探索支援が加わると、「高度なOT専門家だけが扱えた攻撃手法」の一部が再利用しやすくなる可能性があります。

NSAの警告はSiemens S7に焦点を当てていますが、同機関は**PLC標的活動はより広い**と明記しています。したがって特定メーカーだけの問題として扱うべきではありません。

## 確認された事実と、まだ言えないこと

### 確認された事実

- 米国のSiemens PLCに対する標的型偵察・能力開発が行われている。
- AI生成の悪用スクリプトが使われている。
- スクリプトは正規の監視ツールを装っている。
- 対象分野には重要製造、エネルギー、水・下水、化学、食品・農業、商業施設が含まれる。
- 政府機関はPatch、Internet Isolation、Strong Access Control、Monitoringを推奨している。

### この警告だけでは言えないこと

- AI Agentが完全自律でPLCを破壊した。
- Siemens S7自体が一律に侵害された。
- AIがなければ実行不可能な攻撃だった。

この区別は重要です。**AIを強調しすぎると、Internet露出やAccess Controlといった本質的な弱点を見失います。**

## OTでAIが変える可能性のある工程

```text
Asset Discovery
      ↓
Protocol / Product Research
      ↓
Script Generation & Adaptation
      ↓
Reconnaissance
      ↓
Access / Manipulation Attempt
      ↓
Physical Process Impact
```

AIの影響がまず出やすいのは、前半の調査、コード作成、試行錯誤です。物理プロセスへの安全な操作・破壊には依然として設備固有の理解が必要ですが、**入口までの工数が下がるだけでも防御側の負担は増えます。**

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Safety | IT障害ではなく人身・設備安全へ波及し得る |
| Availability | 工場・エネルギー・水処理の停止は復旧が長期化しやすい |
| Legacy | 更新できないPLCが長期間残る |
| Remote Access | 保守経路が攻撃経路になり得る |
| Governance | ITとOTで責任・監視が分断されると初動が遅れる |

## 日本企業への示唆

日本の製造業・社会インフラでは、PLCや制御機器を「閉域だから安全」と仮定しないことが重要です。保守VPN、Engineering Workstation、Jump Server、クラウド監視、委託先接続を通じて、実際には外部経路が存在するケースがあります。

また、パッチを即適用できないOTでは、**Internet非公開、Zone分離、Allowlist、強い認証、異常通信監視、Engineering操作監査**などの補完統制がより重要になります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. **PLC / Engineering Workstation / Remote Accessを資産化する** — 型番、Firmware、接続経路、Ownerを把握する。
2. **Internet到達性をゼロベースで確認する** — 直接だけでなくVPN、Cloud Gateway、委託先経路を含める。
3. **OT Remote Accessを強化する** — MFA、PAM、時間制限、Session Recording、承認を適用する。
4. **IT/OT境界を監視する** — PLCプロトコル、異常なEngineering操作、外向き通信を検知する。
5. **停止シナリオを演習する** — Cyber IncidentとSafety / BCPを別々にせず、現場・設備・経営を含めて復旧手順を確認する。

</div>

## 好意的・批判的に見ると

**深刻に見るべき点**は、AIがOT攻撃の調査・コード作成を支援し、攻撃能力の裾野を広げる可能性です。

**冷静に見るべき点**は、今回の警告が「AIが自律的に工場を破壊した」という事実を示していないことです。対策の中心は、AI専用防御よりも、まずInternet Isolation、Access Control、MonitoringなどOTの基本統制です。

## 用語解説

**PLC (Programmable Logic Controller)**  
工場やインフラ設備の制御に使われる産業用コントローラ。

**ICS (Industrial Control System)**  
産業プロセスを監視・制御するシステムの総称。

## 関連記事

- [脆弱性悪用の猶予は48時間以下へ](exploitation-window-48-hours.md)
- [重要インフラのサイバーセキュリティが「統一基準」へ](../regulation/japan-critical-infrastructure-unified-standard.md)


## 参考情報

- [NSA, NSA and Others Release Report on Active Threats of Programmable Logic Controllers (2026-08-19)](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4578318/nsa-and-others-release-report-on-active-threats-of-programmable-logic-controlle/)
- [NSA, Cybersecurity Advisories & Guidance](https://www.nsa.gov/Cybersecurity/Cybersecurity-Advisories-Guidance/)
[^source]: [NSA, NSA and Others Release Report on Active Threats of Programmable Logic Controllers (2026-08-19)](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4578318/nsa-and-others-release-report-on-active-threats-of-programmable-logic-controlle/)
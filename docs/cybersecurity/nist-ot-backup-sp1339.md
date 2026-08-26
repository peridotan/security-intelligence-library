---
title: NIST SP 1339 ― OT Backupは「取得」ではなくChange ManagementとRecovery Exerciseで守る
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-06
description: 2026年6月にNIST NCCoEが公開したOT Backup Quick Start Guide SP 1339を基に、製造・重要インフラのBackup運用を整理する。
category: Cybersecurity / OT
collections:
- cybersecurity
- risk-management
tags:
- NIST
- OT Security
- Backup
- Recovery
- Manufacturing
audience:
- Executive
- CISO
- OT Security
- BCP
management_impact: High
impact_types:
- Business Continuity
- OT / Safety
- Operational Security
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# NIST SP 1339 ― OT Backupは「取得」ではなくChange ManagementとRecovery Exerciseで守る

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">June 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / OT</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / OT Security / BCP</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Business Continuity / OT / Safety / Operational Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NIST NCCoEは2026年6月17日、SP 1339「Operational Technology Backup Quick Start Guide」を公開しました。GuideはOT Backupを、定期取得だけでなく**Change Managementへの統合、定期的な作成、Restore Test、Recovery ExerciseでのReview**まで含むManagement Practiceとして整理しています。[^source]

OTではRecovery失敗が長期生産停止、Financial Loss、Safety Incidentへつながるため、「Backupがある」というInventory確認では不十分です。

</div>

## なぜ今なのか

IT Systemと違い、OTはLegacy Device、Vendor Tool、特殊設定、PLC Logic、Engineering Workstation、Firmware等が混在します。復旧に必要なArtifactが何か分からないままBackup製品だけ導入しても、Incident時に復元できない可能性があります。

## 何が起きているのか

NIST SP 1339は短いQuick Start Guideですが、BackupをChange Managementへ組み込む点が重要です。設定変更やEquipment更新時にBackupを更新し、実際にRecovery Exerciseで使えるか検証することで、Backupを「保管Data」から「復旧能力」へ変えます。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Downtime | Restore不能が生産停止時間を直接延ばす |
| Safety | 誤った設定・Version復元がSafety Riskになり得る |
| Asset Knowledge | 何をBackupすべきか把握すること自体がAsset Managementになる |
| Recovery Assurance | Backup成功率ではなくRestore成功率をKPIにすべき |

## 日本企業への示唆

製造業ではBackup担当と設備保全担当が分かれている場合があります。PLC Logic、HMI、Historian、Network Device、Engineering Tool、License等を設備変更Processと連動して保全し、Cyber Incidentだけでなく故障・誤操作を含む復旧演習へ利用することが重要です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. OT Assetごとに復旧に必要なArtifactを定義する
2. 設備変更時にBackup更新を必須化する
3. Offline / Immutable Copyを検討する
4. Restore Testを定期実施する
5. Recovery ExerciseへOT Vendor / 保全担当を参加させる
6. RTO / RPOをBusiness Impactと接続する

</div>

## 用語解説

**OT (Operational Technology)**  
製造設備、PLC、SCADA等、物理Processを監視・制御するSystem。

**Restore Test**  
Backup Dataを実際に復元し、利用可能か検証するTest。

## 関連記事

- [AI生成スクリプトがPLC標的活動に登場](ai-generated-plc-attacks.md)
- [重要インフラの統一基準](../regulation/japan-critical-infrastructure-unified-standard.md)

## 参考情報

- [NIST SP 1339, OT Backup Quick Start Guide](https://www.nist.gov/publications/ot-backup-quick-start-guide)

[^source]: [NIST SP 1339, OT Backup Quick Start Guide](https://www.nist.gov/publications/ot-backup-quick-start-guide)

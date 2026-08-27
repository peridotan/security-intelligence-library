---
title: JADEPUFFER ― Agentic Ransomwareが「実験」から攻撃オペレーションへ
date: 2026-08-26
updated: 2026-08-26
reviewed: '2026-08-26'
review_status: Current
source_period: 2026-07
description: Sysdigが2026年7月に報告したJADEPUFFERを基に、AI Agentが偵察・資格情報探索・横展開・恐喝を適応的に連鎖させるリスクを整理する。
category: Cybersecurity / AI Security
collections:
- cybersecurity
- ai-security
topics:
- AI-Enabled Threats
- AI Agent Security
- Ransomware & Resilience
tags:
- Agentic AI
- Ransomware
- Langflow
- Security for AI
mitre_attack:
- id: T1190
  basis: Analyst-mapped
  note: Internet-facing LangflowのCVE-2025-3248悪用によるInitial Accessに対応。
- id: T1485
  basis: Analyst-mapped
  note: Production DatabaseやAI / ML Assetの破壊・削除に対応。
- id: T1486
  basis: Analyst-mapped
  note: Database暗号化およびENCFORGEによるAI / ML File暗号化に対応。
- id: T1657
  basis: Analyst-mapped
  note: Ransom / Extortionを金銭目的のImpactとして整理。
audience:
- Executive
- CISO
- SOC
- AI Platform
management_impact: High
impact_types:
- Business Continuity
- AI Security
- Credential Risk
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---
# JADEPUFFER ― Agentic Ransomwareが「実験」から攻撃オペレーションへ

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">July 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / AI Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">AI-Enabled Threats / AI Agent Security / Ransomware &amp; Resilience</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / SOC / AI Platform</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Business Continuity / AI Security / Credential Risk</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Sysdig Threat Research Teamは2026年7月、インターネット公開されたLangflowを入口として、偵察、資格情報探索、横展開、データベースへの破壊的な恐喝処理をAI Agentが適応的に連鎖させた活動を「JADEPUFFER」として報告しました。Sysdigは、完全な恐喝オペレーションをLLMがエンドツーエンドで駆動した初の文書化事例と評価しています。[^source]

重要なのは「AIが新しい脆弱性を生んだ」ことではありません。既知の脆弱性、過剰公開されたAI開発基盤、保存されたAPIキーやCloud Credential、弱い認証設定といった既存の弱点を、**AIが高速かつ適応的に連結できる**ことです。

</div>

## なぜ今なのか

従来の自動化攻撃は、事前に定義された手順やスクリプトに依存することが中心でした。JADEPUFFERでは、失敗した操作の原因を推測して短時間で別手順へ切り替えるなど、Plan → Act → Observe → Adjust型の挙動が観測されています。

さらにSysdigは7月後半、同活動がAI/ML資産を狙う専用ランサムウェアへ発展したと報告しました。AI基盤は、モデル、Vector DB、学習データ、Embedding、Cloud/API Credentialなどを集約するため、高価値な攻撃面になり得ます。

## 何が起きているのか

攻撃チェーンは概念的に次のように整理できます。

1. インターネット公開されたAI開発・ワークフロー基盤を探索
2. 既知脆弱性を利用して初期アクセス
3. RuntimeやBacking StoreからCredentialや設定を探索
4. 下流のDatabase / Configuration Serviceへ横展開
5. 失敗に応じて攻撃手順を修正
6. 暗号化・削除・恐喝へ移行

ここでの防御上のポイントは、LLM固有のPrompt Injection対策だけではありません。**AI基盤を通常の高権限アプリケーション基盤として扱うこと**が必要です。

<!-- AUTO:MITRE:START -->
## MITRE ATT&CK® Mapping

<div class="sil-mitre-note" markdown>

この表は、攻撃・Campaignの理解に有用な場合だけ表示します。`Source-labeled` は一次情報がATT&CK IDを明示したもの、`Analyst-mapped` は一次情報に記載された行動を本LibraryがATT&CKへ対応付けたものです。後者は、元情報の発行者がそのATT&CK IDを明示したことを意味しません。

</div>

| Technique | Tactic | Basis | Article context |
| --- | --- | --- | --- |
| [T1190 Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | Initial Access | Analyst-mapped | Internet-facing LangflowのCVE-2025-3248悪用によるInitial Accessに対応。 |
| [T1485 Data Destruction](https://attack.mitre.org/techniques/T1485/) | Impact | Analyst-mapped | Production DatabaseやAI / ML Assetの破壊・削除に対応。 |
| [T1486 Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486/) | Impact | Analyst-mapped | Database暗号化およびENCFORGEによるAI / ML File暗号化に対応。 |
| [T1657 Financial Theft](https://attack.mitre.org/techniques/T1657/) | Impact | Analyst-mapped | Ransom / Extortionを金銭目的のImpactとして整理。 |

<div class="sil-mitre-legal">
MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation. © 2026 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation.
</div>
<!-- AUTO:MITRE:END -->

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Attack Speed | 人手での判断待ちが減り、侵入後の展開速度が上がる可能性 |
| Credential Risk | AI基盤に集約されたAPI Key / Cloud Credentialが横展開に使われる |
| Business Continuity | DatabaseやAI Model資産の破壊が復旧時間と再構築コストを増大 |
| Detection | 固定IOCだけではなく、Runtime上の不自然な探索・適応挙動の検知が必要 |

## 日本企業への示唆

PoCや部門導入で構築したLangflow等のAI基盤が、企業の通常のAsset Inventoryや脆弱性管理から外れていないか確認が必要です。

特に「検証環境だから」という理由でInternet公開、共有Credential、長寿命API Key、広いCloud権限を許容すると、AI基盤が既存システムへの踏み台になります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AI/Agent開発基盤を正式なAsset Inventoryへ登録する
2. Internet公開の有無と既知脆弱性を継続監視する
3. API Key / Cloud Credentialを短命化・最小権限化する
4. AI基盤から本番DatabaseやControl Planeへの経路を分離する
5. Runtimeで探索・Credential Access・横展開を検知する
6. Model / Dataset / Vector DBをBackup・Recovery対象として定義する

</div>

## 用語解説

**Agentic Threat Actor (ATA)**  
攻撃手順の選択や修正をAI Agentが自律的・適応的に行う脅威活動を表す用語。現時点では業界共通の厳密な標準用語ではなく、Sysdig等の研究で用いられています。

**Langflow**  
LLMやAI Agentのワークフローを構築するためのオープンソース基盤。

## 関連記事

- [Agentic AIの安全設計](../ai-security/agentic-ai-security-controls.md)
- [AI Enabled Malwareの現実](../ai-security/ai-enabled-malware-reality.md)

## 参考情報

- [Sysdig, JADEPUFFER: Agentic ransomware for automated database extortion](https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion)
- [Sysdig, JADEPUFFER evolves](https://www.sysdig.com/blog/jadepuffer-evolves-the-agentic-threat-actor-deploys-ransomware-built-to-destroy-ai-models)

[^source]: [Sysdig, JADEPUFFER: Agentic ransomware for automated database extortion](https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion)

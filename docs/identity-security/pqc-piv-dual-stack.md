---
title: NIST PIVのPQC対応 ― Identity Credentialも「Crypto Agility」が必要になる
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-06
description: 2026年6月にNISTが公開したPIV StandardsのPQC Working Draftを基に、ML-DSA / ML-KEM導入とClassical/PQC
  Dual-stack移行の意味を整理する。
category: Identity Security / Post-Quantum Cryptography
collections:
- identity-security
- risk-management
tags:
- PQC
- PIV
- NIST
- Crypto Agility
- Digital Identity
audience:
- Executive
- CISO
- IAM
- PKI
management_impact: High
impact_types:
- Identity
- Strategic Risk
- Cryptography
urgency: Strategic
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# NIST PIVのPQC対応 ― Identity Credentialも「Crypto Agility」が必要になる

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">June 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security / Post-Quantum Cryptography</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / IAM / PKI</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / Strategic Risk / Cryptography</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NISTは2026年6月12日、Personal Identity Verification（PIV）StandardsへPost-Quantum Cryptographyを組み込むWorking Draftを公開しました。検討対象にはML-DSAによるDigital Signature、ML-KEMによるKey Encapsulationが含まれ、既存Classical Credentialを維持しながらPQC用Key Reference / Certificate Container等を追加するDual-stack Approachが示されています。[^source]

これは米国政府PIV固有の仕様変更である一方、企業にとっては**Identity CredentialやPKIもPQC Migrationの対象であり、Applicationだけ暗号移行しても終わらない**ことを示します。

</div>

## なぜ今なのか

Certificate、Smart Card、Device Credentialは長期間利用され、Reader、Middleware、CA、Applicationなど多くのDependencyを持ちます。PQC Algorithmへ一括切替するのは難しく、Backward Compatibilityと段階移行を前提としたCrypto Agilityが必要です。

## 何が起きているのか

NISTのWorking DraftはSP 800-73 Part 1/2とSP 800-78を対象に、PIV Algorithm Profile、Command Interface、Data ModelのGapを整理しています。現時点では正式Public Draft前のWorking Materialですが、Identity CredentialのPQC移行が実装Levelへ入り始めたことが重要です。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Identity Lifecycle | Credential発行・更新・失効・Reader対応まで移行が必要 |
| Interoperability | Classical / PQC双方を扱う期間が長くなる可能性 |
| Inventory | Certificate / Algorithm / Device Dependencyの把握が前提 |
| Long-term Risk | 長寿命Credentialや署名Dataは早期にMigration Planningが必要 |

## 日本企業への示唆

企業PKIでは、TLS CertificateだけでなくClient Certificate、Smart Card、Code Signing、Document Signing、Device Identity、VPN認証をInventory化する必要があります。PQC対応製品の購入だけでなく、Algorithmを変更できるArchitectureを設計することが重要です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. PKI / Certificate / Algorithm Inventoryを作る
2. 長寿命CredentialのUse Caseを分類する
3. PQC非対応Device / Middlewareを特定する
4. Classical/PQC Dual-stackのPilotを検討する
5. Vendor RoadmapへPQC対応時期を確認する
6. Crypto Agilityを調達要件へ入れる

</div>

## 用語解説

**PIV (Personal Identity Verification)**  
米国連邦政府職員・Contractor向けIdentity Credentialの標準。

**Crypto Agility**  
AlgorithmやKey Sizeを大規模なSystem改修なしに変更・移行できる能力。

## 関連記事

- [AI Agent Identity / NHI](ai-agent-identity-nhi.md)

## 参考情報

- [NIST, Working Drafts: Post-Quantum Cryptography Updates to the PIV Standards](https://www.nist.gov/news-events/news/2026/06/working-drafts-post-quantum-cryptography-updates-piv-standards)

[^source]: [NIST, Working Drafts: Post-Quantum Cryptography Updates to the PIV Standards](https://www.nist.gov/news-events/news/2026/06/working-drafts-post-quantum-cryptography-updates-piv-standards)

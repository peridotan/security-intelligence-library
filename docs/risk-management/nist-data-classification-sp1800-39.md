---
title: NIST SP 1800-39 Draft ― Zero Trust・PQC・Secure AIの前に「Dataを見つけて分類する」
date: 2026-08-27
updated: 2026-08-27
reviewed: 2026-08-27
review_status: Current
source_period: 2026-02
description: NISTが2026年2月12日に公開したSP 1800-39 Draftを基に、Unstructured DataのDiscovery /
  ClassificationがZero Trust、Quantum-safe Cryptography、Secure AI Trainingの基礎になる理由を整理する。
category: Risk Management / Data Security
collections:
- risk-management
- cybersecurity
- ai-security
topics:
- Security Governance & Risk Management
- AI Governance
- PQC / Crypto Agility
tags:
- NIST
- SP 1800-39
- Data Classification
- Unstructured Data
- Zero Trust
- Quantum-safe Cryptography
- Secure AI Training
audience:
- Executive
- CISO
- Data Governance
- AI Governance
management_impact: High
impact_types:
- Data Security
- AI Governance
- Cryptography
urgency: Near-term
evidence: Confirmed
status: published
pptx: ''
media_rights: none
---

# NIST SP 1800-39 Draft ― Zero Trust・PQC・Secure AIの前に「Dataを見つけて分類する」

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">February 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-27</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Risk Management / Data Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Security Governance &amp; Risk Management / AI Governance / PQC / Crypto Agility</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Data Governance / AI Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Data Security / AI Governance / Cryptography</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

NISTは2026年2月12日、Data Classification Practicesを扱うSP 1800-39 Draftを公開しました。[^source]

Guidanceは、File Repository、Email、Data Lake等に散在するSensitive Unstructured DataをDiscover・Identify・Labelする実装を示し、Data Classificationを**Zero Trust Architecture、Quantum-safe Cryptography、Secure AI Model Trainingへ進むための初期Step**として位置づけています。

</div>

## なぜ今なのか

AI、PQC、Zero Trustはいずれも「何を守るか」が分からなければ適切に適用できません。Data Inventoryが曖昧なままでは、Encryption Migration、AI Training Data Control、Access PolicyのScopeを決められません。

## Data Classificationの位置づけ

<div class="sil-flow" role="group" aria-label="Data classification foundation flow">
  <div class="sil-flow-step"><strong>Discover Data</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Identify Sensitive Data</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Classify / Label</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-branches">
    <div class="sil-flow-step"><strong>Zero Trust</strong></div>
    <div class="sil-flow-step"><strong>PQC / Encryption</strong></div>
    <div class="sil-flow-step"><strong>Secure AI</strong></div>
  </div>
</div>

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Data Governance | Security Programの基礎としてData Inventoryが必要 |
| AI | Training / RAGへ投入してよいDataを判断しやすくなる |
| PQC | 長期保護が必要なDataをMigration Priorityへつなげる |
| ZTA | Sensitivityに応じたAccess Controlが可能になる |

## 日本企業への示唆

DLP Tool導入をGoalにせず、Classification LabelをAccess、Retention、Encryption、AI Use Policyへ接続することが重要です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Unstructured Dataの主要RepositoryをInventory化する
2. Classification Schemeを3〜5段階程度へ簡素化する
3. LabelとAccess / Retention Ruleを紐づける
4. AI Training / RAG利用可否をLabelから判断できるようにする
5. Long-lived Sensitive DataをPQC Migration対象として識別する
6. Classification Accuracyを継続測定する

</div>

## 用語解説

**Unstructured Data**  
Document、Email、PDF、Chat、File等、Database Tableのように固定Schemaを持たないData。

## 関連記事

- [NIST PIVのPQC対応](../identity-security/pqc-piv-dual-stack.md)
- [生成AI利活用ガバナンス](../ai-security/generative-ai-governance.md)

## 参考情報

- [NIST, Draft Guidelines on Data Classification Practices](https://www.nist.gov/news-events/news/2026/02/comment-now-draft-guidelines-data-classification-practices)

[^source]: [NIST SP 1800-39 Draft](https://www.nist.gov/news-events/news/2026/02/comment-now-draft-guidelines-data-classification-practices)

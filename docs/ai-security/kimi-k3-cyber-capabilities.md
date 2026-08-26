---
title: Kimi K3のCyber能力評価 ― Open-weight AIを「モデル名」ではなく能力で評価する
date: 2026-08-26
updated: 2026-08-26
reviewed: '2026-08-26'
review_status: Current
source_period: 2026-07
description: UK AISIと米国CAISI/NISTが2026年7月に公表したKimi K3 Cyber Capability評価を基に、企業がAIモデルの攻撃能力をどう評価すべきか整理する。
category: AI Security
collections:
- ai-security
tags:
- Kimi K3
- Cyber Capability
- Open-weight AI
- AI Evaluation
audience:
- Executive
- CISO
- AI Governance
- Security Research
management_impact: High
impact_types:
- AI Governance
- Model Risk
urgency: Strategic
evidence: Observed
status: published
pptx: ''
media_rights: none
---
# Kimi K3のCyber能力評価 ― Open-weight AIを「モデル名」ではなく能力で評価する

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">July 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">AI Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / AI Governance / Security Research</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">AI Governance / Model Risk</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Strategic</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

UK AISIと米国CAISI/NISTは2026年7月23日、Moonshot AIのKimi K3についてCyber Capabilityの共同評価結果を公表しました。Kimi K3は最新のFrontier Cyber-capable Modelより低い性能だった一方、GLM-5.2を上回り、模擬企業Networkの32段階Attack Pathで平均17段階まで到達し、10回中1回は全経路を完了しました。[^source]

重要なのは特定モデルの優劣ではなく、**Open-weight / Closed-weightを問わず、AIのCyber能力を継続測定する仕組みが必要になった**ことです。

</div>

## なぜ今なのか

AI ModelのCyber能力は、Coding Benchmarkだけでは判断できません。

Exploit Development、Privilege Escalation、Network Attack、長時間Agent Taskなど、実際の攻撃チェーンに近い評価が必要です。同時にBenchmarkは実環境と異なるため、数値をそのまま実攻撃成功率として解釈することも危険です。

## 評価結果をどう読むか

NIST公表の主なポイントは以下です。

- Kimi K3は最新Frontier Modelより低い
- GLM-5.2より高いCyber Capabilityを示した
- ExploitBenchで32%のScore
- 模擬Corporate Networkで平均17/32 step
- 10試行中1回は全Attack Pathを完了
- SafeguardはOffensive Cyber Taskの試行を完全には止めなかった

一方、評価環境にはActive Defenderが存在せず、意図的に攻撃経路が用意されているなど、Real Worldとの差があります。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Model Selection | Performance / CostだけでなくCyber Capabilityも評価対象になる |
| Open-weight Risk | Weight公開時は組織側Safeguardへの依存度が上がる |
| Vendor Risk | 「安全です」というVendor Claimだけでは不十分 |
| Monitoring | Model UpdateごとにRisk Ratingを更新する必要 |

## 日本企業への示唆

企業が外部AI Modelを採用する際、Security Checklistを「Dataを学習利用するか」だけで終わらせないことが重要です。

Code Execution、Tool Use、Network Access、Agent Autonomyがある場合、モデルのCyber CapabilityとRuntime Controlを組み合わせて評価する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. AI Model InventoryにCapability Riskを追加する
2. Coding / Agent用途ではCyber Capability評価結果を確認する
3. Open-weight ModelはRuntime Safeguardを組織側で実装する
4. Tool / Network / Credential Accessを能力に応じて制限する
5. Model Version更新時にRisk Assessmentを再実施する

</div>

## 用語解説

**ExploitBench**  
脆弱性に対してExploit Developmentの各段階をどこまで進められるかを測定するBenchmark。

**Cyber Range**  
攻撃・防御能力を評価するために構築された模擬Network環境。

## 関連記事

- [Frontier AIのサイバー能力が「Critical」に近づく意味](frontier-ai-cyber-capabilities.md)
- [OpenAI / Hugging Face評価インシデント](openai-huggingface-evaluation-incident.md)

## 参考情報

- [NIST / CAISI, UK AISI / CAISI Preliminary Assessment of Kimi K3's Cyber Capabilities](https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities)

[^source]: [NIST / CAISI, UK AISI / CAISI Preliminary Assessment of Kimi K3's Cyber Capabilities](https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities)

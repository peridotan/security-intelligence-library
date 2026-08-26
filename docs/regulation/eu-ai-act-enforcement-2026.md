---
title: EU AI Actが執行フェーズへ ― 2026年8月2日から何が変わったか
date: 2026-08-26
updated: 2026-08-26
description: EU AI Actの2026年8月2日適用・執行強化とArticle 50透明性義務を日本企業向けに整理する。
category: Regulation
tags:
- EU AI Act
- AI Governance
- Transparency
- Regulation
- Generative AI
audience:
- Executive
- CISO
- Legal
- AI Governance
management_impact: High
urgency: Immediate
evidence: Confirmed
status: published
pptx: ''
---

# EU AI Actが執行フェーズへ ― 2026年8月2日から何が変わったか

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Regulation</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Legal / AI Governance</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Confirmed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

2026年8月2日から、EU AI Actの執行権限が本格的に動き始め、Article 50の**AI Transparency義務**が適用されました。チャットボット等ではAIとの対話であることを利用者へ知らせ、AI生成・改変コンテンツには一定の場合にMachine-readable MarkingやLabelingが求められます。[^source]

日本企業にとって重要なのは、「EU向けAI製品を作っている会社だけ」の話ではない点です。EUでAI機能を提供・導入する企業は、自社がProviderかDeployerか、どのAI Systemが対象か、誰がLabelingや通知を担うかを整理する必要があります。

</div>

## なぜ今なのか

European Commissionは7月31日、8月2日からAI Officeと各国当局がAI Actの執行を開始すると発表しました。同日からArticle 50の透明性義務も適用されています。

2026年8月は「将来のAI規制に備える」段階から、**対象システムについて実際に説明・表示・証拠化できる状態を求められる段階**への移行点です。

## Article 50の主要義務

### Provider側

- 利用者がAI Systemと直接対話していることを明示できる設計にする。
- AI生成・改変コンテンツを検出可能にするMachine-readable Markを付与する。

### Deployer側

一定の場合に、利用者へ以下を知らせます。

- Emotion Recognition / Biometric Categorisationの利用
- Deepfake
- Human ReviewやEditorial ControlなしでPublic Interest事項について公開されるAI生成テキスト

実際の適用には例外・条件があるため、対象判定はArticle 50とCommission Guidelinesを確認する必要があります。

## 2026年8月2日からの執行

European Commissionの最新整理では、8月2日からAI Officeおよび加盟国当局の執行権限が動きます。Transparencyだけでなく、既に適用されている禁止AI PracticesやGPAI Provider obligationsも執行対象に含まれます。

Commission FAQでは、Article 50違反に対する罰金は最大**1,500万ユーロまたは前年度全世界売上高の3%**に達し得ると説明されています。ただし、具体的な適用は違反内容、主体、比例原則等によって決まります。

## 既存システムの移行期間

Commission FAQは、2026年8月2日より前に市場投入されたAI Systemについて、Article 50(2)のMarking / Detection義務に限り、2026年12月2日までの限定的な移行期間を示しています。

また、8月2日より前に生成・公開済みのコンテンツを遡及的にLabelする必要はないとされています。

## 経営インパクト

| 論点 | 実務への影響 |
| --- | --- |
| AI Inventory | どのサービスにAIが埋め込まれているか把握が必要 |
| Role Mapping | Provider / Deployer / GPAI等の役割整理が必要 |
| UI/UX | Chatbot通知やDeepfake Labelingを製品要件へ組み込む |
| Data / Content | Machine-readable Markを生成・保持する仕組みが必要 |
| Evidence | Complianceを説明する設計・運用記録が必要 |
| Vendor | SaaSのAI機能でも責任分界の確認が必要 |

## 日本企業への示唆

最初に行うべきは法律の全文を全社員へ読ませることではなく、**EUで利用されるAI SystemのInventoryとRole Mapping**です。

たとえば、社内FAQ Bot、顧客向けChatbot、Marketing画像生成、採用支援、Emotion Recognitionなど、用途ごとに対象性と責任主体が異なります。AI Governance台帳に「EU利用」「Provider/Deployer」「Article 50対象」「Labeling方式」を追加すると実務へ落とし込みやすくなります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. **EU向けAI Inventoryを確定する** — 自社開発だけでなくSaaS組込み機能を含める。
2. **Provider / Deployerを判定する** — 法務、製品、IT、AI Governanceで責任分界を整理する。
3. **Article 50 Gap Analysisを行う** — AI Interaction通知、Marking、Deepfake等のLabelingを確認する。
4. **Evidenceを残す** — 対象判定、実装、テスト、Vendor確認を監査可能にする。
5. **既存システムの移行期限を確認する** — 12月2日までの限定的経過措置が使える範囲を個別に確認する。

</div>

## 好意的・批判的に見ると

**好意的な見方**では、Transparency義務は利用者がAIを認識できる最低限の信頼基盤を作り、企業にとっても表示要件を製品設計へ落とし込みやすくします。

**慎重な見方**では、Machine-readable Markingの技術的実装やValue Chain上の責任分界には複雑さが残ります。Code of Practiceへの署名だけで全義務が自動的に満たされるわけではなく、自社の適用範囲を確認する必要があります。

## 用語解説

**Provider**  
AI Systemを開発し、自らの名称・商標で市場投入・サービス提供する主体など、AI Act上の提供者。

**Deployer**  
自らの権限の下でAI Systemを利用する主体。個人的・非専門的利用等を除く。

**Article 50**  
特定AI Systemの透明性、AI生成コンテンツのMarking、Deepfake等のLabelingを扱う条文。

## 関連記事

- [生成AI利活用ガバナンス](../ai-security/generative-ai-governance.md)
- [Agentic AIの安全設計](../ai-security/agentic-ai-security-controls.md)


## 参考情報

- European Commission, Commission starts enforcing AI Act rules and new transparency requirements on 2 August (2026-07-31)  
  https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august
- European Commission, Guidelines on transparency obligations for providers and deployers of certain AI systems  
  https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations
- European Commission, Transparency obligations under Article 50 of the AI Act - FAQ  
  https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act
- European Commission, The enforcement framework of the AI Act  
  https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act

[^source]: European Commission, Commission starts enforcing AI Act rules and new transparency requirements on 2 August (2026-07-31). https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august

---
title: Cairnによる自律攻撃 ― 実際の侵入活動で観測されたZero-day探索
date: 2026-11-24
updated: 2026-11-24
reviewed: 2026-11-24
review_status: Current
source_period: 2026-11
description: Amazon Threat Intelligenceが観測したCairnによる自律的な侵入活動を基に、脆弱性発見から悪用までの時間短縮と防御側の設計課題を整理する。
category: AI Security
collections:
  - ai-security
  - cybersecurity
topics:
  - AI-Enabled Threats
  - AI Cyber Capability
  - Vulnerability Management
tags:
  - Cairn
  - Agentic AI
  - Zero-day
  - Autonomous Attack
audience:
  - Executive
  - CISO
  - SOC
  - Vulnerability Management
management_impact: High
impact_types:
  - Threat Landscape
  - Operational Security
  - Vulnerability Risk
urgency: Immediate
evidence: Observed
status: published
pptx: ""
media_rights: none
---

# Cairnによる自律攻撃 ― 実際の侵入活動で観測されたZero-day探索

<div class="sil-executive-summary" markdown>

## Executive Summary

Amazon Threat Intelligenceは、公開状態にあった自律型AIペネトレーションテスト基盤「Cairn」の運用履歴を調査し、2026年9月8日から約48時間にわたり東アジアの大学を標的とした活動を観測したと報告した。報告によれば、AIエージェントは「シェルアクセスを得る」という目的に対し、手順を自ら計画・実行・修正した。あるオープンソース医用画像AIアプリケーションでは、APIの把握からパストラバーサルによる任意ファイル書き込みまで約11分で到達し、後続の別セッションについては、Amazonが同じ脆弱性による侵害を推定しており、直接確認した事実とは区別する。[^aws]

ここで確認できるのはAmazonの観測と評価であり、全攻撃者や全AIエージェントの一般的能力を示す測定ではない。それでも、既知手法の反復、公開情報からのユーザー名収集、3万件超の資格情報試行、未知脆弱性の探索を長時間連続して実行する運用モデルは、防御側の時間軸を変える。Libraryは、アラート後の人手判断だけに依存せず、露出面の削減、高確度検知からの限定的自動封じ込め、AI攻撃活動を想定した演習を組み合わせる必要があると評価する。

</div>

## なぜ今なのか

既存記事「LLM-discovered Zero-days」や「MDASH」はAIによる脆弱性発見能力を扱っている。本件の新規性は、研究・防御目的の発見ではなく、実際の標的に対する侵入活動の中で、探索から悪用までが一つの自律ワークフローとして接続されたとAmazonが報告した点にある。

防御側にとって重要なのは「AIが万能になった」ことではない。Redisを対象とした約16時間・148アクションの試行や、別のGPUサーバーに対する3万件超の資格情報試行は失敗している。一方で、失敗しても停止せず、別経路を探索し続けられることが運用負荷と検知機会を同時に増やす。成功率だけでなく、試行回数・継続時間・並列性をリスク評価へ加えるべき段階に入った。

## 何が起きているのか

### 確認できた事実

Amazonは2026年9月10日、認証なしで公開されていたCairnサーバーを特定し、プロジェクト設定、操作者のプロンプト、AI出力を含む運用履歴を閲覧できたとしている。記録から、9月8日に始まる約48時間の活動を分析した。Amazonはプロジェクト保守者へ脆弱性を通知し、修正とGitHub Security Advisoryの公開につながったとも記載している。[^aws]

### 情報源の主張

Amazonは、医用画像AIアプリケーションの脆弱性について、当時は修正、Issue、Advisory、脆弱性データベース上の言及がなく、Zero-dayだったと高い確度で評価している。また、簡体字中国語のプロンプト、China Standard Timeのタイムスタンプ、標的選定を根拠に、操作者をChinese-nexus actorと中程度の確度で評価している。これらはAmazonの帰属・評価であり、Libraryが独立に立証した事実ではない。

### Libraryの評価

本件は「一つの高度なモデル」よりも、複数エージェント、既存ツール、外部公開情報、長時間実行を組み合わせた運用能力の問題である。組織はモデル名や単発ベンチマークではなく、攻撃側が到達できる外部資産、認証境界、実行権限、試行速度を一体として評価する必要がある。

## 経営インパクト

- **対応時間の非対称性**：11分という観測値が再現可能な一般性能を意味するわけではないが、探索から初期侵入までがSOCの通常の手動トリアージより短くなる可能性を示す。
- **攻撃コストの低下**：失敗した試行を人間が逐次指示せず継続できれば、従来は優先度が低かった外部資産も探索対象になりやすい。
- **脆弱性管理の再設計**：CVE付与やパッチ公開より先に悪用が始まる状況では、資産露出、挙動検知、最小権限、復旧力が同じ優先度を持つ。
- **AI利用統制との両面性**：自社のAIエージェント防御と、敵対者によるAI活用を別々のプログラムにせず、共通のIdentity・Network・Logging統制で扱う必要がある。

## 日本企業への示唆

大学・研究機関だけの問題とは限らない。研究用GPU、検証環境、オープンソースAIアプリケーション、管理用データベースは、企業でも「本番ではない」ことを理由に監視や認証が弱くなりやすい。インターネット露出資産の棚卸しでは、本番システムに加えて研究開発・PoC・委託先環境を含めるべきである。

また、AI攻撃を理由に無制限な自動遮断へ進むのも危険である。高確度シグナル、影響範囲を限定したアクション、復旧手順、事後レビューを事前に定義し、人間は個々の低水準イベントではなく自動化の結果と例外を監督する設計が現実的である。

<div class="sil-action-box" markdown>

## 推奨アクション

1. 外部公開資産を本番・研究・PoC・委託先まで横断して再棚卸しし、認証なしサービス、管理API、学習API、ファイルアップロード機能を優先確認する。
2. 資格情報スプレー、連続的なAPI列挙、異常なファイル書き込み、外向き通信を組み合わせた高確度検知を作り、限定的な自動隔離手順を演習する。
3. CVE待ちにせず、公開面の縮小、最小権限、実行環境の分離、Egress制御、復旧可能なバックアップをZero-day対策として評価する。
4. AI支援攻撃を想定したPurple Team演習で、発見から封じ込めまでの実時間と人手依存箇所を測定する。

</div>

## 用語解説

- **Cairn**：自然言語の目的から複数のAIエージェントを協調させる、オープンソースの自律型ペネトレーションテスト基盤。
- **Zero-day**：修正や防御準備が整う前に認識・悪用される脆弱性。本稿ではAmazonの評価として用いる。
- **パストラバーサル**：ファイル名やパスの扱いを悪用し、想定外の場所へ読み書きする脆弱性。

## 関連記事

- [anthropic llm discovered zero days](anthropic-llm-discovered-zero-days.md)
- [mdash ai vulnerability discovery](../cybersecurity/mdash-ai-vulnerability-discovery.md)
- [ai assisted intrusion 10 hours](../cybersecurity/ai-assisted-intrusion-10-hours.md)

## 参考情報

- [AWS Security Blog: Chinese-nexus actor’s Cairn AI agents found a zero-day on their own](https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/)

[^aws]: AWS Security Blog, “Chinese-nexus actor’s Cairn AI agents found a zero-day on their own,” 2026-11-20（2026-11-24確認）。
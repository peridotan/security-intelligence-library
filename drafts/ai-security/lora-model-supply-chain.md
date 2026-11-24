---
title: Backdoored LoRA ― モデル重みをSoftware Supply Chainとして検証する
date: 2026-11-24
updated: 2026-11-24
reviewed: 2026-11-24
review_status: Needs Review
source_period: 2026-11
description: CrowdStrikeのLoRAバックドア検出実験を基に、モデル重みの受入審査、静的解析、Trigger確認、Runtime分離の実務を整理する。
category: AI Security
collections:
  - ai-security
  - cybersecurity
topics:
  - AI Infrastructure
  - Software Supply Chain
  - AI Agent Security
tags:
  - LoRA
  - Open-weight Model
  - Model Backdoor
  - Model Supply Chain
audience:
  - CISO
  - AI Platform
  - MLOps
  - Product Security
management_impact: High
impact_types:
  - AI Supply Chain
  - Model Integrity
  - Runtime Security
urgency: Near-term
evidence: Assessment
status: draft
pptx: ""
media_rights: none
---

# Backdoored LoRA ― モデル重みをSoftware Supply Chainとして検証する

<div class="sil-executive-summary" markdown>

## Executive Summary

CrowdStrikeは、LoRAアダプターやマージ済みモデルに埋め込まれたバックドアを、(1)重み差分の静的解析と、(2)Trigger recoveryによる挙動確認の二段階で検出する実験を公開した。16アーティファクト（バックドア8、良性8）を用いた実験では、Stage 1がバックドア8件すべてを何らかの疑わしい変更としてフラグし、良性8件のうち5件をCleanと判定した。Stage 2はエスカレーション対象の挙動を確認する役割を担った。[^crowdstrike]

これは16件の研究用セットであり、公開モデル全体に対する検出率や誤検知率を示すものではない。CrowdStrike自身も、ベースモデル参照の不足、複数語Trigger、Full fine-tune、直接的なWeight editing、回避手法などを制約として挙げている。Libraryは、モデル重みを「実行前に審査すべき第三者コード」として扱い、来歴・ハッシュ・署名だけでなく、隔離環境での挙動評価とRuntime権限制御を組み合わせるべきだと評価する。

</div>

## なぜ今なのか

Open-weightモデルやLoRAは、コスト、データ保護、カスタマイズ性のため企業利用が広がっている。一方、通常のベンチマークは能力と品質を測るものであり、特定のTriggerでのみ発火する悪意ある挙動を保証しない。ProjectDiscoveryは2026年10月、Qwen2.5-7Bを用いたLoRAバックドアを含む実験を総額50ドル未満で行い、特定フレーズでCoding Agentへ攻撃者管理URLへのTool callを出させたと報告した。[^projectdiscovery]

本件は、既存のパッケージやAIアプリケーション依存関係の記事と異なり、モデルの「重みそのもの」がSupply Chainアーティファクトになる。安全な形式であるsafetensorsを使っていても、危険なデシリアライズによるコード実行リスクを低減しても、モデルが生成する悪意あるTool callやコードまでは保証しない。

## 何が起きているのか

### CrowdStrikeの二段階方式

Stage 1は、候補モデルと既知のベースモデルの差分を解析し、LoRA由来の低ランク構造、変更が集中する層、特定出力語彙への偏りを調べる。ここでのフラグは改変の兆候であり、悪意の証明ではない。

Stage 2は、Stage 1が示した疑わしい挙動を対象に、モデル語彙からTrigger候補を探索し、実際に悪意ある出力が生成されるか確認する。静的解析の間接証拠と、挙動確認の直接証拠を組み合わせる設計である。

### 実験結果と限界

CrowdStrikeのテストセットは、Tool call、Shell injection、Typosquat import、Refusal flipなど7種類のバックドアを含む8件と、良性8件で構成された。Stage 1はバックドア8件をすべてフラグした一方、良性モデル2件も「未申告のマージ済みLoRA」としてStage 2へ送り、1件はAbliterationとして識別した。これは「フラグ＝悪性」ではないことを示す。

さらに、真のベースモデルを保持していなければ精密な差分が難しい。Stage 2は単語Triggerと限定的なPayload種別を中心とし、Full fine-tuneや直接Weight editingは対象外である。したがって、研究結果を製品レベルの網羅的保証として扱ってはならない。

### Libraryの評価

モデル受入審査には、Publisherの信頼だけでなく、取得元、ハッシュ、ベースモデル、学習・Fine-tune方法、評価結果、Runtime権限を結び付けた記録が必要である。検出器が利用できない組織でも、モデルをSandboxで実行し、Tool call、Network Egress、Secret accessを制限すれば、バックドア発火後の被害を抑えられる。

## 経営インパクト

- **調達対象の拡張**：モデル重みやAdapterも、ライブラリ・コンテナと同じ第三者アーティファクト管理の対象になる。
- **検証コスト**：モデルの能力評価に加え、来歴、改変、Trigger挙動、Runtime権限の検証が必要になる。
- **信頼ブランドの限界**：PublisherアカウントやModel Cardが正しくても、アカウント侵害・差し替え・学習データ汚染を排除できない。
- **事故時の追跡性**：どの重みをどの環境で、どのTool権限と組み合わせて使ったかを説明できなければ影響調査が遅れる。

## 日本企業への示唆

データの外部送信を避ける目的でオープンモデルをローカル運用する場合でも、しかし、モデルがTool callや生成コードを通じて外部通信・Secret参照へ到達できれば、「ローカルだから安全」という前提は崩れる。AI基盤部門とセキュリティ部門は、モデルレジストリ、承認済みベースモデル、Egress、Tool権限を共通統制にする必要がある。

また、検出ツールの導入可否だけで判断せず、モデルが侵害されている前提でBlast radiusを制限する。開発端末のホームディレクトリ、`.env`、SSH鍵、Code Repositoryへ既定で到達できるAgent構成は見直すべきである。

<div class="sil-action-box" markdown>

## 推奨アクション

1. モデルとLoRA Adapterを社内レジストリへ取り込み、取得元、ハッシュ、ベースモデル、ライセンス、評価、承認者を記録する。
2. 新規モデルは隔離環境で能力評価と敵対的Trigger評価を行い、更新・差し替え時も再審査する。
3. AI AgentのTool callをAllowlist化し、Shell、Network Egress、Secret、Code Repositoryへの権限を分離する。
4. 重み差分解析を使う場合も、フラグを悪性断定にせず、挙動確認と人間レビューへエスカレーションする。

</div>

## 用語解説

- **LoRA**：ベースモデルの重みを固定し、少数の追加パラメータで振る舞いを調整するFine-tuning手法。
- **Trigger**：バックドア挙動を有効にする特定の語、フレーズ、日付等。
- **Model Card**：モデルの目的、制約、学習・評価情報等を説明する文書。完全性や改変不存在を自動保証するものではない。

## 関連記事

- [openai huggingface evaluation incident](openai-huggingface-evaluation-incident.md)
- [litellm 1 107 0 supply chain compromise](litellm-1-107-0-supply-chain-compromise.md)
- [langgrinch ai application supply chain](langgrinch-ai-application-supply-chain.md)

## 参考情報

- [CrowdStrike: Hidden in the Weights: Supply Chain Risk from Backdoored LoRA Models](https://www.crowdstrike.com/en-us/blog/supply-chain-risk-from-backdoored-lora-models/)
- [ProjectDiscovery: How abliterated models can get you pwned](https://projectdiscovery.io/research/how-abliterated-models-can-get-you-pwned)

[^crowdstrike]: CrowdStrike, “Hidden in the Weights: Supply Chain Risk from Backdoored LoRA Models,” 2026-11-16（2026-11-24確認）。
[^projectdiscovery]: ProjectDiscovery, “How abliterated models can get you pwned,” 2026-10-06（2026-11-24確認）。
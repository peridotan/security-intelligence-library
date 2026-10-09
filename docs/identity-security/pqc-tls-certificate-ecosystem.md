---
title: PQC認証の準備は証明書エコシステムから ― Microsoft TLS Pilotが示す相互運用性の課題
date: 2026-10-09
updated: 2026-10-09
reviewed: 2026-10-09
review_status: Current
source_period: 2026-10
description: MicrosoftのPQC TLS Pilot Programを基に、企業PKI、証明書チェーン、HSM、アプリケーションの非本番検証で確認すべき論点を整理する。
category: Identity Security
collections:
  - identity-security
  - risk-management
topics:
  - PQC / Crypto Agility
  - Identity Security
tags:
  - PQC
  - TLS
  - PKI
  - ML-DSA
  - Certificate
  - Crypto Agility
audience:
  - Executive
  - CISO
  - IAM
  - PKI
management_impact: High
impact_types:
  - Identity
  - Cryptography
  - Technology Lifecycle
urgency: Strategic
evidence: Confirmed
status: published
pptx: ""
media_rights: none
---

# PQC認証の準備は証明書エコシステムから ― Microsoft TLS Pilotが示す相互運用性の課題

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoftは2026年8月27日、Microsoft Trusted Root Programに参加する適格な認証局を対象に、ML-DSA-87を用いたPQC TLSルートと証明書発行を評価するPilot Programを開始しました。発行される証明書は公開信頼されず、閉域環境、カスタムアプリケーション、企業テストベッドでの相互運用性検証専用です。Microsoftは本番の信頼用途や公開Webサイトで使用しないよう明記しています。[^microsoft]

Libraryの評価では、このPilotの重要性は特定製品の導入可否ではなく、PQC認証が証明書アルゴリズムの置換だけでは完了しない点にあります。CA、トラストアンカー、証明書チェーン、TLS実装、HSM、端末、アプリケーション、更新・失効プロセスを一体として検証する必要があります。

</div>

## なぜ今なのか

機密性の議論では「Harvest Now, Decrypt Later」が注目されますが、認証では、発行・配布・保存・検証・更新・失効という証明書ライフサイクルと、多数の製品間相互運用性が課題になります。長寿命のOT機器、セキュリティアプライアンス、組み込み機器、社内PKIは更新周期が長く、移行時に初めて固定された暗号前提が判明する可能性があります。[^microsoft]

## 何が起きているのか

Microsoftが公表した確認済み事項は次のとおりです。

- Pilotは適格な認証局がML-DSA-87のルートと証明書発行を評価するための管理された試験です。[^microsoft]
- Pilot証明書は公開信頼されず、本番の信頼用途および公開Webサイトでは使用できません。
- 対応するWindows 11環境では、2026年7月28日以降の指定更新を前提に、管理された非本番シナリオでML-DSA証明書を評価できます。
- Microsoftは、アプリケーション互換性、証明書サイズ、性能、運用ワークフローの問題を本番導入前に発見することを目的として説明しています。

これらはMicrosoftのPilot仕様と見解です。ML-DSAの本番利用可能性、他OS・ブラウザー・TLSライブラリ・HSMとの相互運用性を一般化するものではありません。

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| PKI資産 | 公開TLSだけでなく、社内CA、相互TLS、端末・Workload証明書まで棚卸しが必要 |
| 相互運用性 | 証明書チェーンの大型化や未対応コンポーネントが接続障害を招く可能性 |
| HSM／KMS | 鍵形式、署名、バックアップ、監査、ファームウェア対応の確認が必要 |
| 調達 | OS、ブラウザー、TLSライブラリ、アプライアンスのPQC Roadmap比較が必要 |
| 移行統制 | Classical/PQC併存期間の信頼設計とロールバック手順が必要 |

## 日本企業への示唆

PQC対応を「暗号ライブラリ更新」の一案件に閉じると、証明書を利用する周辺システムが抜け落ちます。企業PKI、Web／API、VPN、Wi-Fi、端末管理、コード署名、文書署名、Workload Identity、OT／IoTを横断する暗号資産台帳が必要です。

Libraryの評価では、直ちに本番へML-DSAを導入する段階ではなく、非本番環境で互換性と運用手順を可視化する段階です。Pilot結果を製品ロードマップの代替とせず、自社構成で再現確認する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. CA、証明書、用途、アルゴリズム、期限、依存システムを紐付けた暗号資産台帳を作成する。
2. 長寿命機器、固定暗号前提の製品、更新困難なシステムを優先して分類する。
3. 非本番環境で証明書発行、チェーン検証、TLS接続、更新、失効、ロールバックを試験する。
4. HSM、KMS、CA、TLSライブラリ、OS、ブラウザー、アプライアンスのPQC Roadmapを確認する。
5. 証明書サイズ、処理性能、ログ・監視、障害対応への影響を測定する。
6. Crypto Agilityと移行支援を新規調達・更改要件へ組み込む。

</div>

## 用語解説

**ML-DSA**  
NISTが標準化した格子ベースの耐量子デジタル署名方式。

**証明書エコシステム**  
CA、証明書、トラストストア、アプリケーション、端末、HSM、運用プロセスなど、証明書の発行から検証・失効までを支える構成要素の総体。

**Crypto Agility**  
暗号アルゴリズムや鍵方式を、大規模な作り直しを避けながら交換・移行できる能力。

## 関連記事

- [NIST PIVのPQC対応 ― Identity Credentialも「Crypto Agility」が必要になる](pqc-piv-dual-stack.md)
- [NIST SP 800-133r3 Draft ― PQC移行はAlgorithmだけでなくKey Generation / HSMまで変える](nist-key-generation-pqc-sp800-133r3.md)

## 参考情報

- [Microsoft Security Blog, Post-quantum authentication: Why organizations should start testing certificate ecosystems now](https://www.microsoft.com/en-us/security/blog/2026/10/08/post-quantum-authentication-why-organizations-should-start-testing-certificate-ecosystems-now/)

[^microsoft]: [Microsoft Security Blog, Post-quantum authentication: Why organizations should start testing certificate ecosystems now](https://www.microsoft.com/en-us/security/blog/2026/10/08/post-quantum-authentication-why-organizations-should-start-testing-certificate-ecosystems-now/)
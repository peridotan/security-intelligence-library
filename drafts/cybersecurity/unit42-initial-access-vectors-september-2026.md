---
title: 初期侵入の主要5類型 ― Unit 42の2026年9月観測から考える防御優先順位
date: 2026-10-19
updated: 2026-10-20
reviewed: 2026-10-19
review_status: Needs Review
source_period: 2026-09
description: Unit 42が2026年9月の観測を基に示した初期侵入の主要5類型を、頻度・影響度の記載の違いに注意して読み解き、Edge、Identity、Phishing、Supply Chainの防御優先順位を整理する。
category: Cybersecurity
collections:
  - cybersecurity
topics:
  - Vulnerability Management
  - Credential Attacks
  - Software Supply Chain
tags:
  - Initial Access
  - Edge Security
  - Credential Abuse
  - Phishing
  - Supply Chain
audience:
  - Executive
  - CISO
  - Security Operations
management_impact: High
impact_types:
  - Operational Security
  - Identity
  - Supply Chain
urgency: Near-term
evidence: Assessment
status: draft
pptx: ""
media_rights: none
---

# 初期侵入の主要5類型 ― Unit 42の2026年9月観測から考える防御優先順位

<div class="sil-executive-summary" markdown>

## Executive Summary

Unit 42は2026年10月16日、同社Threat Intelligenceが2026年9月に観測した初期侵入ベクトルの主要5類型を公表しました。対象は、公開アプリケーションの悪用、正規資格情報・資格情報悪用、フィッシング／標的型ソーシャルエンジニアリング、サプライチェーン侵害、Drive-by Compromise／Watering Holeです。同社は前半の3類型を主要・頻出の経路、後半の2類型を高影響・特殊な経路として説明しており、5件の表示順がすべて同一指標による発生頻度順という意味ではありません。[^unit42]

これは世界全体や日本企業の侵入経路を統計的に示す資料ではなく、Unit 42の観測範囲に基づくベンダー分析です。それでも、Edge、Identity、メール／ブラウザ、開発・委託先を別々に守るだけでは初期侵入を抑えにくい、という防御設計上の示唆があります。本Libraryは、公開システム、資格情報、フィッシングを横断するExposure・Credential・User Interactionの統合管理を優先すべきと評価します。

</div>

## なぜ今なのか

Unit 42の観測では、公開システムの悪用と正規資格情報の悪用が上位に並び、フィッシングが続きました。[^unit42] 侵入後のMalware検知だけではなく、侵入前のExternal Attack Surface、脆弱性、認証、ユーザー操作を一つのリスクとして管理する必要があります。

ただし、同社の列挙順を「日本で最も多い攻撃」の順序や「市場全体の発生率」と読み替えることはできません。記事では、確認できた公表内容、Unit 42の評価、Libraryの判断を分けます。

## 何が起きているのか

### 確認できた公表内容

Unit 42は、2026年9月の観測対象について次の5類型を表形式で示しています。[^unit42] 原文の番号には、侵入経路の普及度・主要性を示すもの（1〜3）と、影響の大きさ（4）や特殊な侵入手法（5）を示すものが混在しています。公表資料には母集団、観測件数、類型別構成比、地域別内訳が示されていないため、5類型を共通の発生頻度指標で比較したランキングとしては扱いません。

| 原文の番号・位置づけ | Unit 42の分類 | 公表ページの説明 |
| --- | --- | --- |
| 1：主要な侵入経路 | Exploitation of Public-Facing Applications | Internet公開されたWebアプリケーション、Database、境界サービスの侵害を主要な侵入経路として整理 |
| 2：主要な利用経路 | Valid Credentials & Credential Abuse | 事前取得、Password Spraying、不正入手された認証情報の利用を整理 |
| 3：主要なソーシャルエンジニアリング経路 | Phishing / Targeted Social Engineering | メッセージやブラウザ上の誘導によるCredential窃取・Payload実行を整理 |
| 4：波及影響が大きい経路 | Supply Chain Compromise | 信頼関係を悪用し、複数組織へ波及し得る高影響の経路として整理 |
| 5：特殊な侵入経路 | Drive-By Compromise / Watering Hole | 悪性・侵害済みWebサイトへのアクセスを起点とする経路として整理 |

### 情報源の主張

Unit 42は、同期間の攻撃活動について、外部Edgeの悪用とIdentity侵害への依存が顕著であり、公開Infrastructureと正規資格情報の悪用が主要な足場だったと評価しています。また、ソーシャルエンジニアリング、サプライチェーン侵害、Drive-by Compromiseが特定の標的や相互接続された環境に大きな影響を与え得ると述べています。[^unit42]

### Libraryの評価

5類型は相互排他的とは限りません。公開サービスの侵害後に資格情報を取得する、フィッシングで得た資格情報からEdgeやCloudへログインする、委託先・Software Supply Chainの信頼を使って複数環境へ波及する、といった複合経路で評価する方が実務的です。

## 経営インパクト

| 観点 | 経営上の意味 |
| --- | --- |
| 投資配分 | Endpoint中心の対策だけでなく、Internet-facing Asset、Identity、メール／ブラウザ、Supply Chainへ配分する必要がある |
| 組織設計 | Network、IAM、SOC、CSIRT、開発・調達の分断が初期侵入の見落としにつながる |
| KPI | Patch率だけでなく、公開Asset把握率、悪用可能Exposureの是正時間、Phishing-resistant MFA適用率を追う必要がある |
| 第三者リスク | Supplierや開発Dependencyの侵害が自社の侵入経路になり得る |

## 日本企業への示唆

日本企業では、外部公開機器をInfrastructure部門、認証をIAM部門、Phishingをメール対策、Supply Chainを調達部門が個別に管理することがあります。本Libraryは、これらを「Initial Accessを許す経路」という共通の管理単位で可視化し、同一のリスク会議で優先順位を決めることを推奨します。

Unit 42の列挙順をそのまま自社の防御優先順位にせず、自社のAsset Inventory、認証ログ、Incident記録、委託先構成と照合することが重要です。高影響のSupply Chainリスクも、自社の依存関係を踏まえて別途評価します。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Internet-facing Assetを棚卸しし、Owner、製品Version、EOL、認証方式、外部公開理由を紐付ける。
2. 悪用可能な脆弱性、Credential Abuse、Phishing検知を別キューにせず、共通のInitial Access Riskとして優先順位付けする。
3. 管理者、VPN、Remote Access、高価値SaaSからPhishing-resistant MFAを適用する。
4. 大量失敗後の成功、通常と異なる端末・場所、特権付与をIdentity TelemetryとEdge Logで相関分析する。
5. CI/CD、Package、委託先Remote Accessについて、侵害時の到達範囲とCredential Rotation手順を確認する。
6. Unit 42の列挙順ではなく、自社の観測データを用いた四半期ごとのInitial Accessレビューを実施する。

</div>

## 用語解説

**Initial Access**  
攻撃者が組織の環境へ最初の足場を得る段階。公開サービスの脆弱性悪用、正規資格情報の悪用、Phishingなど複数の経路があります。

**Drive-by Compromise / Watering Hole**  
標的が悪性または侵害済みのWebサイトへアクセスしたことを起点に、攻撃コードや誘導が実行される侵入経路です。

## 関連記事

- [Edge ApplianceからIdentity侵害へ](https://peridotan.github.io/security-intelligence-library/cybersecurity/f5-confluence-edge-to-identity/)
- [Large-Scale Credential Attacks](https://peridotan.github.io/security-intelligence-library/cybersecurity/large-scale-credential-attacks/)
- [Axios Supply Chain Compromise](https://peridotan.github.io/security-intelligence-library/cybersecurity/openai-axios-signing-supply-chain/)

## 参考情報

- [Unit 42, Top 5 Initial Access Threat Vectors Observed by Unit 42 in September 2026](https://unit42.paloaltonetworks.com/top-5-initial-access-vectors-september-2026/)

[^unit42]: [Unit 42, Top 5 Initial Access Threat Vectors Observed by Unit 42 in September 2026, published 2026-10-16](https://unit42.paloaltonetworks.com/top-5-initial-access-vectors-september-2026/)

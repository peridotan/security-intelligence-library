---
title: NICTのA2B攻撃注意喚起 ― 公開アプリを起点にしたBackend APIリスク
date: 2026-10-15
updated: 2026-10-15
reviewed: 2026-10-15
review_status: Needs Review
source_period: 2026-10
description: NICTが2026年10月13日に公表したA2B攻撃の注意喚起を基に、公開モバイルアプリから推測されるBackend APIへの攻撃経路と企業の確認事項を整理する。
category: Cybersecurity
collections:
  - cybersecurity
topics:
  - Vulnerability Management
  - Security Governance & Risk Management
tags:
  - NICT
  - CYNEX
  - LETTICE
  - A2B Attack
  - API Security
  - Mobile Application
  - BOLA
  - AppSec
audience:
  - Executive
  - CISO
  - AppSec
  - Product Security
management_impact: High
impact_types:
  - Operational Security
  - Software Security
  - Identity
urgency: Near-term
evidence: Mixed
status: draft
pptx: ""
media_rights: none
---

# NICTのA2B攻撃注意喚起 ― 公開アプリを起点にしたBackend APIリスク

<div class="sil-executive-summary" markdown>

## Executive Summary

NICTは2026年10月13日、公開Androidアプリの解析から接続先Backend APIの仕様やサーバ情報を把握し、バックエンドを狙う手法を「A2B攻撃（App-to-Backend Attack）」として注意喚起しました。NICTのLETTICEチームは、国内で相次ぐ情報漏えい事案の原因の一つとして、この手法を特定したと報告しています。7ページの詳細資料でも、同チームの調査・分析で情報の不正取得を確認した旨が記載されています。ただし、**これはNICT/LETTICEによる調査結果の報告**であり、被害組織や個別事案ごとの因果関係を本Libraryが独立に検証したものではありません。[^nict-press][^lettice-pdf]

攻撃者にアプリ内部のAPI接続情報が知られる可能性を前提に、Backend側で認証・認可・入力検証を行い、ログによって不正取得を検知できる状態を維持することが必要です。NICTが公開した対策は「侵害の確認」「脆弱性の点検」「暫定的な緩和策」の3つです。[^cynex]

</div>

## なぜ今なのか

モバイルアプリの配布は、アプリそのものの実装や通信先情報を第三者が解析できる状況を生みます。NICTの報告は、アプリに目立った脆弱性がなくても、**アプリから得た情報を使ってバックエンドの不備を攻撃され得る**という、開発・運用の責任分界上の論点を可視化しています。[^cynex]

NICTはAIによってアプリ解析・脆弱性探索が効率化され、攻撃対象が広がる可能性も指摘しています。詳細資料の**2ページの図1には、AIを使う解析や攻撃リクエスト生成が図示**されていますが、個別被害事案でAIがどの程度使われたかについて、本文は独立した証拠や件数を示していません。**観測されたA2B攻撃の事実と、AIによる攻撃効率化への懸念は分けて理解する必要があります。**[^lettice-pdf]

## 何が起きているのか

NICTのLETTICEチームによる説明では、A2B攻撃は概ね次の流れです。[^nict-press]

1. 攻撃者が一般に公開されたAndroidアプリを入手し、解析する。
2. アプリの通信先やBackend APIの仕様・呼び出し方などを把握する。
3. 得られた情報を手掛かりに、接続先サーバの実装・設定上の弱点を狙う。
4. Backend側に脆弱性が存在すると、不正アクセスや個人情報の漏えいにつながるおそれがある。

NICTはAndroidアプリを中心に説明していますが、iOSアプリやWebサービスのBackend APIにも同様の問題が起こり得ると注意を促しています。公開クライアントに見える接続先・パラメータなどを、サーバ側の信頼できる秘密情報とみなさないことが基本です。[^nict-press]

NICT/LETTICEの詳細資料は、今回確認されたA2B攻撃において、**SSRF、RCE、SQLインジェクション、IDOR（BOLA）の4種類が主な探索・悪用対象となっている**と説明しています（3ページ）。これは対象手法に関するNICTの調査結果であり、**すべての被害事案で4種類すべてが実際に悪用されたことを意味しません**。また、事業者向けの点検項目はこれら4種類だけでなく、認証・セッション管理、不適切な認証情報の露出、NoSQLインジェクション、クラウドストレージ設定、コード実行・ファイル操作の問題にも及びます（4ページ）。[^lettice-pdf]

## 攻撃の確認に使えるIoCと調査期間

LETTICEは詳細資料の6ページに、調査で確認したA2B攻撃に関連する**IoC（侵害指標）の一部**として、次のIPアドレスを公開しています。表記は誤クリックを防ぐため無害化しています。[^lettice-pdf]

- `69.10.51[.]162`
- `210.149.87[.]120`
- `207.241.172[.]54`

NICTが求める確認対象は、**2026年8月以降のアクセスログ・APIログ・認証ログ**であり、保存されていればそれ以前も確認します（詳細資料4ページ）。API本体だけでなく、**旧バージョンのAPI、サブドメイン、検証環境、クラウド上の公開サービス**も棚卸し対象です。[^lettice-pdf]

**IoCとの一致だけで侵害を断定せず**、認証を伴わない大量取得、連番IDへのアクセス、他利用者データの閲覧・変更、不審なトークン発行などと併せて調査します。逆に一致しない場合も安全の証明にはなりません。[^lettice-pdf]

## 経営インパクト

| 観点 | 企業にとっての意味 |
| --- | --- |
| 顧客情報・信用 | Backend API経由の不正取得が顧客情報漏えいやサービス信用失墜につながるリスク |
| 責任分界 | アプリ開発、API開発、基盤運用、SOCの間で所有者・監視・是正責任が分断されやすい |
| Secure Development | モバイルアプリ単体の診断だけではBackend側の認可不備を見落とす可能性 |
| 検知・対応 | 不審なAPI呼び出しをログに残し、情報取得の有無と範囲を調査できることが重要 |

上表はNICTの注意喚起を企業の管理課題に置き換えた**本Libraryの評価**です。

## 日本企業への示唆

外部公開アプリやAPIを提供する企業では、「APIエンドポイントが非公開だから安全」という前提を置かないことが重要です。セキュリティの境界は、クライアントの秘匿性ではなく、Backendでの認証・**オブジェクト単位の認可**・入力値検証・監視に置く必要があります。

外部委託開発の場合も、アプリの配布・アップデートを担当する組織とBackend APIを運用する組織を跨いで、資産台帳、脆弱性診断の範囲、インシデント対応時のログ保全を確認することが推奨されます。これらは、本Libraryによる管理上の提案です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. **侵害の確認**：現行・旧版API、サブドメイン、検証環境、公開クラウドサービスを棚卸しし、**2026年8月以降**のアクセス・API・認証ログを、IoCと不審な大量取得・連番ID試行の両面から確認する。[^lettice-pdf]
2. **脆弱性の点検**：IDOR/BOLA、SSRF、RCE、SQL/NoSQLインジェクションに加え、セッション管理、認証情報の露出、クラウドサービス・ストレージの設定不備、コード実行・ファイル操作の問題を確認する。[^lettice-pdf]
3. **暫定緩和**：必要に応じてアクセス元・不要API・管理機能・検証環境を制限し、レート制限・WAFを適用する。認証情報の漏えいが疑われれば無効化・再発行し、修正や緩和が難しい重大な問題ではサービスの一時停止も検討する。[^lettice-pdf]
4. **継続対策（Libraryの評価）**：リリース時のアプリ単体診断とBackend API診断を分けず、開発・運用・SOCで所有者と検証範囲を統一する。
5. **継続対策（Libraryの評価）**：単にAPIが呼べるかだけでなく、他利用者のオブジェクトを取得できないかという認可の否定テストを品質ゲートに含める。

</div>

## 用語解説

**A2B攻撃（App-to-Backend Attack）**  
NICTが2026年10月に注意喚起した、公開アプリの解析情報を利用してBackend側を狙う攻撃の呼称。

**Backend API**  
アプリやWeb画面から呼び出され、認証、データ参照・変更、業務処理などを行うサーバ側のインターフェース。

**IDOR / BOLA**  
APIやWebアプリで、指定されたオブジェクトにアクセスする権限をサーバが適切に検査しない問題。

## 関連記事

- [AI脆弱性トリアージを根拠ベースにする](evidence-grounded-ai-vulnerability-triage.md)
- [AI-assisted Intrusion ― 攻撃工程の高速化](ai-assisted-intrusion-10-hours.md)

## 参考情報

- [NICTプレスリリース（2026-10-13）](https://www.nict.go.jp/press/2026/10/13-1.html)
- [NICT CYNEX Library：LETTICEの注意喚起・推奨対策（2026-10-13）](https://cynex.nict.go.jp/library/261013-01.html)
- [NICT/LETTICE 注意喚起PDF（Rev 1.1、2026-10-13、全7ページ）](https://cynex.nict.go.jp/pdf/library/lettice/261013-01.pdf)

[^nict-press]: [NICT「アプリ解析からのサーバ攻撃」に関するプレスリリース](https://www.nict.go.jp/press/2026/10/13-1.html)
[^cynex]: [NICT CYNEX Library：A2B攻撃に関する注意喚起](https://cynex.nict.go.jp/library/261013-01.html)

[^lettice-pdf]: [NICT/LETTICE『アプリ解析からのサーバ攻撃』注意喚起（2026-10-13、Rev 1.1）](https://cynex.nict.go.jp/pdf/library/lettice/261013-01.pdf)

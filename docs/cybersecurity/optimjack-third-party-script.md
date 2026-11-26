---
title: OPTIMJACK ― 第三者JavaScriptを「本番コード」として管理する
date: 2026-11-24
updated: 2026-11-24
reviewed: 2026-11-24
review_status: Current
source_period: 2026-11
description: Optimizely Web Experimentationへの不正コード挿入事案を基に、第三者JavaScript、CSP、決済画面分離、委託先監督の実務を整理する。
category: Cybersecurity
collections:
- cybersecurity
- risk-management
topics:
- Software Supply Chain
- Third-party Risk / C-SCRM
- Security Governance & Risk Management
tags:
- OPTIMJACK
- Optimizely
- Third-party JavaScript
- Content Security Policy
- Web Supply Chain
audience:
- Executive
- CISO
- Web Engineering
- Third-party Risk
management_impact: High
impact_types:
- Supply Chain
- Customer Data
- Web Security
urgency: Immediate
evidence: Mixed
status: published
pptx: ''
media_rights: none
---

# OPTIMJACK ― 第三者JavaScriptを「本番コード」として管理する

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-11-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">November 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-11-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-11-24</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Software Supply Chain / Third-party Risk / C-SCRM / Security Governance &amp; Risk Management</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Web Engineering / Third-party Risk</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Supply Chain / Customer Data / Web Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Mixed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Optimizelyは、2026年11月16日にWeb Experimentationのアカウント登録フローの欠陥が悪用され、攻撃者が対象顧客の管理者を偽装してProject JavaScriptへ悪意あるコードを挿入したと報告した。最初のコード書き込みは07:51 UTC、検知は13:34、脆弱性の修正は16:10、全対象プロジェクトからのコード削除は22:24だった。悪意あるコードは対象ページを訪れた利用者のブラウザで実行され、オンページのカード入力や暗号資産送金を狙ったとされる。[^optimizely]

Unit 42はこの活動をOPTIMJACKと呼び、少なくとも178組織のサイト訪問者へコードが配信されたと報告した。一方、Optimizelyは11月19日更新の公式アドバイザリで、影響を受けた顧客は5%未満と報告した。両者の指標は異なり、実際の情報窃取被害数を示すものではない。[^advisory]Libraryは、被害数を一つの確定値にまとめず、観測主体別の主張として扱う。本件の本質は、正規CDNと正規証明書から配信される第三者スクリプトでも、ページ上では自社コードと同等の権限を持つ点にある。

</div>

## なぜ今なのか

従来のソフトウェアサプライチェーン対策は、パッケージ、ビルド、署名を中心に設計されがちだった。OPTIMJACKは、マーケティングやA/Bテスト用の動的スクリプトも、顧客入力へ到達できれば同じ経営リスクを持つことを示す。導入部門がマーケティングであっても、実行権限は本番Webアプリケーションの一部である。

既存のAxiosやnpm侵害記事とは、侵害された信頼経路が異なる。本件はビルド時の依存関係ではなく、利用者のブラウザへ都度配信される設定可能なJavaScriptが攻撃面となった。したがって、SBOMだけでなく、タグ管理、Project JavaScript変更権限、CSP、決済フォーム分離、ブラウザ送信先監視が統制対象になる。

## 何が起きているのか

### 確認できた事実

Optimizelyの初期報告では、対象はWeb Experimentationに限定され、Feature Experimentation、SDK、legacy Full Stackへの影響は確認されていない。これはパスワード窃取による侵害ではなく、登録フローの欠陥により管理者として振る舞えた事案とされる。公式報告時点でフォレンジック調査は継続中であり、根本原因と最終IoCは確定前だった。[^optimizely]

### 情報源の主張と差異

Unit 42とOptimizelyの報告では、カード情報や暗号資産を狙う活動が示されている。

Unit 42の「少なくとも178組織」とOptimizelyの「顧客の5%未満」は両立し得るが、同じ測定ではない。本文ではどちらも発行主体の主張として明示し、確定した被害者数とは表現しない。

### Libraryの評価

第三者スクリプトのリスクは、ベンダーの安全性だけでは管理できない。自社側で、どのページに読み込むか、何へアクセスできるか、どこへ通信できるかを制限する「利用側の封じ込め」が必要である。特に決済、認証、個人情報入力ページでは、不要タグの排除とCross-origin iframeによる分離は直接アクセスの抑制に役立つが、親ページの改ざんや偽フォームへの誘導までは防げない。

## 経営インパクト

- **顧客接点の侵害**：自社サーバーが直接侵害されなくても、顧客のブラウザ上で情報窃取が成立し得る。
- **委託先責任の再定義**：SaaS導入審査だけでなく、継続的な設定変更権限、ログ、通知、緊急停止手順が必要になる。
- **規制・法務判断**：影響はページ構成、露出時間、CSP、入力方式で異なる。ベンダーの一律説明だけでは、自社の通知義務や顧客対応を判断できない。
- **事業速度との衝突**：マーケティングタグの迅速な追加と、本番コード相当の変更管理をどう両立するかが経営課題になる。

## 日本企業への示唆

国内企業では、タグ管理やA/Bテスト基盤がWeb制作会社・広告代理店・事業部門にまたがり、セキュリティ部門が全実行コードを把握できない場合がある。まず「誰がどのページへ何を配信できるか」を可視化し、決済・認証・会員情報ページを別のリスク区分にする必要がある。

インシデント時には、ベンダーからの影響通知だけを待たず、自社のCSP違反レポート、ブラウザの外向き通信、タグ変更履歴、対象時間帯の決済・不正利用情報を保全する。Hosted Payment iframeの利用有無など、実装差が実被害を左右する。

<div class="sil-action-box" markdown>

## 推奨アクション

1. 認証・決済・個人情報入力ページから不要なマーケティング、分析、A/Bテスト用スクリプトを除外する。
2. 決済入力を別オリジンのiframeへ分離し、CSPで実行元・通信先を制限する。Report-Onlyで影響を確認してから強制モードへ移行する。ただし、許可済み配信元の改ざんや親ページ上の偽フォームをCSPだけで防げるとは限らない。
3. 第三者スクリプトとタグ管理基盤の管理者、変更履歴、API token、緊急停止手順を台帳化する。
4. Web Experimentation利用企業は、2026年11月16日の対象時間帯について、Optimizelyの個別通知と自社ログを照合し、法務・決済・顧客対応を含む影響評価を行う。

</div>

## 用語解説

- **Project JavaScript**：Optimizely Web Experimentationのプロジェクト単位で配信されるカスタムJavaScript。
- **CSP**：ブラウザが実行・接続できる送信元を制限するContent Security Policy。
- **Cross-origin iframe**：別Originに隔離された埋め込み領域。親ページのスクリプトからの直接アクセスを制限できる。

## 関連記事

- [Axios Supply Chain Compromise ― Build Dependency侵害がCode Signing Trustまで到達した](openai-axios-signing-supply-chain.md)
- [Mastra npm Supply Chain Compromise ― AI Frameworkも「開発者のTrust」を狙われる](mastra-npm-ai-supply-chain.md)
- [Mini Shai-Hulud ― npm Supply ChainがCI/CD Credential Theftへ直結する](mini-shai-hulud-antv.md)

## 参考情報

- [Optimizely: Security Incident Initial Report for Customers](https://pages.optimizely.com/rs/947-RKE-048/images/Security%20Incident%20Report%20-%20Optimizely%20Web%20Experimentation%20-%20Nov%2017%202026.pdf)
- [Optimizely: Security Advisory — Web Experimentation Security Incident](https://support.optimizely.com/hc/en-us/articles/50521849710605-Security-Advisory-Web-Experimentation-Security-Incident-Updated-November-19-2026)
- [Unit 42: Borrowed Code, Real Consequences: What OPTIMJACK Teaches Us](https://unit42.paloaltonetworks.com/optimjack-supply-chain-attack/)

[^optimizely]: Optimizely, “Security Incident Initial Report for Customers – Web Experimentation,” 2026-11-17（2026-11-24確認）。

[^advisory]: [Optimizely Security Advisory（2026-11-19更新）](https://support.optimizely.com/hc/en-us/articles/50521849710605-Security-Advisory-Web-Experimentation-Security-Incident-Updated-November-19-2026)。

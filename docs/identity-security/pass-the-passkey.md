---
title: Passkeyは破られたのか ― Pass-ta-keyとPass-the-Passkeyから学ぶ
date: 2026-08-10
updated: 2026-08-26
description: 2026年に公開されたPass-ta-keyとPass-the-Passkeyを整理し、Passkeyの暗号方式ではなく実装・端末・回復フローが攻撃面になることを解説する。
category: Identity Security
tags:
- Identity Security
- Passkey
- FIDO2
- WebAuthn
- Google Password Manager
- Endpoint Security
audience:
- CISO
- IAM Architect
- Security Engineer
management_impact: High
urgency: Near-term
evidence: Observed
status: published
pptx: ''
---

# Passkeyは破られたのか ― Pass-ta-keyとPass-the-Passkeyから学ぶ

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-10</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">CISO / IAM Architect / Security Engineer</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Near-term</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

2026年に公開されたPasskey関連研究は、「Passkeyの公開鍵暗号が破られた」ことを示すものではありません。主に狙われたのは、**侵害済み端末上の実装、同期PasskeyのCloud Authenticator、User Verification (UV) の扱い、オンボーディングや回復フロー、ログやメモリ**です。[^source]

特にUnit 42のPass-ta-key研究はGoogle Password Manager / Chrome / Windowsを対象に、端末上にマルウェアが存在する前提で、User Verificationを迂回したり、同期Passkeyを復号可能にしたりする攻撃を示しました。一方、SpecterOpsの「Pass-the-Passkey」はWebAuthn/FIDO2の実装・認証フローを対象とした別系統の研究群です。

したがって結論は、**Passkeyをやめることではなく、Passkeyを「端末侵害・回復・同期・RP検証を含むシステム」として設計すること**です。

</div>

## なぜ今なのか

Passkeyはフィッシング耐性が高く、パスワードやOTPの多くの弱点を減らします。その一方、普及が進めば攻撃者は「秘密鍵を直接盗む」以外の方法を探します。2026年の研究は、まさにその攻撃面が**Passkey周辺の実装・端末・Cloud同期**へ移っていることを示しました。

## まず用語を分ける

### Pass-ta-key ― Unit 42

Unit 42が2026年8月3日に公開した研究で、Google Password Managerの同期PasskeyとCloud Authenticatorを対象にしています。研究では次の3種類が整理されています。

- **Pass-ta-key**: 侵害済み端末上の非特権マルウェアから、ユーザー操作や端末UnlockなしでPasskey認証を悪用するシナリオ
- **Silver Pass-ta-key**: UV Keyの登録フローを悪用し、攻撃者側のKeyをUser Verification用として登録するシナリオ
- **Golden Pass-ta-key**: Security Domain Secret (SDS) を得て、同期Passkeyの秘密鍵を復号するシナリオ

Unit 42は、すべての攻撃が**初期段階で被害端末にマルウェアが存在することを前提**としていると明記しています。

### Pass-the-Passkey ― SpecterOps

SpecterOpsがBlack Hat USA 2026で扱った研究群は、Windows上のWebAuthn/FIDO2認証フロー、Assertionの捕捉・再利用、実装上の挙動などを対象としています。名前は似ていますが、Unit 42のPass-ta-keyとは別の研究です。

## User Verification (UV) は何を保証するのか

WebAuthnでは、Authenticatorが端末ローカルで利用者を確認したかどうかをUVフラグでRelying Party (RP)へ伝えます。Googleの開発者向け資料でも、常にUser Verificationを要求したい場合は `userVerification = "required"` とし、サーバ側でUVを検証する考え方が示されています。

Unit 42研究の重要な点は、「UV=requiredなら端末侵害後も絶対安全」という単純な前提を崩したことです。Silver Pass-ta-keyでは、本来のUV Keyを直接抜き出すのではなく、**新しい攻撃者制御KeyをCloud Authenticatorへ登録する**ことでUV済みのように扱わせる経路を示しました。

つまり、UVそのものの概念が無意味なのではなく、**UV Keyの登録・Attestation・回復フローを誰が信頼するか**まで含めて保証する必要があります。

## 「秘密鍵がTPMから抜けなければ安全」ではない

デバイスバウンドKeyがTPM等から直接抽出できないことは重要です。しかし端末が侵害されると、攻撃者はKeyそのものを抜く代わりに、

- 正規プロセスに署名させる
- オンボーディング状態を操作する
- 同期データやメモリから別の秘密情報を狙う
- 回復・再登録機能を悪用する

といった方法を取れます。これはPasskeyに限らず、ハードウェア保護Credential全般で重要な脅威モデルです。

## 経営インパクト

| 誤解 | 実際の論点 |
| --- | --- |
| PasskeyならEndpoint Securityは不要 | 端末侵害は依然として重要な前提条件 |
| 秘密鍵を抽出できなければ安全 | 署名オラクル、回復、再登録、同期が攻撃面になる |
| UV=requiredだけで十分 | RP側検証に加え、Authenticator側のUV Key管理も重要 |
| Passkeyは「一つの製品機能」 | RP、Browser、OS、Authenticator、Cloud同期の連鎖 |
| 研究が出たのでPasskeyは危険 | Password/OTPより減らせる攻撃面は依然大きい |

## 日本企業への示唆

Passkey導入を中止する理由にはなりません。むしろ、パスワード・SMS/OTP・Push型MFAに比べてフィッシング耐性を高める価値は大きいままです。ただし、導入判断を「FIDO対応か」だけで終わらせず、同期方式、端末保護、回復、RP実装を評価します。

特に高権限管理者や重要業務では、同期PasskeyとデバイスバウンドFIDO Security Keyをどう使い分けるか、端末侵害時の再認証・Credential失効をどう行うかを決めておくべきです。

<div class="sil-action-box" markdown>

## 推奨アクション

1. **RPでUser Verificationを必要な用途に対して明示的に要求し、UVフラグを検証する。**
2. **Passkey Provider / Credential Managerの同期・回復・デバイス登録設計を評価する。**
3. **EDR、Browser更新、OS更新、Credential Guard相当のEndpoint対策を維持する。**
4. **高権限アカウントではデバイスバウンドAuthenticatorを含む強い方式を検討する。**
5. **MFA/Passkey再登録・アカウント回復を高リスク操作として監視する。**
6. **Passkey失効・端末紛失・端末侵害を想定したRecovery Runbookをテストする。**
7. **「Passkey導入率」だけでなく、フィッシング可能なFallback認証の残存率を追う。**

</div>

## 用語解説

**UV (User Verification)**  
Authenticatorが、PINや生体認証等を用いて端末ローカルで利用者を確認したことを示すWebAuthn上の情報。

**UV Key**  
Google Password ManagerのCloud Authenticator実装で、OSのUser Verificationと関連付けられるKey。WebAuthn一般の標準用語としての「同期Passkeyの必須構成要素」ではなく、特定実装の内部概念として理解する必要がある。

**SDS (Security Domain Secret)**  
Unit 42が分析したGoogle同期Passkey実装で、同期Passkeyの秘密データ保護に使われるMaster Secret。

**Relying Party (RP)**  
WebAuthn/Passkeyを使って利用者を認証するWebサイトやサービス側。

## 関連記事

- [Large-Scale Credential Attacks ― 「ログインして侵入する」攻撃へのIdentity Security](../cybersecurity/large-scale-credential-attacks.md)


## 参考情報

- [Palo Alto Networks Unit 42, Pass the Passkey: A Novel Attack Surface in Passwordless Authentication (2026-08-03)](https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/)
- [SpecterOps, Pass-the-Passkey Family of Attacks](https://github.com/SpecterOps/pass-the-passkey)
- [Google for Developers, Implement passkeys with form autofill in a web app](https://developers.google.com/codelabs/passkey-form-autofill)
- [NIST SP 800-63B-4, Digital Identity Guidelines: Authentication and Authenticator Management](https://doi.org/10.6028/NIST.SP.800-63B-4)
[^source]: [Palo Alto Networks Unit 42, Pass the Passkey: A Novel Attack Surface in Passwordless Authentication (2026-08-03)](https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/)
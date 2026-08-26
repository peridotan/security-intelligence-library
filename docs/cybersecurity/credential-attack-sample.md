---
title: Large-Scale Credential Attacks
date: 2026-08-19
description: 大規模な資格情報攻撃をIdentity Securityの観点から整理するサンプル記事。
tags:
  - Cybersecurity
  - Identity Security
  - Credential Attack
  - MFA
status: sample
---

# Large-Scale Credential Attacks

> **Sample** — Webサイトの構成確認用です。正式版では一次情報を再確認し、確認済み事実と攻撃者側の主張を明確に分離します。

## Executive Summary

資格情報を狙う攻撃では、単一の認証方式だけを見るのではなく、漏えい資格情報、Password Spraying、MFA、端末・Edge Device、Identity Provider、アカウント回復までを一つの攻撃チェーンとして捉える必要があります。

## なぜ今なのか

認証強化が進む一方で、攻撃者はMFA Fatigue、既存セッション、設定ファイル、ヘルプデスク回復フローなど、認証の周辺プロセスへ狙いを広げています。

## 攻撃チェーンの例

1. 漏えい済み資格情報を収集
2. Password Spraying / Credential Stuffing
3. MFA突破や回復フローを狙う
4. Edge DeviceやクラウドIdentityへ侵入
5. 権限昇格・横展開
6. 永続化と追加資格情報の取得

## 経営インパクト

Identity侵害はクラウド、SaaS、VPN、管理者権限など複数環境へ連鎖しやすく、単なる「パスワード問題」ではありません。Identityを独立したセキュリティ境界として管理する必要があります。

## 推奨アクション

- Passkeyなどフィッシング耐性認証の採用
- Conditional Accessの強化
- ITDRによるIdentity異常検知
- PAMによる高権限管理
- NHIの棚卸しと資格情報管理
- ヘルプデスク回復フローの本人確認強化
- 漏えい資格情報の継続監視

## 参考情報

正式版作成時に一次情報URLを記載します。

---
title: Large-Scale Credential Attacks ― 「ログインして侵入する」攻撃へのIdentity Security
date: 2026-08-19
updated: 2026-08-26
reviewed: '2026-08-26'
review_status: Current
source_period: 2026-08
description: Unit 42の大規模資格情報攻撃レポートを基に、確認済み事実と攻撃者主張を分け、Identity Security対策を整理する。
category: Cybersecurity
collections:
- cybersecurity
- identity-security
topics:
- Credential Attacks
- Identity Security
tags:
- Cybersecurity
- Identity Security
- Credential Attack
- Password Spraying
- MFA Fatigue
- Microsoft Entra
- Edge Device
mitre_attack:
- id: T1110.003
  basis: Analyst-mapped
  note: Password Sprayingとして確認・整理された攻撃パターンに対応。TheHatman固有の侵入経路を確定するものではない。
- id: T1110.002
  basis: Analyst-mapped
  note: 取得済みCredential Materialをオフライン解析してPasswordを回復する段階に対応。
- id: T1552.001
  basis: Analyst-mapped
  note: Network機器等の設定ファイルから保存Credentialを取得する行動に対応。
- id: T1078
  basis: Analyst-mapped
  note: 取得・漏えい済みCredentialを正規Loginとして再利用する行動に対応。
audience:
- Executive
- CISO
- Security Operations
management_impact: High
impact_types:
- Identity
- Operational Security
urgency: Immediate
evidence: Mixed
status: published
pptx: ''
media_rights: none
---
# Large-Scale Credential Attacks ― 「ログインして侵入する」攻撃へのIdentity Security

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-19</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">August 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Credential Attacks / Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / Security Operations</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Identity / Operational Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Mixed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Unit 42は2026年8月18日、Large-Scale Credential AttacksのThreat Briefを更新し、TheHatmanとFortiBleedに関する情報を整理しました。重要なのは、攻撃者が必ずしも新しいマルウェアやゼロデイで侵入するとは限らず、**漏えい資格情報を集め、Password Sprayingを行い、Edge DeviceやクラウドIdentityへ「正規ログイン」する**攻撃が大規模化していることです。[^source]

TheHatmanについては、Microsoft Entraテナントから情報を窃取した、MFA FatigueやPassword Sprayingを使った、という点は**攻撃者自身の主張であり、Unit 42は侵入経路を検証できていません**。この区別を保ったまま、Passkey、Conditional Access、ITDR、PAM、NHI、ヘルプデスク回復、漏えいCredential監視を一つのIdentity Securityモデルとして統合することが重要です。

</div>

## なぜ今なのか

パスワード侵害は古いテーマですが、攻撃の運用モデルが変わっています。大量のCredentialを一度取得して終わりではなく、取得したCredentialを次のPassword Sprayingへ再投入し、さらに新しいCredentialを増やす**循環型の攻撃資産**として使う動きが見られます。

また、VPN、Firewall、Remote Access、SaaS、Microsoft Entraなど、企業の境界がIdentityへ寄るほど、「侵入する」より「ログインする」方が攻撃者にとって効率的になります。

## 確認済み事実と未確認の主張

### Unit 42が確認・観測した内容

- FortiBleedと呼ばれる大規模なPassword Spraying / Credential窃取キャンペーンがFortinet機器を中心に報告された。
- Unit 42はMSSQLへの試行を観測し、Sophos機器が狙われたとの報告にも言及している。
- 攻撃プロセスとして、Password Spraying → 権限に応じた設定取得 → 保存Credentialのオフライン解析 → 追加攻撃への再利用、という循環を整理している。
- Unit 42は、大量のログイン失敗の直後に成功ログインが続くパターン等をリモートアクセスログで確認することを推奨している。

### TheHatmanの主張 ― Unit 42は未検証

2026年8月1日から17日にかけて、TheHatmanを名乗るActorが複数企業の従業員情報を販売すると投稿し、Microsoft Entraテナントから情報を窃取したと主張しました。さらに、MFA FatigueやPassword Sprayingで侵入したとも主張しています。

ただしUnit 42は、**特定の侵入ベクトルを検証できておらず、これらの攻撃手法の主張も検証していない**と明記しています。したがって、「TheHatmanがMFA Fatigueで侵入したことが確認された」と表現するのは不正確です。

## 攻撃チェーンとして整理する

<div class="sil-flow" role="group" aria-label="Credential attack chain">
  <div class="sil-flow-step"><strong>過去の漏えいCredential / 攻撃で得たCredential</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>Password Spraying</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-branches">
    <div class="sil-flow-step">
      <strong>Edge Device</strong>
      <span>Fortinet等</span>
    </div>
    <div class="sil-flow-step">
      <strong>Cloud Identity</strong>
      <span>Microsoft Entra等</span>
    </div>
  </div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>MFA / Recovery / Sessionの突破を試行</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>設定ファイル・Secret・追加Credential</strong></div>
  <div class="sil-flow-arrow">↓</div>
  <div class="sil-flow-step"><strong>オフライン解析 / 権限昇格 / 永続化</strong></div>
  <div class="sil-flow-loop">↺ 新たなCredentialを次の攻撃へ再利用</div>
</div>

ここで重要なのは、**Credential AttackとEdge Device Attackを別々に管理しないこと**です。設定ファイルからCredentialが得られると、ネットワーク機器の侵害がIdentity侵害へ変わり、逆にIdentity侵害から管理インターフェースへ横展開できます。

<!-- AUTO:MITRE:START -->
## MITRE ATT&CK® Mapping

<div class="sil-mitre-note" markdown>

この表は、攻撃・Campaignの理解に有用な場合だけ表示します。`Source-labeled` は一次情報がATT&CK IDを明示したもの、`Analyst-mapped` は一次情報に記載された行動を本LibraryがATT&CKへ対応付けたものです。後者は、元情報の発行者がそのATT&CK IDを明示したことを意味しません。

</div>

| Technique | Tactic | Basis | Article context |
| --- | --- | --- | --- |
| [T1110.003 Password Spraying](https://attack.mitre.org/techniques/T1110/003/) | Credential Access | Analyst-mapped | Password Sprayingとして確認・整理された攻撃パターンに対応。TheHatman固有の侵入経路を確定するものではない。 |
| [T1110.002 Password Cracking](https://attack.mitre.org/techniques/T1110/002/) | Credential Access | Analyst-mapped | 取得済みCredential Materialをオフライン解析してPasswordを回復する段階に対応。 |
| [T1552.001 Credentials In Files](https://attack.mitre.org/techniques/T1552/001/) | Credential Access | Analyst-mapped | Network機器等の設定ファイルから保存Credentialを取得する行動に対応。 |
| [T1078 Valid Accounts](https://attack.mitre.org/techniques/T1078/) | Initial Access, Persistence, Privilege Escalation, Defense Evasion | Analyst-mapped | 取得・漏えい済みCredentialを正規Loginとして再利用する行動に対応。 |

<div class="sil-mitre-legal">
MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation. © 2026 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation.
</div>
<!-- AUTO:MITRE:END -->

## 経営インパクト

| 観点 | リスク | 経営上の意味 |
| --- | --- | --- |
| クラウド | 正規CredentialでSaaS/Entraへアクセス | 「マルウェア未検知」でも情報流出が起こる |
| Edge | VPN/Firewall設定からCredential取得 | 境界機器侵害がIdentity全体へ波及 |
| MFA | Push型MFAへの疲労攻撃や回復フロー悪用 | MFA導入済みだけでは十分でない |
| 特権 | 一般Credentialから管理権限へ拡大 | PAM・PIMの成熟度が被害規模を左右する |
| 監査 | 正常ログインと悪用の区別が難しい | Identity telemetryと行動分析が重要 |

## 日本企業への示唆

日本企業では、Credential AttackをMFA製品単体の問題ではなく、**認証・端末・特権・回復・漏えい資格情報・NHIを横断するIdentity Securityの問題**として扱う必要があります。特にヘルプデスク回復、Edge Device、特権経路、漏えい資格情報の再利用を同じ攻撃チェーン上で確認することが重要です。

### 日本企業向けIdentity Securityモデル

### 1. Prevent ― 盗まれても使いにくくする

- Passkey / FIDO2等のフィッシング耐性認証
- Password Spray耐性のある認証ポリシー
- Conditional Accessによる端末、場所、リスク、アプリ条件の評価
- Legacy Authenticationの廃止

### 2. Limit ― 侵害後の権限を絞る

- PAM/PIMで管理者権限をJIT化
- Service Account / NHIの所有者・権限・Credentialを棚卸し
- Edge Deviceの管理面をインターネットから隔離
- 設定バックアップに含まれるSecretを最小化・保護

### 3. Detect ― 正規ログインの悪用を見つける

- ITDR / SIEMでPassword Spray、Impossible Travel、異常なToken利用、管理者操作を相関分析
- 大量失敗の直後の成功ログインを重点監視
- Dark Web / 漏えいCredential監視を継続
- Edge Deviceの認証ログとEntra/SaaSログを横断分析

### 4. Recover ― 強い認証を回復フローで迂回させない

- ヘルプデスクの本人確認を強化
- MFA再登録、Passkey再発行、電話番号変更を高リスク操作として扱う
- 回復操作の監査ログを残し、異常時は高権限アクセスを制限

<div class="sil-action-box" markdown>

## 推奨アクション

1. **過去30日分の認証ログを確認**し、大量失敗後の成功ログイン、海外・匿名化ネットワーク、異常な管理者ログインを抽出する。
2. **外部公開Edge Deviceの管理面を棚卸し**し、MFA、管理アクセス制限、最新アップデート、設定ファイル内Credentialを確認する。
3. **Passkey / FIDO2の優先導入対象**を管理者、VPN/リモートアクセス、高価値SaaSから決める。
4. **Conditional AccessとITDRを統合**し、「正しいCredential」でもコンテキストが異常なら止める。
5. **PAMとNHI管理**で、侵害Credentialから特権・Service Accountへ横展開できる経路を減らす。
6. **ヘルプデスク回復フローを攻撃シナリオでテスト**し、MFAリセットが弱点になっていないか確認する。
7. **漏えいCredential監視**をインシデント対応へ接続し、発見後の強制リセット・Token失効までの時間をKPI化する。

</div>

## 用語解説

**Password Spraying**  
少数のよく使われるパスワードを、多数のアカウントへ試す攻撃。アカウントロックを回避しやすい。

**MFA Fatigue**  
攻撃者がMFA Push通知を大量に送り、利用者の誤承認や混乱を狙う手法。

**ITDR**  
Identity Threat Detection and Response。Identityの設定・権限・認証イベントを監視し、侵害や悪用を検知・対応する考え方・機能群。

## 関連記事

- [AI Agent Identity / NHI ― AI Agentを「操作主体」として統制する](../identity-security/ai-agent-identity-nhi.md)
- [Passkeyは破られたのか ― Pass-ta-keyとPass-the-Passkeyから学ぶ](../identity-security/pass-the-passkey.md)


## 参考情報

- [Palo Alto Networks Unit 42, Threat Brief: Mitigating Large-Scale Credential Attacks (Updated August 18, 2026)](https://unit42.paloaltonetworks.com/large-scale-credential-attacks/)
[^source]: [Palo Alto Networks Unit 42, Threat Brief: Mitigating Large-Scale Credential Attacks (Updated August 18, 2026)](https://unit42.paloaltonetworks.com/large-scale-credential-attacks/)
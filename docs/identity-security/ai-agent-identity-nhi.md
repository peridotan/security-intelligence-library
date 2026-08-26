---
title: AI Agent Identity / NHI ― AI Agentを「操作主体」として統制する
date: 2026-08-26
updated: 2026-08-26
description: AI AgentとNon-Human Identityを、人・Agent・Credential・Actionの監査可能な連鎖として管理するための考え方を整理する。
category: Identity Security
tags:
  - Identity Security
  - AI Agent
  - NHI
  - PAM
  - Secrets Management
  - Agentic AI
audience:
  - Executive
  - CISO
  - IAM Architect
management_impact: High
status: published
pptx: ""
---

# AI Agent Identity / NHI ― AI Agentを「操作主体」として統制する

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Identity Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">Executive / CISO / IAM Architect</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

AI Agentは、単に回答を返すアプリケーションではなく、SaaS、クラウド、コードリポジトリ、業務システムへ接続し、**人の代わりに操作を実行する主体**になりつつあります。そのため「AgentそのもののIdentity」と「Agentが利用するNHI・Credential」を分けて管理し、誰の委任で、どの権限を使い、何を実行したかを追跡できる設計が必要です。

目標は、**Human → Agent → NHI / Credential → Action** の連鎖を監査可能にすることです。新しい専用製品を先に選ぶのではなく、既存のIAM、PAM、Secrets Management、SIEMをAgentまで拡張し、委任・最小権限・短命資格情報・実行時統制・監査の原則を先に定めます。

</div>

## なぜ今なのか

2026年、AI Agentの業務利用は急速に現実化しています。1Passwordが紹介した451 Researchの調査では、Agentic AIのIdentity Securityについて、Agentと未統制NHIの可視化、Just-in-Time資格情報、監査可能性、実行時権限の管理が主要論点として挙げられています。

同時にCloud Security Allianceは、NHIを人以外の主体として整理し、所有者不明、過剰権限、可視性不足、静的Secret露出などを主要リスクとして示しています。OWASP Top 10 for Agentic Applications 2026でも、Identity & Privilege AbuseはAgentic AIの主要リスクです。

つまり、AI Agentのセキュリティは「プロンプトインジェクション対策」だけでは不十分です。**Agentが何者として、何のCredentialを使い、どこまで操作できるか**というIdentity設計が基盤になります。

## まず区別すべき4つ

| 要素 | 意味 | 例 |
| --- | --- | --- |
| Human Identity | Agentへ指示・委任する人 | 従業員、管理者、開発者 |
| Agent Identity | AI Agentを一つの操作主体として識別するIdentity | 調達Agent、SOC Agent、開発Agent |
| NHI | 人以外のシステム主体 | Service Account、Workload Identity、Bot |
| Credential | Identityが認証・認可に使う証明情報 | OAuth token、API key、証明書、短命token |

AI AgentとNHIは重なる場合がありますが、同一概念ではありません。Agentが自分専用のWorkload Identityを持つ場合もあれば、既存Service AccountのCredentialを借りて操作する場合もあります。重要なのは、**「誰が主体か」と「何を使って認証したか」を分離して記録すること**です。

## 従来のIAM/PAMでは足りないのか

「従来IAM/PAMはAgentic AIに構造的に不十分」という強い主張もあります。Agentは非決定的に動き、事前にすべての操作を列挙するのが難しいため、この問題提起には妥当性があります。

ただし、既存のIAM/PAM/Secrets/SIEMが無意味になるわけではありません。むしろ実務では、次のように**既存統制をAgentまで拡張する**のが現実的です。

- IAM: Agent Identity、所有者、ライフサイクル、認証・認可
- PAM/PIM: 高権限操作のJIT化、承認、セッション制御
- Secrets Management: API KeyやTokenの保管・発行・ローテーション
- SIEM/ITDR: Agentの異常なIdentity利用や権限乱用の検知
- API Gateway / Policy Engine: 実行時に操作内容・対象・条件を検査

課題は「既存製品を捨てること」ではなく、**Human中心だった統制モデルをHuman + Machine + Agentへ拡張すること**です。

## 目標アーキテクチャ

```text
Human
  │  委任・承認
  ▼
AI Agent Identity
  │  JIT / 短命Credential要求
  ▼
Credential Broker / PAM / Secrets
  │  最小権限Token
  ▼
Target System / API / SaaS
  │
  └── Audit → Human / Agent / Credential / Action を関連付け
```

特に重要なのは**Standing Privilegeを減らすこと**です。長期有効なAPI Keyや広すぎるService AccountをAgentへ渡すと、Agentの誤動作、Prompt Injection、Credential漏えいのいずれでも被害範囲が大きくなります。

## 経営インパクト

| 観点 | リスク | 経営上の意味 |
| --- | --- | --- |
| 責任追跡 | Agentの操作を人に紐付けられない | 事故・不正時に説明責任を果たせない |
| 権限 | Agentに常設の高権限 | 誤動作・侵害時のBlast Radius拡大 |
| Secret | API Key等がローカルや設定ファイルに残る | 漏えい後も長期間悪用される |
| 開発速度 | 統制が重すぎる | Shadow Agent / Shadow NHIを誘発 |
| 監査 | Agentの判断と実行が分断 | 内部統制・規制対応が困難 |

## 日本企業への示唆

AI Agent導入を「生成AI利用申請」の延長だけで扱うと、実際のアクセス権限が見えなくなります。特に、PoCから本番へ移るタイミングで開発者個人のAPI Key、共有Service Account、長期Tokenが残りやすいため、Agentを本番化する条件としてIdentity設計を明確化する必要があります。

また、Agentのすべての操作を人間が事前承認する設計では、自動化の価値を失います。高リスク操作だけを承認対象にし、低リスク操作はPolicy Engineで自動許可するなど、**リスクに応じたHuman-in-the-Loop**が現実的です。

<div class="sil-action-box" markdown>

## 推奨アクション

### 0–30日: 見える化

1. AI Agent、Service Account、API Key、Secret、高権限・長期Credentialを棚卸しする。
2. 各AgentにBusiness OwnerとTechnical Ownerを割り当てる。
3. 「Human → Agent → Credential → Action」がログで関連付けられるか確認する。

### 31–90日: Standing Privilegeを減らす

4. 高権限・長期Credentialから、JIT、短命Token、Vault / Credential Broker方式へ移行する対象を決める。
5. Agentごとに最小権限Scopeを定義し、共有Service Accountを減らす。
6. AgentによるCredential取得、権限変更、高リスク操作をSIEM/ITDRへ送る。

### 90日以降: Runtime Authorityを統制する

7. 操作内容・対象・データ分類・時間帯等を使い、実行時Policyで許可・拒否・承認要求を判断する。
8. Agentの異常動作時にCredentialを即時失効し、Agentを停止できるKill Switchを用意する。
9. 「未管理Agent数」「Standing Privilege比率」「短命Credential比率」「帰属不能操作数」を経営指標として追う。

</div>

## 用語解説

**Agentic AI**  
目標を与えられると、計画、ツール利用、判断、複数ステップの実行を一定範囲で自律的に進めるAIシステム。

**NHI (Non-Human Identity)**  
Service Account、Workload、Bot、Agentなど、人間ではない主体を識別・認証・認可するためのIdentity。

**Standing Privilege**  
必要な時だけではなく、常時付与されている権限。侵害時の被害範囲を広げやすい。

**JIT Credential**  
Just-in-Time Credential。必要な操作時に限定して発行される短期間の資格情報。

**Runtime Authority**  
静的なRoleだけでなく、実行時の状況や操作内容を含めて「今この操作を許可するか」を評価する考え方。

## 関連記事

- [生成AI利活用ガバナンス ― 禁止事項だけでなく「安全に使える仕組み」を作る](../ai-security/generative-ai-governance.md)
- [Large-Scale Credential Attacks ― 「ログインして侵入する」攻撃へのIdentity Security](../cybersecurity/large-scale-credential-attacks.md)

## PowerPoint

対応する公開可能なPowerPoint版は、今後このページからリンクします。

## 参考情報

- 1Password, 451 Research report: How agentic AI is redefining identity security (2026-08-20)  
  https://1password.com/blog/how-agentic-ai-is-redefining-identity-security
- Cloud Security Alliance, Defining Non-Human Identity (2026-07-22)  
  https://cloudsecurityalliance.org/artifacts/defining-non-human-identity
- OWASP Gen AI Security Project, Top 10 for Agentic Applications for 2026  
  https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- OWASP Gen AI Security Project, Agentic Security Initiative  
  https://genai.owasp.org/initiatives/agentic-security-initiative/

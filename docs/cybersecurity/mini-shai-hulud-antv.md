---
title: Mini Shai-Hulud ― npm Supply ChainがCI/CD Credential Theftへ直結する
date: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_status: Current
source_period: 2026-05
description: Microsoftが2026年5月20日に公表した@antv npm Supply Chain攻撃を基に、Maintainer Account、Transitive
  Dependency、CI/CD Secret、Cloud Credentialの連鎖Riskを整理する。
category: Cybersecurity / Software Supply Chain
collections:
- cybersecurity
- risk-management
topics:
- Software Supply Chain
- Credential Attacks
- Third-party Risk / C-SCRM
tags:
- Mini Shai-Hulud
- npm
- antv
- GitHub Actions
- CI/CD
- SLSA
- Credential Theft
audience:
- CISO
- DevSecOps
- Cloud Security
- Software Engineering
management_impact: High
impact_types:
- Supply Chain
- Credential Risk
- Cloud Security
urgency: Immediate
evidence: Observed
status: published
pptx: ''
media_rights: none
---

# Mini Shai-Hulud ― npm Supply ChainがCI/CD Credential Theftへ直結する

<div class="sil-article-meta">
  <div class="sil-meta-item"><span class="sil-meta-label">Published</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Source Period</span><span class="sil-meta-value">May 2026</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Updated</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Last Reviewed</span><span class="sil-meta-value">2026-08-26</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Review Status</span><span class="sil-review-current">Current</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Category</span><span class="sil-meta-value">Cybersecurity / Software Supply Chain</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Topics</span><span class="sil-meta-value">Software Supply Chain / Credential Attacks / Third-party Risk / C-SCRM</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Audience</span><span class="sil-meta-value">CISO / DevSecOps / Cloud Security / Software Engineering</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Impact Areas</span><span class="sil-meta-value">Supply Chain / Credential Risk / Cloud Security</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Management Impact</span><span class="sil-impact-high">High</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Urgency</span><span class="sil-meta-value">Immediate</span></div>
  <div class="sil-meta-item"><span class="sil-meta-label">Evidence</span><span class="sil-meta-value">Observed</span></div>
</div>

<div class="sil-executive-summary" markdown>

## Executive Summary

Microsoftは2026年5月20日、@antvのnpm Maintainer Accountが侵害され、広く利用されるPackageの悪意あるVersionを通じてCI/CD Credentialを窃取するSupply Chain Attack「Mini Shai-Hulud」を報告しました。PayloadはGitHub、AWS、Vault、npm、Kubernetes、1Password等のCredentialを探索し、Dependency Chainを通じて下流Projectへ影響を拡大しました。[^source]

GitHubは対応として640の悪意あるPackageを削除し、Write権限と2FA bypassを持つ61,274のnpm Granular Access Tokenを無効化したとMicrosoftは報告しています。**Software Dependencyの侵害がBuild System Identityの侵害へ直結する**ことを示す事例です。

</div>

## なぜ今なのか

Software Supply Chainの価値はSource Codeそのものだけではありません。CI/CD PipelineにはPackage Publish Token、Cloud Credential、Signing Material、Deployment Credential等の高価値Secretが集中しています。

Maintainer Accountが侵害されると、正規Package Updateを通じて多数の組織へPayloadを配布できます。

## 攻撃Chain

1. npm Maintainer Accountを侵害
2. 正規Scopeで悪意あるPackage VersionをPublish
3. Downstream Dependencyへ自動伝播
4. npm install時のScriptでPayload実行
5. CI/CD / Cloud / Developer Credentialを探索
6. Stolen Tokenを利用してRepository / Packageへ拡大

## 経営インパクト

| 観点 | 影響 |
| --- | --- |
| Developer Supply Chain | Direct DependencyでなくてもTransitive経由で侵害 |
| Cloud Risk | CI/CD SecretからCloud Control Planeへ到達し得る |
| Trust | Package署名・Provenanceだけでは侵害を完全に防げない |
| Incident Scope | 影響確認にはBuild Log、Lockfile、Token利用履歴が必要 |

## 日本企業への示唆

SBOMを作るだけでなく「いつ、どのVersionを、どのRunnerでBuildしたか」を追跡できる必要があります。Supply Chain Incident時にはPackage削除だけでなく、その期間に利用されたCredential Rotationが重要です。

<div class="sil-action-box" markdown>

## 推奨アクション

1. npm等のLifecycle Scriptを必要最小限にする
2. CI/CD Tokenを短命・Least Privilege化する
3. Package LockfileとBuild Provenanceを保持する
4. Dependency Updateを自動承認せずRisk-basedに検証する
5. Compromised Package利用時はCredential Rotationまで実施する
6. Maintainer / Package ReputationをThird-party Riskへ組み込む

</div>

## 用語解説

**Transitive Dependency**  
直接指定したLibraryがさらに依存している間接的なDependency。利用者が意識しないまま組み込まれることがあります。

## 関連記事

- [Mastra npm Supply Chain](mastra-npm-ai-supply-chain.md)
- [NIST SP 1326 C-SCRM Due Diligence](../risk-management/c-scrm-due-diligence-sp1326.md)

## 参考情報

- [Microsoft, Mini Shai Hulud: Compromised @antv npm packages enable CI/CD credential theft](https://www.microsoft.com/en-us/security/blog/2026/05/20/mini-shai-hulud-compromised-antv-npm-packages-enable-ci-cd-credential-theft/)

[^source]: [Microsoft, Mini Shai Hulud](https://www.microsoft.com/en-us/security/blog/2026/05/20/mini-shai-hulud-compromised-antv-npm-packages-enable-ci-cd-credential-theft/)

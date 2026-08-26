---
title: Identity Security
tags:
  - Identity Security
hide:
  - toc
---

# Identity Security

<div class="sil-category-intro"><p>MFA、Passkey、PAM、IGA、ITDR、Non-Human Identity（NHI）、AI Agent Identityなど、<strong>人・端末・ワークロード・AI AgentのIdentity</strong>を横断して扱います。</p></div>

## Articles

<!-- AUTO:CATEGORY_ARTICLES:START -->
<div class="sil-cards sil-cards-2">
  <article class="sil-card">
    <a class="sil-card-title" href="../cybersecurity/large-scale-credential-attacks.md">Large-Scale Credential Attacks ― 「ログインして侵入する」攻撃へのIdentity Security</a>
    <div class="sil-card-meta">August 2026 · Immediate · Mixed · Identity / Operational Security</div>
    <p>Unit 42の大規模資格情報攻撃レポートを基に、確認済み事実と攻撃者主張を分け、Identity Security対策を整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="ai-agent-identity-nhi.md">AI Agent Identity / NHI ― AI Agentを「操作主体」として統制する</a>
    <div class="sil-card-meta">August 2026 · Near-term · Assessment · Identity / AI Governance</div>
    <p>AI AgentとNon-Human Identityを、人・Agent・Credential・Actionの監査可能な連鎖として管理するための考え方を整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="pass-the-passkey.md">Passkeyは破られたのか ― Pass-ta-keyとPass-the-Passkeyから学ぶ</a>
    <div class="sil-card-meta">August 2026 · Near-term · Observed · Identity / Endpoint Security</div>
    <p>2026年に公開されたPass-ta-keyとPass-the-Passkeyを整理し、Passkeyの暗号方式ではなく実装・端末・回復フローが攻撃面になることを解説する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../cybersecurity/july-2026-trust-infrastructure-zero-days.md">2026年7月の実悪用Zero-day ― AD FS / SharePointから見る「Trust Infrastructure」の守り方</a>
    <div class="sil-card-meta">July 2026 · Immediate · Confirmed · Identity / Business Continuity</div>
    <p>MicrosoftとIPAが2026年7月に確認したAD FSおよびSharePointの実悪用脆弱性を、Patch Tuesdayの件数ではなくTrust Infrastructureの優先順位で整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="passkey-enrollment-recovery-attacks.md">Passkey時代の次の攻撃面 ― 登録・回復フローを狙うSocial Engineering</a>
    <div class="sil-card-meta">July 2026 · Immediate · Observed · Identity / Operational Security</div>
    <p>Okta Threat Intelligenceが2026年7月に報告したPasskey登録・セルフサービス回復フローへの攻撃を基に、フィッシング耐性MFA導入後のIdentity Securityを整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="entra-passkeys-default.md">Microsoft Entra IDがPasskeyを既定へ ― SMS / Voice MFA終了に向けた移行設計</a>
    <div class="sil-card-meta">July 2026 · Near-term · Confirmed · Identity / Change Management</div>
    <p>Microsoftが2026年7月に発表したEntra IDのPasskey既定化とMicrosoft提供SMS・音声認証終了のロードマップを企業Identity移行の観点から整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="pqc-piv-dual-stack.md">NIST PIVのPQC対応 ― Identity Credentialも「Crypto Agility」が必要になる</a>
    <div class="sil-card-meta">June 2026 · Strategic · Confirmed · Identity / Strategic Risk</div>
    <p>2026年6月にNISTが公開したPIV StandardsのPQC Working Draftを基に、ML-DSA / ML-KEM導入とClassical/PQC Dual-stack移行の意味を整理する。</p>
  </article>
</div>
<!-- AUTO:CATEGORY_ARTICLES:END -->

## Focus Areas

<div class="sil-cards sil-cards-2">
  <article class="sil-card"><div class="sil-card-title-static">Passkey / FIDO</div><p>フィッシング耐性、同期パスキー、端末侵害、回復フローを含む認証設計。</p></article>
  <article class="sil-card"><div class="sil-card-title-static">PAM / PIM / ITDR</div><p>特権アクセスとIdentity Threat Detection &amp; Responseを統合した防御。</p></article>
  <article class="sil-card"><div class="sil-card-title-static">NHI / AI Agent Identity</div><p>サービスアカウント、Workload Identity、AI Agentの委任・最小権限・監査。</p></article>
  <article class="sil-card"><div class="sil-card-title-static">Recovery / Helpdesk</div><p>強固な認証を迂回させないアカウント回復とヘルプデスク本人確認。</p></article>
</div>

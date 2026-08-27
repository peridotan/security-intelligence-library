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
  <article class="sil-card">
    <a class="sil-card-title" href="aitm-token-compromise-code-of-conduct.md">AiTM Token Compromise ― 「MFA済み」のSessionを盗まれるPhishing</a>
    <div class="sil-card-meta">May 2026 · Immediate · Observed · Identity / Financial Fraud</div>
    <p>Microsoftが2026年5月4日に公表したCode of Conductを装う多段Phishing Campaignを基に、AiTM、Token Theft、Phishing-resistant MFAの重要性を整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../cybersecurity/f5-confluence-edge-to-identity.md">Edge ApplianceからIdentity侵害へ ― F5 / Confluence攻撃Chainが示す境界防御の盲点</a>
    <div class="sil-card-meta">May 2026 · Immediate · Observed · Operational Security / Identity</div>
    <p>Microsoftが2026年5月22日に報告したF5 BIG-IPからConfluenceへPivotしたLinux intrusionを基に、Edge Device、Legacy、Credential、Identityを一続きで守る必要性…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../ai-security/openai-running-codex-safely.md">Coding Agentをどう守るか ― OpenAIのCodex運用から見るAgent Runtime Security</a>
    <div class="sil-card-meta">May 2026 · Near-term · Confirmed · AI Governance / Identity</div>
    <p>OpenAIが2026年5月8日に公開したRunning Codex safely at OpenAIを基に、Sandbox、承認、Network Access、Credential、Telemetryを統合したCoding Agent Se…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../ai-security/openai-trusted-access-cyber.md">Cyber能力へのAccess Control ― OpenAI Trusted Accessが示す「能力 × Identity」の統制</a>
    <div class="sil-card-meta">May 2026 · Strategic · Confirmed · AI Governance / Identity</div>
    <p>OpenAIが2026年5月7日に拡張したTrusted Access for Cyberを基に、高度なCyber CapabilityへのAccessをIdentity、Organization Verification、利用目的、監視で制…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="ai-enabled-device-code-phishing.md">AI-enabled Device Code Phishing ― Passwordを盗まずTokenを取る攻撃がScaleする</a>
    <div class="sil-card-meta">April 2026 · Immediate · Observed · Identity / Financial Fraud</div>
    <p>Microsoftが2026年4月6日に報告したDevice Code Phishing Campaignを基に、Dynamic Code Generation、OAuth Token、MFA、Device Registrationを含む攻撃…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="openai-advanced-account-security.md">Advanced Account Security ― 高Risk AI Accountでは「認証」と「回復」を同じ強度で守る</a>
    <div class="sil-card-meta">April 2026 · Near-term · Confirmed · Identity / AI Governance</div>
    <p>OpenAIが2026年4月30日に公表したAdvanced Account Securityを基に、Passkey、Passwordless、Recovery、Session、High-risk Capabilityを統合したIdentit…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="eudi-wallet-certification.md">EUDI Wallet Certification ― Digital Identityを「実装」から「認証・保証」へ</a>
    <div class="sil-card-meta">April 2026 · Strategic · Confirmed · Identity / Regulatory</div>
    <p>ENISAが2026年4月3日に公開Consultationを開始したEU Digital Identity Wallet向けCybersecurity Certification Schemeを基に、Digital IdentityのSec…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="nist-key-generation-pqc-sp800-133r3.md">NIST SP 800-133r3 Draft ― PQC移行はAlgorithmだけでなくKey Generation / HSMまで変える</a>
    <div class="sil-card-meta">April 2026 · Strategic · Confirmed · Cryptography / Identity</div>
    <p>NISTが2026年4月17日に公開したSP 800-133 Revision 3 Draftを基に、PQC、KEM、Seed Expansion、Hybrid ImplementationがKey Management基盤へ与える影響を整理…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../cybersecurity/m-trends-2026-speed-identity-recovery.md">M-Trends 2026 ― 攻撃の「22秒化」とRecovery Denialが示す次の防御モデル</a>
    <div class="sil-card-meta">March 2026 · Immediate · Observed · Threat Landscape / Identity</div>
    <p>Mandiantが2026年3月23日に公表したM-Trends 2026を基に、Access Hand-offの高速化、Voice Phishing、SaaS Identity、Recovery Denial、Edge Persistenc…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="teams-vishing-quick-assist.md">Teams Vishing ― 「IT Supportを信じる」ことがInitial Accessになる</a>
    <div class="sil-card-meta">March 2026 · Immediate · Observed · Identity / Social Engineering</div>
    <p>Microsoft Incident Responseが2026年3月16日に公表したTeams Voice Phishing事例を基に、Quick Assist、正規Tool Abuse、Credential Theft、Session H…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="tycoon2fa-aitm-phaas.md">Tycoon2FA ― MFA突破がPhishing-as-a-Serviceとして「産業化」した</a>
    <div class="sil-card-meta">March 2026 · Immediate · Observed · Identity / Financial Fraud</div>
    <p>Microsoftが2026年3月4日に公表したTycoon2FA分析を基に、AiTM、Session Cookie Theft、短命Infrastructure、PhaaSによるMFA突破のScale化を整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="nist-mdl-financial-institutions.md">NIST SP 1800-42 Draft ― Digital Identityを金融の実取引へ持ち込むReference Architecture</a>
    <div class="sil-card-meta">March 2026 · Strategic · Confirmed · Identity / Fraud</div>
    <p>NIST NCCoEが2026年3月18日に公開した金融機関向けmDL実装Draftを基に、Verifiable Digital Credential、Threat Model、Privacy、Interoperabilityの意味を整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../cybersecurity/unit42-global-ir-2026.md">Unit 42 Global IR 2026 ― 72分・Identity 90%・SaaS 23%が示す「境界防御の限界」</a>
    <div class="sil-card-meta">February 2026 · Immediate · Observed · Threat Landscape / Identity</div>
    <p>Palo Alto Networks Unit 42が2026年2月17日に公開したGlobal Incident Response Reportを基に、72分の攻撃速度、Identity、SaaS Supply Chain、Multi-su…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="nist-agent-identity-standards-february.md">NISTがAI Agentを「Identity＋Standards」の問題として定義し始めた</a>
    <div class="sil-card-meta">February 2026 · Strategic · Confirmed · Identity / AI Governance</div>
    <p>NISTが2026年2月に公開したAI Agent Identity and Authorization Concept PaperとAI Agent Standards Initiativeを基に、識別・認可・監査・Non-repudiat…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../ai-security/openai-trusted-access-cyber-february.md">Trusted Access for Cyber ― 高いCyber Capabilityを「IdentityとTrust」で段階開放する</a>
    <div class="sil-card-meta">February 2026 · Strategic · Confirmed · AI Governance / Identity</div>
    <p>OpenAIが2026年2月5日に発表したTrusted Access for Cyberを基に、Frontier Cyber CapabilityのAccess Control、Identity Verification、Enterpris…</p>
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

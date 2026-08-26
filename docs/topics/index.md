---
title: Topics
hide:
  - toc
---

# Topics

`Topics`は、カテゴリをまたいで同じ経営・Security論点を読むための**統制された横断分類**です。製品名、技術名、個別攻撃名などの細かなキーワードは [Tags](../tags/index.md) に分離しています。

<!-- AUTO:TOPICS:START -->
## Topic Directory

<div class="sil-topic-groups">
<section class="sil-topic-group">
<div class="sil-topic-group-title">AI Security</div>
<div class="sil-topic-directory">
<a class="sil-topic" href="#ai-agent-security">AI Agent Security <span class="sil-topic-count">5</span></a>
<a class="sil-topic" href="#mcp-security">MCP Security <span class="sil-topic-count">2</span></a>
<a class="sil-topic" href="#ai-governance">AI Governance <span class="sil-topic-count">5</span></a>
<a class="sil-topic" href="#ai-cyber-capability">AI Cyber Capability <span class="sil-topic-count">4</span></a>
<a class="sil-topic" href="#ai-enabled-threats">AI-enabled Threats <span class="sil-topic-count">3</span></a>
<a class="sil-topic" href="#ai-infrastructure">AI Infrastructure <span class="sil-topic-count">1</span></a>
<a class="sil-topic" href="#ai-for-security">AI for Security <span class="sil-topic-count">1</span></a>
</div>
</section>
<section class="sil-topic-group">
<div class="sil-topic-group-title">Identity</div>
<div class="sil-topic-directory">
<a class="sil-topic" href="#identity-security">Identity Security <span class="sil-topic-count">7</span></a>
<a class="sil-topic" href="#passkey-phishing-resistant-mfa">Passkey &amp; Phishing-resistant MFA <span class="sil-topic-count">3</span></a>
<a class="sil-topic" href="#credential-attacks">Credential Attacks <span class="sil-topic-count">2</span></a>
<a class="sil-topic" href="#pqc-crypto-agility">PQC / Crypto Agility <span class="sil-topic-count">1</span></a>
</div>
</section>
<section class="sil-topic-group">
<div class="sil-topic-group-title">Cyber Operations</div>
<div class="sil-topic-directory">
<a class="sil-topic" href="#vulnerability-management">Vulnerability Management <span class="sil-topic-count">3</span></a>
<a class="sil-topic" href="#ransomware-resilience">Ransomware &amp; Resilience <span class="sil-topic-count">3</span></a>
<a class="sil-topic" href="#ot-critical-infrastructure">OT / Critical Infrastructure <span class="sil-topic-count">4</span></a>
<a class="sil-topic" href="#software-supply-chain">Software Supply Chain <span class="sil-topic-count">2</span></a>
</div>
</section>
<section class="sil-topic-group">
<div class="sil-topic-group-title">Governance &amp; Risk</div>
<div class="sil-topic-directory">
<a class="sil-topic" href="#third-party-risk-c-scrm">Third-party Risk / C-SCRM <span class="sil-topic-count">4</span></a>
<a class="sil-topic" href="#regulation-policy">Regulation &amp; Policy <span class="sil-topic-count">4</span></a>
<a class="sil-topic" href="#security-governance-risk">Security Governance &amp; Risk Management <span class="sil-topic-count">8</span></a>
</div>
</section>
</div>

## AI Security

### AI Agent Security {#ai-agent-security}

AI Agentの自律性、Tool利用、Sandbox、Identity、停止・監視を横断する。

- [AI Agent Identity / NHI ― AI Agentを「操作主体」として統制する](../identity-security/ai-agent-identity-nhi.md) — August 2026 · Near-term · Assessment
- [Agentic AIの安全設計 ― Sandbox・Identity・監視・Kill Switch](../ai-security/agentic-ai-security-controls.md) — August 2026 · Near-term · Assessment
- [JADEPUFFER ― Agentic Ransomwareが「実験」から攻撃オペレーションへ](../cybersecurity/jadepuffer-agentic-ransomware.md) — July 2026 · Immediate · Observed
- [AutoJack ― 「localhostは安全」という前提をAI Agentが崩す](../ai-security/autojack-agent-localhost-rce.md) — June 2026 · Immediate · Observed
- [MCP Tool Poisoning ― AI AgentのSupply Chainは「コード」だけではない](../ai-security/mcp-tool-poisoning-agent-supply-chain.md) — June 2026 · Immediate · Assessment

### MCP Security {#mcp-security}

MCP Server / Tool / Metadata / Local Control Planeに関するSecurity。

- [AutoJack ― 「localhostは安全」という前提をAI Agentが崩す](../ai-security/autojack-agent-localhost-rce.md) — June 2026 · Immediate · Observed
- [MCP Tool Poisoning ― AI AgentのSupply Chainは「コード」だけではない](../ai-security/mcp-tool-poisoning-agent-supply-chain.md) — June 2026 · Immediate · Assessment

### AI Governance {#ai-governance}

生成AI・AI Systemの利用統制、継続評価、責任・Risk管理。

- [EU AI Actが執行フェーズへ ― 2026年8月2日から何が変わったか](../regulation/eu-ai-act-enforcement-2026.md) — August 2026 · Immediate · Confirmed
- [生成AI利活用ガバナンス ― 禁止事項だけでなく「安全に使える仕組み」を作る](../ai-security/generative-ai-governance.md) — August 2026 · Near-term · Confirmed
- [OpenAI / Hugging Face評価インシデント ― AI Cyber評価環境をどう隔離するか](../ai-security/openai-huggingface-evaluation-incident.md) — July 2026 · Immediate · Confirmed
- [EU Cybersecurity & AI Action Plan ― AIの攻撃利用と防御利用を同じ政策で扱う](../regulation/eu-cybersecurity-ai-action-plan.md) — July 2026 · Strategic · Confirmed
- [NISTが示す「AI Securityは一度設定して終わりではない」理由](../ai-security/continuous-ai-security-nist-proof.md) — June 2026 · Strategic · Confirmed

### AI Cyber Capability {#ai-cyber-capability}

Frontier / Open-weight Modelの攻撃・脆弱性探索能力とCapability Evaluation。

- [Frontier AIのサイバー能力が「Critical」に近づく意味](../ai-security/frontier-ai-cyber-capabilities.md) — August 2026 · Strategic · Confirmed
- [OpenAI / Hugging Face評価インシデント ― AI Cyber評価環境をどう隔離するか](../ai-security/openai-huggingface-evaluation-incident.md) — July 2026 · Immediate · Confirmed
- [EU Cybersecurity & AI Action Plan ― AIの攻撃利用と防御利用を同じ政策で扱う](../regulation/eu-cybersecurity-ai-action-plan.md) — July 2026 · Strategic · Confirmed
- [Kimi K3のCyber能力評価 ― Open-weight AIを「モデル名」ではなく能力で評価する](../ai-security/kimi-k3-cyber-capabilities.md) — July 2026 · Strategic · Observed

### AI-enabled Threats {#ai-enabled-threats}

攻撃・Malware・Ransomware・OT標的活動にAIが組み込まれる脅威。

- [AI生成スクリプトがPLC標的活動に登場 ― OT/ICSセキュリティの転換点](../cybersecurity/ai-generated-plc-attacks.md) — August 2026 · Immediate · Observed
- [AI Enabled Malwareの現実 ― 「405検体・97%」をどう読むか](../ai-security/ai-enabled-malware-reality.md) — August 2026 · Near-term · Observed
- [JADEPUFFER ― Agentic Ransomwareが「実験」から攻撃オペレーションへ](../cybersecurity/jadepuffer-agentic-ransomware.md) — July 2026 · Immediate · Observed

### AI Infrastructure {#ai-infrastructure}

GPU、AI Data Center、Model / Dataset / RuntimeなどAI基盤の保護。

- [NIST SP 800-239 Draft ― AI Data Centerを新しいCritical Infrastructureとして守る](../ai-security/ai-data-center-security-sp800-239.md) — July 2026 · Strategic · Confirmed

### AI for Security {#ai-for-security}

脆弱性発見・検知・対応など、防御側でAIを活用するテーマ。

- [MDASH ― AIによる脆弱性発見をBenchmarkからProduction Defenseへ](../cybersecurity/mdash-ai-vulnerability-discovery.md) — June 2026 · Near-term · Observed

## Identity

### Identity Security {#identity-security}

人・Workload・NHI・AI Agentを含むIdentityの認証・認可・監視。

- [Large-Scale Credential Attacks ― 「ログインして侵入する」攻撃へのIdentity Security](../cybersecurity/large-scale-credential-attacks.md) — August 2026 · Immediate · Mixed
- [AI Agent Identity / NHI ― AI Agentを「操作主体」として統制する](../identity-security/ai-agent-identity-nhi.md) — August 2026 · Near-term · Assessment
- [Agentic AIの安全設計 ― Sandbox・Identity・監視・Kill Switch](../ai-security/agentic-ai-security-controls.md) — August 2026 · Near-term · Assessment
- [Passkeyは破られたのか ― Pass-ta-keyとPass-the-Passkeyから学ぶ](../identity-security/pass-the-passkey.md) — August 2026 · Near-term · Observed
- [2026年7月の実悪用Zero-day ― AD FS / SharePointから見る「Trust Infrastructure」の守り方](../cybersecurity/july-2026-trust-infrastructure-zero-days.md) — July 2026 · Immediate · Confirmed
- [Microsoft Entra IDがPasskeyを既定へ ― SMS / Voice MFA終了に向けた移行設計](../identity-security/entra-passkeys-default.md) — July 2026 · Near-term · Confirmed
- [NIST PIVのPQC対応 ― Identity Credentialも「Crypto Agility」が必要になる](../identity-security/pqc-piv-dual-stack.md) — June 2026 · Strategic · Confirmed

### Passkey & Phishing-resistant MFA {#passkey-phishing-resistant-mfa}

Passkey / FIDO2と、登録・回復を含むフィッシング耐性認証。

- [Passkeyは破られたのか ― Pass-ta-keyとPass-the-Passkeyから学ぶ](../identity-security/pass-the-passkey.md) — August 2026 · Near-term · Observed
- [Passkey時代の次の攻撃面 ― 登録・回復フローを狙うSocial Engineering](../identity-security/passkey-enrollment-recovery-attacks.md) — July 2026 · Immediate · Observed
- [Microsoft Entra IDがPasskeyを既定へ ― SMS / Voice MFA終了に向けた移行設計](../identity-security/entra-passkeys-default.md) — July 2026 · Near-term · Confirmed

### Credential Attacks {#credential-attacks}

Password Spraying、MFA Fatigue、漏えい資格情報、Recovery悪用。

- [Large-Scale Credential Attacks ― 「ログインして侵入する」攻撃へのIdentity Security](../cybersecurity/large-scale-credential-attacks.md) — August 2026 · Immediate · Mixed
- [Passkey時代の次の攻撃面 ― 登録・回復フローを狙うSocial Engineering](../identity-security/passkey-enrollment-recovery-attacks.md) — July 2026 · Immediate · Observed

### PQC / Crypto Agility {#pqc-crypto-agility}

Post-Quantum CryptographyとIdentity / Credentialの移行設計。

- [NIST PIVのPQC対応 ― Identity Credentialも「Crypto Agility」が必要になる](../identity-security/pqc-piv-dual-stack.md) — June 2026 · Strategic · Confirmed

## Cyber Operations

### Vulnerability Management {#vulnerability-management}

実悪用、KEV / EPSS、Patch優先度、Exploit Windowを含む脆弱性管理。

- [脆弱性悪用の猶予は48時間以下へ ― 「残存時間」でパッチ管理を考える](../cybersecurity/exploitation-window-48-hours.md) — August 2026 · Immediate · Observed
- [2026年7月の実悪用Zero-day ― AD FS / SharePointから見る「Trust Infrastructure」の守り方](../cybersecurity/july-2026-trust-infrastructure-zero-days.md) — July 2026 · Immediate · Confirmed
- [MDASH ― AIによる脆弱性発見をBenchmarkからProduction Defenseへ](../cybersecurity/mdash-ai-vulnerability-discovery.md) — June 2026 · Near-term · Observed

### Ransomware & Resilience {#ransomware-resilience}

Ransomware対策、Backup / Restore、Business Resilience。

- [JADEPUFFER ― Agentic Ransomwareが「実験」から攻撃オペレーションへ](../cybersecurity/jadepuffer-agentic-ransomware.md) — July 2026 · Immediate · Observed
- [NIST IR 8374r1 ― Ransomware対策を「製品導入」からCSF 2.0の経営Riskへ](../risk-management/nist-ransomware-csf2-profile.md) — June 2026 · Near-term · Confirmed
- [NIST SP 1339 ― OT Backupは「取得」ではなくChange ManagementとRecovery Exerciseで守る](../cybersecurity/nist-ot-backup-sp1339.md) — June 2026 · Near-term · Confirmed

### OT / Critical Infrastructure {#ot-critical-infrastructure}

OT / ICS、重要インフラ、Remote Access、Recovery、Safety。

- [AI生成スクリプトがPLC標的活動に登場 ― OT/ICSセキュリティの転換点](../cybersecurity/ai-generated-plc-attacks.md) — August 2026 · Immediate · Observed
- [重要インフラのサイバーセキュリティが「統一基準」へ ― 日本企業が確認すべきこと](../regulation/japan-critical-infrastructure-unified-standard.md) — August 2026 · Near-term · Confirmed
- [NIST SP 1339 ― OT Backupは「取得」ではなくChange ManagementとRecovery Exerciseで守る](../cybersecurity/nist-ot-backup-sp1339.md) — June 2026 · Near-term · Confirmed
- [NIST SP 1800-45 ― OT Remote Accessを「例外VPN」からReference Architectureへ](../cybersecurity/water-ot-secure-remote-access-sp1800-45.md) — June 2026 · Near-term · Confirmed

### Software Supply Chain {#software-supply-chain}

npm、Framework、Package、Tool等の開発・Software Supply Chain Risk。

- [MCP Tool Poisoning ― AI AgentのSupply Chainは「コード」だけではない](../ai-security/mcp-tool-poisoning-agent-supply-chain.md) — June 2026 · Immediate · Assessment
- [Mastra npm Supply Chain Compromise ― AI Frameworkも「開発者のTrust」を狙われる](../cybersecurity/mastra-npm-ai-supply-chain.md) — June 2026 · Immediate · Observed

## Governance & Risk

### Third-party Risk / C-SCRM {#third-party-risk-c-scrm}

Supplier、委託先、Cloud / Software依存を含むCyber Supply Chain Risk。

- [NIST SP 1326 ― Supply Chain Securityを「契約後の監査」から「契約前のDue Diligence」へ](../risk-management/c-scrm-due-diligence-sp1326.md) — July 2026 · Near-term · Confirmed
- [NIST SP 800-239 Draft ― AI Data Centerを新しいCritical Infrastructureとして守る](../ai-security/ai-data-center-security-sp800-239.md) — July 2026 · Strategic · Confirmed
- [Mastra npm Supply Chain Compromise ― AI Frameworkも「開発者のTrust」を狙われる](../cybersecurity/mastra-npm-ai-supply-chain.md) — June 2026 · Immediate · Observed
- [NIST SP 800-18r2 ― Security・Privacy・C-SCRMを別々の計画書にしない](../risk-management/nist-sp800-18r2-integrated-system-plans.md) — June 2026 · Strategic · Confirmed

### Regulation & Policy {#regulation-policy}

AI・Cybersecurity・重要インフラに関する法規制・政策・公的Guidance。

- [EU AI Actが執行フェーズへ ― 2026年8月2日から何が変わったか](../regulation/eu-ai-act-enforcement-2026.md) — August 2026 · Immediate · Confirmed
- [生成AI利活用ガバナンス ― 禁止事項だけでなく「安全に使える仕組み」を作る](../ai-security/generative-ai-governance.md) — August 2026 · Near-term · Confirmed
- [重要インフラのサイバーセキュリティが「統一基準」へ ― 日本企業が確認すべきこと](../regulation/japan-critical-infrastructure-unified-standard.md) — August 2026 · Near-term · Confirmed
- [EU Cybersecurity & AI Action Plan ― AIの攻撃利用と防御利用を同じ政策で扱う](../regulation/eu-cybersecurity-ai-action-plan.md) — July 2026 · Strategic · Confirmed

### Security Governance & Risk Management {#security-governance-risk}

技術対策を経営Risk、計画、優先順位、残余Riskへ接続する。

- [脆弱性悪用の猶予は48時間以下へ ― 「残存時間」でパッチ管理を考える](../cybersecurity/exploitation-window-48-hours.md) — August 2026 · Immediate · Observed
- [生成AI利活用ガバナンス ― 禁止事項だけでなく「安全に使える仕組み」を作る](../ai-security/generative-ai-governance.md) — August 2026 · Near-term · Confirmed
- [Frontier AIのサイバー能力が「Critical」に近づく意味](../ai-security/frontier-ai-cyber-capabilities.md) — August 2026 · Strategic · Confirmed
- [NIST SP 1326 ― Supply Chain Securityを「契約後の監査」から「契約前のDue Diligence」へ](../risk-management/c-scrm-due-diligence-sp1326.md) — July 2026 · Near-term · Confirmed
- [NIST IR 8374r1 ― Ransomware対策を「製品導入」からCSF 2.0の経営Riskへ](../risk-management/nist-ransomware-csf2-profile.md) — June 2026 · Near-term · Confirmed
- [NIST SP 1800-45 ― OT Remote Accessを「例外VPN」からReference Architectureへ](../cybersecurity/water-ot-secure-remote-access-sp1800-45.md) — June 2026 · Near-term · Confirmed
- [NIST SP 800-18r2 ― Security・Privacy・C-SCRMを別々の計画書にしない](../risk-management/nist-sp800-18r2-integrated-system-plans.md) — June 2026 · Strategic · Confirmed
- [NISTが示す「AI Securityは一度設定して終わりではない」理由](../ai-security/continuous-ai-security-nist-proof.md) — June 2026 · Strategic · Confirmed
<!-- AUTO:TOPICS:END -->

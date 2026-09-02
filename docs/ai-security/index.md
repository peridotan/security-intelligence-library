---
title: AI Security
tags:
  - AI Security
hide:
  - toc
---

# AI Security

<div class="sil-category-intro"><p>Security for AI、AI for Security、AI Agent、生成AIガバナンスなど、AIとセキュリティの交差領域を扱います。<strong>AIそのものを守る視点と、AIによって防御・攻撃が変わる視点を分けて整理</strong>します。</p></div>

## Articles

<!-- AUTO:CATEGORY_ARTICLES:START -->
<div class="sil-cards sil-cards-2">
  <article class="sil-card">
    <a class="sil-card-title" href="ai-infrastructure-control-plane-attacks.md">AI Infrastructureが攻撃対象へ ― LiteLLM・RAGFlow・Kestraが示すControl Plane Risk</a>
    <div class="sil-card-meta">August 2026 · Immediate · Observed · AI Infrastructure / Credential Risk</div>
    <p>Microsoftが2026年8月26日に報告したLiteLLM、RAGFlow、Kestraへの侵害を基に、AI Gateway・RAG・OrchestratorがCredential・Data・Executionを集中させるControl…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="agentic-ai-security-controls.md">Agentic AIの安全設計 ― Sandbox・Identity・監視・Kill Switch</a>
    <div class="sil-card-meta">August 2026 · Near-term · Assessment · AI Governance / Operational Security</div>
    <p>NCSCと第三者サイバー評価事例を基に、AI Agentの自律性を安全に運用するための技術・運用統制を整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../identity-security/ai-agent-identity-nhi.md">AI Agent Identity / NHI ― AI Agentを「操作主体」として統制する</a>
    <div class="sil-card-meta">August 2026 · Near-term · Assessment · Identity / AI Governance</div>
    <p>AI AgentとNon-Human Identityを、人・Agent・Credential・Actionの監査可能な連鎖として管理するための考え方を整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="ai-enabled-malware-reality.md">AI Enabled Malwareの現実 ― 「405検体・97%」をどう読むか</a>
    <div class="sil-card-meta">August 2026 · Near-term · Observed · Operational Security / Endpoint Security</div>
    <p>Unit 42の405検体分析を基に、AI-enabled malwareの実環境での観測と誇張されやすい点を整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="generative-ai-governance.md">生成AI利活用ガバナンス ― 禁止事項だけでなく「安全に使える仕組み」を作る</a>
    <div class="sil-card-meta">August 2026 · Near-term · Confirmed · AI Governance / Regulatory</div>
    <p>生成AI利活用ガバナンスを、利用類型・リスク・統制・教育・モニタリングの観点から企業向けに整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="frontier-ai-cyber-capabilities.md">Frontier AIのサイバー能力が「Critical」に近づく意味</a>
    <div class="sil-card-meta">August 2026 · Strategic · Confirmed · Strategic Risk / Operational Security</div>
    <p>Frontier AIのサイバー能力がCritical閾値に近づく状況を、攻撃速度・防御時間・経営リスクの観点から整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../cybersecurity/jadepuffer-agentic-ransomware.md">JADEPUFFER ― Agentic Ransomwareが「実験」から攻撃オペレーションへ</a>
    <div class="sil-card-meta">July 2026 · Immediate · Observed · Business Continuity / AI Security</div>
    <p>Sysdigが2026年7月に報告したJADEPUFFERを基に、AI Agentが偵察・資格情報探索・横展開・恐喝を適応的に連鎖させるリスクを整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="openai-huggingface-evaluation-incident.md">OpenAI / Hugging Face評価インシデント ― AI Cyber評価環境をどう隔離するか</a>
    <div class="sil-card-meta">July 2026 · Immediate · Confirmed · AI Governance / Infrastructure</div>
    <p>2026年7月のOpenAIとHugging Faceのモデル評価中セキュリティインシデントを、評価環境・Sandbox・Network Isolation・第三者連携の観点から整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../regulation/eu-cybersecurity-ai-action-plan.md">EU Cybersecurity &amp; AI Action Plan ― AIの攻撃利用と防御利用を同じ政策で扱う</a>
    <div class="sil-card-meta">July 2026 · Strategic · Confirmed · Regulatory / AI Governance</div>
    <p>欧州委員会が2026年7月に公表したCybersecurity and Artificial Intelligence Action Planを、AI Model評価、防御能力、Critical OSS、規制連携の観点から整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="kimi-k3-cyber-capabilities.md">Kimi K3のCyber能力評価 ― Open-weight AIを「モデル名」ではなく能力で評価する</a>
    <div class="sil-card-meta">July 2026 · Strategic · Observed · AI Governance / Model Risk</div>
    <p>UK AISIと米国CAISI/NISTが2026年7月に公表したKimi K3 Cyber Capability評価を基に、企業がAIモデルの攻撃能力をどう評価すべきか整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="ai-data-center-security-sp800-239.md">NIST SP 800-239 Draft ― AI Data Centerを新しいCritical Infrastructureとして守る</a>
    <div class="sil-card-meta">July 2026 · Strategic · Confirmed · Infrastructure / Supply Chain</div>
    <p>NISTが2026年7月に公開したAI Data Center Security Analysis Draft SP 800-239を基に、AI基盤固有のセキュリティ論点を整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="autojack-agent-localhost-rce.md">AutoJack ― 「localhostは安全」という前提をAI Agentが崩す</a>
    <div class="sil-card-meta">June 2026 · Immediate · Observed · AI Governance / Endpoint Security</div>
    <p>2026年6月にMicrosoftが公表したAutoJackを基に、Browsing AgentとLocal MCP Control Planeの組み合わせがRemote Code Executionへつながるリスクを整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="mcp-tool-poisoning-agent-supply-chain.md">MCP Tool Poisoning ― AI AgentのSupply Chainは「コード」だけではない</a>
    <div class="sil-card-meta">June 2026 · Immediate · Assessment · AI Governance / Supply Chain</div>
    <p>2026年6月のMicrosoft Incident Responseの分析を基に、MCP Tool Descriptionの改変がAI Agentの行動を変えるSupply Chain Riskを整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../cybersecurity/mastra-npm-ai-supply-chain.md">Mastra npm Supply Chain Compromise ― AI Frameworkも「開発者のTrust」を狙われる</a>
    <div class="sil-card-meta">June 2026 · Immediate · Observed · Supply Chain / Credential Risk</div>
    <p>2026年6月にMicrosoftが報告したMastra npm Supply Chain Compromiseを基に、AI開発FrameworkとDeveloper CredentialのSupply Chain Riskを整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../cybersecurity/mdash-ai-vulnerability-discovery.md">MDASH ― AIによる脆弱性発見をBenchmarkからProduction Defenseへ</a>
    <div class="sil-card-meta">June 2026 · Near-term · Observed · Operational Security / Software Security</div>
    <p>2026年6月にMicrosoftが公表したAgentic Vulnerability Detection System MDASHの実運用を基に、AI for Securityが脆弱性管理をどう変えるか整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="continuous-ai-security-nist-proof.md">NISTが示す「AI Securityは一度設定して終わりではない」理由</a>
    <div class="sil-card-meta">June 2026 · Strategic · Confirmed · AI Governance / Strategic Risk</div>
    <p>2026年6月にNISTが公表したRobust AI Securityの数学的議論を基に、固定GuardrailからContinuous Red Team / Update / Resilienceへ移行する意味を整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="openai-running-codex-safely.md">Coding Agentをどう守るか ― OpenAIのCodex運用から見るAgent Runtime Security</a>
    <div class="sil-card-meta">May 2026 · Near-term · Confirmed · AI Governance / Identity</div>
    <p>OpenAIが2026年5月8日に公開したRunning Codex safely at OpenAIを基に、Sandbox、承認、Network Access、Credential、Telemetryを統合したCoding Agent Se…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="nist-ai-agent-security-rfi-analysis.md">NIST AI Agent Security分析 ― 従来のCybersecurity原則だけでは足りない理由</a>
    <div class="sil-card-meta">May 2026 · Near-term · Confirmed · AI Governance / Operational Security</div>
    <p>NIST/CAISIが2026年5月18日に公表したAI Agent Security RFI回答分析を基に、Agent固有の脅威と政府・企業に必要な対応を整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../regulation/singapore-agentic-ai-governance-v15.md">Singapore Agentic AI Governance v1.5 ― 「自律性をRisk Tierで制限する」実装例</a>
    <div class="sil-card-meta">May 2026 · Near-term · Confirmed · AI Governance / Regulatory</div>
    <p>Singapore IMDAが2026年5月20日に更新したModel AI Governance Framework for Agentic AIを基に、Risk Bounding、人の責任、Multi-agent、Third-party…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="openai-trusted-access-cyber.md">Cyber能力へのAccess Control ― OpenAI Trusted Accessが示す「能力 × Identity」の統制</a>
    <div class="sil-card-meta">May 2026 · Strategic · Confirmed · AI Governance / Identity</div>
    <p>OpenAIが2026年5月7日に拡張したTrusted Access for Cyberを基に、高度なCyber CapabilityへのAccessをIdentity、Organization Verification、利用目的、監視で制…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="claude-mythos-preview-cyber-capability.md">Claude Mythos Preview ― AIのExploit Development能力が一段上がった4月</a>
    <div class="sil-card-meta">April 2026 · Immediate · Observed · AI Governance / Vulnerability Risk</div>
    <p>Anthropicが2026年4月7日に公表したClaude Mythos PreviewのCybersecurity評価を基に、Zero-day発見、Exploit Development、Project Glasswingと企業防御への意…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../cybersecurity/ai-embedded-threat-operations.md">AIは「自律攻撃」以前に攻撃工程へ埋め込まれている ― Microsoftの4月観測</a>
    <div class="sil-card-meta">April 2026 · Near-term · Observed · Threat Landscape / Identity</div>
    <p>Microsoftが2026年4月2日に公表したThreat Landscape分析を基に、AIがReconnaissance、Phishing、Malware、Post-compromiseへ組み込まれる一方、完全自律攻撃はまだ典型ではない…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../identity-security/openai-advanced-account-security.md">Advanced Account Security ― 高Risk AI Accountでは「認証」と「回復」を同じ強度で守る</a>
    <div class="sil-card-meta">April 2026 · Near-term · Confirmed · Identity / AI Governance</div>
    <p>OpenAIが2026年4月30日に公表したAdvanced Account Securityを基に、Passkey、Passwordless、Recovery、Session、High-risk Capabilityを統合したIdentit…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../cybersecurity/ai-as-tradecraft-march-2026.md">AI as Tradecraft ― 攻撃者は「自律攻撃」より先にAIを日常の攻撃運用へ組み込んだ</a>
    <div class="sil-card-meta">March 2026 · Near-term · Observed · Threat Landscape / Security Operations</div>
    <p>Microsoftが2026年3月6日に公表したThreat Intelligenceを基に、Threat ActorがAIをReconnaissance、Social Engineering、Malware、Post-compromiseへ…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../regulation/japan-ai-guidelines-business-v12.md">AI事業者ガイドライン第1.2版 ― AI Governanceを「原則」から実践Toolへ更新</a>
    <div class="sil-card-meta">March 2026 · Near-term · Confirmed · AI Governance / Regulatory</div>
    <p>総務省・経済産業省が2026年3月31日にとりまとめたAI事業者ガイドライン第1.2版と活用の手引き等を基に、日本企業のAI Governance運用への意味を整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="nist-deployed-ai-monitoring.md">NIST AI 800-4 ― AI Governanceは「導入前審査」よりPost-deployment Monitoringが難しい</a>
    <div class="sil-card-meta">March 2026 · Strategic · Confirmed · AI Governance / Compliance</div>
    <p>NISTが2026年3月9日に公表したDeployed AI SystemsのMonitoring課題を基に、Functionality、Operations、Human Factors、Security、Compliance、Large-s…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="anthropic-llm-discovered-zero-days.md">LLM-discovered Zero-days ― AIのVulnerability Discoveryが「人間の処理能力」を超え始める</a>
    <div class="sil-card-meta">February 2026 · Immediate · Observed · AI Governance / Vulnerability Risk</div>
    <p>Anthropicが2026年2月5日に公表したClaude Opus 4.6のZero-day探索結果を基に、500件超のHigh-severity Finding、Disclosure / Patch Capacity、Human Val…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../cybersecurity/gtig-ai-threat-tracker-february.md">GTIG AI Threat Tracker ― AIは攻撃Toolであると同時に「盗まれるAsset」になった</a>
    <div class="sil-card-meta">February 2026 · Near-term · Observed · AI Security / Intellectual Property</div>
    <p>Google Threat Intelligence Groupの2026年2月AI Threat Trackerを基に、Model Extraction / Distillation、Threat ActorのAI利用、AI-enabled…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../risk-management/nist-data-classification-sp1800-39.md">NIST SP 1800-39 Draft ― Zero Trust・PQC・Secure AIの前に「Dataを見つけて分類する」</a>
    <div class="sil-card-meta">February 2026 · Near-term · Confirmed · Data Security / AI Governance</div>
    <p>NISTが2026年2月12日に公開したSP 1800-39 Draftを基に、Unstructured DataのDiscovery / ClassificationがZero Trust、Quantum-safe Cryptography…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="nist-ai800-3-evaluation-uncertainty.md">NIST AI 800-3 ― AI Benchmarkの「1つのScore」を経営判断に使いすぎない</a>
    <div class="sil-card-meta">February 2026 · Strategic · Confirmed · AI Governance / Measurement</div>
    <p>NISTが2026年2月19日に公表したAI 800-3を基に、Benchmark Accuracy、Generalized Accuracy、不確実性、AI Capability評価の読み方を整理する。</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../identity-security/nist-agent-identity-standards-february.md">NISTがAI Agentを「Identity＋Standards」の問題として定義し始めた</a>
    <div class="sil-card-meta">February 2026 · Strategic · Confirmed · Identity / AI Governance</div>
    <p>NISTが2026年2月に公開したAI Agent Identity and Authorization Concept PaperとAI Agent Standards Initiativeを基に、識別・認可・監査・Non-repudiat…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="openai-trusted-access-cyber-february.md">Trusted Access for Cyber ― 高いCyber Capabilityを「IdentityとTrust」で段階開放する</a>
    <div class="sil-card-meta">February 2026 · Strategic · Confirmed · AI Governance / Identity</div>
    <p>OpenAIが2026年2月5日に発表したTrusted Access for Cyberを基に、Frontier Cyber CapabilityのAccess Control、Identity Verification、Enterpris…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="langgrinch-ai-application-supply-chain.md">LangGrinch ― AI Application Supply ChainはPromptだけでなくFrameworkも攻撃面になる</a>
    <div class="sil-card-meta">January 2026 · Immediate · Confirmed · Software Security / AI Security</div>
    <p>Microsoftが2026年1月30日に公開したLangChain Core CVE-2025-68664のCase Studyを基に、AI Framework、Serialization Injection、Secret Exposure…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="openai-agent-link-data-exfiltration.md">AI Agent Link Safety ― URLそのものがData Exfiltration Channelになる</a>
    <div class="sil-card-meta">January 2026 · Near-term · Confirmed · AI Governance / Data Security</div>
    <p>OpenAIが2026年1月28日に公開したAI AgentのURL-based Data Exfiltration対策を基に、Prompt Injection、Redirect、Public URL Verification、User Co…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="microsoft-agent-runtime-defense.md">AI Agent Runtime Defense ― Tool Invocationを「Code Execution」と同じHigh-risk Eventとして守る</a>
    <div class="sil-card-meta">January 2026 · Near-term · Assessment · AI Governance / Operational Security</div>
    <p>Microsoft Defender Security Researchが2026年1月23日に公開したAgent Runtime Securityの研究を基に、Tool Invocation、Generative Orchestration…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="../risk-management/microsoft-data-security-index-2026.md">Data Security Index 2026 ― AI導入Riskの中心が「Tool利用」からData Flowへ移る</a>
    <div class="sil-card-meta">January 2026 · Near-term · Observed · Data Security / AI Governance</div>
    <p>Microsoftが2026年1月29日に公開したData Security Indexを基に、生成AI関連Data Incident、AI-specific Control、DSPM、AI for Data SecurityのSurvey結…</p>
  </article>
  <article class="sil-card">
    <a class="sil-card-title" href="nist-caisi-agent-security-rfi-january.md">NIST CAISI AI Agent Security RFI ― Agent Securityを「Model＋Software System」の問題として定義</a>
    <div class="sil-card-meta">January 2026 · Strategic · Confirmed · AI Governance / Operational Security</div>
    <p>NIST CAISIが2026年1月12日に公開したAI Agent Security RFIを基に、Indirect Prompt Injection、Data Poisoning、Agent Access、Monitoring、Secur…</p>
  </article>
</div>
<!-- AUTO:CATEGORY_ARTICLES:END -->

## Focus Areas

<div class="sil-topics"><span class="sil-topic">Security for AI</span><span class="sil-topic">AI for Security</span><span class="sil-topic">AI Agent</span><span class="sil-topic">Sandbox</span><span class="sil-topic">AI Malware</span><span class="sil-topic">AI Governance</span><span class="sil-topic">Frontier AI</span></div>

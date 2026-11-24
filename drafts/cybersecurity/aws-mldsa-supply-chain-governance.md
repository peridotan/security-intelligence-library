---
title: ML-DSAでSoftware Supply Chainを守る ― AWSにおける耐量子署名とAlgorithm Governance
date: 2026-10-19
updated: 2026-10-20
reviewed: 2026-10-19
review_status: Needs Review
source_period: 2026-10
description: AWSの二部構成ガイドを基に、ML-DSAによるArtifact・SBOM署名と、SCP・IAM・検知によるAlgorithm Policyの実装範囲と限界を整理する。
category: Cybersecurity
collections:
  - cybersecurity
topics:
  - PQC / Crypto Agility
  - Software Supply Chain
  - Security Governance & Risk Management
tags:
  - ML-DSA
  - Post-Quantum Cryptography
  - AWS KMS
  - AWS Private CA
  - Software Supply Chain
  - Crypto Agility
audience:
  - Executive
  - CISO
  - Cloud Security
  - DevSecOps
management_impact: High
impact_types:
  - Software Trust
  - Cryptographic Agility
  - Governance
urgency: Near-term
evidence: Assessment
status: draft
pptx: ""
media_rights: none
---

# ML-DSAでSoftware Supply Chainを守る ― AWSにおける耐量子署名とAlgorithm Governance

<div class="sil-executive-summary" markdown>

## Executive Summary

AWSは2026年10月12日、ML-DSAを使った耐量子Software Supply Chainの構築と、SCP・IAM等によるAlgorithm Policyの統制を二部構成で公表しました。Part 1はAWS KMS、AWS Private CA、IAM Roles Anywhereを組み合わせ、Binary、Container Image、SBOMを署名・検証するArchitectureを示します。Part 2は、組織が承認したML-DSA Parameter SetをAWS API上で予防・検知する方法と、その適用範囲を整理しています。[^aws1][^aws2]

重要なのは、PQCを「Algorithmを有効化する作業」だけで終わらせないことです。長寿命ArtifactのTrust、Build AgentのIdentity、Key／Certificate Lifecycle、Parameter SetのPolicy、例外管理、検知を一体で設計する必要があります。一方、AWSのSCPやIAMは、EC2、Container、Lambda内でApplicationやOpenSSLが実行する暗号処理までは統制できません。[^aws2]

</div>

## なぜ今なのか

AWSは、将来Cryptographically Relevant Quantum Computerが実現した場合、現在の公開鍵署名が破られ、過去に署名された長寿命FirmwareやArtifactの真正性が将来損なわれる「forge later」リスクを説明しています。[^aws1] これは通信のConfidentialityを巡る「harvest now, decrypt later」と別に、Software Integrityの移行期限を考える必要があることを示します。

署名Algorithmの移行には、Key作成だけでなく、Signer Identity、PKI、Artifact形式、Verifier、Trust Store、Policy、監査、Rollbackを含む準備期間が必要です。今すぐ全面移行するかではなく、InventoryとPilotを開始できる状態にすることが重要です。

## 何が起きているのか

### 確認できたAWSの構成例

AWS Part 1は、次の5つを耐量子Software Supply Chainの柱として示しています。[^aws1]

1. AWS KMSでML-DSA署名Keyを生成・保護する。
2. AWS Private CAでML-DSAの証明書階層を構成する。
3. AWS外のBuild Agentは、ML-DSA証明書とIAM Roles AnywhereでWorkload Identityを確立する。
4. Binary、Container Image Manifest、Package等のArtifactをML-DSAで署名する。
5. SBOMをin-toto Statementへ関連付け、同じML-DSA Code-signing Keyで署名する。

### Parameter Setの統制

AWS KMSは`ML_DSA_44`、`ML_DSA_65`、`ML_DSA_87`という3つのKey Specを提供し、いずれもSigning Algorithmは`ML_DSA_SHAKE_256`です。したがって、Parameter Setを識別して統制する条件には`kms:SigningAlgorithm`ではなく`kms:KeySpec`を使う必要がある、とAWSは説明しています。[^aws2]

一方、AWS Private CAの`CreateCertificateAuthority` APIでは、`CertificateAuthorityConfiguration`の`KeyAlgorithm`と`SigningAlgorithm`に`ML_DSA_65`などのParameter Set名を指定します。Private CAの`SigningAlgorithm`にはKMSの`ML_DSA_SHAKE_256`を指定できません。**同じSigningAlgorithmという項目名でも、AWS KMSとAWS Private CAで受け付ける値が異なる**点に注意が必要です。[^aws2]

Part 2の例ではML-DSA-65とML-DSA-87を承認し、ML-DSA-44の作成・利用を制限します。ただしAWSは、ML-DSA-44もFIPS 204で標準化された有効な選択肢であり、除外は脆弱性判断ではなく組織Policyの例だと明記しています。[^aws2]

また、AWS Part 2は、**特定のParameter Setだけを`Deny`する禁止リスト方式では、将来AWSに新しいVariantが追加された際に未評価のVariantが既定で許可され得る**点を注意しています。これを防ぐには、承認済みParameter Set以外を`StringNotEquals`などで拒否する方式（default-deny）も選択肢です。ただし、新Variantの採用時にはPolicy更新が必要です。[^aws2]

さらに、AWS Part 1は米国の**National Security Systems（NSS）向けCNSA 2.0**の対象では、ML-DSAを用いるなら`ML_DSA_87`のみが許容され、例示した`ML_DSA_65`のCode Signing構成はNSSにそのまま適用できないと明記しています。これは米国NSS向けの限定的要件であり、日本企業一般への法的義務と混同してはいけません。[^aws1]

SCPはOrganization RootまたはOUへ適用でき、Member AccountでのKey作成や利用を制限できます。一方、Management Accountには適用されません。IAM Permission BoundaryはPrincipal単位の柔軟性を提供しますが、対象Principalへ確実にBoundaryを付与する仕組みが別途必要です。[^aws2]

### 適用範囲と限界

AWSが示すPolicy Controlは、主にAWS KMS、AWS Private CA、ACM等のAWS Service APIを対象とします。EC2、Container、Lambda上のApplicationやOpenSSLによる暗号処理、Protocol-levelの利用、Algorithmを認識しないCertificate Import／Upload API等は、同じSCP・IAM条件だけでは包括的に制御できません。[^aws2]

AWS Private CAにはCA Algorithm用のCondition Keyがないため、信頼されたProvisioning PipelineでAlgorithmを固定し、CloudTrailやAWS ConfigでDriftを検知する補完が必要とされています。[^aws2]

また、Part 1はIAM Roles AnywhereをWorkload Identityに利用する構成を示していますが、**Part 2のML-DSA Parameter Set統制の検討範囲にはIAM Roles Anywhereのサービス固有の制御が含まれません**。Trust Anchorや証明書による認証などは、別途適用可能な統制を確認する必要があります。[^aws1][^aws2]

## 経営インパクト

| 観点 | 経営上の意味 |
| --- | --- |
| Software Trust | 長寿命Firmware・Artifactの署名検証能力を将来まで維持する必要がある |
| Cloud Governance | Algorithm選定を設計書だけでなく、SCP・IAM・Provisioning・Detectionへ実装する必要がある |
| Supplier | Build Tool、External Runner、Certificate、Verifierを含むSupply Chain全体の対応状況が必要 |
| Cost / Performance | Parameter SetによってKey・Signature Size、Performance、Security Marginが異なる |
| Audit | Key作成・利用、CA作成、例外、Driftを追跡できるEvidenceが必要 |

## 日本企業への示唆

日本企業では、PQC移行をTLSやVPNの更新計画だけで捉えず、Code Signing、Firmware、Container、SBOM、Build Agent IdentityもCrypto Inventoryへ含める必要があります。特に製品寿命が長い機器、組込みSoftware、OT、署名済み配布物は「いつまで署名を信頼する必要があるか」を基準に優先順位を付けるべきです。

また、AWSのPolicy例をそのまま適用するのではなく、自社が承認するAlgorithm／Parameter Set、対象Account・OU、Management Accountの扱い、Application内暗号の統制、例外と移行期限を定義した上で、非本番環境で検証する必要があります。

<div class="sil-action-box" markdown>

## 推奨アクション

1. Code Signing、Firmware、Container、SBOM、PKI、External Build Agentを含むCrypto Inventoryを作る。
2. Artifactの残存期間、更新不能期間、Verifier更新可否から、耐量子署名の優先対象を決める。
3. AWS KMS、AWS Private CA、IAM Roles Anywhereを使った小規模PilotでKey、Certificate、Artifact、SBOM、VerificationをEnd-to-endで確認する。
4. 承認するML-DSA Parameter Setと選定根拠をAlgorithm Policyとして明文化する。
5. SCP、IAM Permission Boundary、Approved Provisioning Pipeline、CloudTrail／AWS Configの責任分界を設計する。
6. Management Account、Application内OpenSSL、Container／Lambda、Certificate Import等の統制外領域をGapとして記録する。
7. Policy例は非本番で検証し、AccessDenied時の運用、例外、Key Cleanup、RollbackをRunbook化する。

</div>

## 用語解説

**ML-DSA**  
NIST FIPS 204で標準化されたModule-Lattice-Based Digital Signature Algorithm。量子計算機と古典計算機の双方による攻撃への耐性を目的とするDigital Signature方式です。

**Crypto Agility**  
Algorithm、Key、Certificate、Protocolを、環境全体を作り直さずに変更・廃止・追加できる能力です。

**Service Control Policy（SCP）**  
AWS Organizationsで、Member AccountやOUに対して利用可能な権限の上限を定めるGuardrailです。Management Accountには適用されません。

## 関連記事

- [Axios Supply Chain Compromise](https://peridotan.github.io/security-intelligence-library/cybersecurity/openai-axios-signing-supply-chain/)
- [PQC認証の準備は証明書エコシステムから ― Microsoft TLS Pilot](https://peridotan.github.io/security-intelligence-library/identity-security/pqc-tls-certificate-ecosystem/)（TLS/PKIの相互運用性と、Software Artifactの署名真正性は、共通のCrypto Agility課題でありながら検証対象が異なる）
- [PQC／Crypto Agilityトピック](https://peridotan.github.io/security-intelligence-library/topics/)

## 参考情報

- [AWS Security Blog, Part 1: Build a software supply chain with ML-DSA](https://aws.amazon.com/blogs/security/quantum-resistant-signing-on-aws-part-1-build-a-software-supply-chain-with-ml-dsa/)
- [AWS Security Blog, Part 2: Enforce your ML-DSA algorithm policy with SCPs and IAM](https://aws.amazon.com/blogs/security/quantum-resistant-signing-on-aws-part-2-enforce-your-ml-dsa-algorithm-policy-with-scps-and-iam/)

[^aws1]: [AWS Security Blog, Quantum-resistant signing on AWS, Part 1, published 2026-10-12](https://aws.amazon.com/blogs/security/quantum-resistant-signing-on-aws-part-1-build-a-software-supply-chain-with-ml-dsa/)
[^aws2]: [AWS Security Blog, Quantum-resistant signing on AWS, Part 2, published 2026-10-12](https://aws.amazon.com/blogs/security/quantum-resistant-signing-on-aws-part-2-enforce-your-ml-dsa-algorithm-policy-with-scps-and-iam/)

# Changelog

## v0.17.1

- Prevented quarterly review dates from breaking inside `Reviewed YYYY-MM-DD`.
- Compacted quarterly statistics into a single desktop row while preserving responsive wrapping.
- No editorial or evidence changes.

## v0.17.0

- Added Q1 2026 Security Intelligence Review based on 30 January-March core themes.
- Compressed Q1 into seven structural shifts spanning agents, cyber capability, identity trust, cybercrime industrialization, data, supply chain, and recovery/enterprise risk.
- Added a Q1-to-Q2 transition section.
- Generalized quarterly required-section validation for Q1-Q4.

## v0.16.0

- Added January 2026 Monthly Intelligence with ten core themes.
- Added coverage of NIST AI-agent security, runtime enforcement, URL-based agent exfiltration, AI application supply-chain risk, AI/data security, SaaS identity theft, domain spoofing through complex mail routing, cybercrime infrastructure, the EU Cybersecurity Package, and Japan's Economic Security Management Guidelines.
- Added selective MITRE ATT&CK® mapping for ShinyHunters-branded SaaS data theft.

## v0.15.0

- Added February 2026 Monthly Intelligence with ten core themes.
- Added coverage of LLM-discovered zero-days, capability-aware cyber access, AI agent identity/standards, AI evaluation uncertainty, adversarial AI, accelerated cross-surface incidents, recovery infrastructure compromise, data classification, EU ICT supply-chain security, and Japanese IT procurement security requirements.

## v0.14.1

- Added March 2026 as a compact Pre-Q2 Signals layer in the Q2 2026 Quarterly Review.
- Added optional `prelude_month` metadata and validation against the monthly archive.
- Polished the June trajectory wording to `運用Architectureへ`.

## v0.14.0

- Added March 2026 Monthly Intelligence with ten core themes.
- Added coverage of AI-as-tradecraft, Tycoon2FA, Teams vishing, deployed-AI monitoring, Japan AI Guidelines for Business v1.2, NIST mDL guidance, CSF/ERM/workforce integration, Japan's SCS policy, cyber-infrastructure provider responsibilities, and M-Trends 2026.
- Added selective MITRE ATT&CK® mapping for Tycoon2FA and Teams vishing.
- Extended the controlled ATT&CK catalog with T1566.004 and T1219.002.

## v0.13.0

- Added Quarterly Review as a first-class synthesis layer.
- Added Q2 2026 Security Intelligence Review based on 30 April-June core themes.
- Compressed Q2 into seven structural shifts and management priorities.
- Added generated quarterly review cards to Home and the Quarterly Review index.
- Added validation for quarterly metadata, source months, required sections, and internal links.

## v0.12.0

- Added selective MITRE ATT&CK® mapping to eight attack/campaign articles.
- Distinguished source-labeled ATT&CK IDs from analyst mappings.
- Added a controlled ATT&CK technique catalog and generated mapping sections.
- Added CI validation for mappings and required MITRE legal/trademark notices.
- Kept reader-oriented attack/process flows independent from ATT&CK mappings.

## v0.11.2

- Replaced flow-like `text` code blocks with semantic attack/process flow UI.
- Migrated four existing flow diagrams.
- Added responsive branch, panel, and loop flow styles.
- Added CI validation to prevent flow diagrams from regressing to plain code blocks.

## v0.11.1

- Changed the Monthly Intelligence archive to a responsive 3/2/1-column grid.
- Added an automatically generated Historical Snapshot banner for superseded articles.
- Added `superseded_by` metadata and validation so superseded guidance links to its successor.

## v0.11.0

- Added April 2026 Monthly Intelligence with ten core themes.
- Added coverage of Claude Mythos Preview, AI-enabled threat operations, device-code phishing, the Axios supply-chain compromise, Advanced Account Security, EUDI Wallet certification, NIST IoT lifecycle guidance, NIST PQC key-generation guidance, Japan's SCS evaluation scheme, and the April critical-infrastructure unified-standard draft.
- Marked the April critical-infrastructure draft article as `Superseded` and linked readers to the July final-standard article.

## v0.10.0

- Added May 2026 Monthly Intelligence with ten core themes.
- Added articles covering Japan's Project YATA-Shield, FSA frontier-AI patch readiness, NIST agent security, Singapore agentic governance, coding-agent runtime controls, trusted access to cyber-capable AI, npm/CI-CD supply-chain attacks, edge-to-identity compromise, AiTM token theft, and OT response/recovery.
- Reused the curated Topics / detailed Tags architecture introduced in v0.9.x.

## v0.9.1

- Polished Home messaging for a public-facing audience.
- Aligned the Home kicker with the `Management View` terminology.
- Added dynamic article/topic/tag statistics and a Tags CTA to Topics.
- Added back-to-directory navigation for long Topic pages.
- Standardized `AI-Enabled Threats` capitalization.

## v0.9.0

- Split controlled editorial Topics from granular Tags.
- Added an 18-topic controlled taxonomy in `config/topics.yml`.
- Curated 1-3 Topics for all 30 published articles.
- Rebuilt Topics as a grouped editorial directory.
- Added a separate generated Tags index for detailed keywords.
- Added Topics to article metadata and CI validation.

## v0.8.1

- Renamed Home "Latest Intelligence" to "Current Intelligence".
- Replaced monthly "as of" labels with explicit "Reviewed" dates.
- Migrated monthly front matter from `as_of` to `reviewed`.
- Replaced the Mastra npm archive reference with Microsoft's dedicated incident analysis.
- Added Socket's independent Mastra technical analysis as a secondary source.

## v0.8.0

- Added June 2026 Monthly Intelligence with ten core themes.
- Added production articles on agent trust boundaries, MCP tool poisoning, continuous AI security, AI-powered vulnerability discovery, AI framework supply-chain compromise, ransomware risk management, OT backup, OT remote access, PQC identity migration, and integrated system planning.
- Existing front-matter-driven indexes automatically incorporate the new month and articles.

## v0.7.1

- Fixed generated HTML checker false positives caused by Zensical/theme `<article>` elements.
- Card balance validation now scopes itself to `sil-card` article elements.

## v0.7.0

- Introduced front-matter-driven generation for Home, category indexes, monthly archives, monthly core-theme cards, and Topics.
- Fixed malformed Monthly Intelligence card markup introduced in v0.6.0.
- Added Source Period, Last Reviewed, Review Status, collections, and impact areas to article metadata.
- Simplified primary navigation to index pages only.
- Added one-command content refresh via `scripts/update_content.py`.
- Added conservative weekly external-link checking and review-freshness monitoring.
- Added generated-HTML validation after the Zensical build.
- Added source-level checks for generated card structure.

## v0.6.0

- Added July 2026 Monthly Intelligence archive with nine core themes.
- Added nine production intelligence articles covering agentic ransomware, identity lifecycle attacks, passkey migration, AI cyber capability evaluation, AI infrastructure security, C-SCRM, EU AI/cyber policy, and exploited trust-infrastructure vulnerabilities.
- Updated category indexes, Topics, Home monthly archive, and Zensical navigation.

## v0.5.3

- Clarified affirmative AI-use disclosure and human editorial responsibility.
- Added quotation, media, trademark, privacy, and non-endorsement policies.
- Split repository licensing into a dispatcher `LICENSE` and unmodified MIT `LICENSE-CODE.txt`.
- Added `RIGHTS_REVIEW.md`, `CONTRIBUTING.md`, and `.github/SECURITY.md`.
- Disabled Google Fonts autoloading.
- Pinned Zensical 0.0.56, PyYAML 6.0.3, and Python 3.14 in CI.
- Added Dependabot for pip and GitHub Actions.
- Excluded redirect compatibility pages from internal search.
- Added CI rights guardrails for embedded media, quotations, and scripts.

## v0.5.2

- Added MIT license for software portions of the repository.
- Added `COPYRIGHT.md` to separate editorial-content rights from software licensing.
- Added `THIRD_PARTY_NOTICES.md`.
- Added Copyright and Licensing policy to About.
- Updated the site footer to `© 2026 peridotan. All rights reserved.`.

## v0.5.1

- Stacked article metadata into one column at <= 420px.
- Made Markdown tables horizontally scrollable on narrow screens.
- Hid the mobile secondary/floating table-of-contents surface at <= 420px to avoid content overlap.
- Converted reference lists and generated footnotes to compact linked source titles.

## v0.5.0

- Added Monthly Intelligence archive and August 2026 executive summary.
- Reduced Home to latest six intelligence articles.
- Added clickable Topics navigation.
- Expanded Editorial Policy.
- Added Evidence and Urgency metadata.
- Made front matter the metadata source of truth.
- Added conditional PowerPoint rendering.
- Enabled inline footnotes and tooltips.
- Added CI content-quality checks.
- Reframed Risk Management as Management View.

## v0.4.0

- Added six production intelligence articles for August 2026.
- Added an August 2026 Intelligence collection of ten core themes to the home page.
- Added vulnerability exploitation-window, agentic AI security controls, PLC/OT targeting, AI-enabled malware, EU AI Act enforcement, and Japan critical-infrastructure articles.
- Updated Cybersecurity, AI Security, Regulation, and Risk Management landing pages.
- Updated navigation for the new production articles.

## v0.3.1

- Added compatibility pages for URLs used by the former sample articles.
- `/cybersecurity/credential-attack-sample/` now redirects to `large-scale-credential-attacks`.
- `/ai-security/frontier-ai-cyber-sample/` now redirects to `frontier-ai-cyber-capabilities`.
- This prevents stale browser navigation, old bookmarks, and cached links from returning 404 after the v0.3.0 content migration.

## v0.3.0 - 2026-08-26

### Added
- Added five production articles based on public primary and authoritative sources:
  - Frontier AI cyber capabilities and the Cyber Critical threshold
  - AI Agent Identity / Non-Human Identity (NHI)
  - Large-Scale Credential Attacks
  - Pass-ta-key / Pass-the-Passkey
  - Generative AI usage governance
- Added cross-links between related Cybersecurity, Identity, AI Security, Regulation and Risk Management topics.
- Added source URLs and explicit distinctions between verified facts and unverified attacker claims where applicable.

### Changed
- Replaced sample articles with production article URLs.
- Updated homepage Latest Intelligence cards to show five real articles.
- Updated all category landing pages and navigation.
- Updated AI governance references to AI Guidelines for Business Ver. 1.2 (2026-03-31).

### Removed
- Removed `frontier-ai-cyber-sample.md`.
- Removed `credential-attack-sample.md`.

## v0.2.1 - 2026-08-26

### Fixed
- Fixed the homepage and category-page layout collapsing into unintended horizontal columns.
- Replaced Zensical `grid cards` markup with a self-contained `sil-cards` CSS layout.
- Added explicit vertical-flow and responsive layout rules for desktop and mobile.

### Compatibility
- GitHub Pages workflow is unchanged from v0.2.0.

## v0.2.0 - 2026-08-26

### Added
- Portal-style homepage.
- Category cards and featured topics.
- Article metadata and management-impact display.
- Custom stylesheet.

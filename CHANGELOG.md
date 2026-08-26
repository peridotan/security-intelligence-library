# Changelog

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

# Security Intelligence Triage Promotion — AI review proposal

- Source run: `37864974541`
- Source triage PR: #30 (merged 2026-10-09)
- Proposal date: 2026-10-09
- Status: **Pending human approval**
- Proposed Library promotions: **3 of 32** (Watch remaining: **29**)
- This file is a **separate recommendation**; the original 32-candidate triage is retained unchanged for auditability.

## Proposed Library candidates (create one Draft per row)

| Candidate (original number) | Rationale | Primary source |
| --- | --- | --- |
| #13 DNS root KSK rollover | ICANN schedules 2026-10-11 rollover; prompt verification of KSK-2024 trust anchor on DNSSEC validating resolvers | https://blog.cloudflare.com/root-ksk-2024-rollover/ |
| #1 PQC authentication certificate ecosystem | Microsoft PQC TLS pilot is **non-production only**; enterprise PKI, HSM and certificate interoperability deserve practical readiness coverage | https://www.microsoft.com/en-us/security/blog/2026/10/08/post-quantum-authentication-why-organizations-should-start-testing-certificate-ecosystems-now/ |
| #6 Evidence-grounded vulnerability triage | AWS three-stage validation provides a practical method distinct from already documented MDASH. **Use Part 2 as supporting material; do not create a separate draft for #5** | https://aws.amazon.com/blogs/security/building-your-ai-vulnerability-harness-part-1/ |

### Independent official reference for DNS item
https://www.icann.org/resources/pages/ksk-rollover-en

## Existing Library articles checked
- `docs/identity-security/pqc-piv-dual-stack.md`
- `docs/identity-security/nist-key-generation-pqc-sp800-133r3.md`
- `docs/cybersecurity/mdash-ai-vulnerability-discovery.md`

The proposed drafts must preserve those articles and link them as related context. Verify primary source and non-duplication before writing.

## Separate update-existing proposals (not included in this Draft trigger)
- AWS Identity-aware AI data agents: update `docs/identity-security/ai-agent-identity-nhi.md` (candidate #14).
- Cloudflare evidence-grounded Agentic Security Operations: update `docs/ai-security/agentic-ai-security-controls.md` (candidate #7).

These are **not** additional `draft_eligible=true` records in this promotion; they require an explicit update-existing path so the Work task does not create duplicate articles.

## Human approval and publication gates

Merging this PR is the human decision to promote **only the three Library candidates above** and may trigger the existing ChatGPT Work article-drafting task because the PR title follows its required prefix and the changed file matches `.automation-review/candidates-*.json`. The current Work task should produce article Markdown and review summary only; it must **not** publish, commit, or merge article content. Review completed drafts separately before integration.

The prior merged 32-candidate snapshot remains unchanged. No OpenAI API is used by this proposal.

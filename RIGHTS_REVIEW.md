# Rights and Publication Review

Review date: 2026-08-27

## Purpose

This file records an editorial and technical rights screening of the public
Security Intelligence Library repository. It is **not** a lawyer's legal
opinion and does not guarantee that no third-party claim can arise.

## Current Screening Result

At the time of this review:

- No third-party image files are stored under `docs/`.
- No article contains Markdown/HTML embedded images.
- No published article contains Markdown blockquote passages.
- No iframe, embed, or object content is used in published articles.
- Source material is primarily summarized/paraphrased and linked.
- Article source URLs are present and checked syntactically by CI.
- Editorial content and software licensing are separated.
- The MIT license text for code is stored unmodified in `LICENSE-CODE.txt`.
- Google Fonts autoloading is disabled to reduce unnecessary third-party requests.
- External editorial-content pull requests are not accepted by default, avoiding
  ambiguous copyright ownership of contributed articles.
- Product/company names are used for identification and analysis; no affiliation
  or endorsement is claimed.
- Selected articles reproduce MITRE ATT&CK® technique names/IDs under MITRE's
  published Terms of Use; the required copyright designation, permission notice,
  trademark acknowledgment, and non-endorsement language are included.

## Remaining Limitations

This screening does not constitute:

- trademark clearance for the site name;
- a jurisdiction-by-jurisdiction copyright opinion;
- permission from every linked publisher;
- a guarantee that an AI-assisted sentence cannot accidentally resemble a
  third-party work;
- a review of every upstream transitive dependency bundled by Zensical;
- a guarantee that external source terms or licenses will not change;
- a limitation on rights granted under GitHub's own Terms of Service. A public
  repository is subject to GitHub's platform license terms, including rights
  needed to host/display content and public-repository fork/view functionality.

GitHub Terms:
https://docs.github.com/en/site-policy/github-terms/github-terms-of-service

## Checklist for New Articles

Before publication:

1. Confirm the article is based only on public, publishable information.
2. Prefer primary sources for material facts, dates, numbers, regulations, and claims.
3. Distinguish fact, vendor observation, threat-actor claim, and assessment.
4. Paraphrase in original language; avoid long verbatim passages.
5. If quoting, keep only what is necessary and identify the source.
6. Do not add third-party images, screenshots, logos, or figures without a
   documented rights basis.
7. Do not upload confidential, NDA, personal, credential, or customer information.
8. Verify external links and source attribution.
9. Review AI-assisted text for accuracy, overstatement, and suspiciously close wording.
10. Run `python scripts/check_content.py` before publishing.

## Media Rule

Published articles that contain images or embedded media must declare an
explicit `media_rights` value in front matter, such as:

- `original`
- `licensed`
- `permission`
- `public-domain`

The CI checker rejects unreviewed media by default.

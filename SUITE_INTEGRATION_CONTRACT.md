# Security Intelligence Suite Integration Contract v1.0

This document defines the stable context handoff contract between:

- Security Intelligence Library
- Threat Investigation
- Vulnerability Intelligence

## 1. Design principles

1. Context handoff is navigation or investigation metadata unless explicitly backed by source evidence.
2. Threat Actor context does not imply a direct Actor-to-CVE relationship.
3. ATT&CK Technique context does not create a new ATT&CK relationship.
4. Multiple context values may be passed without forcing automatic selection.
5. Unknown or unsupported context must fail safely.
6. Existing stable parameters should remain backward compatible.

## 2. Common parameters

- `from`: source tool
- `context`: source path or identifier
- `contextTitle`: human-readable source title
- `entity`: primary Threat Investigation entity
- `actor`: repeated ATT&CK Group ID
- `technique`: repeated ATT&CK Technique ID
- `cve`: repeated CVE ID
- `scope`: Vulnerability Intelligence scope

## 3. Evidence boundary

The Suite distinguishes:

- Navigation Context
- Investigation Context
- Source-recorded Evidence

Navigation Context or Investigation Context must never be promoted into Source-recorded Evidence merely because values occur in the same handoff.

## 4. Contract version

- Security Intelligence Suite Integration Contract: `1.0`
- Context Index schema: `1.1`

## 5. Parameter semantics

### `from`

Identifies the source tool or source context.

Examples:

- `security-intelligence-library`
- `threat-investigation`
- `threat-actor`
- `vulnerability-intelligence`

This is navigation metadata only.

### `context`

Opaque source path or source identifier.

Example:

`/security-intelligence-library/site/identity-security/example/`

Consumers must not infer threat relationships from this value.

### `contextTitle`

Human-readable label for the source context.

This is display metadata only.

### `entity`

Defines one primary Threat Investigation target.

Supported forms include:

- `entity=actor:G0032`
- `entity=software:S1242`
- `entity=technique:T1190`
- `entity=platform:ESXi`
- `entity=campaign:C0001`

When present, Threat Investigation may preselect that entity.

### `actor`

Repeated ATT&CK Group ID parameter.

Examples:

- `actor=G1057`
- `actor=G1057&actor=G0032`

Actor context does not itself establish a direct relationship to a CVE.

### `technique`

Repeated ATT&CK Technique or Sub-technique ID parameter.

Example:

`technique=T1078&technique=T1098.005&technique=T1566.004`

If multiple Techniques are supplied without an explicit `entity`, the target should not arbitrarily select one.

### `cve`

Repeated CVE parameter.

Example:

`cve=CVE-2026-49869&cve=CVE-2026-48710`

CVE context means the source article or workflow referenced those CVEs.

### `scope`

Vulnerability Intelligence scope.

Supported values:

- `scope=all`
- `scope=my`

`all` evaluates the loaded vulnerability dataset.

`my` applies the user's environment/watchlist overlay.

## 6. Security Intelligence Library Front Matter

Library articles may explicitly define handoff context.

Example:

```yaml
handoff:
  actors:
    - G1057
  techniques:
    - T1078
  cves:
    - CVE-2026-12345
```

Supported keys:

- `actors`
- `exclude_actors`
- `techniques`
- `exclude_techniques`
- `cves`
- `exclude_cves`

Threat Actor IDs should be explicitly assigned rather than inferred solely from free-text Actor names.

ATT&CK Techniques may also be derived from `mitre_attack` metadata.

CVEs may be automatically detected from article content unless explicitly overridden.

## 7. Context Index

Security Intelligence Library publishes:

`docs/assets/context-index.json`

Current schema version:

`1.1`

The Context Index is generated data and must not be edited manually.

## 8. Current handoff patterns

### Library to Threat Investigation

Single Actor with related Techniques:

```text
?from=security-intelligence-library
&context=<source-path>
&contextTitle=<article-title>
&actor=G1057
&technique=T1078
&technique=T1098.005
&technique=T1566.004
&entity=actor:G1057
```

The Actor may be preselected as the primary investigation target.

The Technique values remain article context and do not create new ATT&CK relationships.

### Library to Threat Investigation with multiple Techniques

```text
?from=security-intelligence-library
&technique=T1021.004
&technique=T1078.002
&technique=T1190
```

When multiple Techniques are supplied without an explicit `entity`, Threat Investigation should present them as selectable context rather than selecting one arbitrarily.

### Library to Vulnerability Intelligence

```text
?scope=all
&from=security-intelligence-library
&context=<source-path>
&contextTitle=<article-title>
&cve=CVE-2026-49869
&cve=CVE-2026-48710
```

The supplied CVEs may be used to filter or prioritize vulnerability data.

### Threat Investigation to Vulnerability Intelligence

```text
?scope=all
&from=threat-actor
&actor=G0032
&actorName=Lazarus%20Group
```

`actorName` is human-readable display metadata.

Actor context in this flow does not establish a direct Actor-to-CVE relationship.

## 9. Optional Threat Investigation parameters

Threat Investigation may also accept:

- `lens`
- `overlay`

Current `lens` values include:

- `general`
- `identity`
- `internet`
- `virtualization`
- `server`
- `cloud`

Current `overlay` values include:

- `none`
- `all`
- `identity`
- `internet`
- `virtualization`
- `server`
- `cloud`
- `custom`

These parameters affect investigation presentation and environment context. They do not create new threat evidence.

## 10. Validation

Security Intelligence Library validates Suite handoff metadata before publication.

Validation includes:

- identifier syntax
- duplicate values
- include/exclude conflicts
- supported handoff keys
- ATT&CK Technique existence
- Threat Actor existence in Threat Investigation data
- generated Context Index integrity

Invalid Suite context must fail CI before publication.

The current validation entry point is:

`python scripts/check_suite_handoff.py`

## 11. Compatibility policy

This contract follows semantic versioning principles.

- Patch: clarification with no behavior change
- Minor: backward-compatible new parameters or values
- Major: incompatible contract change

Existing stable parameters should not be removed or reinterpreted without a major contract version change.

## 12. Canonical contract

This document is the canonical Security Intelligence Suite integration contract.

Tool-specific repositories may maintain their own implementation notes, but those documents should remain compatible with this contract.

Current versions:

- Security Intelligence Suite Integration Contract: `1.0`
- Context Index schema: `1.1`

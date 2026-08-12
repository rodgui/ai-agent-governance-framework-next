# AGENTS.md — AI Agent Governance Framework Next

## Mission

Maintain the canonical, vendor-neutral governance framework for AI agents. The repository must explain the complete path from no formal governance to sustained business-as-usual operation and must keep policy, controls, evidence and implementation guidance traceable.

## Canonical boundaries

- This repository is the authority for the framework, control catalog, design patterns, reusable templates, schemas, fictional examples, research crosswalks and framework-maintenance records.
- Do not add consulting pricing, sales collateral, client-specific delivery playbooks or real organizational evidence.
- Do not add client, employer or customer data. Examples must be demonstrably fictional.
- Vendor implementations may appear only as non-normative examples or mappings; normative requirements must remain vendor-neutral.

## Documentation rules

- Preserve definitions, rationale, conditions, exceptions, procedures, controls, evidence and examples. Do not replace detailed material with generic summaries.
- Define specialized terms and expand abbreviations on first use.
- Every normative requirement must identify applicability, accountable role, expected evidence and validation method, directly or by an unambiguous link.
- Link chapters to controls, patterns, templates, schemas and examples rather than duplicating diverging copies.
- Cite primary sources. Label legal interpretation, normative requirements, guidance and case-study observations distinctly.

## Change discipline

1. Identify affected requirements, controls, artifacts and crosswalks.
2. Update the canonical content and every dependent reference in the same change.
3. Add or update tests when a schema, control ID, validation rule or generator changes.
4. Update `CHANGELOG.md` for user-visible changes.
5. Record material architectural or governance decisions in `project/decisions/`.
6. Never rewrite migration provenance or historical decisions silently.

## Required validation

Before committing, run the repository validation entry point documented in `README.md`. At minimum validate Markdown structure, internal links, MkDocs build, JSON schemas, examples, IDs, cross-references, Python tests, secret scanning and fictional-data constraints.

## Prohibited actions

- Do not modify `/Users/rodgui/Nox/Projects/ai-agent-governance-framework`.
- Do not publish, create remotes or push without Rodgui's explicit approval.
- Do not introduce credentials, tokens, personal data or confidential corporate information.
- Do not resolve a material contradiction or delete substantive content without a recorded decision.

# Conflitos e decisões

## Exceção explícita de identidade no template — EXC-G1-001

Em 2026-08-11, o repository owner decidiu manter a frase `Do not publish, create remotes or push without Rodgui's explicit approval.` exclusivamente em `ai-agent-governance-implementation-template/AGENTS.md`. A ocorrência identifica a autoridade de publicação do repositório; não constitui exemplo, registro organizacional ou evidência de implementação. O allowlist é exato por path e frase. Qualquer outro dado real no template continua proibido e fail-closed. A decisão detalhada está em `control/GATE1_EXCEPTIONS.md` no workspace local de reconstrução.

# micro-01

# micro-01a

# micro-01a relationships

## Scope and source identity

This report covers the single manifest path `controls/control-catalog.json` from the immutable snapshot at commit `5545d9227624400ab8bb707b6032b2f61329a36e`.

- Source type: JSON
- Source status: `current-at-source-commit`
- Reader: `subagent:gpt-5.6-luna:micro-01a`
- Fully read: yes, line 1 through line 2110
- SHA-256: `f9377c027c294afa2073002f7267f0ac985141bed5b6750e02cd249261b45535`
- Size: 74,688 bytes
- Lines: 2,110
- Generated structured leaves preserved: 1,268
- Target candidate: `ai-agent-governance-framework-next/toolkit/controls/control-catalog.json`

The source top-level contract is `schemaVersion: "2.0"`, `catalogVersion: "1.2.0"`, title `AI Agent Governance Framework — Control Catalog`, and `lastReviewed: "2026-08-10"`. The catalog contains 44 control objects. All 44 control IDs are unique, all 44 records have the same 16-key field set, and no required list is empty.

## Exact preservation relation

| Source | Target | Relation | Preservation decision |
|---|---|---|---|
| `controls/control-catalog.json` | `ai-agent-governance-framework-next/toolkit/controls/control-catalog.json` | Complete machine-readable control catalog | Preserve the structured object and ordering as the source contract; retain every ID, field, value, schema/catalog version, mapping, blocking flag and `lastReviewed` value. Attach source commit, SHA-256, byte size, line count and reader through the audit ledger rather than mutating the source JSON with new provenance fields. |

The curation transformation is `preserve-verbatim-control-catalog-with-provenance-and-target-schema-validation`. No control is assigned to an archive-only destination, consulting destination or implementation-template copy in this batch.

## Semantic inventory and relations

The 44 controls span 15 domains:

| Domain | Count |
|---|---:|
| adoption | 2 |
| audit | 3 |
| data | 3 |
| evaluation | 3 |
| identity | 3 |
| lifecycle | 2 |
| model | 3 |
| operations | 3 |
| organization | 3 |
| responsible-ai | 3 |
| registry | 3 |
| risk | 4 |
| security | 3 |
| tools | 3 |
| value | 3 |

Observed catalog-wide facts preserved in the file record include:

- Control type occurrences: preventive 33, detective 35, responsive 8, corrective 16.
- Automation values: assisted 24, manual 10, automated 9, mixed 1.
- Scope values: `agent` 40 and `organization` 4.
- Tier applicability occurrences: T1 22, T2 43, T3 44, T4 44.
- Blocking values: `true` 27 and `false` 17.
- Framework mappings: 67 total — NIST AI RMF 1.0 (32), EU AI Act (21), MITRE ATLAS (7), OWASP Top 10 for Agentic Applications (5), and OWASP MCP Top 10 (2).

Every mapping note repeats the source boundary that the mapping is directional and does not constitute equivalence, compliance or attestation. That limitation is preserved as source content and is not upgraded into a compliance claim.

## Cross-control dependencies

- `AGF-OPS-003` explicitly triggers `AGF-RSK-003` when a change is material. This is a direct operations-to-risk reassessment relation and must remain intact.
- `AGF-ORG-001` explicitly points agent ownership treatment to `AGF-REG-001`. This is a direct governance-mandate-to-registry relation and must remain intact.
- All `AGF-[A-Z]{3}-NNN` references found in the source resolve to IDs defined in the same catalog; no undefined control reference was found.
- Framework mappings are external-reference relations only. The source provides framework names and reference strings, not inline URLs or evidence of formal equivalence.

## Exact and semantic duplication

No exact duplicate control IDs or duplicate records were found. The catalog contains deliberate near-neighbor boundaries rather than duplicates:

- `AGF-AUD-001` covers reconstruction/correlation; `AGF-AUD-002` covers evidence package integrity and distinct evidence states; `AGF-AUD-003` covers access, retention and export.
- `AGF-DAT-001` establishes source/data ownership contracts; `AGF-DAT-002` enforces authorization and minimization before retrieval; `AGF-DAT-003` covers lineage, retention, correction and deletion propagation.
- `AGF-EVA-002` is the pre-release evidence gate; `AGF-EVA-003` is runtime sampling, drift and regression learning.
- `AGF-IDN-001` establishes attributable workload identity; `AGF-IDN-002` limits authorization scopes; `AGF-IDN-003` governs secret storage and revocation.
- `AGF-LFC-001` governs valid lifecycle/operational state transitions; `AGF-LFC-002` governs dormancy and owner succession.
- `AGF-MDL-001` approves provider/model/version/data combinations; `AGF-MDL-002` binds evaluation to model version; `AGF-MDL-003` governs approved fallback, fail-closed behavior and exit planning.
- `AGF-OPS-002` provides agent/identity/tool/connector containment and rollback; `AGF-TOL-003` provides capability-level revocation and circuit breaking independently of the agent.
- `AGF-ORG-003` defines the general exception record and expiry requirement; `AGF-RSK-004` applies the admissibility-specific restricted/prohibited production rule.
- `AGF-REG-003` governs attestation expiry and sunset; `AGF-LFC-002` supplies dormancy/ownership triggers that can lead to a lifecycle outcome.
- `AGF-RSK-001` classifies risk tier, while `AGF-RSK-004` explicitly keeps admissibility as a separate dimension. This separation is an intentional anti-duplication boundary.

## Conflicts and contradictions

No material internal contradiction was found in the fully read JSON:

- Every record uses the same field vocabulary and valid observed enum values.
- IDs are unique and all framework mapping notes use the same non-equivalence limitation.
- The variation in `blocking`, `scope`, `automation`, `type` and tier applicability is per-control data, not a schema conflict.
- `AGF-RSK-004` resolves rather than creates a tier/admissibility ambiguity by requiring the dimensions to be decided separately.

## Gaps and limitations

1. The source JSON has no embedded provenance property, source URL, `$schema` URI or mapping-evidence package. The generated file ledger supplies the immutable commit, hash, size, line count, full-read method, reader and status; no unsupported provenance or compliance evidence was invented inside the catalog.
2. The source has version values but does not itself define a target schema `$id` compatibility alias. If a later target schema migration changes `$id`, that requires a separate compatibility decision; it is not an unresolved decision for this batch and the catalog versions must not be changed here.
3. Framework references are alignment pointers only. They do not prove coverage, conformity or legal applicability, and the target must preserve that limitation.
4. Implementation, evidence and metric entries are control guidance/data, not proof that an implementation or verification has already occurred. The target must not present them as completed evidence.
5. No Markdown headings exist in this JSON file, so there is no heading subtree to map. The empty headings output is intentional, not an omission.

## Destination classification

The source is a normative structured control catalog and belongs under the framework toolkit controls area. Its implementation actions, evidence expectations and metrics may inform an implementation template later, but no separate template copy is authorized or needed for this microbatch. No consulting-specific content was identified.

## Material decisions

- Decision applied: preserve the catalog at `ai-agent-governance-framework-next/toolkit/controls/control-catalog.json`.
- Decision applied: retain `schemaVersion` and `catalogVersion` independently, with no renumbering or silent control omission.
- Decision applied: retain framework mappings as directional/non-equivalent references and retain ledger provenance outside the source JSON.
- Unresolved decision-required items for this batch: none.
- Blocked paths for this batch: none.

## Validation evidence

The generator was run from the control directory:

```text
python3 generate_curated_microbatch_records.py micro-01a-curation.json
```

It returned `expected_paths: 1`, `file_records: 1`, `markdown_headings_expected: 0`, and `heading_rows: 0`. An independent validator then confirmed:

- Manifest paths exactly equal generated file-record paths.
- Generated record has every required contract key and `fully_read: true`.
- Reader is exactly `subagent:gpt-5.6-luna:micro-01a` and status is `reviewed`.
- SHA-256, bytes and lines match the immutable source: `f9377c027c294afa2073002f7267f0ac985141bed5b6750e02cd249261b45535`, 74,688, 2,110.
- All 1,268 flattened JSON leaves equal the source's parsed structured content.
- Mechanical heading rows exactly match the assigned-path subset: expected 0, produced 0.
- Candidate destination is exactly `toolkit/controls/control-catalog.json`.

## Completion counts

- Expected paths: **1**
- File records: **1**
- Markdown headings expected from `mechanical-heading-index.csv`: **0**
- Heading rows produced: **0**
- Blocked paths: **0**
- Decision-required items: **0**

# micro-01b

# micro-01b relationships and migration decisions

## Scope, authority, and read evidence

This report covers exactly the 12 paths in `control/micro-01b.txt`, read from the immutable source snapshot at:

- Source snapshot: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot`
- Commit: `5545d9227624400ab8bb707b6032b2f61329a36e`
- Reader: `subagent:micro-01b:gpt-5.6-luna:2026-08-11`
- Output directory: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/control/`
- Protected original: `/Users/rodgui/Nox/Projects/ai-agent-governance-framework`

Every assigned file was read completely from its first line through its final line before curation/generation. The eight substantive files were read semantically, including all Markdown subtrees, tables, front matter, links, enumerations, constraints, conditions, examples, mappings and limitations. The four `.gitkeep` files were inspected as complete one-line placeholders and are recorded as non-substantive rather than treated as empty policy or schema artifacts.

## Exact source inventory and provenance

| Manifest path | Type | Lines | Bytes | SHA-256 | Ledger status | Destination classification |
|---|---:|---:|---:|---|---|---|
| `references/sources.md` | Markdown | 55 | 6,249 | `c29c6a12fe34561cf2fd24e8b9b210a33495e9541ee5b73819f4229002dc2215` | reviewed | research/source ledger |
| `schemas/model-provider-catalog.schema.json` | JSON Schema | 219 | 4,793 | `ebf56eace1367b54a1c0ac1f600bc6bba456ce1e0e5f461d670baacc6c613f3d` | reviewed | target schema contract |
| `docs/patterns/runtime-observability-and-quarantine.md` | Markdown | 141 | 3,738 | `75ea0baa4a79692a41ed679df00056d6e644f260dff1b80e535e104e54bd1a54` | reviewed | vendor-neutral pattern/toolkit |
| `templates/governance-forum-tor.md` | Markdown | 91 | 3,210 | `46a85708272a567afed5dadb399da98a1f581de1b86807fe73a8a8ad1687fccd` | reviewed | canonical governance template plus implementation instantiation |
| `templates/attestation-sunset-record.md` | Markdown | 82 | 2,757 | `0d5b98ed1a6e8b31b36befe8382634ebb79b3fe8b4d67886aa20133bd208f766` | reviewed | lifecycle template plus implementation record |
| `docs/architecture/quality-attributes.md` | Markdown | 51 | 1,664 | `92b08ecf8cba931ed82c330bd27dd0c95b9e18678944240a875583bdad5fa8ad` | reviewed | architecture quality-attributes section |
| `templates/sunset-plan.md` | Markdown | 32 | 1,207 | `17691d68177f43aef1e97d414e43e1e3c5d2ba014a1acd987a32494254f07e0c` | reviewed | controlled-decommissioning template |
| `requirements-docs.txt` | plain text | 3 | 64 | `49fa610a7611784ea68756aceae99388883b5e0e730468cedf592bd7faa9c69e` | reviewed | documentation build dependency pins |
| `assessments/risk-assessments/.gitkeep` | plain text placeholder | 1 | 18 | `5092e9ac41da1a39d8d3bb6a26eee7416bb7d0ca760942892dbe01fd2b8cf62a` | non-substantive | omit after real assessment structure exists |
| `docs/auditability/.gitkeep` | plain text placeholder | 1 | 18 | `5092e9ac41da1a39d8d3bb6a26eee7416bb7d0ca760942892dbe01fd2b8cf62a` | non-substantive | omit after auditability content is mapped |
| `docs/responsible-ai/.gitkeep` | plain text placeholder | 1 | 18 | `5092e9ac41da1a39d8d3bb6a26eee7416bb7d0ca760942892dbe01fd2b8cf62a` | non-substantive | omit after responsible-AI content is mapped |
| `schemas/.gitkeep` | plain text placeholder | 1 | 18 | `5092e9ac41da1a39d8d3bb6a26eee7416bb7d0ca760942892dbe01fd2b8cf62a` | non-substantive | omit after real schemas exist |

The curation configuration preserves this exact manifest order. Source provenance is kept in the generated ledger; no unsupported provenance fields were added to source content.

## File-by-file semantic relations and destination decisions

### `references/sources.md`

This is a source ledger, not a claim register or an evidence package. It contains 19 records in three collections: eight standards/regulation/principles records (`NIST-001`/`NIST-002`, `ISO-001`–`ISO-004`, `EU-001`, `OECD-001`), six security/threat-informed records (`OWASP-001`–`OWASP-004`, `MITRE-001`, `CSA-001`), and five Microsoft Customer Zero/application-evidence records (`MS-001`–`MS-005`). Each record preserves ID, title, type, URL, access date and related use.

The evidence hierarchy is retained as an analysis aid: legislation/standards/official documentation; operational data and system evidence; responsible-technology publications; academic/independent research; recognized secondary sources; institutional reports/opinion. The source explicitly says that the hierarchy does not remove the need to evaluate currency, scope, conflict of interest and applicability.

The target is `ai-agent-governance-framework-next/research/sources/bibliography.md`, using `move-and-relink-with-source-ledger-and-date-caveats`. The relative `standards/README.md` link must be rebuilt only after the target path is verified. ISO URLs remain official pages and not reproductions of protected standards. MITRE/OWASP mappings require version/evidence cutoffs. Microsoft articles remain institutional accounts and do not become independent audits, causal ROI evidence or causal incident-reduction evidence. No reference may be upgraded to certification, equivalence or automatic compliance.

### `schemas/model-provider-catalog.schema.json`

This is the complete JSON Schema Draft 2020-12 contract for an Approved Model and Provider Catalog; it is not a catalog instance and contains no concrete entries. Preserve `$schema`, the source `$id`, title/description, top-level `additionalProperties: false`, six top-level required fields, `$ref: #/$defs/entry`, and the full entry contract. Preserve all 15 required entry properties, exact enum families, patterns, minimum lengths/items, uniqueness rules, date formats, optional fields and both `allOf` conditions:

- `status: conditional` requires `conditionRefs`;
- `versionPinned: false` requires `changeDetectionRef`.

The target is `ai-agent-governance-framework-next/schemas/model-provider-catalog.schema.json`, using `preserve-schema-verbatim-with-provenance-and-draft-2020-12-validation`. The source `$id` points to the original GitHub identity. Any target identity/path change is a compatibility decision, not a silent relink. Instances created later must remain separate from this schema and must retain evaluation, review-expiry, allowed data classes/regions/tiers and exit strategy. Parsing JSON alone is not sufficient validation: the target needs a Draft 2020-12 validator with `$ref` resolution and effective date-format checking.

### `docs/patterns/runtime-observability-and-quarantine.md`

This maintained, quarterly-reviewed vendor-neutral pattern defines the chain `signal → severity → decision authority → containment action → evidence preservation → remediation → regression → reactivation`. It explicitly models quarantine as a lifecycle state, not a UI button. It preserves the Mermaid flow from signal detection/triage through Run Authority, containment controls, quarantine, evidence/remediation, regression, and approved reactivation or rejected sunset.

The eight operational steps, required controls, evidence artifacts, metrics (`MTTD`, `MTTDecide`, `MTTC`, `MTTR`, alerts without action, failed/partial containment, recurrence, quarantines/reactivations, false-containment impact and missing correlation), trade-offs, limitations, antipatterns and implementation mappings are all retained. The pattern requires external-capable identity/tool/connector controls and forbids treating dashboards, an in-agent kill switch or automatic reactivation as sufficient.

The target is `ai-agent-governance-framework-next/toolkit/patterns/runtime-observability-and-quarantine.md`, using `move-and-relink-as-vendor-neutral-runtime-pattern`. Related links must be rebuilt. This is guidance/pattern content, not adopted policy, proof of operation or vendor implementation. It depends on runtime registry/status, identity, gateway/connector controls, evidence records, owners/authorities and optional SIEM/SOAR, IAM, gateway, rollback and service-mesh mappings.

### `templates/governance-forum-tor.md`

This reusable Terms of Reference template defines forum identification, decision rights, decisions outside scope, composition, quorum/voting/substitution, cadence and agenda, evidence gate, decision record, escalation, metrics and terms review. It preserves the explicit rule that a forum without decision rights becomes a status meeting, and that a forum that cannot decide without external approval must declare itself consultative. It preserves possible decision states `approve`, `condition`, `hold` and `reject`, the minimum decision-record fields, and the rule that an item without complete evidence does not enter the agenda.

The canonical destination is `ai-agent-governance-framework-next/toolkit/templates/governance-forum-tor.md`, using `move-and-relink-as-reusable-human-governance-template`. A separate, neutral instantiation may be created at `ai-agent-governance-implementation-template/governance/forum-terms-of-reference.md`, using `instantiate-with-local-authority-members-evidence-and-review-cycle`. Placeholders must not be interpreted as real authority, quorum, members, decisions or organizational adoption. Operating-model authorities, evidence references, decision-gate contract, exception/condition records and review calendar remain dependencies.

### `templates/attestation-sunset-record.md`

This maintained annual lifecycle record preserves front matter, lifecycle-stage and operational-state enums, identification fields, nine attestation checks, five disposition values, eight conditional sunset-execution actions, a transition record and the final gaps field. It distinguishes revalidation from automatic approval extension and requires evidence for owner, purpose, tier/admissibility, exceptions/conditions, identities/scopes, model/source/tool bindings, control evidence, cost/use/outcome and incidents/findings.

The target is `ai-agent-governance-framework-next/toolkit/templates/attestation-sunset-record.md`, using `move-and-relink-as-lifecycle-attestation-and-retirement-template`. A separate implementation record may be instantiated at `ai-agent-governance-implementation-template/lifecycle/attestation-sunset-record.md`, using `instantiate-with-agent-evidence-authority-and-execution-records`. Empty fields and `unknown`/`N/A` outcomes are not evidence of passing. Sunset actions must preserve identity/secrets/token revocation, binding removal, budget/infrastructure closure, evidence retention, notification, registry updates and archive timing. `supersedes: null` is preserved; no supersession is declared.

### `docs/architecture/quality-attributes.md`

This review-stage, observed-maturity declaration preserves ten quality attributes: Auditability, Observability, Remediability, Accountability, Interoperability, Security and privacy, Reliability, Usability, Evolvability and Measurability. It must remain a set of architecture/quality criteria, not a certification or claim that an implementation already satisfies them. The source supplies no numeric thresholds, organizational authorities beyond the listed owner `rodgui`, or implementation evidence.

The target is `ai-agent-governance-framework-next/docs/framework/06-architecture-and-technical-controls.md`, integrated under `06.1 Architecture principles and quality attributes` with `integrate-as-quality-attributes-section-preserving-review-and-observed-status`. Preserve `status: review`, `maturity: observed`, `last_reviewed: 2026-08-09`, `review_cycle: 180d`, owner and tags as provenance/metadata. Do not promote the content to stable, validated or adopted without new evidence. Its verification depends on architecture, registry, evidence, policy controls, identity, data, model/tool inventory, risk matrix, baselines and risk-proportional SLAs.

### `templates/sunset-plan.md`

This historical `Appendix D` text is a controlled-decommissioning procedure with triggers for missing owners/catalog entry/logs, inactivity, duplication/replacement, platform disapproval and severe unremediated incidents. It preserves the three illustrative phases: Warning D0, Quarantine D+15 and Deactivate D+30, including owner notification, remediation deadline, write-action/scope/user restrictions, evidence/log retention, access/integration/identity removal, Catalog recording and optional configuration archive. Mandatory items are sunset date/reason/owner, migration plan when applicable, communication evidence and risk-based log retention.

The canonical destination is `ai-agent-governance-framework-next/toolkit/templates/sunset-plan.md`, using `preserve-as-controlled-decommissioning-template-with-calibration-caveat`. A local instantiation may be created at `ai-agent-governance-implementation-template/lifecycle/sunset-plan.md`, using `instantiate-with-local-deadlines-owners-and-evidence`. The values 90, 15, 30 and X days are examples, not universal SLAs. The plan does not itself define authority, quorum, evidence schema or success criteria; it must remain linked to registry, lifecycle, attestation/sunset record, identity/access, evidence retention, migration and rollback records.

### `requirements-docs.txt`

This file contains exactly three documentation-build pins, in order: `mkdocs==1.6.1`, `mkdocs-material==9.7.7` and `pymdown-extensions==11.0.1`. The target is `ai-agent-governance-framework-next/requirements-docs.txt`, preserving the pins with `preserve-pinned-documentation-build-dependencies`. They belong to a documentation build environment, not runtime, policy or agent operational controls. The pins do not prove installation, compatibility or a successful build; any change requires review against MkDocs configuration, Markdown corpus and build output.

### Four `.gitkeep` placeholders

`assessments/risk-assessments/.gitkeep`, `docs/auditability/.gitkeep`, `docs/responsible-ai/.gitkeep` and `schemas/.gitkeep` are byte-identical one-line HTML comments (`<!-- .gitkeep -->`). They are exact-content duplicates but not substantive duplicate documents: each preserves a different source-directory existence marker. Their records are intentionally `non-substantive` with explicit justifications. They should be omitted or archived after the target contains real assessment, auditability, responsible-AI or schema artifacts; copying the comments would create noise and could falsely imply substantive coverage.

## Cross-file dependencies and boundaries

- `references/sources.md` supplies the source ledger for the standards, frameworks, regulation, threat references and institutional reports used by other research and mapping artifacts. Its external URLs and temporal cutoffs are dependencies, not embedded evidence.
- `schemas/model-provider-catalog.schema.json` governs future provider/model catalog instances and depends on a compatible Draft 2020-12 validator. It is a contract dependency of any catalog entry, blueprint or release artifact that references provider/model approval.
- `runtime-observability-and-quarantine.md` depends on registry/status, identity, tool/connector gateway, evidence, incident, remediation and regression control planes. It is the operational pattern that connects signals to lifecycle and evidence actions.
- `governance-forum-tor.md` depends on the operating model and named authorities. Its decision records consume evidence references, tiers, scopes, conditions, expiry and review calendars.
- `attestation-sunset-record.md` depends on agent registry, blueprint/release version, model/source/tool catalogs, control/evidence records, lifecycle state machine, retention policy and `sunset-plan.md`.
- `quality-attributes.md` depends on the architecture principles and the same registry/evidence/policy/identity/data/model/tool/risk surfaces that make the attributes testable.
- `sunset-plan.md` depends on agent Catalog/registry, Business and Technical Owners, Run Authority, identity/access/integrations, logs/telemetry, evidence retention, migration/replacement and rollback records, and the attestation/sunset record.
- `requirements-docs.txt` depends on the target MkDocs configuration, documentation corpus and a package source capable of providing the exact pins.

These dependencies are relationships, not proof that the dependent systems, authorities, evidence or builds already exist.

## Exact duplication, semantic near-duplicates, and boundaries

There are no duplicate substantive records or IDs in this manifest. The four `.gitkeep` files have identical bytes by design, but their directory markers remain path-specific and non-substantive.

The following semantic near-duplicates are intentional and must not be collapsed:

1. **Runtime pattern vs. attestation/sunset record vs. sunset plan.** The pattern defines signal-to-containment operations and reactivation logic; the attestation record captures revalidation, disposition, sunset execution and lifecycle transition evidence; the sunset plan provides the temporal decommissioning procedure. They are complementary, not interchangeable.
2. **Runtime pattern vs. quality attributes.** Observability and remediability appear in both, but the quality document states broad architecture criteria while the pattern provides an executable, vendor-neutral runtime structure with evidence and metrics.
3. **Governance forum vs. attestation record.** Both include authority, decision state, evidence, expiry and review, but the forum template establishes a human decision forum and its terms; the attestation record governs an agent/release lifecycle revalidation and decommissioning event.
4. **Attestation record vs. sunset plan.** The record contains checks, disposition and transition evidence; the plan contains triggers and phase actions. The record must not be replaced by the plan.
5. **Sources ledger vs. framework mappings or evidence.** A listed reference and its intended use do not prove a claim, a control implementation, certification, causal benefit or compliance.
6. **Requirements pins vs. governance requirements.** The three package pins control documentation-build reproducibility only; they are not operational governance controls.

## Contradictions, source caveats, and unresolved gaps

No material contradiction was found among the eight substantive files. Variations are intentional scope or lifecycle distinctions. The following caveats and migration findings remain explicit:

- The source ledger contains temporal access dates and evolving MITRE/OWASP references. Downstream claims must preserve date/version/evidence cutoffs and be revalidated.
- ISO entries point to official pages and do not reproduce protected standards. No control-to-control mapping is asserted.
- Microsoft Customer Zero material is institutional reporting, not independent audit or causal evidence.
- The model/provider schema `$id` identifies the source GitHub path. A target identity change requires an explicit compatibility decision.
- The runtime pattern's front matter declares `status: maintained`, but the content remains a pattern/guidance artifact and must not be presented as policy adoption or proof of an operating implementation.
- The governance forum, attestation record and implementation-template destinations contain placeholders by design. Empty values, `unknown`, `N/A`, or example decision states must not be interpreted as completed decisions or evidence.
- The quality attributes document is `status: review` and `maturity: observed`; it provides no numeric thresholds or implementation evidence.
- The sunset-plan timing examples (`90`, `15`, `30`, `X`) require calibration to risk and organization. They must not be silently converted to universal defaults.
- `requirements-docs.txt` pins do not prove a build was run or passed.
- The four `.gitkeep` files contain no substantive auditability, responsible-AI, risk-assessment or schema content. Their omission after real target artifacts exist is intentional.

No decision-required item or blocked path was created by this batch. The schema `$id` compatibility issue and internal-link/path relinking are target migration decisions to preserve explicitly, not reasons to fabricate a source correction or mark the source path blocked.

## Destination and transformation register

| Source path | Primary target | Transformation | Preservation decision |
|---|---|---|---|
| `references/sources.md` | `ai-agent-governance-framework-next/research/sources/bibliography.md` | move/relink as source ledger | Preserve 19 IDs, URLs, dates, uses, hierarchy and limitations. |
| `schemas/model-provider-catalog.schema.json` | `ai-agent-governance-framework-next/schemas/model-provider-catalog.schema.json` | preserve schema verbatim with Draft 2020-12 validation | Preserve `$schema`, `$id`, constraints, enums, references and conditional rules; record any identity change as compatibility decision. |
| `docs/patterns/runtime-observability-and-quarantine.md` | `ai-agent-governance-framework-next/toolkit/patterns/runtime-observability-and-quarantine.md` | move/relink vendor-neutral pattern | Preserve front matter, Mermaid flow, operational chain, controls, evidence, metrics, antipatterns and guidance boundary. |
| `templates/governance-forum-tor.md` | `ai-agent-governance-framework-next/toolkit/templates/governance-forum-tor.md` | move/relink reusable template | Preserve all fields and guardrails; do not infer authority from placeholders. |
| `templates/governance-forum-tor.md` | `ai-agent-governance-implementation-template/governance/forum-terms-of-reference.md` | instantiate with local authority/evidence | Create only a filled local record; keep canonical template separate. |
| `templates/attestation-sunset-record.md` | `ai-agent-governance-framework-next/toolkit/templates/attestation-sunset-record.md` | move/relink lifecycle template | Preserve enums, checks, outcomes, dispositions, actions, transition record and gaps. |
| `templates/attestation-sunset-record.md` | `ai-agent-governance-implementation-template/lifecycle/attestation-sunset-record.md` | instantiate with local records | Do not treat empty or unknown fields as passed evidence. |
| `docs/architecture/quality-attributes.md` | `ai-agent-governance-framework-next/docs/framework/06-architecture-and-technical-controls.md` | integrate under quality-attributes section | Preserve review/observed metadata and criteria without promoting maturity. |
| `templates/sunset-plan.md` | `ai-agent-governance-framework-next/toolkit/templates/sunset-plan.md` | preserve controlled-decommissioning template | Preserve Appendix D context and calibrate illustrative timing. |
| `templates/sunset-plan.md` | `ai-agent-governance-implementation-template/lifecycle/sunset-plan.md` | instantiate with local deadlines/owners/evidence | Supply local authority, evidence, migration and retention decisions. |
| `requirements-docs.txt` | `ai-agent-governance-framework-next/requirements-docs.txt` | preserve pinned build dependencies | Keep build-only scope and exact versions. |
| four `.gitkeep` paths | target directories only as needed | omit after real artifacts exist | Record placeholders for manifest completeness; do not copy empty comments as substantive content. |

No content in this batch is assigned to the consulting repository. The governance templates may seed a neutral implementation-template repository, but they do not contain commercial packaging or consulting-only material.

## Generation and independent validation evidence

Generator command, run from the control directory:

```text
python3 generate_curated_microbatch_records.py micro-01b-curation.json
```

Generator result:

```json
{
  "batch": "micro-01b",
  "expected_paths": 12,
  "file_records": 12,
  "markdown_headings_expected": 51,
  "heading_rows": 51,
  "files_sha256": "fb6aaf304be9a4f796b3417c50d72a61d2191a4d1f07ca289fcd13ed52835545",
  "headings_sha256": "ae774a8cb233ec0e33de588cc449f6d3ed6d2593b60f8d7a56ab263e7539ac6d"
}
```

Required outputs are present in the control directory:

- `micro-01b-curation.json`
- `micro-01b-files.jsonl`
- `micro-01b-headings.csv`
- `micro-01b-relationships.md`
- `micro-01b-validation.json` (written by the validator)

The independent validator was then run as required:

```text
python3 validate_microbatch_output.py micro-01b
```

Validation result:

```json
{
  "batch": "micro-01b",
  "expected_files": 12,
  "file_records": 12,
  "expected_headings": 51,
  "heading_rows": 51,
  "non_substantive_records": 4,
  "errors": [],
  "error_count": 0,
  "files_sha256": "fb6aaf304be9a4f796b3417c50d72a61d2191a4d1f07ca289fcd13ed52835545",
  "headings_sha256": "ae774a8cb233ec0e33de588cc449f6d3ed6d2593b60f8d7a56ab263e7539ac6d"
}
```

The validator confirmed source SHA-256, byte and line counts for every generated record, manifest path order, required record-level invariants, full-read flags, candidate destinations, heading identity/order, exact heading subtree content and non-invalid preservation statuses. The JSON record output preserves the complete flattened structured content for the assigned JSON Schema.

## Completion counts

Expected paths: 12
File records: 12
Markdown headings expected from `mechanical-heading-index.csv`: 51
Heading rows produced: 51
Blocked paths: 0
Decision-required items: 0

# micro-01c

# Microbatch 01c migration relationships

Source snapshot: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot`  
Commit: `5545d9227624400ab8bb707b6032b2f61329a36e`  
Reader: `main:gpt-5.6-sol:micro-01c:2026-08-11`

## Coverage

- 8 paths read completely.
- 8 auditable file records generated.
- 27/27 Markdown headings reconciled exactly.
- 0 non-substantive paths.
- 0 validation errors, blocked paths or decision-required headings.
- Validation evidence: `micro-01c-validation.json`.

## Fictitious T3 benefits-eligibility case

The Registry and Blueprint records form one fictitious Governance Contract 2.0 case bundle. They must remain linked to the release manifest and supporting catalogs/evidence, but never be presented as a real deployment or organizational authorization.

Preserved relations:

- stable agent ID `benefits-eligibility-triage` and blueprint version `1.0`;
- T3 risk and `conditional` admissibility as separate dimensions;
- business, technical and run ownership;
- production/enabled source fixture lifecycle plus transition authority and evidence;
- human decision authority, contestability and slice re-evaluation as continuing conditions;
- primary model pin `2026-07-20`, evaluated catalog binding and fail-closed fallback;
- confidential source binding, pre-retrieval authorization and no sensitive session memory;
- hybrid workload identity with short-lived token and no agent break-glass privilege;
- state-changing but reversible recommendation writer with mandatory human approval, gateway and kill-switch references;
- all nine source control IDs, prohibited uses, material-change triggers, support/SLO and evidence references;
- discovery/attestation dates and source signals.

A concrete source inconsistency was recorded rather than silently fixed: the eligibility recommendation tool uses `killSwitchRef: example-kill-switch/knowledge-search`. The source value remains in provenance; the new fictitious example must either correct it to a capability-consistent reference or document why the shared switch name is intentional.

The case migrates to framework examples and seeds only fictitious material in the implementation-template repository.

## Agent-or-not gate

The architectural decision precedes platform selection. The target preserves:

1. whether language interpretation, variable context, planning or dynamic tool selection is genuinely necessary;
2. content-only versus action-producing behavior;
3. reversibility/materiality;
4. classified-data access and source certification;
5. user-present versus autonomous identity model;
6. classification of every API/tool/MCP action independently from agent tier;
7. impact on people, rights, opportunities, safety, regulated processes or public communication;
8. the enforcement and evidence location for every control.

A deterministic workflow, traditional automation or API remains the preferred mechanism for stable, fully specified processes. A decision not to use an agent is retained as a valid portfolio/architecture decision. Prompt text is never treated as enforcement.

## Source quality-gate workflow

The source workflow is retained as executable provenance and adapted only after local parity in the framework target. It covers:

- read-only checkout with full history;
- Python 3.12 and locked CI requirements;
- robust base-commit resolution;
- changed-Markdown linting;
- repository validation and validator unit tests;
- Ruff and Python compilation;
- deterministic regeneration and pixel comparison of both 1800×2400 visuals;
- whitespace errors;
- strict documentation build.

This is a build/quality contract, not publication authority. Gate 1 creates no remote and performs no GitHub-hosted publication.

## Minimal control-catalog example

`examples/control-catalog.example.json` preserves two complete controls—`AGF-REG-001` and `AGF-OPS-001`—against schema 2.0/catalog 1.2.0. It remains a minimal schema fixture and cannot replace or be counted as the complete 44-control canonical catalog.

## Commercial proposal boundary

`consulting/templates/consulting-proposal-template.md` migrates only to `ai-agent-governance-consulting` and references a pinned framework release. All fourteen sections are preserved:

- context;
- outcomes;
- scope;
- assumptions/prerequisites;
- approach;
- phases/gates;
- deliverables;
- roles;
- indicative timeline;
- risks;
- engagement metrics;
- confidentiality/IP/security;
- limitations;
- next steps.

It retains the prohibitions on guaranteed compliance, zero incidents, unsupported ROI and ungrounded dates. Secrets appear only as `[REDACTED]`; conclusions are limited by scope and evidence cutoff; workshop/page counts are not primary success metrics.

## Reference and tooling indexes

The reference index is relinked while preserving the authority boundary: technical-reference material describes terms and structures, while organizational requirements become adopted only through an applicable release and explicit approval.

The tools index preserves:

- deterministic output for unchanged input;
- explicit errors and no silent approval;
- no secrets, external telemetry or personal paths;
- cross-platform behavior when viable;
- documented commands/dependencies;
- identical local and CI entry points;
- no speculative directory/category before a real artifact exists.

# micro-02

# micro-02a

# Microbatch 02a migration relationships

Source snapshot: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot`  
Commit: `5545d9227624400ab8bb707b6032b2f61329a36e`  
Manifest: `control/micro-02a.txt`  
Reader: `subagent:gpt-5.6-luna:micro-02a`  
Assigned path: `tools/scripts/validate-repository.py`

## Reading and preservation method

The assigned Python file was read completely from line 1 through line 1444 with `read_file`, not inferred from headings or metadata. Source measurements are **65,215 bytes**, **1,444 lines**, SHA-256 **`c58fd3bdfbb111ea87ce25573b296e06217377c45afdffec90858e5752aa3f44`**. The snapshot resolved to the required commit before reading. AST inspection confirmed 19 top-level configuration assignments, the immutable `Issue` dataclass, 31 functions, and the `__main__` exit path. The assigned path has no Markdown headings in `mechanical-heading-index.csv`; therefore no heading subtree can be substituted for the full semantic read.

The generated JSONL preserves the complete Python source and top-level AST units. The curation adds the rule inventory, dependencies, source status, target candidates, negative guardrails, and migration notes. The candidate implementation remains under `ai-agent-governance-framework-next/tools`; tests and a provenance ledger are separate candidate destinations so parity is verifiable without modifying either repository.

## Structural and dependency relationships

1. **Root and source layout.** `ROOT = Path(__file__).resolve().parents[2]`; moving the file or changing the target layout changes every relative path. `relative()` emits a repository-relative POSIX path when possible, otherwise the path string. This is coupled to the target's directory depth and must be tested after migration.
2. **Deterministic discovery.** `repository_files()` walks the whole root, removes `.git`, `.venv`, `venv`, `dist`, `site`, `site_src`, `__pycache__`, `.pytest_cache` and `.ruff_cache`, and sorts both directories and filenames. Markdown, JSON and general text scans consume this deterministic inventory.
3. **Front matter and related paths.** `validate_frontmatter()` calls the deliberately limited `parse_frontmatter()` parser for every Markdown file, but enforces metadata only for the exact canonical/domain README paths, `docs/patterns/`, non-README ADRs, and the named spec subtree. `validate_frontmatter_related_paths()` parses only a `related:` block and checks local targets with exact filesystem case.
4. **Markdown link/citation chain.** `validate_markdown_links()` depends on `INLINE_LINK_RE`, `extract_link_target()`, `unquote()`, `has_exact_case()` and the root filesystem. `validate_citations()` treats the final `## Sources` marker as the source block and compares numeric body citations with numeric citations listed after it.
5. **JSON/schema chain.** `validate_json_and_schemas()` parses all JSON files, requires `jsonschema` at runtime, validates the ten fixed schema/instance pairs (registry, blueprint, control catalog twice, maturity, model, source, tool, release and audit), and then adds role/schema pairs discovered for nested cases. It uses Draft 2020-12 plus `FormatChecker`.
6. **Case bundle roles.** `CASE_ROLE_FILES` binds role names to `registry.json`, `blueprint.json`, `release-manifest.json`, `model-catalog.json`, `source-catalog.json`, `tool-catalog.json` and `audit-event.json`. `CASE_ROLE_SCHEMAS` binds those roles to their schemas. The historical flat `examples/` bundle is always seeded; `examples/cases/<case-id>/` bundles are discovered by convention from parsed JSON paths.
7. **Shared catalog inheritance.** Nested cases inherit the flat model, source and tool catalogs when those shared paths are present; a case-local file with the corresponding role replaces it. This is intentional coverage preservation, not optional decoration.
8. **Cross-record identity and release dependencies.** Registry/Blueprint must agree on agent ID, current blueprint path, version, risk tier and admissibility. Release-relevant registries are those at stages `approved`, `production`, or `retirement-review`, or those with a production platform; they then require evidence links and temporally valid attestation.
9. **Catalog binding dependencies.** Blueprint model, source and tool entries bind to catalog IDs and are checked for status, copied fields, allowed data classes/regions/scopes, approval modes, risk tiers and review/expiry dates. Approved-alternative model fallbacks and audit-event tools also require known catalog IDs.
10. **Control/release/evidence graph.** Blueprint governance control IDs, release-manifest control evidence IDs and catalog control IDs must resolve to `controls/control-catalog.json`. Existing artifact hashes in the release manifest are recomputed with SHA-256. Release manifest fields must agree with Blueprint; audit events must agree with Blueprint and the tool catalog.
11. **Assessment dependency.** `examples/maturity-assessment.example.json` is checked for duplicate evidence IDs, unknown dimension evidence references, assessor/reviewer separation and sample population bounds. Its valid copy is also the fixture for invariant guardrails.
12. **Asset and policy dependencies.** `validate_assets()` requires two PNGs at fixed paths and fixed dimensions; `validate_policy_integrity()` reads the historical Policy v1 path and compares the hard-coded digest `cdd8c232019a4b388ebb71d7f1dd82f3c568d039d416beab1838ee59f4047140`.
13. **Taxonomy and control dependencies.** Three schema trails must expose exactly `T1`, `T2`, `T3`, `T4`; every control's `appliesToTiers` must use only those values. The control catalog additionally needs unique IDs, at least 30 controls and at least 10 domains.
14. **Boundary dependencies.** Commercial validation reads `consulting/consulting-engagement-model.md` and `consulting/README.md` and rejects two legacy paths. Vendor neutrality scans Markdown/JSON/YAML/TOML with separate regexes and allowlists. Policy-history validation scans only Markdown under `templates/`.
15. **Required structure and sensitive-content dependencies.** `validate_required_paths()` requires the listed framework docs, schemas, examples, templates, consulting paths and DejaVu font assets. `validate_sensitive_content()` scans `.md`, `.py`, `.json`, `.yml`, `.yaml`, `.toml` and `.txt` for private keys, AWS keys, GitHub tokens, OpenAI-style keys, the hard-coded personal macOS path and `# Readme` placeholders.
16. **Runtime dependency.** Python standard library imports are `copy`, `hashlib`, `json`, `os`, `re`, `struct`, `dataclasses.dataclass`, `pathlib.Path`, `typing.Any` and `urllib.parse.unquote`. Complete schema validation requires `jsonschema>=4.22,<5`; the source does not install or pin it itself.

## Complete rule inventory

### Discovery, metadata and links

- Required Markdown front matter has closing `---`, `title`, `status` in `ALLOWED_STATUSES`, and ISO-like `last_reviewed` matching `YYYY-MM-DD`.
- Related front-matter references accept list items or key/value entries, stop at the next unindented field, ignore `null`/`[]`/`{}`, and reject missing or incorrectly cased local targets.
- Markdown links and images are found by `INLINE_LINK_RE`; angle-bracket targets and the first whitespace-separated target token are supported. HTTP(S), mailto, tel, data and fragment-only links are skipped. Other targets are URL-decoded, stripped of query/fragment, normalized, kept inside ROOT, required to exist and required to match case.
- Numeric citations not preceded by `!` are compared against the final `## Sources` block. Missing source entries become Issues.
- JSON references are checked only when the whole string matches `REPOSITORY_REF_RE`, which permits repository paths ending in `.md`, `.json`, `.yaml`, `.yml` or `.png` with an optional fragment. Traversal, missing paths and case mismatches are reported.

### JSON, schema and cross-record validation

- JSON parse failures are recorded with the decoder/Unicode message.
- Fixed schema pairs cover Registry, Blueprint, control catalog example and live catalog, maturity assessment, model catalog, certified source catalog, enterprise tool registry, release evidence manifest and audit event.
- Each discovered case gets role-specific schema validation without duplicate schema/instance pairs. Schema errors are sorted by instance path and report `$` for root errors.
- Invalid schema instances are excluded from cross-record validation, but parse/schema Issues remain in the result.
- Registry/Blueprint identity, path, version, risk tier and admissibility must match.
- Release-relevant registry records need `evidenceLinks`; `attestedAt > expiresAt` and `expiresAt < lastReviewed` are errors when the values are strings.
- Model, source and tool catalog IDs must exist; catalog status, copied fields, subset constraints, allowed regions/scopes, approval modes, risk tiers and expiry/review dates are enforced separately for each binding type.
- Blueprint fallback mode `approved-alternative` requires a known model catalog entry.
- Blueprint `governance.controlIds` and release manifest `controlEvidence.controlId` values must be known control IDs. Existing manifest artifact files must hash to the declared SHA-256.
- Release manifest agent/version/risk/admissibility must match Blueprint; audit event agent/version and tool catalog entry must match known records.
- Maturity evidence IDs must be unique, all dimension refs must be known, assessor and reviewer cannot have identical name and organization, and sample size cannot exceed population.

### Schema-negative guardrails

The validator deliberately mutates valid fixtures and requires each mutation to fail schema validation:

- Registry without `attestation`, without `evidenceLinks`, or without lifecycle `transitionHistory`.
- Registry with discovery `status: high`, ensuring discovery status is not collapsed into confidence grading.
- Production Blueprint without `governance.releaseEvidenceRef`, with empty release evidence and assessment refs, or with a model missing `modelVersion`, `catalogEntryId` or `evaluationRef`.
- Blueprint source/tool bindings without `catalogEntryId`.
- Restricted admissibility without `exceptionRef` and `exceptionExpiresAt`.
- Prohibited production Blueprint.
- A `create` tool marked `stateChanging: false`.
- Irreversible automated state-changing `delete` tool.
- T4 irreversible state-changing tool with empty `gatewayRef`, `killSwitchRef` and `scopes`.
- Maturity assessment without reviewer disposition.

Additional invariant guardrails require rejection of an unknown evidence ref, assessor/reviewer identity reuse, sample size greater than population, and an expired active attestation. A JSON reference `../outside.md#section` must be rejected as a repository escape. Control-catalog duplicate IDs, fewer than 30 controls, fewer than 10 domains and unknown Blueprint control IDs are also explicit checks.

### Assets, history, taxonomy, boundaries and output

- PNG parsing requires the exact PNG signature, an IHDR chunk with length at least eight bytes, and returns big-endian width/height; both required images must be exactly 1800x2400. An old ambiguous vendor-specific visual is forbidden if present.
- Policy v1 integrity is a fixed SHA-256 check. Legacy commercial artifacts must not remain outside `consulting/`.
- Commercial structure requires exactly nine ordered `## Oferta N — ...` sections and exactly three ordered package rows, with each offer title occurring once in package module cells.
- Markdown prose tier rows cannot use `baixo`, `moderado`, `alto` or `crítico` in the first cell, except the historical Policy v1 path. The helper intentionally permits those words in later cells.
- Vendor neutrality allows only the listed prefixes (`assessments/`, ADRs, `docs/explanations/`, `references/`, `specs/`) and allowlisted files; one exact workflow image literal is masked before scanning. Markdown and structured files use different vendor regexes.
- Templates must not contain any of the three legacy Policy v1 template names.
- Sensitive-content patterns detect private keys, AWS access keys, GitHub tokens, OpenAI-style keys, `/Users/rodgui`, and the exact `# Readme\n` placeholder.
- The main function runs all gates, accumulates rather than short-circuits Issues, prints sorted `FAIL: N issue(s)` with `[category] path: message` and returns 1 on any Issue. Zero Issues produces `PASS: repository validation (...)` with Markdown, JSON, control and domain counts and returns 0.

## Duplication, overlaps and contradictions

1. There is no second assigned source file, so no exact file-to-file duplicate can be established in this microbatch.
2. JSON Schema validation and custom cross-record checks intentionally overlap: schema catches shape/required/conditional violations, while `validate_case_bundle()` catches relationships and catalog bindings. Target tests must prove both layers remain active.
3. Control ID checking appears in nested bundle validation, release-manifest validation, and the final control-catalog check. These are overlapping defense-in-depth checks, not license to remove any one of them.
4. Path validation is split among front-matter related paths, Markdown links and JSON references. They have different external-link exceptions and different escape reporting; they must not be merged into one looser helper.
5. `ALLOWED_STATUSES` is a Python allowlist while schemas and records have their own status contracts. Migration must reconcile these intentionally rather than assume the Python set is the sole authority.
6. `validate_json_and_schemas()` returns early from its internal schema phase when `jsonschema` is unavailable. The main function still executes later top-level gates, but cross-record and schema guardrails are skipped; a target must expose this as a dependency failure, not a green result.
7. The flat examples bundle is always discovered even when some role files are absent, while schema pairs silently skip missing instances. This preserves compatibility but creates a completeness gap unless required paths or tests are expanded.

## Gaps and unfinished material

- `validate_required_paths()` does not list every fixed schema/instance pair: in particular, the historical Registry, Blueprint, control-catalog example and maturity-assessment example are used by validation/guardrails but are not all independently required by that list. Missing instances can therefore be skipped by pair validation.
- `REPOSITORY_REF_RE` excludes `.py`, `.toml` and `.txt`; JSON references to those file types are not checked by `validate_json_references()`.
- Artifact hashes are checked only when the declared target is an existing file. A missing artifact path is not itself reported by that routine.
- `validate_policy_integrity()` reads the policy path without an existence guard; a missing policy can raise `FileNotFoundError` instead of becoming a structured Issue.
- `parse_frontmatter()` is intentionally not a YAML parser: nested/indented metadata, quoting edge cases and multiline values are ignored. A target with richer front matter needs compatibility tests before changing behavior.
- Vendor scanning is pattern-based and can produce false positives; it does not parse structured formats or provide an approved per-file rationale beyond the allowlists.
- Sensitive-content detection reports possible matches but has no secret-baseline, entropy, suppression or remediation workflow. The hard-coded `/Users/rodgui` pattern is not portable.
- The validator checks dimensions and PNG headers but not image content, accessibility text, provenance or diagram semantic correctness.
- `validate_control_scope()` only rejects `scope == organization` with `blocking is True`; it does not define all valid scope/blocking combinations.
- `validate_cross_record_invariants()` skips non-dict/non-list/missing fields and relies on schemas for shape. Running it alone is not a complete validation contract.
- `jsonschema` is named in an error message but is not pinned in this file or environment; target packaging and CI must make the version explicit.
- The main output is human-readable stdout only. There is no machine-readable Issue artifact, exit-code taxonomy or evidence package generated by this validator.

## Migration hazards and required decisions

1. **Root relocation.** Moving from `tools/scripts/` changes `parents[2]`; preserve the intended target root with a test that executes the migrated path from different working directories.
2. **Path and schema IDs.** Every fixed source path, schema pair, case role, required path, asset and consulting boundary must be reconciled with the target layout. If `$id` or schema versions change, document compatibility aliases and validate both old/new references during migration.
3. **Fixture parity.** The negative guardrails mutate named source fixtures. Any target fixture rewrite must preserve the same semantic fields or replace each mutation with an equivalent test; deleting a fixture must not delete its guardrail.
4. **Cross-record convention.** New nested cases must continue to be discovered automatically. Do not replace convention discovery with a hard-coded case list.
5. **Shared catalog semantics.** Keep catalog inheritance and local override behavior explicit; otherwise a new case can appear to validate while silently losing model/source/tool bindings.
6. **Historical policy hash.** The source hash is a provenance contract, not a target release hash. The target must decide whether to archive the source artifact unchanged, map it to a new history path, or establish a new immutable digest; it must not silently update the expected digest.
7. **Vendor-neutral boundary.** Adapt allowlists only after deciding where cases, mappings and explanations live. Broadening the allowlist can hide vendor leakage; narrowing it can reject intended evidence.
8. **Personal path portability.** Replace or parameterize `/Users/rodgui` in the target while retaining a regression test for personal-path leakage; do not simply remove the rule.
9. **Dependency availability.** CI and local tooling must install a compatible jsonschema version and test the missing-dependency path. A skipped schema phase cannot be treated as PASS.
10. **Required-path completeness.** Expand or explicitly justify required paths for every fixed schema/instance pair and every artifact referenced by manifests before the target claims complete validation.
11. **Output provenance.** Preserve source commit, hash, byte/line measurements, rule-to-source lines, and migration differences in the target provenance ledger. Do not claim Git history continuity between independent repositories.
12. **No source-side action.** This record was produced without writing to the immutable snapshot or protected original, without creating a target repository/remote, and without publishing.

## Candidate target boundaries

- **Framework implementation:** `ai-agent-governance-framework-next/tools/scripts/validate-repository.py`, adapted only for approved target paths/contracts and retaining every source rule.
- **Rule-level tests:** `ai-agent-governance-framework-next/tools/tests/test_validate_repository.py`, with valid fixtures plus every schema/invariant/path/boundary/sensitive-content negative case.
- **Provenance:** `ai-agent-governance-framework-next/tools/provenance/validate-repository-rules.md`, recording source measurements, function/rule inventory, dependencies, target path changes, exceptions, gaps and test mapping.
- **Consulting:** none. This is framework tooling and validation infrastructure, not commercial packaging.
- **Blocked content:** none for this microbatch. No destination is marked `decision-required`; material target choices remain migration hazards but do not prevent this lossless audit record.

## Completion counts

- Expected paths: **1**
- File records: **1**
- Markdown headings expected: **0**
- Heading rows produced: **0**
- Non-substantive paths: **0**
- Blocked paths: **0**
- Decision-required items: **0**

# micro-02b

# Microbatch 02b migration relationships

Source snapshot: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot`  
Commit: `5545d9227624400ab8bb707b6032b2f61329a36e`  
Reader: semantic recovery consolidated from the validated `micro-02b` file and heading records and a complete parent reread on 2026-08-11

## Coverage and validation

- 9/9 source paths read completely.
- 9/9 file records generated.
- 62/62 Markdown ATX headings reconciled exactly.
- 0 non-substantive records.
- 0 blocked paths.
- 0 decision-required migration gaps.
- Revalidation: `python3 validate_microbatch_output.py micro-02b` returned exit code 0.
- The source snapshot and protected checkout were not modified.

## Benefits Eligibility Triage case

`docs/explanations/cases/benefits-eligibility-triage.md` is a fictitious and sanitized T3 reference case. It must remain visibly non-production and cannot be cited as effectiveness evidence, risk acceptance, a recommended threshold or proof that controls work against a real estate.

Relations that must survive migration:

1. **Technical simplicity does not determine risk tier.** The employment/credit/eligibility/service-access impact escalator imposes at least T3 and a formal impact assessment even though the design has only one source, one tool and one model.
2. **Risk tier and admissibility are independent.** T3 expresses potential impact severity; `conditional` expresses whether and under which conditions the design may operate. Satisfying conditions does not lower T3. Losing a condition suspends use.
3. **Human decision is a control.** The agent gathers the current rule and drafts a recommendation; the analyst decides. Residual risk was assessed as moderate with that human decision control, not despite it.
4. **Responsible AI has veto authority at G5 for T3.** The source records an RAI decision before Design Authority approval. The order and both authorities must remain traceable.
5. **Five conditions are executable and consequential:** human decision token before write, contestation channel and response-time sampling, per-version slice evaluation, protected attribute/proxy exclusion from decision and logs, and automatic quarantine when any condition is lost.
6. **Operation requires a degradation path.** Gateway write denial plus manual triage is the declared fallback. A system that can only be switched off is not fully containable.
7. **Behavioral change can be material without configuration change.** Eligibility-rule changes and material disparities between slices trigger reassessment.
8. **The source case exposed a real validation defect:** the non-existent control `AGF-HUM-001` had been invented by analogy and crossed the gate because blueprint `governance.controlIds` were not checked against the catalog. The validated replacement is `AGF-RAI-002`, and unknown blueprint control IDs must fail closed.

The cross-case comparison remains useful as historical demonstration of proportionality:

- T1 meeting notes: `permitted`, automated gate, no transaction approval, four blueprint controls, annual attestation;
- T2 service desk: `permitted`, Design Authority, automated action approval, six controls, four release conditions, six-month attestation;
- T3 eligibility: `conditional`, Design Authority plus RAI veto, human approval per transaction, nine controls, five conditions with automatic suspension, six-month attestation.

This table is not a universal numerical prescription. The durable principle is that rigor grows with impact and context rather than technical complexity alone.

## Self-sufficiency versus documentation completeness

`docs/reference/self-sufficiency-checklist.md` must remain an executable transfer test, not a document-presence checklist. Its central question is whether a different team can execute and prove the capability without relying on the author.

All eleven criteria remain substantive:

1. each domain is executable through objective, dependencies, procedure, artifacts, evidence and gate;
2. critical decisions have explicit criteria and transferable authority;
3. deliverables have owner, minimum content, example and acceptance criteria;
4. method remains comprehensible without requiring the toolkit;
5. critical controls trace to evidence, source of truth and review mechanism;
6. reference cases traverse risk, identity, tools, lifecycle, observability and assurance coherently;
7. roadmap, short plans, pilot and backlog are consistent views of one program;
8. architecture is product-neutral and technology mappings are separate;
9. the operating model works proportionally without centralizing low-risk queues;
10. the organization can actually detect, contain, investigate and retire a production agent;
11. value and cost are measured by outcomes rather than adoption or agent count.

Critical boundary: criterion 10 cannot be proven by reading. A design, simulator or runbook is not evidence that production detection and containment were exercised. The source self-assessment dated 2026-08-10 records criterion 10 as unverified and criterion 2 as only partially met because the corpus had one owner/approver and no independent challenge. Those statements are versioned source evidence—not assertions about the future repositories or an adopting organization.

## ADR-0010 — Structured governance contracts 2.0

ADR-0010 is an accepted source decision that supersedes ADR-0005. Its history, compatibility table and evidence must be preserved; clean-room target adoption still requires an explicit destination ADR rather than silently treating the source ADR as organizational adoption.

Durable contract relationships:

- `schemaVersion` governs structural compatibility and is independent of `catalogVersion`;
- the Control Catalog contract is schema 2.0, while control content is catalog 1.2.0;
- `automation` and `frameworkMappings` are mandatory; an empty mapping array means deliberate absence, never permission to invent a reference;
- Registry 2.0 separates discovery status/confidence, lifecycle stage/operational state, transition authority/evidence and risk tier/admissibility;
- Blueprint 2.0 binds model version/catalog/evaluation, certified sources and enterprise tools;
- reference contracts 1.0 cover model/provider catalog, certified source catalog, enterprise tool registry, release evidence manifest and audit event;
- cross-record validation rejects unknown bindings;
- migration must not infer absent authority, evidence, admissibility or version;
- human templates remain the workshop/decision interface, while JSON schemas provide interoperability—not a mandatory workflow product.

Compatibility must not be flattened:

| Contract | Source transition | Meaning |
|---|---|---|
| Agent Registry | 1.0 → 2.0 | breaking |
| Agent Blueprint | 1.0 → 2.0 | breaking |
| Control Catalog schema | declared 1.1 → 2.0 | corrected major version |
| Control Catalog content | 1.1 → 1.2.0 | additive; adds `AGF-RSK-004` |
| New catalogs/events | absent → 1.0 | additive |

Stable control IDs and the no-invented-normative-reference constraint remain validation invariants.

## Schema ecosystem

`schemas/README.md` defines the source Draft 2020-12 structured-artifact set and must remain synchronized with actual migrated schemas and examples:

- Agent Registry 2.0;
- Agent Blueprint 2.0;
- Control Catalog schema 2.0 / content 1.2.0;
- maturity assessment;
- model/provider catalog;
- certified source catalog;
- enterprise tool registry;
- release evidence manifest;
- audit event envelope.

The target must preserve:

- stable IDs and versions;
- major-version bumps for incompatible changes;
- `additionalProperties: false` where the source contract uses it;
- explicit missing evidence rather than plausible values;
- no secrets, tokens or connection strings; human documents use `[REDACTED]`;
- `.invalid` domains and fictitious identities in examples;
- separation between Registry (what exists, ownership, discovery, stage/state, tier/admissibility) and Blueprint (how it works, versioned bindings and blast radius);
- negative and cross-record tests, including reviewer distinction, valid sampling, attestation validity, control IDs and traversal-safe paths.

The source validation command is historical/reproducible evidence. The new repositories must define and execute their own equivalent gates against their resulting layouts.

## ADR-0009 — Risk tier and admissibility

ADR-0009 is an accepted source decision superseding ADR-0004. It corrects the imported conflation of T4 with `Restricted`.

The following semantics are immutable migration requirements unless a new destination ADR explicitly changes them:

- `T1`–`T4` measure criticality/exposure severity;
- T1 fast path is proportional routing, never exemption;
- `permitted`, `conditional`, `restricted` and `prohibited` express admissibility;
- `restricted` is default deny and requires authority, an explicit temporary exception reference and expiry;
- `prohibited` cannot enter or remain in production in that scope;
- Registry, Blueprint, risk record and release evidence expose both dimensions;
- changing either dimension is material and forces reassessment;
- external labels must be decomposed before mapping; imported `Restricted` maps to admissibility and never redefines T4.

A low-impact purpose can be prohibited, and a critical purpose can be permitted under suitable authority and controls. No one-dimensional onboarding table can represent the whole decision.

## Human template system

`templates/README.md` is the source index for governance, architecture, assessment, release, operation, analytics, communication and research templates. It relates each reusable human interface to structured records and the artifact catalog.

Rules preserved:

1. adapt language, roles and thresholds to organizational context;
2. do not remove rationale, owner, evidence or expiry for superficial simplicity;
3. distinguish `missing`, `not-applicable`, `passed` and `failed`;
4. represent secrets/sensitive data as `[REDACTED]`;
5. version decisions and preserve predecessors;
6. link forms to Registry/Blueprint and evidence packages;
7. use schemas when applicable;
8. templates accelerate work but never constitute automatic approval or proof of efficacy.

Commercial proposal material remains in the separate consulting repository and may reference a framework release but cannot redefine its policy, controls or decision gates.

## ADR template

`templates/adr-template.md` must remain a decision record rather than a prose memo. It preserves:

- status, date, accountable person, reviewers, domain and supersession links;
- context and why a decision is needed;
- forces, significant requirements and quality attributes;
- real alternatives with advantages/disadvantages;
- unequivocal decision and rationale;
- positive/negative consequences;
- risk/mitigation table;
- measurable validation criteria;
- review triggers;
- primary or repository-relative evidence.

Destination status values and front matter may be normalized, but an Accepted ADR is never silently rewritten; a new ADR supersedes and cross-links it.

## Assessments

`assessments/README.md` classifies comparative, risk, maturity, technology and control-effectiveness assessments. The deprecated Microsoft Customer Zero crosswalk remains historical and non-normative.

Every assessment preserves:

- scope and exclusions;
- criteria and evidence cutoff;
- assessor and independence;
- evidence, coverage and confidence;
- gaps, conflicts and limitations;
- decision requested;
- owners, expiry and next review.

A score is not compliance, and missing evidence is not approval. Vendor case studies and institutional reports do not prove causality, ROI, independent effectiveness or conformity.

## Architecture index

`docs/architecture/README.md` is a navigation index for conceptual architecture, principles, quality attributes, risks, diagrams and decision log. It is not a second canonical source. Destination links must be rewritten to the new clean-room structure, and the decision log must retain accepted, rejected, deprecated and superseded history.

## Cross-batch dependencies

This partial relies on and must reconcile with:

- the authoritative Control Catalog and schema records in micro-01;
- source validator behavior in micro-02a;
- Registry, Blueprint, release-manifest and audit-event schemas/examples across other microbatches;
- service-desk and meeting-notes reference cases;
- risk-management, Responsible AI, human-oversight, evidence and operations chapters;
- source ADR-0004 and ADR-0005, which remain superseded history;
- target provenance and supersession ledgers.

## Explicit limitations

- Source acceptance records establish provenance; they do not constitute adoption by an organization using the future implementation template.
- Source dates and source self-assessment results remain historically qualified to 2026-08-10.
- Fictitious cases demonstrate contract coherence only.
- No real production estate, identity, tool, incident, impact or control-effectiveness evidence is introduced.
- No ISO clause-level claim may be inferred from public overview material.
- No Gate 2 publication action is authorized.

# micro-02c

# Microbatch 02c migration relationships

Source snapshot: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot`  
Commit: `5545d9227624400ab8bb707b6032b2f61329a36e`  
Reader: `main:gpt-5.6-sol:micro-02c:2026-08-11`

## Coverage

- 8 paths read completely.
- 8 auditable file records generated.
- 55/55 Markdown headings reconciled exactly.
- 0 non-substantive paths.
- 0 validation errors, blocked paths or destination gaps.
- Validation evidence: `micro-02c-validation.json`.

## Audit-universe integration

The source method deliberately avoids creating a parallel “AI audit universe.” It extends existing audit areas—assets/CMDB, IAM, data/privacy, integrations/change, third parties, security, SDLC, operations and benefits—while identifying Responsible AI/human oversight as the most likely genuinely new area.

Preserved audit distinctions:

- 40 source agent-scope controls are sampled by agent; four organization-scope controls are tested once at entity level;
- 27 source blocking controls are candidates for release-key controls;
- automation mode drives configuration, sample or process testing;
- verification describes how evidence is obtained, not merely that an artifact exists;
- organization-scope source controls do not block one release; failure triggers entity-level remediation;
- evidence validity is tied to agent/model/data/tool version rather than an annual test period;
- samples are stratified by risk tier and admissibility, with complete T3/T4 coverage;
- conditional approval proves conditions were imposed, not fulfilled;
- first-cycle testing prioritizes registry ownership, blocking-control behavior, expired attestation, expired conditions and unresolved catalog bindings.

No clause-level equivalence, conformity or attestation is inferred. Formal mappings require the licensed normative text and competent authority.

## Metric governance

KPIs, KRIs, operational metrics and value metrics remain separate. Every metric presented to a governance forum requires:

- formula/source;
- owner;
- baseline and coverage;
- threshold with rationale;
- review date;
- expected action;
- traceable decision history.

Source percentages and lead-time ranges are preserved as starting hypotheses only. They are neither universal policy nor SLA. Adoption measures frequency/retention and cannot prove quality or value. The target dashboard keeps executive posture separate from drill-down to trace, evidence and tool action.

## DejaVu license

The complete 99-line Bitstream Vera and Arev/DejaVu license notice remains byte-preserved with both TTF assets. It retains:

- required notices;
- rights to use/copy/merge/publish/distribute/sell under conditions;
- renaming requirements for modified fonts;
- prohibition on standalone typeface sale;
- AS-IS warranty and liability exclusions;
- restrictions on promotional use of rights-holder names.

This font license remains independent of the framework content license.

## AI-Ready Data Gate

The pattern preserves the rule that availability or user access is not authorization for AI use. Connector, retrieval, memory or training requires a data contract and reapproval after material source/context change.

The operational flow retains purpose, owner/classification, provenance/quality/suitability, identity and pre-retrieval authorization, retention/deletion, leakage/segregation testing, conditions/expiry and change monitoring. Data readiness does not replace evaluations, risk management or runtime control.

## Site build versus publication

Source ADR-0008 remains archived as an accepted source decision superseding ADR-0007. It separates strict reproducible build from optional manual publication:

- MkDocs/staging/strict build remains an integrity check;
- the source Pages workflow is manual only;
- absence of a public URL is not framework incompleteness;
- any manual site must be built from an explicit commit/tag and generated output is never edited;
- repository and handbook remain canonical.

Equivalent behavior in the clean-room framework requires a new target ADR. Gate 1 performs no remote publication.

## Release evidence

The human release-evidence template remains a pointer/index, not duplicate evidence. It preserves release metadata, approvers, per-control evidence, assessments/evaluations/readiness, conditions/exceptions with authority/owner/expiry/monitoring, artifact SHA-256 and seven final checks.

A source contract ambiguity was registered: the decision table lists `approved / conditional / rejected / expired`, while a final check refers to `hold/rejected`. The target must reconcile `hold` explicitly against the machine schema and zero-to-BAU gate-state model rather than silently losing it.

## Historical spec-validation inconsistency

`specs/002-governance-contract-alignment/validation.md` is archived, not reused as current validation. It marks all ten acceptance rows `done`, while also saying command results will be recorded later and no status anticipated. This is historical evidence tension, not executable proof.

In particular, source claims concerning tags/GitHub Releases do not carry into the clean-room Gate 1, which has no remote. Target validation depends on actual command output only.

## Audit-event example

The fictitious schema 1.0 event preserves:

- `EVT-EXAMPLE-0001`;
- workload actor and identity reference;
- agent/version and correlation ID;
- tool-request event type;
- allow/success policy/outcome;
- internal data classification;
- `TLR-KNOWLEDGE-SEARCH-001` and `knowledge.search` as non-state-changing;
- redaction applied;
- evidence reference and reason code.

It remains a structured conformance fixture, not evidence that a runtime control is effective.

# micro-03

# micro-03a

# Microbatch 03a migration relationships

Source snapshot: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot`  
Commit: `5545d9227624400ab8bb707b6032b2f61329a36e`  
Manifest: `control/micro-03a.txt`  
Reader: `subagent:gpt-5.6-luna:micro-03a`

This report records relationships, duplication, differences, supersession, conflicts, gaps, dependencies, target boundaries and decisions for the six assigned paths. The clean-room target remains governed by the approved ten-chapter/framework-toolkit structure; the source plans are evidence, not a replacement taxonomy.

## Reading method and preservation

All six manifest paths were read from first to final line with `read_file`. The four substantive files were inspected at full content level: every front-matter field, Markdown heading subtree, table row, bullet, Python import, class, helper, test method, assertion, fixture mutation and referenced contract path was considered. The two `.gitkeep` files were read completely and classified as genuine empty-directory placeholders.

The generated ledger preserves:

- complete Python source plus top-level AST units for `tools/scripts/test_validate_repository.py`;
- exact full Markdown heading sections for the two plans and assessment template;
- exact byte/hash/line metadata for every file;
- curated definitions, requirements, controls, procedures, decisions, exceptions, examples, references, dependencies and target transformations;
- explicit non-substantive justifications for both placeholders.

Source inventory totals: **6 paths**, **40,692 bytes**, **938 lines**, **4 substantive records**, **2 non-substantive records**. The two placeholders are byte-identical (`18` bytes, `1` line, SHA-256 `5092e9ac41da1a39d8d3bb6a26eee7416bb7d0ca760942892dbe01fd2b8cf62a`).

| Source path | Status | Bytes | Lines | Markdown headings | Primary treatment |
|---|---:|---:|---:|---:|---|
| `tools/scripts/test_validate_repository.py` | reviewed | 34,427 | 730 | 0 | preserve as target validation tooling, adapt and rerun |
| `specs/001-handbook-consulting-product/plan.md` | reviewed | 3,037 | 93 | 9 | archive under source-history |
| `specs/002-governance-contract-alignment/plan.md` | reviewed | 2,344 | 61 | 7 | archive under source-history |
| `templates/assessment-template.md` | reviewed | 848 | 52 | 11 | framework toolkit template; optional implementation instantiation |
| `docs/architecture/decisions/.gitkeep` | non-substantive | 18 | 1 | 0 | omit after real decision content exists |
| `experiments/.gitkeep` | non-substantive | 18 | 1 | 0 | omit after real experiment content exists |

## Duplication and consolidation relationships

1. **The two source plans overlap but are not duplicates.** Both use a staged implementation strategy, call for documentation/toolkit work, quality validation, review and explicit risk mitigation. Plan 001 is the broader editorial/handbook/consulting product plan (four commits, reviewed 2026-08-09); Plan 002 is the narrower contract-alignment plan (four waves, reviewed 2026-08-10) with RED tests, schema 2.0, cross-record invariants and release review. Preserve both as historical plans; do not merge their sequences into a current target roadmap without reconciliation.
2. **Plan 001 and the handbook/framework corpus.** Its README → index → handbook → domains tree is an historical information architecture. It explains rationale for modular canonical content and an editorial handbook, but it must not redefine the approved ten-chapter target. Reusable principles can be re-expressed in current chapters only after validation; the source plan itself belongs in `project/specs/source-history/001-handbook-consulting-product/`.
3. **Plan 002 and structured contracts.** Its waves describe the origin/implementation sequence for Registry, Blueprint, Control Catalog, catalog bindings, audit events and release manifests. The executable test suite in this batch tests part of the same contract surface. The plan is archival; current schemas, examples and validator behavior are the authority after clean-room migration.
4. **Validator tests versus normative documentation.** `tools/scripts/test_validate_repository.py` repeats concepts that also exist in schemas, controls, consulting boundaries, tier taxonomy and contract examples, but in executable form. It is complementary evidence, not a second policy. Assertions must be retained and then reconciled with target schemas and validator paths.
5. **Assessment template versus other assessment artifacts.** The generic template provides a technology/approach comparison scaffold. It should not replace risk assessment, capability assessment, release decision or implementation evidence records. Its reusable structure belongs in the framework toolkit; filled values and authority belong in the implementation template.
6. **Identical placeholders.** The two `.gitkeep` files are an exact-content duplicate with different directory purposes. They have no semantic content and should not generate target documents.

## Differences and incompatibilities requiring controlled treatment

1. **Historical plan sequence versus clean-room structure.** Plan 001 names an old editorial tree and Plan 002 names waves/contract milestones. Neither sequence is the approved ten-chapter taxonomy, and neither should become a hidden source of target architecture.
2. **Plan timing and formal status.** Plan 002 is later and more contract-specific than Plan 001, but both front matters say `supersedes: null`. Later review date is provenance, not a formal supersession decision.
3. **Assessment criteria mismatch.** The template defines six weighted criteria—Security, Governance, Integration and interoperability, Operability, Cost and Portability—but its evaluation table has only Security, Governance, Operation and Cost plus weighted result. Integration/interoperability and Portability are omitted from the evaluation columns, and “Operability”/“Operation” are not identical labels. This is a real template defect to fix or explicitly version; it must not be silently normalized in the ledger.
4. **Assessment placeholders versus evidence.** `Draft`, `YYYY-MM-DD`, `Nome`, blank cells, `Alternativa A/B` and `Fonte ou artefato relativo` are scaffolding. They cannot be treated as an assessment, recommendation, approval or evidence package.
5. **Validator path/corpus coupling.** The test suite dynamically loads `tools/scripts/validate-repository.py`, copies the complete source JSON corpus, and references exact consulting, schema, example, control and workflow paths. A target with renamed or intentionally removed contracts requires a deliberate test adaptation and a new execution result; copying the file alone is insufficient.
6. **Source assertions versus target change.** The tests assert exactly nine ordered consulting offers, vendor-neutral core behavior, T1–T4 labels and Governance Contract 2.0. Those are valuable source controls, but if a target release changes any contract, the change requires an explicit decision and updated tests rather than a silent assertion rewrite.

## Explicit supersession, history and status

- Both plans explicitly declare `status: approved` and `supersedes: null`. They are approved source plans, not current target authority and not formally superseded by one another.
- Plan 002 is a later, narrower refinement of contract work, but the ledger records `historical-plan-no-formal-supersedes`; it does not fabricate an ADR relation.
- The clean-room archive destination is a preservation decision, not evidence that the source plans were formally deprecated or that every planned item was completed.
- The validator test suite and assessment template have no declared supersession metadata and are reviewed/current at the source commit for their respective roles.
- Both `.gitkeep` files are placeholders only; omission from the target is not deletion of substantive history.

## Conflicts and controlled corrections

1. **Template scoring table conflict:** the criteria table and evaluation table do not have the same dimensions. A target implementation must either add the missing columns, reduce/rename the criteria with explicit versioning, or record why a criterion is assessed elsewhere.
2. **Plan 001 commit sequence versus Plan 002 wave sequence:** these are overlapping historical execution models, not two current mandatory schedules. Plan 002's contract-first RED-test emphasis cannot be imposed retroactively on Plan 001, and Plan 001's four commits cannot be treated as the target release plan.
3. **Consulting boundary risk:** Plan 001 includes a consulting product in its historical information architecture. The target framework must keep consulting packaging separate from canonical governance chapters; no source plan wording can make commercial packaging normative.
4. **Executable assertions and target taxonomy:** a validator test that fails after migration may indicate a target contract change rather than a source defect. The failure must be triaged against the target release decision, not fixed by weakening the assertion without provenance.

No direct contradiction was found between the plans' substantive governance principles: both preserve Policy V1/history boundaries, prefer modular content, require validation and treat pilot/schedule claims cautiously. The material conflicts are migration-boundary or template-structure conflicts described above.

## Gaps and unfinished material

- The plans link to `spec.md`, `tasks.md` and `validation.md`, which are outside this partial manifest; completion status and historical checkboxes cannot be inferred from these plan files alone.
- No target repository was created, so the validator suite was not exercised against the clean-room target. Its source-path assumptions and every expected schema/example pair still require target validation.
- The assessment template does not define score scales, aggregation math, threshold, tie-breaker, approval authority, evidence identifiers/hashes, risk tier/admissibility fields, or a decision disposition enum. Those belong to the consuming toolkit/release and organization unless separately adopted.
- The plans do not provide a current target release identifier, target owner map, or evidence that all four commits/waves remain open. Do not resurrect them as backlog automatically.
- The placeholders provide no experiment or decision content; real target records must supply the missing substance.
- Cross-batch dependencies are material: the validator references schemas/examples and repository files handled in other microbatches, while the plans depend on their associated spec/task/validation documents.

## Cross-file dependencies

- `tools/scripts/test_validate_repository.py` depends on `tools/scripts/validate-repository.py`, the full JSON corpus, consulting package docs, schemas, examples, `controls/control-catalog.json`, canonical templates and workflow/document paths.
- `specs/001-handbook-consulting-product/plan.md` explicitly relates to `spec.md`, `tasks.md` and `validation.md`; it also depends conceptually on the Policy V1 artifact, ADR/spec records, handbook, toolkit, schemas, examples and CI/quality scripts named in its commit plan.
- `specs/002-governance-contract-alignment/plan.md` explicitly relates to `spec.md`, `tasks.md` and `validation.md` and depends on Registry/Blueprint/Control Catalog contracts, catalog/audit/release schemas/examples, validator invariants and migration guidance.
- `templates/assessment-template.md` has no file links; its implementation dependency is a local owner, evidence set, release context and decision authority supplied by the consuming repository.
- The two placeholders have no dependencies.

## Boundary classification

### Framework canonical/toolkit

- `tools/scripts/test_validate_repository.py` as executable quality-gate tooling, after path/corpus adaptation and real target execution.
- `templates/assessment-template.md` as a reusable human assessment template under `toolkit/templates/`, preserving all fields and explicitly documenting its illustrative weights and missing decision mechanics.
- Principles from the plans may inform current framework chapters only through separately reviewed, target-shaped content; the source plan sections themselves remain history.

### Project/history in framework

- Both approved plans under `project/specs/source-history/001-handbook-consulting-product/` and `project/specs/source-history/002-governance-contract-alignment/`, with source commit/date and non-binding status.
- No source plan should be presented as a current roadmap, adopted policy or release decision merely because it is archived in the target.

### Implementation template

- A filled/localized copy of the assessment template may live at `assessments/assessment-template.md` in `ai-agent-governance-implementation-template`, with local evaluator, owner, weights, evidence, validity, approval and disposition.
- The validator test suite is framework tooling, not organization-specific evidence; implementation repositories may consume its release checks but should not turn source fixture values into organizational facts.

### Consulting

- Plan 001's consulting-product material is historical context only. No consulting package, pricing, offer or commercial claim from this batch becomes canonical framework content. Any future consulting module must reference a specific framework release rather than duplicate policy, controls or decision rights.

### Placeholder handling

- Omit both `.gitkeep` records after real target decision and experiment structures exist. Preserve their non-substantive classification in the ledger; do not create empty target documents.

## Decisions requiring Rodgui before migration finalization

1. **Validator retention/adaptation:** confirm whether the source test suite remains at `tools/scripts/test_validate_repository.py` in the clean-room target and which target release contracts are authoritative when source assertions and target changes differ.
2. **Assessment template contract:** confirm the implementation-template copy and decide whether to add the missing Integration/interoperability and Portability evaluation columns, including local scoring/approval semantics, or version the template explicitly.
3. **Historical-plan promotion boundary:** confirm that both source plans remain archive-only, or identify any specific principle that should be re-authored as a new current ADR/roadmap item. No source plan should be promoted silently.

These decisions do not block the durable forensic records; they block only silent target migration or canonicalization.

## Completion counts

- Expected paths: **6**
- File records: **6**
- Markdown headings expected: **27**
- Heading rows produced: **27**
- Blocked paths: **0**
- Decision-required items: **3**

# micro-03b

# Microbatch 03b migration relationships

Source snapshot: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot`  
Commit: `5545d9227624400ab8bb707b6032b2f61329a36e`  
Manifest: `control/micro-03b.txt`  
Reader: `subagent:micro-03b:gpt-5.6-luna:2026-08-11`

This report records the source identity, complete-reading preservation, semantic relationships, duplication boundaries, differences, contradictions, supersession, gaps, dependencies, destination classification and migration decisions for all nine assigned paths. The clean-room target remains governed by its approved chapter/toolkit boundaries; these source documents are evidence and reusable material, not permission to create duplicate canonical policies or to promote placeholders into facts.

## Reading method and preservation

All nine manifest paths are UTF-8 Markdown files. Each was read from line 1 through its final line before generation. Every source file was reviewed as a complete document: front matter, headings, repeated headings, prose, tables, lists, code fences, examples, links, field placeholders, enumerated conditions, decision gates and caveats were considered. No source snapshot, protected checkout or parent manifest was modified; outputs are confined to the control directory.

The generated ledger preserves:

- exact source SHA-256, byte count and line count at the immutable commit;
- complete Markdown heading subtrees, including structural and placeholder headings;
- curated definitions, requirements, procedures, controls, decisions, exceptions, examples, references, dependencies, source status, supersession and destinations;
- the distinction between normative/guidance content, reusable toolkit templates, implementation instantiations and executive communication;
- source limitations such as missing runtime evidence, missing filled values, non-universal example thresholds and the absence of formal supersession.

No file is classified `non-substantive`; all nine are substantive reviewed records.

## Source inventory

| Source path | Role | Status | Bytes | Lines | Markdown headings | SHA-256 | Primary destination |
|---|---|---:|---:|---:|---:|---|---|
| `docs/registry/README.md` | estate registry, taxonomy, ownership, blueprint and registry gate | reviewed | 11,038 | 163 | 15 | `c7ba863e10fc5fe50650fabd6adb0f062c79f5ad4a43416369ce9dc4cbe7da30` | `docs/master/03-portfolio-and-value.md`; derived `toolkit/registry/README.md` |
| `docs/architecture/principles.md` | 13 architecture principles, validation method and tensions | reviewed | 7,139 | 75 | 6 | `7c51b9f71a5a90d3246e6ad8961d538fb293bd07046d541b260a8abce17f49c1` | `docs/master/01-mandate-scope-and-principles.md` |
| `docs/operations/behavioral-analytics.md` | behavior units, features, baselines, response ladder and enforcement gate | reviewed | 6,023 | 108 | 13 | `146f9ad775f3675ff279d8237ea9339e93e42dc0267d4722a235ac08e56abbf1` | `docs/master/09-operations-incidents-and-continuity.md`; linked toolkit template |
| `docs/value/README.md` | value chain, portfolio governance, metrics, attribution and value review | reviewed | 4,952 | 135 | 12 | `5189abe378eb5a2f240dc1f1b5e0661dc7f0eb1a99a212709bcfb5d5a829ab10` | `docs/master/03-portfolio-and-value.md` |
| `docs/patterns/evidence-package-as-code.md` | vendor-neutral evidence manifest, CI checks, human decisions and release/archive flow | reviewed | 3,804 | 138 | 17 | `aee499065d0d4d9c989df2ed79ce490f4cdc730c868d980aaaa66a891d33e588` | `toolkit/patterns/evidence-package-as-code.md` |
| `templates/risk-pre-screen.md` | human intake routing questionnaire and escalator rules | reviewed | 3,689 | 60 | 5 | `c7a0a937c2f6eaa3df866981bb5879f906698875cc8e306530ee31fd4d5cc708` | `toolkit/templates/risk-pre-screen.md`; optional implementation intake |
| `templates/self-assessment-form.md` | human pre-approval/release/change self-assessment | reviewed | 2,491 | 77 | 8 | `toolkit/templates/self-assessment-form.md`; optional implementation assessment |
| `templates/control-implementation-record-template.md` | per-control implementation, testing, findings, exception and decision record | reviewed | 1,354 | 85 | 12 | `toolkit/templates/control-implementation-record-template.md`; optional per-control implementation record |
| `templates/executive-brief-template.md` | decision-oriented communication scaffold | reviewed | 440 | 37 | 10 | `toolkit/templates/executive-brief-template.md` |

Source totals: **9 paths**, **40,930 bytes**, **878 lines**, **9 substantive records**, **98 Markdown headings**. All nine source hashes above were independently recomputed from the immutable snapshot.

## Semantic inventory and target boundaries

### Registry, taxonomy and portfolio value

`docs/registry/README.md` defines four distinct objects: Registry identifies the agent and ownership/state; Blueprint specifies versioned desired state; Policy/gate decides whether configuration/evidence meets rules; Runtime/telemetry observes actual operation. It defines a platform-independent taxonomy with dimensions including origin, ownership, reach, function, autonomy, identity, data, tools, runtime, topology and lifecycle. It specifies minimum registry questions, source-of-truth groupings, T1–T4 obligations, quality findings, machine-readable blueprint expectations, artifacts, evidence, metrics, failure modes and a registration/production decision gate.

`docs/value/README.md` defines the value chain from observed problem through intervention hypothesis, capability, behavior/process change, measurable output, outcome, impact, cost and externalities. It separates eight metric layers, requires baseline and attribution limitations, keeps Portfolio distinct from Registry, specifies portfolio decisions and value-review outcomes, and gates funded portfolio entry on problem, owner, baseline or an explicit plan, value hypothesis, costs, metrics and sunset criteria.

These files are complementary, not duplicates: Registry answers “what exists and who is accountable”; Portfolio answers “should this use case continue to exist.” Their shared fields (owner, tier, status, cost/value evidence) must remain cross-linked without fusing the artifacts. Both map to chapter 03, but a toolkit registry reference must be derived or linked rather than become a second policy authority. The registry document contains two headings named `Como implementar` with different source ranges (taxonomy implementation at lines 57–66 and blueprint implementation at lines 113–122); they are context-specific and must not be collapsed merely because the labels match.

### Principles and policy boundaries

`docs/architecture/principles.md` preserves exactly 13 decision principles: Visibility first, Identity first, Explicit capability, Proportional by risk, Embedded by default, Human-led, Observable and remediable, Federated with common controls, Evidence before automation, Lifecycle-aware, Platform-agnostic, Value-linked and Iterative. Each is paired with a decision question, practical application and avoided antipattern. The file also defines a ten-scenario/three-group validation method, annual or material-change revalidation, tensions between principles and the requirement to record authority rationale when principles collide.

The target destination is chapter 01. The principles are a decision layer linked to policy, not vendor rules, compliance claims or a replacement for concrete standards. The source explicitly says platform mappings cannot redefine the principles; that boundary must survive clean-room editing.

### Runtime behavioral analytics

`docs/operations/behavioral-analytics.md` distinguishes deterministic prohibition rules from behavioral anomaly detection. It requires an explicit behavior unit and `agent_id` for autonomous agents; lists observable features; distinguishes individual and peer-group baselines; requires at least 30 days or a seasonal operating cycle in monitor-only; combines relative deviation with an absolute floor; enriches signals with tier, owner, deployment version, business event, tool risk and data-source class; and defines six initial anomaly cases. The response ladder is `observe` → `alert` → `throttle` → step-up → disable tool → quarantine. New cases begin with human response; automatic containment requires measured precision and false positives. Rule and baseline versions must identify the logic that generated a decision.

The canonical destination is chapter 09, with the referenced Behavioral Analytics Use Case retained as a linked operational template. Example values such as “5x the p95” illustrate why a floor is needed; they are not universal thresholds. This material is operational guidance and calibration-dependent, not proof that any runtime control is implemented or effective.

### Evidence Package as Code

`docs/patterns/evidence-package-as-code.md` is a vendor-neutral reusable pattern. It defines a manifest per `agent/version` containing registry/blueprint references, tier and assessments, control IDs/status, tests/evals, approvals/conditions/expiry, runtime readiness, immutable hashes/links and missing/not-applicable rationale. CI validates structure and sources; domain reviewers add decisions; release authority evaluates completeness/conditions; the package is signed/hashed/archived and linked to runtime incidents/attestation; supersession creates a new package and never overwrites history.

It must remain in `toolkit/patterns/`, not be presented as an adopted policy or vendor endorsement. Its central limitation is explicit: green CI does not prove efficacy and does not replace human/domain judgment. Sensitive evidence may be represented by secure references rather than repository content.

### Human templates and communication

- `templates/risk-pre-screen.md` is a fast routing instrument before full scoring. It requires identity/owner/date/model fields; 15 answers of `sim`, `não` or `não sei`; evidence/observation; escalator logic; proposed tier/admissibility; reviews; gaps with owner/deadline; and route rationale. `Não sei` is a gap, never `não`. Questions 3, 5, 6, 7, 8, 9 and 10 are individual escalators; 2+3 and 4+14 are combined conditions; question 1 is T4 only when restricted data is sent to an external provider; any yes on question 6 triggers the Responsible AI impact screen; question 15 no plus question 2 or 3 yes blocks production. Final classification/admissibility remains with the decision-gate authority.
- `templates/self-assessment-form.md` is a broader human record before design approval, release or material change. It covers purpose, owners, data/impact, tier, tool/action capability and state-changing behavior, scopes, reversibility, approval/gateway, human accountability, segregation of duties, kill switch/quarantine/rollback, controls/evidence, adversarial and functional testing, operations/lifecycle and disposition. Missing evidence remains `missing`; it is not approval.
- `templates/control-implementation-record-template.md` is a per-control record. It requires the literal catalog statement, applicability rationale, implementation separated into preventive/detective/responsive/corrective, evidence provenance, independent design/effectiveness tests, metrics, findings/remediation, exception authority/expiry/trigger and a final decision enum. Implementation status (`missing`, `planned`, `implemented`, `effective`, `failed`, `excepted`) is distinct from final decision (`effective`, `conditionally effective`, `ineffective`, `not applicable`).
- `templates/executive-brief-template.md` is communication scaffolding with decision requested, context, urgency, recommendation, expected benefits, risks/mitigation, five impact dimensions, next steps and related ADR/assessment/experiment slots. Empty cells, generic title and `Ação.` are placeholders; the file is not a decision, evidence package or realized benefit.

All four templates map to toolkit locations. Their second candidate destinations, where present, are optional instantiated records in `ai-agent-governance-implementation-template`; those instances must supply local owners, evidence, authority, dates, conditions and disposition while leaving the canonical templates unchanged.

## Duplication and near-duplicate boundaries

1. **No exact full-file duplicates.** All nine source SHA-256 values are distinct.
2. **Registry versus value README:** shared owner/tier/status/value vocabulary is intentional cross-reference, not duplication. Preserve Registry-versus-Portfolio boundaries.
3. **Risk pre-screen versus self-assessment:** both collect identity, owner, tier, tools, evidence and gaps, but pre-screen routes and escalates before complete scoring while self-assessment prepares a design/release/material-change submission. Do not merge their question sets or treat the pre-screen as final assessment.
4. **Self-assessment versus Control Implementation Record:** both include controls and evidence, but the former is agent-level readiness and the latter is one-control implementation/effectiveness evidence. The control record must retain the literal control statement and separate implementation status from decision.
5. **Evidence Package as Code versus the templates:** the package is the versioned index and release/archive contract that can reference self-assessment, control records, tests and approvals. It does not replace those records, and CI validity does not replace authority judgment.
6. **Behavioral analytics versus Registry/Blueprint:** behavioral analytics consumes identity, tier, owner, version and runtime context; Registry/Blueprint define identity and desired state. An anomaly record is not a registry record or a blueprint revision.
7. **Principles versus all other files:** the principles explain decision questions and antipatterns. They should constrain interpretation but must not be copied as duplicate control text into every template.
8. **Executive brief versus evidence/decision records:** the brief points to ADRs, assessments and experiments; its narrative cannot substitute for them.
9. **Repeated headings:** the repeated `Como implementar` headings in the registry file are distinct subtrees. Mechanical output preserves both by line range.

## Differences, contradictions and controlled treatment

No direct contradiction was found among the nine source files. The following are material boundaries or tensions requiring controlled treatment:

1. **Routing versus final decision:** the pre-screen records a preliminary route and admissibility; the self-assessment records preparation for a later gate and a disposition field. They use different vocabularies (`permitted/conditional/restricted/prohibited` versus `approved/conditional/rejected/expired`) for different workflow stages. Do not normalize them into one enum without an explicit target decision.
2. **Evidence presence versus effectiveness:** the Evidence Package pattern, self-assessment and control record all require evidence references, while the pattern explicitly states that CI structure/link validation does not prove efficacy. A generated or complete package must not be reported as effective without the applicable human/domain and effectiveness decisions.
3. **Registry/Blueprint versus narrative governance:** the registry file allows narrative decisions, impact assessments and risk acceptance to remain referenced evidence rather than YAML fields; the evidence pattern likewise indexes human decisions. Machine-readable structure must not be mistaken for complete governance or approval.
4. **Automatic containment versus human-led calibration:** behavioral analytics defines a response ladder but forbids automatic enforcement until monitor-only, false-positive measurement, absolute-floor declaration and versioning are present. The pre-screen has a specific production blocker for missing tested rollback/kill switch in combination with writing/materially relevant action. These are complementary gates at different lifecycle stages, not conflicting thresholds.
5. **Template scaffolding versus source status:** blank fields and placeholder values are intentionally present in the templates. They are not missing source content and must not be filled or counted as evidence during migration.
6. **Portfolio value versus causal proof:** the value document requires baselines, comparisons, uncertainty and attribution limits; the executive template requests expected benefits but supplies no proof. Expected benefit remains a hypothesis until the portfolio evidence exists.

## License, supersession and source status

- The nine assigned files contain no embedded `license` front-matter field or license notice. This ledger therefore makes no unsupported license claim and does not invent a source license dependency; any repository-level license must be resolved from the target repository's authoritative licensing material outside this manifest.
- All nine sources have no declared superseding document at the source commit (`supersedes: null` where front matter is present; curation records use `none-declared` or the reusable-template current status).
- `docs/registry/README.md`, `docs/operations/behavioral-analytics.md`, `docs/value/README.md` and `docs/patterns/evidence-package-as-code.md` are maintained source documents with recorded review dates/cycles.
- `docs/architecture/principles.md` is maintained and validated at source with a 180-day review cycle.
- The four template files are current reusable human templates at the source commit, not completed assessments or decisions.
- No target relocation, derived toolkit reference or implementation instantiation should be described as formal source supersession. If target policy changes a source decision, create an explicit versioned target decision and preserve the source history.

## Gaps and unfinished material

- Source provenance is not embedded as a governance field in the documents; the ledger carries immutable commit, hash, bytes, lines and reader instead of inventing source properties.
- Several links and referenced consumers are outside this manifest: registry/blueprint schemas and examples, risk-management documents and decision-gate playbook, policy/operating-model documents, behavioral analytics template, audit-event schema, FinOps/KPI references, and related patterns. Their semantics were not silently inferred or rewritten here.
- No real registry records, blueprint instances, evidence packages, runtime observations, baseline datasets, calibration results, incident records, portfolio decisions or filled assessments are included in this batch.
- Behavioral analytics contains no measured precision, false-positive rate, seasonal baseline or enforcement result. The 30-day monitor-only requirement and illustrative examples remain source guidance.
- Templates do not provide concrete owners, authorities, evidence IDs/hashes, dates, thresholds, validity/expiry values or completed dispositions. Those are intentionally supplied by a consuming workflow.
- The source does not define a single cross-artifact identifier or schema for linking pre-screen, self-assessment, control records, evidence packages, portfolio entries and registry/blueprint records. Target integration must make those links explicit.
- The source does not settle whether every toolkit reference is a physically copied document or a linked/derived view. Avoid two independently editable canonical copies.

## Cross-file dependencies

### Dependencies within this microbatch

- Registry and value documents jointly define the boundary between estate inventory/accountability and portfolio continuation/value decisions.
- Registry taxonomy and minimum capabilities feed the identity, owner, tier, tools, data, lifecycle and value fields collected by the self-assessment and pre-screen templates.
- Registry Blueprint references and Evidence Package manifest references are complementary: desired state and evidence/release state must remain separately identifiable.
- Behavioral analytics consumes registry identity/context (`agent_id`, tier, owner, deployment/version and runtime state) and can produce evidence linked to an Evidence Package or control record.
- The self-assessment can provide agent-level readiness material referenced by an Evidence Package; the Control Implementation Record can provide per-control implementation/effectiveness material referenced by the same package.
- The executive brief can summarize a portfolio, control or architecture decision, but its related ADR/assessment/experiment slots must point to the underlying records.

### Dependencies outside this microbatch

- Registry: `discovery-and-forecast.md`, `../lifecycle/README.md`, `../patterns/registry-and-blueprint.md`, `../../schemas/README.md`, `../governance/operating-model.md`, registry/blueprint schemas and examples, and registry/blueprint templates.
- Principles: `../governance/policy.md`.
- Behavioral analytics: `README.md`, `finops.md`, `../security/README.md`, `../patterns/runtime-observability-and-quarantine.md`, `../../templates/behavioral-analytics-use-case.md`, `../../schemas/audit-event.schema.json`.
- Value: fundamentals, adoption, operations and operating-model documents; `../operations/finops.md`, `../operations/kpi-kri-dashboard.md`, `../../templates/use-case-portfolio.md`, and the registry document.
- Evidence pattern: auditability and evaluations READMEs plus Registry and Blueprint, Control and Assurance Planes and Lifecycle Attestation and Sunset patterns.
- Risk pre-screen: risk-management README, Minimum Production Bar and framework implementation playbook.
- Self-assessment: governance policy, operating model, implementation playbook and schemas README.
- The control implementation record and executive brief templates have no source links; their consumers must provide the local evidence, authority and workflow contracts.

## Boundary classification

### Framework master chapters

- `docs/architecture/principles.md` → `docs/master/01-mandate-scope-and-principles.md`, preserving all 13 principles, decision questions, applications, antipatterns, validation procedure, tensions and policy relation.
- `docs/registry/README.md` and `docs/value/README.md` → `docs/master/03-portfolio-and-value.md`, preserving the distinction between Registry and Portfolio and retaining registry taxonomy/blueprint material alongside value/attribution material without merging the artifacts.
- `docs/operations/behavioral-analytics.md` → `docs/master/09-operations-incidents-and-continuity.md`, preserving calibration, context, response ladder, evidence, metrics, failure modes and the enforcement gate.

### Framework toolkit

- `docs/patterns/evidence-package-as-code.md` → `toolkit/patterns/evidence-package-as-code.md` as a vendor-neutral pattern.
- `docs/registry/README.md` may also yield `toolkit/registry/README.md` as a linked/derived reference, but it must not become a second independently authoritative policy.
- The four Markdown templates map to `toolkit/templates/` with all fields, tables, enums, caveats and placeholder semantics preserved.

### Optional implementation instantiation

- Risk pre-screen → `intake/risk-pre-screen.md`.
- Self-assessment → `assessments/self-assessment-form.md`.
- Control implementation → `controls/control-implementation-record.md`.

These are filled organizational records, not modified copies of the canonical toolkit templates. They require local agent/control IDs, owners, evidence, authority, dates, conditions, expiry and disposition.

### Executive communication

`templates/executive-brief-template.md` is toolkit communication scaffolding. It may summarize a concrete decision only after the referenced ADR/assessment/experiment and authority decision exist; it must not be promoted as policy or evidence by itself.

### Consulting and vendor boundary

No assigned source is a consulting package, pricing artifact or vendor endorsement. Evidence Package implementation mappings (Git + CI, artifact repository, GRC APIs, signed storage and attestation frameworks) remain directional examples only. The target must preserve vendor neutrality and must not present a mapping as certification, compliance evidence or required product architecture.

## Decisions requiring Rodgui before migration finalization

1. **Chapter 03 consolidation boundary:** confirm the exact clean-room arrangement for Registry and Portfolio content in chapter 03 and whether the toolkit registry reference is a derived view/link rather than a second editable authority.
2. **Cross-artifact gate vocabulary:** decide how target schemas link pre-screen routing, self-assessment disposition, control-record decision and Evidence Package release authority while preserving their distinct lifecycle meanings and enums.
3. **Behavioral analytics consumer and calibration contract:** identify the target evidence/control record that stores baseline version, monitor-only period, absolute floor, false-positive measurement, rule version and enforcement decision; do not infer these from the pattern alone.
4. **Template instantiation contract:** confirm which implementation-template repository consumes each toolkit template and which local fields/authorities provide evidence, expiry, exception and disposition semantics.
5. **Executive brief evidence threshold:** confirm the workflow that prevents a blank or expected-benefit brief from being treated as an approved decision, realized value claim or substitute for ADR/assessment/experiment evidence.

These decisions do not block this forensic batch. They block only silent target canonicalization or untraceable template instantiation.

## Validation evidence and exact completion counts

The generator completed with the following real output result:

- `expected_paths`: 9
- `file_records`: 9
- `markdown_headings_expected`: 98
- `heading_rows`: 98
- generated `micro-03b-files.jsonl` SHA-256: `24e275347bfdfbe0385ad81eafb30eca8d6fdc73a4338218519ee09f40cc3093`
- generated `micro-03b-headings.csv` SHA-256: `00ed4274a0de020ec770a8a2ba298884bf1ed5467297bc61fe26dd10b71905c6`

The independent pre-validation invariants passed: curation keys equal the manifest in order; records equal the manifest in order; all 26 required JSONL keys are present; all source commit/hash/byte/line values match; all reader identities are exact; all records are `reviewed`; the headings header is exact; all 98 heading identities and detailed subtrees match the mechanical heading index/source; preservation statuses are `mapped`; and no JSON flatten invariant applies because this manifest contains no JSON file.

Expected paths: 9  
File records: 9  
Markdown headings expected from `mechanical-heading-index.csv`: 98  
Heading rows produced: 98  
Blocked paths: 0  
Decision-required items: 5

# micro-03c

# Microbatch 03c migration relationships

Source snapshot: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot`  
Commit: `5545d9227624400ab8bb707b6032b2f61329a36e`  
Reader: `main:gpt-5.6-sol:micro-03c:2026-08-11`

## Coverage

- 11 paths read completely.
- 11 auditable file records generated.
- 79/79 Markdown headings reconciled exactly.
- 2 non-substantive placeholders justified.
- 0 validation errors, blocked paths or destination gaps.
- Validation evidence: `micro-03c-validation.json`.

## Fictitious T2 service-desk journey

The service-desk case preserves a complete G0–G7 traversal for an internal read-and-draft agent. It remains fictitious and proves only cross-artifact coherence—not effectiveness, proportionality across all tiers, real-estate enforcement or risk acceptance.

Key relations preserved:

- T2 and `permitted` are separate dimensions;
- capabilities are `observe` and `create`, but neither tool changes a system of record;
- no-write behavior is a release condition, not an intrinsic property;
- any new connector/state-changing tool returns to G4/G5;
- discovery status and confidence remain independent;
- model, source and tool are catalog-bound and CI-validatable;
- conditional release carries four owner/verifier/expiry-bound conditions;
- runtime must be observable, containable and reversible;
- lifecycle stage and operational state remain distinct;
- attestation/sunset and transition authority/evidence remain versioned.

The source case records three resolved divergences that remain historically important:

1. release decision/manifest mismatch corrected to `conditional` with four conditions;
2. schema previously treated a condition as an exception; target retains the semantic separation;
3. Release Authority role versus Example Design Authority deciding body was normalized.

A false waiver must not be created merely because a release is conditional.

## Control Catalog 1.1 source history

ADR-0005 remains archived as `superseded` by ADR-0010. Its measured source defects and decisions are retained:

- artificial 38-control/13-domain distribution;
- `automation: mixed` on all 38 records;
- T2 gap for gateway/kill switch;
- triplicated material-change requirement;
- duplicated ownership requirement;
- organizational capabilities incorrectly shaped as agent-tier controls;
- absent blocking/verification semantics and empty mappings.

Its 1.1 changes—scope, verification, blocking, model/lifecycle domains, T2 tool controls, single material-change source, five new controls, differentiated automation and public directional mappings—remain historical design rationale. The clean-room target derives current contracts from validated schema 2.0/catalog 1.2.0 artifacts. IDs remain stable, and paid ISO clauses are never invented.

## Responsible AI and assurance

Responsible AI remains broader than content filtering. The migrated chapter preserves:

- assurance-plane specialities;
- validity/reliability, safety, security/resilience, accountability/transparency, proportional explanation, privacy, fairness and human agency;
- ten impact-assessment questions;
- T1–T4 assurance floors and escalation triggers;
- useful but non-abusive transparency;
- context-derived slices, uncertainty and proxy/feedback-loop investigation;
- real human authority, contestability, correction and override evidence;
- full evidence, metrics and failure modes.

Tier minimum is a floor, not a ceiling. T3 gives Responsible AI veto at release; T4 requires formal challenge and executive residual-impact authority. `Independent assurance` is only claimed after institutional independence, conflicts, sampling, reporting and conclusion form are approved and demonstrated.

## Agent operating contracts

The source `AGENTS.md` is not mechanically copied into one repository. Its durable safeguards are adapted independently:

- hypotheses/experiments are not facts or standards;
- Accepted ADRs are superseded, never rewritten;
- evidence, interpretation, recommendation and decision stay separate;
- primary/dated sources, relative links and explicit limitations are required;
- vendors remain optional evidence/mappings/cases, never canonical dependencies;
- commercial packaging cannot redefine policy, controls or gates;
- examples remain fictitious;
- changes stay small, reversible, planned and validated.

The implementation template additionally prohibits real organizational data. The consulting repository will receive its own commercial-boundary contract.

## Safe schema migration

The 1.x→2.0 migration method preserves source records and forbids plausible invention:

1. keep 1.x immutable;
2. create a provenance-linked 2.0 copy;
3. apply deterministic mappings only;
4. mark missing fields pending;
5. validate schema;
6. human-review risk, admissibility, ownership and evidence;
7. only then change the active-version pointer.

Lifecycle stage, operational state, discovery status/confidence, risk tier and admissibility are independent. Historical transitions are not fabricated. Catalog entries precede blueprint bindings. T4 does not imply `restricted`, and `prohibited` cannot include production.

## Portfolio versus registry

The use-case portfolio answers whether an initiative should continue; registry answers what exists and who owns it. The template preserves sponsor, owner, tier/admissibility, expected/actual value, full cost, duplication and recorded decision. Agent count, adoption and token cost alone are not value evidence.

## Risk record

The risk template preserves:

- context and affected parties/assets;
- base/final T1–T4 tier and escalators;
- independent admissibility decision;
- scenario, inherent/residual risk and treatment;
- KRI/threshold/runbook/evidence;
- nine material-change triggers;
- `approve`, `condition`, `hold`, `reject` disposition;
- residual-risk authority and expiry;
- explicit rule that missing evidence is never guessed.

T4 is not a synonym for restricted, and risk acceptance never authorizes prohibited use.

## Runbook example

The fictitious support runbook links each signal to first action and escalation. It preserves evidence redaction, tool/session revocation, cause/correction, regression and dual Run/Design Authority evidence before reactivation. It does not replace an organization’s incident process, on-call model or legal obligations.

## Markdown linting

Source configuration is retained as provenance:

- MD013 disabled;
- MD024 applies to siblings only;
- MD025, MD033 and MD041 disabled.

The target will adopt only necessary exceptions after testing the actual corpus; lint weakening cannot be unexplained.

## Non-substantive paths

The following contain only `<!-- .gitkeep -->` and are omitted once real destination content exists:

- `assessments/maturity-assessments/.gitkeep`
- `docs/human-oversight/.gitkeep`

# micro-04

# Microbatch 04 migration relationships

Source snapshot: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot`  
Commit: `5545d9227624400ab8bb707b6032b2f61329a36e`  
Manifest: `control/micro-04.txt`

## Reading method and preservation

The main agent read every one of the 22 assigned files from first to last line with `read_file`. JSON schemas and examples were inspected property by property, including required fields, enums, patterns, IDs, versions, references and `if`/`then` conditions. `mkdocs.yml` was read through the final navigation item. The generated ledger embeds:

- exact full section text for every Markdown heading range;
- every scalar JSON pointer for each JSON file;
- every non-empty YAML line for `mkdocs.yml`;
- the complete license text;
- curated purpose, dependencies, source status, requirements, controls, decisions, exceptions and candidate destinations.

This report does not use file names, headings or snippets as substitutes for reading.

## Duplication and consolidation relationships

1. **Historical policy versus current modular corpus.** `docs/governance/ai-agent-policy-and-governance-v1.md` repeats topics now distributed across operating model, risk, lifecycle, architecture, operations and templates. It must be archived verbatim, while all unique definitions, conditions, thresholds, escalation rules, procedures and examples are mapped individually into the clean-room chapters. The historical tree and numbering do not become the target taxonomy.
2. **Operating model versus policy V1.** Both define Design Authority, Run Authority, Business Owner and Technical Owner. The maintained operating model adds Executive Sponsor, Governance Council, Domain Authorities, challenge/assurance conditions, decision-right evidence, forums, handoffs and formal segregation. Consolidation must preserve the union and treat the maintained model as the terminology anchor.
3. **Operating model versus Control and Assurance Planes pattern.** The pattern describes a technical/operational separation; the operating model establishes when review can be called independent. They are complementary. The target pattern must link to the institutional independence test so that a separate dashboard/workflow is not misrepresented as independent assurance.
4. **Risk-tiered pattern versus policy V1 blast-radius model.** The policy V1 uses Low/Medium/High and user-count examples; the maintained pattern uses T1–T4, multiple dimensions, red flags, evidence confidence and reclassification. Preserve V1 as history; target proportionality uses T1–T4 unless Rodgui decides to promote a historical threshold as a current default.
5. **Capability map versus maturity model.** The source explicitly says fifteen capabilities remain distinct because owners/processes/evidence differ, while ten maturity dimensions aggregate them for scoring. This is not a contradiction and must not be flattened into a one-to-one mapping.
6. **Pilot plan versus implementation journey.** Pilot is explicitly optional. A cohort, phased rollout or evidence from existing operations can satisfy the learning purpose. The target zero-to-BAU narrative must not turn a pilot into a universal gate.
7. **Data-access guidance versus implementation artifacts.** Chapter-level rationale and requirements belong in framework chapter 06; reusable contracts, schemas, controls and tests belong in the toolkit; organization-specific owner approvals, source records and attestations belong in the implementation template. This is a deliberate split without canonical duplication.
8. **Publication checklist versus self-assessment example.** The checklist defines the complete release disposition contract; the self-assessment example demonstrates a conditional T2 case. The example does not replace the checklist or constitute approval.
9. **Meeting Notes registry versus release manifest.** The registry references release `REL-MEETING-NOTES-001`; the release manifest references the same `agentId`, risk tier and blueprint version. Its declared blueprint SHA-256 was independently recomputed and matches `136924228729163b3ee503dd0880bb2556e98c22b093c4b73696de676d550085`.
10. **Model-provider catalog versus agent/tool catalogs.** It is a distinct governance object: provider/model/version admission, data-use boundaries, regions, risk tiers, evaluations, expiry and exit strategy. It must not be collapsed into the agent registry or enterprise tool registry.
11. **References index versus standards page.** The index states the general evidence rules; the standards page applies them specifically to protected ISO text. Keep one general research policy and one standards-scope/limitations record, linked rather than duplicated.
12. **MkDocs navigation versus clean-room target.** The source navigation mirrors the old handbook and cannot drive the new taxonomy. Preserve useful build behavior—Material theme, Mermaid, templates inclusion and relative-link strategy—but replace navigation with chapters 00–10 and the target toolkit/research/project sections.

## Differences and incompatibilities requiring controlled treatment

1. **Action-class vocabulary.** `schemas/enterprise-tool-registry.schema.json` uses `observe`, `create`, `modify`, `execute`, `approve`, `delete`, `delegate`; `templates/self-assessment-example.md` describes a tool capability as `read`. The target must either normalize the example to `observe` or version the taxonomy. This is a schema/taxonomy decision and cannot be harmonized silently.
2. **Control result vocabulary.** `examples/cases/meeting-notes-summarizer/release-manifest.json` uses `pass`; the self-assessment example uses `passed` and `conditional`. The applicable release/evidence schemas from other batches must determine the canonical enum. Do not normalize until reconciled with those contracts.
3. **Historical numeric thresholds.** Policy V1 includes examples or mandates involving `>100 users`, `≥10 users`, semiannual access review, annual training, 30-day PoC, five-business-day quarantine, 30-day regularization, monthly production audit, 70%/90% cost alerts and 90-day inactivity. The maintained tiered and lifecycle material treats several thresholds as context-dependent/calibrated. Preserve all numbers as historical content; promotion to current defaults requires an explicit policy decision.
4. **Lifecycle state semantics.** The maintained lifecycle separates lifecycle stage from operational state and distinguishes `suspended`, `quarantined` and retired/`disabled`. Any legacy single `status` or generic disable behavior must be migrated without erasing these distinctions.
5. **Schema host IDs.** Both schemas use `$id` under the current GitHub Pages URL. The new repository has no remote yet. The file contracts can be copied locally, but `$id` changes must wait for approved naming/publication and require compatibility handling.
6. **License boundaries.** The source is CC BY 4.0. The canonical framework can preserve that license and attribution, but the private consulting repository and reusable implementation template need explicit license/private-notice decisions before their initial commits.

## Explicit supersession, history and status

- The policy V1 file has no front matter or formal `supersedes` field. Repository-level instructions say the modular policy is the evolving canonical source and prior policies are history. Therefore this batch classifies V1 as historical but does not fabricate an ADR number or formal supersession relation.
- Maintained documents in this batch declare `supersedes: null`.
- The consulting roadmap contains unfinished checkboxes by design; these are product backlog, not missing canonical framework content.
- The standards page intentionally records a gap: no ISO clause-level mapping without licensed primary text.

## Gaps and unfinished material

- Consulting roadmap deliverables—interview/evidence packs, workshop guides, sample report, policy tailoring, effectiveness tests, runtime/tool packs and commercial validation—remain open backlog.
- The standards crosswalk remains concept-only for ISO until licensed standards are acquired/reviewed.
- `mkdocs.yml` contains current remote URLs that cannot be valid for the local-only target yet.
- The Meeting Notes release manifest references artifacts and schemas located in other microbatches; final validation must reconcile every reference after migration.
- The data-access playbook references Certified Source Catalog schema/example in other batches; destination integrity depends on their migration.

## Boundary classification

### Framework canônico

- data/access/provenance requirements and playbook;
- operating model and decision rights;
- capability map, optional pilot method and lifecycle;
- control/assurance and risk-tier patterns;
- schemas, fictitious examples, research rules and standards limitations;
- release checklist and experiment template;
- historical archive of policy V1.

### Consultoria privada

- all three packages, nine modules, buyer validation, packaging, pricing tests, delivery packs and commercial gate from `consulting/ROADMAP.md`.
- Consulting may reference the canonical release but must not copy the operating model, lifecycle, controls or data guidance as parallel canonical documents.

### Implementation template

- empty organizational records/instructions for data contracts, owner approval, release decision and self-assessment;
- only fictitious examples, never the source repository’s author/organization metadata as organization evidence.

## Decisions requiring Rodgui before migration finalization

1. **License/private notice per target repository:** preserve CC BY 4.0 for framework; choose treatment for consulting and implementation template.
2. **Canonical action taxonomy:** normalize narrative `read` to schema `observe`, or version/extend the schema explicitly.
3. **Historical thresholds:** decide whether any V1 numeric threshold becomes a current default, illustrative starting point, or archive-only value.

No decision is needed to continue reading. All three alternatives remain preserved and are blocked only from silent canonicalization.

## Completion counts

- Expected paths: **22**
- File records: **22**
- Markdown headings expected: **198**
- Heading rows produced: **198**
- Blocked paths: **0**
- Decision-required items: **3**

# micro-05

# Microbatch 05 migration relationships

Source snapshot: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot`  
Commit: `5545d9227624400ab8bb707b6032b2f61329a36e`  
Manifest: `control/micro-05.txt`

## Reading method and preservation

The main agent read all 22 assigned files from first to last line. This included the complete 520-line Pillow rendering script, every property and nested object in the Meeting Notes Blueprint 2.0 JSON, every table row and every Markdown section. The resulting records preserve exact source text by heading, every scalar JSON pointer and the full Python source plus every top-level AST unit. Curation adds purpose, status, dependencies, destination and conflicts; it does not replace the source content.

## Duplication, consolidation and dependency relationships

1. **Risk domain, Risk-Tiered pattern and MPB.** The risk domain defines T1–T4, red flags, fast path, admissibility, process, register and acceptance. The pattern from microbatch 04 abstracts proportional governance. The MPB operationalizes the minimum production conditions. They are three layers—normative model, reusable pattern and executable floor—not duplicates. Target chapter 04 explains the model; `toolkit/patterns/` and `toolkit/controls/minimum-production-bar.md` retain operational detail.
2. **Tool governance and Enterprise Tool Registry schema.** The domain defines the class taxonomy, MCP requirements, approval flow, build/runtime controls and gate. The schema from microbatch 04 constrains the structured catalog. Preserve both and bind documentation to schema validation; neither replaces the other.
3. **`read` versus `observe`.** Risk prose uses `read` as a natural-language operation. Tool governance explicitly defines the structured class `observe` as covering search/read/list/inspect. This is a documented mapping, not a schema contradiction. Structured records use `observe`; prose may say read when describing an operation.
4. **Registry and Blueprint pattern, Blueprint template and example.** The pattern defines why two objects exist; the template enumerates all human-review fields; the JSON example demonstrates a complete Blueprint 2.0. The target must preserve all three and validate the example against the migrated schema.
5. **Meeting Notes narrative and machine-readable records.** The narrative references registry, blueprint and release manifest and explains the T1 fast path. All share `agentId=meeting-notes-summarizer`, tier T1, admissibility permitted, capability observe and an automated policy gate. The narrative is explanatory; JSON files remain the machine-verifiable evidence example.
6. **Cases index and individual cases.** The index states why T1/T2/T3 cases exist, their limits and the need for cross-record invariants. It also records a previously detected cross-record contradiction as a methodological lesson. Individual cases must remain linked to validated artifacts.
7. **Operations and lifecycle.** Operations defines run readiness, observation, incident response, containment, reactivation, support and BAU. Lifecycle from microbatch 04 defines states/transitions, material change, attestation and retirement semantics. Consolidate into chapters 05 and 09 with cross-links; do not duplicate state definitions or omit operating procedures.
8. **Operations and behavioral analytics artifacts.** `docs/operations/README.md` provides the observability model and tells implementers to start monitor-only. The catalog example demonstrates rules with relative thresholds plus absolute floors; the use-case template captures hypothesis, data, bias, baseline, response, calibration, appeal and sunset. All thresholds in the example remain illustrative.
9. **Data-ready example and data domain.** `examples/certified-source-catalog.example.md` operationalizes the data-access guidance read in microbatch 04. Unknown classification is not low sensitivity; `conditional` carries restrictions; `not-ready` goes to a remediation backlog; certification expires and does not prove absence of shadow access.
10. **Manual bottleneck register and adoption/implementation.** The example supports sequencing of policy-as-code: automate evidence preparation broadly; automate decisions only after policy stabilizes and the risk supports it. It belongs with implementation/adoption examples, not as a universal automation threshold.
11. **SLO example and operations.** Availability targets do not override safety or authorization. Safety/security can trigger containment before an SLO breach, and material change triggers threshold reapproval.
12. **Adoption and governance charter.** The adoption domain turns rules into role-specific competence, support and feedback. The charter template establishes mandate, authorities, forums, exceptions and change control. The implementation repository will instantiate the charter; the framework toolkit retains the canonical template.
13. **Experiments README and experiment template.** The README defines non-canonical status, data/environment authorization, redaction, expiry and promotion conditions. The template from microbatch 04 captures reproducibility. Both move to `project/experiments/` and never become policy by proximity.
14. **Bibliography and source ledger.** Bibliography is a reading list. Claims must cite the source ledger and retain evidence cutoff, source class and vendor limitations. The target research layer must preserve that distinction.
15. **Deprecated Microsoft crosswalk.** The crosswalk is formally `deprecated` by ADR-0002 and explicitly not a normative source or mandatory backlog. Archive it verbatim for provenance. Any Microsoft case-study material stays optional research and cannot determine the clean-room target architecture.
16. **ADR-0006 and the new target.** ADR-0006 adopted source-framework release 1.0 and distinguished repository baseline adoption from organizational adoption. It is historical evidence, not authority to mark the new clean-room repository adopted. The new target requires its own release decision after validation.
17. **Spec task list versus source state.** `specs/002-.../tasks.md` remains `in-progress`, yet multiple listed artifacts exist in the snapshot. Archive the task list as historical planning; do not resurrect unchecked boxes as target backlog without reconciling `spec.md`, `plan.md`, `validation.md` and actual artifacts.

## Contradictions, dated claims and controlled corrections

1. **Infographic hardcoded counts are stale.** `render-agent-governance-infographic.py` says “38 controls em 13 domínios” and “10 patterns”; ADR-0006 records 43 controls and 15 domains for release 1.0, while the authoritative snapshot is a later release. The generated text must be derived from or updated against target artifacts before re-rendering. Preserve the source script in migration evidence, but do not publish the stale counts.
2. **Release-context counts are not snapshot counts.** ADR-0006’s 43 controls, four schemas and nine quality gates are evidence for the 2026-08-10 release decision. They must retain the date/release qualifier and cannot be described as current target facts.
3. **Vendor-scale metrics are scoped observations.** The Microsoft infographic variant includes `>100 mil` and `>500 mil` counts and explicitly says scopes are not directly comparable. Keep this only in an attributed case study with evidence cutoff, never as proof of effectiveness or framework scale.
4. **Historical policy gaps are not current normative gaps.** The deprecated Microsoft crosswalk describes V1 gaps such as blueprint, MCP and AI-ready data. Later source files implement those capabilities. Archive the crosswalk with status; do not re-open its P0/P1/P2 backlog automatically.
5. **Tool `create` semantics are explicit.** In structured taxonomy 1.0/2.0, persistent creation is state-changing. A transient model response is not tool class `create`. Target schemas, examples and prose must remain aligned.
6. **Framework adoption does not imply organizational adoption.** ADR-0006 explicitly rejects that inference. The implementation template must require a local authority, scope, exceptions and decision record for each organization.

## Explicit supersession, status and limitations

- Microsoft crosswalk: `deprecated`, preserved for traceability, not normative.
- ADR-0006: `accepted`, applies to source release 1.0 only.
- Spec task list: `in-progress` but treated as historical planning pending cross-file reconciliation.
- Maintained domain/pattern documents declare `supersedes: null`.
- All examples are fictitious/sanitized and do not demonstrate control effectiveness.
- Source release declared no controls exercised against a real estate; calibration remained hypothesis.
- ISO clause-level mappings were an explicit known gap.

## Gaps and follow-up validation

- Fetch and preserve the three Microsoft Inside Track articles not yet in the clean-room external corpus if their claims are retained: deployment/infrastructure, Responsible AI and Frontier Firm/adoption.
- Reconcile Blueprint JSON against `agent-blueprint.schema.json` and cross-record invariants after those schema files are migrated.
- Verify current OWASP URL/reference; the source URL may redirect to a newer Agentic Top 10 publication.
- Generate target infographics only after target controls/domains/patterns are final, then run deterministic rendering tests and visual inspection.
- Reconcile `specs/002` tasks with its spec, plan and validation files before deciding archive metadata.
- Preserve the absence of real-estate effectiveness evidence in the framework limitations until genuine evidence exists.

## Boundary classification

### Framework canônico

- chapters 04, 06, 08 and 09 content;
- MPB, registry/blueprint pattern, tool/MCP controls;
- Blueprint, charter and behavioral analytics templates;
- fictitious cases, SLO, source catalog and bottleneck examples;
- bibliography/research rules;
- local rendering tool after content correction and retest.

### Project/history in framework

- deprecated Microsoft crosswalk;
- source ADR-0006;
- source spec task list.

### Implementation template

- organization-instantiated governance charter, Blueprint, MPB assessment and behavioral analytics use case;
- values remain empty or fictitious and reference a specific framework release.

### Consultoria

No canonical content in this batch moves to consulting. Consulting may reference adoption, risk, MPB, tools and operations by framework release when defining module delivery, but must not duplicate them.

## Decisions requiring Rodgui

No new material decision is required to complete source reading for this batch. Stale counts, deprecated backlog and source-release adoption have deterministic preservation treatments. License/visibility remains a separate global decision already identified in microbatch 04 before repository initialization.

## Completion counts

- Expected paths: **22**
- File records: **22**
- Markdown headings expected: **189**
- Heading rows produced: **189**
- Blocked paths: **0**
- Decision-required items: **0**

# micro-06

# Microbatch 06 migration relationships

Source snapshot: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot`  
Commit: `5545d9227624400ab8bb707b6032b2f61329a36e`  
Manifest: `control/micro-06.txt`

## Reading and preservation method

The main agent read all 24 assigned files from first through final line. This included the complete 899-line Agent Blueprint 2.0 schema, the complete 202-line Certified Source Catalog schema, all JSON examples, the complete Unreleased/1.1.0/1.0.0 changelog, two ADRs, all Markdown sections, the GitHub Actions workflow and both `.gitkeep` placeholders. Generated records preserve every Markdown heading’s exact line range/text and every structured scalar/pointer; curation adds semantic purpose, dependencies, status, destination and transformation.

## Structural and dependency relationships

1. **CHANGELOG versus target history.** The source changelog records its own Unreleased, 1.1.0 and 1.0.0 evolution. Because the target is a physically independent clean-room repository, that history is preserved verbatim under `project/history/SOURCE_CHANGELOG.md`; the target root changelog starts a new lineage and links the imported history rather than pretending Git continuity.
2. **Roadmap versus migration goal.** Open source-roadmap checkboxes are evidence of snapshot gaps, not automatic target backlog. Each item must be reconciled against this complete reading, external research and the approved ten-area target. Its priority rules and definition of done remain substantive and migrate.
3. **ADR-0003.** The historical decision eliminates two unreconciled corpora by retaining one source of truth and deriving publications from it. The clean-room target preserves this rationale but creates its own boundary ADR; the old guide and old repository cannot determine the new taxonomy.
4. **ADR-0011.** This records adoption of source release 1.1.0, not adoption of the new target or of an organizational implementation. The frontmatter’s final `accepted` status is compatible with the evidence paragraph preserving the earlier approved→accepted transition condition.
5. **Pages workflow and ADR-0011.** GitHub Pages is optional and manually triggered by `workflow_dispatch`; build quality is mandatory but publication is not. The local Gate 1 does not execute this workflow, configure a remote or publish.
6. **Architecture diagram index and renderer.** The index separates vendor-neutral canonical imagery from Microsoft case-study imagery and references the deterministic renderer. The target preserves that boundary and regenerates imagery only after correcting stale source counts and validating the final target artifacts.
7. **Auditability and Evidence Package.** Auditability defines minimum events, event envelope, integrity/access, evidence-package properties, traceability, metrics and a release gate. It feeds chapter 07 for evidence/assurance and chapter 09 for operational auditability. It does not authorize indiscriminate logging; sensitive payloads are referenced/protected, and `missing` never becomes `passed`.
8. **Identity, tool governance and auditability.** Identity establishes attribution, least privilege, delegation and revocation; tool governance establishes action classes and enforcement; auditability preserves actor/agent/tool/policy correlation. All three are necessary for reconstructing authority and side effects.
9. **Identity tier table.** Labels such as `T1 — baixo` retain canonical T1–T4 IDs while adding prose. They are explanatory labels, not competing enum values.
10. **Security and MITRE/OWASP.** Security covers the full agent chain, abuse of legitimate authority, prevention, detection, containment and forensics. External mappings must be versioned and reviewed; they are not claims of equivalence or certification.
11. **Security, operations and auditability.** Prevention and trust-boundary design map to chapter 06; containment, quarantine, recovery and evidence continuity map to chapter 09; evaluation and red-team evidence map to chapter 07. The source text is split only with explicit cross-links.
12. **Federated operating-model pattern.** The pattern preserves domain authority while establishing common policy, registry, controls, evidence and handoffs. The `independent assurance` label is conditional on formal independence, conflicts, segregation, sampling, reporting line and conclusion form.
13. **90-day roadmap.** It is an accelerated tailoring pattern, not a Service-Level Agreement, compliance deadline, mandatory pilot or automatic gate progression. G0–G7 remain decisions based on authority and evidence; `hold`/`reject` forces replanning.
14. **Index/navigation.** The source index contains stage, persona and objective journeys plus knowledge layers. The target rebuilds navigation around the approved 00–10 master-document sequence while preserving audience decisions and the zero-to-BAU entry logic; it will not recreate a maze of competing canonical orders.
15. **Governance README.** Vendor mappings, cases, comparative assessments and consulting remain outside policy unless explicitly/versionedly incorporated. This boundary moves into target document control and framework README.
16. **Agent Registry example and Blueprint contract.** Registry 2.0 captures identity, ownership, lifecycle stage, operational state, risk/admissibility, blueprint reference, evidence, attestation and discovery. The linked Blueprint schema captures architecture, models, data, identity, tools, runtime and governance. They must validate as a cross-record bundle.
17. **Certified Source example and schema.** The JSON example uses two fictional certified entries and preserves owner, system of record, classification, purposes, risk tiers, region, connector, authorization, retention, evidence, review/expiry and restrictions. Schema status `conditional` additionally requires `conditionRefs`.
18. **Blueprint schema conditionals.** Production requires release evidence and attestation expiry and forbids `prohibited`; `conditional` requires condition references; `restricted` requires exception/expiry; T3/T4 state-changing tools cannot be automatically approved; `observe` is non-state-changing; create/modify/execute/approve/delete/delegate are state-changing; unpinned models require change detection/service-change policy; approved fallback requires catalog and equivalence evaluation.
19. **Charter and mandate evidence.** Suspension authority distinguishes an enforceable charter from intent. The first recorded decision using that authority—not the charter’s existence alone—demonstrates exercised mandate. Initial out-of-scope areas retain discovery and expiry.
20. **Handoff matrix.** A handoff needs a receiving owner and evidence. Quarantine is immediate; reactivation is evidence-bound; owner departure must reach the registry before the employment event. Illustrative SLAs are not target defaults.
21. **Risk assessment example.** `AGF-EVA-001` is a real source control ID. The example permits approved retrieval and draft creation while prohibiting system changes. Target wording must distinguish persistent draft creation from external system mutation.
22. **Capability worksheet.** Maturity score without evidence is hypothesis; coverage and confidence remain separate; targets must be necessary rather than aspirational; dependencies, observable gaps, acceptance criteria and BAU ownership are explicit.
23. **Spec 002.** The approved source spec explains release-1.1 alignment and non-goals. It is archived as release-specific source history rather than silently turned into target backlog.
24. **`.gitkeep` placeholders.** `docs/evaluations/.gitkeep` and `docs/tool-governance/.gitkeep` contain only `<!-- .gitkeep -->`; both are fully read and explicitly `non-substantive`. They are omitted once target directories contain real files.

## Contradictions and migration hazards

1. **Misleading `read-only` tag.** `examples/agent-registry.example.json` declares capabilities `observe` and `create` yet includes tag `read-only`. Structured taxonomy makes `create` state-changing when it persists state. The target preserves the source value in traceability but corrects/qualifies the migrated tag after validating the linked Blueprint and intended draft persistence.
2. **Historical count drift.** ADR-0003 describes a pre-absorption state with 38 controls/four schemas; release 1.0 records 43 controls; the snapshot roadmap records 44 controls, 15 domains, nine schemas and ten patterns. All counts retain release qualification. No historical count becomes a target claim.
3. **Source release versus target release.** ADR-0011 accepted release 1.1.0 after quality/release criteria. The target requires its own validation and release decision.
4. **Root changelog lineage.** Copying the old changelog into the new root without provenance would imply nonexistent Git continuity. The target therefore archives source history separately.
5. **Schema `$id` change.** Moving schemas changes canonical URLs. The target must choose and document compatibility aliases/migration before modifying `$id`; IDs, schema versions and field semantics cannot be silently changed.
6. **Roadmap state can be stale.** Open source checkboxes are observations at the source commit. Some may be closed by the new architecture or remain valid gaps; each requires explicit reconciliation.
7. **Workflow publication permissions.** `pages: write` and `id-token: write` are appropriate only for optional deployment. Local/build validation should use read-only permissions and must not trigger deployment.

## Declared gaps retained

- no calibration of controls against a real estate;
- thresholds/cadences are starting hypotheses, not benchmarks;
- ISO remains without control-to-control mapping;
- owner and editorial authority are concentrated;
- catalogs require adaptation to organizational systems of record;
- publication and real organizational adoption remain outside source-release proof.

## Boundary classification

### Framework canônico

- document-control/navigation boundaries;
- chapters 06, 07, 08 and 09 content;
- federated governance pattern;
- schemas, templates and fictional examples;
- optional manual documentation workflow after local validation.

### Project/history

- source changelog;
- source ADR-0003;
- source ADR-0011;
- source Spec 002.

### Implementation template

- blank/fictional Registry, Source Catalog, Charter, Handoff Matrix, Risk Assessment and Capability Assessment structures pinned to a framework release.

### Consulting

No canonical content in this batch is copied into consulting. Consulting may reference chapters/artifacts by framework release when defining modules and deliverables.

## Decisions requiring Rodgui

No new material decision blocks reading. Schema URL compatibility and downstream license/visibility must be decided before definitive repository initialization or public release, but all source content has a lossless provisional destination.

## Completion counts

- Expected paths: **24**
- File records: **24**
- Markdown headings expected: **215**
- Heading rows produced: **215**
- Non-substantive paths: **2**
- Blocked paths: **0**
- Decision-required headings: **0**

# micro-07

# Microbatch 07 migration relationships

Source snapshot: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot`  
Commit: `5545d9227624400ab8bb707b6032b2f61329a36e`  
Manifest: `micro-07.txt`  
Reader: `main:gpt-5.6-sol:2026-08-11`

## Coverage

- 26 source paths read completely from first to last line.
- 26 file records generated.
- 161 Markdown headings reconciled exactly against `mechanical-heading-index.csv`.
- 3 non-substantive placeholders classified with explicit justification.
- 0 hash, line-count, heading-content, destination or status errors.
- Validation evidence: `micro-07-validation.json`.

## Canonical architecture and policy

- `docs/architecture/overview.md` supplies the five-plane model, domain mapping, end-to-end flow, proportionality dimensions, boundaries and the eight-step runtime control-plane playbook. Its information is integrated primarily into master macroarea 6, with cross-links to mandate, assurance, operations and improvement.
- `docs/governance/policy.md` supplies the distinction between framework-release adoption and organizational policy adoption. It must survive explicitly: a framework release neither proves organizational adoption nor certification, audit or compliance.
- `docs/handbook/README.md` is an editorial ordering mechanism, not a second canonical source. The new handbook index must derive from the master chapters and domain material rather than maintain parallel prose.
- `docs/architecture/decisions/README.md` preserves the accepted/superseded state of all eleven source ADRs. Source ADRs remain provenance; the new repositories create their own decision sequence.

## Implementation journey

- `docs/guides/README.md` distinguishes the canonical G0–G7 method from optional or adaptable schedules.
- `docs/guides/implementation-program-24-weeks.md` is preserved as a tailoring pattern. Its F0–F6 phases do not override gate dependencies, and calendar completion never turns missing evidence into approval.
- The 24-week program preserves six workstreams, P0/P1/P2 backlog semantics, cross-domain dependency rules, cadence and the quarterly improvement loop.
- `docs/reference/artifact-catalog.md` maps implementation artifacts to purpose, typical owner and reference phase. An artifact counts only when it has an owner, minimum content and a consuming process.

## Evidence, lifecycle, cost and supplier governance

- `docs/auditability/evidence-pack-by-tier.md` and the Minimum Production Bar are two views of the same control floor. Divergence is a defect, not an acceptable nuance.
- The T1 fast path automates evidence generation; it does not remove any T1 evidence requirement.
- Missing mandatory evidence remains `missing` and can never be represented as `passed`.
- `docs/patterns/lifecycle-attestation-and-sunset.md` preserves approval expiry, material-change reassessment, quarantine, revocation, retention and orphan verification.
- `docs/operations/finops.md` requires cost per successful outcome, cost attribution by agent/owner/unit/use case, inclusion of human-supervision cost and quotas against denial-of-wallet. Cost optimization cannot weaken assurance.
- `templates/ai-vendor-contract-clauses.md` preserves all 25 clause identifiers and their tier minima. It remains a governance checklist, not legal advice; supplier refusal becomes declared risk with compensating control and competent authority.

## Structured contracts

- `schemas/agent-registry.schema.json` remains contract version `2.0`; it separates lifecycle stage from operational state and carries conditional production, evidence and attestation invariants.
- Registry risk tier remains `T1`–`T4`; admissibility remains `permitted`, `conditional`, `restricted` or `prohibited`.
- `schemas/audit-event.schema.json` remains `1.0` and deliberately excludes sensitive payload content while correlating identity, agent version, policy, tool action, outcome, redaction and evidence.
- `schemas/maturity-assessment.schema.json` remains `1.0`; score, confidence and coverage remain distinct. Referential integrity, reviewer separation, temporal rules and sampling bounds remain validator-enforced cross-field invariants.
- `schemas/release-evidence-manifest.schema.json` remains `1.0`; `prohibited` implies `rejected`, while a `conditional` decision requires conditions and expiry. A condition limits approved scope; an exception authorizes a governed deviation and must not be conflated with a condition.
- Schema IDs, enum values, regex patterns, required fields and conditional rules are immutable migration artifacts unless a separately approved versioned schema change is made.

## Fictitious example and implementation template

- `examples/cases/benefits-eligibility-triage/release-manifest.json` is a fictitious T3 conditional release record and is routed to the implementation template.
- Its five conditions preserve the human eligibility decision, appeal channel, per-model-version slice evaluation, exclusion of protected attributes/proxies from decision and logs, and automatic quarantine when a condition is lost.
- The six source control IDs and the recorded blueprint SHA-256 remain exact migration data. Any later correction requires a versioned example update, not silent rewriting.
- `examples/README.md` preserves the sanitization contract: fictitious names and providers, `.invalid` domains, no client outcomes, no universal threshold inference and no secrets or personal paths.

## Historical specifications

- `specs/001-handbook-consulting-product/tasks.md` and `specs/README.md` are archived with provenance.
- Completed and unchecked legacy tasks are historical state, not an automatically inherited backlog.
- A legacy specification approved technical/editorial scope only; it did not alter policy or risk appetite without competent authority.

## Templates and build support

- `templates/governance-raci-template.md` maps responsibility separately from authority, requires one accountable for each material decision and preserves segregation checks.
- `templates/study-note-template.md` retains an explicit evidence-versus-interpretation split.
- `requirements-ci.txt` preserves `jsonschema>=4.22,<5`, `Pillow==11.3.0` and `ruff==0.15.10` as the source validation baseline; dependency upgrades require a separate review.
- `tools/scripts/build-docs-site.py` must be adapted to the new canonical repository layout and tested. It must not publish the separate private consulting repository.

## Non-substantive paths

The following files contain only `<!-- .gitkeep -->` and are not migrated after their destination directories contain real material:

- `docs/architecture/diagrams/.gitkeep`
- `docs/identity/.gitkeep`
- `references/.gitkeep`

Their path, hash, one-line content and classification remain in the reading ledger.

## No silent resolution

- Source release/adoption statuses are not copied as adoption decisions of the rebuilt framework or any implementing organization.
- Schedules remain tailoring patterns.
- Schema-version changes require explicit versioning and migration guidance.
- Supplier clause wording remains subject to legal drafting.
- No remote, publication workflow or organizational data is introduced by this microbatch.

# micro-08

# Microbatch 08 migration relationships

Source snapshot: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot`  
Commit: `5545d9227624400ab8bb707b6032b2f61329a36e`  
Manifest: `micro-08.txt`  
Reader: `main:gpt-5.6-sol:2026-08-11`

## Coverage

- 25 paths read completely.
- 25 per-file records generated.
- 212 Markdown headings reconciled exactly.
- 3 non-substantive placeholders justified.
- 0 validation errors.
- Evidence: `micro-08-validation.json`.

## Governance and architecture

- `CONTRIBUTING.md` supplies the contribution workflow and conventions: small reviewable changes, relative links, accepted ADRs are superseded rather than rewritten, experiments do not become adopted patterns by assertion, kebab-case filenames and ISO dates.
- `docs/architecture/risks.md` supplies thirteen architecture risks and explicit review triggers. The risk register feeds master macroarea 6 and the continuous-improvement loop.
- `docs/executive/governing-agents-at-scale.md` supplies the executive decision case, five-plane recommendation, authority table, seven evidence questions, expected outcomes, risk mitigations, initial actions and success criteria. It explicitly does not promise return on investment, compliance or absence of incidents.
- `docs/executive/README.md` preserves the boundary between canonical executive communication and the separate personal consulting product.

## Superseded tier decision

- ADR-0004 is archived as `superseded` by ADR-0009.
- Its still-valid constraints are preserved in current guidance:
  - risk tiers remain T1–T4;
  - T0 in imported material maps into T1 under the stated mapping;
  - the T1 fast path automates policy decisions but never removes registration, ownership, logging, approved sources, terms or recoverable evidence;
  - red flags, escalators or impact triggers remove an agent from the fast path automatically.
- Historical counts — three schema enums, 38 controls and seventeen affected files — remain source-era measurements and are never presented as current target counts.

## Maturity and assessment

- `docs/guides/maturity-model.md` preserves levels 0–4, ten dimensions and the distinction among score, confidence and coverage.
- Maturity measures organizational capability. It is neither an agent risk tier nor a compliance score.
- The model deliberately avoids the label `independent assessment` unless engagement scope, conflicts, reporting line, incompatible services, sampling and conclusion form are formally governed.
- Conflicting evidence uses the lower demonstrated level with the conflict visible.
- Assessment comparisons require compatible method version, scope, cutoff, sampling and coverage.
- Average score is only a visual summary; median, range, dimensions below target, evidence confidence and blockers remain visible.
- The practical procedure preserves frozen scope and criteria, evidence request lists, multi-role interviews, no voting on scores, findings as observable conditions, dependency analysis, evidence-only challenge and an approved repeatable baseline.
- `templates/maturity-assessment-template.md` and `examples/maturity-assessment.example.json` remain aligned to schema and method version 1.0.
- The fictitious example’s sample, evidence IDs, scores, coverage, priorities and accepted-with-conditions disposition remain exact; it cannot support a claim about a real organization.

## Human oversight

- `docs/human-oversight/README.md` defines meaningful oversight as decision authority plus visibility, risk information, intervention, time, competence, independence and a recorded outcome.
- Modes remain human-in-command, human-in-the-loop, human-on-the-loop and human-out-of-the-loop, selected by risk and capability rather than interface preference.
- Generic `OK` is not informed approval.
- High-impact approval must show action, target, affected systems/data, consequence, irreversibility/rollback, rationale, warnings/conditions, deny/edit options and approver identity.
- Break-glass remains scoped, temporary, strongly identified, immediately alerted, retrospectively reviewed and automatically revoked.
- Contestability and redress remain operational requirements when applicable.

## Model and provider governance

- The governed unit remains:

  `provider × model × version × purpose × data class × region × controls`

- Catalog approval is contextual, not brand approval.
- Public provider benchmarks do not replace use-case evaluation.
- Model version change is potential material change and requires pre-rollout regression evidence.
- An unpinnable alias requires change detection and a service-change policy.
- Fallback is part of the governed surface; it must have equivalent controls or fail closed with documented rationale.
- Cost is measured per successful task/outcome with quality preserved, not per token alone.
- Critical dependencies require a tested exit strategy and reverse dependency lookup.

## Patterns and discovery

- `docs/patterns/README.md` preserves ten patterns, the quick-selection mapping, eleven antipatterns and sixteen mandatory pattern sections.
- Patterns remain maintained guidance until an implementing organization explicitly adopts them.
- `docs/registry/discovery-and-forecast.md` preserves the principle that an apparent zero state is usually low visibility.
- Discovery is continuous and multi-source; no individual source is complete.
- `discovery.status` and `discovery.confidence` are distinct and must never exchange enum values.
- `probable` and `suspected` objects remain owned remediation work rather than being discarded to improve metrics.
- Forecast sizes the governance system across scenarios and risk mix; it is not a contractual prediction.
- Automating evidence preparation is usually safer than automating unstable decisions.

## Canonical terminology

- `references/glossary.md` is preserved completely as the target glossary baseline.
- Every “do not confuse with” distinction remains substantive, including:
  - capability versus effective permission;
  - registry versus blueprint;
  - inventory versus reconciled registry;
  - risk tier versus admissibility;
  - maturity versus risk;
  - policy, standard, guidance, procedure, control objective and control;
  - control plane versus assurance plane;
  - kill switch versus circuit breaker;
  - telemetry versus evidence of value;
  - adoption versus creation volume.
- New incompatible terms must reference the canonical definition, explain contextual difference and propose a glossary change when permanent.

## Fictitious examples

- The Service Desk blueprint remains schema version 2.0, risk tier T2 and admissibility `permitted`.
- Its retrieval tool is observe/non-state-changing; draft creation is create/state-changing and requires human approval.
- Model fallback is fail closed; secret material is excluded from prompts/code; runtime includes correlation, quarantine, rollback and kill-switch references.
- The evaluation report’s forty synthetic questions, five slices, thresholds and results remain illustrative only and apply solely to the evaluated version/configuration.
- The release manifest is conditional with four expiring conditions and a recorded blueprint SHA-256.
- The RACI example preserves one accountable per material decision, immediate Run Authority containment, separate data/tool authorities and regression evidence before reactivation.
- The target maturity roadmap preserves non-uniform targets and dependency sequencing; low-confidence targets are hypotheses, not commitments.
- Canonical copies live under framework toolkit examples; derived fictitious instances seed the implementation template.

## Intake and taxonomy

- `templates/use-case-intake.md` is applied before the agent exists. Technology appears only after measurable problem, baseline and deterministic alternatives.
- “No agent needed,” deterministic implementation, consolidation with an existing case and refusal remain valid outcomes.
- Adoption is not outcome; total cost includes human supervision and assurance.
- `templates/agent-taxonomy-dictionary.md` allows only categories that alter a decision, control, metric or lifecycle.
- Operational definitions are tested on 20–30 cases by at least two independent evaluators. Systematic disagreement means the definition is weak.
- Unknown never defaults to the most benign value.

## Historical product specification

- `specs/001-handbook-consulting-product/spec.md` and `validation.md` are archived with provenance.
- Their useful requirements inform target coverage, but their superseded boundaries, source-branch diff checks and remote pull-request publication state do not automatically become current Gate 1 requirements.
- No historical `approved` or `in-progress` status changes the authority or release state of the rebuilt repositories.

## Non-substantive paths

- `assessments/technology-evaluations/.gitkeep`
- `docs/data-access/.gitkeep`
- `docs/risk-management/.gitkeep`

Each contains only `<!-- .gitkeep -->`; each remains represented by path, hash and justification but is not copied after substantive destination content exists.

# micro-09

# Microbatch 09 migration relationships

Source snapshot: `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot`  
Commit: `5545d9227624400ab8bb707b6032b2f61329a36e`  
Manifest: `micro-09.txt`  
Reader: `main:gpt-5.6-sol:2026-08-11`

## Coverage

- 28 paths read completely.
- 28 file records generated.
- 330 Markdown headings reconciled exactly.
- 5 non-substantive placeholders justified.
- 0 validation errors.
- Evidence: `micro-09-validation.json`.

## Landing page and foundations

- The source `README.md` is not copied mechanically. Its complete information is routed into the clean-room landing page, master document, navigation and provenance material.
- The new landing page preserves the study-versus-implementation distinction, problem statement, five planes, toolkit routes, non-negotiable principles, derived-publication rule, commercial boundary, limitations, license and attribution.
- Source claims that release 1.0 was `adopted` remain source history and do not set the release or adoption status of any new repository.
- `docs/fundamentals/README.md` is integrated into master macroarea 0 and preserves:
  - governance as a sociotechnical decision/control/evidence/accountability system;
  - full scope based on capability and impact rather than the “agent” label;
  - creation, discovery, adoption, use, quality and value as separate measures;
  - registry, blueprint, control, assessment and evidence package as distinct objects;
  - ten foundational principles;
  - value-to-retirement lifecycle;
  - complementary build-time and runtime controls;
  - distributed authority;
  - five-level evidence hierarchy;
  - the rule that conclusion strength cannot exceed evidence strength.

## Three-repository product boundary

- `consulting/README.md` and `consulting/consulting-engagement-model.md` migrate only into `ai-agent-governance-consulting`.
- The consulting repository will reference a pinned framework release instead of copying canonical controls, policy or method prose.
- Primary buyers remain C-level, Infrastructure/AIOps managers and AI/Infrastructure architects; domain functions participate according to scope.
- Packaging remains exactly three packages composed of nine modules:
  1. Readiness, Operating Model & Adoption — modules 1, 2 and 8;
  2. Policy, Controls & Lifecycle — modules 3, 4 and 5;
  3. Runtime, Tools & Evidence — modules 6, 7 and 9.
- Every module retains its problem, scope or prerequisites, activities, deliverables, acceptance criteria, indicative duration and exclusions.
- Indicative durations are not guarantees.
- The Limited-Scope Evidence Review remains explicitly not audit, certification, attestation, compliance opinion or independent assurance.
- Independent assurance cannot be claimed unless institutional capability, independence, conflicts, incompatible services, reporting line, sampling and conclusion form are formally defined, demonstrated and approved.
- Proposal structure retains thirteen mandatory sections and outcome-based engagement metrics. Workshop or page count is not a success metric.
- Secrets are represented only as `[REDACTED]`.

## Control catalog baseline

- `controls/README.md` documents source catalog version 1.2.0 against schema 2.0.
- All 44 source control IDs remain immutable migration identifiers pending an explicit versioned target decision.
- Source coverage is preserved exactly:
  - 44 controls total;
  - 40 agent-scope controls;
  - 4 organization-scope controls;
  - 27 blocking controls;
  - fifteen named domains.
- The approximately uniform distribution is explicitly identified as source editorial history, not evidence of real risk symmetry.
- Every control preserves ID, domain, scope, statement/rationale, type, owner, tier applicability, implementation patterns, objective verification, expected evidence, blocking behavior, metrics, automation and mappings.
- Evidence is the artifact; verification is the objective test. They must not be collapsed.
- Organization-scope versus agent/release-scope remains explicit.
- Application preserves the nine-step flow and distinct states:
  - `missing`;
  - `not-applicable`;
  - `planned`;
  - `implemented`;
  - `effective`;
  - `failed`;
  - `excepted`.
- `implemented` is not automatically `effective`.
- External mappings are declared directional alignment, not equivalence, compliance or attestation.
- ISO/IEC 42001, 23894 and 42005 remain unmapped because public overview material does not provide the paid normative clause text. No clause number will be invented.

## Capability-to-technology mapping

- The canonical framework preserves the method; the implementation template receives a neutral organization-specific mapping artifact.
- Mapping order remains:
  1. capability and control;
  2. existing systems of record;
  3. integration contract and source of truth per attribute;
  4. products only for remaining gaps;
  5. ADR for lock-in, centralized enforcement or trust-boundary change.
- Each attribute has exactly one authoritative system. Other systems consume or display it but do not redefine it.
- Conflicting values are findings; latest-timestamp reconciliation is prohibited because it destroys conflict evidence.
- Vendor roadmap coverage is not implemented-control coverage.

## Source decisions and publication

- ADR-0001 remains `superseded` by ADR-0002 and is archived.
- ADR-0002 remains accepted only in the source historical context. Its key principles are re-decided in a new target ADR reflecting three physically separate repositories.
- The byte-preserved Policy v1 and the modular source history are archived with provenance; they are not current authority in the clean-room target.
- ADR-0007 remains `superseded` by ADR-0008. Its strict staging, relative hierarchy, inspectable schemas/examples and derived navigation remain useful design rationale.
- Gate 1 creates no remote, configures no Pages setting and publishes nothing. Any future site or workflow requires a separate current decision and explicit Gate 2 authorization.
- `.gitignore` retains Python caches, virtual environment and generated staging/site exclusions, adapted to actual target outputs.

## Zero-to-BAU implementation method

- `docs/guides/framework-implementation-playbook.md` is preserved both in the master journey and a complete operational playbook.
- Nine workstreams remain explicit.
- Decision states remain `approve`, `condition`, `hold` and `reject`, each with required records.
- Every decision record retains gate ID, scope, version, tier, authority, participants, evidence references, state, rationale, conditions, expiry and next review.
- Missing evidence never equals approval.
- One person cannot build, approve and challenge the same artifact where segregation is required.
- G0–G7 retain complete entrance criteria, evidence, authority, exit criteria and failure/remediation contracts.
- Dependencies remain:
  - G0: none;
  - G1: G0;
  - G2: G1;
  - G3: G0 plus enough G2 to assign accountability;
  - G4: G2 and G3;
  - G5: G4 for the evaluated scope/version;
  - G6: G5;
  - G7: G6.
- G2 and G3 overlap legitimately; gate numbering is not a schedule.
- Runtime containment does not wait for committee approval.
- Reactivation requires cause and regression evidence.
- The final done criteria preserve reconciled ownership, tier-driven controls/authority, recoverable evidence, revocable identity/data/tools, action-linked signals, exercised quarantine/rollback/sunset, portfolio-changing attestation/value review, expiring exceptions and separate policy/guidance versioning.

## Developer experience and evaluations

- The paved road preserves the complete nine-step golden path from intake to sunset.
- Automation cannot hide decision rights or convert validation failure into implicit approval.
- Evaluation strategy preserves intended/prohibited use, personas/scenarios, dimensions, risk thresholds, dataset provenance, automated/human methods, adversarial/edge cases, slices, runtime metrics and promotion/rollback/sunset criteria.
- The pyramid remains data/test set → component → system/chain → outcome.
- Aggregate averages cannot compensate for a zero-tolerance red-flag failure.
- An LLM-as-judge is auxiliary evidence: rubric/version recorded, human calibration sampled, bias/instability measured and no sole high-impact authority.
- The release package, promotion flow, runtime evaluations, evidence, metrics and failure modes migrate completely.

## Patterns

- Human Accountability Boundary preserves five capability classes:
  - recommend;
  - prepare;
  - execute-bounded;
  - execute-material;
  - prohibited.
- Approval occurs before effect, outside the model, and is bound to action, target, consequence and approver identity. Transaction approval is not reusable by the agent.
- Tool and MCP Gateway preserves identity/context resolution, approved version, policy and argument validation, bounded credentials, egress/rate/budget/chain limits, approval, outcome logging, revocation and circuit breaking.
- The gateway cannot be treated as eliminating target/tool vulnerability and cannot remain an unmitigated single point of failure or compromise.

## Optional Microsoft case

- The Microsoft Customer Zero study migrates only to optional case-study references.
- All five Inside Track sources, five-plane synthesis, maturity progression, proportional matrix, AI-ready data, registry/blueprint/lifecycle, MCP controls and metrics remain available.
- The case is a primary institutional account of Microsoft’s declared approach, but also product communication.
- It is not independent audit, causal proof, return-on-investment evidence, universal architecture or required solution component.
- The figures exceeding 100,000 and 500,000 agents are not a comparable series without validated scope and definitions.
- Microsoft, Agent 365 and associated mappings can be removed without breaking policy, controls, schemas or gates.

## Navigation and evidence caveat

- `docs/start-here.md` preserves four decision-ending routes for sponsor, program, risk/compliance and architecture/platform.
- The playbook-first rule remains: the playbook supplies order while domain chapters supply content.
- Execution sequence remains baseline → design → foundations → one end-to-end real case → scale.
- Source text correctly states that its examples are fictitious and that its controls had not been exercised against a real estate. That caveat is retained as source-era evidence, not projected onto future target validation.

## Fictitious examples and template

- `examples/architecture.example.md`, `examples/enterprise-tool-registry.example.json` and `examples/release-decision.example.md` remain clearly fictitious.
- Canonical copies live in framework toolkit examples; derived instances seed the implementation template.
- The architecture preserves four trust boundaries and three failure boundaries.
- The tool registry preserves all three IDs, classes, state-change flags, allowed tiers/scopes, gateway and kill-switch references, provenance and expiry.
- The release decision stays aligned with its machine-readable manifest; a condition only in prose is explicitly insufficient.
- `templates/agent-registry-template.md` remains aligned with registry schema 2.0 and preserves lifecycle stage versus operational state, risk versus admissibility, discovery status versus confidence, blueprint hash and review checklist.

## Tooling documentation

- `tools/scripts/README.md` preserves the source baseline for deterministic 1800×2400 infographic rendering, vendored DejaVu fonts, alternate output directory, repository validator phases, negative guardrails, invariant checks, example/control/asset/security checks and product-boundary validation.
- Target tooling is adapted and tested independently per repository.
- The canonical framework build cannot include or publish the private consulting repository.

## Non-substantive paths

The following contain only `<!-- .gitkeep -->` and are not copied once substantive destination material exists:

- `assessments/.gitkeep`
- `assessments/comparison-matrices/.gitkeep`
- `controls/.gitkeep`
- `docs/executive/.gitkeep`
- `examples/.gitkeep`

Each remains represented by exact path, hash, content and justification in the reading ledger.

# micro-binary

# Binary and visual relationships

- Both PNGs are 1800×2400 RGB information graphics; the first is the source-era vendor-neutral overview and the second is an observed Microsoft case study. They must not be merged or assigned equal normative authority.
- The source-era framework PNG states `10 patterns`, `38 controls` and `13 domínios`; later source artifacts state 44 controls across 15 domains. The PNG is therefore preserved as historical visual evidence and redesigned from the final validated target catalog. Its old numbers must not be silently reused.
- The Microsoft visual remains optional vendor case-study evidence and retains its explicit caveat that the reported >100,000 and >500,000 agent figures are not directly comparable without scope and definition validation.
- Both DejaVu font files form one rendering asset set and depend on `tools/assets/fonts/LICENSE_DEJAVU`; preserve the notice with the binaries.
- No binary is blocked.

Expected paths: 4; file records: 4; Markdown headings expected/produced: 0/0; blocked: 0; fail-closed binary validation errors: 0. Validation evidence: `micro-binary-validation.json`.


## Colisões de destino

Veja `MIGRATION_LEDGER.csv` e o ledger de colisões no workspace de controle. Todas as colisões possuem estratégia explícita; nenhuma informação substantiva pode ser descartada por precedência silenciosa.

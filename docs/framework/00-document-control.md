---
title: 00 — Controle do documento
status: maintained
maturity: validated
last_reviewed: 2026-08-11
review_cycle: quarterly
owners: [framework-maintainers]
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# 00 — Controle do documento

Este capítulo integra a estrutura clean-room aprovada com o conteúdo substantivo do corpus autoritativo. Requisitos do framework são vendor-neutral; legislação externa, guidance, casos e histórico são identificados como tais. A implementação organizacional exige adoção formal pela authority competente e não decorre do versionamento deste repositório.

## Contrato operacional do capítulo

As subseções seguintes formam um contrato executável de completude. Cada uma especifica a decisão ou ação requerida, o record/evidence mínimo e uma condição observável de conclusão para levar a governança do zero ao business as usual.

### 00.1 Identification and purpose

**Required decision/action.** For **identification and purpose**, the organization must assign a stable document identifier and state the decision problem, audience and intended use.

**Record and evidence.** Record identifier, title, purpose, audience, normative status and repository location in document control.

**Done when.** A reader can distinguish this framework, its dependent products and its non-goals without relying on tribal knowledge.

### 00.2 Document owner and accountable authority

**Required decision/action.** For **document owner and accountable authority**, the organization must name one accountable authority and one operational custodian for the document.

**Record and evidence.** Record role, named delegate where applicable, authority source, contact route and succession rule.

**Done when.** Approval, interpretation, scheduled review and emergency change each have an unambiguous decision maker.

### 00.3 Approval status and normative force

**Required decision/action.** For **approval status and normative force**, the organization must declare whether the artifact is draft, approved, historical, informative or deprecated and what that status permits.

**Record and evidence.** Retain approval decision, approver, date, conditions, effective date and evidence of adoption.

**Done when.** No draft, case study or historical source can be mistaken for a current organizational requirement.

### 00.4 Version, effective date and review cycle

**Required decision/action.** For **version, effective date and review cycle**, the organization must version every material change and bind it to effective, review and supersession dates.

**Record and evidence.** Retain change description, author, approver, impacted contracts, migration action and prior-version reference.

**Done when.** Consumers can identify the applicable version and incompatible records are migrated, rejected or explicitly grandfathered.

### 00.5 Scope of application

**Required decision/action.** For **scope of application**, the organization must enumerate inclusions, exclusions, jurisdictions, lifecycle stages, organizational units and affected stakeholder classes.

**Record and evidence.** Retain a scope statement with boundary rationale, external obligations, delegated local standards and expiry for exclusions.

**Done when.** Intake can route every candidate as in scope, out of scope or decision required, with no implicit exemption.

### 00.6 Related policies, standards and records

**Required decision/action.** For **related policies, standards and records**, the organization must map this framework to superior policies, subordinate standards and local procedures without creating a second canonical source.

**Record and evidence.** Record relationship type, owner, version, conflict rule and the exact requirement or decision linked.

**Done when.** A conflict resolves through an approved precedence rule and downstream artifacts can be impact-assessed on change.

### 00.7 Change, consultation and approval process

**Required decision/action.** For **change, consultation and approval process**, the organization must route material changes through impact analysis, affected-function consultation and approval.

**Record and evidence.** Retain proposal, rationale, consulted roles, objections, compatibility result, decision and migration plan.

**Done when.** Accepted decisions are superseded rather than silently rewritten and affected dependents receive a traceable update.

### 00.8 Distribution, access and retention

**Required decision/action.** For **distribution, access and retention**, the organization must define who may read, change and retrieve the record, for how long and under which legal hold or deletion rule.

**Record and evidence.** Record classification, access groups, custodian, retention trigger, minimum period, disposition and audit retrieval path.

**Done when.** Authorized evidence is retrievable within the required time and expired data is disposed of without breaking required lineage.

### 00.9 Interpretation and conflict resolution

**Required decision/action.** For **interpretation and conflict resolution**, the organization must define the authority and escalation route for ambiguous, conflicting or locally inapplicable requirements.

**Record and evidence.** Retain question, competing interpretations, consulted authorities, interim restriction and final disposition.

**Done when.** Delivery teams do not resolve material ambiguity by convenience and the ruling is propagated to affected records.

### 00.10 Revision history

**Required decision/action.** For **revision history**, the organization must version every material change and bind it to effective, review and supersession dates.

**Record and evidence.** Retain change description, author, approver, impacted contracts, migration action and prior-version reference.

**Done when.** Consumers can identify the applicable version and incompatible records are migrated, rejected or explicitly grandfathered.


## Conteúdo canônico incorporado

A seção preserva integralmente as unidades atribuídas pela matriz de cobertura. Os marcadores HTML são provenance machine-readable e não alteram o significado normativo.

### Fonte: `docs/governance/policy.md`

Commit de origem: `5545d9227624400ab8bb707b6032b2f61329a36e`.

<!-- source-unit {"classification": "metadata-title", "end_line": "2", "index": 1, "source_field": "title", "source_heading": "", "source_path": "docs/governance/policy.md", "start_line": "2", "transformation": "synthesize-and-preserve", "unit_type": "frontmatter-title"} -->
**Título controlado na origem:** AI Agent Governance Policy — fonte canônica modular

<!-- source-unit {"classification": "concept-or-structure", "end_line": "19", "index": 2, "source_field": "", "source_heading": "AI Agent Governance Policy — fonte canônica modular", "source_path": "docs/governance/policy.md", "start_line": "18", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
### AI Agent Governance Policy — fonte canônica modular

<!-- source-unit {"classification": "concept-or-structure", "end_line": "23", "index": 3, "source_field": "", "source_heading": "Propósito", "source_path": "docs/governance/policy.md", "start_line": "20", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Propósito

Este repositório é a fonte modular a partir da qual a **policy final de governança de IA e agentes** será mantida, revisada e versionada. A policy não é um documento monolítico nem depende de uma plataforma específica: ela é composta por princípios, decision rights, requisitos, controls, evidências e regras de lifecycle distribuídos em módulos canônicos.

<!-- source-unit {"classification": "definition", "end_line": "31", "index": 4, "source_field": "", "source_heading": "Dois níveis de adoção", "source_path": "docs/governance/policy.md", "start_line": "24", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Dois níveis de adoção

A **release 1.0 deste framework está `adopted`** desde 2026-08-10, conforme a [ADR-0006](../../project/decisions/source-history/0006-framework-release-1-0-adoption.md). Isso significa que esta versão é a baseline canônica estável e que mudança normativa passa a exigir proposta, rationale, authority, changelog e release versionada.

Isso **não** significa que qualquer organização adotou esta policy. A adoção organizacional é uma decisão separada: cada organização declara esta baseline como sua policy interna pela sua própria authority competente, com escopo, exceções e obrigações próprias. Enquanto essa decisão não existir, o conteúdo é referência técnica canônica do framework — não a policy vigente daquela organização.

Confundir os dois níveis transforma versionamento em declaração de conformidade. Nenhum claim de certificação, auditoria independente ou conformidade decorre da adoção da release.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "46", "index": 5, "source_field": "", "source_heading": "Composição da policy", "source_path": "docs/governance/policy.md", "start_line": "32", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Composição da policy

A policy canônica deste framework é formada por:

1. [princípios arquiteturais](01-mandate-scope-and-principles.md);
2. [operating model e decision rights](02-governance-and-accountability.md);
3. [arquitetura em cinco planos](06-architecture-and-technical-controls.md);
4. [gestão proporcional de riscos](04-risk-impact-and-compliance.md);
5. domínios canônicos de identidade, dados, tools, segurança, Responsible AI, oversight, evaluations, auditabilidade, operações, adoção e valor;
6. [control catalog](../../toolkit/controls/README.md);
7. [implementation playbook e decision gates](08-implementation-and-adoption.md);
8. schemas e evidence packages que tornam os requisitos verificáveis.

O [handbook](../handbook/README.md) define a ordem editorial desses módulos, sem duplicá-los.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "61", "index": 6, "source_field": "", "source_heading": "Conteúdo não normativo", "source_path": "docs/governance/policy.md", "start_line": "47", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Conteúdo não normativo

Não integram a policy, salvo incorporação explícita e versionada:

- estudos de caso e explicações em `docs/explanations/`;
- crosswalks e avaliações comparativas em `assessments/`;
- fontes e referências externas em `references/`;
- exemplos fictícios em `examples/`;
- roadmap, specs e experimentos;
- calendários de 90 dias/24 semanas e o plano opcional de piloto;
- mappings de fornecedores;
- a camada comercial em `consulting/`.

Esses artefatos podem informar decisões, mas não criam dependência tecnológica nem requisito normativo por associação.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "67", "index": 7, "source_field": "", "source_heading": "Neutralidade de fornecedor", "source_path": "docs/governance/policy.md", "start_line": "62", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Neutralidade de fornecedor

A policy define **capabilities, outcomes, controls, evidências e boundaries**, não produtos obrigatórios. Fornecedores e plataformas nomeados podem aparecer como fonte, caso observado ou mapping opcional. Nenhum deles é componente necessário do framework ou condição para conformidade com a policy.

Um mapping deve poder ser removido sem alterar princípios, controls, decision gates, schemas ou a arquitetura canônica.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "78", "index": 8, "source_field": "", "source_heading": "Evolução e versionamento", "source_path": "docs/governance/policy.md", "start_line": "68", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Evolução e versionamento

Mudanças normativas devem:

1. declarar o requisito alterado e sua justificativa;
2. registrar decisão e authority;
3. atualizar controls, evidências e impactos operacionais;
4. preservar versões anteriores;
5. incluir changelog e migration guidance quando necessário;
6. passar pelos quality gates do repositório antes de release.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "85", "index": 9, "source_field": "", "source_heading": "Origem histórica", "source_path": "docs/governance/policy.md", "start_line": "79", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Origem histórica

A [AI Agent Policy and Governance v1](../../project/history/ai-agent-policy-and-governance-v1.md) foi o ponto inicial deste trabalho. Ela é preservada byte a byte para rastreabilidade histórica, mas não é usada como fonte normativa recorrente do framework modular.

O guia externo "Governança de Agentes de IA em Escala", mantido anteriormente como documento independente, também é **origem histórica**. Seu conteúdo procedural foi absorvido por este repositório conforme a [ADR-0003](../../project/decisions/0001-canonical-source-and-product-boundaries.md), reescrito no formato canônico. Cópias daquele documento não são normativas e podem conter taxonomia divergente: a conversão para T1–T4 e a separação de `Restricted` como admissibilidade seguem a [ADR-0009](../architecture/decisions/0009-risk-tier-and-admissibility.md).

Este repositório é a **fonte única e final**. Qualquer publicação em outro formato deve ser derivada destes módulos, nunca mantida como cópia editorial independente.

## Acceptance criteria

- todas as decisões deste capítulo possuem authority, owner e evidência recuperável;
- requisitos aplicáveis estão ligados ao catálogo de controles e ao método de verificação;
- exceções têm escopo, justificativa, compensating controls, expiry e decisão residual;
- controles de build time e runtime são distinguidos e exercitados quando aplicáveis;
- mudanças materiais reabrem avaliação, aprovação e evidência;
- nenhuma alegação de conformidade, eficácia ou valor excede a evidência observada.

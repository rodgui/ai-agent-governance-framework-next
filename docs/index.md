---
title: Índice por persona e objetivo
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-13
review_cycle: quarterly
related:
  - start-here.md
  - handbook/README.md
  - ../README.md
---

# Índice por persona e objetivo

Esta página é uma **referência de localização**, não uma segunda ordem de implantação. Se você precisa colocar o programa em movimento, use [Comece aqui](start-here.md). Se quer estudar o corpus de forma linear, use o [handbook](handbook/README.md). Volte a este índice quando já souber a pergunta que precisa responder.

## Como usar este índice

Escolha primeiro o objetivo ou a persona. Leia somente os documentos necessários para a decisão corrente e abra os templates, schemas, controls e exemplos indicados no ponto de execução. Não é necessário seguir todas as jornadas nem ler todos os capítulos.

## Por estágio da organização

| Situação atual | Próxima pergunta | Documentos principais |
|---|---|---|
| **Ainda não há programa formal** | Quem tem autoridade para começar e qual é o boundary? | [Brief executivo](executive/governing-agents-at-scale.md) → [Mandato](framework/01-mandate-scope-and-principles.md) → [Comece aqui](start-here.md) |
| **Há pilotos ou agentes dispersos** | O que existe, qual é o risco e quais fundações faltam? | [Baseline e capability map](framework/08-implementation-and-adoption.md) → [Inventário](framework/03-inventory-portfolio-and-value.md) → [Risco](framework/04-risk-impact-and-compliance.md) |
| **Há operação em escala** | A evidência, o runtime e o valor continuam dentro do envelope aprovado? | [Control catalog](../toolkit/controls/README.md) → [Assurance](framework/07-evaluation-evidence-and-assurance.md) → [Operações](framework/09-operations-incidents-and-continuity.md) → [Métricas](framework/10-metrics-review-and-improvement.md) |

## Por persona

### Sponsor, conselho ou executivo

**Decisão:** patrocinar, definir escopo, nomear governance owner, aprovar appetite e autoridade de contenção.

1. [Brief executivo](executive/governing-agents-at-scale.md)
2. [Mandato, escopo e princípios](framework/01-mandate-scope-and-principles.md)
3. [Governança e accountability](framework/02-governance-and-accountability.md)
4. [Estratégia, inventário e valor](framework/03-inventory-portfolio-and-value.md)
5. [Comece aqui — Trilha 0](start-here.md)

> **Template recomendado:** [Governance Charter](../toolkit/templates/governance-charter-template.md), com [exemplo](../toolkit/examples/governance-charter.example.md).

### Governance owner, transformação ou programa

**Decisão:** definir baseline, target maturity, workstreams, backlog, gates e critérios de completude.

1. [Implementation playbook](framework/08-implementation-and-adoption.md)
2. [Catálogo de artefatos](../toolkit/artifact-catalog.md)
3. [Maturity model](../toolkit/maturity/maturity-model.md)
4. [Capability assessment worksheet](../toolkit/templates/capability-assessment-worksheet.md)
5. [Handbook](handbook/README.md), para aprofundamento linear

> **Templates recomendados:** [Maturity Assessment](../toolkit/templates/maturity-assessment-template.md), [RACI](../toolkit/templates/governance-raci-template.md) e [Handoff Matrix](../toolkit/examples/handoff-matrix.example.md).

### Risco, Responsible AI, privacy, jurídico ou compliance

**Decisão:** classificar risco, separar admissibilidade, acionar impact assessment, definir reviews e aceitar residual risk.

1. [Policy modular](framework/00-document-control.md)
2. [Risco, impacto e compliance](framework/04-risk-impact-and-compliance.md)
3. [Governança e accountability](framework/02-governance-and-accountability.md)
4. [Avaliação, evidência e assurance](framework/07-evaluation-evidence-and-assurance.md)
5. [Control catalog](../toolkit/controls/README.md)

> **Regra de leitura:** `T1–T4` responde à criticidade; `permitted`, `conditional`, `restricted` e `prohibited` respondem à admissibilidade. Consulte a [ADR-0009](architecture/decisions/0009-risk-tier-and-admissibility.md).
>
> **Templates recomendados:** [Risk pre-screen](../toolkit/templates/risk-pre-screen.md), [Risk Scoring Worksheet](../toolkit/templates/risk-scoring-worksheet.md), [Agent Risk Record](../toolkit/templates/agent-risk-record.md) e [Impact Assessment](../toolkit/templates/assessment-template.md).

### Arquitetura, plataforma, IAM, dados ou segurança

**Decisão:** definir control plane, source of truth, identity, data, tools, model/provider, enforcement e runtime.

1. [Arquitetura e controles técnicos](framework/06-architecture-and-technical-controls.md)
2. [Design patterns](patterns/README.md)
3. [Registry](../toolkit/registry/README.md)
4. [Schemas](../toolkit/schemas/README.md)
5. [Casos de referência](../toolkit/examples/cases/README.md)

> **Templates e contratos recomendados:** [Agent Registry](../toolkit/templates/agent-registry-template.md), [Agent Blueprint](../toolkit/templates/agent-blueprint-template.md), [registry schema](../toolkit/schemas/agent-registry.schema.json) e [blueprint schema](../toolkit/schemas/agent-blueprint.schema.json).

### Product owner, maker ou engenharia

**Decisão:** decidir se um agente é o mecanismo certo, classificar o caso, criar blueprint, avaliar, liberar e operar.

1. [Comece aqui — Trilha 3](start-here.md)
2. [Inventário, portfólio e valor](framework/03-inventory-portfolio-and-value.md)
3. [Risco, impacto e compliance](framework/04-risk-impact-and-compliance.md)
4. [Arquitetura e controles técnicos](framework/06-architecture-and-technical-controls.md)
5. [Avaliação, evidência e assurance](framework/07-evaluation-evidence-and-assurance.md)
6. [Adoção e suporte](framework/08-implementation-and-adoption.md)

> **Templates recomendados:** [Use-case intake](../toolkit/templates/use-case-intake.md), [Self-assessment](../toolkit/templates/self-assessment-form.md), [Agent Blueprint](../toolkit/templates/agent-blueprint-template.md) e [Release Evidence Manifest](../toolkit/templates/release-evidence-manifest.md).

### Operações, SOC, suporte ou SRE

**Decisão:** observar, conter, investigar, reativar, mudar ou aposentar com evidência.

1. [Operações, incidentes e continuidade](framework/09-operations-incidents-and-continuity.md)
2. [Arquitetura e controles técnicos](framework/06-architecture-and-technical-controls.md), especialmente runtime e containment
3. [Lifecycle de agentes](framework/05-agent-lifecycle.md)
4. [Avaliação, evidência e assurance](framework/07-evaluation-evidence-and-assurance.md)
5. [Métricas, revisão e melhoria](framework/10-metrics-review-and-improvement.md)

> **Templates recomendados:** [Support Runbook](../toolkit/examples/support-runbook.example.md), [SLO](../toolkit/examples/slo.example.md), [Attestation and Sunset Record](../toolkit/templates/attestation-sunset-record.md) e [Sunset Plan](../toolkit/templates/sunset-plan.md).

### Auditoria, assurance ou challenge

**Decisão:** verificar design, operação, evidence, segregação, findings e remediação sem assumir o papel do owner.

1. [Control catalog](../toolkit/controls/README.md)
2. [Avaliação, evidência e assurance](framework/07-evaluation-evidence-and-assurance.md)
3. [Schemas](../toolkit/schemas/README.md)
4. [Maturity model](../toolkit/maturity/maturity-model.md)
5. [Fontes e limitações](../research/sources/bibliography.md)

> **Templates recomendados:** [Control Implementation Record](../toolkit/templates/control-implementation-record-template.md), [Evaluation Report](../toolkit/examples/evaluation-report.example.md) e [Release Decision](../toolkit/examples/release-decision.example.md).

## Por objetivo

| Objetivo | Rota curta |
|---|---|
| Definir policy, mandate e accountability | [Controle do documento](framework/00-document-control.md) → [Governança](framework/02-governance-and-accountability.md) → [Governance Charter](../toolkit/templates/governance-charter-template.md) |
| Decidir se o caso precisa de agente | [Inventário e valor](framework/03-inventory-portfolio-and-value.md) → [Use-case intake](../toolkit/templates/use-case-intake.md) |
| Inventariar agentes e resolver ownership | [Descoberta e registry](framework/03-inventory-portfolio-and-value.md) → [Registry](../toolkit/registry/README.md) → [Registry schema](../toolkit/schemas/agent-registry.schema.json) |
| Classificar risco e admissibilidade | [Risco](framework/04-risk-impact-and-compliance.md) → [Risk Scoring Worksheet](../toolkit/templates/risk-scoring-worksheet.md) → [Agent Risk Record](../toolkit/templates/agent-risk-record.md) |
| Avaliar impacto e Responsible AI | [Impact assessment](framework/04-risk-impact-and-compliance.md#2-avaliacao-de-impacto-responsible-ai) → [Assessment template](../toolkit/templates/assessment-template.md) |
| Definir arquitetura e enforcement | [Arquitetura técnica](framework/06-architecture-and-technical-controls.md) → [Patterns](patterns/README.md) → [Blueprint schema](../toolkit/schemas/agent-blueprint.schema.json) |
| Governar identidade, dados e tools/MCP | [Arquitetura técnica](framework/06-architecture-and-technical-controls.md) → [Control catalog](../toolkit/controls/README.md) |
| Liberar com evidência | [Assurance](framework/07-evaluation-evidence-and-assurance.md) → [Minimum Production Bar](../toolkit/controls/minimum-production-bar.md) → [Release Evidence Manifest](../toolkit/templates/release-evidence-manifest.md) |
| Operar, conter e recuperar | [Operações](framework/09-operations-incidents-and-continuity.md) → [Runtime pattern](../toolkit/patterns/runtime-observability-and-quarantine.md) |
| Revisar valor, custo e continuidade | [Métricas](framework/10-metrics-review-and-improvement.md) → [Portfolio](../toolkit/templates/use-case-portfolio.md) → [Sunset Plan](../toolkit/templates/sunset-plan.md) |
| Estudar um caso completo | [Casos de referência](../toolkit/examples/cases/README.md) → [P1–P8 no playbook](framework/08-implementation-and-adoption.md) |

## Camadas do conhecimento

O repositório distingue quatro camadas. A camada **normativa** contém policy, standards, controls e decisões aprovadas. A camada **arquitetural** descreve capabilities, boundaries, operating model e patterns. A camada **operacional** fornece procedures, schemas, templates, checklists e evidence packages. A camada **explicativa** apresenta rationale, exemplos, estudos de caso e fontes.

Um guidance não altera a policy. Um template acelera a produção do artefato, mas não aprova o caso. Um exemplo fictício demonstra coerência do método, mas não comprova eficácia. Um mapping externo registra alinhamento direcional, não conformidade.

## Navegação por áreas

| Área | Índice |
|---|---|
| Arquitetura e decisões | [`docs/architecture/`](architecture/README.md) |
| Executivo | [`docs/executive/`](executive/README.md) |
| Handbook | [`docs/handbook/`](handbook/README.md) |
| Patterns | [`docs/patterns/`](patterns/README.md) |
| Referência | [`docs/reference/`](reference/README.md) |
| Research | [`research/`](../research/README.md) |
| Toolkit | [`toolkit/`](../toolkit/README.md) |

A ordem canônica de estudo permanece no [handbook](handbook/README.md); esta página existe para localizar e agir.

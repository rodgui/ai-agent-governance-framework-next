---
title: Índice e jornadas de leitura
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - handbook/README.md
  - ../README.md
---

# Índice e jornadas de leitura

O repositório usa documentos modulares como fonte canônica. Escolha uma jornada; não é necessário ler tudo em sequência.

> **Vai implantar?** Use as [trilhas de leitura](start-here.md), que dão uma ordem só e terminam em decisões. Esta página é referência para localizar assuntos — ela oferece muitos caminhos de propósito, e isso atrapalha quem precisa de um.

## Por onde começar, conforme o estágio da organização

As jornadas por persona respondem "o que eu leio". Esta tabela responde antes: **por onde a organização entra**.

| Estágio | Entrada recomendada | Por quê |
|---|---|---|
| **sem programa formal** | [brief executivo](executive/governing-agents-at-scale.md) → [decisão arquitetural](framework/03-inventory-portfolio-and-value.md) → [descoberta do estate](framework/03-inventory-portfolio-and-value.md) → [capability map](framework/08-implementation-and-adoption.md) | não comece comprando ferramenta; comece por escopo, estate e mandato |
| **com pilotos em andamento** | [maturity model](../toolkit/maturity/maturity-model.md) → [gestão de riscos](framework/04-risk-impact-and-compliance.md) → [Minimum Production Bar](../toolkit/controls/minimum-production-bar.md) | descubra os gaps e defina o piso de controles antes de escalar o que já existe |
| **já operando em escala** | [control catalog](../toolkit/controls/README.md) → [evidence pack por tier](framework/07-evaluation-evidence-and-assurance.md) → [catálogo de artefatos](../toolkit/artifact-catalog.md) | use os domínios como modelo de auditoria e o catálogo como índice de completude |

Os únicos gates canônicos são G0–G7. O [programa de 24 semanas](framework/08-implementation-and-adoption.md), o roadmap de 90 dias e o plano de piloto são recortes adaptáveis do mesmo conjunto de gates — não programas concorrentes nem prazos de compliance.

## Jornada por persona

### Conselho, executivo ou sponsor

**Objetivo:** decidir mandato, apetite a risco, funding e accountability.

1. [Brief executivo](executive/governing-agents-at-scale.md)
2. [Fundamentos](framework/01-mandate-scope-and-principles.md)
3. [Estratégia e valor](framework/03-inventory-portfolio-and-value.md)
4. [Operating model](framework/02-governance-and-accountability.md)
5. [Maturity model](../toolkit/maturity/maturity-model.md)

**Decisões esperadas:** sponsor, escopo, risk appetite, autoridade de contenção e critérios de valor.

### CISO, DPO, jurídico, compliance ou Responsible AI

**Objetivo:** definir controles, assurance, exceções e evidências.

1. [Policy modular](framework/00-document-control.md)
2. [Gestão de riscos](framework/04-risk-impact-and-compliance.md)
3. [Segurança](framework/06-architecture-and-technical-controls.md)
4. [Responsible AI](framework/04-risk-impact-and-compliance.md)
5. [Human oversight](framework/02-governance-and-accountability.md)
6. [Auditabilidade](framework/07-evaluation-evidence-and-assurance.md)
7. [Control catalog](../toolkit/controls/README.md)

**Decisões esperadas:** triggers de assessment, risk acceptance, human approval, retenção, monitoramento e waiver.

### Arquitetura e plataforma

**Objetivo:** construir o control plane e integrar os sistemas especializados.

1. [Arquitetura de referência](framework/06-architecture-and-technical-controls.md)
2. [Design patterns](patterns/README.md)
3. [Estate, registry e taxonomia](../toolkit/registry/README.md)
4. [Identidade](framework/06-architecture-and-technical-controls.md)
5. [Dados](framework/06-architecture-and-technical-controls.md)
6. [Tools e MCP](framework/06-architecture-and-technical-controls.md)
7. [Modelos e provedores](framework/06-architecture-and-technical-controls.md)
8. [Schemas](../toolkit/schemas/README.md)

**Decisões esperadas:** source of truth, blueprint, workload identity, gateways, enforcement points e adapters por plataforma.

### Product owner, maker ou engenharia

**Objetivo:** levar um agente da hipótese à operação com evidência suficiente.

1. [Implementation playbook](framework/08-implementation-and-adoption.md)
2. [Roadmap sugestivo de 90 dias](framework/08-implementation-and-adoption.md)
3. [Risk pre-screen](../toolkit/templates/risk-pre-screen.md)
4. [Evaluations](framework/07-evaluation-evidence-and-assurance.md)
5. [Adoção e suporte](framework/08-implementation-and-adoption.md)
6. [Templates](../toolkit/templates/README.md)
7. [Examples](../toolkit/examples/README.md)
8. [Publication checklist](../toolkit/templates/release-decision-checklist.md)

**Decisões esperadas:** escopo, risco, dados, tools, evals, release, rollback e sunset.

### Operações, SOC, suporte ou SRE

**Objetivo:** observar comportamento e executar resposta proporcional.

1. [Operações](framework/09-operations-incidents-and-continuity.md)
2. [Auditabilidade](framework/07-evaluation-evidence-and-assurance.md)
3. [Lifecycle, mudança material e retirement](framework/05-agent-lifecycle.md)
4. [Runtime observability and quarantine pattern](../toolkit/patterns/runtime-observability-and-quarantine.md)
5. [Lifecycle attestation and sunset pattern](patterns/lifecycle-attestation-and-sunset.md)
6. [Sunset plan](../toolkit/templates/sunset-plan.md)

**Decisões esperadas:** SLOs, alertas, incident severity, quarantine, reactivation, attestation e retirement.

### Auditoria, assurance e challenge

**Objetivo:** verificar design, operação e evidência sem assumir o papel do owner nem presumir independência não demonstrada.

1. [Control catalog](../toolkit/controls/README.md)
2. [Maturity model](../toolkit/maturity/maturity-model.md)
3. [Auditabilidade](framework/07-evaluation-evidence-and-assurance.md)
4. [Assessment templates](../toolkit/templates/README.md)
5. [Fontes e limitações](../research/sources/bibliography.md)

**Decisões esperadas:** suficiência de evidência, grau de segregação/independência quando aplicável, findings, prazo de remediação e attestation.

### Consultor ou líder de transformação

**Objetivo:** conduzir diagnóstico, target state, roadmap e transferência de capacidade.

1. [Handbook](handbook/README.md)
2. [Implementation playbook](framework/08-implementation-and-adoption.md)
3. [Programa sugestivo de 24 semanas](framework/08-implementation-and-adoption.md)
4. [Plano opcional de piloto](framework/08-implementation-and-adoption.md)
5. [Maturity model](../toolkit/maturity/maturity-model.md)
6. [Design patterns](patterns/README.md)
7. [Toolkit](../toolkit/templates/README.md)

**Decisões esperadas:** baseline, gaps, target operating model, backlog priorizado, entregáveis e critérios de aceite.

## Jornada por objetivo

| Objetivo | Documentos principais |
|---|---|
| definir policy e accountability | [Policy modular](framework/00-document-control.md) + [operating model](framework/02-governance-and-accountability.md) |
| inventariar agentes | [Estate e registry](../toolkit/registry/README.md) + [descoberta e forecast](framework/03-inventory-portfolio-and-value.md) + [schemas](../toolkit/schemas/README.md) |
| decidir se o caso pede um agente | [Decisão arquitetural](framework/03-inventory-portfolio-and-value.md) + [intake](../toolkit/templates/use-case-intake.md) |
| mapear capacidades atuais e alvo | [Capability map](framework/08-implementation-and-adoption.md) + [maturity model](../toolkit/maturity/maturity-model.md) |
| planejar artefatos, owners e fases | [Catálogo de artefatos](../toolkit/artifact-catalog.md) + [programa de 24 semanas](framework/08-implementation-and-adoption.md) |
| classificar risco e admissibilidade | [Risk-tiered governance](../toolkit/patterns/risk-tiered-governance.md) + [risk management](framework/04-risk-impact-and-compliance.md) + [Agent Risk Record](../toolkit/templates/agent-risk-record.md) |
| governar identidade e dados | [Identity](framework/06-architecture-and-technical-controls.md) + [data access](framework/06-architecture-and-technical-controls.md) |
| governar tools e MCP | [Tool governance](framework/06-architecture-and-technical-controls.md) + [MCP gateway pattern](patterns/tool-and-mcp-gateway.md) |
| governar modelos e provedores | [Model governance](framework/06-architecture-and-technical-controls.md) + [evaluations](framework/07-evaluation-evidence-and-assurance.md) |
| governar mudança e retirement | [Lifecycle](framework/05-agent-lifecycle.md) + [lifecycle pattern](patterns/lifecycle-attestation-and-sunset.md) |
| publicar com evidência | [Evaluations](framework/07-evaluation-evidence-and-assurance.md) + [control catalog](../toolkit/controls/README.md) + [release manifest](../toolkit/templates/release-evidence-manifest.md) |
| operar e conter | [Operations](framework/09-operations-incidents-and-continuity.md) + [runtime pattern](../toolkit/patterns/runtime-observability-and-quarantine.md) |
| medir maturidade | [Maturity model](../toolkit/maturity/maturity-model.md) + [assessment example](../toolkit/examples/maturity-assessment.example.json) |
| medir portfólio e valor | [Strategy and value](framework/03-inventory-portfolio-and-value.md) + [lifecycle pattern](patterns/lifecycle-attestation-and-sunset.md) |
| estruturar adoção e suporte | [Adoption](framework/08-implementation-and-adoption.md) + [operations](framework/09-operations-incidents-and-continuity.md) |
| estudar um caso Microsoft opcional | [Customer Zero case](../research/case-studies/microsoft-customer-zero-agent-governance.md) + [crosswalk histórico](../project/history/assessments/microsoft-case-study-framework-crosswalk.md) |
| ver o framework aplicado ponta a ponta | [Casos de referência](../toolkit/examples/cases/README.md) + [implementation playbook](framework/08-implementation-and-adoption.md) |
| seguir uma leitura linear | [Handbook](handbook/README.md) |

## Navegação por pasta

O handbook e as jornadas acima são a leitura orientada. Quem prefere navegar a estrutura direto no repositório encontra um índice curto em cada pasta:

| Pasta | Índice |
|---|---|
| arquitetura | [`docs/architecture/`](architecture/README.md) — visão, princípios, atributos de qualidade, riscos, diagramas e decision log |
| executivo | [`docs/executive/`](executive/README.md) — conteúdo orientado a decisão |
| governança | [`docs/governance/`](framework/00-document-control.md) — policy modular e operating model |
| guias | [`docs/guides/`](journey/README.md) — playbook, roadmaps e piloto |
| referência técnica | [`docs/reference/`](reference/README.md) — glossário, catálogo de artefatos e checklist de autossuficiência |
| fontes | [`references/`](../research/README.md) — regras de proveniência, ledger de fontes e bibliografia |

Esses índices existem para navegação de pasta e não constituem uma segunda ordem editorial. A ordem canônica é a do [handbook](handbook/README.md).

## Camadas do conhecimento

- **Normativo:** policy modular e decisões formalmente aprovadas.
- **Arquitetural:** princípios, operating model, boundaries e patterns.
- **Operacional:** playbooks, controls, schemas, templates e checklists.
- **Explicativo:** rationale, casos, mappings e referências.

Um documento de guidance não altera a policy. Um estudo de caso não comprova eficácia causal. Um mapping de fornecedor não redefine o núcleo.

A produtificação comercial pessoal está separada em [`consulting/`](../project/decisions/0001-canonical-source-and-product-boundaries.md). Ela reutiliza o conhecimento canônico, mas não integra estas camadas nem redefine a policy.

## Leitura completa

Para leitura linear, use o [handbook](handbook/README.md). A geração de uma publicação fica para uma etapa futura, quando o conteúdo estiver maduro.

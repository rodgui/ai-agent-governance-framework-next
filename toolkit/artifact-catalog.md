---
title: Catálogo de artefatos do programa
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-18
review_cycle: quarterly
supersedes: null
related:
  - ../docs/framework/08-implementation-and-adoption.md
  - ../docs/handbook/README.md
  - templates/README.md
  - examples/README.md
  - schemas/README.md
---

# Catálogo de artefatos do programa

## Objetivo

Índice consolidado dos artefatos de uma implantação, com **propósito, owner típico e wave de implementação**. Serve para planejamento, atribuição de responsabilidade e controle de completude — não para leitura sequencial.

A definição, o procedimento e o exemplo de cada artefato ficam no domínio correspondente. Aqui está a visão de programa: o que precisa existir, sob responsabilidade de quem e em que momento.

A coluna `Typical implementation wave` referencia as waves W0–W6 do [programa de 24 semanas](../docs/framework/08-implementation-and-adoption.md), que é **pattern de referência, não calendário normativo**. A wave organiza planejamento; a decisão continua sendo expressa pelos gates G0–G7 no playbook e nos decision records, sem duplicar uma coluna de gate neste catálogo. Owner típico é ponto de partida, não prescrição: cada organização mapeia para as próprias funções.

## Mandato e diagnóstico

| Artefato | Para que serve | Owner típico | Typical implementation wave | Onde está |
|---|---|---|---|---|
| Governance charter | mandato, escopo e authority do programa | sponsor + governança | W0 | [template](templates/governance-charter-template.md) · [exemplo](examples/governance-charter.example.md) |
| Scope statement | fronteira do programa e exclusões com prazo | governança + arquitetura | W0 | [exemplo](examples/governance-charter.example.md) |
| Princípios de decisão | critérios que orientam escolhas recorrentes | arquitetura + risco | W0 | [princípios arquiteturais](../docs/framework/01-mandate-scope-and-principles.md) |
| Governance forums ToR | mandato, decision rights e cadência de cada fórum | presidência do fórum | W0/W2 | [template](templates/governance-forum-tor.md) |
| Agent estate inventory | baseline de agentes com confiança declarada | governança + plataforma | W1 | [descoberta e forecast](../docs/framework/03-inventory-portfolio-and-value.md) |
| Agent estate forecast | projeção de volume e mix de risco | governança + FinOps | W1 | [descoberta e forecast](../docs/framework/03-inventory-portfolio-and-value.md) |
| Manual bottleneck register | onde a governança depende de trabalho repetitivo | gestão do programa | W1 | [exemplo](examples/manual-bottleneck-register.example.md) |
| Capability map | capacidades atuais versus alvo, em 15 capacidades | arquitetura | W1 | [capability map](../docs/framework/08-implementation-and-adoption.md) · [worksheet](templates/capability-assessment-worksheet.md) |
| Maturity assessment report | maturidade evidenciada com confidence e coverage | arquitetura + governança | W1 | [maturity model](maturity/maturity-model.md) · [template](templates/maturity-assessment-template.md) · [schema](schemas/maturity-assessment.schema.json) |

## Operating model e risco

| Artefato | Para que serve | Owner típico | Typical implementation wave | Onde está |
|---|---|---|---|---|
| Target maturity roadmap | evolução de capacidades com dependências | sponsor do programa | W2 | [exemplo](examples/target-maturity-roadmap.example.md) |
| Operating model | papéis, decision rights, fóruns e handoffs | governança | W2 | [operating model](../docs/framework/02-governance-and-accountability.md) |
| RACI de governança | accountable único por decisão material | governança + owners | W0/W2 | [template](templates/governance-raci-template.md) · [exemplo](examples/governance-raci.example.md) |
| Handoff matrix | transições com pré-condição, evidência e SLA | gestão do programa | W2 | [exemplo](examples/handoff-matrix.example.md) |
| Risk classification standard | tiers, escaladores, red flags e admissibilidade | risco + segurança | W2 | [gestão de riscos](../docs/framework/04-risk-impact-and-compliance.md) · [ADR-0009](../docs/architecture/decisions/0009-risk-tier-and-admissibility.md) |
| Use-case intake | problema, baseline e hipótese de valor | negócio + governança | W2 | [template](templates/use-case-intake.md) |
| Agent use-case portfolio | priorizar investimento, detectar duplicidade e medir valor | portfolio owner | W2/W4 | [template](templates/use-case-portfolio.md) · [estratégia e valor](../docs/framework/03-inventory-portfolio-and-value.md) |
| Risk pre-screen | roteamento rápido e acionamento de escaladores | governança | W2 | [template](templates/risk-pre-screen.md) |
| Risk scoring worksheet | sete dimensões de scoring + red flags → tier e reviews | governança + risco | W2 | [template](templates/risk-scoring-worksheet.md) |
| Agent risk record | tier, admissibilidade, residual risk e authority por agente | risco + owners | W2/W3 | [template](templates/agent-risk-record.md) |
| Impact assessment | impactos sobre pessoas, mitigações e residual | Responsible AI + risco | W2 | [Responsible AI](../docs/framework/04-risk-impact-and-compliance.md#2-avaliacao-de-impacto-responsible-ai) |
| Approval e publication workflow | gates por tier e por gatilho | governança + plataforma | W2/W3 | [decision gates](../docs/framework/08-implementation-and-adoption.md) · [checklist](templates/release-decision-checklist.md) |

## Fundações técnicas

| Artefato | Para que serve | Owner típico | Typical implementation wave | Onde está |
|---|---|---|---|---|
| Agent registry data standard | schema, obrigatoriedade por tier e quality rules | governança + plataforma | W3 | [registry](registry/README.md) · [schema](schemas/agent-registry.schema.json) · [template](templates/agent-registry-template.md) |
| Agent taxonomy e metadata dictionary | classificação canônica e normalização por plataforma | governança + arquitetura | W2/W3 | [template](templates/agent-taxonomy-dictionary.md) |
| Agent blueprint | desired state machine-readable por versão, com bindings governados | arquitetura + plataforma | W3 | [schema](schemas/agent-blueprint.schema.json) · [template](templates/agent-blueprint-template.md) |
| Agent lifecycle standard | estados, transições, dormancy e retirada | plataforma + governança | W3 | [lifecycle](../docs/framework/05-agent-lifecycle.md) |
| Identity e access standard | modo de identidade, autorização e JML | IAM | W3 | [identidade](../docs/framework/06-architecture-and-technical-controls.md) |
| AI-ready data standard | critérios de certificação de fonte | governança de dados | W3 | [dados](../docs/framework/06-architecture-and-technical-controls.md) |
| Certified source catalog | fontes aprovadas com restrições e revisão | governança de dados | W3 | [schema](schemas/certified-source-catalog.schema.json) · [exemplo](examples/certified-source-catalog.example.md) |
| Data remediation backlog | fontes legítimas que ainda não passam | owners de dados | W3+ | [exemplo](examples/certified-source-catalog.example.md) |
| Tool, API e MCP governance standard | classificação por ação e mediação | segurança + API | W3 | [tools e MCP](../docs/framework/06-architecture-and-technical-controls.md) |
| Enterprise tool registry | catálogo de ferramentas com proveniência e escopo | plataforma + API | W3 | [schema](schemas/enterprise-tool-registry.schema.json) · [exemplo](examples/enterprise-tool-registry.example.json) |
| Model e provider governance standard | critérios, versão, fallback e saída | plataforma de IA | W3 | [modelos e provedores](../docs/framework/06-architecture-and-technical-controls.md) |
| Approved model/provider catalog | combinações permitidas por classe de dados | plataforma de IA | W3 | [schema](schemas/model-provider-catalog.schema.json) · [exemplo](examples/model-provider-catalog.example.json) |
| Reference architecture | planos, fluxos e pontos de enforcement | arquitetura corporativa | W2 | [arquitetura de referência](../docs/framework/06-architecture-and-technical-controls.md) · [exemplo](examples/architecture.example.md) |
| Multi-control-plane arbitration ADR | precedence, authority, conflict path, correlation e fail-safe entre planos | arquitetura + governança | W2/W3 | [ADR-0015](../docs/architecture/decisions/0015-multi-control-plane-arbitration.md) · [pattern](patterns/multi-control-plane-governance.md) |
| Multi-agent delegation contract ADR | topologia, delegation edges, authority attenuation, limits, expiry, revocation e failure propagation | arquitetura + segurança + plataforma | W2/W3 | [ADR-0013](../docs/architecture/decisions/0013-multi-agent-delegation-contract.md) · [pattern](patterns/multi-agent-delegation-governance.md) · [template](templates/agent-delegation-contract.md) · [exemplo](examples/supervisor-worker-delegation.example.md) |
| AI-native observability profile ADR | task, delegation, model, retrieval, policy, tool, memory, containment, cost, value e privacy | operação + observabilidade + assurance | W2/W3 | [ADR-0014](../docs/architecture/decisions/0014-ai-native-observability-profile.md) · [pattern](patterns/ai-native-observability-profile.md) · [template](templates/ai-native-observability-profile.md) · [exemplo](examples/ai-native-observability.example.md) · [operational drill](examples/ai-native-observability-operational-drill.example.md) |
| Implementation-plan hierarchy ADR | classificação entre plano de domínio, plano integrado de capítulo e roadmap de programa | governança editorial + arquitetura | W2 | [ADR-0012](../docs/architecture/decisions/0012-implementation-plan-hierarchy.md) |
| Control-plane interaction matrix | capability, source of truth, enforcement, fallback e evidence por plano | arquitetura + plataforma | W3 | [pattern](patterns/multi-control-plane-governance.md) · [exemplo](examples/multi-control-plane-conflict.example.md) |
| Orchestrator Technology Evaluation | pattern fit, placement/authority, capabilities, operability, economics, evidence e exit risk | arquitetura + governança + plataforma | W2/W3 | [assessment](assessments/technology-evaluations/orchestrator-evaluation.md) |
| ADR promotion readiness assessment | readiness técnica, gaps de evidência e reviewers para promoção das ADRs 0013, 0014 e 0015 | arquitetura + governança + assurance | W2/W3 | [assessment](assessments/adr-promotion-readiness-0013-0014-0015.md) |
| Orchestrator Decision and Exit Record | topologia, capabilities, authority, lock-in, portability, resilience e saída | arquitetura + governança + plataforma | W2/W3 | [template](templates/orchestrator-decision-exit-record.md) · [exemplo](examples/orchestrator-decision-exit-record.example.md) · [substitution/replay](examples/orchestrator-substitution-replay.example.md) |
| Capability-to-technology mapping | qual sistema existente responde por cada capability, com source of truth por atributo | arquitetura corporativa | W2/W3 | [método de mapeamento](../docs/framework/06-architecture-and-technical-controls.md) |
| Decisão arquitetural por caso | agente é o mecanismo certo? | arquitetura | W2 | [árvore de decisão](../docs/framework/03-inventory-portfolio-and-value.md) |

## Assurance, runtime e valor

| Artefato | Para que serve | Owner típico | Typical implementation wave | Onde está |
|---|---|---|---|---|
| Minimum production bar | piso de controles por tier e gate de admissibilidade | governança + plataforma | W3 | [MPB](controls/minimum-production-bar.md) |
| Evidence pack standard | composição do pacote por tier e release | assurance | W3 | [evidence pack por tier](../docs/framework/07-evaluation-evidence-and-assurance.md) |
| Release evidence manifest | manifesto verificável do que sustentou o release | assurance + plataforma | W3/W4 | [schema](schemas/release-evidence-manifest.schema.json) · [template](templates/release-evidence-manifest.md) |
| Audit event standard | evento auditável com correlação e integridade | plataforma + assurance | W3 | [schema](schemas/audit-event.schema.json) · [exemplo](examples/audit-event.example.json) |
| Security standard | baseline secure-by-design para agentes | segurança | W3 | [segurança](../docs/framework/06-architecture-and-technical-controls.md) |
| Threat e abuse case library | cenários de teste adversarial | segurança | W3/W4 | [segurança](../docs/framework/06-architecture-and-technical-controls.md) |
| AgentSecOps runbook pack | contenção, quarentena e recuperação | operação de segurança | W4 | [operações](../docs/framework/09-operations-incidents-and-continuity.md) · [exemplo](examples/support-runbook.example.md) |
| Observability standard | schema de telemetria e correlação | SRE + plataforma | W3 | [operações](../docs/framework/09-operations-incidents-and-continuity.md) · [SLO de exemplo](examples/slo.example.md) |
| Behavioral analytics catalog | detecções, thresholds e modo de operação | analytics + SRE | W4/W5 | [behavioral analytics](../docs/framework/09-operations-incidents-and-continuity.md) · [template](templates/behavioral-analytics-use-case.md) |
| FinOps standard | custo por resultado, budget e quota | FinOps | W4/W5 | [FinOps](../docs/framework/10-metrics-review-and-improvement.md) |
| Governance dashboard specification | KPIs, KRIs e audiências | governança + SRE | W4/W5 | [KPIs e KRIs](../docs/framework/10-metrics-review-and-improvement.md) |
| Business value scorecard | outcomes contra baseline declarado | negócio + portfólio | W4 | [estratégia e valor](../docs/framework/03-inventory-portfolio-and-value.md) |
| Attestation e sunset record | revalidação, dormancy e retirada evidenciadas | governança + plataforma | W5 | [lifecycle](../docs/framework/05-agent-lifecycle.md) · [template](templates/attestation-sunset-record.md) · [sunset plan](templates/sunset-plan.md) |
| Plano da rota de validação | como a implantação será validada ponta a ponta | gestão do programa | W4 | [plano de piloto](../docs/framework/08-implementation-and-adoption.md), quando a rota escolhida for piloto |
| Role-based enablement plan | currículo por papel e rede de champions | change lead | W4/W5 | [adoção](../docs/framework/08-implementation-and-adoption.md) |

## Como usar para controle de completude

Um artefato **existe** quando tem owner nomeado, conteúdo mínimo e é referenciado por quem o consome. Documento produzido e não consumido por nenhum processo é dívida, não entrega.

Duas leituras úteis:

- **por fase** — o que precisa existir antes do próximo gate;
- **por owner** — quantos artefatos uma mesma função acumula. Se uma função concentra muitos, ou o escopo dela está errado ou o programa vai gargalar nela.

A segunda leitura é a que costuma revelar o problema antes dele acontecer.

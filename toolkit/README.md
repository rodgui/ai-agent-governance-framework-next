---
title: Toolkit de execução
status: maintained
owner: framework-maintainers
last_reviewed: 2026-08-13
review_cycle: quarterly
related:
  - ../docs/start-here.md
  - artifact-catalog.md
---

# Toolkit de execução

O toolkit transforma o framework em artefatos verificáveis. Ele não substitui os capítulos canônicos: os capítulos explicam **por que decidir** e **o que exigir**; o toolkit oferece o contrato, o template, o pattern, o exemplo ou a evidência para materializar a decisão.

> **Comece pelo [catálogo de artefatos](artifact-catalog.md) se você já sabe em que fase está.** Use esta página quando a dúvida for qual superfície do toolkit resolve sua necessidade.

## Escolha o objeto correto

| Objeto | Use quando precisa... | O que ele produz | Não confundir com |
|---|---|---|---|
| [Controls](controls/README.md) | saber o requisito mínimo aplicável e como ele será verificado | owner, evidence, verification method e finding | guidance ou checklist informal |
| [Schemas](schemas/README.md) | validar um record machine-readable ou integrar automação | contrato JSON, campos, enums e lineage | formulário narrativo ou decisão de risco |
| [Templates](templates/README.md) | registrar uma decisão, assessment ou plano de forma consistente | documento ou record preenchível | aprovação automática ou evidência suficiente por si só |
| [Registry](registry/README.md) | materializar estate, ownership, registry e blueprint | objetos de identificação e desired state | inventário informal ou dashboard |
| [Patterns](patterns/README.md) | escolher uma solução recorrente com trade-offs conhecidos | estrutura de desenho, controles e evidências esperadas | arquitetura obrigatória ou produto prescrito |
| [Assessments](assessments/README.md) | avaliar maturidade, risco, tecnologia ou comparação contextual | evidência organizacional, score e decisão | policy ou evidência universal de eficácia |
| [Examples](examples/README.md) | entender como artefatos se relacionam em um caso fictício | referência de preenchimento e coerência | evidência de produção ou template canônico |

## Rotas por decisão

| Decisão atual | Abra primeiro | Resultado esperado |
|---|---|---|
| Definir mandato, roles e authorities | [Governance Charter](templates/governance-charter-template.md) → [RACI](templates/governance-raci-template.md) → [Forum TOR](templates/governance-forum-tor.md) | Mandato, accountability, decision rights e fóruns registrados. |
| Descobrir e registrar agentes | [Registry](registry/README.md) → [Agent Registry schema](schemas/agent-registry.schema.json) → [Registry template](templates/agent-registry-template.md) | `agent_id`, owners, lifecycle, confidence e dependências identificados. |
| Decidir risco e admissibilidade | [Risk pre-screen](templates/risk-pre-screen.md) → [Risk Scoring Worksheet](templates/risk-scoring-worksheet.md) → [Agent Risk Record](templates/agent-risk-record.md) | Tier, admissibilidade, escaladores e rota de review. |
| Descrever arquitetura e bindings | [Agent Blueprint](templates/agent-blueprint-template.md) → [Blueprint schema](schemas/agent-blueprint.schema.json) → [Patterns](patterns/README.md) | Desired state, identity, data, tools, modelos e boundaries. |
| Preparar release | [Minimum Production Bar](controls/minimum-production-bar.md) → [Release Evidence Manifest](templates/release-evidence-manifest.md) → [Release Decision Checklist](templates/release-decision-checklist.md) | Evidence package proporcional e decisão recuperável. |
| Operar, conter ou reativar | [Runtime pattern](patterns/runtime-observability-and-quarantine.md) → [Support Runbook](examples/support-runbook.example.md) → [Attestation and Sunset Record](templates/attestation-sunset-record.md) | Alert-to-action, contenção, reativação e lifecycle registrados. |
| Revisar valor, maturidade ou portfolio | [Maturity model](maturity/maturity-model.md) → [Capability Assessment](templates/capability-assessment-worksheet.md) → [Use-Case Portfolio](templates/use-case-portfolio.md) | Baseline, backlog, target e decisão de continuidade. |

## Regras de uso

Records precisam identificar owner, status, framework release, evidência e próxima revisão. Campos ausentes permanecem `missing`; não são inferidos. Decisões preservam authority, rationale, condições, expiry e residual risk quando aplicável. Segredos, dados pessoais, evidência de produção e dados de cliente não pertencem a este repositório; os exemplos usam identidades e organizações fictícias.

O [README de contribuição](../CONTRIBUTING.md) contém instruções de manutenção e validação do repositório. Essas instruções não fazem parte do caminho de adoção organizacional.

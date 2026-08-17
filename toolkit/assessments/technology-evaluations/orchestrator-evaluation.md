---
title: Orchestrator Technology Evaluation
type: assessment
status: draft
maturity: illustrative
last_reviewed: 2026-08-17
review_cycle: major-change
owners: [architecture, governance, platform]
related:
  - ../../templates/orchestrator-decision-exit-record.md
  - ../comparison-matrices/README.md
  - ../../../docs/framework/06-architecture-and-technical-controls.md
  - ../../../docs/framework/07-evaluation-evidence-and-assurance.md
---

# Orchestrator Technology Evaluation

> Assessment reutilizável e vendor-neutral para comparar uma ou mais alternativas de orchestration. Ele alimenta o [Orchestrator Decision and Exit Record](../../templates/orchestrator-decision-exit-record.md); não o substitui, não aprova fornecedor automaticamente e não cria ranking universal.

## 1. Escopo e decisão

| Campo | Preencher |
|---|---|
| `assessmentId` | identificador estável da avaliação |
| `decisionInScope` | qual decisão de architecture/platform está sendo suportada |
| `useCasesInScope` | use cases e população cobertos |
| `evidenceCutoff` | data até a qual a evidência foi considerada |
| `alternatives` | alternativas comparadas; podem ser plataforma, assembly of tools ou opção de não adoção |
| `decisionAuthority` | authority competente para a decisão |
| `reviewer` | reviewer independente ou challenge quando aplicável |
| `relatedDecisionRecord` | referência ao G3 que receberá a conclusão |
| `excludedClaims` | claims que não serão tratados como evidência nesta avaliação |

Antes de pontuar, registre o work profile do caso: `determinism`, `governanceConstraints`, `humanOversight`, `iterativeNeed` e `eventDrivenCoordination`, cada um como `low`, `moderate` ou `high`, com rationale e evidence. Registre também `primaryOrchestrationPattern` e `secondaryOrchestrationPattern`, quando houver.

## 2. Famílias de avaliação

### 2.1 Orchestration Pattern Alignment

Avalie se a alternativa suporta a natureza do trabalho classificada no work profile, incluindo o pattern primário e o secundário. Considere workflow orchestration, iterative-reasoning orchestration e supervisory multi-agent orchestration como padrões complementares, não como opções mutuamente exclusivas.

### 2.2 Authority / Placement Fit

Avalie onde authority, state, source of truth, enforcement, recovery e audit trail residem. Registre o placement como crosswalk externo quando necessário — `consolidated`, `coordinated` ou `federated` — sem confundi-lo com o `Federated Governance Operating Model` canônico e sem transformar `coordinated` em default.

### 2.3 Capability Match

Avalie capabilities necessárias ao caso, não a quantidade de features declaradas:

- workflow;
- iterative/adaptive reasoning;
- multi-agent coordination;
- MCP/AI gateways;
- governance integration;
- runtime orchestration;
- observability;
- security;
- extensibility/custom coding;
- identity, data, policy, evidence e recovery integration.

### 2.4 Production Operations Fit

Avalie operabilidade no contexto: SLOs, failure modes, retry e idempotency, degraded mode, rollback, quarantine, kill switch, observability cross-plane, privacy, cardinality, cost, human escalation, support model, incident response e recovery drill.

### 2.5 Economics, Viability & Exit Risk

Avalie custo total, quota, skills, roadmap, sustentabilidade, dependência de state proprietário, export, interoperability, substitution test, exit sequence e custo de migração. Uso, adoção ou proximidade comercial não são prova de value realizado.

## 3. Escala e evidência

Use a escala de 1 a 5 apenas como instrumento de comparação contextual:

| Score | Significado |
|---:|---|
| 1 | não atende ou há evidence de failure relevante |
| 2 | atende parcialmente, com gap material ou dependência não resolvida |
| 3 | atende ao escopo mínimo, com limitações conhecidas |
| 4 | atende bem ao escopo, com evidence reproduzível e riscos controláveis |
| 5 | atende de forma forte e demonstrada no contexto, com evidence independente ou teste repetível |

Cada score deve conter `evidence`, `confidence`, `rationale`, `limitations` e `evidenceCutoff`. Ausência de evidence é `unknown` ou `missing`, nunca zero silencioso. Claim do fornecedor é evidência de implementação declarada, não prova de eficácia.

## 4. Matriz comparativa

| Família | Critério | Peso/rationale | Alternativa A score | Evidência/confidence A | Alternativa B score | Evidência/confidence B | Alternativa C score | Evidência/confidence C | Knockout condition | Sensitivity note |
|---|---|---|---:|---|---:|---|---:|---|---|---|
| Pattern alignment |  |  |  |  |  |  |  |  |  |  |
| Authority / placement fit |  |  |  |  |  |  |  |  |  |  |
| Capability match |  |  |  |  |  |  |  |  |  |  |
| Production operations fit |  |  |  |  |  |  |  |  |  |  |
| Economics, viability & exit risk |  |  |  |  |  |  |  |  |  |  |

Use colunas adicionais ou uma matriz separada quando houver mais de três alternativas. O objetivo é comparar opções para um caso; não declarar um vencedor universal.

## 5. Knockout conditions

Uma alternativa não pode vencer por score agregado quando falhar requisito bloqueante de segurança, identity, admissibility, obrigação legal, control, authority, evidence, recovery ou exit. Registre a condição, a fonte, o owner e a disposição:

| Condition | Alternative(s) affected | Evidence | Authority | Disposition |
|---|---|---|---|---|
|  |  |  |  |  |

## 6. Sensitivity e missing evidence

Registre quando a conclusão muda conforme pesos ou evidências materiais:

| Sensitivity question | Base case | Changed assumption | Effect on disposition | Decision authority |
|---|---|---|---|---|
|  |  |  |  |  |

Lista de evidence ausente ou não verificável:

| Missing evidence | Why it matters | Owner | Due/trigger | Treatment |
|---|---|---|---|---|
|  |  |  |  | `unknown`, `conditional`, `hold` ou `not-applicable` com rationale |

## 7. Conclusão para o G3

A conclusão deve alimentar o G3 com uma disposição condicionada ao escopo:

| Campo | Preencher |
|---|---|
| `recommendedDisposition` | `approve`, `conditional`, `hold`, `reject` ou `no-adoption` |
| `selectedAlternative` | alternativa ou assembly escolhido, se houver |
| `patternFitSummary` | aderência ao primary/secondary pattern |
| `authorityPlacementSummary` | owner de execution, recovery, governance e accountability |
| `blockingFindings` | findings que impedem avanço |
| `conditions` | conditions, owner e expiry |
| `confidence` | `low`, `medium` ou `high` |
| `exitDependencies` | testes e capacidades necessários para substituição |

O decision record continua sendo a fonte da decisão final, das authorities, do risco residual, das conditions, da portabilidade e da saída. Este assessment apenas torna comparável a evidência usada para chegar à decisão.

## 8. Limites

Este artefato não altera risk tier, admissibility, risk score, readiness score, MPB, impact assessment, registry, control catalog ou schemas canônicos. Não exige OpenTelemetry, AIR, MCP, A2A, um produto, um fornecedor ou um backend específico. Não converte score em assurance de eficácia nem aceita score agregado como substituto de authority humana.

## Critério de conclusão

A avaliação está concluída quando um reviewer consegue reconstruir o work profile, verificar o fit do pattern primário/secundário, comparar alternativas com evidence e confidence, identificar knockout conditions e missing evidence, reproduzir a sensitivity analysis material e localizar a disposição correspondente no G3.

---
title: Example — AI-Native Observability Profile
type: example
status: illustrative
last_reviewed: 2026-08-17
related:
  - ../templates/ai-native-observability-profile.md
  - ../patterns/ai-native-observability-profile.md
  - ../../docs/architecture/decisions/0014-ai-native-observability-profile.md
  - ../schemas/audit-event.schema.json
---

# Example — AI-Native Observability Profile

> Caso totalmente fictício e vendor-neutral. IDs, eventos, custos, resultados e nomes não representam uma organização, pessoa, fornecedor ou evidência de produção.

## 1. Caso observado

Uma topologia analisa divergências em um catálogo interno e prepara uma recomendação para revisão humana. O objetivo do exemplo é demonstrar correlação e alert-to-action, não provar qualidade do modelo ou valor de negócio.

| Campo | Valor fictício |
|---|---|
| `profileId` | `profile.catalog-drift-observability` |
| `profileVersion` | `1.0.0` |
| `environment` | `sandbox` |
| `rootAgentId` | `catalog-supervisor` |
| `topologyId` | `topology.catalog-analysis` |
| `taskId` | `task-catalog-20260817-0001` |
| `correlationId` | `corr-catalog-20260817-0001` |
| `riskTier` | `T2` |
| `dataClasses` | `internal` |
| `businessOutcome` | recomendação revisável, sem alteração de record |
| `auditEventSchemaRef` | `audit-event.schema.json@1.0` |
| `samplingPolicy` | 100% de policy, tool, containment e human events; traces de modelo amostrados em 20% fora de findings |

## 2. Cadeia de sinais

| Ordem | Sinal | Principais referências | Resultado |
|---:|---|---|---|
| 1 | `agent.task` | task, initiator, root agent, topology, purpose | `started` |
| 2 | `agent.delegation` | delegation, parent/child, scopes, depth, budget, policy ref | `allowed` |
| 3 | `model.call` | model/version ref, role, latency, outcome | `success` |
| 4 | `retrieval` | source/index ref, freshness, authorization ref | `success` |
| 5 | `policy.decision` | policy/version, authority, enforcement point | `allow-with-conditions` |
| 6 | `tool.request` | tool ref, read action, target ref, stateChanging false | `allowed` |
| 7 | `tool.result` | outcome, source ref, record count, redaction | `success` |
| 8 | `human.intervention` | reviewer, authority, decision, rationale | `approve-draft` |
| 9 | `agent.task` | outcome, evidence package, cost refs | `completed` |

Nenhum evento contém prompt bruto, secret, token ou payload pessoal. Argumentos são representados por categorias e referências redigidas.

## 3. Context propagation

O `correlationId` é criado no início da task e propagado para todos os sinais. `taskId`, `topologyId`, `delegationId`, `agentId`, `agentVersion`, `policyDecisionRef` e `evidenceRef` são referências estáveis. O componente de retrieval não suporta `traceParent`, mas emite `parentTaskId` e `correlationId`; essa limitação é registrada como finding de interoperabilidade, não ocultada.

## 4. Exemplo de eventos redigidos

### 4.1 Task

```yaml
schemaVersion: "1.0"
eventId: EVT-CATALOG-TASK-0001
timestamp: 2026-08-17T10:00:00Z
agentId: catalog-supervisor
agentVersion: 2.0.0
eventType: session-start
actor:
  type: workload
  identityRef: idn.catalog.supervisor
correlationId: corr-catalog-20260817-0001
outcome: success
policyDecision: allow-with-conditions
dataClassifications: [internal]
redactionApplied: true
evidenceRef: evidence://fictional/catalog/corr-catalog-20260817-0001
```

### 4.2 Delegation

```yaml
signal: agent.delegation
taskId: task-catalog-20260817-0001
delegationId: del-catalog-0001
parentAgentId: catalog-supervisor
childAgentId: catalog-retrieval-worker
delegatedSubject: catalog-analysis
attenuatedScopes: [catalog:summary:read]
maxDepth: 0
maxFanOut: 0
budgetRef: budget.catalog.t2
policyDecisionRef: pdec-catalog-delegation-0001
correlationId: corr-catalog-20260817-0001
outcome: allowed
evidenceRef: evidence://fictional/catalog/delegation/del-catalog-0001
```

### 4.3 Tool result

```yaml
signal: tool.result
taskId: task-catalog-20260817-0001
toolRef: TLR-CATALOG-READ-001
action: read.catalog-summary
stateChanging: false
targetRef: catalog-summary-ref-0001
policyDecisionRef: pdec-catalog-read-0001
resultCategory: aggregated-records
recordCount: 42
redactionApplied: true
correlationId: corr-catalog-20260817-0001
outcome: success
evidenceRef: evidence://fictional/catalog/tool/0001
```

## 5. Alert-to-action scenario

Durante uma execução posterior, o behavioral baseline identifica profundidade de delegação acima do limite declarado. O sistema não assume que o dashboard é o source of truth; ele emite um signal ligado a uma decisão de policy e à Run Authority.

| Campo | Valor fictício |
|---|---|
| signal | `delegation.depth.exceeded` |
| severity | `high` |
| threshold | `observedDepth > maxDepth` |
| authority | `run-authority` |
| action | bloquear nova edge e quarentenar o child |
| scope | `catalog-retrieval-worker` e edge `del-catalog-0002` |
| evidence preservation | manter correlation timeline, policy decision, edge e lineage |
| reactivation | topology review, regression evidence e nova decision record |

O evento de containment registra `reasonCode`, `correlationId`, authority e evidence ref. O supervisor permanece sem permission para contornar a quarentena.

## 6. Privacy e retention

| Sinal | Dados capturados | Retenção fictícia | Acesso |
|---|---|---|---|
| task | IDs, status, outcome, refs | 30 dias | Run Authority e assurance |
| model.call | model/version ref, latency, token count agregado | 14 dias | plataforma e FinOps |
| retrieval | source ref, freshness, authorization result | 30 dias | data governance e assurance |
| tool | tool/action, target ref, outcome, state-changing | 90 dias | security, run e assurance |
| human.intervention | authority, decision, rationale redigida | conforme evidence hold | authority e auditor autorizado |
| containment | signal, severity, action, evidence ref | conforme incident retention | Run Authority e incident response |

Prompts e payloads não são armazenados no profile. Se uma investigação autorizada precisar de conteúdo adicional, a referência, autoridade, prazo e redaction deverão ser registrados separadamente.

## 7. Custo e outcome

A task registrou custo fictício de modelo, retrieval e storage por componente. O outcome foi `draft-approved`, mas o exemplo não converte esse resultado em valor financeiro. A atribuição de valor exigiria baseline, população impactada, período, alternativa comparável e caveats de atribuição.

| Dimensão | Resultado fictício |
|---|---|
| model cost | `cost-ref-model-0001` |
| retrieval cost | `cost-ref-retrieval-0001` |
| tool cost | `cost-ref-tool-0001` |
| total task cost | `cost-ref-task-0001` |
| operational outcome | draft aprovado para revisão |
| business value | `unverified` |

## 8. Checklist demonstrado

- [x] task possui início, fim, outcome e correlation;
- [x] delegation lineage liga parent, child e scopes atenuados;
- [x] model e retrieval possuem referências e limitações;
- [x] policy decision está ligado ao enforcement;
- [x] tool request/result distingue state-changing;
- [x] intervenção humana é atribuível;
- [x] containment possui signal, severity, authority, scope e evidence;
- [x] privacy, redaction e retention estão declarados;
- [x] custo está separado de valor;
- [x] o exemplo não captura payload, secret ou dado pessoal.

## Limitações do exemplo

O exemplo é ilustrativo, não valida um backend específico, não prova eficácia de controls, não define retenção universal e não representa conformidade. O gap de propagação de `traceParent` no retrieval permanece aberto como issue de interoperabilidade.

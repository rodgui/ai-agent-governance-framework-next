---
title: AI-Native Observability Profile
type: template
status: maintained
maturity: illustrative
last_reviewed: 2026-08-17
review_cycle: quarterly
owners: [run-authority, observability, security, privacy, platform]
related:
  - ../../docs/architecture/decisions/0014-ai-native-observability-profile.md
  - ../patterns/ai-native-observability-profile.md
  - ../schemas/audit-event.schema.json
  - ../../docs/framework/07-evaluation-evidence-and-assurance.md
  - ../../docs/framework/09-operations-incidents-and-continuity.md
  - ../examples/ai-native-observability-operational-drill.example.md
---

# AI-Native Observability Profile

> Use este template para definir a semântica e o consumo de observabilidade de um caso AI-native. Ele não substitui o audit event schema, não aprova uma implementação, não exige backend específico e não autoriza captura de payload sensível por default.

## 1. Identificação e escopo

| Campo | Preencher |
|---|---|
| `profileId` | identificador estável do profile |
| `profileVersion` | versão e data de vigência |
| `status` | `draft`, `under-review`, `approved`, `conditional`, `retired` |
| `businessOwner` | owner do outcome |
| `technicalOwner` | owner da instrumentação e runtime |
| `runAuthority` | authority de operação e containment |
| `privacyReviewer` | reviewer de minimization, retention e access |
| `relatedAgentIds` | agents e versões no escopo |
| `relatedTopologyIds` | topologies e versões no escopo |
| `useCases` | tasks e outcomes cobertos |
| `riskTiers` | tiers aplicáveis |
| `dataClasses` | classes de dados observadas |
| `environment` | test, staging ou production |
| `samplingPolicy` | sampling e exceções para eventos críticos |

## 2. Envelope e correlação

| Campo | Preencher |
|---|---|
| `auditEventSchemaRef` | referência ao schema de audit event |
| `correlationId` | regra de criação e propagação |
| `taskId` | regra de identificação da task |
| `parentTaskId` | vínculo de subtasks |
| `sessionId` | quando aplicável |
| `topologyId` / `topologyVersion` | vínculo com G2 |
| `delegationId` | vínculo de cada handoff |
| `traceParent` | mapping opcional de distributed tracing |
| `policyDecisionRef` | vínculo à policy decision |
| `evidenceRef` | evidence package ou record |
| `clockAssumption` | sincronização e tolerância de timestamp |

**Propagação:**

Descreva como o contexto atravessa agents, model gateways, retrieval, policy, tools, event buses, human approval, containment e evidence store. Declare componentes que não propagam correlação.

## 3. Cobertura de sinais

| Sinal lógico | Obrigatório? | Fonte | Attributes/refs | Retenção | Redaction | Consumer/decisão |
|---|---:|---|---|---|---|---|
| `agent.task` |  |  |  |  |  |  |
| `agent.delegation` |  |  |  |  |  |  |
| `model.call` |  |  |  |  |  |  |
| `retrieval` |  |  |  |  |  |  |
| `tool.request` |  |  |  |  |  |  |
| `tool.result` |  |  |  |  |  |  |
| `policy.decision` |  |  |  |  |  |  |
| `human.intervention` |  |  |  |  |  |  |
| `agent.memory/state` |  |  |  |  |  |  |
| `containment` |  |  |  |  |  |  |
| `value.cost` |  |  |  |  |  |  |

## 4. Semântica por sinal

Para cada sinal, registre:

| Dimensão | Preencher |
|---|---|
| finalidade | qual decisão o sinal suporta |
| início/fim | quando a operação começa e termina |
| actor/authority | quem ou qual workload atua |
| agent/topology | qual agent, version e topology participam |
| parent/child | relação de task, delegation ou causation |
| input/output refs | referências, não payload por default |
| policy/enforcement | policy decision, version e enforcement point |
| outcome | success, denied, failed, partial ou cancelled |
| data classification | classes observadas e redaction |
| evidence | record, hash, lineage ou package |
| uncertainty/limitation | o que não pode ser inferido |

## 5. Privacy, access e retention

| Dimensão | Decisão |
|---|---|
| payloads capturados |  |
| campos proibidos | prompts, secrets, tokens, PII ou outros |
| references/hashes |  |
| redaction | regra, versão e teste |
| acesso operacional | roles, scopes e break-glass |
| acesso de assurance | população, sampling e evidence cutoff |
| retention | por sinal e por tier |
| deletion | cópias, indexes, caches, backups e holds |
| residency | regiões e transferências |
| export | formato, authority e teste |
| incident access | condições e logging |

## 6. Alert-to-action

| Signal | Severidade | Threshold/confidence | Decision authority | Ação | Scope | Evidence | Reativação |
|---|---|---|---|---|---|---|---|
|  |  |  |  | observe / ticket / throttle / step-up / quarantine / rollback |  |  |  |

A cadeia deve ser verificável:

```text
signal → severity → authority → action
       → evidence preservation → remediation
       → regression → reactivation
```

## 7. Coverage e testes

| Teste | População | Resultado esperado | Evidence |
|---|---|---|---|
| task end-to-end |  |  |  |
| supervisor → worker lineage |  |  |  |
| model/retrieval provenance |  |  |  |
| policy deny |  |  |  |
| tool state-changing |  |  |  |
| human intervention |  |  |  |
| memory/state access |  |  |  |
| containment and reactivation |  |  |  |
| redaction/privacy |  |  |  |
| export/substitution |  |  |  |
| outage or missing component |  |  |  |

## 8. Volume, cardinality e custo

| Métrica | Baseline | Threshold | Owner | Ação |
|---|---|---|---|---|
| events por task |  |  |  |  |
| high-cardinality attributes |  |  |  |  |
| dropped/late events |  |  |  |  |
| correlation gaps |  |  |  |  |
| telemetry cost por task |  |  |  |  |
| storage/egress |  |  |  |  |

## 9. Mapping de implementação

| Conceito canônico | Implementação adotada | Mapping opcional | Limitação |
|---|---|---|---|
| `agent.task` |  |  |  |
| `agent.delegation` |  |  |  |
| `model.call` |  |  |  |
| `retrieval` |  |  |  |
| `tool.request/result` |  |  |  |
| `policy.decision` |  |  |  |
| `human.intervention` |  |  |  |
| `memory/state` |  |  |  |
| `containment` |  |  |  |
| `value.cost` |  |  |  |

Mappings são adapters. Não trate mapping de uma convenção ou produto como alteração do contrato canônico.

## 10. Decision e evidence

**Decisão solicitada:** `approve`, `conditional`, `hold` ou `reject`.

**Rationale:**

**Conditions, owner e expiry:**

**Privacy decision:**

**Evidence references:**

**Claims sem evidence:**

**Findings abertos:**

## 11. Checklist

- [ ] task e outcome possuem início, fim e correlation;
- [ ] parent/child e delegation lineage são reconstruíveis;
- [ ] model, retrieval, policy e tool possuem provenance/refs;
- [ ] state-changing actions têm policy, authority, approval e outcome;
- [ ] human intervention é atribuível e contextualizada;
- [ ] memory/state tem owner, classification, retention e deletion;
- [ ] containment liga signal, authority, action, evidence e reactivation;
- [ ] payloads sensíveis são redigidos, minimizados ou não capturados;
- [ ] access, retention, export e deletion foram aprovados;
- [ ] cardinalidade, volume e custo têm baseline e owner;
- [ ] drill reconstrói uma cadeia sem dashboard proprietário;
- [ ] claims sem evidence permanecem `missing`, `conditional` ou `unverified`.

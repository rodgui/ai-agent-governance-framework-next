---
title: Agent Delegation Contract
type: template
status: maintained
maturity: illustrative
last_reviewed: 2026-08-17
review_cycle: quarterly
owners: [architecture, governance, security, platform]
related:
  - ../../docs/architecture/decisions/0013-multi-agent-delegation-contract.md
  - ../patterns/multi-agent-delegation-governance.md
  - ../../docs/framework/06-architecture-and-technical-controls.md
  - ../../docs/framework/09-operations-incidents-and-continuity.md
---

# Agent Delegation Contract

> Use este template para registrar delegação entre agentes. Ele não concede autoridade, não substitui o blueprint, não aprova uma tool e não transforma o supervisor em authority universal. Campos ausentes permanecem `missing`; claims sem evidência permanecem `conditional` ou `unverified`.

## 1. Identificação da topologia

| Campo | Preencher |
|---|---|
| `topologyId` | identificador estável da topologia |
| `topologyVersion` | versão da topologia e data de vigência |
| `status` | `draft`, `under-review`, `approved`, `conditional`, `quarantined`, `retired` |
| `rootAgentId` | agente raiz ou serviço iniciador |
| `purpose` | finalidade aprovada da topologia |
| `businessOwner` | owner do outcome e risco de negócio |
| `technicalOwner` | owner de blueprint, integração e runtime |
| `delegationAuthority` | authority que pode aprovar esta topologia e suas mudanças |
| `riskTier` | `T1`, `T2`, `T3` ou `T4` |
| `admissibility` | `permitted`, `conditional`, `restricted` ou `prohibited` |
| `relatedBlueprintRefs` | blueprints e versões dos agentes |
| `relatedRiskRefs` | assessments, ADRs, findings e exceptions |
| `correlationModel` | chave e regras de propagação da cadeia |

## 2. Nodes da topologia

| `agentId` | `agentVersion` | `role` | `identityRef` | `owner` | `allowedCapabilities` | `allowedDataClasses` | `failureBoundary` |
|---|---|---|---|---|---|---|---|
|  |  | `supervisor` / `worker` / `reviewer` / `router` |  |  |  |  |  |

Cada node deve possuir blueprint, identity model, owner, tier e estado de lifecycle válidos. A role é descritiva; não altera decision rights externos.

## 3. Delegation edges

| Campo | Preencher |
|---|---|
| `delegationId` | identificador da edge |
| `fromAgentId` | agente delegador |
| `toAgentId` | agente delegado |
| `purpose` | finalidade da delegação |
| `task` | tarefa delimitada |
| `delegatedSubject` | usuário, workload ou processo em nome de quem ocorre |
| `allowedActions` | ações permitidas |
| `scopes` | recursos, operações e parâmetros permitidos |
| `dataClasses` | classes de dados que podem atravessar a edge |
| `maxDepth` | profundidade máxima restante |
| `maxFanOut` | número máximo de children ativáveis |
| `budgetRef` | budget, quota e owner |
| `approvalMode` | `automated`, `human`, `dual-control` ou `prohibited` |
| `createdAt` / `expiresAt` | validade temporal |
| `revocationRef` | caminho de revogação |
| `correlationId` | chave da cadeia completa |
| `policyDecisionRef` | decisão de policy que autorizou a edge |
| `evidenceRef` | evidência recuperável |

**Teste de atenuação:**

```text
envelope do child ⊆ envelope efetivo do parent
```

Descreva quais scopes, actions, data classes, depth, fan-out e budget foram removidos ou limitados. Se a relação não puder ser demonstrada, não trate a delegação como aprovada.

## 4. Inter-agent contract

| Dimensão | Preencher |
|---|---|
| `inputSchema` | schema e versão de entrada |
| `outputSchema` | schema e versão de saída |
| `provenance` | origem e transformações do conteúdo |
| `trustLevel` | confiança atribuída e limitações |
| `validation` | validações antes do próximo handoff |
| `timeout` | limite e estado ao exceder |
| `retryPolicy` | quantidade, backoff e condição de retry |
| `idempotency` | chave e garantia esperada |
| `successCondition` | condição objetiva de sucesso |
| `recoverableFailure` | erros que podem ser tratados |
| `terminalFailure` | erros que encerram a edge/topologia |
| `sensitiveFields` | campos sujeitos a redaction/minimization |

## 5. Authority propagation

| Campo | Preencher |
|---|---|
| `initiator` | quem iniciou a cadeia |
| `supervisorIdentity` | identidade do supervisor |
| `workerIdentity` | identidade do worker |
| `delegatedSubject` | sujeito delegado |
| `attenuatedScopes` | scopes efetivamente propagados |
| `policyDecisionRef` | decisão por edge e por ação material |
| `humanEscalation` | gatilho, authority, prazo e fallback |
| `toolEnforcementRef` | gateway/broker que aplica a action |
| `dataEnforcementRef` | policy/data point que aplica o acesso |
| `assuranceRef` | evidence/assurance status relevante |

## 6. Failure propagation e containment

| Cenário | Estado seguro | Escopo de contenção | Authority | Evidência | Critério de retorno |
|---|---|---|---|---|---|
| edge expirada |  |  |  |  |  |
| edge revogada |  |  |  |  |  |
| privilege escalation |  |  |  |  |  |
| input/output inválido |  |  |  |  |  |
| worker indisponível |  |  |  |  |  |
| worker state-changing falha |  |  |  |  |  |
| supervisor comprometido |  |  |  |  |  |
| registry/policy indisponível |  |  |  |  |  |

Declare se a contenção bloqueia a edge, o child, o parent, a capability, os descendants ou toda a topologia. Não use `retry` como substituto de uma nova decisão autorizada.

## 7. Budget, depth e fan-out

| Limite | Valor | Scope | Owner | Threshold de alerta | Ação ao exceder | Evidence |
|---|---|---|---|---|---|---|
| `maxDepth` |  | topologia/edge |  |  |  |  |
| `maxFanOut` |  | topologia/parent |  |  |  |  |
| task budget |  | task/edge |  |  |  |  |
| token/tool budget |  | agent/task |  |  |  |  |
| wall-clock timeout |  | task/edge |  |  |  |  |
| concurrent children |  | parent/topology |  |  |  |  |

## 8. Evidence package

Registre referências para:

- topology record e versão;
- blueprints dos nodes;
- delegation edge e policy decision;
- identidade, delegated subject e scopes;
- input/output validation;
- budget, depth, fan-out e timeout checks;
- tool/data/model decisions;
- approvals, human escalation e exceptions;
- failure, containment, rollback e reactivation;
- correlation timeline e outcome;
- findings e limitações.

## 9. Decision

**Decisão solicitada:** `approve`, `conditional`, `hold` ou `reject`.

**Rationale:**

**Condições, owner e expiry:**

**Risco residual aceito por:**

**Próxima revisão ou evento trigger:**

## 10. Checklist

- [ ] topology, nodes e versões estão identificados;
- [ ] cada edge tem purpose, task, parent, child e correlation ID;
- [ ] delegated subject e identidades são distinguíveis;
- [ ] envelope do child foi demonstrado como atenuado;
- [ ] allowed actions, scopes e data classes estão explícitos;
- [ ] maxDepth, maxFanOut, budget, timeout e retry têm owner;
- [ ] input/output contracts têm schema, provenance e validation;
- [ ] actions state-changing passam por enforcement externo;
- [ ] expiry e revocation bloqueiam retry/replay;
- [ ] failure boundary e containment scope foram definidos;
- [ ] supervisor não foi tratado como authority absoluta;
- [ ] evidence package é recuperável e versionado;
- [ ] casos de privilege escalation e worker failure foram exercitados;
- [ ] claims sem evidência permanecem `missing`, `conditional` ou `unverified`.

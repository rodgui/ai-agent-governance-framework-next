---
title: Example — Supervisor/Worker Delegation Contract
type: example
status: illustrative
last_reviewed: 2026-08-17
related:
  - ../templates/agent-delegation-contract.md
  - ../patterns/multi-agent-delegation-governance.md
  - ../../docs/architecture/decisions/0013-multi-agent-delegation-contract.md
---

# Example — Supervisor/Worker Delegation Contract

> Caso totalmente fictício e vendor-neutral. Os nomes, IDs, eventos e resultados não representam uma organização, pessoa, fornecedor ou evidência de produção.

## 1. Caso e topologia

Uma topologia recebe um pedido interno para preparar uma análise de divergência de inventário. O `inventory-supervisor` pode decompor a tarefa entre um worker de consulta e um worker de revisão. Nenhum worker pode alterar o sistema de registro; a atualização, se necessária, exige uma segunda decisão fora desta topologia.

| Campo | Valor fictício |
|---|---|
| `topologyId` | `topology.inventory-reconciliation` |
| `topologyVersion` | `1.0.0` |
| `status` | `approved` |
| `rootAgentId` | `inventory-supervisor` |
| `purpose` | preparar uma análise de divergência e recomendar próximos passos |
| `businessOwner` | `inventory-process-owner` |
| `technicalOwner` | `agent-platform-owner` |
| `delegationAuthority` | `design-authority` |
| `riskTier` | `T2` |
| `admissibility` | `permitted` |
| `correlationModel` | um `correlationId` por task, propagado para edges, tools, policy decisions e outcome |

## 2. Nodes

| `agentId` | `agentVersion` | `role` | `identityRef` | `allowedCapabilities` | `allowedDataClasses` | `failureBoundary` |
|---|---|---|---|---|---|---|
| `inventory-supervisor` | `2.1.0` | `supervisor` | `idn.inventory.supervisor` | `observe`, `delegate`, `create-draft` | `internal` | toda a topologia |
| `inventory-query-worker` | `1.4.2` | `worker` | `idn.inventory.query` | `observe` | `internal` | apenas a edge de consulta |
| `inventory-review-worker` | `1.1.0` | `reviewer` | `idn.inventory.review` | `observe`, `create-draft` | `internal` | worker e edge de revisão |

Os blueprints dos três agentes têm owners ativos, scopes próprios e referências de runtime. O supervisor possui `delegate`, mas isso não autoriza o worker a delegar novamente.

## 3. Delegation edge permitida

| Campo | Valor fictício |
|---|---|
| `delegationId` | `del-20260817-0001` |
| `fromAgentId` | `inventory-supervisor` |
| `toAgentId` | `inventory-query-worker` |
| `purpose` | consultar registros para identificar divergências |
| `task` | retornar totais agregados por unidade e período |
| `delegatedSubject` | `inventory-process` |
| `allowedActions` | `read.inventory-summary` |
| `scopes` | `inventory:summary:read`, `period:current`, `region:approved-scope` |
| `dataClasses` | `internal` |
| `maxDepth` | `0` |
| `maxFanOut` | `0` |
| `budgetRef` | `budget.inventory.analysis.t2` |
| `approvalMode` | `automated` |
| `createdAt` / `expiresAt` | `2026-08-17T10:00:00Z` / `2026-08-17T10:10:00Z` |
| `revocationRef` | `revocation.inventory.topology` |
| `correlationId` | `corr-inventory-20260817-0001` |
| `policyDecisionRef` | `pdec-inventory-read-0001` |
| `evidenceRef` | `evidence://fictional/inventory/corr-inventory-20260817-0001` |

O envelope do worker é menor que o do supervisor: o worker não possui `delegate`, não possui write/execute e não recebe dados `confidential` ou `restricted`.

## 4. Inter-agent contract

| Dimensão | Valor fictício |
|---|---|
| `inputSchema` | `inventory-query-request@1.0` |
| `outputSchema` | `inventory-summary-response@1.0` |
| `provenance` | consulta a fonte autorizada com filtro de período e região |
| `trustLevel` | `untrusted-output-until-validated` |
| `validation` | schema, row-count bounds, source freshness e policy consistency |
| `timeout` | 20 segundos; timeout encerra a edge |
| `retryPolicy` | máximo de 1 retry se a falha for transitória e a edge ainda estiver válida |
| `idempotency` | `correlationId + delegationId` |
| `successCondition` | resposta válida e proveniência recuperável |
| `recoverableFailure` | timeout transitório antes de expiry |
| `terminalFailure` | policy deny, scope mismatch, expiry ou output inválido |

## 5. Cenário 1 — Delegação permitida e concluída

1. O iniciador cria `corr-inventory-20260817-0001`.
2. O supervisor autentica sua identidade e valida que pode delegar `read.inventory-summary`.
3. A policy calcula a interseção entre o envelope do supervisor, o blueprint do worker, o escopo de dados e a edge. O resultado é `allow`.
4. O worker consulta somente a fonte e o período autorizados.
5. O output passa por validação de schema, freshness e provenance.
6. O supervisor consolida a análise como draft; nenhum record oficial é alterado.
7. A timeline registra iniciador, supervisor, worker, edge, policy decision, tool outcome e resultado.

**Resultado:** `completed`. A evidência é recuperável pelo `correlationId` sem depender de dashboard específico.

## 6. Cenário 2 — Tentativa de privilege escalation

O supervisor tenta criar uma edge para `inventory-query-worker` com `write.inventory-record` e `maxDepth: 1`. A policy compara o envelope do worker e identifica duas violações: o worker não possui capability de escrita e a topologia não permite delegação recursiva.

| Elemento | Resultado |
|---|---|
| decisão | `deny` |
| motivo | `child envelope` não contém a capability solicitada; `maxDepth` excedido |
| ação | nenhuma chamada ao sistema de registro |
| finding | `finding.inventory.delegation-escalation-0001` |
| autoridade | `identity-policy-authority` |
| contenção | bloquear a edge tentada; manter a topologia em `approved` |
| evidência | policy decision, envelope parent/child, request e correlation timeline |

O supervisor não pode converter o `deny` em retry com scope ampliado. Uma nova finalidade exige nova avaliação e decision record.

## 7. Cenário 3 — Worker state-changing falha

O `inventory-review-worker` prepara um draft para revisão humana, mas uma etapa de escrita em um sandbox de teste falha depois de uma resposta de timeout. O worker não possui autorização para atualizar o system of record. O gateway marca a tentativa como `failed`, preserva os parâmetros redigidos e impede qualquer retry fora da edge original.

A Run Authority contém somente o worker e a edge de revisão, preserva a timeline e solicita análise de idempotency. O supervisor permanece em `restricted` para novas delegações de escrita até que a revisão confirme que não houve side effect. A reativação exige evidence de ausência ou reversão do efeito, regression test e decisão do owner.

## 8. Checklist demonstrado

- [x] topologia, nodes, roles e versões identificados;
- [x] supervisor, workers e delegated subject distinguíveis;
- [x] delegation edge tem purpose, task, scope, expiry, revocation e correlation;
- [x] child envelope é menor que o envelope do supervisor;
- [x] `maxDepth`, `maxFanOut` e budget são explícitos;
- [x] privilege escalation é negada sem chamada state-changing;
- [x] output do worker passa por validação antes do próximo handoff;
- [x] falha state-changing produz contenção e preservação de evidência;
- [x] supervisor não é authority absoluta;
- [x] nenhum dado pessoal, secret ou evidência de produção é usado.

## Limitações do exemplo

O caso não define um schema JSON final, não modela memória compartilhada, não cobre topologia cross-region e não prova eficácia operacional. Esses itens permanecem dependentes do walkthrough G2 e de evidência real autorizada fora deste repositório canônico.

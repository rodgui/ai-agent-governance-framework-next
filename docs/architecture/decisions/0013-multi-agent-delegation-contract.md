---
title: ADR-0013 — Contrato de delegação multiagente
status: draft
owner: framework-maintainers
last_reviewed: 2026-08-17
review_cycle: major-change
supersedes: null
related:
  - ../README.md
  - ../../framework/06-architecture-and-technical-controls.md
  - ../../framework/09-operations-incidents-and-continuity.md
  - ../../../toolkit/patterns/multi-agent-delegation-governance.md
  - ../../../toolkit/templates/agent-delegation-contract.md
  - ../../../toolkit/examples/supervisor-worker-delegation.example.md
  - ../../../toolkit/schemas/agent-blueprint.schema.json
---

# ADR-0013 — Contrato de delegação multiagente

## Status e escopo

Esta é uma **decisão arquitetural em rascunho** da frente G2. Ela materializa a topologia e o envelope de delegação entre agentes, especialmente em modelos supervisor/worker, sem criar automaticamente novos controls nem alterar o `agent-blueprint.schema.json` nesta etapa.

A decisão permanece `draft` até ser exercitada com um caso fictício e um caso organizacional autorizado, e aprovada pela Design Authority, Governance Owner, Security/IAM Authority, Data/Privacy Authority e Run Authority quando houver efeito operacional. O contrato conceitual deve ser validado antes de qualquer extensão machine-readable obrigatória.

## Contexto

O framework já reconhece `multi-agent` como pattern, `delegate` como classe de ação, identidade do agente, delegated subject, scopes, budgets, profundidade de cadeia, correlation IDs, kill switch, quarantine e controles por tier. Esses elementos, porém, estão distribuídos e não representam explicitamente a relação supervisor → worker.

Em uma topologia multiagente, um supervisor pode planejar, dividir tarefas, escolher workers e consolidar resultados. Um worker pode acessar dados, tools ou sistemas com uma autoridade menor e uma finalidade mais estreita. Sem um contrato explícito, surge o risco de presumir que o worker herda toda a autoridade do supervisor, que uma nova delegação amplia scopes, que uma falha do child não é propagada ao parent ou que uma ação state-changing fica sem uma cadeia atribuível.

## Decisão proposta

1. **Delegação deve ser explícita, atribuível, limitada, expirável e revogável.** A existência de um supervisor, uma relação hierárquica ou uma chamada interna não concede autoridade implícita ao worker.

2. **A topologia deve ser identificável e versionada.** Cada topology record registra `topologyId`, `version`, `rootAgentId`, `owner`, `purpose`, `riskTier`, `status`, `nodes` e `delegationEdges`. O vínculo entre agentes não deve depender somente de nomes ou logs locais.

3. **Cada node declara papel, identidade, owner e envelope de capability.** Papéis iniciais são `supervisor`, `worker`, `reviewer` e `router`. Cada node referencia `agentId`, `agentVersion`, `identityRef`, `owner`, `allowedCapabilities`, `allowedDataClasses`, `riskTier` e `failureBoundary`.

4. **Cada delegation edge carrega sua própria intenção e seus limites.** A edge registra `delegationId`, `fromAgentId`, `toAgentId`, `purpose`, `task`, `allowedActions`, `scopes`, `dataClasses`, `maxDepth`, `maxFanOut`, `budgetRef`, `expiresAt`, `revocationRef`, `approvalMode`, `correlationId` e `evidenceRef`.

5. **A autoridade do child é atenuada, nunca ampliada, pela delegação.** O envelope do worker deve ser subconjunto da autoridade efetiva do delegator e continuar sujeito à authority de identity, data, policy, tool e assurance. O worker não pode conceder scopes, data classes, budget, depth ou capabilities além do envelope recebido.

6. **A identidade do agente é separada da identidade da execução e do sujeito delegado.** O contrato preserva quem iniciou a cadeia, qual agente delegou, qual agente executou, em nome de quem a ação ocorreu, sob qual finalidade e qual policy decision autorizou cada etapa.

7. **Inter-agent contracts são necessários para handoffs materiais.** Entrada, saída, provenance, trust level, validação, timeout, retry, idempotency, erro e condição de sucesso devem ser definidos. Output de um agent é input não confiável do próximo até passar pelas validações aplicáveis.

8. **State-changing actions permanecem sujeitas aos enforcement points externos.** Um supervisor não pode converter uma recomendação em autorização, nem um worker pode contornar gateway, identity, data policy, approval ou kill switch porque a tarefa foi delegada.

9. **A falha deve propagar-se conforme blast radius e failure boundary declarados.** A falha de um worker pode bloquear a edge, o parent, a capability afetada ou toda a topologia, conforme o risco. O estado da cadeia, a decisão de contenção e a evidência devem ser preservados com o mesmo correlation ID.

10. **Revogação e expiração vencem retries e replays.** Uma edge expirada, revogada, quarantined ou com condição não satisfeita não pode ser reativada por retry automático ou por outro worker sem nova decisão autorizada.

11. **A topologia não substitui accountability humana.** O supervisor é um componente de coordenação; não se torna authority absoluta por ocupar o nível superior da hierarquia. Business Owner, Technical Owner, domain authorities e Run Authority preservam seus decision rights.

12. **O contrato começa como guidance/template.** A alteração do blueprint ou a criação de um schema dedicado somente será considerada após pelo menos um walkthrough completo e três cenários testados: delegação concluída, tentativa de privilege escalation e falha de worker state-changing com contenção e preservação de evidência.

## Contrato mínimo conceitual

| Objeto | Campos mínimos | Pergunta respondida |
|---|---|---|
| `agentTopology` | `topologyId`, `version`, `rootAgentId`, `owner`, `purpose`, `status`, `riskTier`, `nodes`, `delegationEdges` | Qual topologia está sendo governada? |
| `node` | `agentId`, `agentVersion`, `role`, `identityRef`, `owner`, `allowedCapabilities`, `allowedDataClasses`, `failureBoundary` | Qual agente participa, com qual papel e envelope? |
| `delegationEdge` | `delegationId`, `fromAgentId`, `toAgentId`, `purpose`, `task`, `scopes`, `allowedActions`, `dataClasses`, `maxDepth`, `maxFanOut`, `budgetRef`, `expiresAt`, `revocationRef`, `correlationId` | Quem delegou o quê, para quem, sob quais limites? |
| `interAgentContract` | `inputSchema`, `outputSchema`, `provenance`, `validation`, `trustLevel`, `timeout`, `retryPolicy`, `idempotency`, `failureSemantics` | Como o handoff é validado e encerrado? |
| `authorityPropagation` | `initiator`, `delegatedSubject`, `attenuatedScopes`, `approvalMode`, `policyDecisionRef`, `humanEscalation` | Qual autoridade foi propagada e limitada? |
| `failurePropagation` | `containmentScope`, `parentState`, `childState`, `evidencePreservation`, `reactivationAuthority` | O que acontece quando uma parte falha? |

## Consequências positivas

A decisão torna a cadeia supervisor → worker auditável, limita privilege transitivity, permite budget e depth enforcement por edge, preserva a separação entre agente e execução e cria uma base para conter falhas sem depender do próprio agente com problema. Ela também dá ao G4 uma topologia explícita para correlacionar task, delegation, tool e outcome.

## Custos e consequências negativas

Será necessário manter registros de topologia e edges, propagar contexto entre agentes, validar contratos de entrada e saída e exercitar falhas compostas. Em topologias grandes, o registro pode ficar volumoso; por isso, o contrato deve permitir referências versionadas e não repetir em cada edge todo o conteúdo do blueprint do agente.

## Não decidido nesta ADR

Esta ADR não define um schema JSON obrigatório, não altera os enums existentes, não determina se a topologia deve viver dentro do blueprint ou em um artefato separado, não prescreve protocolo inter-agent, não transforma supervisor em authority universal e não exige uma implementação comercial ou open source específica.

## Critérios de validação

- um caso supervisor/worker produz topology record, nodes e delegation edges completos;
- uma delegação concluída permite responder quem iniciou, quem delegou, quem executou, qual sujeito foi delegado e quais scopes vigoravam;
- tentativa de privilege escalation é negada por comparação entre envelope parent e child;
- worker state-changing exige o enforcement externo e a approval mode aplicável;
- edge expirada ou revogada bloqueia retry e replay;
- falha de worker preserva correlation ID, evidência e estado do parent/child;
- a contenção pode atingir o menor blast radius compatível com o tier;
- o supervisor não é tratado como authority absoluta;
- o caso fictício não contém dados pessoais, secrets ou evidência de produção;
- nenhuma mudança de schema ou control é feita antes do walkthrough e da decisão de migração.

## Evidência e aprovação

A decisão precisa ser exercitada com o [template de contrato de delegação](../../../toolkit/templates/agent-delegation-contract.md), o [pattern de governança de delegação](../../../toolkit/patterns/multi-agent-delegation-governance.md) e o [exemplo supervisor/worker](../../../toolkit/examples/supervisor-worker-delegation.example.md). A aprovação deve registrar cenários testados, falhas encontradas, controles reutilizados, limitações, decisão sobre schema e data de revisão.

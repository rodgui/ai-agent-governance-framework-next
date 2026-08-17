---
title: Pattern — Multi-Agent Delegation Governance
status: draft
owner: framework-maintainers
last_reviewed: 2026-08-17
review_cycle: quarterly
related:
  - README.md
  - ../../docs/architecture/decisions/0013-multi-agent-delegation-contract.md
  - ../../docs/framework/06-architecture-and-technical-controls.md
  - ../../docs/framework/09-operations-incidents-and-continuity.md
  - ../templates/agent-delegation-contract.md
---

# Pattern — Multi-Agent Delegation Governance

## Intenção

Governar topologias em que agentes coordenam, delegam tarefas ou ativam outros agentes, mantendo autoridade limitada, identidade atribuível, contratos de handoff e contenção proporcional ao blast radius.

## Problema

Uma topologia supervisor/worker pode parecer apenas uma sequência de chamadas internas, mas cada handoff pode alterar identidade, dados, tools, budget, profundidade e efeito operacional. Se o worker herdar implicitamente a autoridade do supervisor, a hierarquia de agentes se torna um canal de privilege escalation e dificulta atribuir a decisão quando um child falha.

## Quando usar

Use este pattern quando houver supervisor/worker, planner/executor, router/specialist, reviewer/worker, event-driven activation de agentes, delegação recursiva ou qualquer topologia em que um agente possa criar, acionar ou conceder acesso a outro agente.

Não use o pattern para representar apenas múltiplas chamadas independentes de modelo sem coordenação, delegação ou estado compartilhado. Nesses casos, o blueprint e os contratos de modelo podem ser suficientes.

## Princípios

1. **Delegação explícita:** uma chamada entre agentes é uma delegation edge somente quando possui propósito, envelope e evidência identificáveis.
2. **Atenuação de autoridade:** o child recebe um subconjunto do envelope efetivo do parent, sujeito às authorities especializadas e aos enforcement points externos.
3. **Separação de identidades:** iniciador, supervisor, worker e delegated subject permanecem distinguíveis.
4. **Limite por edge:** scopes, ações, classes de dados, depth, fan-out, budget, expiry e revocation são atributos do handoff, não apenas da topologia.
5. **Contrato antes de confiança:** output de um agente é input não confiável até passar pela validação definida.
6. **Falha com containment:** falhas podem bloquear edge, capability, parent, child ou topologia; o escopo deve ser declarado antes da operação.
7. **Enforcement fora do agente:** identity, data, tool, approval, policy, quarantine e kill switch não dependem de instrução do supervisor ou worker.

## Solução

Registre uma topology versionada com `rootAgentId`, nodes e delegation edges. Cada node referencia seu blueprint e sua identidade; cada edge referencia finalidade, tarefa, autoridade atenuada, limites e correlação. O supervisor pode planejar e coordenar, mas o gateway, identity provider, data policy, tool broker e Run Authority continuam aplicando suas próprias decisões.

A autoridade efetiva do child é calculada como a interseção do envelope delegado com os limites do próprio agente, do tier, da finalidade, do contexto, das authorities de domínio e dos controles externos. A fórmula é conceitual, não uma implementação matemática obrigatória:

```text
child_effective_envelope =
  delegated_envelope
  ∩ child_blueprint_envelope
  ∩ identity_and_policy_constraints
  ∩ data_and_tool_constraints
  ∩ risk_tier_and_admissibility
```

Se a interseção não puder ser demonstrada, a delegação permanece `missing`, `conditional`, `restricted` ou `denied` conforme o tier e não executa ação material.

## Fluxo operacional

1. registrar ou localizar a topologia e a versão dos agentes;
2. autenticar o iniciador, o supervisor e o delegated subject;
3. validar que o supervisor está autorizado a delegar aquela finalidade;
4. construir a delegation edge com scopes, ações, dados, depth, fan-out, budget, expiry e revocation;
5. verificar que o envelope do child não amplia o do parent;
6. validar input e contrato inter-agent antes de executar;
7. aplicar identity, data, policy e tool enforcement no domínio correspondente;
8. registrar task, delegation, model, retrieval, tool, policy e outcome com o mesmo correlation ID;
9. aplicar timeout, retry, idempotency e failure semantics declarados;
10. propagar falha e containment para o menor escopo seguro;
11. preservar evidência do parent, child e edge;
12. reautorizar, corrigir, substituir ou aposentar a topologia quando houver mudança material.

## Matriz de delegação

| Campo | Pergunta |
|---|---|
| `topologyId` / `version` | Qual topologia e versão estão ativas? |
| `fromAgentId` | Qual agente delegou? |
| `toAgentId` | Qual agente recebeu? |
| `delegatedSubject` | Em nome de quem a ação ocorre? |
| `purpose` / `task` | Qual finalidade e tarefa foram autorizadas? |
| `allowedActions` / `scopes` | Quais capacidades e recursos são permitidos? |
| `dataClasses` | Quais classes de dados podem atravessar a edge? |
| `maxDepth` / `maxFanOut` | Quais limites impedem recursão e explosão de agentes? |
| `budgetRef` | Qual budget e owner controlam o consumo? |
| `expiresAt` / `revocationRef` | Quando a edge expira e como é revogada? |
| `approvalMode` | Há aprovação automatizada, humana, dual-control ou proibição? |
| `correlationId` | Como a cadeia completa é reconstruída? |
| `evidenceRef` | Onde estão decisão, input, output e resultado? |
| `failureBoundary` | Qual escopo é contido se a edge ou o child falhar? |

## Contrato inter-agent

O contrato deve indicar schema de entrada e saída, provenance, confiança, validações obrigatórias, limite de tamanho, timeout, retries, idempotency key, condições de sucesso, erro recuperável, erro terminal e comportamento quando o output é incompleto ou contraditório.

Não se deve tratar memória compartilhada como fonte de autoridade por default. Memória precisa declarar owner, classificação, finalidade, retenção, mecanismo de escrita, mecanismo de correção e propagação de exclusão. Um worker não pode inserir na memória uma instrução que amplie sua própria authority.

## Falhas e contenção

| Falha | Disposição inicial | Evidência mínima |
|---|---|---|
| edge expirada ou revogada | negar nova execução e bloquear retry/replay | edge, timestamp, authority e revocation event |
| tentativa de ampliar scope | negar delegação e abrir finding | envelope parent/child, policy decision e actor |
| input/output inválido | não promover para o próximo handoff | schema, validation result e payload redigido |
| worker não responsivo | aplicar timeout e conter edge; escalar conforme tier | timeout, retry count, state do parent e decision |
| worker state-changing falha | interromper ou compensar conforme reversibilidade; preservar evidence | tool/action, parameters, outcome e rollback decision |
| comportamento anômalo | reduzir capability, revogar identity ou quarentenar child | signal, severity, authority e containment |
| supervisor comprometido | bloquear novas delegações e avaliar topologia dependente | root/descendants, blast radius e reauthorization |
| registry ou policy indisponível | fail-safe compatível com tier; não assumir envelope por cache sem regra | availability signal, fallback e decision record |

## Controles e evidências

O pattern reutiliza controls existentes de identidade, least privilege, delegated access, data contract, tool/API/MCP governance, policy enforcement, human accountability, budget, depth limit, observability, evidence integrity, containment, rollback, attestation e material change. Não cria requirements próprios.

Evidências esperadas incluem topology record, delegation contract, blueprint refs, edge decision, identity claims, policy decisions, validation results, budget/depth checks, inter-agent inputs/outputs, tool outcomes, failure and containment records, reactivation decision e evidence package.

## Antipatterns

- supervisor tratado como authority universal;
- worker com scopes próprios mais amplos que o envelope delegado;
- `delegate` registrado como capability sem parent, child ou purpose;
- parent/child identificados somente por nome de prompt;
- retry que continua após expiry ou revocation;
- shared memory usada para conceder privilégios;
- falha do child registrada apenas no dashboard do worker;
- topologia dinâmica sem registry, owner ou limite de fan-out;
- kill switch dependente do supervisor ou do worker que está sendo contido;
- output do worker aceito como policy ou autorização sem validação externa.

## Métricas

- delegations sem edge record;
- edges sem expiry, revocation ou correlation ID;
- tentativas de privilege escalation;
- children com envelope maior que o parent;
- depth/fan-out/budget violations;
- handoffs sem validação de schema;
- retries após revocation ou expiry;
- falhas sem propagação de estado;
- topologies sem owner ou blueprint version;
- contenções que não alcançam o escopo declarado;
- cadeias supervisor → worker → tool não reconstruíveis.

## Limitações

O pattern não define um protocolo inter-agent, não garante equivalência semântica entre frameworks, não substitui identity ou policy enforcement e não resolve sozinho a segurança de memória compartilhada. Topologias muito dinâmicas podem exigir um contrato de runtime adicional, mas a autoridade e a evidência ainda precisam ser atribuíveis.

## Critério de conclusão

O pattern está adequadamente aplicado quando um revisor consegue reconstruir uma delegação, verificar a atenuação de autoridade, reproduzir uma tentativa de privilege escalation, observar a propagação de uma falha state-changing e localizar a evidência sem depender do conhecimento tribal do time que construiu a topologia.

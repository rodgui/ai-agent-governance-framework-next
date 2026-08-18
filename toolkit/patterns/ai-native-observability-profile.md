---
title: Pattern — AI-Native Observability Profile
status: draft
owner: framework-maintainers
last_reviewed: 2026-08-18
review_cycle: quarterly
related:
  - README.md
  - ../../docs/architecture/decisions/0014-ai-native-observability-profile.md
  - ../../docs/framework/07-evaluation-evidence-and-assurance.md
  - ../../docs/framework/09-operations-incidents-and-continuity.md
  - ../schemas/audit-event.schema.json
  - ../templates/ai-native-observability-profile.md
---

# Pattern — AI-Native Observability Profile

## Intenção

Tornar reconstruível a cadeia de uma execução AI-native, de uma task ou delegation até model, retrieval, policy, tool, human intervention, containment, outcome e value/cost, sem exigir um dashboard ou fornecedor único.

> **Crosswalk de observabilidade.** O modelo em 8 camadas do [capítulo 09](../../docs/framework/09-operations-incidents-and-continuity.md) define **WHAT** precisa ser observável. Este profile define **HOW** uma execução agentic material é correlacionada semanticamente. O [audit-event schema](../schemas/audit-event.schema.json) define o **MINIMUM** machine-readable event envelope; ele não representa sozinho toda a semântica do profile.

## Problema

Eventos tradicionais registram request, response e erro, mas sistemas agentic introduzem planning, retries, tool selection, retrieval, memory, delegation, policy decisions, human step-up, loops e contenção. Sem um modelo semântico comum, a organização pode ter telemetria abundante e ainda não responder quem fez o quê, sob qual authority, com quais dados, qual resultado e qual custo.

## Quando usar

Use este pattern quando um agente possui tools, retrieval, memory, delegation, ações state-changing, dados sensíveis, exposição externa, requirements de incident reconstruction ou dependências em múltiplas plataformas. Em sistemas simples de leitura sem persistência, o envelope mínimo de audit event pode ser suficiente.

## Princípios

1. **Task-centered:** a task e seu outcome são a unidade de reconstrução; requests isolados não são suficientes.
2. **Correlation first:** parent/child, session, task, tool, policy e evidence compartilham uma chave comum ou referências navegáveis.
3. **Provenance without payload hoarding:** registre origem, versão e decisão; não capture conteúdo sensível por conveniência.
4. **Policy and enforcement visible:** telemetry deve mostrar decisão, autoridade e ponto de enforcement sem transformar log em autorização.
5. **Delegation-aware:** supervisor, worker, delegated subject, edge, depth, budget e failure boundary são observáveis.
6. **Memory is data:** leitura, escrita, alteração e deleção de memória têm owner, classification, retention e policy decision.
7. **Operational closure:** signals levam a decision, action, evidence preservation, remediation, regression e reactivation.
8. **Value/cost separation:** uso, custo, qualidade e outcome não são a mesma métrica.
9. **Privacy by design:** minimization, redaction, retention, access e deletion fazem parte do perfil.

## Solução

Mantenha o envelope do `AI Agent Audit Event` e adicione um profile semântico por meio de event types, spans, logs ou references. O profile não precisa ser um schema único para todos os backends; precisa ser uma superfície comum de significado e correlação.

```text
task
 ├─ delegation / model / retrieval
 ├─ policy decision
 ├─ tool request → tool result
 ├─ human intervention / containment
 └─ outcome → value/cost → evidence
```

Cada sinal deve declarar source, owner, classification, retention, access, evidence reference e mapping opcional para a tecnologia de observability escolhida.

## Semântica de sinais

| Sinal lógico | Atributos essenciais | Limite de interpretação |
|---|---|---|
| `agent.task` | task, purpose, initiator, root agent, topology, risk, status, outcome | início/fim não prova valor |
| `agent.delegation` | delegation, parent, child, subject, scopes, budget, depth, expiry, policy | evento não concede authority |
| `model.call` | provider/model/version ref, role, data classes, evaluation ref, latency, outcome | modelo registrado não prova qualidade |
| `retrieval` | source/index ref, provenance, freshness, authorization, result | retrieval não prova que a fonte é correta |
| `tool.request/result` | tool/action, target ref, stateChanging, approval, policy, outcome | request não prova side effect concluído |
| `policy.decision` | policy/version, authority, enforcement, decision, reason | log não substitui enforcement |
| `human.intervention` | actor, authority, action, object, rationale, decision, expiry | presença não prova informed approval |
| `agent.memory/state` | state ref, operation, owner, classification, retention, policy | state ref não autoriza acesso |
| `containment` | signal, severity, scope, authority, action, evidence, reactivation | containment registrado não prova eficácia |
| `value/cost` | cost dimensions, outcome ref, attribution caveat, period | custo e uso não são valor |

## Fluxo de implementação

1. classificar o agente, task, topology, data classes e tier;
2. definir o correlation model e propagação parent/child;
3. mapear os events/spans para o audit event envelope existente;
4. declarar os atributos necessários e os que são proibidos por privacy/minimization;
5. instrumentar task, model, retrieval, policy, tool e outcome;
6. adicionar delegation e memory/state quando aplicável;
7. ligar signals à Run Authority, alert-to-action e containment;
8. definir retention, access, redaction, deletion e export;
9. medir cardinalidade, volume, custo e gaps de cobertura;
10. executar um drill de reconstrução e corrigir lacunas;
11. registrar limitações e claims sem evidence;
12. reavaliar o profile em material changes.

## Correlação e contexto

Propague `correlationId` e, quando aplicável, `taskId`, `parentTaskId`, `sessionId`, `topologyId`, `delegationId`, `agentId`, `agentVersion`, `policyDecisionRef`, `evidenceRef` e `traceParent`. IDs devem ser estáveis durante a execução, não conter dados pessoais por composição e não substituir authorization checks.

A propagação pode ocorrer por context, metadata, event envelope ou references entre sistemas. Se um componente não suporta propagação, o gap precisa ser declarado e a cadeia não deve ser apresentada como totalmente reconstruível.

## Privacy, redaction e access

Classifique prompts, traces, arguments, retrieval content, memory, outputs e error details como dados. Prefira references, hashes, counts e categorias quando o payload não for necessário. Defina quem pode consultar dados brutos, quem vê dados redigidos, quando o acesso é break-glass e como a evidência é preservada sem ampliar a superfície de exposição.

Retention deve ser proporcional ao tier, ao objetivo do evento e às obrigações aplicáveis. Deletion e subject requests devem considerar cópias, indexes, caches, backups e evidence holds. O profile não autoriza manter dados só porque o backend os captura por default.

## Operação e evidências

A cadeia operacional é:

```text
signal → severity → authority → action
       → evidence preservation → remediation
       → regression → reactivation
```

Evidências esperadas incluem coverage map, event/span mapping, correlation test, sample redacted trace, policy decision trail, delegation lineage, tool outcome, incident drill, containment record, retention/access decision, export test e limitações conhecidas.

## Mappings de implementação

Podem ser usados audit logs, distributed tracing, event buses, SIEM/SOAR, metrics backends, OpenTelemetry e conventions GenAI, desde que sejam adapters substituíveis. Um mapping de implementação não altera o envelope canônico nem cria assurance por si só.

## Métricas

- tasks sem início/fim correlacionável;
- spans/events sem `correlationId`;
- delegation edges sem lineage;
- tool calls sem policy decision ou outcome;
- retrievals sem provenance ou authorization result;
- memory/state events sem owner ou retention;
- containment sem authority ou evidence preservation;
- chains não reconstruíveis em drill;
- payloads capturados sem necessidade ou redaction;
- custo de telemetry por task e cardinalidade excessiva;
- value claims sem outcome evidence.

## Antipatterns

- dashboard único tratado como authoritative audit trail;
- tracing que captura prompts, secrets e tool arguments por default;
- correlation ID que contém identidade pessoal ou segredo;
- task success confundido com business value;
- token count confundido com unit economics;
- policy decision registrada depois do enforcement sem relação temporal;
- supervisor/worker sem delegation lineage;
- memory observada sem access, retention ou deletion governance;
- OpenTelemetry ou vendor convention tratada como compliance;
- cobertura de eventos usada como prova de eficácia do controle.

## Limitações

O pattern não define protocolo de transporte, não garante que sistemas legados propaguem contexto, não mede sozinho factualidade, fairness, segurança ou eficácia e não substitui audit event, policy, assurance, incident response ou privacy governance. Perfis AI-native devem começar com uma população e um caso de uso delimitados para evitar instrumentação excessiva sem consumidor de decisão.

## Critério de conclusão

O pattern está adequadamente aplicado quando um revisor autorizado reconstrói uma task multiagente por correlation ID, identifica parent/child, model/retrieval, policy, tool, human intervention, containment e outcome, verifica redaction/retention/access e reproduz o fluxo sem depender de dashboard proprietário ou pesquisa manual em sistemas desconectados.

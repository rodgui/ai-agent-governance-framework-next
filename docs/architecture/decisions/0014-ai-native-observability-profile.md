---
title: ADR-0014 — Profile opcional de observabilidade AI-native
status: draft
owner: framework-maintainers
last_reviewed: 2026-08-17
review_cycle: major-change
supersedes: null
related:
  - ../README.md
  - ../../framework/07-evaluation-evidence-and-assurance.md
  - ../../framework/09-operations-incidents-and-continuity.md
  - ../../../toolkit/schemas/audit-event.schema.json
  - ../../../toolkit/patterns/ai-native-observability-profile.md
  - ../../../toolkit/templates/ai-native-observability-profile.md
  - ../../../toolkit/examples/ai-native-observability.example.md
---

# ADR-0014 — Profile opcional de observabilidade AI-native

## Status e escopo

Esta é uma **decisão arquitetural em rascunho** da frente G4. Define um profile semântico opcional para tornar observáveis tarefas, delegações, chamadas de modelo, retrieval, tools, policy decisions, intervenções humanas, memória/estado, contenção e valor/custo em sistemas de IA e topologias multiagente.

O profile complementa o envelope existente do [AI Agent Audit Event schema](../../../toolkit/schemas/audit-event.schema.json). Não altera o schema `1.0`, não cria um novo control, não obriga OpenTelemetry, não exige uma plataforma de observability específica e não autoriza capturar prompts, payloads, segredos ou dados pessoais sem finalidade, classificação, minimização e retenção aprovadas.

A decisão permanece `draft` até ser exercitada com uma execução fictícia e uma implementação autorizada, incluindo reconstrução de incidente, privacy review, teste de exportação e validação de cardinalidade/custo.

## Contexto

O framework já exige eventos atribuíveis, correlation IDs, outcome, policy decision, data classifications, redaction, evidence references, baselines comportamentais, alert-to-action, containment, quarantine, rollback e reactivation. O schema de audit event cobre um envelope mínimo para session, model call, retrieval, tool request/result, approval, policy decision, containment e session end.

A evolução para sistemas AI-native cria perguntas adicionais: qual task gerou uma cadeia de calls; qual agente delegou para qual worker; qual retrieval provenance influenciou a resposta; qual modelo e versão foram usados; quais tools foram escolhidas e com quais scopes; qual policy decidiu; qual memória foi lida ou alterada; qual pessoa interveio; e quanto custo e valor foram atribuídos à execução.

Sem uma semântica comum, uma organização pode ter muitos dashboards e ainda precisar juntar manualmente logs de runtime, gateway, IAM, policy, data, model provider, FinOps e incident response. O profile deve melhorar a interoperabilidade sem transformar uma convenção de telemetria em evidência automática de segurança, qualidade ou compliance.

## Decisão proposta

1. **O envelope mínimo existente permanece a base canônica.** Todo evento material conserva `eventId`, `timestamp`, `agentId`, `agentVersion`, `eventType`, `actor`, `correlationId`, `outcome`, `policyDecision`, `dataClassifications`, `redactionApplied` e `evidenceRef` quando aplicável.

2. **O profile define semântica, não uma implementação única.** Uma organização pode implementar o profile com events, traces, spans, logs ou uma combinação. OpenTelemetry GenAI conventions podem ser um mapping opcional; não são requisito normativo nesta ADR.

3. **A unidade de reconstrução é a task e sua cadeia de execução.** Cada task possui `taskId`, finalidade, initiator, rootAgent, topology/version, parentTaskId quando aplicável, status, outcome, riskTier, data classes e evidence reference.

4. **Delegação é uma dimensão observável própria.** Uma `agent.delegation` liga parent, child, delegationId, purpose, task, attenuatedScopes, budget, depth, fan-out, expiry, revocation, policy decision e outcome. A semântica deve reutilizar o contrato G2 quando disponível.

5. **Model, retrieval, tool e policy possuem provenance separada.** Eventos registram referências, versões, decisão e outcome sem exigir payload bruto. Argumentos sensíveis devem ser classificados, redigidos, tokenizados ou substituídos por hashes/identificadores conforme a finalidade de investigação.

6. **Memória e estado são dados governados.** Um `agent.memory` ou `agent.state` registra operação, owner, classificação, finalidade, retention, state reference e policy decision. O profile não autoriza persistência nem leitura; apenas torna a decisão observável.

7. **Intervenção humana é um evento atribuível.** `human.intervention` registra authority, actor, action, object, rationale, decision, timestamp, expiry e evidence. Um login ou presença no canal não prova informed approval.

8. **Containment e reactivation fecham o ciclo operacional.** Eventos de contenção devem ligar signal, severity, authority, scope, action, evidence preservation, remediation, regression e reactivation decision.

9. **Value e cost permanecem distintos.** O profile pode correlacionar tokens, calls, latency, tool cost, storage, egress, task cost e outcome, mas não trata uso, adoção ou gasto como prova de valor realizado.

10. **Privacy, minimization e redaction são parte do profile.** Cada implementação declara quais atributos são necessários, quem pode acessá-los, por quanto tempo são retidos, como são redigidos e como exportação e deletion requests são tratados.

11. **Observability não substitui assurance.** Um trace completo prova que certos eventos foram emitidos e correlacionados; não prova que a policy estava correta, que o modelo foi seguro, que o outcome foi justo ou que o controle foi eficaz.

## Semântica mínima do profile

| Signal/span lógico | Pergunta respondida | Referências mínimas |
|---|---|---|
| `agent.task` | Qual tarefa, finalidade, initiator e outcome estão sendo governados? | `taskId`, `correlationId`, `agentId`, `purpose`, `status`, `outcome`, `riskTier` |
| `agent.delegation` | Qual agente delegou para qual agente e com qual envelope? | `delegationId`, parent/child, scopes, data classes, budget, depth, expiry, policy decision |
| `model.call` | Qual combinação provider/model/version foi usada e com qual finalidade? | model/provider/version refs, role, data classes, latency, outcome, evaluation ref |
| `retrieval` | Quais fontes autorizadas influenciaram o contexto? | source/index refs, provenance, freshness, authorization decision, result status |
| `tool.request` / `tool.result` | Qual tool/action foi chamada e qual efeito ocorreu? | tool ref, action, stateChanging, target ref, approval/policy refs, outcome |
| `policy.decision` | Qual policy permitiu, negou, condicionou ou escalou? | policy ref/version, decision, reason, authority, enforcement point |
| `human.intervention` | Qual authority humana revisou, aprovou, editou, negou ou interrompeu? | actor, authority, object, decision, rationale, expiry, evidence |
| `agent.memory` / `agent.state` | Qual estado foi lido, criado, alterado ou eliminado? | state ref, operation, owner, data class, retention, policy decision |
| `containment` | Qual signal produziu throttle, revocation, quarantine, rollback ou sunset? | signal, severity, scope, authority, action, evidence preservation, reactivation |
| `value.cost` | Qual custo e qual outcome foram atribuídos à task? | cost dimensions, outcome ref, attribution caveat, period, owner |

## Propagação e correlação

O profile exige uma chave comum por execução e uma relação explícita entre parent e child spans/events. A correlação deve responder, sem pesquisa manual em sistemas desconectados:

```text
initiator → task → agent/topology → delegation → model/retrieval
          → policy → tool/action → human intervention/containment
          → outcome → value/cost → evidence package
```

A correlação não autoriza centralizar todos os dados. Sistemas especializados podem manter seus eventos locais, desde que emitam referências compatíveis, preservem provenance e permitam reconstrução autorizada. A arquitetura deve declarar quais campos são exportáveis, quais são apenas references e quais ficam sujeitos a minimização ou retenção curta.

## Não decidido nesta ADR

Esta ADR não altera `audit-event.schema.json`, não cria enums obrigatórios para todos os spans, não escolhe backend, collector, vendor, protocol ou dashboard, não determina retenção universal, não define fórmula de valor, não exige captura de prompt/payload e não transforma observability coverage em assurance de eficácia.

## Consequências positivas

O profile cria uma linguagem comum para task, delegation, tool, policy, memory, containment e outcome. Ele reduz a dependência de dashboards específicos, facilita incident reconstruction, torna o G2 observável, permite mapping opcional para convenções abertas e fornece uma base melhor para cost/value attribution e evidence packages.

## Custos e consequências negativas

Instrumentação adicional aumenta custo, cardinalidade, volume de dados, risco de exposição e carga operacional. Correlation IDs e references precisam ser propagados por plataformas que talvez não suportem o modelo. O profile exige governança de privacy, access, retention, deletion e export e não elimina a necessidade de adapters.

## Critérios de validação

- uma task multiagente pode ser reconstruída pelo `correlationId`;
- a cadeia task → delegation → model/retrieval → policy → tool → outcome é navegável;
- uma policy denial e uma containment action são ligadas à authority e à evidência;
- campos sensíveis são redigidos ou referenciados sem payload indevido;
- memory/state registra owner, operation, classification e retention;
- uma intervenção humana é atribuível e não é inferida apenas pela presença do usuário;
- custo e outcome ficam distintos e recebem caveats de atribuição;
- exportação e reconstrução funcionam sem depender de dashboard proprietário;
- um drill de incidente preserva evidence e executa containment;
- o profile não exige alteração imediata de schema ou vendor.

## Evidência e aprovação

A decisão precisa ser exercitada com o [profile de observabilidade AI-native](../../../toolkit/patterns/ai-native-observability-profile.md), o [template](../../../toolkit/templates/ai-native-observability-profile.md) e o [exemplo fictício](../../../toolkit/examples/ai-native-observability.example.md). A aprovação deve registrar cobertura, limitações, privacy review, custo/cardinality review, export test, retention decision e data de revisão.

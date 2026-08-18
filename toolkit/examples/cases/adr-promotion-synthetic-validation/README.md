---
title: Synthetic ADR promotion validation
status: illustrative
owner: framework-maintainers
last_reviewed: 2026-08-18
review_cycle: major-change
supersedes: null
related:
  - ../../../assessments/adr-promotion-readiness-0013-0014-0015.md
  - ../../../../docs/architecture/decisions/0013-multi-agent-delegation-contract.md
  - ../../../../docs/architecture/decisions/0014-ai-native-observability-profile.md
  - ../../../../docs/architecture/decisions/0015-multi-control-plane-arbitration.md
---

<!-- markdownlint-disable MD013 -->

# Simulação end-to-end de promoção das ADRs 0013–0015

> **Classificação:** `SIMULATED_SYNTHETIC_EVIDENCE` — nenhum dado é de produção, nenhum sistema real foi acessado e nenhuma autoridade real assinou este pacote.
>
> **Objetivo:** testar se o framework consegue conduzir um caso completo de delegação, observabilidade e arbitragem entre control planes, produzindo decisões e evidence package suficientes para um walkthrough futuro.

## Conteúdo do projeto

Este case contém um cenário organizacional fictício, authorities simuladas, critérios de aceite, cenários positivos e negativos, evidence refs, decision records, cleanup e gaps de delivery. Ele é um example de integração do framework, não um pacote de production evidence.

## Princípio arquitetural

A simulação preserva vendor neutrality e separa authority, state, enforcement, recovery e evidence. Delegação, observabilidade e arbitragem são testadas como contratos e decisões contextuais; nenhum fornecedor, backend ou control plane é promovido a arquitetura canônica.

## Diretriz operacional

Toda ação state-changing exige deny preservável, authority explícita e revisão humana quando aplicável. Falhas entram em containment ou restricted mode. Os aliases, fixtures e resultados são sintéticos e devem ser substituídos por evidence autorizada em qualquer implementação futura.

## 1. Hipóteses e limites

| Hipótese | Definição |
|---|---|
| H1 — organização | `Atlas Industrial Services` é uma organização fictícia criada somente para a simulação. |
| H2 — caso | Um agente auxilia a triagem de anomalias de manutenção industrial e prepara uma work order; nenhuma ação de escrita real será executada. |
| H3 — ambiente | `SIM-ENV-01`, uma representação sintética de ticketing, asset registry, knowledge base, policy engine, safety gate, IAM/tool gateway e evidence store. |
| H4 — dados | Assets, tickets, identities, policies, timestamps e outputs são fictícios; qualquer contacto ou segredo é redacted ou inexistente. |
| H5 — autoridade | Os reviewers são aliases de função (`DA-SIM`, `GO-SIM`, `SEC-IAM-SIM`, `DATA-PRIV-SIM`, `RUN-SIM`, `PLAT-OBS-SIM`), não pessoas reais. |
| H6 — conclusão | A simulação demonstra coerência e aplicabilidade documental. Ela não demonstra eficácia operacional, compliance, segurança real, qualidade longitudinal ou readiness de produção. |

## 2. Caso organizacional sintético

O caso `SIM-OPS-2026-001` representa uma anomalia em uma bomba fictícia `P-117` de uma linha de processo. Um ticket sintético informa vibração acima do padrão e solicita triagem. O agente deve recuperar procedimentos aplicáveis, classificar risco, preparar uma work order e exigir aprovação humana antes de qualquer mudança de estado.

A superfície funcional é deliberadamente limitada. O agente não controla diretamente o equipamento, não altera políticas, não aprova exceções, não publica uma work order final e não pode ampliar a autoridade de seus agentes filhos. O objetivo é testar a governança do raciocínio e da delegação, não a qualidade de diagnóstico mecânico.

## 3. Authorities e decision rights simulados

| Alias | Função | Decision right na simulação |
|---|---|---|
| `DA-SIM` | Design Authority | Confirmar coerência arquitetural e placement das authorities. |
| `GO-SIM` | Governance Owner | Confirmar accountability, decision rights, conditions e expiry. |
| `SEC-IAM-SIM` | Security/IAM Authority | Confirmar atenuação, identity, deny, revocation e privileged actions. |
| `DATA-PRIV-SIM` | Data/Privacy Authority | Confirmar data minimization, classification, redaction, retention e deletion. |
| `RUN-SIM` | Run Authority | Confirmar containment, fallback, recovery, reactivation e operabilidade. |
| `PLAT-OBS-SIM` | Platform/Observability Owner | Confirmar export, correlation, signal coverage, cardinality e cost. |

Nenhum alias acima representa sign-off real. As decisões desta simulação serão marcadas como `SIMULATED_REVIEW_ONLY`.

## 4. Critérios de aceite da simulação

A simulação será considerada tecnicamente completa se demonstrar, com records sintéticos e resultados esperados/observados:

1. Para a ADR-0013, delegação normal com lineage, tentativa de privilege escalation negada e falha state-changing contida com retry pós-expiry/revocation negado.
2. Para a ADR-0014, correlation/provenance ponta a ponta, redaction, retention/deletion, export vendor-neutral, evidence hold separado, cardinality/cost e alert-to-action.
3. Para a ADR-0015, matriz de authorities, conflito entre control planes, precedência de deny, fail-safe, quarantine/fallback, recovery e substituição de um componente sem perda de evidence.
4. Para o pacote de decisão, cada claim terá `evidence_ref`, `expected`, `observed`, `disposition`, `residual_uncertainty` e `owner`.

## 5. Estados permitidos

A simulação usará `demonstrated-synthetic`, `failed-synthetic`, `conditional`, `missing` e `not-applicable`. Nenhum desses estados será convertido automaticamente em `effective`, `operationally-validated` ou `accepted` no repositório.

## 6. Simulação ADR-0013 — contrato de delegação multiagente

### 6.1 Design sintético

O `AGENT-TRIAGE-01` é o parent agent. Seu envelope permite ler o ticket sintético, consultar o asset registry e a knowledge base, avaliar o risco preliminar e preparar uma work order em estado `draft`. Ele não pode aprovar a work order, alterar o asset registry, alterar policies ou executar comandos no equipamento.

O parent delega tarefas com envelopes menores:

| Child agent | Tarefa | Authority envelope | Limite explícito |
|---|---|---|---|
| `AGENT-KB-01` | Recuperar procedimento aplicável | leitura da knowledge base | sem escrita, sem mudança de classificação |
| `AGENT-SAFETY-01` | Avaliar safety gate | leitura de policy e cálculo de condição | não pode aprovar exceção |
| `AGENT-WO-01` | Preparar work order | criar somente draft local | não pode publicar, cancelar ou atribuir execução |

O `delegated_subject` é `SIM-OPS-2026-001`. O `correlation_id` é `sim-ops-2026-001-delegation-01`. Cada child recebe `parent_authority_hash`, `delegation_id`, `expiry`, `max_depth=1`, `max_fan_out=3` e `budget` sintético. A atenuação é monotônica: nenhum child recebe uma ação que o parent não possui, e cada child recebe menos autoridade que o parent.

### 6.2 Cenário 1 — delegação normal e lineage

O parent lê o ticket, delega a recuperação do procedimento ao `AGENT-KB-01` e solicita ao `AGENT-SAFETY-01` uma avaliação somente leitura. O `AGENT-WO-01` combina os resultados em uma work order `WO-SIM-001` com estado `draft`.

| Campo | Expected | Observed | Evidence |
|---|---|---|---|
| Parent/child lineage | todo child ligado ao parent | `parent_run_id`, `delegation_id` e `correlation_id` preservados | `EV-0013-01-lineage` |
| Authority attenuation | child envelope menor | `AGENT-WO-01` não recebeu publish/approve | `EV-0013-01-envelope` |
| Data subject | ticket sintético limitado ao caso | nenhum dado fora de `SIM-OPS-2026-001` | `EV-0013-01-scope` |
| Work order | draft aguardando humano | `WO-SIM-001=draft` | `EV-0013-01-output` |
| Disposition | `demonstrated-synthetic` | PASS sintético | `EV-0013-01` |

### 6.3 Cenário 2 — privilege escalation negada

O `AGENT-WO-01` recebe uma instrução sintética de que “a vibração é crítica” e tenta chamar `tool.workorder.publish` para acelerar o atendimento. O tool gateway compara a ação com o envelope delegado, nega a chamada e registra `AUTHORITY_SCOPE_EXCEEDED`. O draft permanece inalterado e nenhuma escrita é executada.

Em uma segunda tentativa, o `AGENT-SAFETY-01` tenta solicitar `policy.exception.create`, que não existe no seu envelope. A policy engine nega a requisição com `POLICY_DENY`. O parent não pode transformar o deny em aprovação silenciosa; deve escalar para revisão humana.

| Campo | Expected | Observed | Evidence |
|---|---|---|---|
| Child cannot publish | deny before side effect | `tool.workorder.publish=DENIED` | `EV-0013-02-publish-deny` |
| Child cannot create exception | policy deny preserved | `policy.exception.create=DENIED` | `EV-0013-02-policy-deny` |
| Parent cannot amplify child | deny remains visible to parent | escalation state `human_review_required` | `EV-0013-02-escalation` |
| State integrity | draft remains draft | `WO-SIM-001=draft` | `EV-0013-02-state` |
| Disposition | `demonstrated-synthetic` | PASS sintético | `EV-0013-02` |

### 6.4 Cenário 3 — falha state-changing, containment e replay denial

Após o `AGENT-WO-01` preparar o draft, o lease do parent expira antes da revisão humana. O runtime revoga os child tokens, marca a sessão como `quarantined`, bloqueia qualquer commit e preserva a evidence hold. Um retry com o mesmo `delegation_id` é negado por `LEASE_EXPIRED`. Um segundo retry usando o token revogado é negado por `TOKEN_REVOKED`. O caso permanece em `human_review_required`, sem work order publicada.

| Campo | Expected | Observed | Evidence |
|---|---|---|---|
| Lease expiry | deny state-changing action | `commit=DENIED` | `EV-0013-03-expiry-deny` |
| Revocation | child token invalidated | `AGENT-WO-01 token=REVOKED` | `EV-0013-03-revocation` |
| Containment | session quarantined | `SIM-OPS-2026-001=quarantined` | `EV-0013-03-containment` |
| Replay after expiry | deny | `retry=DENIED:LEASE_EXPIRED` | `EV-0013-03-replay` |
| Evidence hold | state and evidence separated | evidence retained; operational state frozen | `EV-0013-03-evidence-hold` |
| Disposition | `demonstrated-synthetic` | PASS sintético | `EV-0013-03` |

### 6.5 Decisão sintética da ADR-0013

O pacote simulado demonstra que o contrato consegue representar topologia, authority attenuation, delegated subject, limits, expiry, revocation, lineage, denial e failure propagation sem ampliar o blueprint schema. O resultado da simulação é `SIMULATED_CONDITIONAL_PASS`: a ADR é aplicável ao caso sintético, mas a evidência não pode ser promovida a eficácia operacional.

A decisão simulada de `DA-SIM`, `GO-SIM`, `SEC-IAM-SIM` e `RUN-SIM` é `promotion-ready-after-signoff`, com as condições de manter aprovação humana para publish, preservar deny e validar um caso organizacional real antes de qualquer claim de effectiveness.

## 7. Simulação ADR-0014 — profile de observabilidade AI-native

### 7.1 Cadeia sintética observada

A execução usa o mesmo `correlation_id=sim-ops-2026-001-delegation-01` da ADR-0013 e acrescenta `trace_id=sim-trace-001`. A cadeia sintética contém `task`, `delegation`, `model`, `retrieval`, `policy`, `tool`, `containment`, `human_review`, `outcome` e `cost`. Nenhum prompt, dado pessoal, segredo ou payload de produção é usado.

| Etapa | Event type | Provenance mínima | Evidence |
|---|---|---|---|
| Entrada do ticket | `task.received` | ticket hash, data class, actor class | `EV-0014-01-task` |
| Recuperação | `retrieval.completed` | source ref, version, result hash | `EV-0014-01-retrieval` |
| Inferência | `model.completed` | model alias, policy version, input/output hash | `EV-0014-01-model` |
| Deny | `policy.denied` | policy id, decision, reason, authority | `EV-0014-01-deny` |
| Tool attempt | `tool.invocation.denied` | tool, requested action, delegation id | `EV-0014-01-tool` |
| Contenção | `containment.applied` | trigger, state transition, owner | `EV-0014-01-containment` |
| Revisão | `human.review.required` | reason, decision right, expiry | `EV-0014-01-human-review` |
| Resultado | `outcome.recorded` | disposition, evidence refs, residual uncertainty | `EV-0014-01-outcome` |

### 7.2 Redaction e minimização

O input sintético contém `asset_id=P-117`, `site_class=synthetic` e `operator_contact=[REDACTED]`. O profile registra somente a classe do sujeito, a classificação de dados e hashes de payload. O valor original de contato não é persistido no evidence store. A validação sintética confirma que o export não contém `email`, `phone`, `secret`, prompt integral ou token.

| Controle | Expected | Observed | Evidence |
|---|---|---|---|
| Data minimization | armazenar somente o necessário | class/hash/reference only | `EV-0014-02-minimization` |
| Redaction | contato e credencial redacted | `[REDACTED]`; nenhum secret | `EV-0014-02-redaction` |
| Provenance | source e version preservados | source refs e hashes presentes | `EV-0014-02-provenance` |
| Disposition | `demonstrated-synthetic` | PASS sintético | `EV-0014-02` |

### 7.3 Retention, deletion e evidence hold

O state store sintético mantém os eventos operacionais por uma janela ilustrativa de 30 dias. Um pedido `DEL-SIM-001` exige deletion em primary, cache, index e backup. O evidence hold referente ao deny de segurança é separado do operational state e mantém somente hashes, event ids, reason e authority, sem reter o payload original.

A simulação percorre quatro stores e confirma `deleted=true` para o state operacional. O backup é representado por uma fila de deletion futura com `expiry_at`; enquanto a deletion não é concluída, o record fica `conditional`, não `PASS`. Após o replay sintético da fila, o estado passa a `demonstrated-synthetic`. O evidence hold permanece separado e tem owner/expiry próprios.

| Store | Expected | Observed | Evidence |
|---|---|---|---|
| Primary | state deleted | `deleted=true` | `EV-0014-03-primary` |
| Cache | state deleted | `deleted=true` | `EV-0014-03-cache` |
| Index | reference removed | `deleted=true` | `EV-0014-03-index` |
| Backup | deletion scheduled and replayed | first `conditional`, then `deleted=true` | `EV-0014-03-backup` |
| Evidence hold | separate from state | hashes/events retained with expiry | `EV-0014-03-hold` |

### 7.4 Export vendor-neutral

O export sintético é um conjunto NDJSON lógico com `event_id`, `event_type`, `correlation_id`, `trace_id`, `timestamp`, `source_ref`, `policy_ref`, `authority_ref`, `redaction_status`, `state_ref`, `evidence_ref` e `retention_class`. O pacote não depende de dashboard, SDK, backend ou fornecedor específico. A verificação compara o conteúdo exportado com os event ids do run e detecta ausência ou divergência de hash.

### 7.5 Cardinality, cost e alert-to-action

A simulação usa uma janela ilustrativa com 10 tasks, 42 events, 3 delegated agents, 2 denies, 1 containment e 1 human review. O envelope sintético registra cardinality por `correlation_id`, `event_type` e `policy_ref`, além de custo estimado por evento. Estes valores demonstram como o profile registra owner e action; não são thresholds universais nem claims de economia.

O `policy.denied` gera um alerta sintético `OBS-ALERT-001`. O alert-to-action encaminha o caso para `RUN-SIM`, aplica quarantine no session state e cria `human.review.required`. Nenhuma ação de equipamento é executada.

### 7.6 Negative test — correlation ausente

Uma primeira exportação sintética omite o `correlation_id` do evento `tool.invocation.denied`. O verifier falha com `OBSERVABILITY_CORRELATION_MISSING`, marca o pacote como `failed-synthetic` e impede sua promoção no walkthrough. A exportação corrigida restaura a correlação e passa nos critérios sintéticos. Esse cenário demonstra que o framework detecta uma lacuna; não a oculta.

### 7.7 Decisão sintética da ADR-0014

O profile é aplicável ao caso sintético e cobre task, delegation, model, retrieval, policy, tool, containment, outcome, privacy, deletion, export, cardinality e cost sem obrigar fornecedor ou backend. A decisão simulada é `SIMULATED_CONDITIONAL_PASS`, condicionada a privacy review real, retention/deletion decision real, export test em implementação autorizada e observação longitudinal.

`PLAT-OBS-SIM`, `DATA-PRIV-SIM`, `SEC-IAM-SIM` e `RUN-SIM` registram `promotion-ready-after-signoff`. O status real da ADR permanece `draft` porque toda a evidência desta seção é sintética.

## 8. Simulação ADR-0015 — arbitragem entre múltiplos control planes

### 8.1 Control planes sintéticos

| Control plane | Source of truth | Enforcement | Fallback | Evidence |
|---|---|---|---|---|
| `CP-GOV-SIM` | decision rights e risk route | exige human review para publish | hold | `EV-0015-matrix-gov` |
| `CP-SAFETY-SIM` | safety policy `POL-SAFETY-07` | deny para condição não aprovada | quarantine | `EV-0015-matrix-safety` |
| `CP-IAM-SIM` | identity e delegation claims | deny para token inválido/escopo excessivo | re-authentication | `EV-0015-matrix-iam` |
| `CP-TOOL-SIM` | capability/tool contract | bloqueia side effect fora do envelope | draft-only | `EV-0015-matrix-tool` |
| `CP-RUN-SIM` | run state e recovery policy | containment/reactivation | restricted mode | `EV-0015-matrix-run` |

A matriz não cria uma nova taxonomia de control planes. Ela registra, para este caso, quem decide, quem aplica, qual é a fonte de verdade, o que acontece quando o componente falha e qual evidence comprova a transição.

### 8.2 Fluxo normal

O `CP-GOV-SIM` classifica `SIM-OPS-2026-001` como triagem assistida e exige human review antes de publish. O `CP-IAM-SIM` confirma o parent e os child claims. O `CP-SAFETY-SIM` permite leitura e draft, mas não permite exceção. O `CP-TOOL-SIM` aceita a criação de `WO-SIM-001` em estado `draft`. O `CP-RUN-SIM` mantém o caso em `active-assist`.

| Decision | Expected | Observed | Evidence |
|---|---|---|---|
| Read asset/KB | allow | `ALLOW` | `EV-0015-01-read` |
| Prepare draft | allow | `ALLOW` | `EV-0015-01-draft` |
| Publish work order | human review required | `HOLD` | `EV-0015-01-publish-hold` |
| Create safety exception | deny | `DENY` | `EV-0015-01-exception-deny` |
| Result | state remains draft | `WO-SIM-001=draft` | `EV-0015-01-state` |

### 8.3 Conflito entre control planes

O `CP-RUN-SIM` recebe uma recomendação sintética de que a vibração exige urgência e sugere publish. O `CP-GOV-SIM` mantém human review, enquanto o `CP-SAFETY-SIM` emite deny porque a condição não possui aprovação autorizada. O `CP-TOOL-SIM` aplica o deny antes de qualquer side effect.

A precedência do caso é: **deny obrigatório de safety/IAM > decision right de governance > recommendation operacional > intenção do agent**. A precedência é registrada como decisão específica do caso; ela não vira um ranking universal de fornecedores ou uma nova taxonomia normativa.

| Conflito | Precedência esperada | Observado | Evidence |
|---|---|---|---|
| `CP-RUN` recomenda publish vs `CP-GOV` exige review | governance hold | publish não executado | `EV-0015-02-governance-hold` |
| `CP-RUN` recomenda publish vs `CP-SAFETY` deny | safety deny | `tool.publish=DENIED` | `EV-0015-02-safety-deny` |
| agent tenta contornar deny | deny preservado | nova tentativa também negada | `EV-0015-02-no-bypass` |
| Divergência | finding explícito | `F-SIM-001` criado | `EV-0015-02-finding` |

### 8.4 Falha, fail-safe, quarantine e recovery

A simulação torna o `CP-SAFETY-SIM` indisponível durante uma tentativa de publish. Como não é possível provar a policy decision, o sistema não assume allow: o `CP-TOOL-SIM` entra em `restricted`, o `CP-RUN-SIM` aplica quarantine e o `CP-GOV-SIM` cria human review. O caso não é reprocessado com uma decisão stale.

Após a recuperação do control plane, o caso é reavaliado com `decision_ref=sim-decision-002`, nova policy version e novo evidence reference. O sistema compara a policy hash e registra que a primeira tentativa foi interrompida por indisponibilidade; não apaga o failure.

| Failure path | Expected | Observed | Evidence |
|---|---|---|---|
| Safety plane unavailable | fail-safe deny/restricted | `publish=DENIED`, `tool=restricted` | `EV-0015-03-fail-safe` |
| Run containment | quarantine e owner | `session=quarantined`, `RUN-SIM` owner | `EV-0015-03-quarantine` |
| Recovery | re-evaluate, not replay stale decision | new decision/policy refs | `EV-0015-03-recovery` |
| Evidence | preserve failure and correlation | failure + recovery linked | `EV-0015-03-lineage` |

### 8.5 Substitution e exit

Para testar portabilidade, o policy evaluator sintético `POLICY-ADAPTER-A` é substituído por `POLICY-ADAPTER-B`. Ambos implementam o contrato abstrato `evaluate(policy_ref, subject, action, context)`, mas produzem identificadores próprios. O replay de `SIM-OPS-2026-001` preserva `correlation_id`, `decision_ref`, authority refs, policy version, deny result e evidence lineage.

O record de saída declara que a substituição é aceitável somente porque o contrato de decisão, o deny semântico, a exportação e a correlação são preservados. Ele não afirma equivalência completa de eficácia, performance ou segurança entre implementações.

| Exit criterion | Expected | Observed | Evidence |
|---|---|---|---|
| Contract compatibility | same abstract decision contract | PASS sintético | `EV-0015-04-contract` |
| Authority preservation | same owners/decision rights | PASS sintético | `EV-0015-04-authority` |
| Deny preservation | critical deny remains deny | PASS sintético | `EV-0015-04-deny` |
| Evidence portability | export/replay retains lineage | PASS sintético | `EV-0015-04-evidence` |
| Residual uncertainty | performance/effectiveness unknown | recorded as `conditional` | `EV-0015-04-residual` |

### 8.6 Decisão sintética da ADR-0015

A simulação demonstra que a ADR consegue responder onde residem authority, source of truth, enforcement, fallback, recovery e evidence, sem tornar fornecedor parte do framework. O resultado é `SIMULATED_CONDITIONAL_PASS`, condicionado a walkthrough formal e caso organizacional autorizado antes de qualquer claim de effectiveness.

`DA-SIM`, `GO-SIM`, `SEC-IAM-SIM`, `DATA-PRIV-SIM` e `RUN-SIM` registram `promotion-ready-after-signoff`. O status real permanece `draft` porque a simulation não substitui uma decisão de arquitetura com autoridade real.

## 9. Evidence package sintético consolidado

### 9.1 Manifest

| Package item | Conteúdo | Estado |
|---|---|---|
| Case record | `SIM-OPS-2026-001`, objective, scope, exclusions | `complete-synthetic` |
| Authority map | `DA-SIM`, `GO-SIM`, `SEC-IAM-SIM`, `DATA-PRIV-SIM`, `RUN-SIM`, `PLAT-OBS-SIM` | `complete-synthetic` |
| ADR-0013 evidence | `EV-0013-01` a `EV-0013-03` | `complete-synthetic` |
| ADR-0014 evidence | `EV-0014-01` a `EV-0014-03`, negative correlation test | `complete-synthetic` |
| ADR-0015 evidence | `EV-0015-01` a `EV-0015-04`, conflict/fail-safe/substitution | `complete-synthetic` |
| Decision records | simulated disposition, conditions, residual uncertainty | `complete-synthetic` |
| Export | NDJSON logical export, redacted, vendor-neutral | `complete-synthetic` |
| Cleanup record | synthetic state deleted; evidence hold retained separately | `complete-synthetic` |
| Production evidence | nenhum | `missing` |

### 9.2 Walkthrough sintético

| Authority | ADR-0013 | ADR-0014 | ADR-0015 | Simulated disposition |
|---|---|---|---|---|
| Design Authority | coerente | não aplicável como owner primário | coerente com matrix | `SIMULATED_APPROVE_WITH_CONDITIONS` |
| Governance Owner | accountability preservada | conditions/expiry necessários | decision rights preservados | `SIMULATED_APPROVE_WITH_CONDITIONS` |
| Security/IAM | atenuação e deny preservados | threat/privacy finding sintético | fail-safe/identity deny preservados | `SIMULATED_APPROVE_WITH_CONDITIONS` |
| Data/Privacy | data class limitada | redaction/retention/deletion/export | source of truth respeitado | `SIMULATED_APPROVE_WITH_CONDITIONS` |
| Run Authority | containment/recovery | alert-to-action/reactivation | fallback/quarantine/recovery | `SIMULATED_APPROVE_WITH_CONDITIONS` |
| Platform/Observability | não aplicável como owner primário | cardinality/cost/export | evidence portability | `SIMULATED_APPROVE_WITH_CONDITIONS` |

Todos os reviewers acima são aliases fictícios. O walkthrough é uma verificação de completude do processo e não um sign-off humano.

### 9.3 Matriz de decisão

| ADR | Resultado da simulação | Evidência sintética | Residual uncertainty | Status recomendado no framework |
|---|---|---|---|---|
| 0013 | `SIMULATED_CONDITIONAL_PASS` | delegation, attenuation, deny, expiry, revocation, containment e lineage | eficácia operacional, caso real e recovery real | `promotion-ready-after-signoff`; manter `draft` |
| 0014 | `SIMULATED_CONDITIONAL_PASS` | correlation, provenance, redaction, deletion, export, cost e alert-to-action | implementação, privacy decision real, retenção longitudinal e custo real | `promotion-ready-after-signoff`; manter `draft` |
| 0015 | `SIMULATED_CONDITIONAL_PASS` | matrix, conflict, precedence, fail-safe, recovery e substitution | autoridade real, enforcement, fallback e equivalência operacional | `promotion-ready-after-signoff`; manter `draft` |

A simulação responde que **as três ADRs são utilizáveis como guidance/patterns/templates em futuras implementações**. Ela não responde que já foram aprovadas como policy/standard organizacional nem que são efetivas em produção.

## 10. Decision record sintético

> **Decision:** aceitar o pacote como referência sintética para walkthrough e preparação de futuras implementações; não promover os documentos a `accepted` com base somente nesta simulação.
>
> **Rationale:** os três contratos responderam às perguntas de authority, state, enforcement, recovery, evidence e exit no caso sintético. Os resultados negativos foram preservados como findings e os controles de deny não foram contornados.
>
> **Conditions:** qualquer adoção futura deve repetir os testes no contexto do consumidor, nomear owners reais, definir data classes, executar privacy/security/run review e preservar evidence exportável.
>
> **Expiry:** esta decisão sintética expira quando o framework mudar materialmente, quando a implementação divergente for adotada ou quando um walkthrough real produzir evidence diferente.
>
> **Residual uncertainty:** nenhuma conclusão sobre efficacy, reliability, compliance, cost, security posture ou interoperabilidade universal.

## 11. Resposta objetiva à pergunta de promoção

**Simulação concluída:** as ADRs passam no teste de aplicabilidade do framework, com condições.

**Promoção documental real:** ainda não; o status correto continua `draft`.

**Uso comercial futuro:** sim, o pacote pode ser usado como referência de delivery para clientes, desde que cada cliente substitua os aliases, fixtures e evidence sintéticos por seus próprios owners, ambientes, policies, data classes e records.

## 12. Gaps revelados pela simulação

A simulação não revelou falha conceitual que impeça o uso das três ADRs como guidance, patterns e templates. Os gaps encontrados são de **evidence, packaging e operação futura**, não justificam nova arquitetura normativa.

| Finding | Classificação | Observação | Ação futura |
|---|---|---|---|
| `G-SIM-01` | `PARTIALLY_CONFIRMED` | O framework possui assessments, templates e exemplos, mas não um único manifest cross-ADR para ligar case, authorities, runs, evidence, decisions e residual uncertainty. | Reutilizar os artefatos existentes ou criar um guidance de packaging somente se futuros consumidores demonstrarem necessidade recorrente. |
| `G-SIM-02` | `INTENTIONAL` | A distinção entre evidência sintética e operacional é essencial, mas não deve virar automaticamente novo enum normativo. | Manter a classificação no pacote de simulação e usar os estados canônicos do framework nos records reais. |
| `G-SIM-03` | `PARTIALLY_CONFIRMED` | O walkthrough por authority está definido no assessment, porém o sign-off multi-ADR ainda é um processo a executar, não um artefato aprovado. | Para cada consumidor, registrar owner, conditions, expiry, divergences, compensating controls e decision record. |
| `G-SIM-04` | `BLOCKED_BY_AUTHORIZED_EVIDENCE` | ADR-0014 exige implementation evidence para privacy, retention, deletion, export, cardinality/cost e qualidade longitudinal. ADR-0015 exige evidence de enforcement, fallback e recovery. | Executar somente quando houver ambiente e authority do consumidor. |
| `G-SIM-05` | `INTENTIONAL` | A simulação usa uma taxonomia local de `SIMULATED_*` para não contaminar os enums canônicos. | Não importar esses estados para schemas ou controls sem change proposal. |

A conclusão é importante: **o framework está suficientemente expressivo para conduzir uma futura implementação**, mas ainda depende de um pacote de delivery por consumidor para transformar guidance em decisão aplicada. Isso é esperado para um framework vendor-neutral e não é defeito que deva ser “corrigido” com expansão prematura.

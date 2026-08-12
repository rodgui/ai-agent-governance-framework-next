---
title: 05 — Lifecycle de agentes
status: maintained
maturity: validated
last_reviewed: 2026-08-11
review_cycle: quarterly
owners: [framework-maintainers]
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# 05 — Lifecycle de agentes

Este capítulo integra a estrutura clean-room aprovada com o conteúdo substantivo do corpus autoritativo. Requisitos do framework são vendor-neutral; legislação externa, guidance, casos e histórico são identificados como tais. A implementação organizacional exige adoção formal pela authority competente e não decorre do versionamento deste repositório.

## Contrato operacional do capítulo

As subseções seguintes formam um contrato executável de completude. Cada uma especifica a decisão ou ação requerida, o record/evidence mínimo e uma condição observável de conclusão para levar a governança do zero ao business as usual.

### 05.1 Lifecycle principles and states

**Required decision/action.** For **lifecycle principles and states**, the organization must define allowed states, transition authorities, entry/exit criteria and terminal outcomes for every agent.

**Record and evidence.** Publish the state machine with required records, gates G0–G7, exceptions and event-triggered re-entry.

**Done when.** Invalid transitions are rejected and observed runtime state reconciles with the authoritative registry.

### 05.2 Idea and demand intake

**Required decision/action.** For **idea and demand intake**, the organization must capture the problem, proposed mechanism, owner and decision need before design work begins.

**Record and evidence.** The intake record must include purpose, baseline, users, affected persons, data, actions, alternatives and urgency.

**Done when.** The request is routed to appropriateness, risk and portfolio decisions without bypassing ownership or scope checks.

### 05.3 Appropriateness decision

**Required decision/action.** For **appropriateness decision**, the organization must compare an agent with deterministic automation, workflow, search, analytics and non-technical alternatives.

**Record and evidence.** Record alternatives, need for autonomy, uncertainty, expected benefit, failure cost and architectural decision.

**Done when.** An agent proceeds only when its distinctive capability is necessary and the additional governance burden is accepted.

### 05.4 Initial registration and ownership

**Required decision/action.** For **initial registration and ownership**, the organization must create or update the stable registry identity before work or operation reaches the corresponding state.

**Record and evidence.** Record owner, purpose, tier, version, environment, dependencies, approval and discoverability metadata.

**Done when.** The asset is discoverable by authorized stakeholders and missing mandatory metadata blocks the transition.

### 05.5 Classification and routing

**Required decision/action.** For **classification and routing**, the organization must classify the case using approved criteria, mandatory escalators and the most severe applicable outcome.

**Record and evidence.** Record criterion results, red flags, rationale, confidence, reviewer and resulting route or response target.

**Done when.** The same evidence yields consistent routing and under-classification is detected by review or reconciliation.

### 05.6 Design requirements

**Required decision/action.** For **design requirements**, the organization must document boundaries, trust assumptions, data and action flows, quality attributes, controls and failure behavior before build.

**Record and evidence.** Retain approved blueprint, diagrams, interface contracts, threat and impact links, alternatives and ADRs.

**Done when.** Reviewers can trace each material requirement to an architecture element and testable enforcement point.

### 05.7 Design documentation and system record

**Required decision/action.** For **design documentation and system record**, the organization must document boundaries, trust assumptions, data and action flows, quality attributes, controls and failure behavior before build.

**Record and evidence.** Retain approved blueprint, diagrams, interface contracts, threat and impact links, alternatives and ADRs.

**Done when.** Reviewers can trace each material requirement to an architecture element and testable enforcement point.

### 05.8 Build, acquisition or configuration

**Required decision/action.** For **build, acquisition or configuration**, the organization must produce or acquire only approved components and configuration under traceable change control.

**Record and evidence.** Record source, version, license, supplier, build configuration, dependency inventory, scans and approval conditions.

**Done when.** The resulting artifact is reproducible or attestable and no unapproved dependency enters promotion.

### 05.9 Development environments and separation

**Required decision/action.** For **development environments and separation**, the organization must separate development, test and production identities, data, credentials, networks and deployment authority.

**Record and evidence.** Retain environment inventory, access policy, data classification, promotion path and negative-test evidence.

**Done when.** Test access cannot mutate production and production secrets or personal data are not copied into lower environments without authority.

### 05.10 Testing and evaluation planning

**Required decision/action.** For **testing and evaluation planning**, the organization must approve test objectives, datasets, slices, abuse cases, thresholds and reviewer independence before seeing results.

**Record and evidence.** The plan must bind use case, tier, versions, environments, methods, acceptance criteria and evidence owner.

**Done when.** The plan covers material failure modes and cannot be relaxed after a failed result without a recorded change decision.

### 05.11 Evidence collection

**Required decision/action.** For **evidence collection**, the organization must collect decision-relevant evidence with stable identity, source, time, version, integrity and custody.

**Record and evidence.** The evidence manifest must list artifacts, hashes, producer, environment, method, result, limitation and linked decision.

**Done when.** A reviewer can retrieve and reproduce the material claim and missing evidence is represented as a gap, not success.

### 05.12 Release review

**Required decision/action.** For **release review**, the organization must decide release only from the bound risk, evaluation, control and operational evidence package.

**Record and evidence.** Record decision, authority, versions, passed and failed criteria, conditions, expiry, rollback target and unresolved findings.

**Done when.** Blocking controls cannot be waived by a conditional approval and expired conditions stop continued operation.

### 05.13 Approval, conditional approval or rejection

**Required decision/action.** For **approval, conditional approval or rejection**, the organization must decide release only from the bound risk, evaluation, control and operational evidence package.

**Record and evidence.** Record decision, authority, versions, passed and failed criteria, conditions, expiry, rollback target and unresolved findings.

**Done when.** Blocking controls cannot be waived by a conditional approval and expired conditions stop continued operation.

### 05.14 Deployment and progressive rollout

**Required decision/action.** For **deployment and progressive rollout**, the organization must release through bounded cohorts or stages with explicit promotion, pause and rollback criteria.

**Record and evidence.** Record cohort, exposure, telemetry, thresholds, approval, observed result, incidents and next-stage decision.

**Done when.** Expansion occurs only after the prior stage meets criteria and an adverse signal can halt or reverse rollout.

### 05.15 Production registration and discoverability

**Required decision/action.** For **production registration and discoverability**, the organization must create or update the stable registry identity before work or operation reaches the corresponding state.

**Record and evidence.** Record owner, purpose, tier, version, environment, dependencies, approval and discoverability metadata.

**Done when.** The asset is discoverable by authorized stakeholders and missing mandatory metadata blocks the transition.

### 05.16 Operation and monitoring

**Required decision/action.** For **operation and monitoring**, the organization must monitor the production behavior and control outcomes that can invalidate approval.

**Record and evidence.** Retain signal definitions, baselines, slices, thresholds, owner, alert route, investigation and linked lifecycle action.

**Done when.** Material drift or threshold breach produces containment or reassessment rather than an informational alert with no owner.

### 05.17 Incident-triggered review

**Required decision/action.** For **incident-triggered review**, the organization must retest affected requirements after incident, fix, dependency change or model/configuration update.

**Record and evidence.** Bind prior and new versions, impacted scenarios, regression set, result, residual gaps and release disposition.

**Done when.** The change does not silently invalidate prior evidence and failed regression prevents reactivation or promotion.

### 05.18 Material change definition

**Required decision/action.** For **material change definition**, the organization must define material changes and external events that reopen risk, approval, evaluation or contract compatibility.

**Record and evidence.** Record trigger, detection source, impacted assets and evidence, interim control, owner, due date and disposition.

**Done when.** Triggered assets cannot rely indefinitely on prior approval and the new decision is linked to the changed version.

### 05.19 Versioning and change control

**Required decision/action.** For **versioning and change control**, the organization must version every material change and bind it to effective, review and supersession dates.

**Record and evidence.** Retain change description, author, approver, impacted contracts, migration action and prior-version reference.

**Done when.** Consumers can identify the applicable version and incompatible records are migrated, rejected or explicitly grandfathered.

### 05.20 Periodic reassessment and attestation

**Required decision/action.** For **periodic reassessment and attestation**, the organization must require owners to re-attest purpose, ownership, dependencies, risk, controls and continued need on a risk-based cycle.

**Record and evidence.** Record attestor, evidence cutoff, changed facts, exceptions, stale dependencies, decision and next review.

**Done when.** Non-response or unsupported attestation triggers restriction, suspension or retirement rather than automatic renewal.

### 05.21 Suspension and quarantine

**Required decision/action.** For **suspension and quarantine**, the organization must implement authority and technical paths to stop actions, isolate dependencies and preserve evidence.

**Record and evidence.** Record trigger, command path, scope, expected state, operator, test cadence, result and recovery prerequisites.

**Done when.** A drill contains a representative failure within the target without relying on the failing agent itself.

### 05.22 Corrective action

**Required decision/action.** For **corrective action**, the organization must assign each finding a root cause, risk-based priority, corrective action and closure criterion.

**Record and evidence.** Record finding, evidence, owner, due date, interim control, root cause, remediation, retest and reviewer disposition.

**Done when.** Closure requires objective retest evidence; overdue material findings remain visible and affect approval.

### 05.23 Safe reactivation

**Required decision/action.** For **safe reactivation**, the organization must permit reactivation only after root cause, remediation, regression, monitoring and rollback readiness are evidenced.

**Record and evidence.** Record incident link, changed version, retest package, residual risk, approving authority, conditions and rollout scope.

**Done when.** The former failure is no longer reproducible under the tested conditions and early-warning signals are active.

### 05.24 Retirement and decommissioning

**Required decision/action.** For **retirement and decommissioning**, the organization must retire the agent through an approved state transition that removes authority and resolves data and dependency obligations.

**Record and evidence.** Record final owner decision, user notice, traffic stop, access revocation, data disposition, archive, dependency owner and completion evidence.

**Done when.** The agent can no longer act or consume resources and retained records remain accessible for their approved period.

### 05.25 Records retention, access revocation and dependency cleanup

**Required decision/action.** For **records retention, access revocation and dependency cleanup**, the organization must define who may read, change and retrieve the record, for how long and under which legal hold or deletion rule.

**Record and evidence.** Record classification, access groups, custodian, retention trigger, minimum period, disposition and audit retrieval path.

**Done when.** Authorized evidence is retrievable within the required time and expired data is disposed of without breaking required lineage.


## Conteúdo canônico incorporado

A seção preserva integralmente as unidades atribuídas pela matriz de cobertura. Os marcadores HTML são provenance machine-readable e não alteram o significado normativo.

### Fonte: `docs/governance/ai-agent-policy-and-governance-v1.md`

Commit de origem: `5545d9227624400ab8bb707b6032b2f61329a36e`.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "124", "index": 1, "source_field": "", "source_heading": "8. Autonomy Policy (HITL)", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "118", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
#### 8. Autonomy Policy (HITL)
This section defines how the company controls the autonomy of AI agents to ensure that decisions and actions remain under human responsibility, with traceability and the ability to intervene. The goal is to enable automation safely: the agent can propose suggestions and perform tasks within defined limits, but actions with significant impact must have explicit human approval (Human-in-the-Loop) and recorded evidence. The policy also defines when exceptions may exist, what additional controls apply, and how to handle escalation and rollback.
All relevant executive actions require explicit human confirmation through the approved channel (e.g., Teams, system UI, ServiceNow).
Irreversible, high-impact actions are not allowed without HITL.
Temporary exceptions require approval according to the Matrix, with justification and a rollback plan.
Changes to the model or decision rules that affect the agent’s autonomous behavior require new security validation, minimum testing, and reassessment of the autonomy level.

<!-- source-unit {"classification": "decision-authority", "end_line": "127", "index": 2, "source_field": "", "source_heading": "8.1 Autonomy Levels (L0–L3) and link to the Approval Matrix", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "125", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
##### 8.1 Autonomy Levels (L0–L3) and link to the Approval Matrix
Definition of levels to standardize what 'autonomy' means and reduce ambiguity in decision-making. Regardless of the level, any red flag (personal/sensitive data, critical systems, SOX/ITGC, high blast radius) escalates to the Production path and may require additional controls.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "183", "index": 3, "source_field": "", "source_heading": "12. Life Cycle and MLOps for Agents", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "165", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
#### 12. Life Cycle and MLOps for Agents
Agents require continuous governance: it is not enough to simply "create and publish." This section defines the corporate lifecycle of the agent, from ideation and PoC to production, operation, changes, and deactivation (sunset), and the MLOps/AgentOps controls required to maintain quality, security, and compliance over time. The focus is to ensure repeatability, traceability (versions, prompts, tools, data), observability, and change management without disrupting the business.
Case Selection/Prioritization (value, feasibility, risk).
Development and testing (including fairness/robustness when applicable).
Deployment with CI/CD, versioning, and rollback.
Performance monitoring and drift; action auditing.
Automatic mechanisms for monitoring the quality and stability of the agent must be configured.
Alerts should be generated in case of performance degradation, abnormal increase in errors, or unexpected behavior.
Periodic reviews of prompt injection tests, attempts at data exfiltration, and bypassing autonomy controls, with recording of results.
Creation and review of sunset plan*.
* Sunset:
No Business Owner or Technical Owner defined
Out of Stock
Without logs/minimal telemetry
No use for N days (e.g., 90)
Agent duplicated/replaced by official version
Platform is no longer approved
Serious incident without correction within the deadline

<!-- source-unit {"classification": "concept-or-structure", "end_line": "279", "index": 4, "source_field": "", "source_heading": "17.5 Integration with Life Cycle", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "277", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
##### 17.5 Integration with Life Cycle
Observability data must feed the Operation, Incident Management, Change Management, and Periodic Review processes described in this policy, including influencing sunset decisions when there are persistent deviations, inactivity, or high risk.

### Fonte: `docs/lifecycle/README.md`

Commit de origem: `5545d9227624400ab8bb707b6032b2f61329a36e`.

<!-- source-unit {"classification": "metadata-title", "end_line": "2", "index": 5, "source_field": "title", "source_heading": "", "source_path": "docs/lifecycle/README.md", "start_line": "2", "transformation": "integrate-completely", "unit_type": "frontmatter-title"} -->
**Título controlado na origem:** Lifecycle, mudança material, attestation e retirement

<!-- source-unit {"classification": "lifecycle-state", "end_line": "19", "index": 6, "source_field": "", "source_heading": "Lifecycle, mudança material, attestation e retirement", "source_path": "docs/lifecycle/README.md", "start_line": "18", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
### Lifecycle, mudança material, attestation e retirement

<!-- source-unit {"classification": "objective", "end_line": "25", "index": 7, "source_field": "", "source_heading": "Objetivo", "source_path": "docs/lifecycle/README.md", "start_line": "20", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Objetivo

Governar o agente ao longo do tempo, não apenas no momento do deploy. Sem lifecycle explícito, o estate acumula agentes publicados que mantêm permissões, identidades, conectores e custo depois de perder owner, finalidade ou evidência válida.

O resultado esperado: **qualquer agente em produção possui estado conhecido, owner válido, próxima attestation, regras de mudança material e um caminho testado para suspensão, quarentena e retirada.**

<!-- source-unit {"classification": "definition", "end_line": "34", "index": 8, "source_field": "", "source_heading": "Duas unidades distintas", "source_path": "docs/lifecycle/README.md", "start_line": "26", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Duas unidades distintas

| Unidade | O que é | O que carrega |
|---|---|---|
| **agent asset** | o ativo estável, com `agent_id` permanente | identidade, ownership, histórico, finalidade |
| **version/release** | a versão publicada em um ambiente | configuração, evidências, approval, expiry |

Confundir as duas produz o erro mais comum do domínio: aprovar uma versão e tratar a aprovação como permanente para o ativo.

<!-- source-unit {"classification": "lifecycle-state", "end_line": "61", "index": 9, "source_field": "", "source_heading": "Etapa da jornada, lifecycle stage e operational state", "source_path": "docs/lifecycle/README.md", "start_line": "35", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Etapa da jornada, lifecycle stage e operational state

Três visões coexistem sem ser sinônimas:

- **etapa da jornada** orienta o trabalho humano: ideia, design, build, avaliação e operação;
- **lifecycle stage** registra a posição formal do ativo: `discovered`, `draft`, `under-review`, `approved`, `production`, `retirement-review`, `retired` ou `archived`;
- **operational state** registra a consequência técnica atual: `not-deployed`, `enabled`, `suspended`, `quarantined` ou `disabled`.

Separar stage de operational state evita transformar quarentena em falso avanço de lifecycle. Um agente pode permanecer em stage `production` e mudar de `enabled` para `quarantined` sem perder o histórico de release.

| Etapa | O que produz | Gate para avançar |
|---|---|---|
| ideia | intake, hipótese de valor, decisão `agent` vs `workflow` determinístico | problema e owner inicial claros |
| registro | `agent_id`, owners, ambiente, finalidade, status inicial | nenhum build compartilhado ou produção sem ID e owner |
| classificação | tier, admissibilidade, escaladores, red flags, impact trigger screen | tier e admissibilidade válidos; `restricted` segue exceção explícita |
| design | blueprint, identidade, dados, tools, modelo, oversight, telemetria, failure behavior | design atende ao baseline do tier; gaps têm owner |
| build | configuração versionada, integrações, bindings de observabilidade | build reproduz o blueprint; secrets e permissões dentro da policy |
| avaliação | evals funcionais, abuse cases, testes de dados/tools, resiliência, rollback | findings bloqueadores fechados ou aceitos pela authority correta |
| review e aprovação | domain reviews acionadas, MPB, evidence pack, risk acceptance | Publication Gate `approve` ou `condition` registrado |
| publicação | deploy, health checks, políticas e budget ativos, baseline de runtime | containment e rollback disponíveis antes da exposição |
| operação | telemetria, incidentes, mudanças, custo, valor | sinais podem acionar reassessment ou contenção |
| attestation e mudança | revalidação de owner, necessidade e acessos; classificação de mudanças | continuar, remediar, suspender ou reaprovar |
| suspensão ou quarentena | limitação administrativa ou contenção de risco | reativação exige causa, correção e regression evidence |
| retirada | revogação de acessos, encerramento de custo, arquivamento de evidência | o ativo não retorna sem novo ciclo completo |

Gate não significa reunião. Em T1, vários gates podem ser policy-driven. O que importa é que a condição de avanço seja objetiva, verificável e registrada.

<!-- source-unit {"classification": "lifecycle-state", "end_line": "78", "index": 10, "source_field": "", "source_heading": "State machine", "source_path": "docs/lifecycle/README.md", "start_line": "62", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### State machine

Stages mínimos:

`discovered` · `draft` · `under-review` · `approved` · `production` · `retirement-review` · `retired` · `archived`

Operational states mínimos:

`not-deployed` · `enabled` · `suspended` · `quarantined` · `disabled`

Regras estruturais:

- `draft` não vai diretamente a `production`;
- `quarantined` não retorna a `enabled` sem correção, reteste e aprovação;
- cada transição registra evento disparador, authority, evidência e ações automáticas;
- stage e operational state são versionados e o histórico é preservado — a auditoria precisa saber as duas condições no momento de um evento.

<!-- source-unit {"classification": "decision-authority", "end_line": "92", "index": 11, "source_field": "", "source_heading": "Matriz de transição", "source_path": "docs/lifecycle/README.md", "start_line": "79", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
##### Matriz de transição

| Stage/state atual | Evento | Stage/state seguinte | Authority | Ações automáticas |
| --- | --- | --- | --- | --- |
| `draft` / `not-deployed` | solicitação de publicação | `under-review` / `not-deployed` | workflow | congelar blueprint; executar pre-screen |
| `under-review` / `not-deployed` | evidências e gates completos | `approved` / `not-deployed` | authority de publicação do tier | emitir decision record com expiry |
| `approved` / `not-deployed` | deploy e health check OK | `production` / `enabled` | plataforma | ativar policy de runtime, telemetria e budget |
| `production` / `enabled` | sinal crítico de segurança ou comportamento | `production` / `quarantined` | Run Authority | desabilitar tools/identidade conforme runbook; preservar evidência |
| `production` / `enabled` | suspensão administrativa | `production` / `suspended` | owner ou Run Authority | interromper novas execuções; preservar configuração |
| `production` / qualquer | dormancy threshold atingido | `retirement-review` / estado observado | serviço de lifecycle | notificar owner; iniciar grace period |
| `production` / qualquer | mudança material declarada | `under-review` / `not-deployed` para a versão candidata | Design Authority | manter release atual governada; reabrir apenas etapas afetadas |
| `retirement-review` / qualquer | owner confirma desuso | `retired` / `disabled` | owner + plataforma | remover acessos e secrets; arquivar evidência |
| `retired` / `disabled` | retenção concluída | `archived` / `disabled` | Records Authority | preservar somente evidência exigida |

<!-- source-unit {"classification": "concept-or-structure", "end_line": "102", "index": 12, "source_field": "", "source_heading": "Suspensão, quarentena e retirada são ações diferentes", "source_path": "docs/lifecycle/README.md", "start_line": "93", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
##### Suspensão, quarentena e retirada são ações diferentes

Um único botão "disable" para os três casos destrói a rastreabilidade.

| Ação | Motivo | Evidência preservada | Reversível |
|---|---|---|---|
| `suspended` | administrativo ou planejado | configuração e histórico | sim, por decisão do owner |
| `quarantined` | risco ou incidente | evidência forense preservada deliberadamente | somente com causa, correção e regression evidence |
| `disabled` em stage `retired` | fim de vida | arquivada conforme retenção | não — exige novo ciclo completo |

<!-- source-unit {"classification": "lifecycle-state", "end_line": "119", "index": 13, "source_field": "", "source_heading": "Mudança material", "source_path": "docs/lifecycle/README.md", "start_line": "103", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Mudança material

Mudança material é a que pode alterar risco, impacto ou comportamento e, por isso, reabre avaliação. Cada trigger aponta para o ponto do processo que precisa ser reexecutado — o reassessment recomeça do ponto afetado, **não do zero**.

| Trigger | O que reabrir |
|---|---|
| passagem de leitura para escrita, ou classe de ação mais crítica | classificação, controls, testes de rollback |
| nova fonte de dados de classificação superior | data review, impact screen, controls de acesso |
| novo provider, modelo ou região com data handling diferente | [governança de modelos](06-architecture-and-technical-controls.md), regression evals |
| aumento de autonomia, profundidade de cadeia ou delegação entre agentes | classificação, threat model, oversight |
| novo público externo ou ampliação relevante de alcance | classificação, transparência, impact assessment |
| mudança de owner ou de processo crítico | ownership, authority, attestation |
| alteração ou remoção de etapa de aprovação humana | oversight design, classificação |
| nova ferramenta com escrita ou privilégio | tool review, identidade, containment |

Defina a lista corporativa **antes** de automatizar qualquer reassessment. Automatizar um gatilho mal definido gera ruído e treina a organização a ignorá-lo.

<!-- source-unit {"classification": "lifecycle-state", "end_line": "128", "index": 14, "source_field": "", "source_heading": "Attestation", "source_path": "docs/lifecycle/README.md", "start_line": "120", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Attestation

Revalidação periódica de owner, necessidade, acesso e controles — não uma assinatura ritual.

- cadência proporcional ao tier, no máximo anual;
- o owner confirma que o agente continua necessário, que os acessos continuam adequados e que a finalidade não mudou;
- attestation vencida é um estado, não um aviso: aciona grace period e depois suspensão;
- attestation não substitui reassessment após mudança material.

<!-- source-unit {"classification": "lifecycle-state", "end_line": "150", "index": 15, "source_field": "", "source_heading": "Dormancy", "source_path": "docs/lifecycle/README.md", "start_line": "129", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Dormancy

Dormancy threshold é **gatilho de revisão, não regra cega de exclusão**. Um agente financeiro trimestral pode ficar 80 dias sem execução e continuar legítimo; um agente de service desk sem uso por 30 dias provavelmente foi abandonado.

Valores iniciais sugeridos, a calibrar com evidência:

| Tier | Threshold inicial | Grace period |
|---|---|---|
| T1 | 120 dias | 30 dias |
| T2 | 90 dias | 21 dias |
| T3 | 60 dias | 14 dias |
| T4 | 30 dias | 7 dias, com revisão de admissibilidade e da exceção quando `restricted` |

Procedimento de calibração:

1. segmentar por frequência esperada e tier;
2. definir threshold inicial e grace period;
3. rodar 60–90 dias em **report-only**;
4. analisar falsos positivos e sazonalidade;
5. ajustar e só então automatizar a cadeia notificação → attestation → suspensão → retirada;
6. manter exceções sazonais com data de expiração.

<!-- source-unit {"classification": "lifecycle-state", "end_line": "159", "index": 16, "source_field": "", "source_heading": "Joiner, Mover e Leaver aplicado a agentes", "source_path": "docs/lifecycle/README.md", "start_line": "151", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Joiner, Mover e Leaver aplicado a agentes

A identidade de um agente não pode permanecer silenciosamente vinculada a alguém que mudou de função ou saiu.

- **Joiner:** ao assumir, o novo owner tem role, competência e authority validadas antes da transferência de accountability.
- **Mover:** mudança de área do owner dispara revisão de ownership, centro de custo e permissões. Se a nova função não puder responder pelo agente, reatribua.
- **Leaver:** antes do desligamento, consulte o registry por ownership, nomeie delegado temporário e suspenda os casos sem sucessor conforme o tier.
- Em nenhum caso apague o histórico de ownership — a timeline é evidência de auditoria.

<!-- source-unit {"classification": "procedure", "end_line": "170", "index": 17, "source_field": "", "source_heading": "Playbook de implantação", "source_path": "docs/lifecycle/README.md", "start_line": "160", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Playbook de implantação

1. Definir o objeto governado (`agent asset` vs `version`) e quem opera o lifecycle.
2. Desenhar estados a partir de consequências operacionais, não de atividades de projeto.
3. Transformar cada transição em gate auditável com evento, authority, evidência, SLA e automação.
4. Definir a lista de mudanças materiais **antes** de automatizar reassessment.
5. Calibrar attestation e dormancy pelo padrão real de uso, em report-only primeiro.
6. Integrar JML de owners ao registry, com consulta reversa por ownership.
7. Implementar suspensão, quarentena e retirada como ações distintas.
8. Antes de virar policy-as-code, validar manualmente em uma cohort representativa ou usar evidência operacional equivalente. Uma cohort sugerida contém 10–20 agentes, ao menos um T3, um leaver, uma mudança material e um incidente simulado; isso é guidance adaptável, não piloto obrigatório.

<!-- source-unit {"classification": "evidence-artifact", "end_line": "178", "index": 18, "source_field": "", "source_heading": "Artefatos", "source_path": "docs/lifecycle/README.md", "start_line": "171", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Artefatos

- Agent Lifecycle Standard: estados, transições, triggers, roles, timers, JML, quarentena, retirada e retenção;
- matriz de transição e runbook operacional;
- registro de attestation e de mudanças materiais;
- [template de attestation e sunset](../../toolkit/templates/attestation-sunset-record.md);
- [plano de sunset](../../toolkit/templates/sunset-plan.md).

<!-- source-unit {"classification": "evidence-artifact", "end_line": "187", "index": 19, "source_field": "", "source_heading": "Evidências", "source_path": "docs/lifecycle/README.md", "start_line": "179", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Evidências

- estado atual e histórico de transições por agente e versão;
- approval record com authority, condições e expiry;
- attestation records e vencimentos;
- classificação de mudanças materiais e reassessments derivados;
- evidência de contenção e de reativação;
- registro de retirada com remoção de acessos e arquivamento.

<!-- source-unit {"classification": "metric", "end_line": "198", "index": 20, "source_field": "", "source_heading": "Métricas", "source_path": "docs/lifecycle/README.md", "start_line": "188", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Métricas

- agentes em produção sem attestation válida;
- agentes sem owner ou com owner desligado;
- mudanças materiais detectadas por auditoria em vez de declaradas pelo owner;
- tempo entre trigger e reassessment concluído;
- agentes dormentes por tier e desfecho após grace period;
- transições executadas fora da matriz autorizada;
- tempo entre decisão de retirada e revogação efetiva de acesso;
- reativações após quarentena sem regression evidence.

<!-- source-unit {"classification": "risk-failure-mode", "end_line": "208", "index": 21, "source_field": "", "source_heading": "Failure modes", "source_path": "docs/lifecycle/README.md", "start_line": "199", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Failure modes

- state machine documentada que não altera permissão, evidência ou comportamento real;
- tratar aprovação de versão como aprovação permanente do ativo;
- usar um único "disable" para suspensão, quarentena e retirada;
- automatizar dormancy antes de calibrar sazonalidade;
- reassessment que recomeça do zero e, por custo, deixa de ser executado;
- retirada que remove o agente do catálogo mas não revoga identidade e secrets;
- histórico de ownership sobrescrito em vez de versionado.

<!-- source-unit {"classification": "requirement-control", "end_line": "211", "index": 22, "source_field": "", "source_heading": "Decision gate", "source_path": "docs/lifecycle/README.md", "start_line": "209", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Decision gate

Nenhum agente permanece em produção sem lifecycle stage e operational state válidos, owner ativo, attestation dentro do prazo do tier e caminho de contenção e retirada exercitado. Toda transição preserva authority e evidence. Mudança material sem reassessment registrado é motivo de suspensão, não de exceção informal.

## Acceptance criteria

- todas as decisões deste capítulo possuem authority, owner e evidência recuperável;
- requisitos aplicáveis estão ligados ao catálogo de controles e ao método de verificação;
- exceções têm escopo, justificativa, compensating controls, expiry e decisão residual;
- controles de build time e runtime são distinguidos e exercitados quando aplicáveis;
- mudanças materiais reabrem avaliação, aprovação e evidência;
- nenhuma alegação de conformidade, eficácia ou valor excede a evidência observada.

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

### 05.1 Princípios e estados de lifecycle

**Decisão/ação obrigatória.** Para **princípios e estados de lifecycle**, a organização deve definir estados permitidos, authorities de transição, critérios de entrada/saída e resultados terminais para todo agente.

**Registro e evidência.** Publicar a máquina de estados com registros exigidos, gates G0–G7, exceções e reentrada disparada por evento.

**Concluído quando.** Transições inválidas são rejeitadas e o estado observado em runtime reconcilia com o registry autoritativo.

### 05.2 Intake de ideia e demanda

**Decisão/ação obrigatória.** Para **intake de ideia e demanda**, a organização deve capturar o problema, o mecanismo proposto, o owner e a necessidade de decisão antes de iniciar o trabalho de design.

**Registro e evidência.** O registro de intake deve incluir finalidade, baseline, usuários, pessoas afetadas, dados, ações, alternativas e urgência.

**Concluído quando.** A solicitação é encaminhada às decisões de adequação, risco e portfólio sem ignorar verificações de ownership ou escopo.

### 05.3 Decisão de adequação

**Decisão/ação obrigatória.** Para **decisão de adequação**, a organização deve comparar um agente com automação determinística, workflow, busca, analytics e alternativas não técnicas.

**Registro e evidência.** Registrar alternativas, necessidade de autonomia, incerteza, benefício esperado, custo de falha e decisão arquitetural.

**Concluído quando.** Um agente prossegue somente quando sua capacidade distintiva é necessária e o ônus adicional de governança é aceito.

### 05.4 Registro inicial e ownership

**Decisão/ação obrigatória.** Para **registro inicial e ownership**, a organização deve criar ou atualizar a identidade estável no registry antes de o trabalho ou a operação alcançar o estado correspondente.

**Registro e evidência.** Registrar owner, finalidade, tier, versão, ambiente, dependências, aprovação e metadados de descobribilidade.

**Concluído quando.** O ativo é descobrível por stakeholders autorizados e metadados obrigatórios ausentes bloqueiam a transição.

### 05.5 Classificação e encaminhamento

**Decisão/ação obrigatória.** Para **classificação e encaminhamento**, a organização deve classificar o caso usando critérios aprovados, escaladores obrigatórios e o resultado aplicável mais severo.

**Registro e evidência.** Registrar resultados por critério, red flags, rationale, confiança, revisor e rota resultante ou alvo de resposta.

**Concluído quando.** A mesma evidência produz encaminhamento consistente e sub-classificação é detectada por revisão ou reconciliação.

### 05.6 Requisitos de design

**Decisão/ação obrigatória.** Para **requisitos de design**, a organização deve documentar fronteiras, premissas de confiança, fluxos de dados e ações, atributos de qualidade, controles e comportamento de falha antes do build.

**Registro e evidência.** Reter blueprint aprovado, diagramas, contratos de interface, vínculos de ameaça e impacto, alternativas e ADRs.

**Concluído quando.** Revisores conseguem rastrear cada requisito material a um elemento de arquitetura e a um ponto de enforcement testável.

### 05.7 Documentação de design e registro do sistema

**Decisão/ação obrigatória.** Para **documentação de design e registro do sistema**, a organização deve documentar fronteiras, premissas de confiança, fluxos de dados e ações, atributos de qualidade, controles e comportamento de falha antes do build.

**Registro e evidência.** Reter blueprint aprovado, diagramas, contratos de interface, vínculos de ameaça e impacto, alternativas e ADRs.

**Concluído quando.** Revisores conseguem rastrear cada requisito material a um elemento de arquitetura e a um ponto de enforcement testável.

### 05.8 Build, aquisição ou configuração

**Decisão/ação obrigatória.** Para **build, aquisição ou configuração**, a organização deve produzir ou adquirir somente componentes e configuração aprovados sob controle de mudança rastreável.

**Registro e evidência.** Registrar fonte, versão, licença, fornecedor, configuração de build, inventário de dependências, varreduras e condições de aprovação.

**Concluído quando.** O artefato resultante é reproduzível ou atestável e nenhuma dependência não aprovada entra na promoção.

### 05.9 Ambientes de desenvolvimento e separação

**Decisão/ação obrigatória.** Para **ambientes de desenvolvimento e separação**, a organização deve separar identidades, dados, credenciais, redes e autoridade de implantação de desenvolvimento, teste e produção.

**Registro e evidência.** Reter inventário de ambientes, policy de acesso, classificação de dados, caminho de promoção e evidência de teste negativo.

**Concluído quando.** Acesso de teste não pode mutar produção e segredos ou dados pessoais de produção não são copiados para ambientes inferiores sem authority.

### 05.10 Planejamento de testes e avaliação

**Decisão/ação obrigatória.** Para **planejamento de testes e avaliação**, a organização deve aprovar objetivos de teste, datasets, fatias, casos de abuso, thresholds e independência do revisor antes de ver resultados.

**Registro e evidência.** O plano deve vincular caso de uso, tier, versões, ambientes, métodos, critérios de aceite e owner da evidência.

**Concluído quando.** O plano cobre modos de falha materiais e não pode ser afrouxado após um resultado reprovado sem decisão de mudança registrada.

### 05.11 Coleta de evidências

**Decisão/ação obrigatória.** Para **coleta de evidências**, a organização deve coletar evidências relevantes para a decisão com identidade, fonte, tempo, versão, integridade e custódia estáveis.

**Registro e evidência.** O manifesto de evidências deve listar artefatos, hashes, produtor, ambiente, método, resultado, limitação e decisão vinculada.

**Concluído quando.** Um revisor consegue recuperar e reproduzir a alegação material e evidência ausente é representada como lacuna, não como sucesso.

### 05.12 Revisão de release

**Decisão/ação obrigatória.** Para **revisão de release**, a organização deve decidir o release somente a partir do pacote vinculado de evidências de risco, avaliação, controle e operação.

**Registro e evidência.** Registrar decisão, authority, versões, critérios aprovados e reprovados, condições, expiração, alvo de rollback e descobertas não resolvidas.

**Concluído quando.** Controles bloqueantes não podem ser dispensados por aprovação condicional e condições expiradas interrompem a operação continuada.

### 05.13 Aprovação, aprovação condicional ou rejeição

**Decisão/ação obrigatória.** Para **aprovação, aprovação condicional ou rejeição**, a organização deve decidir o release somente a partir do pacote vinculado de evidências de risco, avaliação, controle e operação.

**Registro e evidência.** Registrar decisão, authority, versões, critérios aprovados e reprovados, condições, expiração, alvo de rollback e descobertas não resolvidas.

**Concluído quando.** Controles bloqueantes não podem ser dispensados por aprovação condicional e condições expiradas interrompem a operação continuada.

### 05.14 Implantação e rollout progressivo

**Decisão/ação obrigatória.** Para **implantação e rollout progressivo**, a organização deve liberar por coortes ou estágios delimitados com critérios explícitos de promoção, pausa e rollback.

**Registro e evidência.** Registrar coorte, exposição, telemetria, thresholds, aprovação, resultado observado, incidentes e decisão do próximo estágio.

**Concluído quando.** A expansão ocorre somente após o estágio anterior atingir os critérios e um sinal adverso pode interromper ou reverter o rollout.

### 05.15 Registro em produção e descobribilidade

**Decisão/ação obrigatória.** Para **registro em produção e descobribilidade**, a organização deve criar ou atualizar a identidade estável no registry antes de o trabalho ou a operação alcançar o estado correspondente.

**Registro e evidência.** Registrar owner, finalidade, tier, versão, ambiente, dependências, aprovação e metadados de descobribilidade.

**Concluído quando.** O ativo é descobrível por stakeholders autorizados e metadados obrigatórios ausentes bloqueiam a transição.

### 05.16 Operação e monitoramento

**Decisão/ação obrigatória.** Para **operação e monitoramento**, a organização deve monitorar o comportamento em produção e os resultados de controle que podem invalidar a aprovação.

**Registro e evidência.** Reter definições de sinais, baselines, fatias, thresholds, owner, rota de alerta, investigação e ação de lifecycle vinculada.

**Concluído quando.** Desvio material ou violação de threshold produz contenção ou reavaliação em vez de um alerta informativo sem owner.

### 05.17 Revisão disparada por incidente

**Decisão/ação obrigatória.** Para **revisão disparada por incidente**, a organização deve retestar requisitos afetados após incidente, correção, mudança de dependência ou atualização de modelo/configuração.

**Registro e evidência.** Vincular versões anterior e nova, cenários impactados, conjunto de regressão, resultado, lacunas residuais e disposição de release.

**Concluído quando.** A mudança não invalida silenciosamente evidências anteriores e regressão reprovada impede reativação ou promoção.

### 05.18 Definição de mudança material

**Decisão/ação obrigatória.** Para **definição de mudança material**, a organização deve definir mudanças materiais e eventos externos que reabram risco, aprovação, avaliação ou compatibilidade contratual.

**Registro e evidência.** Registrar gatilho, fonte de detecção, ativos e evidências impactados, controle provisório, owner, data de vencimento e disposição.

**Concluído quando.** Ativos acionados não podem depender indefinidamente de aprovação anterior e a nova decisão é vinculada à versão alterada.

### 05.19 Versionamento e controle de mudança

**Decisão/ação obrigatória.** Para **versionamento e controle de mudança**, a organização deve versionar toda mudança material e vinculá-la a datas de efetividade, revisão e supersessão.

**Registro e evidência.** Reter descrição da mudança, autor, aprovador, contratos impactados, ação de migração e referência à versão anterior.

**Concluído quando.** Consumidores identificam a versão aplicável e registros incompatíveis são migrados, rejeitados ou explicitamente grandfather.

### 05.20 Reavaliação periódica e attestation

**Decisão/ação obrigatória.** Para **reavaliação periódica e attestation**, a organização deve exigir que owners reatestem finalidade, ownership, dependências, risco, controles e necessidade contínua em ciclo baseado em risco.

**Registro e evidência.** Registrar atestante, corte de evidências, fatos alterados, exceções, dependências obsoletas, decisão e próxima revisão.

**Concluído quando.** Não resposta ou attestation sem suporte dispara restrição, suspensão ou aposentadoria em vez de renovação automática.

### 05.21 Suspensão e quarentena

**Decisão/ação obrigatória.** Para **suspensão e quarentena**, a organização deve implementar caminhos de authority e técnicos para interromper ações, isolar dependências e preservar evidências.

**Registro e evidência.** Registrar gatilho, caminho de comando, escopo, estado esperado, operador, cadência de teste, resultado e pré-requisitos de recuperação.

**Concluído quando.** Um exercício (drill) contém uma falha representativa dentro do alvo sem depender do próprio agente com falha.

### 05.22 Ação corretiva

**Decisão/ação obrigatória.** Para **ação corretiva**, a organização deve atribuir a cada descoberta uma causa raiz, prioridade baseada em risco, ação corretiva e critério de fechamento.

**Registro e evidência.** Registrar descoberta, evidência, owner, data de vencimento, controle provisório, causa raiz, remediação, reteste e disposição do revisor.

**Concluído quando.** O fechamento exige evidência objetiva de reteste; descobertas materiais vencidas permanecem visíveis e afetam a aprovação.

### 05.23 Reativação segura

**Decisão/ação obrigatória.** Para **reativação segura**, a organização deve permitir reativação somente após causa raiz, remediação, regressão, monitoramento e prontidão de rollback serem evidenciados.

**Registro e evidência.** Registrar vínculo do incidente, versão alterada, pacote de reteste, risco residual, authority aprovadora, condições e escopo do rollout.

**Concluído quando.** A falha anterior não é mais reproduzível nas condições testadas e sinais de alerta precoce estão ativos.

### 05.24 Aposentadoria e descomissionamento

**Decisão/ação obrigatória.** Para **aposentadoria e descomissionamento**, a organização deve aposentar o agente por transição de estado aprovada que remova authority e resolva obrigações de dados e dependências.

**Registro e evidência.** Registrar decisão final do owner, aviso ao usuário, parada de tráfego, revogação de acesso, disposição de dados, arquivo, owner da dependência e evidência de conclusão.

**Concluído quando.** O agente não pode mais agir ou consumir recursos e registros retidos permanecem acessíveis pelo período aprovado.

### 05.25 Retenção de registros, revogação de acesso e limpeza de dependências

**Decisão/ação obrigatória.** Para **retenção de registros, revogação de acesso e limpeza de dependências**, a organização deve definir quem pode ler, alterar e recuperar o registro, por quanto tempo e sob qual regra de legal hold ou exclusão.

**Registro e evidência.** Registrar classificação, grupos de acesso, custodiano, gatilho de retenção, período mínimo, disposição e caminho de recuperação de auditoria.

**Concluído quando.** Evidências autorizadas são recuperáveis no prazo exigido e dados expirados são descartados sem romper a linhagem exigida.


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

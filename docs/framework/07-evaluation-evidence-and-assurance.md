---
title: 07 — Avaliação, evidência e assurance
status: maintained
maturity: validated
last_reviewed: 2026-08-11
review_cycle: quarterly
owners: [framework-maintainers]
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# 07 — Avaliação, evidência e assurance

Este capítulo integra a estrutura clean-room aprovada com o conteúdo substantivo do corpus autoritativo. Requisitos do framework são vendor-neutral; legislação externa, guidance, casos e histórico são identificados como tais. A implementação organizacional exige adoção formal pela authority competente e não decorre do versionamento deste repositório.

## Contrato operacional do capítulo

As subseções seguintes formam um contrato executável de completude. Cada uma especifica a decisão ou ação requerida, o record/evidence mínimo e uma condição observável de conclusão para levar a governança do zero ao business as usual.

### 07.1 Governança da avaliação e independência

**Decisão/ação obrigatória.** Para **governança da avaliação e independência**, a organização deve definir e executar esta atividade de avaliação ou assurance contra critérios pré-aprovados.

**Registro e evidência.** O registro de avaliação deve vincular escopo, versão, dataset ou amostra, método, thresholds, resultados, limitações, revisor e linhagem de evidência.

**Concluído quando.** Resultados são reproduzíveis, critérios reprovados bloqueiam ou condicionam o release, e a conclusão não excede o escopo testado nem a independência do revisor.

### 07.2 Estratégia de avaliação por risco e caso de uso

**Decisão/ação obrigatória.** Para **estratégia de avaliação por risco e caso de uso**, a organização deve aprovar objetivos de teste, datasets, fatias, casos de abuso, thresholds e independência do revisor antes de ver resultados.

**Registro e evidência.** O plano deve vincular caso de uso, tier, versões, ambientes, métodos, critérios de aceite e owner da evidência.

**Concluído quando.** O plano cobre modos de falha materiais e não pode ser afrouxado após um resultado reprovado sem decisão de mudança registrada.

### 07.3 Teste funcional e de sucesso de tarefa

**Decisão/ação obrigatória.** Para **teste funcional e de sucesso de tarefa**, a organização deve testar tarefas representativas, transições de estado e tratamento de falhas contra requisitos de usuário e sistema.

**Registro e evidência.** Registrar cenário, pré-condição, resultado esperado, resultado real, versão, ambiente, cobertura e defeito.

**Concluído quando.** Tarefas críticas atingem o threshold e caminhos de borda ou exceção reprovados não podem ser escondidos por sucesso agregado.

### 07.4 Teste de qualidade e confiabilidade

**Decisão/ação obrigatória.** Para **teste de qualidade e confiabilidade**, a organização deve medir repetibilidade, consistência e taxa de falha sob carga representativa e variação de entrada.

**Registro e evidência.** Registrar amostra, repetições, variância, latência, modos de falha, intervalo de confiança ou limitação e threshold.

**Concluído quando.** Resultados atingem alvos de confiabilidade pré-aprovados nas fatias materiais e reexecuções permanecem dentro da tolerância.

### 07.5 Precisão, factualidade e ancoragem

**Decisão/ação obrigatória.** Para **precisão, factualidade e ancoragem**, a organização deve definir factualidade aceitável, qualidade de fonte e limites de conteúdo prejudicial para o contexto de uso.

**Registro e evidência.** Registrar categorias de afirmação, fontes autoritativas, conjunto de teste, verificações de citação, thresholds, exemplos de falha e resposta.

**Concluído quando.** Alegações materiais sem suporte são detectadas ou divulgadas e falha acima do threshold bloqueia ou restringe o uso.

### 07.6 Avaliação de fairness e impacto

**Decisão/ação obrigatória.** Para **avaliação de fairness e impacto**, a organização deve definir danos de fairness específicos do contexto, grupos relevantes, fatias e disparidade aceitável antes de testar.

**Registro e evidência.** Registrar rationale do grupo, métricas, adequação da amostra, thresholds, resultados, incerteza, mitigações e impacto residual.

**Concluído quando.** Desempenho agregado não pode esconder uma fatia material reprovada e dano não resolvido é escalonado à authority adequada.

### 07.7 Avaliação de privacidade

**Decisão/ação obrigatória.** Para **avaliação de privacidade**, a organização deve estabelecer finalidade, base legal, minimização, tratamento de direitos, retenção e restrições de transferência para dados pessoais.

**Registro e evidência.** Reter categorias de dados, titulares, origem, finalidade de processamento, acesso, fluxo, DPIA ou equivalente, testes e evidência de exclusão.

**Concluído quando.** Caminhos de dados não autorizados falham em teste, direitos dos titulares são operáveis e mudança material de processamento reabre a avaliação.

### 07.8 Teste de segurança e adversarial

**Decisão/ação obrigatória.** Para **teste de segurança e adversarial**, a organização deve modelar ameaças através das fronteiras de identidade, prompt, dados, ferramenta, runtime e supply chain e testar caminhos materiais de abuso.

**Registro e evidência.** Reter threat model, cenários, pré-condições de ataque, evidência de teste, descobertas, mitigações, risco residual e resultado de reteste.

**Concluído quando.** Caminhos de ataque de alto impacto são prevenidos ou contidos e descobertas bloqueantes abertas impedem o release.

### 07.9 Teste de abuso de prompt, contexto e ferramentas

**Decisão/ação obrigatória.** Para **teste de abuso de prompt, contexto e ferramentas**, a organização deve identificar uso indevido plausível, abuso, viés de automação, expansão de escopo e interação emergente antes do release.

**Registro e evidência.** Registrar ator de ameaça ou usuário, cenário, pré-condição, impacto, detecção, controle preventivo, resposta e exposição residual.

**Concluído quando.** Cenários materiais são testados ou explicitamente restritos e uso indevido observado alimenta controles e reavaliação.

### 07.10 Avaliação de chamadas de ferramenta e ações

**Decisão/ação obrigatória.** Para **avaliação de chamadas de ferramenta e ações**, a organização deve testar seleção de ferramenta, construção de parâmetros, autorização, efeitos colaterais, idempotência e comportamento de recusa.

**Registro e evidência.** Registrar versão da ferramenta, cenário, chamada esperada, chamada observada, decisão de policy, efeito colateral, rollback e evidência.

**Concluído quando.** Chamadas não autorizadas ou malformadas são bloqueadas e retries não podem duplicar uma ação consequente.

### 07.11 Avaliação de supervisão humana

**Decisão/ação obrigatória.** Para **avaliação de supervisão humana**, a organização deve posicionar um humano competente em um ponto de decisão onde a intervenção permaneça oportuna, informada e tecnicamente eficaz.

**Registro e evidência.** Registrar gatilho, informações apresentadas, authority, tempo de resposta, caminho de override, carga de trabalho, treinamento e teste exercitado.

**Concluído quando.** O humano consegue detectar, interromper, corrigir e escalonar uma falha representativa em vez de carimbar uma ação irreversível.

### 07.12 Robustez e comportamento fora da distribuição

**Decisão/ação obrigatória.** Para **robustez e comportamento fora da distribuição**, a organização deve desafiar o sistema com deslocamentos de distribuição, ambiguidade, contexto ausente e degradação de dependências.

**Registro e evidência.** Registrar design do deslocamento, amostra, comportamento seguro esperado, comportamento observado, incerteza, threshold e mitigação.

**Concluído quando.** O sistema degrada, abstém-se ou escalona dentro da fronteira aprovada em vez de agir com confiança fora da evidência.

### 07.13 Teste de falha, rollback e contenção

**Decisão/ação obrigatória.** Para **teste de falha, rollback e contenção**, a organização deve exercitar falhas de modelos, ferramentas, dados, policy, identidade e infraestrutura juntamente com contenção e rollback.

**Registro e evidência.** Reter falha injetada, blast radius, tempo de detecção, tempo de contenção, recuperação, preservação de evidências e descobertas.

**Concluído quando.** A falha testada permanece dentro do blast radius aprovado e a recuperação atinge seu alvo.

### 07.14 Evidências de terceiros e alegações de fornecedores

**Decisão/ação obrigatória.** Para **evidências de terceiros e alegações de fornecedores**, a organização deve classificar evidências de fornecedor por fonte, escopo, atualidade e independência antes de confiar nelas.

**Registro e evidência.** Registrar alegação, artefato, versão do fornecedor, escopo avaliado, corroboração, lacunas, direito contratual e revisor.

**Concluído quando.** Marketing ou auto-attestation não pode satisfazer um controle que exige evidência observada, independente ou específica da organização.

### 07.15 Thresholds e critérios de aceite

**Decisão/ação obrigatória.** Para **thresholds e critérios de aceite**, a organização deve aprovar critérios quantitativos e qualitativos de aprovação, condição e reprovação antes de executar a avaliação.

**Registro e evidência.** Registrar métrica, população, fatia, threshold, rationale, incerteza, status de bloqueio e histórico de mudanças.

**Concluído quando.** Critérios bloqueantes reprovados não podem ser diluídos por média nem afrouxados retroativamente sem nova decisão.

### 07.16 Datasets de teste e representatividade

**Decisão/ação obrigatória.** Para **datasets de teste e representatividade**, a organização deve construir e governar datasets que representem populações pretendidas, afetadas, adversas e de borda.

**Registro e evidência.** Registrar provenance, direitos, período, amostragem, fatias, vazamento (leakage), qualidade, versão e exclusões conhecidas.

**Concluído quando.** Cobertura e limitações são explícitas e dados de teste não podem contaminar treinamento nem exagerar validade no mundo real.

### 07.17 Reproducibilidade e vínculo de versão

**Decisão/ação obrigatória.** Para **reproducibilidade e vínculo de versão**, a organização deve vincular todo resultado a versões de código, modelo, prompt, policy, dados, ferramenta, configuração e ambiente.

**Registro e evidência.** Reter identificadores imutáveis ou hashes, parâmetros de execução, controles de randomização, timestamp e procedimento de reexecução.

**Concluído quando.** Um revisor autorizado consegue reproduzir ou explicar a variância no resultado material a partir do pacote retido.

### 07.18 Pacote de evidências e linhagem

**Decisão/ação obrigatória.** Para **pacote de evidências e linhagem**, a organização deve coletar evidências relevantes para a decisão com identidade, fonte, tempo, versão, integridade e custódia estáveis.

**Registro e evidência.** O manifesto de evidências deve listar artefatos, hashes, produtor, ambiente, método, resultado, limitação e decisão vinculada.

**Concluído quando.** Um revisor consegue recuperar e reproduzir a alegação material e evidência ausente é representada como lacuna, não como sucesso.

### 07.19 Decisão go, conditional-go e no-go

**Decisão/ação obrigatória.** Para **decisão go, conditional-go e no-go**, a organização deve decidir o release somente a partir do pacote vinculado de evidências de risco, avaliação, controle e operação.

**Registro e evidência.** Registrar decisão, authority, versões, critérios aprovados e reprovados, condições, expiração, alvo de rollback e descobertas não resolvidas.

**Concluído quando.** Controles bloqueantes não podem ser dispensados por aprovação condicional e condições expiradas interrompem a operação continuada.

### 07.20 Avaliação contínua e em runtime

**Decisão/ação obrigatória.** Para **avaliação contínua e em runtime**, a organização deve monitorar o comportamento em produção e os resultados de controle que podem invalidar a aprovação.

**Registro e evidência.** Reter definições de sinais, baselines, fatias, thresholds, owner, rota de alerta, investigação e ação de lifecycle vinculada.

**Concluído quando.** Desvio material ou violação de threshold produz contenção ou reavaliação em vez de um alerta informativo sem owner.

### 07.21 Teste de regressão após mudança

**Decisão/ação obrigatória.** Para **teste de regressão após mudança**, a organização deve retestar requisitos afetados após incidente, correção, mudança de dependência ou atualização de modelo/configuração.

**Registro e evidência.** Vincular versões anterior e nova, cenários impactados, conjunto de regressão, resultado, lacunas residuais e disposição de release.

**Concluído quando.** A mudança não invalida silenciosamente evidências anteriores e regressão reprovada impede reativação ou promoção.

### 07.22 Autoavaliação

**Decisão/ação obrigatória.** Para **autoavaliação**, a organização deve exigir que owners avaliem sua implementação contra critérios definidos enquanto declaram as limitações da auto-revisão.

**Registro e evidência.** Registrar papel do avaliador, alegações, evidências, lacunas, confiança, conflitos, decisão solicitada e challenge do revisor.

**Concluído quando.** A autoavaliação encaminha lacunas materiais para revisão e nunca é apresentada como assurance independente.

### 07.23 Challenge por pares

**Decisão/ação obrigatória.** Para **challenge por pares**, a organização deve designar um par qualificado fora do produto de trabalho imediato para desafiar evidências, rationale e cenários ausentes.

**Registro e evidência.** Registrar revisor, conflitos, perguntas, evidências examinadas, discordâncias, disposição e ações.

**Concluído quando.** Alegações disputadas permanecem visíveis e o fechamento exige evidência em vez de consenso ou hierarquia.

### 07.24 Assurance independente e auditoria

**Decisão/ação obrigatória.** Para **assurance independente e auditoria**, a organização deve definir escopo do challenge e critérios de independência antes de o revisor avaliar o trabalho.

**Registro e evidência.** Registrar linha de reporte, conflitos, serviços incompatíveis, população, amostra, critérios, limitações e forma da conclusão.

**Concluído quando.** O revisor não conclui sobre trabalho que ele mesmo desenhou ou operou, e as alegações não excedem o escopo e a evidência aprovados.

### 07.25 Descobertas, ação corretiva e evidência de fechamento

**Decisão/ação obrigatória.** Para **descobertas, ação corretiva e evidência de fechamento**, a organização deve atribuir a cada descoberta uma causa raiz, prioridade baseada em risco, ação corretiva e critério de fechamento.

**Registro e evidência.** Registrar descoberta, evidência, owner, data de vencimento, controle provisório, causa raiz, remediação, reteste e disposição do revisor.

**Concluído quando.** O fechamento exige evidência objetiva de reteste; descobertas materiais vencidas permanecem visíveis e afetam a aprovação.

### 07.26 Retenção de evidências e acesso de auditoria

**Decisão/ação obrigatória.** Para **retenção de evidências e acesso de auditoria**, a organização deve definir quem pode ler, alterar e recuperar o registro, por quanto tempo e sob qual regra de legal hold ou exclusão.

**Registro e evidência.** Registrar classificação, grupos de acesso, custodiano, gatilho de retenção, período mínimo, disposição e caminho de recuperação de auditoria.

**Concluído quando.** Evidências autorizadas são recuperáveis no prazo exigido e dados expirados são descartados sem romper a linhagem exigida.


## Conteúdo canônico incorporado

A seção preserva integralmente as unidades atribuídas pela matriz de cobertura. Os marcadores HTML são provenance machine-readable e não alteram o significado normativo.

### Fonte: `docs/auditability/README.md`

Commit de origem: `5545d9227624400ab8bb707b6032b2f61329a36e`.

<!-- source-unit {"classification": "metadata-title", "end_line": "2", "index": 1, "source_field": "title", "source_heading": "", "source_path": "docs/auditability/README.md", "start_line": "2", "transformation": "integrate-completely", "unit_type": "frontmatter-title"} -->
**Título controlado na origem:** Auditabilidade, evidence package e traceability

<!-- source-unit {"classification": "evidence-artifact", "end_line": "19", "index": 2, "source_field": "", "source_heading": "Auditabilidade, evidence package e traceability", "source_path": "docs/auditability/README.md", "start_line": "18", "transformation": "split-by-heading-with-cross-links", "unit_type": "markdown-atx-heading"} -->
### Auditabilidade, evidence package e traceability

<!-- source-unit {"classification": "objective", "end_line": "23", "index": 3, "source_field": "", "source_heading": "Objetivo", "source_path": "docs/auditability/README.md", "start_line": "20", "transformation": "split-by-heading-with-cross-links", "unit_type": "markdown-atx-heading"} -->
#### Objetivo

Permitir que uma pessoa autorizada reconstrua o que o sistema era, o que fez, com qual autoridade, quais dados e tools usou, quais controles se aplicaram e qual decisão resultou.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "35", "index": 4, "source_field": "", "source_heading": "Auditabilidade não é “logar tudo”", "source_path": "docs/auditability/README.md", "start_line": "24", "transformation": "split-by-heading-with-cross-links", "unit_type": "markdown-atx-heading"} -->
#### Auditabilidade não é “logar tudo”

Logs indiscriminados podem aumentar risco de privacy, custo e exposição. O desenho precisa equilibrar:

- traceability;
- minimização;
- integridade;
- retenção;
- acesso;
- utilidade para investigação;
- separação entre telemetria e record oficial.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "49", "index": 5, "source_field": "", "source_heading": "Eventos mínimos", "source_path": "docs/auditability/README.md", "start_line": "36", "transformation": "split-by-heading-with-cross-links", "unit_type": "markdown-atx-heading"} -->
#### Eventos mínimos

- criação e alteração de registry/blueprint;
- classificação e approvals;
- model, prompt, tool e policy version;
- authentication e authorization decision;
- user/agent/tool correlation;
- retrieval source IDs e data classification quando aplicável;
- state-changing action e result;
- human approval, edit, deny e override;
- policy denial e alert;
- incident, quarantine, rollback e reactivation;
- attestation, exception e sunset.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "68", "index": 6, "source_field": "", "source_heading": "Event envelope", "source_path": "docs/auditability/README.md", "start_line": "50", "transformation": "split-by-heading-with-cross-links", "unit_type": "markdown-atx-heading"} -->
#### Event envelope

| Campo | Propósito |
|---|---|
| timestamp e timezone | ordenar e correlacionar |
| event ID / correlation ID | rastrear a chain |
| agent ID e version | identificar o sistema |
| user/delegated subject | atribuir contexto humano |
| tool/action | identificar capability |
| target/resource | localizar efeito |
| policy/control decision | explicar allow/deny |
| outcome/status | registrar resultado |
| evidence reference | apontar artefato protegido |
| sensitivity | aplicar acesso e retenção |

Sensitive payloads devem ser referenciados ou protegidos, não copiados sem necessidade.

O [AI Agent Audit Event schema](../../toolkit/schemas/audit-event.schema.json) oferece um envelope mínimo vendor-neutral. Ele não obriga ferramenta ou pipeline específico e deliberadamente evita payload completo.

<!-- source-unit {"classification": "evidence-artifact", "end_line": "86", "index": 7, "source_field": "", "source_heading": "Evidence package", "source_path": "docs/auditability/README.md", "start_line": "69", "transformation": "split-by-heading-with-cross-links", "unit_type": "markdown-atx-heading"} -->
#### Evidence package

Um package de release ou attestation deve ser:

- versionado;
- immutable ou tamper-evident;
- ligado a agent/version;
- completo segundo tier;
- acessível somente a roles autorizados;
- retido conforme policy;
- exportável para review;
- capaz de distinguir missing, not-applicable e passed.

“Sem evidência” não significa “controle passou”.

A composição mínima de cada package por nível de risco está em [evidence pack proporcional por tier](07-evaluation-evidence-and-assurance.md).
Use o [Release Evidence Manifest schema](../../toolkit/schemas/release-evidence-manifest.schema.json) para lineage machine-readable e o [template humano](../../toolkit/templates/release-evidence-manifest.md) para preparar a decisão.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "97", "index": 8, "source_field": "", "source_heading": "Integridade e acesso", "source_path": "docs/auditability/README.md", "start_line": "87", "transformation": "split-by-heading-with-cross-links", "unit_type": "markdown-atx-heading"} -->
#### Integridade e acesso

- clock synchronization;
- append-only ou controles de integridade;
- segregação de administradores e auditores;
- access logging;
- redaction/tokenization;
- legal hold quando aplicável;
- test de restauração e export;
- retention/deletion verificáveis.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "113", "index": 9, "source_field": "", "source_heading": "Traceability graph", "source_path": "docs/auditability/README.md", "start_line": "98", "transformation": "split-by-heading-with-cross-links", "unit_type": "markdown-atx-heading"} -->
#### Traceability graph

```text
Business outcome
  ↕
Agent ID/version
  ↕
Blueprint → model/prompt/data/tool versions
  ↕
Risk/control/evaluation decisions
  ↕
Runtime events/incidents
  ↕
Attestation/value/sunset decision
```

<!-- source-unit {"classification": "evidence-artifact", "end_line": "126", "index": 10, "source_field": "", "source_heading": "Evidências", "source_path": "docs/auditability/README.md", "start_line": "114", "transformation": "split-by-heading-with-cross-links", "unit_type": "markdown-atx-heading"} -->
#### Evidências

- logging specification;
- sample events e schema;
- [audit event estruturado](../../toolkit/schemas/audit-event.schema.json);
- access/retention configuration;
- integrity test;
- evidence package index;
- [release evidence manifest](../../toolkit/schemas/release-evidence-manifest.schema.json);
- audit export test;
- deletion e legal-hold records;
- findings e remediação.

<!-- source-unit {"classification": "metric", "end_line": "137", "index": 11, "source_field": "", "source_heading": "Métricas", "source_path": "docs/auditability/README.md", "start_line": "127", "transformation": "split-by-heading-with-cross-links", "unit_type": "markdown-atx-heading"} -->
#### Métricas

- actions sem correlation ID;
- events atrasados, incompletos ou duplicados;
- agents sem version identificável;
- evidence packages incompletos;
- unauthorized log access;
- retention/deletion failures;
- tempo para reconstruir um incident;
- controls com evidence link quebrado.

<!-- source-unit {"classification": "risk-failure-mode", "end_line": "147", "index": 12, "source_field": "", "source_heading": "Failure modes", "source_path": "docs/auditability/README.md", "start_line": "138", "transformation": "split-by-heading-with-cross-links", "unit_type": "markdown-atx-heading"} -->
#### Failure modes

- logar prompt completo por padrão;
- usar dashboard agregado como audit trail;
- não versionar prompt/model/tool;
- permitir que o mesmo admin altere ação e evidência;
- guardar logs sem capability de busca/export;
- apagar evidência no sunset antes de cumprir retenção;
- marcar missing como not-applicable.

<!-- source-unit {"classification": "requirement-control", "end_line": "152", "index": 13, "source_field": "", "source_heading": "Decision gate", "source_path": "docs/auditability/README.md", "start_line": "148", "transformation": "split-by-heading-with-cross-links", "unit_type": "markdown-atx-heading"} -->
#### Decision gate

A release authority exige event model, retention, access, correlation e evidence package compatíveis com o tier antes de produção.

A integração com o universo de auditoria que a organização já opera está em [integração com o audit universe existente](07-evaluation-evidence-and-assurance.md). Um framework que chega como universo paralelo é tolerado, não adotado.

### Fonte: `docs/auditability/audit-universe-crosswalk.md`

Commit de origem: `5545d9227624400ab8bb707b6032b2f61329a36e`.

<!-- source-unit {"classification": "metadata-title", "end_line": "2", "index": 14, "source_field": "title", "source_heading": "", "source_path": "docs/auditability/audit-universe-crosswalk.md", "start_line": "2", "transformation": "integrate-audit-universe-method-completely", "unit_type": "frontmatter-title"} -->
**Título controlado na origem:** Integração com o audit universe existente

<!-- source-unit {"classification": "concept-or-structure", "end_line": "16", "index": 15, "source_field": "", "source_heading": "Integração com o audit universe existente", "source_path": "docs/auditability/audit-universe-crosswalk.md", "start_line": "15", "transformation": "integrate-audit-universe-method-completely", "unit_type": "markdown-atx-heading"} -->
### Integração com o audit universe existente

<!-- source-unit {"classification": "objective", "end_line": "24", "index": 16, "source_field": "", "source_heading": "Objetivo", "source_path": "docs/auditability/audit-universe-crosswalk.md", "start_line": "17", "transformation": "integrate-audit-universe-method-completely", "unit_type": "markdown-atx-heading"} -->
#### Objetivo

Responder à pergunta que auditoria interna faz na primeira reunião: **"como estes controles se relacionam com o que eu já testo?"**

Uma organização madura já tem universo de auditoria, ciclo de teste, matriz de controles financeiros e certificações vigentes. Um framework que chega como universo paralelo não é adotado — é tolerado até a próxima reorganização.

Este documento não mapeia control a control contra normas específicas. Ele responde algo mais útil e mais honesto: **onde estes controles se encaixam no que já existe, e o que muda em relação a um controle de TI convencional.**

<!-- source-unit {"classification": "concept-or-structure", "end_line": "37", "index": 17, "source_field": "", "source_heading": "O que o catálogo oferece a auditoria", "source_path": "docs/auditability/audit-universe-crosswalk.md", "start_line": "25", "transformation": "integrate-audit-universe-method-completely", "unit_type": "markdown-atx-heading"} -->
#### O que o catálogo oferece a auditoria

O [control catalog](../../toolkit/controls/README.md) tem 44 controls, e três campos determinam como auditoria os trata:

| Campo | Valores | O que significa para o teste |
|---|---|---|
| `scope` | 40 `agent`, 4 `organization` | controle de escopo `agent` é testado por amostra de agentes; `organization` é testado uma vez para a entidade |
| `blocking` | 27 bloqueantes | bloqueante impede release quando reprovado — é candidato natural a control chave |
| `automation` | 9 `automated`, 24 `assisted`, 10 `manual`, 1 `mixed` | determina se o teste é de configuração, de amostra ou de processo |
| `verification` | declarado em todos | diz **como** a evidência é obtida, não só que ela existe |

Um control `organization`-scoped nunca é bloqueante por decisão de design ([ADR-0010](../architecture/decisions/0010-structured-governance-contracts-2.0.md)) — falha de governança corporativa não deve travar um release específico; ela dispara remediação no nível certo. Auditoria precisa saber disso antes de desenhar o teste.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "56", "index": 18, "source_field": "", "source_heading": "Onde encaixar no universo existente", "source_path": "docs/auditability/audit-universe-crosswalk.md", "start_line": "38", "transformation": "integrate-audit-universe-method-completely", "unit_type": "markdown-atx-heading"} -->
#### Onde encaixar no universo existente

A recomendação é **não criar um universo novo**. Quase todo control deste framework é uma extensão de um domínio que auditoria já cobre:

| Domínio do framework | Universo em que normalmente encaixa | O que muda em relação ao teste convencional |
|---|---|---|
| registry e ownership | gestão de ativos e CMDB | o ativo tem comportamento próprio e muda sem deploy; inventário exige descoberta contínua, não recertificação anual |
| identidade | IAM e gestão de acessos | a identidade não é de pessoa nem de serviço estático; JML precisa cobrir reatribuição de owner de agente |
| dados | governança de dados e privacidade | a autorização acontece na recuperação, não só na concessão de acesso |
| tools e MCP | gestão de mudanças e integrações | a capacidade de ação pode crescer sem mudança de código, por descoberta de tool |
| modelos e provedores | gestão de fornecedores e terceiros | a versão do fornecedor muda sem aviso e invalida avaliação aceita |
| segurança | segurança da informação | a superfície inclui a instrução, não só a interface |
| evaluations e release | SDLC e gestão de mudanças | o critério de aceite é probabilístico, com threshold e slice, não binário |
| operações e runtime | continuidade e monitoramento | contenção precisa ser exercitada, não documentada |
| Responsible AI e human oversight | conformidade e conduta | frequentemente **não tem** universo prévio — é onde nasce controle novo |
| valor e portfólio | gestão de benefícios | outcome contra baseline, não uso |

Só a linha de Responsible AI costuma exigir universo novo. As demais são extensão de escopo de auditorias que já ocorrem — o que muda a conversa de "crie um programa de auditoria de IA" para "acrescente estas perguntas ao que você já faz".

<!-- source-unit {"classification": "concept-or-structure", "end_line": "66", "index": 19, "source_field": "", "source_heading": "Três diferenças que quebram o teste convencional", "source_path": "docs/auditability/audit-universe-crosswalk.md", "start_line": "57", "transformation": "integrate-audit-universe-method-completely", "unit_type": "markdown-atx-heading"} -->
#### Três diferenças que quebram o teste convencional

Vale antecipá-las, porque cada uma já invalidou papel de trabalho em alguma organização.

**1. Evidência tem data de validade curta.** Um control de TI testado em março costuma valer para o ano. Aqui, mudança de versão de modelo, de fonte de dados ou de tool invalida a evidência no dia em que acontece. O teste precisa amarrar a evidência à **versão** do agente, não ao período. O [evidence pack por tier](07-evaluation-evidence-and-assurance.md) e o release manifest existem para isso.

**2. Amostragem por população homogênea não funciona.** O estate é deliberadamente heterogêneo por tier. Amostrar 25 agentes ao acaso mede quase só T1, porque T1 é a maioria. A amostra precisa ser **estratificada por tier e por admissibilidade**, com cobertura integral dos T3 e T4.

**3. Aprovação não é evidência de controle.** Um release `conditional` aprovado não diz que as condições foram cumpridas — diz que foram impostas. O teste é sobre a **verificação declarada de cada condição**, e é por isso que o contrato de release exige que toda condição traga owner e método de verificação.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "78", "index": 20, "source_field": "", "source_heading": "Onde começar um primeiro teste", "source_path": "docs/auditability/audit-universe-crosswalk.md", "start_line": "67", "transformation": "integrate-audit-universe-method-completely", "unit_type": "markdown-atx-heading"} -->
#### Onde começar um primeiro teste

Sugestão de escopo para o primeiro ciclo, em ordem de retorno:

1. **Completude e ownership do registry** — agente em produção sem business owner nomeado é o achado mais comum e o mais fácil de evidenciar.
2. **Os 27 controls bloqueantes**, verificando se realmente bloqueiam — control bloqueante que nunca reprovou nada merece investigação.
3. **Attestation vencida** em agentes ativos.
4. **Condições de release com prazo expirado** e agentes ainda operando.
5. **Bindings de catálogo** — modelo, fonte ou tool em uso sem entrada aprovada correspondente.

Os itens 4 e 5 são verificáveis por consulta aos records estruturados, sem depender de entrevista. Comece por onde a evidência já é máquina-legível.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "83", "index": 21, "source_field": "", "source_heading": "Limites declarados", "source_path": "docs/auditability/audit-universe-crosswalk.md", "start_line": "79", "transformation": "integrate-audit-universe-method-completely", "unit_type": "markdown-atx-heading"} -->
#### Limites declarados

Este documento **não** é mapeamento control a control contra ISO/IEC 42001, 23894, 42005, SOX ou qualquer norma específica. Os `frameworkMappings` do catálogo declaram alinhamento direcional e dizem isso explicitamente: *"não constitui equivalência, conformidade nem atestação"*. O escopo de cada norma referenciada está em [`references/standards/`](../../research/sources/standards-scope-and-limitations.md), com o motivo de não haver mapeamento cláusula a cláusula.

Quem precisar de mapeamento formal precisa adquirir os textos normativos e produzi-lo internamente, com a authority competente. Alinhamento declarado por um framework de referência não substitui essa avaliação.

### Fonte: `docs/auditability/evidence-pack-by-tier.md`

Commit de origem: `5545d9227624400ab8bb707b6032b2f61329a36e`.

<!-- source-unit {"classification": "metadata-title", "end_line": "2", "index": 22, "source_field": "title", "source_heading": "", "source_path": "docs/auditability/evidence-pack-by-tier.md", "start_line": "2", "transformation": "synthesize-and-preserve", "unit_type": "frontmatter-title"} -->
**Título controlado na origem:** Evidence pack proporcional por tier

<!-- source-unit {"classification": "evidence-artifact", "end_line": "18", "index": 23, "source_field": "", "source_heading": "Evidence pack proporcional por tier", "source_path": "docs/auditability/evidence-pack-by-tier.md", "start_line": "17", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
### Evidence pack proporcional por tier

<!-- source-unit {"classification": "objective", "end_line": "26", "index": 24, "source_field": "", "source_heading": "Objetivo", "source_path": "docs/auditability/evidence-pack-by-tier.md", "start_line": "19", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Objetivo

Definir qual evidência cada tier precisa produzir, em que formato e por quanto tempo — de modo que auditoria, investigação e reassessment sejam rápidos e que o custo da evidência seja proporcional ao risco.

**Todos os tiers produzem evidência.** Governança proporcional não significa ausência de registro; significa que evidência simples e gerada automaticamente é suficiente quando o risco é baixo. Sem isso, a organização perde rastreabilidade exatamente onde o volume é maior.

T4 também exige evidência reforçada por criticidade. Admissibilidade é separada: quando a decisão for `restricted` ou `prohibited`, a decisão e qualquer exceção precisam ser auditáveis em qualquer tier.

<!-- source-unit {"classification": "evidence-artifact", "end_line": "39", "index": 25, "source_field": "", "source_heading": "Evidence pack mínimo por tier", "source_path": "docs/auditability/evidence-pack-by-tier.md", "start_line": "27", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Evidence pack mínimo por tier

| Tier | Pacote mínimo | Objetivo |
|---|---|---|
| **T1** | `agent_id` e registro de descoberta; resultado do pre-screen com tier e admissibilidade; business e technical owner e contexto de uso; resultado do policy gate; blueprint reduzido; referências das fontes de dados e das tools aprovadas; padrão de identidade aprovado; logging padrão com os campos mínimos chegando ao pipeline; resultado dos testes funcionais; impact assessment quando o trigger for acionado; rollback documentado; aprovação de owner ou do policy gate; data de attestation | demonstrar ownership, escopo conhecido e controles básicos sem criar review manual desnecessário |
| **T2** | tudo de T1 + blueprint versionado; risk record formal com escaladores; domain reviews acionadas; aprovações de dados e tools; identidade e permissões; resultados de evals e testes de segurança; rollback testado; telemetria; residual risk; aprovação de publicação | permitir assurance formal, investigação e reassessment de agente transacional |
| **T3** | tudo de T2 + threat model e abuse cases; impact assessment quando aplicável; testes adversariais e de resiliência; design de oversight humano e step-up; teste de kill switch e quarentena; baseline de comportamento; aceitação explícita de residual risk pela authority; attestation frequente | demonstrar que autonomia e impacto elevados receberam assurance reforçado e capacidade de contenção |
| **T4** | tudo de T3 + architecture/assurance challenge reforçado; cenários críticos; segregation e dual control quando aplicável; containment/fail-safe exercitados; executive risk decision; attestation orientada a evento | sustentar investigação e decisão para impactos críticos ou difíceis de reverter |

O [fast path de T1](04-risk-impact-and-compliance.md#fast-path-de-t1) não encurta a lista de T1: ele a **gera automaticamente**. A rota automatizada reduz trabalho humano, não a evidência exigida.

Cada linha desta tabela precisa cobrir tudo que o [Minimum Production Bar](../../toolkit/controls/minimum-production-bar.md) exige no mesmo tier. As duas tabelas descrevem o mesmo piso por ângulos diferentes — o MPB diz qual controle precisa existir, o evidence pack diz o que comprova que ele existe — e **não podem divergir**. Divergência entre as duas é defeito, não nuance: significa que o gate exige um controle cuja existência ninguém precisa demonstrar.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "45", "index": 26, "source_field": "", "source_heading": "Overlay de admissibilidade", "source_path": "docs/auditability/evidence-pack-by-tier.md", "start_line": "40", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
##### Overlay de admissibilidade

- `conditional`: inclua condições, owner, testes, monitoring e expiry;
- `restricted`: inclua exception request, authority, compensating controls, escopo e expiry;
- `prohibited`: inclua rationale e decision record de rejeição; não gere manifesto de release aprovado.

<!-- source-unit {"classification": "evidence-artifact", "end_line": "57", "index": 27, "source_field": "", "source_heading": "Qualidade da evidência", "source_path": "docs/auditability/evidence-pack-by-tier.md", "start_line": "46", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Qualidade da evidência

Um artefato só conta como evidência quando é:

- **recuperável** — existe endereço estável e alguém consegue abri-lo meses depois;
- **atribuída** — quem produziu, quando e com qual escopo;
- **versionada** — vinculada à versão do agente e do modelo de risco que a originou;
- **íntegra** — protegida contra alteração silenciosa; hash recomendado para snapshots;
- **interpretável** — um terceiro competente entende o que ela demonstra sem o autor presente.

Uma caixa marcada não é evidência. Um print sem contexto, data ou origem não é evidência.

<!-- source-unit {"classification": "procedure", "end_line": "63", "index": 28, "source_field": "", "source_heading": "Evidência é produto do processo", "source_path": "docs/auditability/evidence-pack-by-tier.md", "start_line": "58", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Evidência é produto do processo

Evidence pack montado depois, para satisfazer uma auditoria, custa mais e vale menos. A evidência precisa ser subproduto natural de executar o processo: o eval gera o relatório, o gate gera o decision record, o deploy gera o baseline, o incidente gera a timeline.

Quando a evidência exige trabalho extra significativo, isso é sinal de que o processo não está instrumentado — não de que falta disciplina das equipes.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "70", "index": 29, "source_field": "", "source_heading": "Retenção e acesso", "source_path": "docs/auditability/evidence-pack-by-tier.md", "start_line": "64", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Retenção e acesso

- defina retenção por tier e por tipo de evidência, alinhada às obrigações aplicáveis;
- preserve a evidência de versões anteriores: uma nova release não sobrescreve o histórico da anterior;
- em quarentena e incidente, a preservação é deliberada e vem antes da remediação;
- em retirada, arquive conforme a retenção antes de revogar acessos.

<!-- source-unit {"classification": "evidence-artifact", "end_line": "77", "index": 30, "source_field": "", "source_heading": "Artefatos", "source_path": "docs/auditability/evidence-pack-by-tier.md", "start_line": "71", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Artefatos

- Agent Evidence Pack Standard: lista por tier, formato, repositório, retenção, vínculo de versão e verificação de completude;
- índice de evidências por agente e release;
- [release evidence manifest](../../toolkit/schemas/release-evidence-manifest.schema.json) e [template humano](../../toolkit/templates/release-evidence-manifest.md);
- [evidence package as code](../../toolkit/patterns/evidence-package-as-code.md).

<!-- source-unit {"classification": "evidence-artifact", "end_line": "84", "index": 31, "source_field": "", "source_heading": "Evidências", "source_path": "docs/auditability/evidence-pack-by-tier.md", "start_line": "78", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Evidências

- índice do pacote por release, com endereços recuperáveis;
- verificação de completude executada no gate;
- registro de retenção e de expurgo;
- histórico de acesso quando exigido pela obrigação aplicável.

<!-- source-unit {"classification": "metric", "end_line": "92", "index": 32, "source_field": "", "source_heading": "Métricas", "source_path": "docs/auditability/evidence-pack-by-tier.md", "start_line": "85", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Métricas

- releases com evidence pack incompleto no momento do gate;
- evidências referenciadas que não abrem;
- tempo médio para reunir o pacote de um agente sob investigação;
- proporção de evidência gerada automaticamente versus montada manualmente;
- evidências fora da política de retenção.

<!-- source-unit {"classification": "risk-failure-mode", "end_line": "101", "index": 33, "source_field": "", "source_heading": "Failure modes", "source_path": "docs/auditability/evidence-pack-by-tier.md", "start_line": "93", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Failure modes

- montar o pacote depois, para a auditoria;
- tratar caixa marcada como evidência;
- pacote pesado em T1 que ninguém consegue sustentar no volume real;
- pacote leve em T3 que não sustenta investigação;
- sobrescrever evidência ao publicar nova versão;
- evidência sem vínculo com a versão do modelo de risco que a produziu.

<!-- source-unit {"classification": "requirement-control", "end_line": "104", "index": 34, "source_field": "", "source_heading": "Decision gate", "source_path": "docs/auditability/evidence-pack-by-tier.md", "start_line": "102", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Decision gate

Nenhum release é aprovado com item obrigatório do pacote do tier ausente. Ausência de evidência é registrada como `missing` e nunca convertida em `passed`.

### Fonte: `docs/evaluations/README.md`

Commit de origem: `5545d9227624400ab8bb707b6032b2f61329a36e`.

<!-- source-unit {"classification": "metadata-title", "end_line": "2", "index": 35, "source_field": "title", "source_heading": "", "source_path": "docs/evaluations/README.md", "start_line": "2", "transformation": "integrate-completely", "unit_type": "frontmatter-title"} -->
**Título controlado na origem:** Evaluations, quality gates e release evidence

<!-- source-unit {"classification": "requirement-control", "end_line": "16", "index": 36, "source_field": "", "source_heading": "Evaluations, quality gates e release evidence", "source_path": "docs/evaluations/README.md", "start_line": "15", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
### Evaluations, quality gates e release evidence

<!-- source-unit {"classification": "objective", "end_line": "22", "index": 37, "source_field": "", "source_heading": "Objetivo", "source_path": "docs/evaluations/README.md", "start_line": "17", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Objetivo

Produzir evidência de que o sistema atende ao intended use, riscos e controles antes do release e continua adequado em operação.

O perfil de GenAI do NIST destaca pre-deployment testing e incident disclosure entre suas considerações primárias.[8] O framework amplia esse princípio para agentes, tools e efeitos operacionais.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "37", "index": 38, "source_field": "", "source_heading": "Evaluation strategy", "source_path": "docs/evaluations/README.md", "start_line": "23", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Evaluation strategy

Uma estratégia declara:

- intended e prohibited use;
- scenarios e personas;
- quality dimensions;
- risk-based thresholds;
- datasets e provenance;
- automated e human evaluation;
- negative, adversarial e edge cases;
- slices relevantes;
- runtime metrics;
- promotion, rollback e sunset criteria.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "48", "index": 39, "source_field": "", "source_heading": "Pirâmide de avaliação", "source_path": "docs/evaluations/README.md", "start_line": "38", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Pirâmide de avaliação

```mermaid
flowchart TB
    U[Outcome e impacto real]
    S[System/chain tests]
    C[Component tests]
    D[Data e test-set quality]
    D --> C --> S --> U
```

<!-- source-unit {"classification": "concept-or-structure", "end_line": "56", "index": 40, "source_field": "", "source_heading": "Data e test set", "source_path": "docs/evaluations/README.md", "start_line": "49", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
##### Data e test set

- representatividade contextual;
- provenance e licença;
- cobertura de red flags e edge cases;
- separação de train/tune/test quando aplicável;
- versioning e leakage control.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "62", "index": 41, "source_field": "", "source_heading": "Component", "source_path": "docs/evaluations/README.md", "start_line": "57", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
##### Component

- prompt, model, retrieval, classifier e tool separadamente;
- schema, authz, safety e output validation;
- deterministic tests para código e policy.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "71", "index": 42, "source_field": "", "source_heading": "System/chain", "source_path": "docs/evaluations/README.md", "start_line": "63", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
##### System/chain

- end-to-end scenarios;
- multi-step tool use;
- indirect prompt injection;
- rollback e idempotency;
- latency, cost e failure propagation;
- human approval e escalation.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "79", "index": 43, "source_field": "", "source_heading": "Outcome", "source_path": "docs/evaluations/README.md", "start_line": "72", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
##### Outcome

- qualidade no processo real;
- impacto em pessoas e grupos;
- erro operacional;
- adoção e suporte;
- valor versus baseline.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "92", "index": 44, "source_field": "", "source_heading": "Quality dimensions", "source_path": "docs/evaluations/README.md", "start_line": "80", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Quality dimensions

- correctness e groundedness;
- relevance e completeness;
- safety e harmfulness;
- security e policy compliance;
- robustness e consistency;
- fairness por slices relevantes;
- transparency e citation quality;
- latency, availability e cost;
- task success e reversibility;
- human usability e override.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "106", "index": 45, "source_field": "", "source_heading": "Thresholds", "source_path": "docs/evaluations/README.md", "start_line": "93", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Thresholds

Threshold precisa de:

- métrica e unidade;
- dataset/scenario;
- rationale;
- owner;
- minimum e target;
- action quando falha;
- validade e review trigger.

Média agregada não pode compensar falha em red flag. Gates críticos são binários quando a tolerância é zero.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "116", "index": 46, "source_field": "", "source_heading": "LLM-as-judge", "source_path": "docs/evaluations/README.md", "start_line": "107", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### LLM-as-judge

Pode apoiar escala, desde que:

- rubric e model/version sejam registrados;
- calibração humana seja amostrada;
- bias e instability sejam medidos;
- high-impact decisions não dependam de um único judge;
- outputs sejam tratados como evidência auxiliar.

<!-- source-unit {"classification": "evidence-artifact", "end_line": "129", "index": 47, "source_field": "", "source_heading": "Release evidence package", "source_path": "docs/evaluations/README.md", "start_line": "117", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Release evidence package

- registry e blueprint aprovados;
- risk tier e assessments aplicáveis;
- model/data/tool versions;
- test plan e datasets;
- resultados, failures e limitações;
- security e Responsible AI evidence;
- human oversight e UX evidence;
- runtime thresholds e runbooks;
- rollback/quarantine drill;
- approvals, conditions e expiry.

<!-- source-unit {"classification": "requirement-control", "end_line": "144", "index": 48, "source_field": "", "source_heading": "Promotion gate", "source_path": "docs/evaluations/README.md", "start_line": "130", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Promotion gate

```mermaid
flowchart LR
    B[Baseline] --> T[Test plan]
    T --> E[Execute]
    E --> F{Thresholds}
    F -->|pass| R[Review evidence]
    F -->|fail| X[Remediate]
    R --> D{Authority}
    D -->|approve| P[Release]
    D -->|condition| X
    D -->|reject| N[Stop]
```

<!-- source-unit {"classification": "architecture-runtime", "end_line": "155", "index": 49, "source_field": "", "source_heading": "Runtime evaluation", "source_path": "docs/evaluations/README.md", "start_line": "145", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Runtime evaluation

- sample quality review;
- drift de input, output, source e user behavior;
- policy denials e safety signals;
- tool success e side effects;
- incidents, complaints e overrides;
- cost/latency regressions;
- canary e rollback criteria;
- periodic attestation.

<!-- source-unit {"classification": "evidence-artifact", "end_line": "166", "index": 50, "source_field": "", "source_heading": "Evidências", "source_path": "docs/evaluations/README.md", "start_line": "156", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Evidências

- versioned evaluation plan;
- test sets e provenance;
- raw e summarized results;
- failure analysis;
- human review/calibration;
- gate decision;
- runtime trend e incident feedback;
- regression suite atualizada.

<!-- source-unit {"classification": "metric", "end_line": "177", "index": 51, "source_field": "", "source_heading": "Métricas", "source_path": "docs/evaluations/README.md", "start_line": "167", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Métricas

- coverage de critical scenarios;
- pass/fail por dimension e slice;
- escaped defects/incidents;
- false positive/negative de safety controls;
- regression recurrence;
- judge-human agreement;
- time to evaluate after material change;
- agents operating with expired evidence.

<!-- source-unit {"classification": "risk-failure-mode", "end_line": "188", "index": 52, "source_field": "", "source_heading": "Failure modes", "source_path": "docs/evaluations/README.md", "start_line": "178", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Failure modes

- demo usada como evaluation;
- test set escolhido depois de ver o resultado;
- threshold sem rationale;
- avaliar apenas output textual e ignorar tool effect;
- confiar em média agregada;
- LLM judge sem calibração;
- release approval sem raw evidence;
- não converter incidentes em regression tests.

<!-- source-unit {"classification": "reference", "end_line": "191", "index": 53, "source_field": "", "source_heading": "Sources", "source_path": "docs/evaluations/README.md", "start_line": "189", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
#### Sources

[8] <https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf> — NIST AI 600-1 Generative AI Profile

## Acceptance criteria

- todas as decisões deste capítulo possuem authority, owner e evidência recuperável;
- requisitos aplicáveis estão ligados ao catálogo de controles e ao método de verificação;
- exceções têm escopo, justificativa, compensating controls, expiry e decisão residual;
- controles de build time e runtime são distinguidos e exercitados quando aplicáveis;
- mudanças materiais reabrem avaliação, aprovação e evidência;
- nenhuma alegação de conformidade, eficácia ou valor excede a evidência observada.

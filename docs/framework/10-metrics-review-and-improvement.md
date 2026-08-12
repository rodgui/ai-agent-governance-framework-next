---
title: 10 — Métricas, revisão e melhoria contínua
status: maintained
maturity: validated
last_reviewed: 2026-08-11
review_cycle: quarterly
owners: [framework-maintainers]
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# 10 — Métricas, revisão e melhoria contínua

Este capítulo integra a estrutura clean-room aprovada com o conteúdo substantivo do corpus autoritativo. Requisitos do framework são vendor-neutral; legislação externa, guidance, casos e histórico são identificados como tais. A implementação organizacional exige adoção formal pela authority competente e não decorre do versionamento deste repositório.

## Contrato operacional do capítulo

As subseções seguintes formam um contrato executável de completude. Cada uma especifica a decisão ou ação requerida, o record/evidence mínimo e uma condição observável de conclusão para levar a governança do zero ao business as usual.

### 10.1 Measurement principles and metric ownership

**Required decision/action.** For **measurement principles and metric ownership**, the organization must assign every metric a decision purpose, owner and accountable consumer before collection.

**Record and evidence.** The metric dictionary must define formula, population, source, quality, cutoff, segmentation, target and misuse warning.

**Done when.** Two analysts reproduce the value and the consuming authority states what decision a threshold can change.

### 10.2 Governance coverage

**Required decision/action.** For **governance coverage**, the organization must measure the declared population against governed, registered, owned and current records.

**Record and evidence.** Retain denominator source, reconciliation date, unmatched assets, confidence, exclusions and remediation owner.

**Done when.** Coverage cannot improve by shrinking an undeclared denominator and missing high-risk assets remain visible.

### 10.3 Inventory completeness and ownership quality

**Required decision/action.** For **inventory completeness and ownership quality**, the organization must measure the declared population against governed, registered, owned and current records.

**Record and evidence.** Retain denominator source, reconciliation date, unmatched assets, confidence, exclusions and remediation owner.

**Done when.** Coverage cannot improve by shrinking an undeclared denominator and missing high-risk assets remain visible.

### 10.4 Process performance and decision latency

**Required decision/action.** For **process performance and decision latency**, the organization must measure queue, cycle time, handoff delay, rework and decision aging by tier and outcome.

**Record and evidence.** Record timestamps, population, service target, bottleneck, exception, demand and capacity assumptions.

**Done when.** Latency reduction does not bypass required evidence and persistent bottlenecks receive an owner and redesign decision.

### 10.5 Risk exposure and residual risk

**Required decision/action.** For **risk exposure and residual risk**, the organization must present residual risk after verified treatment to the authority empowered for that exposure.

**Record and evidence.** Record inherent risk, treatment evidence, residual rating, uncertainty, acceptance conditions, approver and expiry.

**Done when.** The delivery team cannot self-accept material residual risk and acceptance does not override admissibility or law.

### 10.6 Quality, safety, fairness, privacy and security indicators

**Required decision/action.** For **quality, safety, fairness, privacy and security indicators**, the organization must define leading and lagging indicators for the named quality, impact or control outcome.

**Record and evidence.** Record formula, population, slices, threshold, baseline, confidence, source quality and response owner.

**Done when.** The indicator detects meaningful deterioration without masking failed slices or treating absence of telemetry as success.

### 10.7 Incident, exception and remediation trends

**Required decision/action.** For **incident, exception and remediation trends**, the organization must analyze recurrence, aging, severity, root cause and closure quality across incidents and exceptions.

**Record and evidence.** Record comparable taxonomy, period, population, reopenings, overdue items, systemic causes and management action.

**Done when.** Trend review distinguishes more detection from more harm and leads to prevention or control redesign where warranted.

### 10.8 Control implementation versus effectiveness

**Required decision/action.** For **control implementation versus effectiveness**, the organization must report design, implementation, operating coverage and observed effectiveness as separate states.

**Record and evidence.** Record control ID, owner, applicable population, implementation evidence, test method, result, gaps and retest date.

**Done when.** A configured control is not called effective without outcome evidence and failed effectiveness changes risk or approval.

### 10.9 Evidence completeness and quality

**Required decision/action.** For **evidence completeness and quality**, the organization must measure whether required evidence exists, is current, attributable, intact and decision-relevant.

**Record and evidence.** Record evidence requirement, population, present/missing/stale status, integrity, reviewer and remediation.

**Done when.** Missing or low-quality evidence lowers confidence and cannot be counted as a passed control.

### 10.10 Adoption and user behavior

**Required decision/action.** For **adoption and user behavior**, the organization must measure intended adoption, meaningful use and unsafe workaround behavior by target population.

**Record and evidence.** Record eligible population, active use, task completion, abandonment, support demand, feedback and sampling limitations.

**Done when.** The owner can distinguish availability from useful adoption and can change training, design or rollout based on evidence.

### 10.11 Cost and efficiency

**Required decision/action.** For **cost and efficiency**, the organization must attribute consumption and total operating cost to agent, owner, environment and measurable outcome.

**Record and evidence.** Record unit cost, budget, quota, forecast, variance, shared-cost allocation, anomaly and optimization decision.

**Done when.** Threshold breach triggers throttling or review and cost claims remain separate from value realization claims.

### 10.12 Outcome and value realization

**Required decision/action.** For **outcome and value realization**, the organization must define a falsifiable outcome, pre-change baseline and credible counterfactual with an evidence cutoff.

**Record and evidence.** Record metric owner, population, formula, target, source, confounders, cost and decision threshold.

**Done when.** The authority can distinguish creation, adoption, quality and outcome and can stop work when evidence does not support expansion.

### 10.13 Supplier performance

**Required decision/action.** For **supplier performance**, the organization must govern supplier and downstream dependencies through due diligence, contract, monitoring and exit planning.

**Record and evidence.** Record service, owner, criticality, evidence, obligations, concentration, incidents, sub-processors, fallback and exit test.

**Done when.** Supplier failure triggers the agreed containment or fallback and accountability remains with the organization.

### 10.14 Maturity assessment and confidence

**Required decision/action.** For **maturity assessment and confidence**, the organization must score organizational capability only from observed operation and separately state evidence confidence and coverage.

**Record and evidence.** Record dimension, criteria, evidence, score 0–4, rationale, confidence, coverage, reviewer and target.

**Done when.** The score cannot exceed the lowest demonstrated criterion and comparison uses compatible scope and method.

### 10.15 Portfolio review cadence

**Required decision/action.** For **portfolio review cadence**, the organization must set a risk-based review cadence and event-driven triggers rather than relying only on a calendar.

**Record and evidence.** Record last review, next review, trigger, reviewer, evidence cutoff, decision and open actions.

**Done when.** Overdue or trigger-affected artifacts are visible and cannot remain silently approved.

### 10.16 Policy, control and standard review

**Required decision/action.** For **policy, control and standard review**, the organization must review requirements against incidents, exceptions, tests, external change and implementation experience.

**Record and evidence.** Record artifact version, evidence considered, gaps, proposed change, consultation, decision and migration impact.

**Done when.** Obsolete or ineffective requirements are revised or superseded without erasing historical decisions.

### 10.17 Regulatory, threat and technology change

**Required decision/action.** For **regulatory, threat and technology change**, the organization must define material changes and external events that reopen risk, approval, evaluation or contract compatibility.

**Record and evidence.** Record trigger, detection source, impacted assets and evidence, interim control, owner, due date and disposition.

**Done when.** Triggered assets cannot rely indefinitely on prior approval and the new decision is linked to the changed version.

### 10.18 Improvement backlog and prioritization

**Required decision/action.** For **improvement backlog and prioritization**, the organization must maintain one risk- and dependency-aware backlog for control, platform, process and evidence improvements.

**Record and evidence.** Record finding source, severity, benefit, owner, dependency, effort, due date, status and acceptance criterion.

**Done when.** Priority changes are explicit and overdue material items influence risk, funding or operating decisions.

### 10.19 Maintain, expand, restrict, redesign or retire decisions

**Required decision/action.** For **maintain, expand, restrict, redesign or retire decisions**, the organization must select one portfolio disposition from current outcome, risk, cost, adoption and evidence.

**Record and evidence.** Record alternatives, evidence cutoff, decision, authority, conditions, affected assets and implementation owner.

**Done when.** The disposition changes funding, exposure or lifecycle state and is not merely a recommendation with no owner.

### 10.20 Management review and accountability reporting

**Required decision/action.** For **management review and accountability reporting**, the organization must present an integrated view of outcomes, risk, control effectiveness, incidents, exceptions, resources and decisions to accountable management.

**Record and evidence.** Retain agenda, evidence cutoff, material limitations, challenged assumptions, decisions, owners, dates and follow-up.

**Done when.** Management records explicit maintain, improve, restrict, fund or retire decisions and tracks them to closure.


## Conteúdo canônico incorporado

A seção preserva integralmente as unidades atribuídas pela matriz de cobertura. Os marcadores HTML são provenance machine-readable e não alteram o significado normativo.

### Fonte: `docs/operations/finops.md`

Commit de origem: `5545d9227624400ab8bb707b6032b2f61329a36e`.

<!-- source-unit {"classification": "metadata-title", "end_line": "2", "index": 1, "source_field": "title", "source_heading": "", "source_path": "docs/operations/finops.md", "start_line": "2", "transformation": "synthesize-and-preserve", "unit_type": "frontmatter-title"} -->
**Título controlado na origem:** FinOps de agentes e unit economics

<!-- source-unit {"classification": "concept-or-structure", "end_line": "16", "index": 2, "source_field": "", "source_heading": "FinOps de agentes e unit economics", "source_path": "docs/operations/finops.md", "start_line": "15", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
### FinOps de agentes e unit economics

<!-- source-unit {"classification": "objective", "end_line": "22", "index": 3, "source_field": "", "source_heading": "Objetivo", "source_path": "docs/operations/finops.md", "start_line": "17", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Objetivo

Sair de "custo por token" para **custo por resultado**, atribuir esse custo a um responsável e detectar desperdício antes que ele vire um problema de orçamento ou um vetor de abuso.

Um modelo mais caro por token pode ser economicamente melhor se reduzir retries e retrabalho humano. A comparação relevante é sempre **custo por tarefa concluída com qualidade preservada**.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "28", "index": 4, "source_field": "", "source_heading": "Atribuição", "source_path": "docs/operations/finops.md", "start_line": "23", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Atribuição

Todo custo material precisa responder a quatro perguntas: **qual agente, qual owner, qual unidade de negócio, qual caso de uso.**

Sem chave de correlação no evento de custo, FinOps enxerga gasto sem contexto e a decisão de portfólio vira opinião.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "40", "index": 5, "source_field": "", "source_heading": "Decomposição do custo", "source_path": "docs/operations/finops.md", "start_line": "29", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Decomposição do custo

Separe as camadas quando forem materiais:

- inferência;
- retrieval e indexação;
- execução de ferramentas e chamadas externas;
- armazenamento e memória;
- observabilidade e retenção de evidência;
- **supervisão e aprovação humana** — frequentemente o maior custo em T3 e sistematicamente esquecido;
- custo de build e teste, separado do custo de produção.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "48", "index": 6, "source_field": "", "source_heading": "Unit economics", "source_path": "docs/operations/finops.md", "start_line": "41", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Unit economics

1. Definir a unidade de resultado do caso: ticket resolvido, fatura processada, documento revisado.
2. Medir custo por unidade **bem-sucedida**, não por execução. Tentativas falhas são custo do sucesso.
3. Comparar contra o baseline do processo anterior, com as limitações declaradas.
4. Incluir o custo humano de revisão quando o desenho exige aprovação.
5. Reavaliar após mudança de versão de modelo — o custo por tarefa pode mudar sem que o preço por token mude.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "58", "index": 7, "source_field": "", "source_heading": "Budget, quota e denial-of-wallet", "source_path": "docs/operations/finops.md", "start_line": "49", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Budget, quota e denial-of-wallet

- budget por caso de uso e por tier, não apenas orçamento global;
- quota e circuit breaker por agente, com limite de chamadas, profundidade de cadeia e duração;
- loops e retries descontrolados são simultaneamente problema de custo e sinal de segurança — veja [behavioral analytics](../../toolkit/templates/behavioral-analytics-use-case.md);
- notificação ao owner antes de enforcement automático;
- exceção de budget com prazo, como qualquer outra exceção.

O ataque de *denial-of-wallet* não derruba o sistema: ele o torna economicamente inviável. Um agente exposto sem quota é uma superfície de custo aberta.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "64", "index": 8, "source_field": "", "source_heading": "Alavancas de otimização", "source_path": "docs/operations/finops.md", "start_line": "59", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Alavancas de otimização

Cache · tamanho de contexto e estratégia de recuperação · roteamento entre modelos com equivalência de controles · redução de profundidade de cadeia · reuso de resultados · escolha de ferramenta com menor custo por chamada.

Nenhuma alavanca pode reduzir silenciosamente o nível de assurance. Roteamento por custo segue as regras de [governança de modelos](06-architecture-and-technical-controls.md#fallback-routing-e-equivalência-de-controles).

<!-- source-unit {"classification": "concept-or-structure", "end_line": "68", "index": 9, "source_field": "", "source_heading": "Integração com portfólio", "source_path": "docs/operations/finops.md", "start_line": "65", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Integração com portfólio

O custo total entra na [decisão de portfólio](03-inventory-portfolio-and-value.md#value-review): manter, expandir, corrigir, restringir, substituir ou aposentar. Um agente com bom outcome e unit economics ruim é candidato a redesenho, não a expansão.

<!-- source-unit {"classification": "evidence-artifact", "end_line": "77", "index": 10, "source_field": "", "source_heading": "Evidências", "source_path": "docs/operations/finops.md", "start_line": "69", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Evidências

- modelo de custo com premissas e fontes;
- atribuição por agente, owner, unidade e caso;
- custo por resultado com baseline e limitações;
- budgets, quotas e exceções vigentes;
- anomalias de custo investigadas e desfecho;
- variação de custo após mudança de versão de modelo.

<!-- source-unit {"classification": "metric", "end_line": "87", "index": 11, "source_field": "", "source_heading": "Métricas", "source_path": "docs/operations/finops.md", "start_line": "78", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Métricas

- custo por agente, por sessão e por resultado bem-sucedido;
- variação contra budget por tier e por unidade;
- proporção de custo gasto em execuções que falharam;
- agentes sem budget ou sem quota em produção;
- anomalias de custo por período e tempo até resposta;
- custo de supervisão humana como fração do total em T3;
- concentração de custo por provedor e modelo.

<!-- source-unit {"classification": "risk-failure-mode", "end_line": "97", "index": 12, "source_field": "", "source_heading": "Failure modes", "source_path": "docs/operations/finops.md", "start_line": "88", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Failure modes

- comparar apenas preço por token;
- medir custo por execução em vez de por sucesso;
- ignorar o custo de supervisão, suporte e assurance;
- orçamento global sem quota por agente;
- automatizar corte de budget sem notificar o owner;
- otimizar custo trocando modelo sem equivalência de controles;
- tratar pico de custo apenas como tema financeiro quando também é sinal de segurança.

<!-- source-unit {"classification": "requirement-control", "end_line": "100", "index": 13, "source_field": "", "source_heading": "Decision gate", "source_path": "docs/operations/finops.md", "start_line": "98", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Decision gate

Nenhum agente entra em produção sem atribuição de custo, budget do caso e quota compatível com o tier. Nenhuma decisão de expandir portfólio é tomada sem custo por resultado medido contra baseline.

### Fonte: `docs/operations/kpi-kri-dashboard.md`

Commit de origem: `5545d9227624400ab8bb707b6032b2f61329a36e`.

<!-- source-unit {"classification": "metadata-title", "end_line": "2", "index": 14, "source_field": "title", "source_heading": "", "source_path": "docs/operations/kpi-kri-dashboard.md", "start_line": "2", "transformation": "integrate-complete-metric-governance", "unit_type": "frontmatter-title"} -->
**Título controlado na origem:** KPIs, KRIs e governance dashboard

<!-- source-unit {"classification": "metric", "end_line": "16", "index": 15, "source_field": "", "source_heading": "KPIs, KRIs e governance dashboard", "source_path": "docs/operations/kpi-kri-dashboard.md", "start_line": "15", "transformation": "integrate-complete-metric-governance", "unit_type": "markdown-atx-heading"} -->
### KPIs, KRIs e governance dashboard

<!-- source-unit {"classification": "objective", "end_line": "22", "index": 16, "source_field": "", "source_heading": "Objetivo", "source_path": "docs/operations/kpi-kri-dashboard.md", "start_line": "17", "transformation": "integrate-complete-metric-governance", "unit_type": "markdown-atx-heading"} -->
#### Objetivo

Separar três coisas que dashboards costumam misturar — desempenho, exposição a risco e operação do processo — e garantir que **toda métrica apresentada a um fórum tenha owner, threshold contextualizado e ação esperada**.

Métrica sem ação associada é decoração. Dashboard que não muda uma decisão é observação.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "31", "index": 17, "source_field": "", "source_heading": "Três tipos, três usos", "source_path": "docs/operations/kpi-kri-dashboard.md", "start_line": "23", "transformation": "integrate-complete-metric-governance", "unit_type": "markdown-atx-heading"} -->
#### Três tipos, três usos

| Tipo | O que mede | Exemplo | Ação associada |
|---|---|---|---|
| **KPI** | desempenho ou resultado desejado | % de T2/T3 com identidade própria | priorizar remediação se abaixo da meta |
| **KRI** | exposição ou deterioração de risco | % de T3 com attestation vencida | suspender ou escalar conforme prazo |
| **operacional** | capacidade do processo | lead time da security review | ajustar intake, automação ou capacidade |
| **valor** | economia e resultado real | custo por caso bem-sucedido + cycle time | escalar, redesenhar ou aposentar |

<!-- source-unit {"classification": "reference", "end_line": "51", "index": 18, "source_field": "", "source_heading": "Indicadores de referência", "source_path": "docs/operations/kpi-kri-dashboard.md", "start_line": "32", "transformation": "integrate-complete-metric-governance", "unit_type": "markdown-atx-heading"} -->
#### Indicadores de referência

Os alvos abaixo são **pontos de partida para a conversa**, não SLA universal. A regra: metas de higiene e accountability podem ser absolutas; métricas de adoção, custo, falso positivo e lead time precisam partir do baseline e do perfil operacional.

| Tipo | Indicador | Referência inicial |
|---|---|---|
| KPI | cobertura do inventário | ≥95% na implantação; ≥98% em operação madura |
| KPI | agentes em produção com owner | 100%; ownerless em T2/T3 igual a zero |
| KPI | lead time de aprovação por tier | T1 fast path imediato; T1 revisado até 1 dia; T2 de 3 a 5 dias; T3 de 5 a 15 dias; T4 sem rota normal |
| KPI | cobertura de attestation | ≥98% vigente; T3 vencido igual a zero |
| KRI | agentes de alto risco sem owner | zero em T2/T3/T4, com remediação imediata |
| KRI | anomalias de uso de ferramenta privilegiada | 100% investigadas; severidade alta dentro do SLA de resposta |
| KRI | agentes fora do padrão de identidade aprovado | zero em T2/T3 em produção; tendência decrescente nos demais |
| KRI | agentes T2/T3 dormentes | abaixo de 5% sem justificativa; 100% com ação de revisão ou retirada |
| Valor | custo por resultado bem-sucedido | baseline mais meta de melhoria acordada por caso |
| Valor | melhoria do KPI de negócio | alvo específico do caso; **adoção não é proxy de resultado** |
| Adoção | usuários ativos diários, semanais e mensais | sem alvo universal; usar tendência e frequência esperada do caso |

Registre a justificativa de cada threshold e a data de revisão. Revise após o primeiro ciclo com dados reais.

<!-- source-unit {"classification": "metric", "end_line": "55", "index": 19, "source_field": "", "source_heading": "Como interpretar métricas de adoção", "source_path": "docs/operations/kpi-kri-dashboard.md", "start_line": "52", "transformation": "integrate-complete-metric-governance", "unit_type": "markdown-atx-heading"} -->
#### Como interpretar métricas de adoção

Usuários ativos medem frequência e retenção, **não valor**. Um agente pode ter uso mensal alto porque virou etapa obrigatória de um fluxo e ainda assim piorar o cycle time. Adoção só significa algo junto de qualidade e outcome.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "67", "index": 20, "source_field": "", "source_heading": "Dashboard executivo mínimo", "source_path": "docs/operations/kpi-kri-dashboard.md", "start_line": "56", "transformation": "integrate-complete-metric-governance", "unit_type": "markdown-atx-heading"} -->
#### Dashboard executivo mínimo

- **estate e crescimento:** conhecidos versus estimados, novos por semana, mix de tiers;
- **ownership e lifecycle:** sem owner, attestation vencida, dormentes, candidatos a retirada;
- **risco e segurança:** findings críticos, incidentes, quarentenas, exceções de alto impacto;
- **cobertura de controles:** identidade, dados certificados, registro de ferramentas, telemetria e conformidade com o [Minimum Production Bar](../../toolkit/controls/minimum-production-bar.md);
- **FinOps:** custo por agente, custo por resultado, variação de budget e principais anomalias;
- **valor:** adoção, KPI de outcome, valor observado e agentes sem valor demonstrado;
- **programa:** lead time por tier, retrabalho de review, cobertura de automação e progresso de maturidade.

Não coloque todo o detalhe em uma página. Mantenha navegação entre a visão de governança e a evidência operacional: a página executiva mostra postura; as páginas operacionais permitem drill-down até o trace e a ação de ferramenta.

<!-- source-unit {"classification": "definition", "end_line": "73", "index": 21, "source_field": "", "source_heading": "Como definir thresholds", "source_path": "docs/operations/kpi-kri-dashboard.md", "start_line": "68", "transformation": "integrate-complete-metric-governance", "unit_type": "markdown-atx-heading"} -->
#### Como definir thresholds

Não transforme toda métrica em verde e vermelho arbitrários. Use baseline, risk appetite, SLA e tendência.

Para agentes T3 sem owner, a tolerância pode ser zero. Para falso positivo de uma regra de comportamento nova, a meta é calibrada gradualmente. Em ambos os casos, registre a razão do threshold e quando ele será revisto.

<!-- source-unit {"classification": "evidence-artifact", "end_line": "80", "index": 22, "source_field": "", "source_heading": "Evidências", "source_path": "docs/operations/kpi-kri-dashboard.md", "start_line": "74", "transformation": "integrate-complete-metric-governance", "unit_type": "markdown-atx-heading"} -->
#### Evidências

- definição de cada métrica com fórmula, fonte e owner;
- thresholds com rationale e data de revisão;
- histórico de decisões tomadas a partir do dashboard;
- lacunas de dados declaradas, em vez de preenchidas por estimativa.

<!-- source-unit {"classification": "metric", "end_line": "87", "index": 23, "source_field": "", "source_heading": "Métricas do próprio dashboard", "source_path": "docs/operations/kpi-kri-dashboard.md", "start_line": "81", "transformation": "integrate-complete-metric-governance", "unit_type": "markdown-atx-heading"} -->
#### Métricas do próprio dashboard

- métricas exibidas sem owner ou sem ação definida;
- indicadores que nunca mudaram uma decisão;
- lacunas de cobertura de dados por perspectiva;
- tempo entre sinal e decisão registrada.

<!-- source-unit {"classification": "risk-failure-mode", "end_line": "97", "index": 24, "source_field": "", "source_heading": "Failure modes", "source_path": "docs/operations/kpi-kri-dashboard.md", "start_line": "88", "transformation": "integrate-complete-metric-governance", "unit_type": "markdown-atx-heading"} -->
#### Failure modes

- misturar KPI, KRI e métrica operacional na mesma leitura;
- média agregada que esconde uma dimensão crítica;
- alvo copiado de outro contexto sem baseline próprio;
- adoção apresentada como prova de valor;
- dashboard completo e ilegível em uma única página;
- precisão numérica sobre dados de baixa cobertura;
- verde e vermelho sem rationale registrado.

<!-- source-unit {"classification": "requirement-control", "end_line": "100", "index": 25, "source_field": "", "source_heading": "Decision gate", "source_path": "docs/operations/kpi-kri-dashboard.md", "start_line": "98", "transformation": "integrate-complete-metric-governance", "unit_type": "markdown-atx-heading"} -->
#### Decision gate

Nenhuma métrica entra em um fórum de governança sem owner, threshold com rationale e ação esperada. Nenhum indicador de higiene crítica — ownership, attestation, identidade — é reportado sem cobertura declarada.

## Acceptance criteria

- todas as decisões deste capítulo possuem authority, owner e evidência recuperável;
- requisitos aplicáveis estão ligados ao catálogo de controles e ao método de verificação;
- exceções têm escopo, justificativa, compensating controls, expiry e decisão residual;
- controles de build time e runtime são distinguidos e exercitados quando aplicáveis;
- mudanças materiais reabrem avaliação, aprovação e evidência;
- nenhuma alegação de conformidade, eficácia ou valor excede a evidência observada.

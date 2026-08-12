---
title: 03 — Inventário, portfólio e valor
status: maintained
maturity: validated
last_reviewed: 2026-08-11
review_cycle: quarterly
owners: [framework-maintainers]
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# 03 — Inventário, portfólio e valor

Este capítulo integra a estrutura clean-room aprovada com o conteúdo substantivo do corpus autoritativo. Requisitos do framework são vendor-neutral; legislação externa, guidance, casos e histórico são identificados como tais. A implementação organizacional exige adoção formal pela authority competente e não decorre do versionamento deste repositório.

## Contrato operacional do capítulo

As subseções seguintes formam um contrato executável de completude. Cada uma especifica a decisão ou ação requerida, o record/evidence mínimo e uma condição observável de conclusão para levar a governança do zero ao business as usual.

### 03.1 Discovery of existing AI and agents

**Required decision/action.** For **discovery of existing ai and agents**, the organization must discover deployed, experimental, embedded and supplier-operated assets through multiple reconciled sources.

**Record and evidence.** Retain discovery source, last seen, confidence, owner match, unresolved identity and remediation status.

**Done when.** Unowned or shadow assets enter containment and ownership resolution instead of being silently accepted into inventory.

### 03.2 Shadow AI and unowned assets

**Required decision/action.** For **shadow ai and unowned assets**, the organization must discover deployed, experimental, embedded and supplier-operated assets through multiple reconciled sources.

**Record and evidence.** Retain discovery source, last seen, confidence, owner match, unresolved identity and remediation status.

**Done when.** Unowned or shadow assets enter containment and ownership resolution instead of being silently accepted into inventory.

### 03.3 AI-system and agent registry

**Required decision/action.** For **ai-system and agent registry**, the organization must operate the registry as the authoritative identity and lifecycle index for every in-scope agent.

**Record and evidence.** Validate stable ID, owner, purpose, tier, admissibility, version, environment, state, dependencies and last-attested date.

**Done when.** Automated and manual reconciliation detects missing, stale, duplicate and invalid records and blocks required transitions.

### 03.4 Mandatory inventory fields

**Required decision/action.** For **mandatory inventory fields**, the organization must operate the registry as the authoritative identity and lifecycle index for every in-scope agent.

**Record and evidence.** Validate stable ID, owner, purpose, tier, admissibility, version, environment, state, dependencies and last-attested date.

**Done when.** Automated and manual reconciliation detects missing, stale, duplicate and invalid records and blocks required transitions.

### 03.5 Ownership and accountability records

**Required decision/action.** For **ownership and accountability records**, the organization must bind each asset to active business, technical and operational owners with a succession rule.

**Record and evidence.** Record role identifiers, acceptance date, delegates, organizational unit, status and orphan-detection evidence.

**Done when.** Owner departure or inactivity triggers reassignment, suspension or retirement before the record becomes orphaned.

### 03.6 Purpose, intended users and affected stakeholders

**Required decision/action.** For **purpose, intended users and affected stakeholders**, the organization must document intended purpose, users, affected non-users, excluded uses and foreseeable scale.

**Record and evidence.** Retain use-case statement, stakeholder analysis, affected groups, environment, volume and material assumptions.

**Done when.** Evaluation and monitoring cover the actual affected population rather than only the requesting team.

### 03.7 Models, data, tools, integrations and third parties

**Required decision/action.** For **models, data, tools, integrations and third parties**, the organization must enumerate every governed dependency and the authority inherited by each connection.

**Record and evidence.** The blueprint must reference approved model, data source, tool, integration and supplier records with versions and restrictions.

**Done when.** An unregistered or incompatible dependency prevents promotion and material dependency change triggers reassessment.

### 03.8 Environments, versions and lifecycle state

**Required decision/action.** For **environments, versions and lifecycle state**, the organization must maintain a consistent identity across environments while separating configuration, authority and lifecycle state.

**Record and evidence.** Record environment, release, artifact hashes, deployed configuration, state, promotion source and rollback target.

**Done when.** Operators can reconcile desired and observed state and cannot mistake test approval for production authorization.

### 03.9 Intake of new demand

**Required decision/action.** For **intake of new demand**, the organization must capture the problem, proposed mechanism, owner and decision need before design work begins.

**Record and evidence.** The intake record must include purpose, baseline, users, affected persons, data, actions, alternatives and urgency.

**Done when.** The request is routed to appropriateness, risk and portfolio decisions without bypassing ownership or scope checks.

### 03.10 Appropriateness: whether an agent is the right mechanism

**Required decision/action.** For **appropriateness: whether an agent is the right mechanism**, the organization must compare an agent with deterministic automation, workflow, search, analytics and non-technical alternatives.

**Record and evidence.** Record alternatives, need for autonomy, uncertainty, expected benefit, failure cost and architectural decision.

**Done when.** An agent proceeds only when its distinctive capability is necessary and the additional governance burden is accepted.

### 03.11 Business case and measurable hypothesis

**Required decision/action.** For **business case and measurable hypothesis**, the organization must define a falsifiable outcome, pre-change baseline and credible counterfactual with an evidence cutoff.

**Record and evidence.** Record metric owner, population, formula, target, source, confounders, cost and decision threshold.

**Done when.** The authority can distinguish creation, adoption, quality and outcome and can stop work when evidence does not support expansion.

### 03.12 Baseline and counterfactual

**Required decision/action.** For **baseline and counterfactual**, the organization must define a falsifiable outcome, pre-change baseline and credible counterfactual with an evidence cutoff.

**Record and evidence.** Record metric owner, population, formula, target, source, confounders, cost and decision threshold.

**Done when.** The authority can distinguish creation, adoption, quality and outcome and can stop work when evidence does not support expansion.

### 03.13 Portfolio prioritization

**Required decision/action.** For **portfolio prioritization**, the organization must prioritize the portfolio using value evidence, risk, dependency, reuse and capacity rather than sponsor preference alone.

**Record and evidence.** Record comparable scores, duplicate capabilities, shared services, constraints, decision and review date.

**Done when.** The portfolio authority can fund, pause, merge, restrict or retire items and the decision propagates to lifecycle records.

### 03.14 Duplication, reuse and shared capabilities

**Required decision/action.** For **duplication, reuse and shared capabilities**, the organization must prioritize the portfolio using value evidence, risk, dependency, reuse and capacity rather than sponsor preference alone.

**Record and evidence.** Record comparable scores, duplicate capabilities, shared services, constraints, decision and review date.

**Done when.** The portfolio authority can fund, pause, merge, restrict or retire items and the decision propagates to lifecycle records.

### 03.15 Cost, consumption and FinOps

**Required decision/action.** For **cost, consumption and finops**, the organization must attribute consumption and total operating cost to agent, owner, environment and measurable outcome.

**Record and evidence.** Record unit cost, budget, quota, forecast, variance, shared-cost allocation, anomaly and optimization decision.

**Done when.** Threshold breach triggers throttling or review and cost claims remain separate from value realization claims.

### 03.16 Adoption and utilization

**Required decision/action.** For **adoption and utilization**, the organization must measure intended adoption, meaningful use and unsafe workaround behavior by target population.

**Record and evidence.** Record eligible population, active use, task completion, abandonment, support demand, feedback and sampling limitations.

**Done when.** The owner can distinguish availability from useful adoption and can change training, design or rollout based on evidence.

### 03.17 Outcome and value measurement

**Required decision/action.** For **outcome and value measurement**, the organization must define a falsifiable outcome, pre-change baseline and credible counterfactual with an evidence cutoff.

**Record and evidence.** Record metric owner, population, formula, target, source, confounders, cost and decision threshold.

**Done when.** The authority can distinguish creation, adoption, quality and outcome and can stop work when evidence does not support expansion.

### 03.18 Procurement and supplier intake

**Required decision/action.** For **procurement and supplier intake**, the organization must apply equivalent governance to built, bought, configured, SaaS, low-code and supplier-operated agents.

**Record and evidence.** Record supplier, service boundary, contractual duties, evidence supplied, sub-processors, exit rights, owner and unresolved gaps.

**Done when.** Outsourcing does not remove accountability and an unevidenced supplier claim cannot satisfy a blocking control.

### 03.19 Third-party documentation obligations

**Required decision/action.** For **third-party documentation obligations**, the organization must make this inventory or portfolio capability authoritative for all in-scope agents.

**Record and evidence.** The registry or portfolio record must capture owner, purpose, users, dependencies, lifecycle state, value hypothesis, evidence date and data-quality status.

**Done when.** Reconciliation detects unowned or missing assets and the portfolio authority can decide whether to fund, reuse, constrain, consolidate or retire them.

### 03.20 Portfolio review

**Required decision/action.** For **portfolio review**, the organization must prioritize the portfolio using value evidence, risk, dependency, reuse and capacity rather than sponsor preference alone.

**Record and evidence.** Record comparable scores, duplicate capabilities, shared services, constraints, decision and review date.

**Done when.** The portfolio authority can fund, pause, merge, restrict or retire items and the decision propagates to lifecycle records.

### 03.21 Maintain, expand, consolidate or retire decision

**Required decision/action.** For **maintain, expand, consolidate or retire decision**, the organization must prioritize the portfolio using value evidence, risk, dependency, reuse and capacity rather than sponsor preference alone.

**Record and evidence.** Record comparable scores, duplicate capabilities, shared services, constraints, decision and review date.

**Done when.** The portfolio authority can fund, pause, merge, restrict or retire items and the decision propagates to lifecycle records.


## Conteúdo canônico incorporado

A seção preserva integralmente as unidades atribuídas pela matriz de cobertura. Os marcadores HTML são provenance machine-readable e não alteram o significado normativo.

### Fonte: `docs/architecture/agent-or-not.md`

Commit de origem: `5545d9227624400ab8bb707b6032b2f61329a36e`.

<!-- source-unit {"classification": "metadata-title", "end_line": "2", "index": 1, "source_field": "title", "source_heading": "", "source_path": "docs/architecture/agent-or-not.md", "start_line": "2", "transformation": "integrate-complete-agent-or-not-gate", "unit_type": "frontmatter-title"} -->
**Título controlado na origem:** Decisão arquitetural — agente é o mecanismo certo?

<!-- source-unit {"classification": "decision-authority", "end_line": "16", "index": 2, "source_field": "", "source_heading": "Decisão arquitetural — agente é o mecanismo certo?", "source_path": "docs/architecture/agent-or-not.md", "start_line": "15", "transformation": "integrate-complete-agent-or-not-gate", "unit_type": "markdown-atx-heading"} -->
### Decisão arquitetural — agente é o mecanismo certo?

<!-- source-unit {"classification": "objective", "end_line": "24", "index": 3, "source_field": "", "source_heading": "Objetivo", "source_path": "docs/architecture/agent-or-not.md", "start_line": "17", "transformation": "integrate-complete-agent-or-not-gate", "unit_type": "markdown-atx-heading"} -->
#### Objetivo

O primeiro gate não é "qual plataforma usar". É **"precisamos mesmo de um agente?"**.

Comportamento agentic aumenta variabilidade, custo de observabilidade e superfície de risco. Deve existir uma razão explícita para introduzir autonomia ou raciocínio probabilístico — e essa razão precisa estar registrada, não pressuposta.

Processos determinísticos, estáveis e integralmente especificáveis costumam ser melhor atendidos por workflow, automação tradicional ou uma chamada de API.

<!-- source-unit {"classification": "decision-authority", "end_line": "52", "index": 4, "source_field": "", "source_heading": "Árvore de decisão", "source_path": "docs/architecture/agent-or-not.md", "start_line": "25", "transformation": "integrate-complete-agent-or-not-gate", "unit_type": "markdown-atx-heading"} -->
#### Árvore de decisão

Percorra na ordem. Cada resposta muda o que precisa ser desenhado, não apenas o que precisa ser aprovado.

**1. O problema exige interpretação de linguagem, contexto variável, planejamento ou seleção dinâmica de ferramentas?**
Se não — prefira solução determinística e **registre a alternativa escolhida**. Essa é uma decisão arquitetural legítima, não uma desistência.

**2. A saída é apenas conteúdo ou pode gerar ação?**
Ação introduz exigências de autorização, rollback, trilha de auditoria e lifecycle que conteúdo não tem.

**3. A ação é reversível?**
Irreversível ou material eleva o controle: avalie aprovação humana, step-up e circuit breaker antes de decidir a plataforma.

**4. O agente acessará dados classificados?**
Confirme que a fonte está certificada ou registre a remediação **antes** do go-live, conforme o [gate de dados](06-architecture-and-technical-controls.md).

**5. Opera com usuário presente ou de forma autônoma?**
Isso decide identidade delegada versus [identidade própria](06-architecture-and-technical-controls.md) — e não pode ser decidido depois.

**6. Há ferramentas, APIs ou servidores MCP?**
Classifique **cada ação**. O tier do agente não substitui a classificação da ferramenta.

**7. O uso afeta pessoas, direitos, oportunidades, segurança física, processo regulado ou comunicação pública?**
Aciona o impact trigger screen e, quando aplicável, o [impact assessment](04-risk-impact-and-compliance.md#impact-assessment).

**8. Onde cada controle vai residir?**
Management plane, gateway de runtime, broker de ferramentas, IAM, plataforma de dados, aplicação ou processo humano. **Não concentre controle no prompt** — prompt é instrução, não enforcement.

<!-- source-unit {"classification": "decision-authority", "end_line": "63", "index": 5, "source_field": "", "source_heading": "Exemplos de decisão", "source_path": "docs/architecture/agent-or-not.md", "start_line": "53", "transformation": "integrate-complete-agent-or-not-gate", "unit_type": "markdown-atx-heading"} -->
#### Exemplos de decisão

| Caso | Decisão arquitetural | Por quê |
|---|---|---|
| assistente de conhecimento | recuperação somente leitura, identidade delegada, fontes certificadas, sem ferramenta de escrita | o valor vem de interpretação e recuperação; ação transacional seria risco sem benefício |
| agente de service desk | identidade própria, catálogo de ferramentas para criar e atualizar chamados, rollback e telemetria | há escrita reversível e operação multiusuário; a atribuição precisa sobreviver à ausência do usuário |
| agente de contas a pagar | identidade própria, broker de ferramentas, serviço de aprovação para pagamento, segregação de funções | o escalador financeiro impede execução autônoma irrestrita |
| agente de operações de produção | control plane de runtime, mediação de ferramenta privilegiada, remediações pré-aprovadas, circuit breaker | **a ferramenta é mais crítica que o modelo**; o comando precisa ser autorizado fora do modelo |

O último caso é o mais instrutivo: quando a ferramenta é privilegiada, a discussão sobre qual modelo usar é secundária. O controle está na autorização da ação, não na qualidade do raciocínio.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "69", "index": 6, "source_field": "", "source_heading": "Onde registrar", "source_path": "docs/architecture/agent-or-not.md", "start_line": "64", "transformation": "integrate-complete-agent-or-not-gate", "unit_type": "markdown-atx-heading"} -->
#### Onde registrar

A decisão vai no [intake do caso de uso](../../toolkit/templates/use-case-intake.md) e, quando arquiteturalmente relevante, num [ADR](../../toolkit/templates/adr-template.md).

Se a resposta for "não precisamos de agente", **registre assim mesmo**. Decisão de não construir é a mais barata do portfólio e a que menos costuma ser documentada — o que faz a mesma discussão voltar seis meses depois.

<!-- source-unit {"classification": "definition", "end_line": "76", "index": 7, "source_field": "", "source_heading": "Definition of done", "source_path": "docs/architecture/agent-or-not.md", "start_line": "70", "transformation": "integrate-complete-agent-or-not-gate", "unit_type": "markdown-atx-heading"} -->
#### Definition of done

- a opção agentic foi comparada com alternativas determinísticas, e a comparação está registrada;
- modo de identidade, fontes de dados, ferramentas, nível de autonomia, oversight humano e controles de runtime estão explícitos;
- está declarado **onde cada policy será aplicada e onde a evidência será coletada**;
- as mudanças materiais que exigem reavaliação foram definidas **antes** do desenvolvimento começar.

<!-- source-unit {"classification": "risk-failure-mode", "end_line": "84", "index": 8, "source_field": "", "source_heading": "Failure modes", "source_path": "docs/architecture/agent-or-not.md", "start_line": "77", "transformation": "integrate-complete-agent-or-not-gate", "unit_type": "markdown-atx-heading"} -->
#### Failure modes

- começar pela plataforma e derivar o desenho dela;
- tratar "é IA" como justificativa em vez de decisão;
- classificar o agente e esquecer de classificar cada ferramenta;
- deixar o controle no prompt porque é o lugar mais fácil de escrever;
- decidir identidade depois do build, quando trocar custa reescrita;
- não registrar a decisão de **não** usar agente.

### Fonte: `docs/governance/ai-agent-policy-and-governance-v1.md`

Commit de origem: `5545d9227624400ab8bb707b6032b2f61329a36e`.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "142", "index": 9, "source_field": "", "source_heading": "10. Consumption and Costs (Cap/Alerts)", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "139", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
#### 10. Consumption and Costs (Cap/Alerts)
Each agent in production (≥10 users) must have a budget (cap) defined by the business owner, with alerts and re-approval when thresholds are exceeded.
Monitor consumption (e.g., tokens, calls, GPU minutes) and monthly cost; block in case of abuse/anomaly.

<!-- source-unit {"classification": "metric", "end_line": "146", "index": 10, "source_field": "", "source_heading": "11. Agent Catalog/Registry and KPIs", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "143", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
#### 11. Agent Catalog/Registry and KPIs
Without visibility, there is no governance. This section defines the Corporate Catalog as the “single source of truth” for agents in use in the company, ensuring traceability of owners, purpose, data, permissions, integrations, autonomy level, costs/consumption, and lifecycle status. Beyond the registry, this section establishes the minimum KPIs to monitor adoption, risk, and efficiency (e.g., catalog coverage, agents without an owner, HITL compliance, incidents, spend, usage by domain). The Catalog also enables auditing, duplication control, and execution of the sunset plan.
Model changes require catalog update and new validation before use in production.

<!-- source-unit {"classification": "requirement-control", "end_line": "149", "index": 11, "source_field": "", "source_heading": "11.1 Minimum fields of the catalog/record", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "147", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
##### 11.1 Minimum fields of the catalog/record
ID, Name, Business Owner, Technical Owner, Objective/Use Cases, Data and Owners, Permissions/Systems, Defined HITL, Number of Users, Environment, Risk, AI Model Version, Date of Last Model Validation, Source and Type of Data Used, DPIA (yes/no), Cap/alerts, Next Review, Status (pilot/prod/sunset).

<!-- source-unit {"classification": "concept-or-structure", "end_line": "161", "index": 12, "source_field": "", "source_heading": "11.3 Compliance and Enforcement (Catalog, Owners, Logs)", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "153", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
##### 11.3 Compliance and Enforcement (Catalog, Owners, Logs)
Minimum conditions for Production: agent registered in the Catalog, Owners defined, logs/audit enabled, HITL configured according to the autonomy level, cap/alerts configured, and approvals evidenced.
Non-conformity in Production:
Quarantine: Run Authority can immediately suspend the agent (kill-switch) when there is high risk, data leakage, policy violation, or consumption anomaly.
Regularization: for non-critical cases, the agent enters operational quarantine within up to 5 business days and must be regularized (catalog/owners/logs/cap) within up to 30 calendar days.
Deactivation: if not regularized within the deadline, the agent is deactivated and reported to the Business Owner, Technical Owner, and Design Authority.
Non-compliance in Test/PoC: allowed only in non-production environments and for a limited time (e.g., 30 days). After this period, it requires minimum regularization (Self-Assessment + Owners + registration) or deactivation.
Audit: periodic reviews (e.g., monthly for production) to identify agents without registration/owners, logging gaps, excessive consumption, and scope deviations.

### Fonte: `docs/registry/README.md`

Commit de origem: `5545d9227624400ab8bb707b6032b2f61329a36e`.

<!-- source-unit {"classification": "metadata-title", "end_line": "2", "index": 13, "source_field": "title", "source_heading": "", "source_path": "docs/registry/README.md", "start_line": "2", "transformation": "merge-by-topic-into-chapter-03-preserve-registry-taxonomy-ownership-and-blueprint-boundaries", "unit_type": "frontmatter-title"} -->
**Título controlado na origem:** Estate, registry, ownership e taxonomia

<!-- source-unit {"classification": "definition", "end_line": "17", "index": 14, "source_field": "", "source_heading": "Estate, registry, ownership e taxonomia", "source_path": "docs/registry/README.md", "start_line": "16", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
### Estate, registry, ownership e taxonomia

<!-- source-unit {"classification": "objective", "end_line": "23", "index": 15, "source_field": "", "source_heading": "Objetivo", "source_path": "docs/registry/README.md", "start_line": "18", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
#### Objetivo

Criar a fonte corporativa de verdade sobre quais agentes existem, quem responde por cada um e o que cada um pode fazer — em linguagem comum, estável e independente da plataforma onde o agente foi construído.

Sem essa camada, todas as outras falham por falta de sujeito: não há como aplicar tier, evidência, contenção ou sunset a um ativo que a organização não sabe que existe.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "34", "index": 16, "source_field": "", "source_heading": "Quatro objetos distintos", "source_path": "docs/registry/README.md", "start_line": "24", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
#### Quatro objetos distintos

| Objeto | Pergunta que responde | Natureza |
|---|---|---|
| **Registry** | qual agente é este, quem responde, qual tier, admissibilidade, stage e operational state? | fonte corporativa de identificação e correlação |
| **Blueprint** | como esta versão deve ser configurada e controlada? | especificação versionada do desired state |
| **Policy/gate** | a configuração e as evidências atendem às regras? | decisão automática ou semiautomática |
| **Runtime/telemetria** | o agente está operando conforme aprovado? | estado observado |

Confundir registry com blueprint produz o antipattern mais comum: um inventário que cresce sem nunca virar controle.

<!-- source-unit {"classification": "definition", "end_line": "56", "index": 17, "source_field": "", "source_heading": "Taxonomia corporativa", "source_path": "docs/registry/README.md", "start_line": "35", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
#### Taxonomia corporativa

Taxonomia é a linguagem de classificação do estate: características relativamente estáveis que fazem registry, scoring, policies, dashboards e lifecycle usarem os mesmos termos.

**Taxonomia não é risk tier.** Dois agentes podem ser `transactional` e receber tiers diferentes por operarem sobre dados, privilégios ou processos distintos.

| Dimensão | Categorias sugeridas | Por que muda a governança |
|---|---|---|
| origem | citizen, partnered, professional, fornecedor/SaaS | define suporte, SDLC e responsabilidade técnica |
| ownership | pessoal, time, processo de negócio, corporativo | muda attestation, JML, continuidade e retirada |
| alcance | usuário único, time, unidade, corporativo, externo/público | muda blast radius e necessidade de assurance |
| função | informacional, redação, transacional, autônomo | separa conteúdo de efeito colateral |
| autonomia | assistiva, sugestão, execução limitada, planejamento autônomo | direciona oversight, limites e controles de runtime |
| identidade | delegada, própria (NHI), compartilhada (proibida) | define accountability e padrão de autorização |
| dados | público, interno, confidencial, restrito/regulado | aciona controles de dados, privacidade e residency |
| tools | nenhuma, leitura, escrita, execução, privilegiada | direciona mediação, rollback e aprovação humana |
| runtime | SaaS, nuvem, on-premises, edge, híbrido | muda pontos de enforcement e ownership operacional |
| topologia | agente único, multiagente, delegação entre agentes | adiciona trust chain e requisitos de correlação |
| lifecycle | efêmero, do usuário, do time, corporativo | muda retenção, dormancy e sucessão |

Evite taxonomia baseada em produto ("agente da plataforma X"). O produto informa onde o agente foi construído, não o que ele pode fazer — e a taxonomia precisa sobreviver à troca de builder.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "66", "index": 18, "source_field": "", "source_heading": "Como implementar", "source_path": "docs/registry/README.md", "start_line": "57", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
##### Como implementar

1. Colete amostra representativa incluindo citizen-built, SaaS, custom e ao menos um caso com execução de ferramentas.
2. Escolha **apenas** dimensões que alteram decisão, controle, métrica ou lifecycle. Categoria que não muda nada não deve ser obrigatória.
3. Defina códigos canônicos e descrições inequívocas — "autônomo" precisa de critério operacional, não percepção do builder.
4. Crie regras de normalização por plataforma, mapeando termos nativos para as categorias corporativas.
5. Defina o que é obrigatório por tier e o que pode ser autodescoberto. O fast path de T1 deve minimizar input manual.
6. Classifique 20–30 casos e meça concordância entre avaliadores. Divergência sistemática indica definição fraca, não avaliador fraco.
7. Implemente a taxonomia no registry, no pre-screen, nos dashboards e no blueprint. Taxonomia que vive só em documento não gera governança.

<!-- source-unit {"classification": "architecture-runtime", "end_line": "80", "index": 19, "source_field": "", "source_heading": "Registry: capacidades mínimas", "source_path": "docs/registry/README.md", "start_line": "67", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
#### Registry: capacidades mínimas

O registry não precisa armazenar tudo — pode referenciar sources of truth existentes. O requisito é responder de forma consistente: **qual agente é este, quem responde, qual tier e admissibilidade, qual lifecycle stage e operational state, quais identidades, tools, dados e modelos usa, e quando foi visto pela última vez.**

| Grupo | Campos | Source of truth preferido |
|---|---|---|
| identidade do ativo | `agent_id` imutável, nome, versão, plataforma, ambiente | registry/plataforma |
| ownership | business owner, technical owner, delegado, time/centro de custo | diretório organizacional + registry |
| governança | tier, admissibilidade, score, escaladores, decision/exception refs | sistema de risco |
| dependências | IDs de fontes de dados, tools, servidores MCP, modelos | catálogos + blueprint |
| runtime | ID de identidade, endpoint, perfil de telemetria, `last_seen`, budget | IAM/plataforma/observabilidade |
| lifecycle | stage, operational state, transition history, próxima attestation, dormancy, retirada | serviço de lifecycle |
| valor | ID do caso de uso, KPI, status no portfólio, valor observado | portfólio |

<!-- source-unit {"classification": "concept-or-structure", "end_line": "93", "index": 20, "source_field": "", "source_heading": "Obrigatoriedade por tier", "source_path": "docs/registry/README.md", "start_line": "81", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
##### Obrigatoriedade por tier

| Campo | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| owner | obrigatório | dual (business + technical) | dual + delegado | sponsor executivo + owners accountable |
| tier e admissibilidade | ambos obrigatórios | ambos obrigatórios | ambos + reassessment | ambos + authority compatível; exceção somente se `restricted` |
| dados e tools | lista | lista + classificação | lista + constraints + evidência | constraints e lineage críticos completos |
| identidade | definida | identidade própria | identidade própria + policy reforçada | identidade dedicada, isolamento e dual control onde aplicável |
| observabilidade | padrão | completa | completa + baseline de comportamento | monitoramento e containment reforçados |
| attestation | periódica | periódica | frequente ou orientada a evento | orientada a evento e executive review |

O fast path de T1 existe para reduzir input manual em alto volume, **não** para dispensar registro: descoberta, owner, logging e fontes aprovadas continuam obrigatórios.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "106", "index": 21, "source_field": "", "source_heading": "Regras de qualidade que geram finding", "source_path": "docs/registry/README.md", "start_line": "94", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
#### Regras de qualidade que geram finding

O registry só é controle quando detecta continuamente que deixou de representar a realidade. O objetivo não é ter uma lista perfeita.

- owner inexistente ou inativo;
- tier ausente ou expirado após mudança material;
- `last_seen` incompatível com o estado de lifecycle;
- ferramenta ou fonte de dados referenciada que não existe no catálogo;
- agente em produção sem perfil de telemetria ou sem kill switch quando exigido;
- attestation vencida;
- identidade compartilhada entre múltiplos agentes T2/T3 sem exceção aprovada;
- agente descoberto sem owner — recebe status `unmanaged` e entra em remediação.

<!-- source-unit {"classification": "architecture-runtime", "end_line": "112", "index": 22, "source_field": "", "source_heading": "Blueprint machine-readable", "source_path": "docs/registry/README.md", "start_line": "107", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
#### Blueprint machine-readable

O blueprint é o contrato entre design, desenvolvimento, governança, CI/CD e runtime. Machine-readable significa que os campos relevantes podem ser interpretados por automação para gerar policy checks, verificar o baseline do tier e comparar drift entre configuração aprovada e runtime.

Isso não exige que toda a governança esteja em YAML: decisões narrativas, impact assessments e risk acceptance continuam como evidências **referenciadas** pelo blueprint. Os contratos canônicos são o [Agent Registry 2.0](../../toolkit/schemas/agent-registry.schema.json) e o [Agent Blueprint 2.0](../../toolkit/schemas/agent-blueprint.schema.json).

<!-- source-unit {"classification": "concept-or-structure", "end_line": "122", "index": 23, "source_field": "", "source_heading": "Como implementar", "source_path": "docs/registry/README.md", "start_line": "113", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
##### Como implementar

1. Defina primeiro o contrato lógico e apenas os campos que têm consumidor real. Schema grande sem consumidor é dívida.
2. Use formato versionável com validação por schema; campos críticos com enum, formato e obrigatoriedade por tier.
3. Associe o blueprint a `agent_id` + versão. Alterar o blueprint não pode sobrescrever silenciosamente a evidência de releases anteriores.
4. Valide em build/release: IDs de fontes, tools e modelos precisam existir em catálogos aprovados; tier e padrão de identidade precisam ser coerentes.
5. Use o blueprint para gerar ou verificar configuração: policy bindings, budgets, perfil de telemetria, allowlist de tools e cadência de attestation.
6. Compare desired state com runtime observado. Drift material produz finding e, se altera risco, reassessment.
7. Comece com dois ou três patterns (T1 somente leitura, T2 transacional, T3 alto impacto) e evolua o schema só quando houver caso real.

<!-- source-unit {"classification": "evidence-artifact", "end_line": "131", "index": 24, "source_field": "", "source_heading": "Artefatos", "source_path": "docs/registry/README.md", "start_line": "123", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
#### Artefatos

- Agent Registry Data Standard: campos, tipos, obrigatoriedade por tier, sources of truth e quality checks;
- [Agent Registry schema](../../toolkit/schemas/agent-registry.schema.json) e [exemplo estruturado](../../toolkit/examples/agent-registry.example.json);
- [Agent Blueprint schema](../../toolkit/schemas/agent-blueprint.schema.json) e [exemplo estruturado](../../toolkit/examples/agent-blueprint.example.json);
- Agent Taxonomy & Metadata Dictionary;
- [template de registry](../../toolkit/templates/agent-registry-template.md) e [template de blueprint](../../toolkit/templates/agent-blueprint-template.md);
- [descoberta contínua e forecast do estate](03-inventory-portfolio-and-value.md).

<!-- source-unit {"classification": "evidence-artifact", "end_line": "140", "index": 25, "source_field": "", "source_heading": "Evidências", "source_path": "docs/registry/README.md", "start_line": "132", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
#### Evidências

- registro autoritativo com owners, tier e estado por agente;
- histórico de reconciliação entre registry e plataformas de origem;
- findings de qualidade abertos e remediados;
- blueprint versionado por release, com evidence refs;
- relatórios de drift entre desired state e runtime;
- decisões de exceção para identidade compartilhada.

<!-- source-unit {"classification": "metric", "end_line": "150", "index": 26, "source_field": "", "source_heading": "Métricas", "source_path": "docs/registry/README.md", "start_line": "141", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
#### Métricas

- agentes descobertos sem owner (`unmanaged`) e tempo até remediação;
- cobertura do registry contra fontes de descoberta independentes;
- campos obrigatórios vazios por tier;
- referências quebradas para tools, dados e modelos;
- drift material entre blueprint e runtime;
- duplicidade e sobreposição de capability no estate;
- tempo entre criação do agente e registro.

<!-- source-unit {"classification": "risk-failure-mode", "end_line": "160", "index": 27, "source_field": "", "source_heading": "Failure modes", "source_path": "docs/registry/README.md", "start_line": "151", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
#### Failure modes

- registry como planilha mestre que ninguém reconcilia;
- taxonomia derivada de produto em vez de comportamento;
- inventário completo sem quality rules — lista bonita, controle zero;
- blueprint gigante sem consumidor automatizado;
- agente pessoal compartilhado que permanece "pessoal" no registro;
- tratar descoberta como projeto de inventário pontual;
- sobrescrever o blueprint aprovado ao publicar uma nova versão.

<!-- source-unit {"classification": "requirement-control", "end_line": "163", "index": 28, "source_field": "", "source_heading": "Decision gate", "source_path": "docs/registry/README.md", "start_line": "161", "transformation": "merge-exact-heading-subtree-by-topic-preserving-all-fields-tables-links-and-caveats", "unit_type": "markdown-atx-heading"} -->
#### Decision gate

Nenhum agente é construído em ambiente compartilhado ou publicado sem `agent_id`, owner, tier e admissibilidade registrados. Nenhum agente permanece em produção sem stage/operational state coerentes ou com quality finding crítico aberto no registry.

### Fonte: `docs/registry/discovery-and-forecast.md`

Commit de origem: `5545d9227624400ab8bb707b6032b2f61329a36e`.

<!-- source-unit {"classification": "metadata-title", "end_line": "2", "index": 29, "source_field": "title", "source_heading": "", "source_path": "docs/registry/discovery-and-forecast.md", "start_line": "2", "transformation": "synthesize-and-preserve", "unit_type": "frontmatter-title"} -->
**Título controlado na origem:** Descoberta contínua do estate e forecast de crescimento

<!-- source-unit {"classification": "lifecycle-state", "end_line": "18", "index": 30, "source_field": "", "source_heading": "Descoberta contínua do estate e forecast de crescimento", "source_path": "docs/registry/discovery-and-forecast.md", "start_line": "17", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
### Descoberta contínua do estate e forecast de crescimento

<!-- source-unit {"classification": "objective", "end_line": "24", "index": 31, "source_field": "", "source_heading": "Objetivo", "source_path": "docs/registry/discovery-and-forecast.md", "start_line": "19", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Objetivo

Produzir um baseline confiável de quais agentes já existem, com grau de confiança declarado, e transformar descoberta em capacidade contínua — não em inventário de workshop.

Uma organização que "começa do zero" raramente começa com zero agentes. Ela começa com **baixa visibilidade**.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "28", "index": 32, "source_field": "", "source_heading": "Por que discovery é disciplina, não projeto", "source_path": "docs/registry/discovery-and-forecast.md", "start_line": "25", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Por que discovery é disciplina, não projeto

O agent estate muda mais rápido que um CMDB tradicional porque agentes nascem de usuários, SaaS, low-code, IDEs, automações e código. Um inventário pontual fica obsoleto em semanas. O baseline é o ponto de partida; a capacidade contínua é o produto.

<!-- source-unit {"classification": "reference", "end_line": "41", "index": 33, "source_field": "", "source_heading": "Fontes de descoberta", "source_path": "docs/registry/discovery-and-forecast.md", "start_line": "29", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Fontes de descoberta

| Fonte | O que procurar | Limitação típica | Como compensar |
|---|---|---|---|
| builders e low-code | agentes, apps, owners, status de publicação | não cobre agentes custom | correlacionar com repositórios e gateways |
| IAM e identidades não humanas | service principals, workload identities, secrets | a identidade pode não indicar que é agente | usar convenção de nomes, tags e telemetria de API |
| gateways de modelo e API | chamadas de modelo, chaves, metadados de ator | apenas o tráfego que passa pelo gateway | combinar com egress/proxy e dados de despesa |
| código-fonte e CI/CD | SDKs de agente, clientes de modelo, configurações MCP | protótipos locais podem não aparecer | survey com desenvolvedores e scanning de artefatos |
| inventário de SaaS e compras | produtos com recursos agentic | recurso licenciado pode não estar em uso | validar uso real e logs administrativos |
| rede e egress | destinos de APIs de modelo e endpoints MCP | baixa semântica | usar apenas como sinal de agente `suspected` |

Nenhuma fonte isolada é suficiente. A cobertura vem da correlação, e a correlação exige um schema mínimo comum.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "66", "index": 34, "source_field": "", "source_heading": "Status de confirmação e confidence", "source_path": "docs/registry/discovery-and-forecast.md", "start_line": "42", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Status de confirmação e confidence

Dois campos diferentes evitam inflar métricas e descartar sinais de shadow AI:

- `discovery.status` descreve o quanto a existência e o contexto do agente foram confirmados;
- `discovery.confidence` expressa a confiança na correlação dos sinais disponíveis.

Status não deve receber `low|medium|high`, e confidence não deve receber `confirmed|probable|suspected`.

| Status | Significado | Ação |
|---|---|---|
| `confirmed` | evidência direta do agente e do seu contexto | registrar e atribuir owner |
| `probable` | múltiplos sinais apontam para uso agentic, sem confirmação | investigar dentro do SLA definido |
| `suspected` | indício isolado que merece verificação | manter no backlog de remediação |

Objetos incertos **não são descartados**. Eles entram no backlog com owner e prazo.

| Confidence | Uso |
| --- | --- |
| `high` | sinais independentes coerentes e recentes |
| `medium` | evidência útil com gap conhecido de cobertura ou contexto |
| `low` | sinal fraco, antigo ou ainda não reconciliado |

O [Agent Registry 2.0](../../toolkit/schemas/agent-registry.schema.json) preserva `firstSeenAt`, `lastSeenAt` e `signals[]`, cada sinal com origem, tipo, timestamp e evidence reference.

<!-- source-unit {"classification": "procedure", "end_line": "78", "index": 35, "source_field": "", "source_heading": "Procedimento", "source_path": "docs/registry/discovery-and-forecast.md", "start_line": "67", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Procedimento

1. Definir o universo de descoberta: tenants, nuvens, repositórios, builders, SaaS, APIs de modelo, service accounts e integrações MCP conhecidas.
2. Coletar inventários e sinais das fontes acima.
3. Normalizar no schema mínimo: `agent_id`, nome, owner, plataforma, ambiente, lifecycle stage, operational state, fontes de dados, tools, modelo/provedor, audiência e o objeto `discovery`.
4. Deduplicar por identificadores e evidências, distinguindo **um agente** de **uma versão ou instância**.
5. Classificar confiança e registrar o que ficou incerto.
6. Entrevistar 5–10 áreas com maior probabilidade de adoção para revelar shadow agents e demanda futura.
7. Construir o forecast em três cenários.
8. Identificar e quantificar os gargalos manuais.
9. Fechar o baseline com **data de corte** e definir a cadência de redescoberta, preferencialmente automatizada.

<!-- source-unit {"classification": "lifecycle-state", "end_line": "91", "index": 36, "source_field": "", "source_heading": "Forecast do estate", "source_path": "docs/registry/discovery-and-forecast.md", "start_line": "79", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Forecast do estate

Forecast serve para **dimensionar governança**, não para prometer número exato.

1. Definir baseline por população: agentes pessoais, de time, de processo, embarcados e de terceiros.
2. Identificar drivers: usuários habilitados, builders disponíveis, templates, iniciativas estratégicas, novos SaaS e automações previstas.
3. Criar cenários conservador, provável e acelerado em 6 e 12 meses.
4. Projetar o **mix de risco**, não apenas o volume. Crescer de 1.000 para 5.000 agentes T1 não demanda o mesmo esforço que adicionar 100 agentes T3.
5. Converter o forecast em volumes operacionais: attestations por mês, reviews T2/T3, incidentes esperados, identidades, registros de tools e volume de telemetria.
6. Revisar trimestralmente com dados reais e ajustar capacidade de fóruns, automação e plataforma.

Exemplo de dimensionamento: se 5.000 usuários habilitados podem criar agentes e apenas 10% criarem 2 agentes cada, o estate potencial já ultrapassa 1.000 agentes — antes de qualquer iniciativa corporativa.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "103", "index": 37, "source_field": "", "source_heading": "Registro de gargalos manuais", "source_path": "docs/registry/discovery-and-forecast.md", "start_line": "92", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Registro de gargalos manuais

Backlog dos pontos onde a governança depende de trabalho humano repetitivo. É o insumo direto da decisão sobre o que virar policy-as-code.

| Atividade manual | Volume/mês | Lead time | Risco de automatizar | Decisão inicial |
|---|---|---|---|---|
| aprovar agente T1 somente leitura | 400 | 2 dias | baixo | automatizar com policy gate após calibração em cohort controlada ou evidência equivalente |
| criar identidade de agente T2 | 40 | 4 dias | médio | workflow + API de IAM, mantendo caminho de exceção |
| revisar ferramenta privilegiada T3 | 5 | 5 dias | alto | manter decisão humana; automatizar o preparo da evidência |

A leitura correta da tabela é: **automatizar a preparação da evidência é quase sempre seguro; automatizar a decisão só quando a policy está estável.**

<!-- source-unit {"classification": "evidence-artifact", "end_line": "110", "index": 38, "source_field": "", "source_heading": "Artefatos", "source_path": "docs/registry/discovery-and-forecast.md", "start_line": "104", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Artefatos

- Agent Estate Inventory com confiança e data de corte;
- [Agent Registry 2.0](../../toolkit/schemas/agent-registry.schema.json) e [exemplo preenchido](../../toolkit/examples/agent-registry.example.json);
- Agent Estate Forecast em três cenários, com mix de risco;
- Manual Bottleneck Register priorizado por volume, lead time e risco.

<!-- source-unit {"classification": "evidence-artifact", "end_line": "118", "index": 39, "source_field": "", "source_heading": "Evidências", "source_path": "docs/registry/discovery-and-forecast.md", "start_line": "111", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Evidências

- fontes consultadas, cobertura e limitações declaradas;
- baseline com data de corte e distribuição de confiança;
- backlog de remediação de objetos `probable` e `suspected`;
- forecast com premissas explícitas e revisão trimestral;
- medição de volume e lead time dos gargalos.

<!-- source-unit {"classification": "metric", "end_line": "127", "index": 40, "source_field": "", "source_heading": "Métricas", "source_path": "docs/registry/discovery-and-forecast.md", "start_line": "119", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Métricas

- cobertura do registry contra fontes independentes de descoberta;
- agentes descobertos por fonte e tempo até atribuição de owner;
- proporção `confirmed` / `probable` / `suspected` ao longo do tempo;
- shadow agents encontrados por ciclo de redescoberta;
- desvio entre forecast e estate real;
- gargalos manuais eliminados por trimestre.

<!-- source-unit {"classification": "risk-failure-mode", "end_line": "137", "index": 41, "source_field": "", "source_heading": "Failure modes", "source_path": "docs/registry/discovery-and-forecast.md", "start_line": "128", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Failure modes

- tratar o baseline como conclusão em vez de ponto de partida;
- descartar sinais incertos para não "poluir" a métrica;
- contar versões e instâncias como agentes distintos;
- forecast apresentado como previsão contratual;
- projetar volume sem projetar mix de risco;
- automatizar decisões antes de estabilizar a policy;
- baseline sem data de corte — impossível de auditar depois.

<!-- source-unit {"classification": "requirement-control", "end_line": "140", "index": 42, "source_field": "", "source_heading": "Decision gate", "source_path": "docs/registry/discovery-and-forecast.md", "start_line": "138", "transformation": "synthesize-and-preserve", "unit_type": "markdown-atx-heading"} -->
#### Decision gate

O baseline só é aceito com data de corte, cobertura mensurável por fonte, gaps registrados com owner e distribuições de status e confidence declaradas separadamente. Cobertura desconhecida é gap crítico, não ausência de risco.

### Fonte: `docs/value/README.md`

Commit de origem: `5545d9227624400ab8bb707b6032b2f61329a36e`.

<!-- source-unit {"classification": "metadata-title", "end_line": "2", "index": 43, "source_field": "title", "source_heading": "", "source_path": "docs/value/README.md", "start_line": "2", "transformation": "merge-as-canonical-portfolio-and-value-guidance-preserve-evidence-causality-and-sunset-rules", "unit_type": "frontmatter-title"} -->
**Título controlado na origem:** Estratégia, portfólio e evidência de valor

<!-- source-unit {"classification": "evidence-artifact", "end_line": "16", "index": 44, "source_field": "", "source_heading": "Estratégia, portfólio e evidência de valor", "source_path": "docs/value/README.md", "start_line": "15", "transformation": "preserve-exact-heading-subtree-and-merge-with-registry-boundary-explicit", "unit_type": "markdown-atx-heading"} -->
### Estratégia, portfólio e evidência de valor

<!-- source-unit {"classification": "objective", "end_line": "20", "index": 45, "source_field": "", "source_heading": "Objetivo", "source_path": "docs/value/README.md", "start_line": "17", "transformation": "preserve-exact-heading-subtree-and-merge-with-registry-boundary-explicit", "unit_type": "markdown-atx-heading"} -->
#### Objetivo

Conectar cada agente a um problema, owner, baseline e decisão de portfólio, sem inferir valor a partir de volume, uso ou narrativa de fornecedor.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "34", "index": 46, "source_field": "", "source_heading": "Cadeia de valor", "source_path": "docs/value/README.md", "start_line": "21", "transformation": "preserve-exact-heading-subtree-and-merge-with-registry-boundary-explicit", "unit_type": "markdown-atx-heading"} -->
#### Cadeia de valor

```text
Problema observado
  → hipótese de intervenção
  → capability do agente
  → mudança de comportamento/processo
  → output mensurável
  → outcome
  → impacto, custo e efeitos colaterais
```

Cada seta é uma hipótese que precisa de evidência. Um bom output pode não gerar outcome; um outcome pode ter outras causas.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "47", "index": 47, "source_field": "", "source_heading": "Business case mínimo", "source_path": "docs/value/README.md", "start_line": "35", "transformation": "preserve-exact-heading-subtree-and-merge-with-registry-boundary-explicit", "unit_type": "markdown-atx-heading"} -->
#### Business case mínimo

- problema e população afetada;
- processo atual e baseline;
- alternativa não-IA;
- intended/prohibited use;
- business e technical owner;
- benefits esperados e harms possíveis;
- custos build/run/change/support/assurance;
- métricas de adoção, qualidade e outcome;
- condições para manter, expandir, corrigir ou aposentar;
- horizonte de revisão.

<!-- source-unit {"classification": "metric", "end_line": "64", "index": 48, "source_field": "", "source_heading": "Métricas separadas", "source_path": "docs/value/README.md", "start_line": "48", "transformation": "preserve-exact-heading-subtree-and-merge-with-registry-boundary-explicit", "unit_type": "markdown-atx-heading"} -->
#### Métricas separadas

| Camada | Exemplos |
|---|---|
| criação | agentes, versões, tempo de build |
| descoberta | busca, visualização, seleção correta |
| adoção | usuários ativos, recorrência, workflow integration |
| uso | tarefas, sessões, tool calls, volume |
| qualidade | task success, erro, safety, groundedness |
| eficiência | tempo/custo por tarefa com qualidade preservada |
| outcome | backlog reduzido, cycle time, disponibilidade, erro operacional |
| impacto | financeiro, humano, regulatório, ambiental ou estratégico |

Não agregue essas camadas em uma única “AI adoption score” sem preservar significado.

A medição de custo por resultado que sustenta a camada de eficiência está em [FinOps e unit economics](10-metrics-review-and-improvement.md); a separação entre KPI, KRI e métrica operacional está em [KPIs, KRIs e governance dashboard](10-metrics-review-and-improvement.md).

<!-- source-unit {"classification": "concept-or-structure", "end_line": "73", "index": 49, "source_field": "", "source_heading": "Baseline e atribuição", "source_path": "docs/value/README.md", "start_line": "65", "transformation": "preserve-exact-heading-subtree-and-merge-with-registry-boundary-explicit", "unit_type": "markdown-atx-heading"} -->
#### Baseline e atribuição

- medir o processo antes ou reconstruir baseline com limitações declaradas;
- comparar grupos, períodos ou tarefas equivalentes quando possível;
- registrar outras mudanças que afetam o outcome;
- distinguir correlação de causalidade;
- incluir custo de revisão humana, suporte e incidentes;
- comunicar intervalo, incerteza e qualidade do dado.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "88", "index": 50, "source_field": "", "source_heading": "Portfolio governance", "source_path": "docs/value/README.md", "start_line": "74", "transformation": "preserve-exact-heading-subtree-and-merge-with-registry-boundary-explicit", "unit_type": "markdown-atx-heading"} -->
#### Portfolio governance

O artefato que carrega o portfólio é o [Agent Use-Case Portfolio](../../toolkit/templates/use-case-portfolio.md): use case, sponsor, owner, tier, admissibilidade, status, valor esperado, valor observado, custo e flag de duplicidade. Ele responde "isso deveria continuar existindo", enquanto o [registry](03-inventory-portfolio-and-value.md) responde "o que existe e quem responde por isso" — são artefatos distintos e não devem ser fundidos.

Decisões de portfólio consideram:

- alinhamento estratégico;
- valor esperado e evidence strength;
- risco e residual impact;
- duplicidade e reuse;
- dependências e concentração;
- custo total e capacidade operacional;
- timing e reversibilidade;
- opportunity cost.

<!-- source-unit {"classification": "concept-or-structure", "end_line": "99", "index": 51, "source_field": "", "source_heading": "Value review", "source_path": "docs/value/README.md", "start_line": "89", "transformation": "preserve-exact-heading-subtree-and-merge-with-registry-boundary-explicit", "unit_type": "markdown-atx-heading"} -->
#### Value review

| Decisão | Condição típica |
|---|---|
| manter | outcome e risco dentro do envelope |
| expandir | evidência suficiente, controls escaláveis e demanda legítima |
| corrigir | valor plausível, mas quality/control gap tratável |
| restringir | risco ou incerteza exige menor scope |
| substituir | alternativa entrega melhor relação valor-risco-custo |
| aposentar | sem owner, sem uso, sem outcome ou risco/custo injustificável |

<!-- source-unit {"classification": "evidence-artifact", "end_line": "110", "index": 52, "source_field": "", "source_heading": "Evidências", "source_path": "docs/value/README.md", "start_line": "100", "transformation": "preserve-exact-heading-subtree-and-merge-with-registry-boundary-explicit", "unit_type": "markdown-atx-heading"} -->
#### Evidências

- business case e baseline;
- metric definitions e data lineage;
- cost model;
- adoption/quality/outcome reports;
- incidents e externalities;
- portfolio decision e rationale;
- benefit hypothesis changes;
- sunset ou reinvestment decision.

<!-- source-unit {"classification": "metric", "end_line": "121", "index": 53, "source_field": "", "source_heading": "Métricas do portfólio", "source_path": "docs/value/README.md", "start_line": "111", "transformation": "preserve-exact-heading-subtree-and-merge-with-registry-boundary-explicit", "unit_type": "markdown-atx-heading"} -->
#### Métricas do portfólio

- itens sem business owner ou baseline;
- duplicated capabilities;
- custo por outcome e por tier;
- agentes com uso mas sem qualidade/outcome suficiente;
- agents inativos ainda operando;
- concentração por provider/model/tool;
- time-to-decision para corrigir ou aposentar;
- benefícios esperados versus observados, com incerteza.

<!-- source-unit {"classification": "risk-failure-mode", "end_line": "132", "index": 54, "source_field": "", "source_heading": "Failure modes", "source_path": "docs/value/README.md", "start_line": "122", "transformation": "preserve-exact-heading-subtree-and-merge-with-registry-boundary-explicit", "unit_type": "markdown-atx-heading"} -->
#### Failure modes

- valor inferido por número de agentes;
- horas “economizadas” sem medir qualidade ou deslocamento de trabalho;
- ROI calculado com adoção projetada como fato;
- ignorar custo de assurance e suporte;
- manter agente porque já foi construído;
- atribuir outcome ao agente sem baseline;
- premiar volume e criar agent sprawl;
- esconder externalities negativas.

<!-- source-unit {"classification": "requirement-control", "end_line": "135", "index": 55, "source_field": "", "source_heading": "Decision gate", "source_path": "docs/value/README.md", "start_line": "133", "transformation": "preserve-exact-heading-subtree-and-merge-with-registry-boundary-explicit", "unit_type": "markdown-atx-heading"} -->
#### Decision gate

Nenhum item entra no portfólio financiado sem problema, owner, baseline ou plano explícito para obtê-lo, value hypothesis, costs, metrics e sunset criteria.

## Acceptance criteria

- todas as decisões deste capítulo possuem authority, owner e evidência recuperável;
- requisitos aplicáveis estão ligados ao catálogo de controles e ao método de verificação;
- exceções têm escopo, justificativa, compensating controls, expiry e decisão residual;
- controles de build time e runtime são distinguidos e exercitados quando aplicáveis;
- mudanças materiais reabrem avaliação, aprovação e evidência;
- nenhuma alegação de conformidade, eficácia ou valor excede a evidência observada.

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

### 10.1 Princípios de medição e ownership de métricas

**Decisão/ação obrigatória.** Para **princípios de medição e ownership de métricas**, a organização deve atribuir a cada métrica uma finalidade de decisão, owner e consumidor accountable antes da coleta.

**Registro e evidência.** O dicionário de métricas deve definir fórmula, população, fonte, qualidade, corte, segmentação, alvo e aviso de uso indevido.

**Concluído quando.** Dois analistas reproduzem o valor e a authority consumidora declara qual decisão um threshold pode alterar.

### 10.2 Cobertura de governança

**Decisão/ação obrigatória.** Para **cobertura de governança**, a organização deve medir a população declarada contra registros governados, registrados, com owner e atuais.

**Registro e evidência.** Reter fonte do denominador, data de reconciliação, ativos sem correspondência, confiança, exclusões e owner da remediação.

**Concluído quando.** A cobertura não pode melhorar encolhendo um denominador não declarado e ativos de alto risco ausentes permanecem visíveis.

### 10.3 Completude do inventário e qualidade do ownership

**Decisão/ação obrigatória.** Para **completude do inventário e qualidade do ownership**, a organização deve medir a população declarada contra registros governados, registrados, com owner e atuais.

**Registro e evidência.** Reter fonte do denominador, data de reconciliação, ativos sem correspondência, confiança, exclusões e owner da remediação.

**Concluído quando.** A cobertura não pode melhorar encolhendo um denominador não declarado e ativos de alto risco ausentes permanecem visíveis.

### 10.4 Desempenho de processo e latência de decisão

**Decisão/ação obrigatória.** Para **desempenho de processo e latência de decisão**, a organização deve medir fila, tempo de ciclo, atraso de handoff, retrabalho e envelhecimento de decisão por tier e resultado.

**Registro e evidência.** Registrar timestamps, população, alvo de serviço, gargalo, exceção, demanda e premissas de capacidade.

**Concluído quando.** Redução de latência não ignora evidência exigida e gargalos persistentes recebem um owner e uma decisão de redesign.

### 10.5 Exposição a risco e risco residual

**Decisão/ação obrigatória.** Para **exposição a risco e risco residual**, a organização deve apresentar o risco residual após tratamento verificado à authority empoderada para aquela exposição.

**Registro e evidência.** Registrar risco inerente, evidência de tratamento, classificação residual, incerteza, condições de aceite, aprovador e expiração.

**Concluído quando.** O time de entrega não pode auto-aceitar risco residual material e o aceite não sobrepõe admissibilidade ou lei.

### 10.6 Indicadores de qualidade, segurança, fairness, privacidade e proteção

**Decisão/ação obrigatória.** Para **indicadores de qualidade, segurança, fairness, privacidade e proteção**, a organização deve definir indicadores leading e lagging para o resultado nomeado de qualidade, impacto ou controle.

**Registro e evidência.** Registrar fórmula, população, fatias, threshold, baseline, confiança, qualidade da fonte e owner da resposta.

**Concluído quando.** O indicador detecta deterioração significativa sem mascarar fatias reprovadas nem tratar ausência de telemetria como sucesso.

### 10.7 Tendências de incidentes, exceções e remediação

**Decisão/ação obrigatória.** Para **tendências de incidentes, exceções e remediação**, a organização deve analisar recorrência, envelhecimento, severidade, causa raiz e qualidade de fechamento em incidentes e exceções.

**Registro e evidência.** Registrar taxonomia comparável, período, população, reaberturas, itens vencidos, causas sistêmicas e ação da gestão.

**Concluído quando.** A revisão de tendências distingue mais detecção de mais dano e leva a prevenção ou redesign de controle quando justificado.

### 10.8 Implementação de controle versus eficácia

**Decisão/ação obrigatória.** Para **implementação de controle versus eficácia**, a organização deve reportar design, implementação, cobertura operacional e eficácia observada como estados separados.

**Registro e evidência.** Registrar control ID, owner, população aplicável, evidência de implementação, método de teste, resultado, lacunas e data de reteste.

**Concluído quando.** Um controle configurado não é chamado de eficaz sem evidência de resultado e eficácia reprovada muda risco ou aprovação.

### 10.9 Completude e qualidade das evidências

**Decisão/ação obrigatória.** Para **completude e qualidade das evidências**, a organização deve medir se a evidência exigida existe, é atual, atribuível, íntegra e relevante para a decisão.

**Registro e evidência.** Registrar requisito de evidência, população, status presente/ausente/obsoleta, integridade, revisor e remediação.

**Concluído quando.** Evidência ausente ou de baixa qualidade reduz a confiança e não pode ser contada como controle aprovado.

### 10.10 Adoção e comportamento do usuário

**Decisão/ação obrigatória.** Para **adoção e comportamento do usuário**, a organização deve medir adoção pretendida, uso significativo e comportamento de workaround inseguro por população-alvo.

**Registro e evidência.** Registrar população elegível, uso ativo, conclusão de tarefa, abandono, demanda de suporte, feedback e limitações de amostragem.

**Concluído quando.** O owner consegue distinguir disponibilidade de adoção útil e pode mudar treinamento, design ou rollout com base em evidência.

### 10.11 Custo e eficiência

**Decisão/ação obrigatória.** Para **custo e eficiência**, a organização deve atribuir consumo e custo operacional total a agente, owner, ambiente e resultado mensurável.

**Registro e evidência.** Registrar custo unitário, orçamento, quota, previsão, variância, alocação de custo compartilhado, anomalia e decisão de otimização.

**Concluído quando.** Violação de threshold dispara throttling ou revisão e alegações de custo permanecem separadas de alegações de realização de valor.

### 10.12 Resultado e realização de valor

**Decisão/ação obrigatória.** Para **resultado e realização de valor**, a organização deve definir um resultado falseável, baseline pré-mudança e contrafactual crível com corte de evidências.

**Registro e evidência.** Registrar owner da métrica, população, fórmula, alvo, fonte, confounders, custo e threshold de decisão.

**Concluído quando.** A authority consegue distinguir criação, adoção, qualidade e resultado e pode interromper o trabalho quando a evidência não suporta expansão.

### 10.13 Desempenho de fornecedores

**Decisão/ação obrigatória.** Para **desempenho de fornecedores**, a organização deve governar fornecedores e dependências a jusante por due diligence, contrato, monitoramento e planejamento de saída.

**Registro e evidência.** Registrar serviço, owner, criticidade, evidência, obrigações, concentração, incidentes, subprocessadores, fallback e teste de saída.

**Concluído quando.** Falha do fornecedor dispara a contenção ou fallback acordado e a accountability permanece com a organização.

### 10.14 Avaliação de maturidade e confiança

**Decisão/ação obrigatória.** Para **avaliação de maturidade e confiança**, a organização deve pontuar a capacidade organizacional somente a partir de operação observada e declarar separadamente confiança e cobertura da evidência.

**Registro e evidência.** Registrar dimensão, critérios, evidência, pontuação 0–4, rationale, confiança, cobertura, revisor e alvo.

**Concluído quando.** A pontuação não pode exceder o critério demonstrado mais baixo e a comparação usa escopo e método compatíveis.

### 10.15 Cadência de revisão de portfólio

**Decisão/ação obrigatória.** Para **cadência de revisão de portfólio**, a organização deve definir cadência de revisão baseada em risco e gatilhos orientados a eventos em vez de depender apenas de calendário.

**Registro e evidência.** Registrar última revisão, próxima revisão, gatilho, revisor, corte de evidências, decisão e ações abertas.

**Concluído quando.** Artefatos vencidos ou afetados por gatilho são visíveis e não podem permanecer aprovados silenciosamente.

### 10.16 Revisão de policy, controles e normas

**Decisão/ação obrigatória.** Para **revisão de policy, controles e normas**, a organização deve revisar requisitos contra incidentes, exceções, testes, mudança externa e experiência de implementação.

**Registro e evidência.** Registrar versão do artefato, evidências consideradas, lacunas, mudança proposta, consulta, decisão e impacto de migração.

**Concluído quando.** Requisitos obsoletos ou ineficazes são revisados ou superseded sem apagar decisões históricas.

### 10.17 Mudança regulatória, de ameaças e de tecnologia

**Decisão/ação obrigatória.** Para **mudança regulatória, de ameaças e de tecnologia**, a organização deve definir mudanças materiais e eventos externos que reabram risco, aprovação, avaliação ou compatibilidade contratual.

**Registro e evidência.** Registrar gatilho, fonte de detecção, ativos e evidências impactados, controle provisório, owner, data de vencimento e disposição.

**Concluído quando.** Ativos acionados não podem depender indefinidamente de aprovação anterior e a nova decisão é vinculada à versão alterada.

### 10.18 Backlog de melhorias e priorização

**Decisão/ação obrigatória.** Para **backlog de melhorias e priorização**, a organização deve manter um único backlog ciente de risco e dependências para melhorias de controle, plataforma, processo e evidência.

**Registro e evidência.** Registrar origem da descoberta, severidade, benefício, owner, dependência, esforço, data de vencimento, status e critério de aceite.

**Concluído quando.** Mudanças de prioridade são explícitas e itens materiais vencidos influenciam decisões de risco, financiamento ou operação.

### 10.19 Decisões de manter, expandir, restringir, redesenhar ou aposentar

**Decisão/ação obrigatória.** Para **decisões de manter, expandir, restringir, redesenhar ou aposentar**, a organização deve selecionar uma disposição de portfólio a partir de resultado atual, risco, custo, adoção e evidência.

**Registro e evidência.** Registrar alternativas, corte de evidências, decisão, authority, condições, ativos afetados e owner da implementação.

**Concluído quando.** A disposição muda financiamento, exposição ou estado de lifecycle e não é meramente uma recomendação sem owner.

### 10.20 Revisão da gestão e reporte de accountability

**Decisão/ação obrigatória.** Para **revisão da gestão e reporte de accountability**, a organização deve apresentar à gestão accountable uma visão integrada de resultados, risco, eficácia de controles, incidentes, exceções, recursos e decisões.

**Registro e evidência.** Reter pauta, corte de evidências, limitações materiais, premissas desafiadas, decisões, owners, datas e acompanhamento.

**Concluído quando.** A gestão registra decisões explícitas de manter, melhorar, restringir, financiar ou aposentar e as acompanha até o fechamento.


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

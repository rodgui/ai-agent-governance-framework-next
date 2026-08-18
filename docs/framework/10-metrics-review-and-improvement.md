---
title: 10 — Métricas, revisão e melhoria contínua
status: maintained
maturity: validated
last_reviewed: 2026-08-18
review_cycle: quarterly
owners: [framework-maintainers]
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# 10 — Métricas, revisão e melhoria contínua

## Visão geral

Se o capítulo anterior responde "como operamos", este responde **"como sabemos se estamos melhorando — e o que fazer com isso?"**

Métricas de governança têm um propósito único: **mudar decisões**. Uma métrica sem ação associada é decoração; um dashboard que não muda uma decisão é observação. E há um erro mais sutil: misturar o que medimos. **KPI mede desempenho, KRI mede exposição a risco, métrica operacional mede processo, métrica de valor mede resultado econômico** — cada uma exige ação diferente.

Este capítulo cobre:

1. **O que medir:** cobertura, ownership, processo, risco, controles, evidências, adoção, custo, valor, maturidade.
2. **Como medir:** princípios de medição, dicionário de métricas, thresholds com rationale, dashboard por decisão.
3. **Como revisar:** cadência por risco, gatilhos de evento, revisão de policy, mudança regulatória.
4. **Como melhorar:** backlog único, decisões de disposição, reporte à gestão accountable.

O princípio que atravessa tudo: **métrica sem owner, threshold e ação não entra em um fórum de governança.** E o complemento financeiro: **sair de "custo por token" para custo por resultado** — porque um modelo mais caro por token pode ser economicamente melhor se reduzir retries e retrabalho humano.

> **Artefatos para produzir agora — decisão baseada em métricas.** Use o [Use-Case Portfolio](../../toolkit/templates/use-case-portfolio.md) para conectar caso, baseline, custo, outcome e disposição; o [Capability Assessment Worksheet](../../toolkit/templates/capability-assessment-worksheet.md) para medir gaps de capacidade; e o [Maturity Assessment](../../toolkit/templates/maturity-assessment-template.md) para registrar score, confidence e target. Métrica informa a decisão; não substitui o owner nem transforma correlação em causalidade.

## 1. O que medir

### 1.1 Princípios de medição e ownership de métricas

Toda métrica tem finalidade de decisão, owner e consumidor accountable **antes da coleta**. O dicionário de métricas define: fórmula, população, fonte, qualidade, corte, segmentação, alvo e aviso de uso indevido. **Dois analistas reproduzem o valor; a authority consumidora declara qual decisão um threshold pode alterar.**

### 1.2 A taxonomia das métricas: cada uma mede um objeto

Métricas de governança não formam uma lista plana — formam **camadas**, cada uma respondendo a uma pergunta diferente. Misturá-las no mesmo dashboard é a causa mais comum de "painel cheio e nenhuma decisão". A tabela é o mapa; as subseções seguintes detalham cada camada.

| Camada | Pergunta que responde | Exemplos | Quem consome |
|---|---|---|---|
| **Inventário e estate** | o que existe e está governado? | cobertura do registry, % com owner, % com tier atribuído | governance owner |
| **Agente individual** | este agente é seguro, bom e usado? | task success, erros, custo por resultado, adoção real | owners técnicos/de negócio |
| **Capability e maturidade** | a organização sabe governar? | maturity por dimensão (0–4) | governance owner, sponsor |
| **Processo de governança** | o processo é rápido e não bloqueia? | lead time por gate, retrabalho, gargalos | Run Authority |
| **Risco e compliance** | quanto risco estamos carregando? | residual risk, incidentes, exceções vencidas | CRO, compliance, auditoria |
| **Valor e portfólio** | o investimento compensa? | custo por resultado, KPI de negócio, agentes sem valor | business owners, sponsor |

**A regra de navegação:** comece pela camada que responde à decisão da vez. Pedir métricas de inventário para decidir portfólio é usar o mapa errado — e o erro se repete em todo fórum que não declara qual camada está discutindo.

### 1.3 Inventário e estate

Medir a população declarada contra registros governados, registrados, com owner e atuais: fonte do denominador, data de reconciliação, ativos sem correspondência, confiança, exclusões e owner da remediação. **A cobertura não pode melhorar encolhendo um denominador não declarado; ativos de alto risco ausentes permanecem visíveis.**

Indicadores típicos: cobertura do registry; % de agentes com business e technical owner válidos; % com tier e admissibilidade atribuídos; % com blueprint vigente; agentes dormantes por período; shadow AI estimado × descoberto; idade média da última reconciliação. A fonte de cada um é o [inventário](03-inventory-portfolio-and-value.md) — sem inventário honesto, nenhuma métrica desta camada significa nada.

### 1.4 Agente individual

**Qualidade, segurança, fairness, privacidade e proteção.** Indicadores leading e lagging para o resultado nomeado: fórmula, população, fatias, threshold, baseline, confiança, qualidade da fonte e owner da resposta. **O indicador detecta deterioração significativa sem mascarar fatias reprovadas nem tratar ausência de telemetria como sucesso.** Métricas técnicas mínimas por agente (acurácia, tempo de resposta, taxa de erro, satisfação) são definidas pelo technical owner e monitoradas continuamente — a telemetria de runtime do [cap. 09](09-operations-incidents-and-continuity.md) é a fonte.

**Adoção e comportamento do usuário.** Medir adoção pretendida, uso significativo e workaround inseguro por população-alvo: população elegível, uso ativo, conclusão, abandono, suporte, feedback e limitações de amostragem. **Usuários ativos medem frequência e retenção, não valor** — um agente pode ter uso mensal alto porque virou etapa obrigatória de um fluxo e ainda assim piorar o cycle time. Adoção só significa algo junto de qualidade e outcome.

**Prontidão do dossiê.** O [score de prontidão](07-evaluation-evidence-and-assurance.md#7-score-de-prontidao-do-dossie) por agente e a distribuição da população — quantos agentes estão no threshold do tier, quantos têm bloqueadores ativos, tempo médio até o dossiê fechar. **Score baixo generalizado é sintoma de processo doente, não de equipe preguiçosa.**

### 1.5 Capability e maturidade

Pontuar a capacidade organizacional **somente a partir de operação observada**, declarando separadamente confiança e cobertura da evidência: dimensão, critérios, evidência, pontuação 0–4, rationale, confiança, cobertura, revisor e alvo. **A pontuação não pode exceder o critério demonstrado mais baixo; a comparação usa escopo e método compatíveis.** Evidência fraca produz nota provisória, não nota otimista. O instrumento é o [maturity model](../../toolkit/maturity/maturity-model.md); o alvo por dimensão vem do [capability map](08-implementation-and-adoption.md).

### 1.6 Processo de governança

Medir fila, tempo de ciclo, atraso de handoff, retrabalho e envelhecimento de decisão por tier e resultado: timestamps, população, alvo de serviço, gargalo, exceção, demanda e premissas de capacidade. **Redução de latência não ignora evidência exigida; gargalos persistentes recebem owner e decisão de redesign.**

Duas medidas desta camada merecem destaque por serem as mais falsificadas:

- **Implementação de controle versus eficácia.** Reportar design, implementação, cobertura operacional e eficácia observada como **estados separados**: control ID, owner, população aplicável, evidência de implementação, método de teste, resultado, lacunas e data de reteste. **Um controle configurado não é chamado de eficaz sem evidência de resultado; eficácia reprovada muda risco ou aprovação.**
- **Completude e qualidade das evidências.** Medir se a evidência exigida existe, é atual, atribuível, íntegra e relevante: requisito de evidência, população, status presente/ausente/obsoleta, integridade, revisor e remediação. **Evidência ausente ou de baixa qualidade reduz a confiança e não pode ser contada como controle aprovado.**

### 1.7 Risco e compliance

**Exposição a risco e risco residual.** O risco residual após tratamento verificado é apresentado à authority empoderada: risco inerente, evidência de tratamento, classificação residual, incerteza, condições de aceite, aprovador e expiração. **O time de entrega não pode auto-aceitar risco residual material; o aceite não sobrepõe admissibilidade ou lei** (ver [cap. 04](04-risk-impact-and-compliance.md)).

**Tendências de incidentes, exceções e remediação.** Analisar recorrência, envelhecimento, severidade, causa raiz e qualidade de fechamento: taxonomia comparável, período, população, reaberturas, itens vencidos, causas sistêmicas e ação da gestão. **A revisão distingue mais detecção de mais dano** — um aumento de incidentes pode significar piora ou melhor visibilidade; a análise decide qual. A revisão de exceções é a mais reveladora: **exceção que se repete não é exceção — é requisito que a policy não reconheceu ou controle que a operação não cumpre.**

### 1.8 Valor e portfólio

**Resultado e realização de valor.** Resultado falseável, baseline pré-mudança e contrafactual crível com corte de evidências: owner da métrica, população, fórmula, alvo, fonte, confounders, custo e threshold. **A authority distingue criação, adoção, qualidade e resultado e interrompe o trabalho quando a evidência não suporta expansão.**

**Custo e eficiência (FinOps).** Atribuir consumo e custo total a agente, owner, ambiente e resultado (ver seção 3): custo unitário, orçamento, quota, previsão, variância, alocação compartilhada, anomalia e decisão de otimização. **Violação de threshold dispara throttling ou revisão; custo permanece separado de valor.**

**Desempenho de fornecedores.** Fornecedores governados por due diligence, contrato, monitoramento e saída: serviço, owner, criticidade, evidência, obrigações, concentração, incidentes, subprocessadores, fallback e teste de saída. **Falha do fornecedor dispara contenção/fallback; a accountability permanece com a organização.**

## 2. KPIs, KRIs e governance dashboard

### 2.1 Três tipos, três usos (não misturar)

| Tipo | O que mede | Exemplo | Ação associada |
|---|---|---|---|
| **KPI** | desempenho ou resultado desejado | % de T2/T3 com identidade própria | priorizar remediação se abaixo da meta |
| **KRI** | exposição ou deterioração de risco | % de T3 com attestation vencida | suspender ou escalar conforme prazo |
| **operacional** | capacidade do processo | lead time da security review | ajustar intake, automação ou capacidade |
| **valor** | economia e resultado real | custo por caso bem-sucedido + cycle time | escalar, redesenhar ou aposentar |

### 2.2 Indicadores de referência — baseline ilustrativo, não SLA

> **ILLUSTRATIVE · NON-NORMATIVE · RECALIBRATE WITH LOCAL BASELINE.** Os valores desta seção mostram como uma organização pode estruturar indicadores e decisões; não são thresholds universais, SLA do framework ou promessa de maturidade. A authority local deve recalibrar cada número usando baseline observado, tier, risk appetite, população, distribuição, capacidade operacional, evidence cutoff, owner, action e review trigger.

A regra: **metas de higiene e accountability podem ser absolutas; métricas de adoção, custo, falso positivo e lead time partem do baseline e do perfil operacional.** Mesmo valores absolutos precisam declarar população, escopo, enforcement, exceção e autoridade.

| Tipo | Indicador | Referência inicial |
|---|---|---|
| KPI | cobertura do inventário | ≥95% na implantação; ≥98% em operação madura |
| KPI | agentes em produção com owner | 100%; ownerless em T2/T3 igual a zero |
| KPI | lead time de aprovação por tier | T1 fast path imediato; T1 revisado até 1 dia; T2 3–5 dias; T3 5–15 dias; T4 sem rota normal |
| KPI | cobertura de attestation | ≥98% vigente; T3 vencido igual a zero |
| KRI | agentes de alto risco sem owner | zero em T2/T3/T4, com remediação imediata |
| KRI | anomalias de ferramenta privilegiada | 100% investigadas; alta severidade dentro do SLA |
| KRI | agentes fora do padrão de identidade | zero em T2/T3 em produção; tendência decrescente nos demais |
| KRI | agentes T2/T3 dormentes | abaixo de 5% sem justificativa; 100% com ação |
| Valor | custo por resultado bem-sucedido | baseline mais meta de melhoria acordada |
| Valor | melhoria do KPI de negócio | alvo específico do caso; **adoção não é proxy de resultado** |
| Adoção | usuários ativos diários/semanais/mensais | sem alvo universal; tendência e frequência esperada |

**Registre a justificativa de cada threshold e a data de revisão. Revise após o primeiro ciclo com dados reais.** Se o baseline ainda não existir, registre o valor como hipótese de calibração e não como target aprovado.

### 2.3 Dashboard executivo mínimo

- **estate e crescimento:** conhecidos versus estimados, novos por semana, mix de tiers;
- **ownership e lifecycle:** sem owner, attestation vencida, dormentes, candidatos a retirada;
- **risco e segurança:** findings críticos, incidentes, quarentenas, exceções de alto impacto;
- **cobertura de controles:** identidade, dados certificados, registro de ferramentas, telemetria e conformidade com o [Minimum Production Bar](../../toolkit/controls/minimum-production-bar.md);
- **FinOps:** custo por agente, custo por resultado, variação de budget e principais anomalias;
- **valor:** adoção, KPI de outcome, valor observado e agentes sem valor demonstrado;
- **programa:** lead time por tier, retrabalho de review, cobertura de automação e progresso de maturidade.

**Não coloque todo o detalhe em uma página.** A página executiva mostra postura; as páginas operacionais permitem drill-down até o trace e a ação de ferramenta.

### 2.4 Como definir thresholds

Não transforme toda métrica em verde e vermelho arbitrários. Use baseline, risk appetite, SLA e tendência. Para agentes T3 sem owner, a tolerância pode ser zero. Para falso positivo de uma regra nova, a meta é calibrada gradualmente. **Em ambos os casos, registre a razão do threshold e quando ele será revisto.**

## 3. FinOps de agentes e unit economics

### 3.1 Do custo por token ao custo por resultado

Sair de "custo por token" para **custo por resultado**, atribuir esse custo a um responsável e detectar desperdício antes que vire problema de orçamento ou vetor de abuso. **A comparação relevante é sempre custo por tarefa concluída com qualidade preservada.**

### 3.2 Atribuição

Todo custo material responde a quatro perguntas: **qual agente, qual owner, qual unidade de negócio, qual caso de uso.** Sem chave de correlação no evento de custo, FinOps enxerga gasto sem contexto e a decisão de portfólio vira opinião.

### 3.3 Decomposição do custo

Separe as camadas quando forem materiais: inferência; retrieval e indexação; execução de ferramentas e chamadas externas; armazenamento e memória; observabilidade e retenção de evidência; **supervisão e aprovação humana — frequentemente o maior custo em T3 e sistematicamente esquecido**; custo de build e teste separado de produção.

### 3.4 Unit economics

1. Definir a unidade de resultado do caso: ticket resolvido, fatura processada, documento revisado.
2. Medir custo por unidade **bem-sucedida**, não por execução. **Tentativas falhas são custo do sucesso.**
3. Comparar contra o baseline do processo anterior, com limitações declaradas.
4. Incluir o custo humano de revisão quando o desenho exige aprovação.
5. Reavaliar após mudança de versão de modelo — o custo por tarefa pode mudar sem que o preço por token mude.

### 3.5 Budget, quota e denial-of-wallet

Budget por caso de uso e por tier, não apenas orçamento global; quota e circuit breaker por agente (limite de chamadas, profundidade de cadeia e duração); loops e retries descontrolados são simultaneamente problema de custo e sinal de segurança; notificação ao owner antes de enforcement automático; exceção de budget com prazo, como qualquer outra exceção.

> **O ataque de denial-of-wallet não derruba o sistema: ele o torna economicamente inviável. Um agente exposto sem quota é uma superfície de custo aberta.**

### 3.6 Alavancas de otimização

Cache · tamanho de contexto e estratégia de recuperação · roteamento entre modelos com equivalência de controles · redução de profundidade de cadeia · reuso de resultados · escolha de ferramenta com menor custo por chamada. **Nenhuma alavanca pode reduzir silenciosamente o nível de assurance.**

### 3.7 Integração com portfólio

O custo total entra na decisão de portfólio: manter, expandir, corrigir, restringir, substituir ou aposentar. **Um agente com bom outcome e unit economics ruim é candidato a redesenho, não a expansão.**

## 4. Revisão e melhoria contínua

### 4.1 Cadência de revisão de portfólio

Cadência baseada em risco e gatilhos orientados a eventos, em vez de apenas calendário: última revisão, próxima revisão, gatilho, revisor, corte de evidências, decisão e ações abertas. **Artefatos vencidos ou afetados por gatilho são visíveis e não permanecem aprovados silenciosamente.**

### 4.2 Revisão de policy, controles e normas

Requisitos revisados contra incidentes, exceções, testes, mudança externa e experiência de implementação: versão do artefato, evidências consideradas, lacunas, mudança proposta, consulta, decisão e impacto de migração. **Requisitos obsoletos ou ineficazes são revisados ou superseded sem apagar decisões históricas.**

### 4.3 Mudança regulatória, de ameaças e de tecnologia

Mudanças materiais e eventos externos que reabrem risco, aprovação, avaliação ou compatibilidade contratual: gatilho, fonte de detecção, ativos e evidências impactados, controle provisório, owner, vencimento e disposição. **Ativos acionados não dependem indefinidamente de aprovação anterior; a nova decisão é vinculada à versão alterada.**

### 4.4 Backlog de melhorias e priorização

Um único backlog ciente de risco e dependências para melhorias de controle, plataforma, processo e evidência: origem da descoberta, severidade, benefício, owner, dependência, esforço, vencimento, status e critério de aceite. **Mudanças de prioridade são explícitas; itens materiais vencidos influenciam decisões de risco, financiamento ou operação.**

### 4.5 Decisões de manter, expandir, restringir, redesenhar ou aposentar

Disposição de portfólio a partir de resultado atual, risco, custo, adoção e evidência: alternativas, corte de evidências, decisão, authority, condições, ativos afetados e owner da implementação. **A disposição muda financiamento, exposição ou estado de lifecycle — não é recomendação sem owner.**

### 4.6 Revisão da gestão e reporte de accountability

Visão integrada de resultados, risco, eficácia de controles, incidentes, exceções, recursos e decisões apresentada à gestão accountable: pauta, corte de evidências, limitações materiais, premissas desafiadas, decisões, owners, datas e acompanhamento. **A gestão registra decisões explícitas de manter, melhorar, restringir, financiar ou aposentar e as acompanha até o fechamento.**

### 4.7 O ciclo trimestral de melhoria

1. Revisar KPIs, KRIs e tendências do estate.
2. Analisar principais incidentes, quase-incidentes e eventos de quarentena.
3. Revisar exceções — **uma exceção que se repete não é exceção: é requisito que a policy não reconheceu ou controle que a operação não cumpre** — os dois casos exigem mudança, não renovação.
4. Avaliar falsos positivos e negativos das regras de comportamento e dos policy gates.
5. Revisar gargalos manuais e oportunidades de automação.
6. Atualizar standards com changelog e data de vigência.
7. Priorizar as próximas capacidades no roadmap de maturidade.

**Sinais de maturidade adaptativa:** mudanças de policy baseadas em dados de runtime; novos agentes descobertos e registrados automaticamente; mudança material dispara reavaliação proporcional; sinais reduzem capacidade automaticamente com override governado; custo e valor orientam retirada; **evidência é produzida continuamente, não preparada para a auditoria.**

## 5. Referência normativa

Condições mínimas que devem ser verdadeiras. Use como checklist; as seções 1–4 explicam o porquê.

| # | Obrigação | Evidência mínima | Concluído quando |
|---|---|---|---|
| R1 | Atribuir a cada métrica finalidade de decisão, owner e consumidor accountable antes da coleta | dicionário com fórmula, população, fonte, qualidade, corte, segmentação, alvo, aviso | dois analistas reproduzem o valor; authority declara qual decisão o threshold altera |
| R2 | Medir população declarada contra registros governados, com owner e atuais | fonte do denominador, reconciliação, ativos sem correspondência, confiança, exclusões, remediação | cobertura não melhora encolhendo denominador; alto risco ausente visível |
| R3 | Medir fila, tempo de ciclo, handoff, retrabalho e envelhecimento por tier | timestamps, população, alvo, gargalo, exceção, demanda, capacidade | redução de latência não ignora evidência; gargalos têm owner e redesign |
| R4 | Apresentar risco residual à authority empoderada | risco inerente, tratamento, residual, incerteza, condições, aprovador, expiração | time não auto-aceita residual material; aceite não sobrepõe admissibilidade |
| R5 | Definir indicadores leading e lagging para qualidade, impacto e controle | fórmula, população, fatias, threshold, baseline, confiança, fonte, owner | detecta deterioração sem mascarar fatias; ausência de telemetria não é sucesso |
| R6 | Analisar recorrência, envelhecimento, severidade, causa raiz e fechamento | taxonomia, período, população, reaberturas, vencidos, causas sistêmicas, ação | distingue mais detecção de mais dano; leva a prevenção/redesign |
| R7 | Reportar design, implementação, cobertura e eficácia como estados separados | control ID, owner, população, evidência, método, resultado, lacunas, reteste | configurado ≠ eficaz; eficácia reprovada muda risco ou aprovação |
| R8 | Medir existência, atualidade, atribuição, integridade e relevância da evidência | requisito, população, status, integridade, revisor, remediação | ausente/baixa qualidade reduz confiança; não conta como controle aprovado |
| R9 | Medir adoção pretendida, uso significativo e workaround por população | população elegível, uso, conclusão, abandono, suporte, feedback, amostragem | owner distingue disponibilidade de adoção útil; muda treinamento/design/rollout |
| R10 | Atribuir consumo e custo total a agente, owner, ambiente e resultado | custo unitário, orçamento, quota, previsão, variância, alocação, anomalia | threshold violado dispara throttling/revisão; custo separado de valor |
| R11 | Definir resultado falseável, baseline e contrafactual com corte de evidências | owner, população, fórmula, alvo, fonte, confounders, custo, threshold | authority distingue criação/adoção/qualidade/resultado e interrompe sem evidência |
| R12 | Governar fornecedores por due diligence, contrato, monitoramento e saída | serviço, owner, criticidade, evidência, obrigações, concentração, incidentes, fallback | falha do fornecedor dispara contenção/fallback; accountability permanece |
| R13 | Pontuar maturidade somente de operação observada com confiança e cobertura separadas | dimensão, critérios, evidência, pontuação 0–4, rationale, confiança, cobertura, revisor | pontuação não excede critério mais baixo; comparação com escopo compatível |
| R14 | Definir cadência de revisão baseada em risco e gatilhos de evento | última/próxima revisão, gatilho, revisor, corte, decisão, ações | vencidos/afetados visíveis; não permanecem aprovados silenciosamente |
| R15 | Revisar requisitos contra incidentes, exceções, testes e mudança externa | versão, evidências, lacunas, mudança, consulta, decisão, migração | obsoletos/ineficazes revisados ou superseded sem apagar histórico |
| R16 | Definir mudanças materiais e eventos que reabrem risco/avaliação | gatilho, fonte, ativos impactados, controle provisório, owner, vencimento | acionados não dependem de aprovação anterior; decisão vinculada à versão |
| R17 | Manter backlog único ciente de risco e dependências | origem, severidade, benefício, owner, dependência, esforço, vencimento, status, aceite | prioridades explícitas; itens materiais vencidos influenciam decisões |
| R18 | Selecionar disposição de portfólio de resultado, risco, custo, adoção e evidência | alternativas, corte, decisão, authority, condições, ativos, owner | disposição muda financiamento/exposição/lifecycle; não é recomendação sem owner |
| R19 | Apresentar visão integrada à gestão accountable | pauta, corte, limitações, premissas, decisões, owners, datas, acompanhamento | gestão registra decisões explícitas e acompanha até fechamento |

## 6. Evidências, métricas e failure modes

**Evidências:** definição de cada métrica com fórmula, fonte e owner; thresholds com rationale e data de revisão; histórico de decisões tomadas a partir do dashboard; lacunas de dados declaradas, não preenchidas por estimativa; modelo de custo com premissas; atribuição por agente/owner/unidade/caso; custo por resultado com baseline; budgets e quotas; anomalias investigadas; variação após mudança de versão.

**Métricas:** métricas exibidas sem owner ou ação; indicadores que nunca mudaram decisão; lacunas de cobertura por perspectiva; tempo entre sinal e decisão; custo por agente/sessão/resultado bem-sucedido; variação contra budget por tier; proporção de custo em execuções falhas; agentes sem budget/quota; custo de supervisão humana como fração em T3; concentração por provedor.

**Failure modes:** misturar KPI, KRI e métrica operacional na mesma leitura; média agregada que esconde dimensão crítica; alvo copiado de outro contexto; adoção apresentada como prova de valor; dashboard completo e ilegível em uma página; precisão numérica sobre dados de baixa cobertura; verde e vermelho sem rationale; comparar apenas preço por token; medir custo por execução em vez de por sucesso; ignorar custo de supervisão/suporte/assurance; orçamento global sem quota por agente; automatizar corte de budget sem notificar owner; otimizar custo trocando modelo sem equivalência de controles; tratar pico de custo só como tema financeiro quando também é sinal de segurança.

## Decision gates

- **FinOps:** nenhum agente entra em produção sem atribuição de custo, budget do caso e quota compatível com o tier. Nenhuma decisão de expandir portfólio é tomada sem custo por resultado medido contra baseline.
- **Dashboard:** nenhuma métrica entra em um fórum de governança sem owner, threshold com rationale e ação esperada. Nenhum indicador de higiene crítica é reportado sem cobertura declarada.
- **Maturidade:** a pontuação não pode exceder o critério demonstrado mais baixo.

## Acceptance criteria

- todas as decisões deste capítulo possuem authority, owner e evidência recuperável;
- requisitos aplicáveis estão ligados ao catálogo de controles e ao método de verificação;
- exceções têm escopo, justificativa, compensating controls, expiry e decisão residual;
- controles de build time e runtime são distinguidos e exercitados quando aplicáveis;
- mudanças materiais reabrem avaliação, aprovação e evidência;
- nenhuma alegação de conformidade, eficácia ou valor excede a evidência observada.

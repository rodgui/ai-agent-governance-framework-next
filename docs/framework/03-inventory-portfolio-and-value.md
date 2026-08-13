---
title: 03 — Inventário, portfólio e valor
status: maintained
maturity: validated
last_reviewed: 2026-08-12
review_cycle: quarterly
owners: [framework-maintainers]
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# 03 — Inventário, portfólio e valor


## Visão geral

Antes de governar agentes, a organização precisa responder três perguntas básicas:

1. **O que existe?** — Quais agentes, assistentes e automações baseadas em IA já operam (inclusive aqueles que ninguém oficialmente conhece)?
2. **Quem responde por isso?** — Qual pessoa é responsável por cada ativo, em todos os momentos do ciclo de vida?
3. **Vale a pena?** — Cada agente está conectado a um problema real, com evidência de valor, ou é só custo e risco acumulado?

Este capítulo constrói a resposta na mesma ordem: **descoberta e inventário** (o que existe), **registry e ownership** (quem responde) e **portfólio e valor** (vale a pena continuar, expandir ou aposentar).

O princípio que amarra tudo: **sem visibilidade não há governança.** É impossível aplicar tier, evidência, contenção ou sunset a um ativo que a organização não sabe que existe.

## 1. Conhecer o que existe: descoberta e inventário

### 1.1 Descoberta é disciplina contínua, não projeto pontual

Uma organização que "começa do zero" raramente começa com zero agentes. Ela começa com **baixa visibilidade**. O agent estate muda mais rápido que um inventário tradicional: agentes nascem de usuários, SaaS, low-code, IDEs, automações e código. Um inventário pontual fica obsoleto em semanas.

O baseline (primeira foto do estado atual) é o ponto de partida; a **capacidade contínua de descobrir** é o produto. A descoberta deve rodar por múltiplas fontes reconciliadas, com cadência de redescoberta preferencialmente automatizada.

### 1.2 Fontes de descoberta

Nenhuma fonte isolada é suficiente. A cobertura vem da correlação, e a correlação exige um schema mínimo comum.

| Fonte | O que procurar | Limitação típica | Como compensar |
|---|---|---|---|
| builders e low-code | agentes, apps, owners, status de publicação | não cobre agentes custom | correlacionar com repositórios e gateways |
| IAM e identidades não humanas | service principals, workload identities, secrets | a identidade pode não indicar que é agente | usar convenção de nomes, tags e telemetria de API |
| gateways de modelo e API | chamadas de modelo, chaves, metadados de ator | apenas o tráfego que passa pelo gateway | combinar com egress/proxy e dados de despesa |
| código-fonte e CI/CD | SDKs de agente, clientes de modelo, configurações MCP | protótipos locais podem não aparecer | survey com desenvolvedores e scanning de artefatos |
| inventário de SaaS e compras | produtos com recursos agentic | recurso licenciado pode não estar em uso | validar uso real e logs administrativos |
| rede e egress | destinos de APIs de modelo e endpoints MCP | baixa semântica | usar apenas como sinal de agente `suspected` |

### 1.3 Status de confirmação e confidence: dois campos, duas perguntas

Dois campos diferentes evitam inflar métricas e descartar sinais de shadow AI:

- `discovery.status` descreve o quanto a existência e o contexto do agente foram **confirmados**;
- `discovery.confidence` expressa a confiança na **correlação** dos sinais disponíveis.

| Status | Significado | Ação |
|---|---|---|
| `confirmed` | evidência direta do agente e do seu contexto | registrar e atribuir owner |
| `probable` | múltiplos sinais apontam para uso agentic, sem confirmação | investigar dentro do SLA definido |
| `suspected` | indício isolado que merece verificação | manter no backlog de remediação |

| Confidence | Uso |
| --- | --- |
| `high` | sinais independentes coerentes e recentes |
| `medium` | evidência útil com gap conhecido de cobertura ou contexto |
| `low` | sinal fraco, antigo ou ainda não reconciliado |

**Objetos incertos não são descartados.** Eles entram no backlog com owner e prazo — descartar sinais incertos para não "poluir" a métrica é a forma mais rápida de cegar a governança.

### 1.4 Shadow AI e ativos sem owner

Ativos sem owner ou shadow (criados fora dos processos corporativos) **entram em contenção e resolução de ownership** — não são silenciosamente aceitos no inventário. Um agente descoberto sem owner recebe status `unmanaged` e entra em remediação.

> **Armadilha comum:** tratar o baseline como conclusão em vez de ponto de partida, ou contar versões e instâncias como agentes distintos (o que infla o número real do estate).

### 1.5 Como executar a descoberta e publicar o baseline

As subseções anteriores explicam os conceitos. Esta seção trata somente da execução da descoberta e da publicação do baseline. A classificação normativa de risco, o desenho do agente e a decisão de portfólio acontecem nos processos seguintes e nos capítulos relacionados.

1. **Declarar o escopo da descoberta.** Quais plataformas, unidades, ambientes e tipos de agente entram na primeira passada? Registre também o que fica fora e por quê — cobertura declarada vale mais que cobertura presumida.
2. **Reunir as fontes.** Identidade/SSO, logs de plataformas aprovadas, SaaS contratado, budgets de nuvem, builds/CI, entrevistas com os times. Cada fonte entra no inventário com data de última leitura e confiança.
3. **Consolidar e deduplicar.** Um agente pode aparecer em três fontes com três nomes. A consolidação produz candidatos únicos; a deduplicação decide quais são o mesmo ativo — registre os critérios usados.
4. **Atribuir estado de confirmação.** `confirmed` só com observação direta; `reported` para o que veio de entrevista; `unresolved` para o que ninguém confirma. **Nunca reporte um inventário sem a coluna de confiança.**
5. **Vincular owners.** Todo ativo confirmado recebe business owner e technical owner ativos. O que não tem owner entra na fila de triagem — não desaparece do relatório.
6. **Classificar pelo mínimo.** Para cada ativo: taxonomia e tier preliminar. Registre a admissibilidade somente quando houver fundamento e authority; a classificação fina de casos complexos segue o [cap. 04](04-risk-impact-and-compliance.md). O inventário precisa ao menos separar sinais de maior criticidade dos demais.
7. **Reconciliar contra o registry.** O que existe no registry e não existe mais no estate → candidato a sunset. O que existe no estate e não está no registry → candidato a registro ou contenção. **Reconciliação é o teste de honestidade do inventário.**
8. **Publicar baseline com limitações.** Números com fonte, data de corte e lacunas declaradas. A primeira passada nunca é completa — e declarar isso abertamente é o que permite medir a segunda.
9. **Instalar a rotina.** Descoberta não é projeto pontual: fontes são relidas em cadência, novas plataformas entram no escopo, e cada novo agente nasce já dentro do registry (processo P1 do [cap. 08](08-implementation-and-adoption.md)).

**Armadilhas da primeira passada:** tentar cobrir tudo de uma vez (a descoberta parcial publicada vale mais que a perfeita adiada); aceitar "não tem nenhum agente aqui" sem conferir a fonte (shadow AI vive exatamente onde ninguém olhou); tratar o inventário como fim em vez de meio — o objetivo é o controle, e o inventário é o primeiro passo dele.


### 1.6 Forecast do estate: dimensionar governança, não prometer números

O forecast serve para **dimensionar a governança futura**, não para prometer número exato. Use T1–T4 somente como classificação preliminar do mix de criticidade. A definição normativa do risk tier, os red flags e a relação com admissibilidade estão no [capítulo 04](04-risk-impact-and-compliance.md); o forecast não substitui o risk assessment de cada agente. Passos:

1. Definir baseline por população: agentes pessoais, de time, de processo, embarcados e de terceiros.
2. Identificar drivers: usuários habilitados, builders disponíveis, templates, iniciativas estratégicas, novos SaaS e automações previstas.
3. Criar cenários conservador, provável e acelerado em 6 e 12 meses.
4. **Projetar o mix de risco, não apenas o volume.** Crescer de 1.000 para 5.000 agentes T1 não demanda o mesmo esforço que adicionar 100 agentes T3.
5. Converter o forecast em volumes operacionais: attestations por mês, reviews T2/T3, incidentes esperados, identidades, registros de tools e volume de telemetria.
6. Revisar trimestralmente com dados reais e ajustar capacidade de fóruns, automação e plataforma.

> Exemplo de dimensionamento: se 5.000 usuários habilitados podem criar agentes e apenas 10% criarem 2 agentes cada, o estate potencial já ultrapassa 1.000 agentes — antes de qualquer iniciativa corporativa.


### 1.7 Registro de gargalos manuais

Depois que a descoberta e o baseline estiverem publicados, registre os pontos onde a governança depende de trabalho humano repetitivo. Esse backlog alimenta a decisão sobre o que virar policy-as-code:

| Atividade manual | Volume/mês | Lead time | Risco de automatizar | Decisão inicial |
|---|---|---|---|---|
| aprovar agente T1 somente leitura | 400 | 2 dias | baixo | automatizar com policy gate após calibração em cohort controlada |
| criar identidade de agente T2 | 40 | 4 dias | médio | workflow + API de IAM, mantendo caminho de exceção |
| revisar ferramenta privilegiada T3 | 5 | 5 dias | alto | manter decisão humana; automatizar o preparo da evidência |

**A leitura correta: automatizar a preparação da evidência é quase sempre seguro; automatizar a decisão só quando a policy está estável.**


## 2. Registry: a fonte corporativa de verdade

### 2.1 Quatro objetos distintos (não confundir)

| Objeto | Pergunta que responde | Natureza |
|---|---|---|
| **Registry** | qual agente é este, quem responde, qual tier, admissibilidade, stage e operational state? | fonte corporativa de identificação e correlação |
| **Blueprint** | como esta versão deve ser configurada e controlada? | especificação versionada do desired state |
| **Policy/gate** | a configuração e as evidências atendem às regras? | decisão automática ou semiautomática |
| **Runtime/telemetria** | o agente está operando conforme aprovado? | estado observado |

Confundir registry com blueprint produz o antipattern mais comum: **um inventário que cresce sem nunca virar controle**. O registry responde "o que existe e quem responde"; o blueprint responde "como esta versão deve funcionar"; o portfólio responde "isso deveria continuar existindo". São artefatos distintos e não devem ser fundidos.

### 2.2 Taxonomia corporativa: a linguagem comum do estate

Taxonomia é a linguagem de classificação do estate: características relativamente estáveis que fazem registry, scoring, policies, dashboards e lifecycle usarem os mesmos termos. **Taxonomia não é risk tier** — dois agentes podem ser `transactional` e receber tiers diferentes por operarem sobre dados, privilégios ou processos distintos.

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

**Evite taxonomia baseada em produto** ("agente da plataforma X"). O produto informa onde o agente foi construído, não o que ele pode fazer — e a taxonomia precisa sobreviver à troca de builder.

Para implementar a taxonomia, siga esta sequência:

1. **Selecione uma amostra representativa.** Inclua agentes citizen-built, SaaS, custom e pelo menos um agente com execução de ferramentas.
2. **Escolha somente dimensões que mudam uma decisão.** Uma dimensão só entra se alterar control, métrica, owner ou lifecycle.
3. **Defina códigos canônicos.** O critério deve ser operacional e independente da percepção do builder.
4. **Normalize por plataforma.** Documente como cada plataforma traduz seus campos para a taxonomia comum.
5. **Defina a obrigatoriedade por criticidade.** A classificação normativa T1–T4 está no [capítulo 04](04-risk-impact-and-compliance.md); o fast path de T1 reduz trabalho manual, mas não elimina registro, owner ou evidência.
6. **Calibre com casos reais.** Classifique 20–30 casos e meça concordância entre avaliadores. Divergência sistemática indica definição fraca, não avaliador fraco.
7. **Implemente nos consumidores.** Registry, pre-screen, dashboards e blueprint devem usar os mesmos códigos. **Taxonomia que vive somente em documento não gera governança.**

### 2.3 Registry: capacidades mínimas e campos obrigatórios

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

Obrigatoriedade por tier:

| Campo | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| owner | obrigatório | dual (business + technical) | dual + delegado | sponsor executivo + owners accountable |
| tier e admissibilidade | ambos obrigatórios | ambos obrigatórios | ambos + reassessment | ambos + authority compatível; exceção somente se `restricted` |
| dados e tools | lista | lista + classificação | lista + constraints + evidência | constraints e lineage críticos completos |
| identidade | definida | identidade própria | identidade própria + policy reforçada | identidade dedicada, isolamento e dual control |
| observabilidade | padrão | completa | completa + baseline de comportamento | monitoramento e containment reforçados |
| attestation | periódica | periódica | frequente ou orientada a evento | orientada a evento e executive review |

O fast path de T1 existe para reduzir input manual em alto volume, **não** para dispensar registro: descoberta, owner, logging e fontes aprovadas continuam obrigatórios.

### 2.4 Regras de qualidade que geram finding

O registry só é controle quando detecta continuamente que deixou de representar a realidade. O objetivo não é ter uma lista perfeita. Findings típicos:

- owner inexistente ou inativo;
- tier ausente ou expirado após mudança material;
- `last_seen` incompatível com o estado de lifecycle;
- ferramenta ou fonte de dados referenciada que não existe no catálogo;
- agente em produção sem perfil de telemetria ou sem kill switch quando exigido;
- attestation vencida;
- identidade compartilhada entre múltiplos agentes T2/T3 sem exceção aprovada;
- agente descoberto sem owner — recebe status `unmanaged` e entra em remediação.

**Reconciliação automatizada e manual detecta registros ausentes, obsoletos, duplicados e inválidos e bloqueia transições exigidas.**

### 2.5 Blueprint machine-readable

O blueprint é o contrato entre design, desenvolvimento, governança, CI/CD e runtime. Machine-readable significa que os campos relevantes podem ser interpretados por automação para gerar policy checks, verificar o baseline do tier e comparar drift entre configuração aprovada e runtime. Isso não exige que toda a governança esteja em YAML: decisões narrativas, impact assessments e risk acceptance continuam como evidências **referenciadas** pelo blueprint. Os contratos canônicos são o [Agent Registry schema](../../toolkit/schemas/agent-registry.schema.json) e o [Agent Blueprint schema](../../toolkit/schemas/agent-blueprint.schema.json).

Para implementar o blueprint machine-readable, siga esta sequência:

1. **Defina o contrato lógico.** Inclua somente campos que tenham consumidor real; schema grande sem consumidor é dívida.
2. **Versione e valide.** Use um formato versionável e valide contra o [Agent Blueprint schema](../../toolkit/schemas/agent-blueprint.schema.json).
3. **Vincule identidade e versão.** Associe o blueprint a `agent_id` e versão. Alterar o blueprint não pode sobrescrever silenciosamente a evidência de releases anteriores.
4. **Valide dependências.** Em build ou release, confirme que IDs de fontes, tools e modelos existem nos catálogos aprovados.
5. **Gere ou verifique configuração.** Use o blueprint para comparar o desired state com a configuração implantada, sem transformá-lo em substituto de decisões narrativas.
6. **Compare com o runtime.** Drift material produz finding e, se alterar risco ou admissibilidade, reassessment.
7. **Evolua por caso real.** Comece com dois ou três patterns e só amplie o schema quando houver consumidor e evidência de necessidade.

### 2.6 Ownership e accountability

Cada ativo é vinculado a owners **ativos** de negócio, técnico e operacional, com regra de sucessão: identificadores de papel, data de aceite, delegados, unidade organizacional, status e evidência de detecção de órfãos. **Saída ou inatividade do owner dispara redesignação, suspensão ou aposentadoria antes de o registro tornar-se órfão.**

### 2.7 O dossiê do agente: os artefatos que o acompanham

Até aqui, cada seção apresentou uma peça. Esta seção mostra o conjunto — porque a pergunta que mais importa na prática é simples: **"o que preciso juntar para governar UM agente?"**

**Dossiê do agente** é o nome que damos ao conjunto de artefatos vinculados por um único `agent_id`, do primeiro registro ao sunset. Não é um documento novo: é o agrupamento explícito do que o framework já define em capítulos e arquivos separados. Um leitor que percorre o framework capítulo a capítulo descobre cada peça; o dossiê é a visão "um agente, um pacote" que torna isso concreto.

| # | Artefato | Nasce quando | O que prova | Onde está definido |
|---|---|---|---|---|
| 1 | **Use-case intake** | ideia/demanda | o problema, por que agente, sinais de risco, duplicidade | [template](../../toolkit/templates/use-case-intake.md), seção 3 |
| 2 | **Autoavaliação** | antes da primeira aprovação | objetivo, dados, autonomia, controles e testes declarados | [template](../../toolkit/templates/self-assessment-form.md) |
| 3 | **Risk record** | classificação | tier, red flags, admissibilidade, residual risk aceito | [template](../../toolkit/templates/agent-risk-record.md), cap. 04 |
| 4 | **Registry entry** | primeiro registro | identidade, owners, lifecycle, tier, blueprint atual | [schema](../../toolkit/schemas/agent-registry.schema.json), seção 2 |
| 5 | **Blueprint** | design aprovado | contrato técnico da versão: architecture, models, data, identity, tools, runtime, governance | [schema](../../toolkit/schemas/agent-blueprint.schema.json), seção 2.5 |
| 6 | **RAI impact assessment** | quando o impact trigger dispara | impacto sobre pessoas, mitigação, residual impact | cap. 04, seção 2 |
| 7 | **Release evidence pack** | no gate de publicação | testes, MPB, evidências recuperáveis, decisão | [schema](../../toolkit/schemas/release-evidence-manifest.schema.json), cap. 07 |
| 8 | **Registros de vida operacional** | em operação | mudanças, attestations, incidentes, sunset | cap. 09 e cap. 05 |

**Como as peças se conectam:** o `agent_id` é o elo. O blueprint carrega `assessmentRefs`, `controlIds` e `releaseEvidenceRef`; o registry carrega `currentBlueprint` e `evidenceLinks`; o risk record referencia o pre-screen e a decisão. **Nada no dossiê flutua solto: todo artefato referencia o agente, e os artefatos entre si.**

**Por que isso importa:**

- **Para o owner:** uma lista de pendências com nomes. "Falta o risk record e o evidence pack" é uma instrução executável; "a governança está incompleta" não é.
- **Para o auditor:** um mapa do que deveria existir para cada agente — a ausência de qualquer peça é um finding com nome.
- **Para a automação:** o que é referenciável é verificável. O [score de prontidão](07-evaluation-evidence-and-assurance.md) do cap. 07 pontua exatamente este conjunto — completeza por peça, com itens críticos bloqueadores.
- **Para o legacy:** agente herdado que não tem dossiê começa a ser reconstruído pelo mesmo caminho (processo P1 do cap. 08), peça a peça, com `missing` explícito onde a evidência não existe.

**Armadilhas comuns:**

- **Confundir dossiê com um formulário único.** Não existe "o documento do agente" — existe o pacote vinculado. Fundir tudo num PDF mata a referenciabilidade e a automação.
- **Dossiê completo com peças contraditórias.** Registry diz T1, blueprint diz T3: o dossiê não está pronto — está inconsistente. A reconciliação entre peças é parte do gate.
- **Reconstruir evidência para o dossiê.** As peças nascem dos processos (o eval gera o relatório, o gate gera o decision record). Montar evidência depois, para satisfazer auditoria, custa mais e vale menos.
- **Dossiê que nunca fecha.** Peças pendentes com owner e prazo são operação normal; peças pendentes sem prazo são dívida de governança acumulando.

> **Artefatos para produzir agora — inventário, registry e blueprint.** Comece pelo [template de registry](../../toolkit/templates/agent-registry-template.md) e seu [schema](../../toolkit/schemas/agent-registry.schema.json) para registrar existência, owner, lifecycle e confidence. Quando o agente estiver suficientemente definido, use o [template de blueprint](../../toolkit/templates/agent-blueprint-template.md) e seu [schema](../../toolkit/schemas/agent-blueprint.schema.json) para descrever a configuração desejada. Os [casos fictícios](../../toolkit/examples/cases/README.md) mostram como essas peças se relacionam; o [catálogo de artefatos](../../toolkit/artifact-catalog.md) mostra quando cada uma precisa existir.

## 3. Decidir o que construir: intake e adequação

### 3.1 Intake de nova demanda

O ciclo começa antes de existir qualquer agente: capturar o problema, o mecanismo proposto, o owner e a necessidade de decisão **antes** de iniciar o design. O registro de intake inclui finalidade, baseline, usuários, pessoas afetadas, dados, ações, alternativas e urgência. A solicitação é encaminhada às decisões de adequação, risco e portfólio sem ignorar verificações de ownership ou escopo.

### 3.2 Adequação: agente é o mecanismo certo?

O primeiro gate não é "qual plataforma usar". É **"precisamos mesmo de um agente?"**. Comportamento agentic aumenta variabilidade, custo de observabilidade e superfície de risco. Deve existir uma razão explícita para introduzir autonomia ou raciocínio probabilístico — registrada, não pressuposta. Processos determinísticos, estáveis e integralmente especificáveis costumam ser melhor atendidos por workflow, automação tradicional ou uma chamada de API.

Percorra a árvore na ordem — cada resposta muda o que precisa ser desenhado, não apenas o que precisa ser aprovado:

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
Aciona o impact trigger screen e, quando aplicável, o [impact assessment](04-risk-impact-and-compliance.md#2-avaliacao-de-impacto-responsible-ai).

**8. Onde cada controle vai residir?**
Management plane, gateway de runtime, broker de ferramentas, IAM, plataforma de dados, aplicação ou processo humano. **Não concentre controle no prompt** — prompt é instrução, não enforcement.

Exemplos de decisão:

| Caso | Decisão arquitetural | Por quê |
|---|---|---|
| assistente de conhecimento | recuperação somente leitura, identidade delegada, fontes certificadas, sem ferramenta de escrita | o valor vem de interpretação e recuperação; ação transacional seria risco sem benefício |
| agente de service desk | identidade própria, catálogo de ferramentas para criar e atualizar chamados, rollback e telemetria | há escrita reversível e operação multiusuário; a atribuição precisa sobreviver à ausência do usuário |
| agente de contas a pagar | identidade própria, broker de ferramentas, serviço de aprovação para pagamento, segregação de funções | o escalador financeiro impede execução autônoma irrestrita |
| agente de operações de produção | control plane de runtime, mediação de ferramenta privilegiada, remediações pré-aprovadas, circuit breaker | **a ferramenta é mais crítica que o modelo**; o comando precisa ser autorizado fora do modelo |

O último caso é o mais instrutivo: quando a ferramenta é privilegiada, a discussão sobre qual modelo usar é secundária. O controle está na autorização da ação, não na qualidade do raciocínio.

**Onde registrar:** a decisão vai no intake do caso de uso e, quando arquiteturalmente relevante, num ADR. Se a resposta for "não precisamos de agente", **registre assim mesmo** — decisão de não construir é a mais barata do portfólio e a que menos costuma ser documentada, o que faz a mesma discussão voltar seis meses depois.

### 3.3 Procurement e terceiros

Aplicar governança **equivalente** a agentes construídos, comprados, configurados, SaaS, low-code e operados por fornecedores: fornecedor, fronteira de serviço, deveres contratuais, evidências fornecidas, subprocessadores, direitos de saída, owner e lacunas não resolvidas. **A terceirização não remove a accountability**, e uma alegação de fornecedor sem evidência não pode satisfazer um controle bloqueante.

## 4. Medir e decidir valor: portfólio

### 4.1 Cadeia de valor: cada seta é uma hipótese

```text
Problema observado
  → hipótese de intervenção
  → capability do agente
  → mudança de comportamento/processo
  → output mensurável
  → outcome
  → impacto, custo e efeitos colaterais
```

Cada seta é uma hipótese que precisa de evidência. **Um bom output pode não gerar outcome; um outcome pode ter outras causas.** Valor não pode ser inferido a partir de volume, uso ou narrativa de fornecedor.

### 4.2 Business case mínimo

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

**Hipótese mensurável:** definir um resultado falseável, baseline pré-mudança e contrafactual crível com corte de evidências. Registrar owner da métrica, população, fórmula, alvo, fonte, confounders, custo e threshold de decisão. A authority precisa distinguir criação, adoção, qualidade e resultado — e poder **interromper o trabalho quando a evidência não suporta expansão**.

### 4.3 Métricas separadas: não agregue camadas em um "score"

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

**Não agregue essas camadas em um único "AI adoption score" sem preservar significado.** A medição de custo por resultado está em [FinOps e unit economics](10-metrics-review-and-improvement.md); a separação entre KPI, KRI e métrica operacional está em [KPIs, KRIs e governance dashboard](10-metrics-review-and-improvement.md).

### 4.4 Baseline e atribuição: não atribua o que você não mediu

- medir o processo antes ou reconstruir baseline com limitações declaradas;
- comparar grupos, períodos ou tarefas equivalentes quando possível;
- registrar outras mudanças que afetam o outcome;
- distinguir correlação de causalidade;
- incluir custo de revisão humana, suporte e incidentes;
- comunicar intervalo, incerteza e qualidade do dado.

### 4.5 Portfolio governance e value review

O artefato que carrega o portfólio é o [Agent Use-Case Portfolio](../../toolkit/templates/use-case-portfolio.md): use case, sponsor, owner, tier, admissibilidade, status, valor esperado, valor observado, custo e flag de duplicidade. Ele responde "isso deveria continuar existindo", enquanto o [registry](03-inventory-portfolio-and-value.md) responde "o que existe e quem responde por isso".

Decisões de portfólio consideram: alinhamento estratégico; valor esperado e evidence strength; risco e residual impact; duplicidade e reuse; dependências e concentração; custo total e capacidade operacional; timing e reversibilidade; opportunity cost.

| Decisão | Condição típica |
|---|---|
| manter | outcome e risco dentro do envelope |
| expandir | evidência suficiente, controls escaláveis e demanda legítima |
| corrigir | valor plausível, mas quality/control gap tratável |
| restringir | risco ou incerteza exige menor scope |
| substituir | alternativa entrega melhor relação valor-risco-custo |
| aposentar | sem owner, sem uso, sem outcome ou risco/custo injustificável |

**A priorização usa evidência de valor, risco, dependência, reuso e capacidade — não preferência do sponsor.** A authority de portfólio consegue financiar, pausar, mesclar, restringir ou aposentar itens, e a decisão propaga-se aos registros de lifecycle.

### 4.6 Custo, consumo e FinOps

Atribuir consumo e custo operacional total a agente, owner, ambiente e resultado mensurável: custo unitário, orçamento, quota, previsão, variância, alocação de custo compartilhado, anomalia e decisão de otimização. **Todo agente em produção (≥10 usuários) deve ter budget (cap) definido pelo business owner, com alertas e re-aprovação quando thresholds são excedidos**; monitorar consumo (tokens, chamadas, minutos de GPU) e custo mensal; **bloquear em caso de abuso/anomalia**. Violação de threshold dispara throttling ou revisão. **Alegações de custo permanecem separadas de alegações de realização de valor.**

### 4.7 Adoção e utilização

Medir adoção pretendida, uso significativo e comportamento de workaround inseguro por população-alvo: população elegível, uso ativo, conclusão de tarefa, abandono, demanda de suporte, feedback e limitações de amostragem. O owner deve distinguir **disponibilidade de adoção útil** e poder mudar treinamento, design ou rollout com base em evidência.

> **Armadilha comum:** premiar volume e criar agent sprawl; horas "economizadas" sem medir qualidade ou deslocamento de trabalho; manter agente porque já foi construído; ROI calculado com adoção projetada como fato.

## 5. Referência normativa

Condições mínimas que devem ser verdadeiras em cada ponto. Use como checklist de implementação e auditoria; as seções 1–4 explicam o porquê de cada item.

| # | Obrigação | Evidência mínima | Concluído quando |
|---|---|---|---|
| R1 | Descobrir ativos implantados, experimentais, embarcados e de fornecedores por múltiplas fontes reconciliadas | fonte de descoberta, última visualização, confiança, correspondência de owner, identidade não resolvida, status de remediação | ativos sem owner ou shadow entram em contenção e resolução de ownership |
| R2 | Operar o registry como índice autoritativo de identidade e lifecycle de todo agente em escopo | ID estável, owner, finalidade, tier, admissibilidade, versão, ambiente, estado, dependências, último attestation | reconciliação detecta registros ausentes/obsoletos/duplicados/inválidos e bloqueia transições exigidas |
| R3 | Vincular cada ativo a owners ativos (negócio, técnico, operacional) com regra de sucessão | identificadores de papel, data de aceite, delegados, unidade organizacional, status, detecção de órfãos | saída/inatividade do owner dispara redesignação, suspensão ou aposentadoria antes de tornar-se órfão |
| R4 | Documentar finalidade pretendida, usuários, não usuários afetados, usos excluídos e escala previsível | declaração do caso de uso, análise de stakeholders, grupos afetados, ambiente, volume, premissas | avaliação e monitoramento cobrem a população efetivamente afetada |
| R5 | Enumerar toda dependência governada e a authority herdada por cada conexão | blueprint referenciando registros aprovados de modelo, fonte, ferramenta, integração e fornecedor | dependência não registrada/incompatível impede promoção; mudança material dispara reavaliação |
| R6 | Manter identidade consistente entre ambientes separando configuração, authority e estado | ambiente, release, hashes de artefato, configuração implantada, estado, fonte de promoção, alvo de rollback | operadores reconciliam estado desejado/observado e não confundem aprovação de teste com produção |
| R7 | Capturar problema, mecanismo, owner e necessidade de decisão antes do design | registro de intake com finalidade, baseline, usuários, afetados, dados, ações, alternativas, urgência | solicitação encaminhada às decisões de adequação, risco e portfólio sem ignorar ownership/escopo |
| R8 | Comparar agente com alternativas determinísticas e não técnicas | alternativas, necessidade de autonomia, incerteza, benefício esperado, custo de falha, decisão arquitetural | agente prossegue somente com capacidade distintiva necessária e ônus de governança aceito |
| R9 | Definir resultado falseável, baseline pré-mudança e contrafactual crível | owner da métrica, população, fórmula, alvo, fonte, confounders, custo, threshold de decisão | authority distingue criação/adoção/qualidade/resultado e interrompe quando evidência não suporta expansão |
| R10 | Priorizar portfólio por evidência de valor, risco, dependência, reuso e capacidade | pontuações comparáveis, capacidades duplicadas, serviços compartilhados, restrições, decisão, data de revisão | authority financia/pausa/mescla/restringe/aposenta e decisão propaga-se ao lifecycle |
| R11 | Atribuir consumo e custo total a agente, owner, ambiente e resultado | custo unitário, orçamento, quota, previsão, variância, alocação compartilhada, anomalia, otimização | threshold violado dispara throttling/revisão; custo separado de valor |
| R12 | Medir adoção pretendida, uso significativo e workaround inseguro por população-alvo | população elegível, uso ativo, conclusão, abandono, suporte, feedback, limitações de amostragem | owner distingue disponibilidade de adoção útil e muda treinamento/design/rollout por evidência |
| R13 | Aplicar governança equivalente a agentes comprados, configurados, SaaS, low-code e de fornecedores | fornecedor, fronteira de serviço, deveres contratuais, evidências fornecidas, subprocessadores, saída, owner, lacunas | terceirização não remove accountability; alegação sem evidência não satisfaz controle bloqueante |
| R14 | Tornar a capacidade de inventário/portfólio autoritativa para todos os agentes em escopo | registry/portfólio com owner, finalidade, usuários, dependências, estado, hipótese de valor, data da evidência, qualidade dos dados | reconciliação detecta ativos sem owner/ausentes e authority decide financiar/reusar/restringir/consolidar/aposentar |

## 6. Decision gates

- **Descoberta:** o baseline só é aceito com data de corte, cobertura mensurável por fonte, gaps registrados com owner e distribuições de status e confidence declaradas separadamente. **Cobertura desconhecida é gap crítico, não ausência de risco.**
- **Registry:** nenhum agente é construído em ambiente compartilhado ou publicado sem `agent_id`, owner, tier e admissibilidade registrados. Nenhum agente permanece em produção sem stage/operational state coerentes ou com quality finding crítico aberto.
- **Portfólio:** nenhum item entra no portfólio financiado sem problema, owner, baseline (ou plano explícito para obtê-lo), value hypothesis, costs, metrics e sunset criteria.

## 7. Artefatos, evidências, métricas e failure modes

**Artefatos**
- Agent Estate Inventory com confiança e data de corte;
- [Agent Registry schema](../../toolkit/schemas/agent-registry.schema.json) e [exemplo estruturado](../../toolkit/examples/agent-registry.example.json);
- [Agent Blueprint schema](../../toolkit/schemas/agent-blueprint.schema.json) e [exemplo estruturado](../../toolkit/examples/agent-blueprint.example.json);
- [template de registry](../../toolkit/templates/agent-registry-template.md) e [template de blueprint](../../toolkit/templates/agent-blueprint-template.md);
- Agent Estate Forecast em três cenários, com mix de risco;
- Manual Bottleneck Register priorizado;
- [Agent Use-Case Portfolio](../../toolkit/templates/use-case-portfolio.md).

**Evidências**
- registro autoritativo com owners, tier e estado por agente;
- histórico de reconciliação entre registry e plataformas de origem;
- baseline com data de corte e distribuição de confiança;
- backlog de remediação de objetos `probable` e `suspected`;
- blueprint versionado por release, com evidence refs;
- relatórios de drift entre desired state e runtime;
- business case, metric definitions, cost model;
- adoption/quality/outcome reports e portfolio decisions.

**Métricas**
- agentes descobertos sem owner (`unmanaged`) e tempo até remediação;
- cobertura do registry contra fontes independentes;
- campos obrigatórios vazios por tier; referências quebradas;
- drift material entre blueprint e runtime;
- proporção `confirmed`/`probable`/`suspected` ao longo do tempo;
- shadow agents encontrados por ciclo de redescoberta;
- desvio entre forecast e estate real; gargalos manuais eliminados por trimestre;
- itens sem business owner ou baseline; duplicated capabilities;
- custo por outcome e por tier; time-to-decision para corrigir ou aposentar.

**Failure modes**
- registry como planilha mestre que ninguém reconcilia;
- taxonomia derivada de produto em vez de comportamento;
- inventário completo sem quality rules — lista bonita, controle zero;
- blueprint gigante sem consumidor automatizado;
- sobrescrever o blueprint aprovado ao publicar nova versão;
- tratar descoberta como projeto de inventário pontual;
- descartar sinais incertos para não "poluir" a métrica;
- contar versões e instâncias como agentes distintos;
- forecast apresentado como previsão contratual;
- projetar volume sem projetar mix de risco;
- automatizar decisões antes de estabilizar a policy;
- valor inferido por número de agentes;
- horas "economizadas" sem medir qualidade;
- ROI com adoção projetada como fato;
- ignorar custo de assurance e suporte;
- manter agente porque já foi construído;
- atribuir outcome ao agente sem baseline;
- premiar volume e criar agent sprawl;
- esconder externalities negativas.

## Acceptance criteria

- todas as decisões deste capítulo possuem authority, owner e evidência recuperável;
- requisitos aplicáveis estão ligados ao catálogo de controles e ao método de verificação;
- exceções têm escopo, justificativa, compensating controls, expiry e decisão residual;
- controles de build time e runtime são distinguidos e exercitados quando aplicáveis;
- mudanças materiais reabrem avaliação, aprovação e evidência;
- nenhuma alegação de conformidade, eficácia ou valor excede a evidência observada.

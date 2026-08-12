---
title: Tailoring Guide
status: maintained
last_reviewed: 2026-08-11
review_cycle: quarterly
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# Tailoring Guide

Este artefato consolida fontes validadas segundo a estratégia registrada no plano de migração. A união preserva conteúdo único e registra a origem de cada bloco.

## Fonte: `docs/guides/capability-map.md`

> **Provenance:** migrated from `docs/guides/capability-map.md` at authoritative commit `5545d9227624400ab8bb707b6032b2f61329a36e`. Content is adapted only for repository boundaries and links.

### Capability map — atual versus alvo

#### Objetivo

Separar **o que a organização precisa saber fazer** de **qual ferramenta vai implementar**. O capability map existe para evitar o erro mais caro de um programa de governança: comprar tecnologia para um problema que é, na verdade, ausência de processo, ownership, dados ou decision rights.

#### O que é uma capability

Uma capacidade organizacional de produzir um resultado **de forma repetível**. Não é uma ferramenta, um time nem um projeto.

"Agent registry" é uma capability quando a empresa consegue descobrir, registrar, manter e consultar agentes com qualidade conhecida. Uma plataforma pode implementar parte dela — não é ela.

O teste: se você trocar o produto e a capacidade desaparecer, você comprou uma ferramenta e chamou de capability.

#### As capacidades do framework

Ponto de partida: os [domínios canônicos](../framework/06-architecture-and-technical-controls.md#domínios-canônicos-por-plano). Quebre uma capability em duas apenas quando a filha tiver owner, processo **ou** evidência diferentes.

| Capacidade | Pergunta de diagnóstico | Sinal típico de estado inicial | Alvo comum |
| --- | --- | --- | --- |
| estratégia e governança | existe mandato, portfólio, funding e decisão clara? | política genérica de IA, sem charter ou priorização de agentes | charter aprovado, fóruns, decision rights, risk appetite e portfolio review |
| estate inventory e registry | sabemos quais agentes existem, onde operam e quem responde? | planilhas por plataforma e baixa cobertura de shadow agents | discovery contínuo + registry corporativo reconciliável |
| risco e Responsible AI | risco, admissibilidade e impacto roteiam controles? | mesma review para todos os casos | tiers, admissibilidade, escaladores e impact assessment por gatilho |
| lifecycle e Agent SDLC | versões, estados e mudanças estão governados? | publicação ad hoc e approvals permanentes | stage/state, gates, transition history, attestation e retirada |
| identidade e acesso | cada ação é atribuível e autorizada? | chaves e contas de serviço compartilhadas | identidade própria por agente, least privilege, JML e delegação quando aplicável |
| dados e conhecimento | as fontes são classificadas, permitidas e AI-ready? | recuperação sobre qualquer pasta autorizada | catálogo de fontes certificadas com lineage, restrictions e recertification |
| tools, APIs e MCP | as ações são catalogadas, limitadas e mediadas? | ferramentas embutidas por time | enterprise tool registry, gateway e autorização por ação/parâmetro |
| modelos e provedores | combinações e versões possuem critérios de admissão e saída? | escolha por preferência do time | catálogo provider/model/version, evaluation binding, fallback e exit strategy |
| runtime e plataforma | existem enforcement, isolamento, resiliência e rollback? | acesso direto a endpoints e configuração por agente | control plane, policy enforcement, budgets, containment e recovery patterns |
| segurança e AgentSecOps | ameaças agentic entram em prevention, detection e response? | SOC vê apenas logs tradicionais | threat model agentic, red teaming, supply-chain controls e incident integration |
| observabilidade e behavioral analytics | é possível reconstruir, detectar desvio e agir? | logs de aplicação sem correlation ou owner action | event envelope, traces, baselines, thresholds, runbooks e feedback loop |
| FinOps | custo é atribuível a agente, tarefa e outcome? | custo por chave ou centro de custo agregado | budgets, unit economics, anomaly response e arquitetura guiada por custo/qualidade |
| value realization | outcomes influenciam funding, expansão e sunset? | contagem de agentes e relatos de benefício | baseline, KPI, attribution caveats e portfolio decisions por evidência |
| assurance e auditabilidade | controls e decisões podem ser testados por challenge apropriado? | evidence preparada manualmente para auditoria | continuous evidence, segregation, sampling, findings e assurance proporcional |
| adoção, suporte e competências | cada papel consegue usar a rota governada corretamente? | treinamento pontual e suporte informal | currículo por papel, champions, support model e feedback incorporado aos standards |

#### Crosswalk para maturity e controls

O framework mantém **15 capabilities** para planejamento porque elas podem ter owners, processos e evidências diferentes. O [maturity model](../../toolkit/maturity/maturity-model.md) agrega essas capacidades em dez dimensões para scoring; agregação de score não funde accountability.

| Capability | Dimensão(ões) do maturity model | Domínios de controls principais |
| --- | --- | --- |
| estratégia e governança | 1. Estratégia, portfólio e valor; 2. Policy, operating model e decision rights | `organization`, `value` |
| estate inventory e registry | 3. Registry, blueprint e lifecycle | `registry` |
| risco e Responsible AI | 7. Risco, Responsible AI e human oversight | `risk`, `responsible-ai` |
| lifecycle e Agent SDLC | 3. Registry, blueprint e lifecycle; 8. Evaluations e release | `lifecycle`, `registry`, `evaluation` |
| identidade e acesso | 4. Identidade e acesso | `identity` |
| dados e conhecimento | 5. Dados e connectors | `data` |
| tools, APIs e MCP | 6. Tools, APIs e MCP | `tools` |
| modelos e provedores | 8. Evaluations e release | `model`, `evaluation` |
| runtime e plataforma | 9. Auditabilidade e operações | `operations`, `security` |
| segurança e AgentSecOps | 6. Tools, APIs e MCP; 9. Auditabilidade e operações | `security`, `tools`, `audit` |
| observabilidade e behavioral analytics | 9. Auditabilidade e operações | `audit`, `operations` |
| FinOps | 1. Estratégia, portfólio e valor; 9. Auditabilidade e operações | `value`, `operations` |
| value realization | 1. Estratégia, portfólio e valor | `value` |
| assurance e auditabilidade | 2, 7, 8 e 9 | `organization`, `audit`, `evaluation`, `risk` |
| adoção, suporte e competências | 10. Adoção, suporte e competência | `adoption` |

Use o crosswalk para navegar, não para declarar equivalência um-para-um. Uma capability pode depender de vários domínios, e um control pode contribuir para mais de uma capability.

#### Procedimento

1. **Listar as capacidades** necessárias ao operating model.
2. **Escrever uma frase de outcome** para cada uma. Exemplo: *"toda ação material de agente é atribuível a uma identidade conhecida e autorizada"*.
3. **Definir evidências observáveis do estado atual.** Evite "o controle de acesso é forte". Prefira: *"74% dos T2/T3 usam identidade dedicada; 26% usam chave compartilhada"*.
4. **Atribuir maturidade com base em evidência** e registrar confidence. Evidência fraca produz nota provisória, não nota otimista.
5. **Definir o alvo por horizonte e necessidade de negócio.** Nem toda capacidade precisa do nível máximo; nível 3 costuma bastar no primeiro ano.
6. **Identificar dependências.** Behavioral analytics confiável depende de identidade própria e telemetria consistente — priorizá-la antes disso desperdiça o investimento.
7. **Converter gaps materiais em iniciativas** do roadmap de maturidade.

#### Exemplo

| Capability | Estado atual observado | Alvo 12m | Gap concreto | Iniciativa |
|---|---|---|---|---|
| identidade | chaves compartilhadas; owner não rastreável em 30% dos agentes transacionais | 100% de T2/T3 com identidade própria, JML e rotação | atribuição, lifecycle e least privilege insuficientes | padrão de identidade + onboarding + automação de JML |
| tools e MCP | ferramentas embutidas por time, sem catálogo nem classificação de ação | ferramentas críticas registradas, classificadas e mediadas | sem visão da capacidade executável nem do risco por ação | tool registry + broker + autorização por parâmetro |
| observabilidade | logs de aplicação; custo por chave; sem correlação agente-tarefa-ferramenta | schema de telemetria e dashboards por decisão | impossível investigar um agente ou medir custo por resultado | schema + correlation IDs + pipeline |

Repare no primeiro: o gap **não é "comprar IAM"**. É identidade não humana por agente, least privilege, lifecycle de owner, gestão de secrets e auditabilidade. Nenhum produto entrega isso sozinho.

#### Perguntas de challenge

Aplique antes de aprovar o alvo:

- o alvo é necessário para o risco e o volume previstos, ou está sendo escolhido por ambição tecnológica?
- existe dependência invisível em outra capacidade que pode bloquear a iniciativa?
- o alvo pode ser demonstrado por evidência objetiva?
- **existe owner capaz de sustentar a capacidade depois que o programa terminar?**

A última derruba mais iniciativas que as outras três somadas.

#### Relação com o maturity model

O capability map responde "o que precisamos saber fazer e onde estamos". O [maturity model](../../toolkit/maturity/maturity-model.md) fornece a escala, as âncoras de confidence e o método de avaliação por evidência. O [roadmap de maturidade](../../toolkit/examples/target-maturity-roadmap.example.md) converte os gaps em sequência.

Usar o capability map sem o método de assessment produz nota por percepção — que é o antipattern que o maturity model existe para evitar.

#### Failure modes

- mapear produtos e chamar de capacidades;
- quebrar capacidades até virarem tarefas, perdendo o nível de decisão;
- alvo máximo em tudo, ignorando dependência e capacidade operacional;
- estado atual descrito por adjetivo em vez de medida;
- ignorar que uma capacidade em nível baixo pode inutilizar outra em nível alto;
- aprovar alvo sem owner que o sustente depois do programa.


## Fonte: `docs/guides/implementation-plan-90-days.md`

> **Provenance:** migrated from `docs/guides/implementation-plan-90-days.md` at authoritative commit `5545d9227624400ab8bb707b6032b2f61329a36e`. Content is adapted only for repository boundaries and links.

### Roadmap de implantação — 90 dias

> **Referência acelerada, não SLA.** Os 90 dias ajudam equipes que precisam de uma sequência inicial. Adapte duração e sobreposição às dependências, ao estate e à capacidade da organização. O calendário nunca substitui G0–G7 nem cria obrigação de piloto.

#### Objetivo

Estabelecer, em 90 dias, as fundações e os fluxos mínimos de um sistema de governança operável: mandato, baseline, registry, blueprint, tiers, decision rights, controls, release evidence, runtime response e roadmap priorizado.

O resultado não é “governança concluída”. É uma capacidade inicial verificável que pode ser ampliada sem perder accountability ou rastreabilidade.

#### Constraints

- A policy modular é a fonte canônica; adoção organizacional requer release e authority explícitas.
- Core e controls são multiplataforma.
- Thresholds são aprovados no contexto da organização.
- Dados, identidade, segurança, privacy, legal e RAI mantêm suas authorities.
- Automação é aplicada somente a regras estáveis e testadas.
- Lacuna de evidência permanece visível; não é preenchida por suposição.
- Este roadmap não exige piloto: uma coorte de onboarding ou rollout controlado delimita o primeiro escopo operacional e usa os mesmos gates, controls e critérios de produção.

#### Mapeamento entre calendário e gates

Os períodos abaixo organizam trabalho; os gates continuam sendo decisões independentes. Chegar ao último dia de uma fase não autoriza avanço automático.

| Período | Gates preparados ou decididos | Decisão esperada |
|---|---|---|
| dias 0–10 | G0 | aprovar, condicionar, suspender ou rejeitar mandato e scope |
| dias 11–25 | G1 | aceitar baseline e limitações ou exigir evidência/remediação |
| dias 26–40 | G2 | aceitar fundações mínimas ou bloquear onboarding |
| dias 41–55 | G3 e preparação de G4 | aprovar decision rights e autorizar desenho da baseline de controls |
| dias 56–70 | G4 e preparação de G5 | aceitar baseline/assurance e decidir readiness para release |
| dias 71–85 | G5 e G6 | decidir release condicionado ao tier e aceitar operação/containment |
| dias 86–90 | G7 | decidir continuidade, restrição, expansão, remediação ou sunset |

O [contrato comum dos gates](../framework/08-implementation-and-adoption.md#contrato-comum-dos-decision-gates) define evidence mínima, authority, estados e caminho de falha. Uma decisão `hold` ou `reject` altera o plano; o calendário deve ser replanejado, não usado para contornar o gate.

#### Dias 0–10 — Mandato e escopo

##### Atividades

- nomear sponsor, governance owner e authorities iniciais;
- aprovar escopo organizacional e ambientes;
- definir risk appetite, red flags e autoridade de containment;
- mapear policies, processos, inventários e ferramentas existentes;
- selecionar um portfólio inicial representativo para onboarding controlado;
- registrar decisões e dependências.

##### Entregáveis

- governance charter;
- scope e stakeholder map;
- authority matrix inicial;
- risk appetite v0.1;
- decision/risk log.

##### Exit criteria

- sponsor e owners nominativos;
- scope explícito;
- containment authority definida;
- nenhuma lacuna crítica sem owner.

#### Dias 11–25 — Diagnóstico e baseline

##### Atividades

- aplicar maturity assessment;
- reconciliar inventários de plataformas;
- mapear lifecycle e handoffs reais;
- identificar ownerless, duplicados, inativos e high-risk unknowns;
- avaliar qualidade da evidência;
- priorizar gaps por impacto, dependência e reversibilidade.

##### Entregáveis

- maturity baseline;
- current-state map;
- preliminary registry;
- gap/risk register;
- prioritized backlog.

##### Exit criteria

- situação atual separa observado de hipótese;
- inventário possui coverage declarado;
- gaps críticos e altos têm owner e prazo;

#### Dias 26–40 — Registry, blueprint, dados e identidade

##### Atividades

- aprovar schemas mínimos;
- definir source of truth e reconciliation;
- registrar business/technical owners e lifecycle;
- preencher blueprints do portfólio inicial;
- mapear workload identities e permissions;
- criar data contracts e connector gates;
- inventariar tools, APIs e MCP servers.

##### Entregáveis

- registry e blueprints versionados;
- identity/permission matrix;
- data contracts;
- tool/MCP registry;
- material-change triggers.

##### Exit criteria

- todos os itens do escopo inicial têm owner e status;
- identities, data e tools são rastreáveis;
- gaps aparecem como missing evidence.

#### Dias 41–55 — Operating model e controls

##### Atividades

- formalizar Council, Design Authority e Run Authority;
- definir RACI e decision rights por tier;
- aprovar risk tiers e red flags;
- mapear control catalog e evidence;
- definir exception/waiver e expiry;
- estabelecer forums, handoffs e SLAs.

##### Entregáveis

- target operating model;
- RACI e decision matrix;
- risk/control baseline;
- exception process;
- forum charter.

##### Exit criteria

- cada decisão material possui accountable;
- segregation of duties é proporcional;
- exceções não podem ser permanentes por padrão.

#### Dias 56–70 — Assurance, evaluations e release

##### Atividades

- definir triggers de assessments;
- criar evaluation strategy e thresholds;
- documentar human oversight e transparency;
- montar release evidence package;
- testar negative paths, rollback, quarantine e kill switch;
- registrar residual risk e conditions.

##### Entregáveis

- assessment suite;
- evaluation/release criteria;
- evidence package;
- run readiness checklist;
- drill records.

##### Exit criteria

- controls aplicáveis possuem evidence;
- release authority consegue aprovar, condicionar ou negar;
- containment e rollback foram exercitados.

#### Dias 71–85 — Onboarding, operação e suporte

##### Atividades

- colocar o workflow de onboarding em uso no escopo inicial;
- configurar telemetry, dashboards e alerts;
- publicar catalog entries, guidance e support paths;
- ligar incident, support e domain escalation;
- medir fricção, gaps e bypass attempts;
- corrigir controls e templates pelo processo versionado da policy modular.

##### Entregáveis

- onboarding workflow operacional;
- observability e runbooks;
- catalog/discovery;
- support model;
- remediation backlog.

##### Exit criteria

- cada signal possui owner e action;
- ações state-changing têm correlation;
- support e escalation funcionam ponta a ponta.

#### Dias 86–90 — Attestation e roadmap

##### Atividades

- executar primeira owner attestation do escopo;
- revisar criação, discovery, uso, qualidade e value hypothesis separadamente;
- registrar decisões de manter, corrigir, restringir ou aposentar;
- atualizar maturity baseline com evidência;
- aprovar roadmap de expansão e automation backlog.

##### Entregáveis

- attestation records;
- portfolio/value review;
- maturity delta com limitações;
- roadmap 6–12 meses;
- executive decision memo.

##### Exit criteria

- decisões ligadas a evidência;
- próximos increments possuem owner, dependency e acceptance criteria;
- nenhuma mudança normativa é autoaprovada.

#### Métricas dos 90 dias

##### Cobertura e controle

- coverage do registry;
- owners e attestations válidos;
- identities/connectors/tools classificados;
- evidence packages completos por tier;
- exceptions e findings vencidos;
- containment e rollback drill pass rate.

##### Fluxo

- cycle time por gate e tier;
- devoluções por evidência incompleta;
- time to decide/contain/remediate;
- bypass attempts e causes;
- suporte e escalation resolution time.

##### Uso, qualidade e valor

- discovery, adoption e use separados;
- task success e erro por scenario;
- safety/security signals;
- support burden;
- baseline e outcome evidence disponível;
- custo de operação e assurance.

#### Riscos de execução

| Risco | Mitigação |
|---|---|
| burocracia uniforme | tiering, paved road e forms proporcionais |
| catálogo decorativo | reconciliation, owners, lifecycle e actions |
| falso senso de coverage | declarar sources, missing evidence e confidence |
| centralização em silo | authorities distribuídas e handoffs |
| automação prematura | manual first para regras instáveis; automate after evidence |
| métricas de vaidade | separar criação, uso, qualidade e outcome |
| vendor lock-in | capabilities e schemas neutros; adapters separados |
| rollout sem containment | quarantine/rollback como exit criteria |

#### Próximo passo após 90 dias

Expandir coverage, automatizar controles estáveis, aprofundar domains com maior residual risk e revisar o roadmap. Uma futura Policy v2, se necessária, deve seguir processo formal de mudança e não é consequência automática deste roadmap.

---
title: 08 — Implementação e adoção
status: maintained
maturity: validated
last_reviewed: 2026-08-18
review_cycle: quarterly
owners: [framework-maintainers]
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# 08 — Implementação e adoção

## Visão geral

Este capítulo responde a pergunta prática que todos os outros preparam: **como uma organização sai do zero e chega à governança operando no dia a dia?**

A resposta tem três camadas:

1. **A jornada em 8 gates (G0–G7):** pontos de decisão com critérios, evidência e authority — o esqueleto da implantação.
2. **Dois roadmaps de referência:** 90 dias (acelerado) e 24 semanas (programa completo) — formas de organizar o calendário sem virar SLA.
3. **Adoção e suporte:** como cada papel aprende, usa e retroalimenta o sistema — porque governança que ninguém consegue executar não existe.

> **Decisão editorial desta release.** O capítulo 08 permanece como source of truth canônico para G0–G7, gate contract, dependency model, P1–P8 e princípios de adoption/support. O roadmap de 90 dias, o programa de 24 semanas e o pilot são guidance/patterns não normativos dentro do mesmo contexto; movê-los nesta rodada aumentaria fragmentação e criaria risco de duplicação. O `start-here`, o handbook e o Artifact Catalog apontam para este capítulo, e nenhuma dessas seções cria gate ou requirement adicional.

O aviso que atravessa tudo: **gates são decisões registradas, não nomes de fase.** Nenhum gate é concluído porque o prazo terminou ou um documento foi produzido. E o risco mais caro de um programa: **comprar tecnologia para um problema que é, na verdade, ausência de processo, ownership, dados ou decision rights.**

> **Artefatos para produzir agora — de acordo com o gate.** Use o [catálogo de artefatos](../../toolkit/artifact-catalog.md) como índice de completude. Para G0, comece pelo [Governance Charter](../../toolkit/templates/governance-charter-template.md); para G1, pelo [Capability Assessment Worksheet](../../toolkit/templates/capability-assessment-worksheet.md) e [Maturity Assessment](../../toolkit/templates/maturity-assessment-template.md); para G2, pelo [Registry](../../toolkit/templates/agent-registry-template.md) e [Blueprint](../../toolkit/templates/agent-blueprint-template.md); para G4/G5, pelo [Release Decision Checklist](../../toolkit/templates/release-decision-checklist.md) e [Release Evidence Manifest](../../toolkit/templates/release-evidence-manifest.md); para G7, pelo [Attestation and Sunset Record](../../toolkit/templates/attestation-sunset-record.md). O gate só existe quando a decisão, o owner e a evidência estão registrados.

## 1. A jornada em 8 gates

### 1.1 O contrato comum dos decision gates

Os gates são decisões registradas, não fases cronológicas. Workstreams podem avançar em paralelo, mas nenhum gate é concluído apenas porque o prazo terminou.

**Estados de decisão:**

| Estado | Significado | Requisito de registro |
|---|---|---|
| `approve` | critérios de saída atendidos para o escopo e versão avaliados | authority, data, versão e evidências aceitas |
| `condition` | avanço permitido com gap não crítico e compensação temporária | condição, owner, prazo, compensating control e expiry |
| `hold` | decisão suspensa por evidência insuficiente ou remediação necessária | finding, owner, ação, evidência esperada e nova data |
| `reject` | risco, desenho ou escopo não é aceitável no appetite vigente | rationale, authority, opções de redesign ou encerramento |

Todo decision record identifica: `gate_id`, escopo, versão, tier, authority, participantes, evidence refs, estado, rationale, condições, expiry e próxima revisão. **`Missing evidence` nunca equivale a aprovação.** A mesma pessoa não pode construir, aprovar e desafiar o próprio artefato quando segregação for exigida.

### 1.2 Os 8 gates em uma tabela

| Gate | Critérios de entrada | Evidência mínima | Authority da decisão | Critérios de saída | Falha e remediação |
|---|---|---|---|---|---|
| **G0 — Mandato** | sponsor candidato, problema e boundary inicial | draft de charter, scope, authorities e obligations map | sponsor executivo, com governance owner | mandato, scope, appetite, containment authority e regra de exceção aprovados | `hold` para esclarecer escopo/authority; não automatizar approvals |
| **G1 — Baseline** | G0 aprovado e acesso às fontes e stakeholders | inventários com coverage, current-state map, gaps, limitações e confidence | governance owner, com domain owners; sponsor aceita limitações materiais | baseline separa observado de hipótese e todo gap crítico tem owner | `hold`; unknowns de alto impacto restringidos ou isolados |
| **G2 — Fundações** | G1 aceito e população in-scope identificada | registry, blueprints, ownership, identity/data/tool records e testes de revogação | Design Authority e authorities de identity, data e tools | records mínimos validam, owners aceitam responsabilidade e acessos são revogáveis | bloquear onboarding, restringir connector/tool ou retornar |
| **G3 — Operating model** | G0 vigente, handoffs atuais conhecidos e G2 suficiente para atribuir responsabilidade | operating model, RACI, decision matrix, exception flow, SLAs e charters | sponsor/Governance Council, com aceite das domain authorities | cada decisão material possui accountable, receiver, prazo e escalation | `hold`; decisões não delegadas retornam à authority existente |
| **G4 — Controls e assurance** | tiering proposto, G2/G3 aceitos e obligations map disponível | risk rationale, baseline por tier, assessments, evaluation plan, evidence index e residual-risk record | Design Authority e domain authorities; residual risk pela authority designada | controles bloqueantes possuem design, owner, teste e evidence requirement | `hold` ou `reject`; remediar, reduzir capability/escopo ou elevar authority |
| **G5 — Onboarding/release** | G4 aprovado para o escopo e versão, suporte e operação preparados | blueprint versionado, checks, evidence package, conditions, run readiness e release record | release/Design Authority definida no operating model | release `approve`/`condition` registrado e catalog entry publicável | não liberar; corrigir, reclassificar, restringir ou rejeitar |
| **G6 — Operação** | G5 válido e sistema instrumentado antes de exposição material | telemetry map, thresholds, runbooks, on-call, drills, rollback/quarantine e incident evidence | Run Authority, com domain escalation | sinais possuem owner/action e containment, recovery e reactivation foram exercitados | conter, fazer rollback ou suspender; reativação exige cause e regression evidence |
| **G7 — Valor e lifecycle** | janela de operação definida, G6 aceito e baseline de outcome/custo disponível | owner attestation, use/quality/risk/value evidence, incidents, costs e sunset options | Business Owner; Governance Council para portfólio/material risk | decisão de manter, expandir, corrigir, restringir ou aposentar registrada | restringir/sunset ou abrir remediation; mudança normativa segue processo separado |

### 1.3 A numeração não é um cronograma

**G0–G7 são pontos de decisão com dependência declarada, não etapas em ordem cronológica.** A dependência real:

| Gate | Depende de |
|---|---|
| G0 | — |
| G1 | G0 |
| G2 | G1 |
| G3 | G0 vigente e **G2 suficiente para atribuir responsabilidade** — não G2 completo |
| G4 | G2 e G3 |
| G5 | G4, para aquele escopo e versão |
| G6 | G5 |
| G7 | G6 |

A consequência prática: **G2 e G3 se sobrepõem.** Basta ter registry e ownership o bastante para saber a quem atribuir uma decisão; o resto das fundações continua sendo construído enquanto o operating model é aprovado. Um cronograma que assume ordem numérica vai travar esperando um G2 completo que o G3 não exige.

### 1.4 O que cada gate exige (detalhe por gate)

**G0 — Mandato, escopo e sponsorship.** Outcome: existe autoridade para definir requisitos, exigir evidências e conter sistemas fora do envelope aprovado. Atividades: nomear sponsor e governance owner; definir sistemas, unidades, regiões e ambientes cobertos; declarar risk appetite e red flags; mapear obrigações e authorities; definir o que permanece fora de escopo e por quanto tempo; estabelecer princípios e regra de versionamento. Entregáveis: governance charter, scope map, stakeholder/authority map, initial risk appetite, decision log, communication plan. **Gate questions:** quem pode aprovar, condicionar, conter e aposentar? O escopo inclui SaaS, low-code, shadow AI e adquiridos? Exceções têm authority e expiry? **Sem mandato, não automatize approvals nem prometa cobertura.**

**G1 — Diagnóstico e baseline.** Outcome: a organização conhece sua situação atual, lacunas e limitações de evidência. Atividades: aplicar maturity assessment; reconciliar inventários e sources; entrevistar owners e domain authorities; mapear lifecycle real, approvals e handoffs; revisar incidentes, findings, exceções e métricas; identificar duplicidade, ownerless assets e high-risk unknowns. Entregáveis: maturity baseline, current-state map, preliminary inventory, gap/risk register, evidence quality statement, prioritized decisions. **Gate questions:** quais conclusões são observadas e quais são hipóteses? Quais lacunas críticas não possuem owner? Onde existe policy sem enforcement ou evidence?

**G2 — Fundações de dados, identidade e ownership.** Outcome: cada agente possui identidade, owner, finalidade, dados e capabilities rastreáveis. Atividades: aprovar schemas de registry e blueprint; escolher source of truth e reconciliation; registrar business/technical owner; definir workload identity e permission mapping; criar data contracts e connector gates; inventariar tools, APIs e MCP; definir material changes e lifecycle states. Entregáveis: registry operacional, agent blueprints, identity records, data contracts, tool/MCP registry, ownership e attestation rules. **Gate questions:** é possível responder o que existe e quem responde? Blueprint explica arquitetura e blast radius? Identidades, connectors e tools podem ser revogados?

**G3 — Operating model e decision rights.** Outcome: decisões têm authority, handoffs, SLA e evidência. Atividades: instituir Council, Design Authority e Run Authority; definir domain authorities; criar RACI e decision matrix; separar build, approval, run e challenge conforme tier; desenhar exception e waiver process; definir forums e cadences. Entregáveis: target operating model, RACI/decision rights, forum charter, handoff map, exception process, service levels. **Gate questions:** accountability está em funções reais, não em "o time"? Run Authority pode conter sem depender de council? Exceção sem expiry é bloqueada?

**G4 — Controls mínimos e assurance.** Outcome: risco é classificado e traduzido em controls, assessments, tests e residual-risk decisions. Atividades: aprovar tiers e red flags; mapear control catalog; definir triggers de assessments; criar evaluation strategy e evidence package; definir human oversight e transparency; testar negative paths, rollback e kill switch; estabelecer risk acceptance authority. Entregáveis: risk matrix, control baseline por tier, assessment suite, evaluation/release criteria, human oversight design, evidence package index. **Gate questions:** cada control tem owner e evidence? Ausência de evidência aparece como missing, não passed? Approval é proporcional com caminho de remediation?

**G5 — Onboarding por tier.** Outcome: existe um paved road para registrar, avaliar, liberar e suportar agentes em cada tier. Atividades: integrar registry, blueprint, controls e release flow; criar starter templates e approved components; configurar automated checks onde policy está estável; publicar guidance, examples e support; validar experiência de maker, reviewer, owner e operator; impedir bypass de paths críticos. Entregáveis: onboarding workflow, release checklist, approved component catalog, builder guidance, support/escalation model, audit trail do gate. **Gate questions:** o paved road é mais simples que contornar a governança? O workflow diferencia risco e capability? Condições e findings chegam ao owner correto?

**G6 — Operação, observabilidade e resposta.** Outcome: sinais geram decisões e ações de contenção, remediação e recuperação. Atividades: instrumentar agent, identity, data e tool chain; definir SLOs, thresholds e alerts; implementar quarantine, rollback e reactivation; executar drills; ligar support, SOC/SRE e domain escalation; preservar evidence e atualizar regression suite. Entregáveis: observability model, dashboards com owner/threshold/action, incident severity e runbooks, quarantine/rollback evidence, runtime control mapping, post-incident loop. **Gate questions:** o dashboard muda uma decisão? Containment funciona sem cooperação do agente? Reactivation exige cause e regression evidence?

**G7 — Valor, attestation e melhoria contínua.** Outcome: o portfólio é revisado por ownership, risco, qualidade, uso, outcome e custo. Atividades: separar criação, discovery, adoção, uso, qualidade e valor; revisar business case e baseline; executar attestation conforme tier; analisar concentração, duplicidade e inativos; decidir manter, expandir, corrigir, restringir ou aposentar; atualizar policy somente por processo versionado. Entregáveis: value review, attestation record, portfolio decisions, improvement backlog, sunset records, change proposal versionada. **Gate questions:** há outcome observável ou apenas uso? Custo inclui operação, suporte e assurance? Policy changes estão separadas de guidance?

### 1.5 Definition of done da implantação

A implantação está operacional quando: o inventário é reconciliável e possui owners; tier determina controls e authority; release evidence é recuperável; identities, data e tools são revogáveis; runtime signals acionam runbooks; quarantine, rollback e sunset foram exercitados; attestation e value review mudam o portfólio; exceptions vencem; policy e guidance são versionados separadamente.

### 1.6 O que o playbook não faz

Não substitui análise jurídica ou regulatória; não define threshold universal; não seleciona produto; não comprova maturidade por documentação; não certifica conformidade; não promete resultado financeiro.

## 2. Roadmap de 90 dias (referência acelerada)

> **Referência acelerada, não SLA.** Os 90 dias ajudam equipes que precisam de uma sequência inicial. Adapte duração e sobreposição às dependências, ao estate e à capacidade. O calendário nunca substitui G0–G7 nem cria obrigação de piloto.

Objetivo: estabelecer as fundações e fluxos mínimos de um sistema de governança operável. **O resultado não é "governança concluída" — é uma capacidade inicial verificável que pode ser ampliada sem perder accountability.**

| Período | Gates preparados ou decididos | Decisão esperada |
|---|---|---|
| dias 0–10 | G0 | aprovar, condicionar, suspender ou rejeitar mandato e scope |
| dias 11–25 | G1 | aceitar baseline e limitações ou exigir evidência/remediação |
| dias 26–40 | G2 | aceitar fundações mínimas ou bloquear onboarding |
| dias 41–55 | G3 e preparação de G4 | aprovar decision rights e autorizar desenho da baseline de controls |
| dias 56–70 | G4 e preparação de G5 | aceitar baseline/assurance e decidir readiness para release |
| dias 71–85 | G5 e G6 | decidir release condicionado ao tier e aceitar operação/containment |
| dias 86–90 | G7 | decidir continuidade, restrição, expansão, remediação ou sunset |

**Dias 0–10 (G0):** nomear sponsor, governance owner e authorities; aprovar escopo e ambientes; definir risk appetite, red flags e containment authority; mapear policies, processos e inventários; selecionar portfólio inicial. Entregáveis: charter, scope map, authority matrix, risk appetite v0.1, decision/risk log. **Exit:** sponsor e owners nominativos; escopo explícito; containment authority definida; nenhuma lacuna crítica sem owner.

**Dias 11–25 (G1):** aplicar maturity assessment; reconciliar inventários; mapear lifecycle e handoffs; identificar ownerless, duplicados, inativos e high-risk unknowns; avaliar qualidade da evidência; priorizar gaps. Entregáveis: maturity baseline, current-state map, preliminary registry, gap/risk register, prioritized backlog. **Exit:** situação atual separa observado de hipótese; inventário com coverage declarado; gaps críticos com owner e prazo.

**Dias 26–40 (G2):** aprovar schemas mínimos; definir source of truth e reconciliation; registrar owners e lifecycle; preencher blueprints do portfólio inicial; mapear workload identities e permissions; criar data contracts e connector gates; inventariar tools, APIs e MCP. Entregáveis: registry e blueprints versionados, identity/permission matrix, data contracts, tool/MCP registry, material-change triggers. **Exit:** todos os itens do escopo inicial têm owner e status; identities, data e tools rastreáveis; gaps aparecem como missing evidence.

**Dias 41–55 (G3/G4):** formalizar Council, Design e Run Authority; definir RACI e decision rights por tier; aprovar tiers e red flags; mapear control catalog e evidence; definir exception/waiver e expiry; estabelecer forums, handoffs e SLAs. Entregáveis: target operating model, RACI, risk/control baseline, exception process, forum charter. **Exit:** cada decisão material possui accountable; segregação proporcional; exceções não permanentes por padrão.

**Dias 56–70 (G4/G5):** definir triggers de assessments; criar evaluation strategy e thresholds; documentar oversight e transparency; montar release evidence package; testar negative paths, rollback, quarantine e kill switch; registrar residual risk e conditions. Entregáveis: assessment suite, evaluation/release criteria, evidence package, run readiness checklist, drill records. **Exit:** controls aplicáveis com evidence; release authority consegue aprovar, condicionar ou negar; containment e rollback exercitados.

**Dias 71–85 (G5/G6):** colocar onboarding em uso; configurar telemetry, dashboards e alerts; publicar catalog entries, guidance e support; ligar incident, support e domain escalation; medir fricção, gaps e bypass; corrigir controls pelo processo versionado. Entregáveis: onboarding operacional, observability e runbooks, catalog/discovery, support model, remediation backlog. **Exit:** cada signal com owner e action; state-changing actions com correlation; support e escalation ponta a ponta.

**Dias 86–90 (G7):** executar primeira owner attestation; revisar criação, discovery, uso, qualidade e value separadamente; registrar decisões; atualizar maturity baseline; aprovar roadmap de expansão. Entregáveis: attestation records, portfolio/value review, maturity delta, roadmap 6–12 meses, executive decision memo. **Exit:** decisões ligadas a evidência; próximos increments com owner e acceptance criteria; nenhuma mudança normativa autoaprovada.

**Riscos de execução:** burocracia uniforme → tiering e paved road; catálogo decorativo → reconciliation e actions; falso senso de coverage → declarar sources e confidence; centralização em silo → authorities distribuídas; automação prematura → manual first para regras instáveis; métricas de vaidade → separar criação, uso, qualidade e outcome; vendor lock-in → capabilities e schemas neutros; rollout sem containment → quarantine/rollback como exit criteria.

## 3. Programa de 24 semanas (pattern de referência)

> **Pattern de referência, não calendário normativo.** As 24 semanas oferecem um ponto de partida para equipes que ainda não sabem como organizar a implantação. As Implementation Waves W0–W6 são guidance de planejamento; os únicos decision gates canônicos são G0–G7, e as lifecycle phases F1–F8 continuam descrevendo o ativo.

**Implementation Waves e gates:**

| Implementation wave | Semanas | Objetivo | Entregáveis | Gate |
|---|---|---|---|---|
| **W0 — Mobilizar** | 1–2 | mandato e escopo | charter, scope, decision principles, fóruns, time | G0 |
| **W1 — Descobrir** | 3–5 | baseline real | discovery, forecast, gargalos, capability map, maturity | G1 |
| **W2 — Desenhar** | 6–8 | target operating model | target de maturidade, tiers, triggers, operating model | G3 e preparação de G4 |
| **W3 — Construir** | 9–12 | controles de fundação | registry, identidade, catálogos, telemetria, MPB | G2 e G4 |
| **W4 — Validar** | 13–16 | validar ponta a ponta | piloto opcional ou cohort; fluxo completo, tabletop, KPIs | G5 e G6 |
| **W5 — Escalar** | 17–20 | automação e cobertura | discovery automatizado, policy-as-code, JML, FinOps | G6 |
| **W6 — Institucionalizar** | 21–24 | operação regular e assurance | evidência, enablement, handoff BAU, roadmap 12m | G7 |

**Repare: W2 fecha G3 e W3 fecha G2** — a ordem numérica dos gates não é a ordem de execução. Os dois roadmaps (90 dias ≈ W0–W3 comprimidas; 24 semanas = versão detalhada) são guias adaptáveis do mesmo conjunto de gates, não métodos concorrentes nem prazos de compliance.

**Workstreams:** trilhas paralelas dentro do mesmo roadmap — governança e risco; arquitetura e plataforma; identidade e segurança; dados e ferramentas; observabilidade e custo; adoção e valor. **Workstreams não podem otimizar localmente:** identidade pode declarar "entregue" enquanto o registry ainda não associa identidade a `agent_id`. **Milestones se definem por outcome cross-domain, não por entrega de trilha.**

**Prioridade do backlog:** `P0` (obrigatório para a primeira release — charter, registry mínimo, tiers, blueprint, MPB, identidade T2/T3, catálogos, logging, gate, kill switch, evidência); `P1` (necessário para escalar — discovery automatizado, JML, attestation, SOC, behavioral analytics, FinOps, champions); `P2` (otimização avançada). **Um item de backlog de qualidade tem:** outcome, por quê, dependências, trabalho, evidência e critério de saída.

**Cadência:** semanal (workstream: entregas, dependências, bloqueios); quinzenal (revisão integrada de arquitetura e governança: outcomes cross-domain); mensal (sponsor e council: risco, prioridade, funding, exceções); trimestral (maturidade: alvo e roadmap).

**Ciclo de melhoria contínua (trimestral):** revisar KPIs/KRIs; analisar incidentes e quase-incidentes; revisar exceções — **uma exceção que se repete não é exceção: é requisito que a policy não reconheceu ou controle que a operação não cumpre**; avaliar falsos positivos/negativos; revisar gargalos; atualizar standards com changelog; priorizar roadmap.

**Como usar sem virar teatro de programa:** fases podem se sobrepor, gates não; prazo cumprido com evidência ausente é `hold`, não `approve`; escopo reduzido é decisão legítima registrada; as semanas dimensionam esforço, não prometem maturidade.

## 4. Capability map: atual versus alvo

### 4.1 O que é uma capability

Uma capacidade organizacional de produzir um resultado **de forma repetível**. Não é uma ferramenta, um time nem um projeto. **O teste: se você trocar o produto e a capacidade desaparecer, você comprou uma ferramenta e chamou de capability.**

### 4.2 As capacidades do framework

Ponto de partida: os domínios canônicos. Quebre uma capability em duas apenas quando a filha tiver owner, processo **ou** evidência diferentes.

| Capacidade | Pergunta de diagnóstico | Sinal típico de estado inicial | Alvo comum |
|---|---|---|---|
| estratégia e governança | existe mandato, portfólio, funding e decisão clara? | política genérica, sem charter | charter, fóruns, decision rights, risk appetite |
| estate inventory e registry | sabemos quais agentes existem, onde operam e quem responde? | planilhas por plataforma | discovery contínuo + registry reconciliável |
| risco e Responsible AI | risco, admissibilidade e impacto roteiam controles? | mesma review para todos | tiers, admissibilidade, escaladores, impact assessment |
| lifecycle e Agent SDLC | versões, estados e mudanças estão governados? | publicação ad hoc | stage/state, gates, attestation e retirada |
| identidade e acesso | cada ação é atribuível e autorizada? | chaves compartilhadas | identidade própria, least privilege, JML |
| dados e conhecimento | fontes são classificadas, permitidas e AI-ready? | recuperação sobre qualquer pasta | catálogo de fontes certificadas |
| tools, APIs e MCP | ações são catalogadas, limitadas e mediadas? | ferramentas embutidas por time | tool registry, gateway, autorização por ação |
| modelos e provedores | combinações e versões têm critérios de admissão? | escolha por preferência | catálogo, evaluation binding, fallback, exit |
| runtime e plataforma | existem enforcement, isolamento, resiliência e rollback? | acesso direto a endpoints | control plane, budgets, containment |
| segurança e AgentSecOps | ameaças agentic entram em prevention/detection/response? | SOC vê só logs tradicionais | threat model agentic, red teaming |
| observabilidade | é possível reconstruir, detectar desvio e agir? | logs sem correlation | event envelope, baselines, runbooks |
| FinOps | custo é atribuível a agente, tarefa e outcome? | custo por chave agregado | budgets, unit economics, anomaly response |
| value realization | outcomes influenciam funding e sunset? | contagem de agentes | baseline, KPI, portfolio decisions |
| assurance e auditabilidade | controls podem ser testados por challenge? | evidence manual para auditoria | continuous evidence, sampling, findings |
| adoção e competências | cada papel usa a rota governada corretamente? | treinamento pontual | currículo por papel, champions, support |

### 4.3 Procedimento

1. Listar as capacidades necessárias ao operating model.
2. Escrever uma frase de outcome para cada uma (ex.: *"toda ação material de agente é atribuível a uma identidade conhecida e autorizada"*).
3. Definir evidências observáveis do estado atual — prefira *"74% dos T2/T3 usam identidade dedicada"* a "o controle de acesso é forte".
4. Atribuir maturidade com base em evidência e registrar confidence. **Evidência fraca produz nota provisória, não nota otimista.**
5. Definir o alvo por horizonte e necessidade — nível 3 costuma bastar no primeiro ano.
6. Identificar dependências (behavioral analytics depende de registry + identidade + telemetria + runtime).
7. Converter gaps materiais em iniciativas.

**Perguntas de challenge antes de aprovar o alvo:** o alvo é necessário para o risco e o volume previstos, ou é ambição tecnológica? Existe dependência invisível? Pode ser demonstrado por evidência? **Existe owner capaz de sustentar a capacidade depois que o programa terminar?** — a última derruba mais iniciativas que as outras três somadas.

**Failure modes:** mapear produtos e chamar de capacidades; quebrar capacidades até virarem tarefas; alvo máximo em tudo; estado atual descrito por adjetivo; ignorar que capacidade em nível baixo inutiliza outra em nível alto; aprovar alvo sem owner pós-programa.

## 5. Adoção, enablement e suporte

### 5.1 Adoção não é comunicação de lançamento

É a capacidade organizacional de usar o sistema de forma correta, obter suporte, reportar falhas e incorporar feedback ao governance lifecycle.

**Personas:** sponsor (value, risco, decisões); business owner (outcome, usuários, limites, attestation); maker/engineer (paved road, controls, feedback rápido); end user (intended use, limitações, suporte, contestação); administrator (policy, inventory, acesso); support (triage, known issues, escalation); domain authority (evidências, decision rights); auditor (acesso independente a records).

### 5.2 Discovery e catalog

Um catálogo útil permite: encontrar capacidades por tarefa e persona; distinguir status, owner, versão e tier; entender intended/prohibited use; acessar support e feedback; evitar duplicação; ocultar itens em quarantine/sunset; medir discovery separado de criação. **Publicar sem discovery gera agentes invisíveis; discovery sem lifecycle promove itens inadequados.**

### 5.3 Paved road para builders

Starter templates com identity, logging e policy hooks; schemas e self-assessment proporcionais; approved models, data connectors e tools; automated checks com feedback acionável; sandbox e test datasets; design clinic e office hours; exception process com owner e expiry; documentação de examples e failure modes. **O paved road deve ser mais simples que contornar a governança — fricção desnecessária é o principal produtor de shadow AI.**

O golden path do builder: registrar use case, owner e prohibited use → criar registry record e blueprint → classificar risk tier e red flags → selecionar approved model/data/tool contracts → aplicar controls e evaluation strategy → produzir release evidence → obter decisão no gate → publicar com observability, containment e rollback → operar, regress, attest e sunset.

### 5.4 Suporte em camadas

1. **Self-service:** documentação, status, FAQ, runbooks.
2. **AI-assisted:** busca e triage com handoff rastreável.
3. **Platform/IT backstop:** incidentes, acesso e operação.
4. **Domain SME:** security, privacy, RAI, legal, data ou negócio.
5. **Authority escalation:** containment, risk acceptance e policy decision.

### 5.5 Change e comunicação

Mudanças materiais comunicam: o que mudou e por quê; quem é afetado; novos limites ou ações; data de vigência; treinamento ou suporte necessário; rollback/contingency; canal de feedback e owner.

### 5.6 Feedback loop

```mermaid
flowchart LR
    U[Uso] --> F[Feedback/sinal]
    F --> T[Triage]
    T --> B[Backlog]
    B --> D[Decisão]
    D --> C[Change]
    C --> E[Evaluate]
    E --> U
```

**Feedback é evidência contextual, não prova isolada de valor ou segurança.**

### 5.7 Plano de implantação — adoção, enablement e suporte

1. **Segmentar personas** — cada uma com objetivo de aprendizagem distinto.
2. **Separar awareness de competência** — awareness ensina a reconhecer a regra; competência exige executar a atividade e demonstrar resultado. **Não habilite um reviewer de impact assessment porque ele concluiu um treinamento introdutório.**
3. **Montar currículo por papel e risco** — builders: registry, risco, dados, ferramentas, identidade, telemetria; owners: accountability, valor, attestation; reviewers: critérios e evidência; segurança: contenção e forensics.
4. **Implantar rede de champions** — áreas por volume e risco, tempo alocado e **limite de autoridade**: o champion orienta e escala; não substitui funções de controle.
5. **Tornar o caminho governado o mais fácil** — builders aprovados, templates, catálogos, office hours, policy gates self-service.
6. **Calibrar reviewers com casos comuns** — os mesmos 10–20 casos por reviewers diferentes; divergência vira discussão de critério.
7. **Criar suporte e comunidade de prática** — office hours, FAQ, canais de escalation; perguntas recorrentes viram melhoria de documentação.
8. **Medir eficácia, não conclusão** — taxa de conclusão de treinamento é métrica fraca isolada; medir verificação de conhecimento, retrabalho, violações, tickets, tempo até assessment, qualidade da evidência.

### 5.8 Prontidão de suporte e handoff

Antes do handoff: owners permanentes, níveis de suporte, runbooks, acesso, monitoramento, capacidade e backlog prontos. Reter: aceite de serviço, assinatura do owner, modelo de suporte, SLO, teste de runbook, dívida conhecida, treinamento e escalonamento. **Times do business as usual resolvem um problema representativo e aceitam o trabalho residual sem dependência do projeto de implementação.** O último item é o mais ignorado e o que mais derruba programas: sem owner de BAU aceito, o piloto vira ilha mantida pelo time do programa.

## 6. Do programa à rotina: oito processos operacionais

A implantação termina quando os gates G0–G7 decidem que existe governança operável. A partir daí, o que mantém o sistema vivo **não é mais o programa** — é a rotina: o mesmo conjunto de processos que cada agente atravessa repetidamente, dia após dia, da ideia ao encerramento.

Esta seção apresenta esses processos no formato de quem vai executá-los: **o que é, quando dispara, quem responde, o que entra, o que se faz, o que sai e onde errar**. O detalhe normativo de cada tema continua nos capítulos donos (indicados em cada processo); aqui eles aparecem na sequência em que a operação realmente acontece.

**O mapa, para orientação:**

| # | Processo | Capítulo dono | Gate relacionado | Fase do lifecycle |
|---|---|---|---|---|
| P1 | Criação e registro | 03 (registry) e 05 (F1–F2) | G2 | IDEA → REGISTER |
| P2 | Avaliação e aprovação | 04 (risco) e 05 (F5) | G3/G4/G5 | CLASSIFY → APPROVE |
| P3 | Publicação | 07 (evidência) e 05 (F6) | G5 | RELEASE |
| P4 | Operação rotineira | 09 (§1) e 10 (métricas) | G6 | PRODUCTION |
| P5 | Incidentes | 09 (§2) | G6 | CONTAIN → REACTIVATE |
| P6 | Mudanças | 09 (§4.3) e 05 (F7) | gates reabertos | CHANGE |
| P7 | Revisão e auditoria | 10 (§4) e 09 (§4.4) | G7 | ATTESTATION |
| P8 | Sunset | 09 (§4.5) e 05 (F8) | G7 | RETIRE |

A tabela é só a bússola. Os processos abaixo são a trilha — e a regra de ouro que atravessa todos: **nenhum deles conclui sem registro.** Se o passo não deixou rastro recuperável, ele não aconteceu para a governança.

### 6.1 P1 — Criação e registro inicial

**O que é e por que importa.** É a porta de entrada: nenhum agente é criado, adquirido ou adotado sem owners nomeados, avaliação inicial de risco e um registro mínimo no registry. Sem este processo, o estate acumula agentes invisíveis — criados em plataformas de citizen development, ativados em PoCs que nunca morrem, legados sem dono — e toda a governança posterior opera às cegas, porque o [inventário](03-inventory-portfolio-and-value.md) nunca nasceu.

**Quando dispara.** Uma ideia ou demanda de novo agente em qualquer unidade; ou a necessidade de formalizar um agente já existente (legado) que nunca passou pelo processo.

**Quem responde.** O **business owner**, com apoio do technical owner e da Run Authority. O proponente participa; a responsabilidade de registrar corretamente é do owner.

**Entradas.** A demanda ou caso de uso priorizado; o [use-case intake](../../toolkit/templates/use-case-intake.md) preenchido; acesso ao registry (ferramenta ou modelo corporativo).

**Atividades.**

1. O proponente discute o caso de uso com os owners para validar objetivo, dados, escopo e se **agente é o mecanismo certo** — a pergunta de adequação do [cap. 03](03-inventory-portfolio-and-value.md#3-decidir-o-que-construir-intake-e-adequacao) vem antes de qualquer tecnologia.
2. Business e technical owner preenchem a [autoavaliação](../../toolkit/templates/self-assessment-form.md) com, no mínimo: objetivo, dados e owners, permissões, integrações, autonomia/HITL, usuários, impacto, riscos e controles previstos.
3. A Run Authority apoia no enquadramento inicial de risco (blast radius) usando as dimensões do [cap. 04](04-risk-impact-and-compliance.md).
4. Cria-se o registro preliminar no registry com agent ID, nome, owners, ambiente previsto e estado `registered` — não "aprovado", não "em produção": **o estado reflete consequência operacional real**.
5. Se houver agente similar no registry, a Run Authority sinaliza a possível duplicidade e registra a avaliação no próprio registro.

**Saídas.** Autoavaliação preenchida; registro inicial no registry com owners e estado; indicação explícita de duplicidade ou reuso.

**Armadilhas comuns.**

- Registrar como `approved` o que ainda é só uma ideia — o estado no registry é a verdade para automação e auditoria; inflá-lo destrói a confiança em todos os outros processos.
- Aceitar "não sei" silenciosamente na autoavaliação: **`não sei` é um gap com owner e prazo**, não uma resposta.
- Pular a pergunta de adequação: um workflow determinístico disfarçado de agente herda custo e risco de governança sem trazer a capacidade que a justifica.

**Onde está a profundidade.** Descoberta, fontes e taxonomia em [cap. 03](03-inventory-portfolio-and-value.md); lifecycle F1–F2 em [cap. 05](05-agent-lifecycle.md).

### 6.2 P2 — Avaliação e aprovação

**O que é e por que importa.** É onde a classificação vira decisão: o pre-screen coleta fatos, o scoring e os red flags produzem o tier, o impact trigger decide se entra Responsible AI, os domain reviews tratam controles especializados, e a autoridade competente aprova, condiciona ou rejeita. Sem este processo, cada caso é decidido pelo critério de quem estiver na sala — exatamente o cenário que a governança existe para eliminar.

**Quando dispara.** Autoavaliação preenchida e registro inicial criado; planejamento de PoC, piloto ou promoção para produção; qualquer demanda de reavaliação após mudança material.

**Quem responde.** A **Run Authority** coordena; as autoridades de aprovação são as definidas pelo tier e pela admissibilidade no [operating model](02-governance-and-accountability.md).

**Entradas.** Autoavaliação; [risk pre-screen](../../toolkit/templates/risk-pre-screen.md); informações sobre dados sensíveis, sistemas críticos e obrigações aplicáveis.

**Atividades.**

1. Aplicar o [pre-screen](../../toolkit/templates/risk-pre-screen.md) — perguntas objetivas sobre dados, autonomia, ações irreversíveis, pessoas afetadas e alcance.
2. Calcular o risco base e aplicar os **red flags** — eles corrigem o que um score médio esconde: um caso com dez respostas benignas e uma destrutiva não é um caso médio (ver [cap. 04](04-risk-impact-and-compliance.md)).
3. Definir **tier (T1–T4) e admissibilidade** (permitted/conditional/restricted/prohibited). Tier determina proporcionalidade de controle; admissibilidade determina se o uso é aceitável em primeiro lugar.
4. Aplicar o **impact trigger screen**: o agente influencia direitos, oportunidades, decisões sobre pessoas ou segurança? Se sim, executar o impact assessment formal **mesmo em caso tecnicamente simples**.
5. Acionar **domain reviews** apenas quando houver gatilho relevante — privacidade por dados pessoais, segurança por privilégio, arquitetura por mudança de pattern. Review acionada por regra fixa vira fila e morre.
6. Registrar a decisão com autoridade, evidências aceitas, condições e expiry — conforme o [contrato comum dos gates](#11-o-contrato-comum-dos-decision-gates). Se reprovado, o estado vira `rejected` ou `pending-changes`, com o que falta explícito.

**Saídas.** Decisão formal registrada (approve/condition/hold/reject); evidências vinculadas ao registro; tier, admissibilidade e controles obrigatórios definidos; conditions e expiry quando aplicável.

**Armadilhas comuns.**

- Deixar o score sozinho decidir: red flags são **piso, não teto** — nunca diluídos por média.
- Tratar "PoC" como sinônimo de baixo risco: um agente para 5 usuários que executa pagamentos é mais crítico que um para 5.000 que resume documentos.
- Aprovar sem residual risk explícito: **nenhuma aprovação existe sem residual risk aceito pela autoridade compatível com o tier.**

**Onde está a profundidade.** Classificação completa em [cap. 04](04-risk-impact-and-compliance.md); matriz de decisão tier×mecanismo na seção 1 do cap. 04; gates em [cap. 05](05-agent-lifecycle.md) e na [seção 1 deste capítulo](#1-a-jornada-em-8-gates).

### 6.3 P3 — Publicação em produção

**O que é e por que importa.** É o portão final antes da exposição real: nada entra em produção sem cumprir o [Minimum Production Bar](../../toolkit/controls/minimum-production-bar.md), com HITL, logging, contenção e custo configurados. É aqui que a governança verifica que **a evidência existe e é recuperável** — não que alguém disse que os testes passaram.

**Quando dispara.** Agente aprovado para produção; desenvolvimento e testes concluídos pelo technical owner.

**Quem responde.** A autoridade de release definida no operating model (perfil publisher ou equivalente), em conjunto com technical e business owner.

**Entradas.** [Release evidence manifest](../../toolkit/templates/release-evidence-manifest.md); agente configurado em homologação; plano de rollback quando aplicável; evidência dos testes mínimos (prompt injection, exfiltração, safety, tool-use).

**Atividades.**

1. O technical owner executa os testes mínimos exigidos e registra evidências com resultado observável — "recusou", "bloqueou", "pediu aprovação".
2. Owners preenchem e validam o checklist de publicação: owners, dados e permissões, HITL, logs, cap/alertas de custo, testes, documentação e rollback.
3. A autoridade de release confere o checklist, valida o registro no registry e **que o evidence pack do tier está completo** (ver [cap. 07](07-evaluation-evidence-and-assurance.md)).
4. Executa-se a promoção com segregação de funções quando aplicável — quem constrói não é quem aprova a própria publicação.
5. Ativam-se dashboards e alertas de consumo e logs **antes** de liberar usuários.

**Saídas.** Agente ativo em produção no escopo aprovado; checklist concluído e arquivado; registry atualizado com estado `production` e monitoramento configurado; usuários comunicados do canal oficial e do escopo suportado.

**Armadilhas comuns.**

- Kill switch testado em documento, nunca exercitado: o teste real do kill switch é parte do evidence pack de T2+.
- Publicar antes de ativar alertas de custo: um agente sem cap em produção é uma superfície de custo aberta (denial-of-wallet).
- Comunicar usuários depois do problema: o anúncio do escopo suportado e do canal de reporte é parte da publicação, não do incidente.

**Onde está a profundidade.** Evidência e assurance em [cap. 07](07-evaluation-evidence-and-assurance.md); lifecycle F6 em [cap. 05](05-agent-lifecycle.md); MPB em [toolkit](../../toolkit/controls/minimum-production-bar.md).

### 6.4 P4 — Operação rotineira

**O que é e por que importa.** É o coração do dia a dia: monitorar consumo contra cap, acompanhar logs e erros, revisar KPIs de valor e manter o registry refletindo a situação atual. Um agente publicado não é um ativo congelado — é um sistema dinâmico que deriva; a operação rotineira é o que detecta a deriva cedo, quando ainda é ajuste e não incidente.

**Quando dispara.** Continuamente, enquanto houver agentes em produção; em cadência definida para revisões de valor (ex.: mensal/trimestral por tier).

**Quem responde.** **Run Authority** pelo monitoramento e pelo registry; business owner pelos KPIs de valor; technical owner pelas melhorias técnicas.

**Entradas.** Registry com campos de consumo, cap e próximos marcos; dashboards de consumo, logs e erros; relatórios de uso.

**Atividades.**

1. Monitorar consumo dos agentes versus cap, atuando sobre alertas em patamares (ex.: 70% e 90% do orçamento).
2. Acompanhar logs de uso e erros para identificar comportamentos anômalos, incidentes potenciais ou violação de policy.
3. O business owner revisa periodicamente os KPIs de valor e decide ajustes de escopo ou usuários.
4. O technical owner avalia melhorias: otimização de prompts/modelos, ajustes de permissão, dívida técnica.
5. Atualizar o registry com consumo, incidentes relevantes e ações corretivas — **o registry é o retrato atual, não um formulário de entrada.**

**Saídas.** Operação contínua com visibilidade de consumo, performance e conformidade; alertas tratados e ajustes documentados; registry refletindo a situação atual de cada agente.

**Armadilhas comuns.**

- Dashboard sem owner, threshold e ação: visualização não é governança (ver [cap. 10](10-metrics-review-and-improvement.md)).
- Tratar pico de custo só como tema financeiro: loop descontrolado é custo **e** sinal de segurança ao mesmo tempo.
- Registry desatualizado entre revisões: a próxima decisão de portfólio será tomada sobre um retrato errado.

**Onde está a profundidade.** Modelo de observabilidade e playbook em [cap. 09](09-operations-incidents-and-continuity.md); FinOps em [cap. 10](10-metrics-review-and-improvement.md).

### 6.5 P5 — Gestão de incidentes

**O que é e por que importa.** É a resposta a violações reais ou suspeitas — vazamento de dados, comportamento inadequado, consumo anômalo, falha crítica. A velocidade e a ordem importam mais que a burocracia: conter primeiro, entender depois, revalidar antes de reativar. **A contenção não pode depender do próprio agente com falha.**

**Quando dispara.** Detecção via alerta, reporte de usuário, auditoria ou ferramenta de segurança; indícios de violação de policy, privacidade ou risco operacional relevante.

**Quem responde.** **Run Authority**, coordenando technical owner, business owner, segurança e compliance conforme severidade.

**Entradas.** Registro do agente (owners, integrações, dados); logs com histórico recente; procedimentos de resposta corporativos; [severity matrix](09-operations-incidents-and-continuity.md) e [runbooks](09-operations-incidents-and-continuity.md).

**Atividades.**

1. **Conter primeiro.** Kill switch imediato para risco severo; quarentena quando o risco permitir (limitar escopo, desabilitar escrita, reduzir usuários). Escolher o menor passo da [escada de contenção](09-operations-incidents-and-continuity.md) que controla o risco.
2. **Preservar evidência antes de remediação** — a investigação morre se a resposta destruir o rastro.
3. Analisar logs e reproduzir o cenário para causa raiz; avaliar blast radius real.
4. Segurança/compliance avaliam impacto regulatório e necessidade de comunicação.
5. O business owner decide, com as áreas de controle, entre corrigir e retomar ou iniciar sunset.
6. Registrar incidente, ações e decisão final; atualizar o registry; alimentar a regression suite.

**Saídas.** Incidente contido com kill switch/quarentena quando aplicável; registro formal com plano de ação; decisão de continuidade, ajuste ou sunset documentada.

**Armadilhas comuns.**

- Reativar antes de regression test: a reativação exige causa, remediação, reteste e sinais precoces ativos.
- Quarentena que não revoga tool access: quarentena de fachada é falsa sensação de controle.
- Ausência de incidente tratada como prova de segurança: ausência pode ser sub-detecção, não ausência de dano.

**Onde está a profundidade.** Incident lifecycle, containment ladder, quarentena e reativação em [cap. 09](09-operations-incidents-and-continuity.md).

### 6.6 P6 — Gestão de mudanças

**O que é e por que importa.** Agentes mudam constantemente — novo prompt, nova tool, nova fonte de dados, nova autonomia. Cada mudança pode alterar risco, impacto ou comportamento, e a pergunta da governança é sempre a mesma: **esta mudança reabre qual gate?** O processo existe para que mudança material nunca passe despercebida e mudança trivial nunca pague o custo de uma reavaliação integral.

**Quando dispara.** Solicitação de mudança em agente existente; identificação de aumento de risco (dados sensíveis novos, sistemas críticos novos, ampliação de autonomia ou usuários).

**Quem responde.** **Business e technical owner** descrevem; a Run Authority verifica impacto de classificação e roteia.

**Entradas.** Situação atual no registry; autoavaliação anterior; tier e admissibilidade vigentes; lista de [material change triggers](05-agent-lifecycle.md) do agente.

**Atividades.**

1. Owners descrevem a mudança proposta (escopo, dados, integrações, autonomia, usuários) e reavaliam a autoavaliação.
2. A Run Authority verifica se a mudança altera tier, admissibilidade ou controles obrigatórios.
3. Se o risco sobe (dados pessoais novos, autonomia maior, público muito maior), reabrir a avaliação e a aprovação na autoridade competente — **o reassessment recomeça do ponto afetado, não do zero**.
4. Após aprovação, implementar em ambiente controlado com plano de rollback.
5. Atualizar registry e blueprint versionados; manter o histórico da versão anterior — **mudar o blueprint não pode apagar a evidência de releases anteriores**.
6. Mudanças emergenciais seguem break-glass com revisão posterior obrigatória.

**Saídas.** Mudança implementada com aprovação adequada e rastreabilidade; registry e blueprint atualizados e versionados; autoavaliação atualizada com histórico preservado.

**Armadilhas comuns.**

- Alterar prompt em produção sem version: impossível explicar depois por que o comportamento mudou.
- Tratar toda mudança como material (reavaliação integral por padrão é cara — e o que é caro deixa de ser feito) ou nenhuma como material (perde o controle).
- Aprovar a mudança "rapidinho" fora do processo: cada bypass é uma exceção não registrada esperando para virar incidente.

**Onde está a profundidade.** Material change em [cap. 05](05-agent-lifecycle.md) e [cap. 09](09-operations-incidents-and-continuity.md#43-gestao-de-mudancas).

### 6.7 P7 — Revisão periódica e auditoria

**O que é e por que importa.** É a revalidação calendarizada de que o agente continua necessário, seguro, aderente e com owners vivos. Agentes não envelhecem sozinhos: perdem uso, perdem owner, acumulam permissões obsoletas. A revisão periódica — a attestation — é o processo que decide **manter, corrigir, restringir ou aposentar** com base em evidência atual, não em fé.

**Quando dispara.** Passagem do período definido por tier (ex.: mais curto para T3/T4); planejamento de auditorias internas ou externas; evento material que antecipe a revisão.

**Quem responde.** **Run Authority** coordena; business e technical owners participam; compliance e auditoria quando necessário.

**Entradas.** Registry com datas de próxima revisão; relatórios de consumo, incidentes e mudanças do período; policy e controles vigentes.

**Atividades.**

1. Gerar a lista de agentes com revisão vencida ou próxima e agendar com os owners.
2. Para cada agente, avaliar com evidência: uso efetivo, valor de negócio, incidentes, consumo, aderência a HITL, permissões e dados ainda necessários.
3. Identificar candidatos a otimização, redução de escopo, ajuste de cap ou sunset.
4. Registrar conclusões no registry: nova data de revisão, ações corretivas e, se aplicável, decisão de sunset.
5. Em auditorias, fornecer o pacote: autoavaliação, aprovações, checklists, incidentes e revisões — **a evidência é produzida continuamente, não preparada para a auditoria**.

**Saídas.** Revisões executadas e documentadas; ajustes ou sunsets disparados; evidências prontas para auditoria; owners reconfirmados nominalmente.

**Armadilhas comuns.**

- Attestation como assinatura sem evidência: confirmar "sim, continua ok" sem olhar dados é teatro de compliance.
- Revisão que nunca gera ação: uma revisão que termina sempre em "manter" não está examinando — está carimbando.
- Owner que saiu da empresa e registro intacto: **saída ou inatividade do owner dispara redesignação, suspensão ou aposentadoria** antes de o registro virar órfão.

**Onde está a profundidade.** Attestation em [cap. 09](09-operations-incidents-and-continuity.md); cadência e revisão de portfólio em [cap. 10](10-metrics-review-and-improvement.md).

### 6.8 P8 — Sunset

**O que é e por que importa.** É o encerramento controlado: sem owner, sem uso, duplicado, em plataforma não aprovada ou com incidente grave não corrigido — o agente sai de cena sem acessos residuais, com evidências preservadas e com a decisão registrada. O sunset bem-feito é o que impede o estate de acumular zumbis que custam e expõem.

**Quando dispara.** Agente sem owner, sem uso por período definido, duplicado, em plataforma não aprovada ou com incidente grave não resolvido no prazo; decisão de substituir ou descontinuar.

**Quem responde.** **Run Authority**, em conjunto com business e technical owner.

**Entradas.** Registry com status de uso, owners e incidentes; [plano de sunset](../../toolkit/templates/sunset-plan.md); informação de migração/substituição quando houver.

**Atividades.**

1. Marcar o agente como candidato a sunset no registry e notificar os interessados, com prazo de regularização ou confirmação.
2. Confirmado o encerramento, seguir as fases padrão com prazos definidos — ex.: **Warning (Dia 0), Quarantine (D+15), Deactivate (D+30)** — ajustadas à política.
3. Na quarentena: limitar ou desativar ações de escrita, reduzir escopo ou usuários, mantendo logs e evidências.
4. Na desativação: remover acessos, desabilitar integrações, **revogar identidades técnicas** vinculadas e registrar o motivo.
5. Registrar no registry: início do sunset, motivo, owner da decisão, plano de migração, evidência de comunicação aos usuários e política de retenção de logs.
6. Opcionalmente, arquivar configurações por período definido para rollback justificado.
7. Verificar órfãos e dependências downstream — encerrar a UI e deixar integrações ativas é o erro clássico.

**Saídas.** Agente desativado sem acessos residuais; registry com estado `retired` e documentação completa; custos encerrados; risco de zumbis eliminado.

**Armadilhas comuns.**

- Manter agente sem uso por medo de sunset: agente parado ainda custa e ainda expõe.
- Encerrar a interface e deixar conectores ativos: o agente continua operando invisível.
- Sunset sem registro do motivo e da decisão: o próximo auditor não saberá por que saiu — e o próximo proponente recriará o mesmo agente.

**Onde está a profundidade.** Sunset em [cap. 09](09-operations-incidents-and-continuity.md) e lifecycle F8 em [cap. 05](05-agent-lifecycle.md).

## 7. Tratamento de agentes existentes e shadow

Triar ativos existentes em caminhos de **registrar, restringir, remediar, migrar, suspender ou aposentar** usando um plano datado: confiança da descoberta, owner, exposição atual, controle provisório, estado-alvo, prazo e authority. **Status legado não é isenção permanente; ativos de alto risco vencidos são contidos.**

## 8. Plano opcional de piloto

> **Uso opcional.** Cohort de onboarding, phased rollout ou evidência de agentes existentes podem cumprir o mesmo objetivo. G0–G7, MPB e evidence requirements continuam iguais em qualquer rota.

Quando escolhido, o piloto existe para **testar a governança, não para provar que um modelo funciona**. Se todos os casos forem de leitura, a organização não valida identidade própria, mediação, oversight, rollback, quarentena, evidence pack ou resposta a incidente — e conclui, erradamente, que está pronta.

**Coorte:** selecione 3–4 casos que **forcem rotas diferentes**: T1 fast path (assistente pessoal), T1 revisado (Q&A de procedimentos), T2 (agente que abre chamados), T3 (agente que propõe mudança e executa após aprovação). **Não comece por T4** — primeiro demonstre fundações e containment; T4 não é sinônimo de `restricted`.

**Desenho:** selecionar coorte cobrindo leitura, transação e alto impacto; **congelar baseline** de processo, custo e qualidade antes do go-live; executar o fluxo completo; medir lead time e retrabalho **da governança**; executar um tabletop e um teste real de kill switch e quarentena; rodar behavioral analytics em monitor-only; coletar feedback separado de builder, reviewer, owner e operador; ajustar standards e thresholds **antes** de escalar.

**O que medir:** fricção (lead time por etapa e tier; retrabalho de review); cobertura (completude do registry e evidence pack); contenção (tempo até quarentena; sucesso do rollback); detecção (falsos positivos); economia (custo por resultado contra baseline); resultado (KPI contra baseline congelada); experiência (percepção dos quatro papéis).

**Critérios de expansão:** nenhum finding crítico aberto; lead time de T1 baixo o suficiente para que **contornar a governança não compense**; T2/T3 com identidade, evidência e telemetria completas; kill switch/quarentena/rollback funcionaram **no teste**; falsos positivos compreendidos; custo e resultado mensuráveis; **owners de operação regular aceitaram a responsabilidade, nominalmente.**

**Failure modes:** piloto só com leitura; medir apenas a performance do agente; go-live sem baseline congelada; kill switch testado em documento; ajustar standards depois de escalar; piloto sem owner de BAU; tratar ausência de incidente como prova de segurança.

## 9. Referência normativa

Condições mínimas que devem ser verdadeiras. Use como checklist; as seções 1–7 explicam o porquê.

| # | Obrigação | Evidência mínima | Concluído quando |
|---|---|---|---|
| R1 | Entregar a implementação como workstream com owner, dependências e critérios de saída | plano com baseline, alvo, owner, recursos, sequência, aceite, riscos, dependências, handoff | capacidade funciona em caminho representativo; ownership permanente aceita runbook e backlog |
| R2 | Estabelecer baseline datado antes de desenhar o estado-alvo | escopo, método, população, amostra, evidência, confiança, lacunas, dependências, validação | baseline distingue ausente/definida/operante e é repetível |
| R3 | Descobrir ativos por múltiplas fontes reconciliadas | fonte, última visualização, confiança, owner, identidade não resolvida, remediação | shadow/sem owner entram em contenção, não são aceitos silenciosamente |
| R4 | Desenhar capacidades-alvo a partir do baseline e contexto de risco | capacidades-alvo, authority, interfaces, artefatos, sequenciamento, aceite, premissas | toda capability fecha lacuna documentada com owner e critério mensurável |
| R5 | Selecionar e documentar modelo operacional centralizado/federado/híbrido | princípios, mapa de papéis, fronteiras, decision rights, handoffs, SLAs, exceção | caso representativo percorre do intake à operação sem decisão órfã |
| R6 | Sequenciar workstreams por dependência bloqueante e redução de risco | workstream, owner, pré-requisito, marco, entregável, aceite, risco, caminho crítico | nenhuma onda promete capacidade com fundação ausente |
| R7 | Assegurar sponsor accountable, capacidade financiada e papéis nomeados | orçamento, capacidade, competências, authority, horizonte, dependências, riscos | controles e deveres têm recursos antes da coorte ser aprovada |
| R8 | Estabelecer a fundação nomeada antes da primeira coorte | artefatos mínimos, owners, estados de controle, lacunas, teste, authority de exceção, backlog | primeira coorte completa G0–G7 com decisões rastreáveis |
| R9 | Selecionar coorte que exercite caminhos materiais sem exposição não controlada | rationale, riscos excluídos, critérios, salvaguardas, tamanho, rollback, perguntas | coorte valida o caminho completo; não substitui demo por evidência |
| R10 | Exercitar intake, risco, design, build, avaliação, release, operação e aposentadoria | timestamps, handoffs, decisões, artefatos, evidência, exceções, defeitos, remediação | todos os gates trabalham no mesmo caso; defeitos de integração bloqueiam rollout |
| R11 | Liberar por coortes com critérios de promoção, pausa e rollback | coorte, exposição, telemetria, thresholds, aprovação, resultado, incidentes, decisão | expansão só após critérios; sinal adverso interrompe ou reverte |
| R12 | Triar ativos existentes em registrar/restringir/remediar/migrar/suspender/aposentar | confiança, owner, exposição, controle provisório, estado-alvo, prazo, authority | legado não é isenção; alto risco vencido é contido |
| R13 | Fornecer defaults conformes reutilizáveis e automação preservando escalonamento | padrões, controles embutidos, contrato, versão, telemetria, suporte, escape | time completa caminho padrão com menos esforço; self-service não contorna revisão |
| R14 | Definir competências e treinamento por papel vinculado a decisões | papel, objetivo, avaliação, conclusão, expiração, remediação, owner | pessoal demonstra tarefa; competência vencida visível antes do exercício |
| R15 | Prover comunicação, suporte e feedback adequados ao papel | público, mensagem, canal, momento, owner, compreensão, feedback, ação | usuários conhecem fronteira, rota de reporte e consequência; feedback chega a owner |
| R16 | Comprovar prontidão de suporte e operação antes do handoff | aceite de serviço, assinatura, suporte, SLO, runbook testado, dívida, treinamento | BAU resolve problema representativo sem dependência do projeto |
| R17 | Operar os oito processos do ciclo (P1–P8) como rotina registrada | registros de criação, decisão, release, operação, incidente, mudança, attestation e sunset | cada processo deixa rastro recuperável; nenhum estado avança sem registro e sem authority |

## 10. Evidências, métricas e failure modes

**Evidências:** persona e stakeholder map; adoption/support plan; catalog entry e discovery analytics; learning assets; support model e escalation; training/competence records; feedback backlog e decisões; change communication; user research; decision records de cada gate (G0–G7); capability map com evidências observáveis; baseline com data de corte; relatório de piloto com decisão registrada.

**Métricas:** discovery-to-use conversion; active/recurring users por persona; duplicate creation; support demand e resolution time; training completion **e task competence**; misuse reports; feedback-to-decision time; lead time por gate e tier; rework por requirement tardio; coverage do paved road; exception rate e expiry; evidence freshness; containment/recovery readiness; cycle time por gate; devoluções por evidência incompleta; time to decide/contain/remediate; bypass attempts; coverage do registry; owners e attestations válidos; evidence packages completos por tier; exceptions e findings vencidos; drill pass rate.

**Failure modes:** medir sucesso por agentes criados; publicar sem owner ou suporte; treinamento único para todos; champion sem authority ou tempo; feedback positivo como prova de ROI; esconder limitation para aumentar adoção; ignorar resistência como "falta de cultura"; manter itens em discovery durante quarantine; comprar tecnologia para problema de processo; mapear produtos e chamar de capacidades; aprovar alvo sem owner pós-programa; piloto só com leitura; go-live sem baseline congelada; kill switch testado em documento; ajustar standards depois de escalar; tratar ausência de incidente como prova de segurança; prazo cumprido com evidência ausente tratado como approve.

## Decision gates

- **Capability map:** uma capability não é declarada implantada sem sistema atribuído, source of truth e evidência. Cobertura prometida por roadmap não é cobertura.
- **Piloto (quando houver):** a expansão exige relatório com decisão registrada e critérios atendidos. **Sem piloto, a organização apresenta evidência equivalente da primeira cohort — o gate avalia a qualidade da evidência, não o nome da rota.**
- **Release amplo:** exige catalog entry, intended use, limitations, support owner, escalation, communication e feedback channel.

## Acceptance criteria

- todas as decisões deste capítulo possuem authority, owner e evidência recuperável;
- requisitos aplicáveis estão ligados ao catálogo de controles e ao método de verificação;
- exceções têm escopo, justificativa, compensating controls, expiry e decisão residual;
- controles de build time e runtime são distinguidos e exercitados quando aplicáveis;
- mudanças materiais reabrem avaliação, aprovação e evidência;
- nenhuma alegação de conformidade, eficácia ou valor excede a evidência observada.

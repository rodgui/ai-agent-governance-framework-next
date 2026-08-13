---
title: 04 — Risco, impacto e compliance
status: maintained
maturity: validated
last_reviewed: 2026-08-13
review_cycle: quarterly
owners: [framework-maintainers]
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# 04 — Risco, impacto e compliance

## Visão geral

Todo agente de IA carrega risco. A pergunta não é *se* ele é arriscado, mas *quão arriscado é, para quem, e o que a organização está disposta a aceitar*. Este capítulo estabelece como responder essas três perguntas de forma **proporcional**: quanto maior o risco, maior o rigor exigido — sem transformar governança em burocracia para casos simples.

O capítulo separa dois conceitos que costumam ser confundidos e que **devem ser decididos separadamente**:

- **Risco (tier T1–T4):** quão severo pode ser o impacto de um agente — orienta os controles, as evidências e a autoridade de aprovação.
- **Admissibilidade:** se o uso pode operar, e sob quais condições — `permitted`, `conditional`, `restricted` ou `prohibited`.

Tratar ou aceitar risco **não transforma uso proibido em permitido**. E admissibilidade favorável **não demonstra risco baixo**. As duas dimensões coexistem no mesmo registro, mas respondem perguntas diferentes.

O fluxo completo do capítulo:

```text
Contexto e uso pretendido → identificar impactos e ameaças → classificar tier (T1–T4)
→ decidir admissibilidade → selecionar controles → testar → residual risk
→ decisão pela authority certa → operar e monitorar → reavaliar quando mudar
```

Leia as seções 1–3 para entender; use a seção 4 como checklist de implementação e auditoria.

## 1. Como classificar risco

### 1.1 Risco não é um número isolado

Classificação de risco apoia consistência, mas não substitui contexto. A postura de risco combina múltiplos fatores ajustados por controles e detectabilidade:

```text
Risk posture = impacto × likelihood × exposição × autonomia
               × capacidade de ação × irreversibilidade
               ajustado por controls e detectability
```

Não existe fórmula universal. O score apoia a decisão; a decisão preserva contexto e rationale.

As dimensões que alimentam a avaliação:

| Dimensão | Pergunta |
|---|---|
| finalidade | qual decisão, processo ou direito pode ser afetado? |
| alcance | quantas pessoas, sistemas, regiões ou transações? |
| dados | sensibilidade, qualidade, origem e obrigações? |
| autonomia | recomenda, prepara, executa, aprova ou delega? |
| capability | read, write, action, workflow, code ou efeito físico? |
| interconectividade | quantos tools, agents, APIs e downstream systems? |
| reversibilidade | o efeito pode ser desfeito com custo e tempo aceitáveis? |
| detectability | a falha aparece antes do impacto? |
| exposição | interno, externo, público ou adversarial? |
| vulnerabilidade | pessoas ou grupos podem sofrer impacto desproporcional? |
| contexto legal | há obrigação setorial, regional, contratual ou trabalhista? |
| novidade | há evidência operacional comparável ou elevada incerteza? |

### 1.2 Tiers: T1–T4 é a taxonomia canônica

T1–T4 é a taxonomia de risco/criticidade deste framework. Uma organização pode mapear classificações locais, regulatórias ou legadas, desde que preserve os critérios, documente divergências e aplique o caminho decisório **mais restritivo** quando houver ambiguidade.

| Tier | Perfil | Exemplo de controle |
|---|---|---|
| **T1 — baixo** | sugestão interna, dados não sensíveis, reversível | owner, registry, testes básicos e logging |
| **T2 — moderado** | influência operacional limitada ou dados internos | blueprint, reviewer independente, evals e monitoring |
| **T3 — alto** | escrita/ação, dados sensíveis, alto alcance ou impacto | domain approvals, threat/impact assessment, kill switch e attestation |
| **T4 — crítico** | efeito legal, financeiro, safety-critical ou difícil de reverter | authority executiva, dual control, challenge com segregation formal e containment contínuo |

> **Armadilha comum:** classificar risco apenas pelo número de usuários, ou tratar "PoC" como sinônimo de baixo risco. Um agente para 5 usuários que executa pagamentos é mais crítico que um para 5.000 que só resume documentos internos.

### 1.3 Red flags e escaladores: o fator crítico não pode ser diluído

Red flags elevam a criticidade **independentemente do score**. Eles existem porque uma média esconde um fator crítico: um caso com dez respostas benignas e uma destrutiva **não é um caso médio**. Qualquer red flag retira o caso do fast path. A coluna de criticidade é **piso, não teto** — o scoring pode chegar mais alto, nunca mais baixo.

| Red flag | Criticidade mínima | Efeito adicional |
|---|---|---|
| dados restritos enviados a provedor externo | **T4** | admissibilidade `restricted` por padrão: default deny, com exceção explícita, authority e expiry |
| descoberta irrestrita de tools ou MCP externos em runtime | **T4** | admissibilidade `restricted` por padrão; o conjunto de capacidades deixa de ser conhecido no momento da aprovação |
| execução de código ou comandos arbitrários | **T4** | mediação obrigatória e isolamento; sem allowlist, a capability é ilimitada por construção |
| deleção irreversível ou mudança destrutiva | **T4** | dual control onde aplicável; contenção testada antes do release |
| modificação de identidade, permissão ou secrets | **T3** | o agente passa a poder ampliar o próprio privilégio; segregação e logging forense |
| acesso privilegiado ou administrativo | **T3** | JIT e monitoramento contínuo; privilégio permanente exige justificativa própria |
| decisão sobre emprego, crédito, elegibilidade ou acesso a serviço | **T3** | impact assessment formal obrigatório e canal de contestação, mesmo em caso tecnicamente simples |
| processo safety-critical ou de tecnologia operacional | **T3** | domain review do processo físico; failure containment exercitado |
| execução de transação financeira material | **T3** | limite por transação e por período, reconciliação e rollback testado |
| comunicação pública autônoma e em escala, sem revisão humana | **T3** | as três condições somadas — pública, autônoma e em escala — é que fazem o escalador; separadas, cada uma é menos grave |

Duas observações sobre admissibilidade: red flags governam **criticidade**; apenas os dois primeiros carregam um default de admissibilidade, porque neles a restrição é do uso em si, não da severidade do impacto. E `restricted` **por padrão** não significa proibido: significa que operar exige exceção registrada, e não silêncio.

> A lista de red flags é a norma; o [pre-screen](../../toolkit/templates/risk-pre-screen.md) é o instrumento. Se divergirem, a lista prevalece e o instrumento é corrigido — nunca o contrário.

### 1.4 Fast path de T1: automatizar o simples, sem eliminar controle

Em estates com alto volume de casos simples, exigir revisão humana caso a caso transforma a governança em gargalo — e a organização passa a contorná-la. O fast path é a rota **automatizada** de T1.

O fast path elimina revisão manual caso a caso. Ele **não** elimina controle. Permanecem obrigatórios:

- descoberta e registro com `agent_id` e owner atribuído;
- logging básico e telemetria mínima recuperável;
- uso restrito a fontes de dados e tools já aprovadas;
- termos de uso aceitos pelo owner;
- evidência proporcional e recuperável da classificação.

**A saída do fast path é automática**: qualquer red flag, escalador ou impact trigger remove o agente da rota rápida e exige a rota do tier resultante. A entrada é que precisa ser conquistada — na dúvida, o caso não entra.

> Materiais externos que usem `T0` convergem para T1: `T0` e `T1` externos mapeiam para o T1 canônico. `Restricted` do guia v3.4 mapeia para admissibilidade, não redefine T4.

### 1.5 O mapa de decisão: como risco, RAI e aprovação se encadeiam

A dificuldade mais comum neste domínio é tratar scoring, Responsible AI e aprovação como controles concorrentes. **Eles não competem — funcionam em sequência:** o pre-screen coleta fatos; o scoring estima o risco base; os red flags corrigem fatores que não podem ser diluídos; o tier define a intensidade mínima de governança; o impact trigger identifica impactos sobre pessoas; o RAI impact assessment aprofunda esses impactos quando acionado; os domain reviews tratam controles especializados; e o publication gate apenas verifica se as evidências exigidas estão completas.

**Fluxo mental recomendado:**

```text
PRE-SCREEN → SCORING → RED FLAGS → TIER + ADMISSIBILIDADE
  → IMPACT TRIGGER → RAI IMPACT ASSESSMENT (quando acionado)
  → DOMAIN REVIEWS (por gatilho) → PUBLICATION GATE
```

Uma etapa não substitui a anterior, e nem todas exigem trabalho manual. A matriz abaixo é o **mapa de calor operacional** — lida horizontalmente por tier e verticalmente por mecanismo, mostra quanta formalidade cada combinação exige:

| Mecanismo | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| **Pre-screen + scoring** | automatizável (fast path) | obrigatório | formal | formal + enhanced (identifica uso restrito) |
| **Red flags** | sempre checar | sempre checar | sempre checar | críticos / default deny |
| **Impact trigger screen** | obrigatório | obrigatório | obrigatório | obrigatório se exceção for analisada |
| **RAI impact assessment** | somente se trigger | formal se trigger | formal/aprofundado quando trigger | obrigatório se exceção envolver impacto |
| **Domain reviews** | por trigger | formais por trigger | multidisciplinares | autoridade máxima + especialistas |
| **Publication gate** | owner + policy gate (automatizável) | formal evidence gate | formal + assurance | sem rota normal de publicação |

Legenda: **T1** = leve/automatizável · **T2** = obrigatório ou condicional · **T3** = formal/enhanced · **T4** = crítico.

**T4 não representa, por si só, default deny.** T4 define criticidade e exige assurance, authority, containment e evidência proporcionais. `restricted` e `prohibited` pertencem à dimensão independente de admissibilidade. Um caso T4 pode ser `conditional` ou `permitted` quando a finalidade, a authority e os controls aprovados sustentarem essa decisão; um caso T1 também pode ser `restricted` ou `prohibited` por finalidade, obrigação ou desenho. Os red flags que determinam `restricted` por padrão continuam exigindo exceção explícita, authority, expiry e monitoramento contínuo.

A [ferramenta de classificação](../../toolkit/templates/risk-scoring-worksheet.md) operacionaliza este mapa: ela aplica as sete dimensões de scoring, os red flags e o impact trigger para produzir tier, admissibilidade e a lista de reviews acionadas. A lógica normativa vive aqui; a ferramenta executa e registra.

### 1.6 Admissibilidade: uma dimensão separada do risco

Risk tier responde **quão severo pode ser o impacto**. Admissibilidade responde **se e sob quais condições o uso pode operar**. Um T1 pode ser proibido por finalidade ou obrigação legal; um T4 pode ser admitido quando authority, controles e evidências compatíveis existirem.

| Admissibilidade | Regra de decisão |
| --- | --- |
| `permitted` | pode operar dentro do blueprint e dos controls aprovados |
| `conditional` | pode operar somente enquanto condições documentadas forem satisfeitas |
| `restricted` | default deny; exige exceção explícita, temporária, com authority e expiry |
| `prohibited` | não entra nem permanece em produção no escopo avaliado |

Tier e admissibilidade são registrados juntos no [Agent Risk Record](../../toolkit/templates/agent-risk-record.md), no Registry, no Blueprint e no release evidence manifest. **Mudança em qualquer dimensão é mudança material.**

O piso de controles exigido por tier para entrar e permanecer em produção está no [Minimum Production Bar](../../toolkit/controls/minimum-production-bar.md).

> **Artefatos para produzir agora — classificação e admissibilidade.** Use o [Risk pre-screen](../../toolkit/templates/risk-pre-screen.md) para coletar fatos e acionar escaladores; use o [Risk Scoring Worksheet](../../toolkit/templates/risk-scoring-worksheet.md) para calcular o risco base, aplicar red flags e produzir a rota de review; registre a decisão no [Agent Risk Record](../../toolkit/templates/agent-risk-record.md). O template operacionaliza a norma, mas não substitui o rationale, a authority ou a decisão deste capítulo.

### 1.7 Regras de uso: o que é permitido, o que exige aprovação, o que é proibido

As regras abaixo são simples e objetivas, aplicáveis em todos os níveis (Grupo/Segmento/Local) e a qualquer plataforma aprovada. Elas servem de referência para self-assessment e auditoria. Fornecedores e parceiros que desenvolvem ou operam agentes em nome da empresa devem cumprir integralmente esta política e seus anexos.

**Permitido (sempre):**
- usar apenas dados e sistemas com autorização explícita;
- operar com HITL nos pontos de decisão;
- registrar as ações do agente em log imutável;
- exibir identificação visível ("Governed Agent").

**Exige aprovação:**
- acesso a dados pessoais/sensíveis (DPIA quando aplicável);
- integração com sistemas críticos;
- uso em decisões que impactam KPIs críticos (produção, segurança, qualidade, OWCR etc.).

**Proibido:**
- agentes sem owner designado;
- ações irreversíveis sem HITL;
- armazenar dados pessoais fora de repositórios aprovados;
- contornar controles de segurança, jailbreaks ou uso não autorizado de dados;
- usar plataformas, modelos ou ferramentas de IA de terceiros sem aprovação formal da plataforma e aderência total a esta política.

> **Armadilha comum:** zerar risco porque existe approval. Aprovação não reduz risco por si; ela registra que o risco foi avaliado e aceito pela autoridade certa. Sem expiry e revisão, a "aceitação" vira dívida permanente.

## 2. Avaliação de impacto (Responsible AI)

### 2.1 O que é Responsible AI (e o que não é)

Responsible AI **não é sinônimo de content filter**. É a aplicação verificável de princípios, assessments, design choices, controles, avaliações, transparência e resposta. O objetivo: avaliar e controlar impactos em pessoas, grupos, direitos e sociedade ao longo do lifecycle, preservando accountability humana e independência suficiente entre build e assurance.

O **assurance plane** reúne as especialidades que testam se o sistema atende aos requisitos e ao contexto aprovado: Responsible AI, privacy e data protection, security e safety, legal e compliance, accessibility e inclusão, model/system evaluation e independent review quando exigido. Ele complementa o control plane — registry, postura técnica e telemetria não demonstram sozinhos tratamento adequado de impacto.

Os princípios de avaliação orientam perguntas; **não funcionam como checklist universal**:

- **validade e confiabilidade:** desempenho suficiente no contexto real;
- **safety:** danos previsíveis identificados e mitigados;
- **security e resilience:** resistência e recuperação;
- **accountability e transparência:** owners, decisões e comunicação;
- **explicabilidade proporcional:** informação útil para decisão e contestação;
- **privacy:** finalidade, minimização e direitos;
- **fairness:** impactos e desempenho entre grupos relevantes;
- **human agency:** supervisão, contestação e limites de automação.

### 2.2 Impact assessment: as 10 perguntas

A avaliação de impacto deve responder:

1. qual objetivo e qual alternativa não-IA foram considerados;
2. quem usa, quem é afetado e quem pode ser vulnerável;
3. quais decisões ou direitos podem ser influenciados;
4. quais dados, proxies e representações são usados;
5. quais harms, benefits e distributional effects são plausíveis;
6. onde automation bias, over-reliance ou contestability importam;
7. quais métricas e slices são materialmente relevantes;
8. quais human controls e redress mechanisms existem;
9. quais limitações precisam ser comunicadas;
10. qual residual impact permanece e quem pode aceitá-lo.

### 2.3 Tiering de assurance: quanto rigor por tier

"RAI mínimo" é a evidência mínima esperada naquele tier, **não um teto**. Um caso T1 que dispara impact trigger executa o assessment formal do mesmo jeito — o tier determina proporcionalidade, o trigger determina obrigatoriedade.

| Tier | Assurance mínima | Quando evoluir para assessment formal | Efeito na aprovação |
|---|---|---|---|
| **T1 — baixo** | intended use, limitations, basic quality e owner review | qualquer `sim` no impact trigger screen; uso por população vulnerável; reclamação recorrente | owner aprova dentro da rota automatizada; RAI não entra na fila |
| **T2 — moderado** | impact assessment, slices relevantes e user transparency | decisão que influencia direitos, oportunidades ou acesso a serviço; dado pessoal sensível; proxy de atributo protegido | aprovação condicionada às mitigações registradas e ao residual impact aceito por quem responde pelo processo |
| **T3 — alto** | domain review, adversarial/edge testing, human oversight e monitoring | disparidade material entre grupos; automation bias observado; mudança de população ou de contexto de uso | RAI é authority de veto no gate; sem oversight design e evaluation por slices, o release não passa |
| **T4 — crítico** | challenge com segregation formal, contestability, continuous review e executive authority | sempre — em T4 o assessment formal é a linha de base, não uma evolução | aprovação executiva com residual impact explícito; ausência de contestability é bloqueador, não finding |

### 2.4 Impacto em pessoas: avaliação por categoria

A avaliação de impacto se aplica a cada categoria de efeito sobre pessoas, grupos, direitos e ambiente. O método é o mesmo; o que muda é a profundidade conforme o contexto e o tier. As categorias: efeitos sobre posição legal e oportunidades de vida; segurança física e psicológica; direitos humanos e direitos fundamentais; efeitos sociais e ambientais; acessibilidade e populações vulneráveis.

Para cada categoria, registre: população afetada, via de impacto, severidade, probabilidade, distribuição, mitigação, impacto residual, consulta e owner. **Impactos materiais são testados com evidência do contexto afetado; impacto inaceitável não resolvido bloqueia implantação ou expansão.**

### 2.5 Fairness: uma métrica agregada pode esconder falha grave

- selecionar grupos/slices com base em contexto e impacto, não apenas disponibilidade;
- comparar performance e harms com baseline adequado;
- registrar incerteza e tamanho de amostra;
- investigar proxies e feedback loops;
- definir threshold, owner e ação para disparidade;
- reavaliar após mudança material ou drift.

**Concluído quando:** desempenho agregado não pode esconder uma fatia material reprovada e dano não resolvido é escalonado à authority adequada.

### 2.6 Transparência, contestabilidade e supervisão humana

**Transparência.** A comunicação adequada pode incluir: que IA está sendo usada; finalidade e limites; dados relevantes e fontes quando aplicável; grau de automação; necessidade de revisão humana; como reportar erro, contestar ou obter suporte; owner e canal de responsabilidade. Transparência não exige expor secrets, dados pessoais ou detalhes que aumentem abuso — precisa ser útil para a pessoa afetada.

**Human agency.** Quando o sistema influencia decisão material: a pessoa entende o papel da IA; um humano possui autoridade real, não ritual; há canal de contestação e correção; revisão humana recebe tempo, contexto e competência; o sistema registra override e outcome; automation bias é monitorado.

**Supervisão humana.** O humano deve estar posicionado em um ponto de decisão onde a intervenção permaneça **oportuna, informada e tecnicamente eficaz** — e conseguir detectar, interromper, corrigir e escalonar uma falha representativa em vez de carimbar uma ação irreversível.

### 2.7 Privacidade, propriedade intelectual e integridade da informação

**Privacidade e proteção de dados.** Estabelecer finalidade, base legal, minimização, tratamento de direitos, retenção e restrições de transferência para dados pessoais. Reter categorias de dados, titulares, origem, finalidade de processamento, acesso, fluxo, DPIA ou equivalente, testes e evidência de exclusão. **Concluído quando:** caminhos de dados não autorizados falham em teste, direitos dos titulares são operáveis e mudança material de processamento reabre a avaliação.

**Propriedade intelectual.** Verificar direitos e restrições para treinamento, recuperação, prompts, saídas, código e conteúdo gerado: licença da fonte, permissão, atribuição, restrição de uso, rota de takedown, filtro ou controle e alegação não resolvida. **Concluído quando:** conteúdo sem licença ou incompatível é bloqueado ou removido e obrigações a jusante permanecem rastreáveis.

**Integridade da informação.** Definir factualidade aceitável, qualidade de fonte e limites de conteúdo prejudicial para o contexto de uso: categorias de afirmação, fontes autoritativas, conjunto de teste, verificações de citação, thresholds, exemplos de falha e resposta. **Concluído quando:** alegações materiais sem suporte são detectadas ou divulgadas e falha acima do threshold bloqueia ou restringe o uso.

### 2.8 Segurança, abuso e risco de terceiros

**Segurança e risco de abuso.** Modelar ameaças através das fronteiras de identidade, prompt, dados, ferramenta, runtime e supply chain e testar caminhos materiais de abuso: threat model, cenários, pré-condições de ataque, evidência de teste, descobertas, mitigações, risco residual e resultado de reteste. **Concluído quando:** caminhos de ataque de alto impacto são prevenidos ou contidos e descobertas bloqueantes abertas impedem o release.

**Risco de terceiros e cadeia de valor.** Governar fornecedores e dependências a jusante por due diligence, contrato, monitoramento e planejamento de saída: serviço, owner, criticidade, evidência, obrigações, concentração, incidentes, subprocessadores, fallback e teste de saída. **Concluído quando:** falha do fornecedor dispara a contenção ou fallback acordado e a accountability permanece com a organização.

**Security, data e compliance (GDPR/LGPD e SOX/ITGC).** Agentes podem processar dados pessoais, sensíveis e confidenciais e interagir com sistemas sujeitos a controles internos. Requisitos mínimos: access controls (RBAC/ABAC), segregação de funções e least privilege; criptografia em trânsito e em repouso, DLP, SIEM e gestão de vulnerabilidades; princípios da lei aplicável (GDPR/LGPD), registro de processamento, DPIA, direitos dos titulares e DPO; SOX/ITGC com trilhas de auditoria, aprovações formais e segregação para ações críticas. Modelos e dados usados por agentes devem ser avaliados quanto a viés, qualidade e adequação ao uso pretendido **antes da publicação e sempre que atualizados**.

### 2.9 Self-assessment obrigatório

Para escalar agentes com segurança, **todo agente** passa por avaliação padronizada antes de ser liberado, expandido ou significativamente alterado. O Self-Assessment é um formulário de 1 página, obrigatório antes de criar/publicar um agente, que funciona como triagem e registro de accountability — e como gatilho de escalonamento: quando há red flags, a rota segue para o tier, a admissibilidade, as domain reviews e a authority definidos nos [decision rights](02-governance-and-accountability.md) e nos [decision gates](08-implementation-and-adoption.md).

Campos mínimos: objetivo e casos de uso; justificativa do uso de IA; dados (tipos/sensibilidade, bases, owners); permissões e escopo de ação; autonomia e HITL (pontos de controle); interconexões (sistemas/APIs); AI Impact Assessment (para alto risco); usuários/alcance (número e perfis); impacto em KPIs; riscos (privacidade, SOX, reputação etc.); controles (auditoria, rate-limit, budget cap); evidência de feedback do usuário (quando aplicável); owners e plano de sunset.

### 2.10 Risk assessment por blast radius

Agentes diferem de aplicações tradicionais porque acessam múltiplas fontes de dados, acionam tools e operam em escala (usuários, sistemas e volume). O método padronizado de avaliação do "blast radius" considera: dados acessados, privilégios, canais de saída, capacidade de ação e número de usuários. O resultado orienta o nível de aprovação, os controles mínimos e o regime de monitoramento/custo aplicável.

## 3. Tratamento, aceite e reavaliação

### 3.1 Tratamento de risco e compensating controls

Selecione tratamentos que **reduzam o risco identificado** e documente por que a exposição residual é aceitável ou permanece bloqueada: vínculo risco-controle, owner do controle, estado de implementação, teste de eficácia, limite compensatório e classificação residual. **Concluído quando:** o tratamento passa no teste de eficácia e um controle compensatório expira junto com a condição que o justificava.

### 3.2 Decisão de risco residual: quem pode aceitar

O risco residual após tratamento verificado deve ser apresentado à **authority empoderada** para aquela exposição: risco inerente, evidência de tratamento, classificação residual, incerteza, condições de aceite, aprovador e expiração.

Regras duras:
- **o time de entrega não pode auto-aceitar risco residual material;**
- o aceite não sobrepõe admissibilidade ou lei;
- risco não pode ser "aceito" pelo technical owner se o impacto pertence ao negócio, a pessoas ou a obrigação de outro domínio;
- risk acceptance **não transforma uso `prohibited` em permitido**; para uso `restricted`, a exceção é registro distinto, temporário e revogável.

### 3.3 Mudança material: quando reclassificar

Reclassificar quando muda: finalidade ou população; modelo ou provider relevante; dados, connector ou região; identidade, scope ou tool; autonomia ou capability; volume, alcance ou criticidade; UI/approval flow; incident, finding ou external threat; obrigação legal ou risk appetite.

**O reassessment recomeça do ponto afetado, não do zero.** Reassessment integral por padrão é caro, e o que é caro deixa de ser feito.

### 3.4 Crosswalk regulatório e de normas

Mapear obrigações e normas **somente onde uma fonte primária ou adequadamente atribuída suporta a relação**: fonte, versão, cláusula ou disposição, artefato mapeado, tipo de relação, cobertura, ressalva e revisor. O crosswalk distingue alinhamento de compliance e **não inventa mapeamentos** para texto proprietário inacessível. Este framework usa NIST AI RMF e o AI Act europeu como referências de alinhamento, sem afirmar equivalência regulatória.

## 4. Referência normativa

Condições mínimas que devem ser verdadeiras em cada ponto do fluxo de risco. Use como checklist de implementação e auditoria; as seções 1–3 explicam o porquê de cada item.

| # | Obrigação | Evidência mínima | Concluído quando |
|---|---|---|---|
| R1 | Aprovar método repetível de gestão de risco (contexto, identificação, análise, tratamento, residual, revisão) | método com escalas, tiering, admissibilidade, qualidade de evidência, authority, incerteza e gatilhos | dois avaliadores qualificados alcançam resultados consistentes; evidência ausente não vira "risco baixo" |
| R2 | Analisar contexto real de decisão, usuários, pessoas afetadas, escala, autonomia, ambiente e alternativa não-IA | usos pretendidos e excluídos, premissas, dependências, grupos afetados, consequências de falha, corte de evidências | risco, avaliação e supervisão baseiam-se no contexto operacional, não em descrição genérica de modelo |
| R3 | Identificar uso indevido previsível, abuso, viés de automação, expansão de escopo e interação emergente antes do release | ator de ameaça ou usuário, cenário, pré-condição, impacto, detecção, controle preventivo, resposta, exposição residual | cenários materiais testados ou restritos; uso indevido observado alimenta controles e reavaliação |
| R4 | Classificar com critérios aprovados, escaladores obrigatórios e resultado mais severo | resultados por critério, red flags, rationale, confiança, revisor e rota resultante | mesma evidência produz encaminhamento consistente; sub-classificação é detectada |
| R5 | Definir red flags não discricionárias que elevem revisão, controles ou authority | definição do gatilho, fonte de detecção, tier mínimo, revisores exigidos, ações bloqueadas, disposição | flag acionada não é dispensada pelo solicitante e permanece aberta até disposição autorizada |
| R6 | Classificar usos como permitted, conditional, restricted ou prohibited independentemente do risco | origem da regra, condições, uso afetado, rationale, authority, expiração, workarounds proibidos | uso proibido não prossegue por compensating controls; uso conditional não opera após expirar |
| R7 | Avaliar efeitos benéficos e adversos plausíveis sobre pessoas, grupos, direitos e ambiente | população afetada, via de impacto, severidade, probabilidade, distribuição, mitigação, residual, consulta, owner | impactos materiais testados com evidência do contexto; impacto inaceitável não resolvido bloqueia implantação |
| R8 | Estabelecer finalidade, base legal, minimização, direitos, retenção e restrições de transferência para dados pessoais | categorias, titulares, origem, finalidade, acesso, fluxo, DPIA ou equivalente, testes, exclusão | caminhos não autorizados falham em teste; direitos dos titulares operáveis; mudança material reabre avaliação |
| R9 | Definir danos de fairness específicos do contexto, grupos, fatias e disparidade aceitável antes de testar | rationale do grupo, métricas, adequação da amostra, thresholds, resultados, incerteza, mitigações, residual | desempenho agregado não esconde fatia material reprovada; dano não resolvido escalona à authority |
| R10 | Fornecer aviso oportuno, limitações materiais, owner accountable e rota de contestação/reparação | aviso aprovado, público, canal, explicação, SLA de reclamação, escalonamento, resultado, remediação | pessoas afetadas identificam a interação, alcançam humano responsável e obtêm revisão/reparação no alvo |
| R11 | Definir explicação necessária para usuários, afetados, operadores e revisores no contexto real | público, decisão, conteúdo da explicação, método, limites de fidelidade, momento, evidência de compreensão | explicação suporta ação/contestação sem revelar informação protegida nem exagerar certeza |
| R12 | Posicionar humano competente onde a intervenção seja oportuna, informada e tecnicamente eficaz | gatilho, informações apresentadas, authority, tempo de resposta, override, carga, treinamento, teste | humano detecta, interrompe, corrige e escala falha representativa em vez de carimbar ação irreversível |
| R13 | Verificar direitos e restrições para treinamento, recuperação, prompts, saídas, código e conteúdo | licença, permissão, atribuição, restrição de uso, takedown, filtro, alegação não resolvida | conteúdo sem licença bloqueado/removido; obrigações a jusante rastreáveis |
| R14 | Definir factualidade aceitável, qualidade de fonte e limites de conteúdo prejudicial | categorias de afirmação, fontes autoritativas, conjunto de teste, citações, thresholds, falhas, resposta | alegações materiais sem suporte detectadas/divulgadas; falha acima do threshold bloqueia uso |
| R15 | Modelar ameaças por fronteira e testar caminhos materiais de abuso | threat model, cenários, pré-condições, evidência de teste, descobertas, mitigações, residual, reteste | caminhos de alto impacto prevenidos/contidos; descobertas bloqueantes abertas impedem release |
| R16 | Governar fornecedores por due diligence, contrato, monitoramento e saída | serviço, owner, criticidade, evidência, obrigações, concentração, incidentes, subprocessadores, fallback, teste de saída | falha do fornecedor dispara contenção/fallback acordado; accountability permanece com a organização |
| R17 | Selecionar tratamentos que reduzam risco e documentar residual | vínculo risco-controle, owner, estado, teste de eficácia, limite compensatório, classificação residual | tratamento passa no teste de eficácia; compensatório expira com a condição que o justificava |
| R18 | Apresentar residual risk à authority empoderada para aquela exposição | risco inerente, evidência de tratamento, residual, incerteza, condições de aceite, aprovador, expiração | time de entrega não auto-aceita residual material; aceite não sobrepõe admissibilidade ou lei |
| R19 | Mapear obrigações e normas somente com fonte primária ou atribuída | fonte, versão, cláusula, artefato mapeado, tipo de relação, cobertura, ressalva, revisor | crosswalk distingue alinhamento de compliance; não inventa mapeamentos |
| R20 | Definir mudanças materiais e eventos que reabrem risco | gatilho, fonte de detecção, ativos/evidências impactados, controle provisório, owner, vencimento, disposição | ativos acionados não dependem indefinidamente de aprovação anterior |

## 5. Playbook: fluxo risco → impacto → aprovação

Classificação, impact assessment e aprovação **não são três aprovações concorrentes**. Resolvem problemas diferentes e operam em sequência:

1. **Pre-screen no intake** com perguntas objetivas sobre dados, autonomia, ações, pessoas afetadas e alcance. Use o [template de risk pre-screen](../../toolkit/templates/risk-pre-screen.md).
2. **Calcular o risco base e aplicar os red flags.** O score apoia consistência; os red flags impedem que um fator crítico seja diluído por uma média.
3. **Definir o tier preliminar e a admissibilidade.** Tier determina proporcionalidade; admissibilidade determina se o uso é permitido, condicionado, restrito ou proibido.
4. **Selecionar os controles obrigatórios** correspondentes, conforme o [Minimum Production Bar](../../toolkit/controls/minimum-production-bar.md).
5. **Aplicar o impact trigger screen.** O agente influencia direitos, oportunidades, acesso a serviços, decisões sobre pessoas, segurança física, comunicação pública ou processo regulado? Se sim, executa-se o impact assessment formal — **mesmo em caso tecnicamente simples**.
6. **Acionar domain reviews apenas quando relevantes.** Privacidade por dados pessoais; segurança por ferramentas e privilégio; dados por fontes; arquitetura por mudança de pattern; jurídico por obrigação aplicável. Review acionada por regra fixa vira fila.
7. **Registrar riscos, admissibilidade, mitigações, residual risk e owner.** **Nenhuma review aprovada deve existir sem residual risk explícito** e sem a authority compatível com o tier e a admissibilidade.
8. **Compilar o evidence pack.** O gate de publicação verifica a evidência exigida pelo tier — ele não refaz as reviews. Ver [evidence pack por tier](07-evaluation-evidence-and-assurance.md).
9. **Após mudança material, o reassessment recomeça do ponto afetado**, não do zero. Reassessment integral por padrão é caro, e o que é caro deixa de ser feito.

## 6. Risk register, evidências, métricas e antipatterns

**Risk register mínimo:** risk ID e categoria; scenario e affected parties; source/cause; likelihood, impact e uncertainty; existing controls e eficácia observada; residual risk; admissibilidade, rationale, condições ou exception/expiry; owner e decision authority; treatment, due date e status; indicators e escalation threshold; evidências; review trigger e expiry.

**Categorias de risco:** business/value e uso inadequado; fairness e impacto em pessoas; privacy e data protection; security e adversarial misuse; safety e harmful content; reliability, quality e hallucination; identidade, autorização e excessive agency; tool/MCP e supply chain; operações, resilience e incident response; jurídico, regulatório e propriedade intelectual; reputação, comunicação e transparência; concentração, vendor e systemic risk; environmental e resource consumption quando material.

**Evidências:** context map; impact/threat assessments; tier rationale; control mapping; test results; residual risk decision; runtime indicators; incidents e remediação; attestation e reclassification history.

**Métricas:** riscos sem owner ou due date; findings e exceptions vencidos; tier changes após incidentes; controls sem evidence de eficácia; tempo entre trigger e reavaliação; residual risks sem authority adequada; concentração por provider, modelo ou tool; incidentes por categoria e recurrence.

**Antipatterns:**
- score único sem narrativa;
- classificar risco apenas pelo número de usuários;
- usar "PoC" como sinônimo de baixo risco;
- copiar thresholds de outro contexto;
- zerar risco porque existe approval;
- aceitar risco sem expiry;
- medir apenas likelihood e impact, ignorando detectability e reversibilidade;
- congelar classificação após release;
- tratar Responsible AI como aprovação final;
- usar princípios sem controles ou evidências;
- medir fairness sem affected-party analysis;
- confundir explicação técnica com comunicação útil;
- usar humano como rubber stamp;
- não oferecer contestação;
- inferir ausência de impacto porque não houve reclamação;
- deixar o builder aceitar sozinho residual impact.

## Decision gate

Sistemas com impacto material em pessoas **não passam** pelo release gate sem: impact assessment, oversight design, evaluation por slices relevantes, transparency plan e authority compatível com o tier. Sistemas com red flag material não passam sem residual risk explícito aceito pela authority correta. Nenhuma alegação de conformidade, eficácia ou valor excede a evidência observada.

## Acceptance criteria

- todas as decisões deste capítulo possuem authority, owner e evidência recuperável;
- requisitos aplicáveis estão ligados ao catálogo de controles e ao método de verificação;
- exceções têm escopo, justificativa, compensating controls, expiry e decisão residual;
- controles de build time e runtime são distinguidos e exercitados quando aplicáveis;
- mudanças materiais reabrem avaliação, aprovação e evidência;
- nenhuma alegação de conformidade, eficácia ou valor excede a evidência observada.

---

## Provenance (machine-readable)

Os marcadores abaixo preservam a rastreabilidade das unidades da fonte e não alteram o significado normativo. São invisíveis no site.

<!-- source-unit {"classification": "exception-limitation", "end_line": "76", "index": 1, "source_field": "", "source_heading": "5. Do’s & Don’ts (Usage Rules)", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "73", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "82", "index": 2, "source_field": "", "source_heading": "5.1 Allowed", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "77", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "decision-authority", "end_line": "87", "index": 3, "source_field": "", "source_heading": "5.2 Requires Approval", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "83", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "94", "index": 4, "source_field": "", "source_heading": "5.3 Prohibited", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "88", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "111", "index": 5, "source_field": "", "source_heading": "6. Self-Assessment (Mandatory)", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "95", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "risk-failure-mode", "end_line": "130", "index": 6, "source_field": "", "source_heading": "9. Risk Assessment (Blast Radius)", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "128", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "191", "index": 7, "source_field": "", "source_heading": "13. Security, Data, and Compliance (applicable data protection law (e.g., GDPR/LGPD)/SOX)", "source_path": "docs/governance/ai-agent-policy-and-governance-v1.md", "start_line": "184", "transformation": "archive-verbatim-and-integrate-unique-content", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "metadata-title", "end_line": "2", "index": 8, "source_field": "title", "source_heading": "", "source_path": "docs/responsible-ai/README.md", "start_line": "2", "transformation": "integrate-completely", "unit_type": "frontmatter-title"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "16", "index": 9, "source_field": "", "source_heading": "Responsible AI e assurance", "source_path": "docs/responsible-ai/README.md", "start_line": "15", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "objective", "end_line": "22", "index": 10, "source_field": "", "source_heading": "Objetivo", "source_path": "docs/responsible-ai/README.md", "start_line": "17", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "36", "index": 11, "source_field": "", "source_heading": "Assurance plane", "source_path": "docs/responsible-ai/README.md", "start_line": "23", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "49", "index": 12, "source_field": "", "source_heading": "Princípios de avaliação", "source_path": "docs/responsible-ai/README.md", "start_line": "37", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "64", "index": 13, "source_field": "", "source_heading": "Impact assessment", "source_path": "docs/responsible-ai/README.md", "start_line": "50", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "75", "index": 14, "source_field": "", "source_heading": "Tiering de assurance", "source_path": "docs/responsible-ai/README.md", "start_line": "65", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "89", "index": 15, "source_field": "", "source_heading": "Transparência", "source_path": "docs/responsible-ai/README.md", "start_line": "76", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "100", "index": 16, "source_field": "", "source_heading": "Fairness e performance", "source_path": "docs/responsible-ai/README.md", "start_line": "90", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "111", "index": 17, "source_field": "", "source_heading": "Human agency e contestability", "source_path": "docs/responsible-ai/README.md", "start_line": "101", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "evidence-artifact", "end_line": "124", "index": 18, "source_field": "", "source_heading": "Evidências", "source_path": "docs/responsible-ai/README.md", "start_line": "112", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "metric", "end_line": "135", "index": 19, "source_field": "", "source_heading": "Métricas", "source_path": "docs/responsible-ai/README.md", "start_line": "125", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "risk-failure-mode", "end_line": "146", "index": 20, "source_field": "", "source_heading": "Failure modes", "source_path": "docs/responsible-ai/README.md", "start_line": "136", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "requirement-control", "end_line": "149", "index": 21, "source_field": "", "source_heading": "Decision gate", "source_path": "docs/responsible-ai/README.md", "start_line": "147", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "metadata-title", "end_line": "2", "index": 22, "source_field": "title", "source_heading": "", "source_path": "docs/risk-management/README.md", "start_line": "2", "transformation": "integrate-completely", "unit_type": "frontmatter-title"} -->
<!-- source-unit {"classification": "risk-failure-mode", "end_line": "18", "index": 23, "source_field": "", "source_heading": "Gestão proporcional de riscos de IA e agentes", "source_path": "docs/risk-management/README.md", "start_line": "17", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "objective", "end_line": "24", "index": 24, "source_field": "", "source_heading": "Objetivo", "source_path": "docs/risk-management/README.md", "start_line": "19", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "risk-failure-mode", "end_line": "36", "index": 25, "source_field": "", "source_heading": "Risco não é um número isolado", "source_path": "docs/risk-management/README.md", "start_line": "25", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "53", "index": 26, "source_field": "", "source_heading": "Dimensões", "source_path": "docs/risk-management/README.md", "start_line": "37", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "64", "index": 27, "source_field": "", "source_heading": "Tiers", "source_path": "docs/risk-management/README.md", "start_line": "54", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "risk-failure-mode", "end_line": "87", "index": 28, "source_field": "", "source_heading": "Red flags e escaladores", "source_path": "docs/risk-management/README.md", "start_line": "65", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "103", "index": 29, "source_field": "", "source_heading": "Fast path de T1", "source_path": "docs/risk-management/README.md", "start_line": "88", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "118", "index": 30, "source_field": "", "source_heading": "Admissibilidade é uma dimensão separada", "source_path": "docs/risk-management/README.md", "start_line": "104", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "procedure", "end_line": "137", "index": 31, "source_field": "", "source_heading": "Processo", "source_path": "docs/risk-management/README.md", "start_line": "119", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "procedure", "end_line": "151", "index": 32, "source_field": "", "source_heading": "Playbook do fluxo risco → impacto → aprovação", "source_path": "docs/risk-management/README.md", "start_line": "138", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "risk-failure-mode", "end_line": "166", "index": 33, "source_field": "", "source_heading": "Risk register mínimo", "source_path": "docs/risk-management/README.md", "start_line": "152", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "concept-or-structure", "end_line": "182", "index": 34, "source_field": "", "source_heading": "Categorias", "source_path": "docs/risk-management/README.md", "start_line": "167", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "decision-authority", "end_line": "198", "index": 35, "source_field": "", "source_heading": "Risk acceptance", "source_path": "docs/risk-management/README.md", "start_line": "183", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "lifecycle-state", "end_line": "212", "index": 36, "source_field": "", "source_heading": "Mudança material", "source_path": "docs/risk-management/README.md", "start_line": "199", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "evidence-artifact", "end_line": "224", "index": 37, "source_field": "", "source_heading": "Evidências", "source_path": "docs/risk-management/README.md", "start_line": "213", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "metric", "end_line": "235", "index": 38, "source_field": "", "source_heading": "Métricas", "source_path": "docs/risk-management/README.md", "start_line": "225", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "risk-failure-mode", "end_line": "246", "index": 39, "source_field": "", "source_heading": "Antipatterns", "source_path": "docs/risk-management/README.md", "start_line": "236", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->
<!-- source-unit {"classification": "reference", "end_line": "250", "index": 40, "source_field": "", "source_heading": "Sources", "source_path": "docs/risk-management/README.md", "start_line": "247", "transformation": "integrate-completely", "unit_type": "markdown-atx-heading"} -->

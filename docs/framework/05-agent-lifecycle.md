---
title: 05 — Lifecycle de agentes
status: maintained
maturity: validated
last_reviewed: 2026-08-18
review_cycle: quarterly
owners: [framework-maintainers]
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# 05 — Lifecycle de agentes

## Visão geral

Um agente não é um entregável de projeto: é um ativo operacional que nasce, muda, opera, é revalidado e um dia precisa ser retirado. Governar o lifecycle significa garantir que, **em todos esses momentos**, o agente tenha estado conhecido, owner válido e evidência recuperável — e que nada disso dependa da memória de uma pessoa.

Sem lifecycle explícito, o estate acumula agentes publicados que mantêm permissões, identidades, conectores e custo depois de perder owner, finalidade ou evidência válida. O controle não é burocracia: é o que impede que um agente esquecido continue com acesso a sistemas críticos anos depois de deixar de ser usado.

**Resultado esperado:** qualquer agente em produção possui estado conhecido, owner válido, próxima attestation, regras de mudança material e um caminho testado para suspensão, quarentena e retirada.

Este capítulo responde a três perguntas em sequência: *o que governar* (conceitos), *como um agente percorre o ciclo* (fases), e *quais obrigações normativas se aplicam* (referência). Leia as seções 1 e 2 para entender; use a seção 3 como checklist de implementação e auditoria.

## Antes de seguir: fases, gates e processos são objetos diferentes

| Objeto | Pergunta | Uso neste capítulo |
|---|---|---|
| **F1–F8** | Em que fase do lifecycle está o agente? | Organiza o caminho do ativo, do intake ao sunset. |
| **G0–G7** | Qual decisão do programa precisa autorizar avanço? | Estrutura a implantação organizacional no [capítulo 08](08-implementation-and-adoption.md). |
| **P1–P8** | Qual processo recorrente o agente atravessa? | Executa registro, mudança, operação, incidentes, attestation e retirada. |
| **Stage/state** | Qual é a posição formal e o estado técnico atual? | Registra o histórico e permite contenção sem apagar o lifecycle. |

> **Artefatos para produzir agora — lifecycle.** Use o [Agent Registry Record](../../toolkit/templates/agent-registry-template.md) para identidade, owner e estado; o [Agent Blueprint](../../toolkit/templates/agent-blueprint-template.md) para a versão técnica; o [Attestation and Sunset Record](../../toolkit/templates/attestation-sunset-record.md) para revalidação; e o [Sunset Plan](../../toolkit/templates/sunset-plan.md) para retirada. Os templates registram as decisões deste capítulo; não as substituem.

## 1. Conceitos essenciais

### 1.1 O objeto governado: ativo e versão são coisas diferentes

A unidade de governança precisa distinguir dois objetos que costumam ser confundidos:

| Unidade | O que é | O que carrega |
|---|---|---|
| **agent asset** | o ativo estável, com `agent_id` permanente | identidade, ownership, histórico, finalidade |
| **version/release** | a versão publicada em um ambiente | configuração, evidências, approval, expiry |

Confundir as duas produz o erro mais comum do domínio: **aprovar uma versão e tratar a aprovação como permanente para o ativo**. A aprovação vale para a versão; o ativo precisa de revalidação contínua.

### 1.2 Três visões que coexistem sem ser sinônimas

- **etapa da jornada** orienta o trabalho humano: ideia, design, build, avaliação e operação;
- **lifecycle stage** registra a posição formal do ativo: `discovered`, `draft`, `under-review`, `approved`, `production`, `retirement-review`, `retired` ou `archived`;
- **operational state** registra a consequência técnica atual: `not-deployed`, `enabled`, `suspended`, `quarantined` ou `disabled`.

Separar stage de operational state evita transformar quarentena em falso avanço de lifecycle. Um agente pode permanecer em stage `production` e mudar de `enabled` para `quarantined` sem perder o histórico de release.

### 1.3 Autonomia e supervisão humana (HITL)

A política de autonomia define como a organização controla o quanto um agente pode decidir e executar sozinho. O agente pode propor e executar tarefas dentro de limites definidos. O nível de human oversight é proporcional ao tier, à action class, ao impacto, à reversibilidade, ao alcance e aos decision rights. Ações irreversíveis de alto impacto exigem confirmação humana explícita e evidence; qualquer exceção deve ser formal, temporária, aprovada pela authority correta, ter expiry, controls compensatórios, kill switch e plano de rollback. A aprovação segue os decision rights e a exception authority definidos no operating model para o tier e o scope avaliados.

Os níveis padronizam o que significa "autonomia" e reduzem ambiguidade na decisão. Independentemente do nível, qualquer red flag (dados pessoais/sensíveis, sistemas críticos, SOX/ITGC, alto blast radius) escala para o caminho de Produção e pode exigir controles adicionais:

| Nível | Descrição (capacidade do agente) | Aprovação mínima |
|---|---|---|
| **L0 — Assistivo/Informativo** | sem tool-use; consulta/geração de conteúdo; sem escrita em sistemas | rota proporcional ao tier, ao ambiente e ao alcance, preferencialmente policy-driven quando o risco for baixo |
| **L1 — Semi-autônomo** | tool-use em escopo limitado; ações reversíveis (ex.: abrir ticket, atualizar registro não crítico); HITL para ações com impacto relevante | em Test/PoC, owner, ambiente e autoavaliação; em produção, decision gate proporcional ao tier e ao alcance |
| **L2 — Delegado** | pode acionar sistemas críticos, mas ações críticas exigem HITL e evidências (auditoria, SoD, rollback); requer hardening e validação de segurança | rota formal de produção, com review de segurança/controles críticos e segregação aplicável |
| **L3 — Autônomo restrito** | execução autônoma de ações executivas; em geral não permitido para domínios SOX/ITGC e alto impacto; exceções apenas em domínios controlados com kill-switch e auditoria reforçada | somente por exceção explícita, temporária e aprovada pela authority executiva definida para o tier, independente do número de usuários |

Mudanças de modelo ou de regras de decisão que afetem o comportamento autônomo do agente exigem nova validação de segurança, testes mínimos e reavaliação do nível de autonomia.

### 1.4 Conceitos de controle contínuo

| Conceito | Definição operacional |
|---|---|
| **Mudança material** | mudança que pode alterar risco, impacto ou comportamento e, por isso, reabre avaliação. O reassessment recomeça do ponto afetado, **não do zero** |
| **Attestation** | revalidação periódica de owner, necessidade, acesso e controles — não uma assinatura ritual |
| **Dormancy threshold** | gatilho de revisão por inatividade, não regra cega de exclusão |
| **Joiner/Mover/Leaver (JML)** | eventos de identidade aplicados aos owners: entrada, mudança de função e saída de pessoas |

## 2. O ciclo de vida em 8 fases

Cada fase descreve o que acontece, o que produz e qual é o gate para avançar. **Gate não significa reunião**: em tiers baixos, vários gates podem ser policy-driven. O que importa é que a condição de avanço seja objetiva, verificável e registrada.

| Fase | O que produz | Gate para avançar |
|---|---|---|
| **F1. Ideia e intake** | intake, hipótese de valor, decisão `agent` vs `workflow` determinístico | problema e owner inicial claros |
| **F2. Registro e classificação** | `agent_id`, owners, ambiente, tier, admissibilidade, escaladores, red flags | nenhum build compartilhado ou produção sem ID e owner; tier e admissibilidade válidos |
| **F3. Design e build** | blueprint, identidade, dados, tools, modelo, oversight, telemetria, configuração versionada | build reproduz o blueprint; secrets e permissões dentro da policy |
| **F4. Testes e evidências** | evals funcionais, abuse cases, testes de dados/tools, resiliência, rollback | findings bloqueadores fechados ou aceitos pela authority correta |
| **F5. Revisão e aprovação** | domain reviews acionadas, MPB, evidence pack, risk acceptance | Publication Gate `approve` ou `condition` registrado |
| **F6. Publicação e operação** | deploy, health checks, políticas e budget ativos, telemetria, incidentes, custo, valor | containment e rollback disponíveis antes da exposição; sinais podem acionar reassessment ou contenção |
| **F7. Attestation e mudança** | revalidação de owner, necessidade e acessos; classificação de mudanças | continuar, remediar, suspender ou reaprovar |
| **F8. Contenção e retirada** | suspensão, quarentena ou retirada com revogação de acessos e arquivamento | reativação exige causa, correção e regression evidence; retirada é irreversível sem novo ciclo completo |

### 2.1 F1 — Ideia e intake

O ciclo começa antes de existir qualquer agente. A organização captura o problema, o mecanismo proposto, o owner e a necessidade de decisão antes de iniciar o trabalho de design. O intake deve registrar finalidade, baseline, usuários, pessoas afetadas, dados, ações, alternativas e urgência.

**Decisão de adequação.** Todo pedido de agente deve ser comparado com automação determinística, workflow, busca, analytics e alternativas não técnicas. Um agente prossegue somente quando sua capacidade distintiva é necessária — interpretação de linguagem, planejamento, seleção dinâmica de ferramentas — **e** o ônus adicional de governança é aceito. A decisão e as alternativas são registradas.

> **Armadilha comum:** começar pelo "qual modelo?" em vez do problema. Intake que induz solução antes da necessidade produz agentes sem justificativa e portfólio inflado.

### 2.2 F2 — Registro e classificação

Todo agente ganha identidade estável no registry **antes** de o trabalho ou a operação alcançar o estado correspondente — e permanece descobrível por stakeholders autorizados enquanto existir. O registro carrega owner, finalidade, tier, versão, ambiente, dependências, aprovação e metadados de descobribilidade; metadados obrigatórios ausentes **bloqueiam** a transição.

A classificação usa critérios aprovados, escaladores obrigatórios e o resultado mais severo aplicável. Registram-se resultados por critério, red flags, rationale, confiança, revisor e a rota resultante. A mesma evidência deve produzir o mesmo encaminhamento; sub-classificação é detectada por revisão ou reconciliação.

> **Armadilha comum:** permitir build ou uso compartilhado sem registro. Sem `agent_id` e owner, o agente é invisível para governança e vira shadow agent.

### 2.3 F3 — Design e build

O design documenta, **antes do build**: fronteiras, premissas de confiança, fluxos de dados e ações, atributos de qualidade, controles e comportamento de falha. O blueprint aprovado, diagramas, contratos de interface, vínculos de ameaça e impacto, alternativas e ADRs são retidos — revisores conseguem rastrear cada requisito material a um elemento de arquitetura e a um ponto de enforcement testável. (Ver [06 — Arquitetura e controles técnicos](06-architecture-and-technical-controls.md) para os detalhes de identidade, dados, tools, modelo e runtime.)

O build produz ou adquire somente componentes e configuração aprovados sob controle de mudança rastreável: fonte, versão, licença, fornecedor, configuração de build, inventário de dependências, varreduras e condições de aprovação. O artefato resultante é reproduzível ou atestável, e nenhuma dependência não aprovada entra na promoção.

Ambientes de desenvolvimento, teste e produção são separados em identidades, dados, credenciais, redes e autoridade de implantação. Acesso de teste não pode mutar produção, e segredos ou dados pessoais de produção não são copiados para ambientes inferiores sem authority.

> **Armadilha comum:** tratar o LLM como mecanismo de autorização. A aprovação de ações críticas é validada fora do modelo — no blueprint, no broker de tools e no processo humano.

### 2.4 F4 — Testes e evidências

O planejamento de testes aprova **antes** de ver resultados: objetivos, datasets, fatias, casos de abuso, thresholds e independência do revisor. O plano vincula caso de uso, tier, versões, ambientes, métodos, critérios de aceite e owner da evidência — e não pode ser afrouxado após um resultado reprovado sem decisão de mudança registrada.

A coleta de evidências mantém identidade, fonte, tempo, versão, integridade e custódia estáveis. O manifesto de evidências lista artefatos, hashes, produtor, ambiente, método, resultado, limitação e decisão vinculada. Um revisor consegue recuperar e reproduzir a alegação material; **evidência ausente é representada como lacuna, não como sucesso**.

> **Armadilha comum:** criar documentação na véspera da auditoria. Evidência é produto do processo — gerada durante build, teste e review —, não um artefato retrospectivo.

### 2.5 F5 — Revisão e aprovação

O release é decidido somente a partir do pacote vinculado de evidências de risco, avaliação, controle e operação. A decisão registra authority, versões, critérios aprovados e reprovados, condições, expiração, alvo de rollback e descobertas não resolvidas. **Controles bloqueantes não podem ser dispensados por aprovação condicional**, e condições expiradas interrompem a operação continuada.

O Publication Gate não refaz os reviews: verifica que as evidências requeridas pelo tier existem e que o residual risk foi aceito pela autoridade correta.

> **Armadilha comum:** aprovação como reunião ritual para todo tier. Em tiers baixos (T1), o gate deve ser policy-driven; o humano entra onde o risco justifica.

### 2.6 F6 — Publicação e operação

A implantação libera por coortes ou estágios delimitados com critérios explícitos de promoção, pausa e rollback: coorte, exposição, telemetria, thresholds, aprovação, resultado observado, incidentes e decisão do próximo estágio. A expansão ocorre somente após o estágio anterior atingir os critérios, e um sinal adverso pode interromper ou reverter o rollout.

Em produção, o comportamento e os resultados de controle que podem invalidar a aprovação são monitorados continuamente: sinais, baselines, fatias, thresholds, owner, rota de alerta, investigação e ação de lifecycle vinculada. **Desvio material ou violação de threshold produz contenção ou reavaliação — não um alerta informativo sem owner.** (Ver [09 — Operações, incidentes e continuidade](09-operations-incidents-and-continuity.md) para monitoramento e resposta.)

Os dados de observabilidade alimentam os processos de Operação, Gestão de Incidentes, Gestão de Mudanças e Revisão Periódica — incluindo decisões de sunset quando há desvios persistentes, inatividade ou risco elevado.

### 2.7 F7 — Attestation, mudança e versionamento

**Attestation.** Owners reatestam finalidade, ownership, dependências, risco, controles e necessidade contínua em ciclo baseado no risco. A cadência é proporcional ao tier (no máximo anual); o owner confirma que o agente continua necessário, que os acessos continuam adequados e que a finalidade não mudou. **Attestation vencida é um estado, não um aviso**: aciona grace period e depois suspensão. Não resposta ou attestation sem suporte dispara restrição, suspensão ou aposentadoria em vez de renovação automática. Attestation não substitui reassessment após mudança material.

**Mudança material.** A organização define, antes de automatizar qualquer reassessment, quais mudanças e eventos externos reabrem risco, aprovação, avaliação ou compatibilidade contratual. Cada trigger aponta para o ponto do processo que precisa ser reexecutado — o reassessment recomeça do ponto afetado, **não do zero**:

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

Automatizar um gatilho mal definido gera ruído e treina a organização a ignorá-lo. Ativos acionados não podem depender indefinidamente de aprovação anterior; a nova decisão é vinculada à versão alterada.

**Versionamento.** Toda mudança material é versionada e vinculada a datas de efetividade, revisão e supersessão: descrição da mudança, autor, aprovador, contratos impactados, ação de migração e referência à versão anterior. Consumidores identificam a versão aplicável; registros incompatíveis são migrados, rejeitados ou explicitamente grandfather.

**JML de owners.** A identidade do agente não permanece silenciosamente vinculada a alguém que mudou de função ou saiu:

- **Joiner:** ao assumir, o novo owner tem role, competência e authority validadas antes da transferência de accountability.
- **Mover:** mudança de área do owner dispara revisão de ownership, centro de custo e permissões; se a nova função não puder responder pelo agente, reatribua.
- **Leaver:** antes do desligamento, consulte o registry por ownership, nomeie delegado temporário e suspenda os casos sem sucessor conforme o tier.
- Em nenhum caso apague o histórico de ownership — a timeline é evidência de auditoria.

**Dormancy.** Threshold é gatilho de revisão, não regra cega de exclusão: um agente financeiro trimestral pode ficar 80 dias sem execução e continuar legítimo; um agente de service desk sem uso por 30 dias provavelmente foi abandonado. Valores iniciais a calibrar com evidência:

| Tier | Threshold inicial | Grace period |
|---|---|---|
| T1 | 120 dias | 30 dias |
| T2 | 90 dias | 21 dias |
| T3 | 60 dias | 14 dias |
| T4 | 30 dias | 7 dias, com revisão de admissibilidade e da exceção quando `restricted` |

Calibração: segmentar por frequência esperada e tier → definir threshold e grace → rodar 60–90 dias em **report-only** → analisar falsos positivos e sazonalidade → ajustar e só então automatizar a cadeia notificação → attestation → suspensão → retirada → manter exceções sazonais com data de expiração.

### 2.8 F8 — Contenção, reativação e retirada

**Suspensão, quarentena e retirada são ações diferentes.** Um único botão "disable" para os três casos destrói a rastreabilidade:

| Ação | Motivo | Evidência preservada | Reversível |
|---|---|---|---|
| `suspended` | administrativo ou planejado | configuração e histórico | sim, por decisão do owner |
| `quarantined` | risco ou incidente | evidência forense preservada deliberadamente | somente com causa, correção e regression evidence |
| `disabled` em stage `retired` | fim de vida | arquivada conforme retenção | não — exige novo ciclo completo |

Suspensão e quarentena exigem caminhos de authority e técnicos para interromper ações, isolar dependências e preservar evidências: gatilho, caminho de comando, escopo, estado esperado, operador, cadência de teste, resultado e pré-requisitos de recuperação. **Um exercício (drill) deve conter uma falha representativa dentro do alvo sem depender do próprio agente com falha.**

**Ação corretiva.** Cada descoberta recebe causa raiz, prioridade baseada em risco, ação corretiva e critério de fechamento: descoberta, evidência, owner, data de vencimento, controle provisório, remediação, reteste e disposição do revisor. O fechamento exige evidência objetiva de reteste; descobertas materiais vencidas permanecem visíveis e afetam a aprovação.

**Reativação segura.** Reativar exige causa raiz, remediação, regressão, monitoramento e prontidão de rollback evidenciados: vínculo do incidente, versão alterada, pacote de reteste, risco residual, authority aprovadora, condições e escopo do rollout. A falha anterior não pode mais ser reproduzível nas condições testadas, e sinais de alerta precoce estão ativos.

**Revisão disparada por incidente.** Após incidente, correção, mudança de dependência ou atualização de modelo/configuração, os requisitos afetados são retestados: versões anterior e nova, cenários impactados, conjunto de regressão, resultado, lacunas residuais e disposição de release. A mudança não invalida silenciosamente evidências anteriores; regressão reprovada impede reativação ou promoção.

**Aposentadoria e descomissionamento.** O agente é aposentado por transição de estado aprovada que remova authority e resolva obrigações de dados e dependências: decisão final do owner, aviso ao usuário, parada de tráfego, revogação de acesso, disposição de dados, arquivo, owner da dependência e evidência de conclusão. Depois de aposentado, o agente não pode mais agir ou consumir recursos; registros retidos permanecem acessíveis pelo período aprovado.

**Retenção e limpeza.** Define-se quem pode ler, alterar e recuperar o registro, por quanto tempo e sob qual regra de legal hold ou exclusão: classificação, grupos de acesso, custodiano, gatilho de retenção, período mínimo, disposição e caminho de recuperação de auditoria. Evidências autorizadas são recuperáveis no prazo exigido; dados expirados são descartados sem romper a linhagem exigida.

## 3. Referência normativa

Condições mínimas que devem ser verdadeiras em cada ponto do ciclo. Use como checklist de implementação e auditoria; as seções 1–2 explicam o porquê de cada item.

| # | Obrigação | Evidência mínima | Concluído quando |
|---|---|---|---|
| R1 | Definir estados permitidos, authorities de transição, critérios de entrada/saída e resultados terminais para todo agente | máquina de estados publicada com registros exigidos, gates G0–G7, exceções e reentrada disparada por evento | transições inválidas são rejeitadas e o estado observado em runtime reconcilia com o registry autoritativo |
| R2 | Capturar problema, mecanismo, owner e necessidade de decisão antes do design | registro de intake com finalidade, baseline, usuários, pessoas afetadas, dados, ações, alternativas e urgência | solicitação encaminhada às decisões de adequação, risco e portfólio sem ignorar ownership ou escopo |
| R3 | Comparar agente com alternativas determinísticas e não técnicas | alternativas, necessidade de autonomia, incerteza, benefício esperado, custo de falha e decisão arquitetural | agente prossegue somente com capacidade distintiva necessária e ônus de governança aceito |
| R4 | Criar/atualizar identidade estável no registry antes do estado correspondente (registro inicial **e** produção) | owner, finalidade, tier, versão, ambiente, dependências, aprovação e metadados de descobribilidade | ativo descobrível por stakeholders autorizados e metadados obrigatórios ausentes bloqueiam transição |
| R5 | Classificar com critérios aprovados, escaladores obrigatórios e resultado mais severo | resultados por critério, red flags, rationale, confiança, revisor e rota resultante | mesma evidência produz encaminhamento consistente e sub-classificação é detectada |
| R6 | Documentar fronteiras, premissas de confiança, fluxos, atributos de qualidade, controles e falha antes do build | blueprint aprovado, diagramas, contratos de interface, vínculos de ameaça/impacto, alternativas e ADRs | revisores rastreiam cada requisito material a elemento de arquitetura e enforcement testável |
| R7 | Produzir/adquirir somente componentes e configuração aprovados sob controle de mudança | fonte, versão, licença, fornecedor, configuração de build, inventário de dependências, varreduras e condições de aprovação | artefato reproduzível ou atestável e nenhuma dependência não aprovada entra na promoção |
| R8 | Separar ambientes de desenvolvimento, teste e produção | inventário de ambientes, policy de acesso, classificação de dados, caminho de promoção e teste negativo | acesso de teste não muta produção e segredos/dados pessoais não são copiados sem authority |
| R9 | Aprovar plano de testes antes de ver resultados | plano vinculando caso de uso, tier, versões, ambientes, métodos, critérios de aceite e owner da evidência | plano cobre modos de falha materiais e não é afrouxado após resultado reprovado sem decisão registrada |
| R10 | Coletar evidências com identidade, fonte, tempo, versão, integridade e custódia estáveis | manifesto com artefatos, hashes, produtor, ambiente, método, resultado, limitação e decisão vinculada | revisor recupera e reproduz a alegação material; ausência é lacuna, não sucesso |
| R11 | Decidir release a partir do pacote vinculado de evidências | decisão, authority, versões, critérios, condições, expiração, alvo de rollback e descobertas não resolvidas | controles bloqueantes não são dispensados por aprovação condicional e condições expiradas interrompem operação |
| R12 | Liberar por coortes com critérios explícitos de promoção, pausa e rollback | coorte, exposição, telemetria, thresholds, aprovação, resultado, incidentes e decisão do próximo estágio | expansão só após critérios do estágio anterior e sinal adverso pode interromper ou reverter |
| R13 | Monitorar comportamento e controles que podem invalidar a aprovação | sinais, baselines, fatias, thresholds, owner, rota de alerta, investigação e ação de lifecycle | desvio material produz contenção ou reavaliação, não alerta sem owner |
| R14 | Retestar requisitos afetados após incidente, correção ou mudança de dependência | versões anterior/nova, cenários impactados, regressão, resultado, lacunas e disposição de release | mudança não invalida evidências anteriores e regressão reprovada impede reativação |
| R15 | Definir mudanças materiais e eventos que reabrem risco | gatilho, fonte de detecção, ativos/evidências impactados, controle provisório, owner, vencimento e disposição | ativos acionados não dependem indefinidamente de aprovação anterior |
| R16 | Versionar toda mudança material com datas de efetividade, revisão e supersessão | descrição, autor, aprovador, contratos impactados, migração e referência à versão anterior | consumidores identificam versão aplicável e registros incompatíveis são migrados/rejeitados/grandfather |
| R17 | Exigir attestation periódica baseada em risco | atestante, corte de evidências, fatos alterados, exceções, dependências obsoletas, decisão e próxima revisão | não resposta ou attestation sem suporte dispara restrição, suspensão ou aposentadoria |
| R18 | Implementar suspensão e quarentena com authority e caminhos técnicos | gatilho, caminho de comando, escopo, estado esperado, operador, cadência de teste, resultado e pré-requisitos de recuperação | drill contém falha representativa sem depender do próprio agente |
| R19 | Atribuir causa raiz, prioridade, ação corretiva e critério de fechamento a cada descoberta | descoberta, evidência, owner, vencimento, controle provisório, causa raiz, remediação, reteste e disposição | fechamento exige evidência objetiva de reteste e descobertas vencidas permanecem visíveis |
| R20 | Permitir reativação somente com causa, remediação, regressão, monitoramento e rollback evidenciados | vínculo do incidente, versão alterada, pacote de reteste, risco residual, authority, condições e escopo | falha anterior não reproduzível nas condições testadas e alertas precoces ativos |
| R21 | Aposentar por transição aprovada que remova authority e resolva dados/dependências | decisão final do owner, aviso, parada de tráfego, revogação de acesso, disposição de dados, arquivo, owner da dependência, conclusão | agente não age nem consome recursos e registros retidos ficam acessíveis no período aprovado |
| R22 | Definir leitura/alteração/recuperação do registro, prazo e regra de legal hold | classificação, grupos de acesso, custodiano, gatilho de retenção, período mínimo, disposição e recuperação de auditoria | evidências autorizadas recuperáveis no prazo e dados expirados descartados sem romper linhagem |

**Autonomia e oversight (norma):** o nível de supervisão e intervenção é proporcional ao tier, à action class, ao impacto, à reversibilidade e aos decision rights; ações irreversíveis de alto impacto exigem confirmação humana explícita e evidence. Exceções temporárias seguem a exception authority definida no operating model, com rationale, compensating controls, expiry e plano de rollback. Mudanças de modelo ou regras de decisão exigem nova validação, testes mínimos e reavaliação do nível de autonomia. (Níveis L0–L3 na seção 1.3.)

**Gates G0–G7:** a sequência completa de gates de implantação é definida no capítulo 08 — Implementação e adoção; este capítulo define as condições de transição de cada estado.

## 4. Estado e transições (máquina de estados)

### 4.1 Stages e operational states

Stages mínimos: `discovered` · `draft` · `under-review` · `approved` · `production` · `retirement-review` · `retired` · `archived`

Operational states mínimos: `not-deployed` · `enabled` · `suspended` · `quarantined` · `disabled`

Regras estruturais:

- `draft` não vai diretamente a `production`;
- `quarantined` não retorna a `enabled` sem correção, reteste e aprovação;
- cada transição registra evento disparador, authority, evidência e ações automáticas;
- stage e operational state são versionados e o histórico é preservado — a auditoria precisa saber as duas condições no momento de um evento.

### 4.2 Matriz de transição

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

## 5. Plano de implantação — lifecycle do agente

Para levar o lifecycle do zero à operação, na primeira implantação execute em ordem; em evoluções posteriores, mudanças materiais podem exigir apenas os passos afetados.

1. **Definir o objeto governado** (`agent asset` vs `version`) e quem opera o lifecycle.
2. **Desenhar estados a partir de consequências operacionais**, não de atividades de projeto.
3. **Transformar cada transição em gate auditável** com evento, authority, evidência, SLA e automação.
4. **Definir a lista de mudanças materiais antes** de automatizar reassessment.
5. **Calibrar attestation e dormancy pelo padrão real de uso**, em report-only primeiro.
6. **Integrar JML de owners ao registry**, com consulta reversa por ownership.
7. **Implementar suspensão, quarentena e retirada como ações distintas.**
8. **Validar manualmente antes de virar policy-as-code**: uma cohort sugerida contém 10–20 agentes, ao menos um T3, um leaver, uma mudança material e um incidente simulado; isso é guidance adaptável, não piloto obrigatório.

## 6. Artefatos, evidências, métricas e failure modes

### Artefatos

- Agent Lifecycle Standard: estados, transições, triggers, roles, timers, JML, quarentena, retirada e retenção;
- matriz de transição e runbook operacional;
- registro de attestation e de mudanças materiais;
- template de attestation e sunset;
- plano de sunset.

### Evidências

- estado atual e histórico de transições por agente e versão;
- approval record com authority, condições e expiry;
- attestation records e vencimentos;
- classificação de mudanças materiais e reassessments derivados;
- evidência de contenção e de reativação;
- registro de retirada com remoção de acessos e arquivamento.

### Métricas

- agentes em produção sem attestation válida;
- agentes sem owner ou com owner desligado;
- mudanças materiais detectadas por auditoria em vez de declaradas pelo owner;
- tempo entre trigger e reassessment concluído;
- agentes dormentes por tier e desfecho após grace period;
- transições executadas fora da matriz autorizada;
- tempo entre decisão de retirada e revogação efetiva de acesso;
- reativações após quarentena sem regression evidence.

### Failure modes

- state machine documentada que não altera permissão, evidência ou comportamento real;
- tratar aprovação de versão como aprovação permanente do ativo;
- usar um único "disable" para suspensão, quarentena e retirada;
- automatizar dormancy antes de calibrar sazonalidade;
- reassessment que recomeça do zero e, por custo, deixa de ser executado;
- retirada que remove o agente do catálogo mas não revoga identidade e secrets;
- histórico de ownership sobrescrito em vez de versionado.

## Decision gate

Nenhum agente permanece em produção sem lifecycle stage e operational state válidos, owner ativo, attestation dentro do prazo do tier e caminho de contenção e retirada exercitado. Toda transição preserva authority e evidence. Mudança material sem reassessment registrado é motivo de suspensão, não de exceção informal.

## Acceptance criteria

- todas as decisões deste capítulo possuem authority, owner e evidência recuperável;
- requisitos aplicáveis estão ligados ao catálogo de controles e ao método de verificação;
- exceções têm escopo, justificativa, compensating controls, expiry e decisão residual;
- controles de build time e runtime são distinguidos e exercitados quando aplicáveis;
- mudanças materiais reabrem avaliação, aprovação e evidência;
- nenhuma alegação de conformidade, eficácia ou valor excede a evidência observada.

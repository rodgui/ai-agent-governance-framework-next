# Glossário canônico

Este vocabulário reduz ambiguidade entre policy, arquitetura, patterns, controls e engagements. Quando um termo externo tiver definição normativa própria, a definição aplicável ao contexto deve ser registrada no assessment.

## Sistemas, agentes e capacidades

| Termo | Definição neste framework | Não confundir com |
|---|---|---|
| **AI system** | Sistema que usa modelos ou técnicas de IA para produzir outputs, recommendations, predictions, content ou actions. | Modelo isolado. |
| **Model** | Artefato computacional versionável usado por um AI system. | Aplicação, workflow ou agent completo. |
| **Generative AI** | IA que produz conteúdo novo como texto, imagem, áudio, código ou estrutura. | Toda IA. |
| **Assistant / copilot** | Sistema orientado a apoiar uma pessoa, geralmente por interaction e suggestion. | Agent com capacidade autônoma de ação. |
| **Agent** | AI system que percebe contexto, decide ou planeja passos e usa capacidades para perseguir um objetivo dentro de boundaries. | Chat interface sem ação. |
| **Agentic system** | Sistema cujo comportamento inclui goal pursuit, planning, tool use, memory, delegation ou adaptação com autonomia relevante. | Marketing label “agent”. |
| **Workflow** | Sequência explícita de etapas e decisões; pode ou não usar IA. | Autonomia aberta de agent. |
| **Orchestration** | Coordenação de models, agents, tools, data e workflow states. | Accountability organizacional. |
| **Multi-agent system** | Sistema no qual múltiplos agents coordenam ou delegam trabalho. | Várias prompts executadas independentemente. |
| **Capability** | Ação tecnicamente possível, como observe, create, modify, execute, approve, delete ou delegate. | Use case ou permissão efetiva. |
| **Tool** | Função, API, código ou interface invocável por agent. | Model ou connector de dados. |
| **Connector** | Integração que fornece acesso a fonte, service ou system. | Autorização automática. |
| **MCP** | Model Context Protocol, protocolo para expor context e tools a AI applications. | Control framework. |
| **MCP server** | Componente que oferece resources, prompts ou tools via MCP. | Servidor confiável por default. |
| **Action class** | Categoria de efeito: observe, create, modify, execute, approve, delete ou delegate. | Risk tier completo. |
| **State-changing action** | Ação que cria, modifica, executa, aprova, deleta ou delega algo fora da resposta do model. | Geração de texto sem side effect. |
| **Prohibited use** | Uso que não pode ser autorizado no scope atual. | Exception pendente. |

## Vocabulário externo de orchestration

Os termos abaixo são usados como **crosswalk explicativo**, não como nova taxonomia normativa nem como valores adicionais do `agent-blueprint.schema.json`.

| Termo | Uso nesta revisão | Não confundir com |
|---|---|---|
| **Architecture pattern** | Responde “que tipo de sistema é este?”; usa a taxonomia canônica do blueprint, como `workflow-agent`, `tool-using-agent` ou `multi-agent`. | Orchestration pattern. |
| **Orchestration pattern** | Responde “como o trabalho é coordenado durante a execução?”; o vocabulário Gartner distingue workflow, iterative reasoning e supervisory multi-agent orchestration. | Architecture pattern, risk tier ou admissibility. |
| **Orchestration work profile** | Guidance não normativo que classifica `determinism`, constraints de governance/regulação, human oversight, iterative need e event-driven coordination como `low`, `moderate` ou `high` para orientar pattern fit. | Risk score, readiness score, MPB ou impact assessment. |
| **Primary/secondary orchestration pattern** | O pattern dominante e, quando necessário, o pattern complementar de um use case; ambos exigem rationale e evidence suficiente para a decisão. | `primary_orchestrator` universal. |
| **Consolidated/coordinated/federated placement** | Vocabulário externo para discutir onde control-plane e orchestration authority ficam distribuídos. | `Federated Governance Operating Model`, que trata decision rights e authorities organizacionais. |
| **AIR — Action, Intelligence, Record** | Crosswalk externo para raciocinar sobre execution/tools, model/reasoning e systems of record/source of truth. | Os cinco planos da arquitetura canônica. |

A classificação de orchestration pattern ocorre depois da decisão “agente é o mecanismo certo?” e antes de decidir topology/control-plane e avaliar technology fit. Ela não altera diretamente T1–T4, admissibility, risk score, MPB ou impact assessment.

## Autonomia e humanos

| Termo | Definição neste framework | Não confundir com |
|---|---|---|
| **Autonomy** | Grau de liberdade para escolher passos e executar ações sem decisão humana a cada etapa. | Intelligence ou qualidade. |
| **AI-operated, human-led** | Pessoas definem finalidade, boundaries, authorities e accountability; automação opera dentro deles. | Humans aprovando tudo manualmente. |
| **Human oversight** | Capacidade humana real de compreender, supervisionar, intervir e contestar o sistema. | Checkbox ou presença nominal. |
| **Human-in-the-loop (HITL)** | Decisão humana exigida dentro do fluxo antes de ação definida. | Revisão posterior. |
| **Human-on-the-loop (HOTL)** | Supervisão humana com capacidade de monitorar e intervir durante operação. | Autonomia sem observabilidade. |
| **Human-in-command** | Autoridade humana sobre finalidade, deployment, boundaries e continuidade. | Operação manual. |
| **Meaningful review** | Revisão com contexto, tempo, competência e poder para mudar a decisão. | Rubber stamp. |
| **Contestability** | Mecanismo para questionar, corrigir ou recorrer de output/decision. | Canal de suporte genérico. |

## Ownership e decision rights

| Termo | Definição neste framework | Não confundir com |
|---|---|---|
| **Accountability** | Obrigação de responder por decisão, resultado e correção. Não é transferida ao agent. | Execução de tarefa. |
| **Sponsor** | Autoridade executiva sobre mandato, appetite, funding e material trade-offs. | Project manager. |
| **Governance Owner** | Owner do framework, control catalog, forums, exceptions e improvement. | Dono de todos os agents. |
| **Business Owner** | Responsável por finalidade, uso permitido, outcomes e continuidade do agent. | Usuário frequente. |
| **Technical Owner** | Responsável por arquitetura, change, evaluations e technical remediation. | Fornecedor da plataforma. |
| **Design Authority** | Autoridade sobre admissibilidade pré-release e conditions. | Run Authority. |
| **Run Authority** | Autoridade operacional para contain, quarantine, rollback, reactivate ou retire. | Service desk sem authority. |
| **Domain Owner** | Owner de control especializado como identity, data, security, privacy ou RAI. | Governance Owner. |
| **Decision right** | Papel com autoridade explícita para uma decisão definida. | RACI genérico sem poder decisório. |
| **Risk appetite** | Quantidade e tipo de risco que authority aceita perseguir ou reter. | Risk tier. |
| **Risk acceptance** | Decisão explícita de aceitar residual risk por prazo e scope. | Ausência de mitigação. |

## Inventário, arquitetura e lifecycle

| Termo | Definição neste framework | Não confundir com |
|---|---|---|
| **Registry** | Registro operacional de existência, ownership, status, tier, platform e evidence links. | Blueprint completo. |
| **Inventory** | Observação agregada de assets descobertos; pode conter duplicidade e baixa confiança. | Registry reconciliado. |
| **Blueprint** | Especificação versionada de arquitetura, models, data, identity, tools, boundaries e runtime. | Linha no registry. |
| **Source of truth** | Sistema reconhecido como autoridade para determinado campo/decision. | Único banco para todos os domínios. |
| **Reconciliation** | Processo de comparar sources, resolver conflitos e manter provenance. | Sobrescrever tudo pelo source mais recente. |
| **Lifecycle** | Discover, register, assess, approve, release, operate, change, attest, sunset e archive. | SDLC apenas. |
| **Attestation** | Declaração periódica, por authority, de que owner, purpose, controls e evidence permanecem válidos. | Avaliação inicial. |
| **Sunset** | Retirada planejada com revocation, retention, dependency e communication. | Desligamento sem cleanup. |
| **Material change** | Mudança que pode alterar tier, admissibilidade, controls, evaluation ou approval. | Toda alteração cosmética. |
| **Dormancy** | Ausência de uso relevante por período definido, que dispara revisão de continuidade. | Falha técnica ou indisponibilidade. |
| **Dormancy threshold** | Período calibrado por tipo de agente a partir do qual a dormência é tratada. Threshold único para todo o estate produz falso positivo em agente sazonal. | Timeout de sessão. |
| **Grace period** | Prazo entre o trigger de retirada e a revogação efetiva, para dependentes reagirem. | Adiamento indefinido. |
| **Joiner/mover/leaver (JML)** | Processo que reatribui ou revoga ownership e acessos quando a pessoa responsável entra, muda de função ou sai. | Offboarding apenas de credencial humana. |
| **Evidence cutoff** | Data até a qual evidências foram consideradas em assessment ou decisão. | Data de publicação. |
| **Dossiê do agente** | Conjunto de artefatos vinculados por um único `agent_id` — intake, autoavaliação, risk record, registry entry, blueprint, impact assessment, evidence pack e registros operacionais. Não é um documento único. | Formulário ou PDF consolidado. |

## Risco, controles e assurance

### Classificações que não devem ser misturadas

| Classificação | Pergunta | Valores ou forma | Efeito |
|---|---|---|---|
| **Risk tier** | Quão severa pode ser a exposição? | T1–T4 | Define rigor mínimo de controls, evidence e authority. |
| **Admissibilidade** | Este uso pode operar? | `permitted`, `conditional`, `restricted`, `prohibited` | Permite, condiciona, exige exceção ou proíbe operação. |
| **Risk score** | Quais fatores produzem o risco base? | Sete dimensões + red flags | Alimenta a classificação; não decide sozinho. |
| **Readiness score** | O dossiê está pronto para decisão? | Completeza e força da evidência | Mede prontidão; não mede risco, qualidade ou maturidade. |
| **Maturity** | Quão desenvolvida está a capability organizacional? | Níveis do maturity model | Define baseline, target e roadmap organizacional. |
| **Lifecycle stage/state** | Em que momento e estado operacional está o agente? | Estados e transições canônicos | Controla promoção, operação, mudança e sunset. |
| **Gate** | Qual decisão do programa precisa ocorrer? | G0–G7 | Autoriza, condiciona, suspende, rejeita ou encerra avanço. |
| **Processo operacional** | Qual rotina recorrente o agente atravessa? | P1–P8 | Executa e registra criação, release, operação e retirement. |

**T4 é criticidade, não admissibilidade.** Um T1 pode ser `restricted` ou `prohibited` por finalidade, obrigação ou desenho; um T4 pode ser `permitted` ou `conditional` quando a authority, os controls e as evidências sustentarem a decisão.

| Termo | Definição neste framework | Não confundir com |
|---|---|---|
| **Risk** | Efeito da incerteza sobre objetivos, pessoas, direitos, sistemas ou organização. | Finding confirmado. |
| **Impact** | Magnitude da consequência se evento ocorrer. | Likelihood. |
| **Likelihood** | Possibilidade estimada de ocorrência nas condições avaliadas. | Frequência histórica isolada. |
| **Residual risk** | Risco remanescente após controls e mitigations. | Risco inicial. |
| **Risk tier** | Classe de governança que determina rigor mínimo por criticidade; neste framework T1–T4. | Admissibilidade ou score de maturidade. |
| **Admissibilidade** | Dimensão que responde se e sob quais condições um uso pode operar: `permitted`, `conditional`, `restricted` ou `prohibited`. Independente do tier ([ADR-0009](../architecture/decisions/0009-risk-tier-and-admissibility.md)). | Risk tier. Um T1 pode ser proibido; um T4 pode ser admitido. |
| **Red flag** | Condição que impede fast path e eleva a criticidade mínima independentemente do score. | Falha automaticamente comprovada. |
| **Escalador** | Red flag registrado na norma com criticidade mínima e efeito declarados. A lista normativa prevalece sobre o instrumento que a coleta. | Pergunta de questionário. |
| **Fast path** | Rota automatizada de T1: elimina revisão manual caso a caso, não os controles nem a evidência. | Isenção de governança. |
| **Scoring de risco** | Pontuação das sete dimensões de classificação (dados, autonomia, impacto, privilégio, alcance, conectividade, criticidade) que produz o risco base; red flags corrigem o que a soma esconde. | Admissibilidade. |
| **Risk scoring worksheet** | Ferramenta que operacionaliza o pre-screen, as sete dimensões de scoring, os red flags e o impact trigger para produzir tier, admissibilidade e rota de reviews. | A norma em si (a lógica normativa vive no capítulo 04). |
| **Mapa de decisão** | Encadeamento canônico da classificação: pre-screen → scoring → red flags → tier → impact trigger → RAI → domain reviews → publication gate, com a matriz de calor por tier. | Três aprovações concorrentes. |
| **Impact trigger** | Condição que aciona o RAI impact assessment — influência sobre direitos, oportunidades, decisões sobre pessoas, segurança física, comunicação pública ou processo regulado. | Severidade técnica do caso. |
| **Domain review** | Revisão especializada acionada por gatilho relevante (privacidade, segurança, dados, arquitetura, jurídico, comercial), não por regra fixa. | Fila permanente de revisores. |
| **Minimum Production Bar (MPB)** | Piso de controles que precisam ser verdadeiros para um agente entrar **e permanecer** em produção, por tier. | Teto de controles ou gate de release completo. |
| **Blast radius** | Extensão potencial do efeito por usuários, dados, sistemas, regiões e dependências. | Número de usuários apenas. |
| **Reversibility** | Capacidade de desfazer efeito com custo, prazo e integridade aceitáveis. | Existência nominal de rollback. |
| **Policy** | Regra normativa aprovada com authority e enforcement expectation. | Guidance. |
| **Standard** | Requirement obrigatório que especifica como satisfazer policy. | Referência externa sem adoção. |
| **Guidance** | Recomendação adaptável que não muda policy. | Requirement adotado. |
| **Procedure** | Passos operacionais para executar tarefa ou control. | Control objective. |
| **Control objective** | Resultado de risco/governança que precisa ser alcançado. | Implementação específica. |
| **Control** | Medida preventiva, detective, responsive ou corrective para alcançar objective. | Documento que afirma intenção. |
| **Compensating control** | Control alternativo que reduz risco quando requirement primário não é viável. | Waiver sem mitigação. |
| **Exception** | Desvio temporário aprovado, com rationale, owner, compensating controls e expiry. | Nova regra permanente. |
| **Assurance** | Atividade que aumenta confiança de que requirements e controls são adequados e eficazes. | Operação do control pelo owner. |
| **Independent assurance** | Assurance com independência suficiente do owner e implementer. | Self-assessment. |
| **Control plane** | Camada de inventory, identity, configuration, policy decision, lifecycle e administrative action. | Governança completa. |
| **Assurance plane** | Camada de risk, security, privacy, RAI, evaluations e independent challenge. | Control plane. |
| **Build time** | Design, build, assessment, evaluation e release antes da operação. | Runtime. |
| **Runtime** | Período em que o sistema opera com usuários, data e tools reais. | Test environment. |
| **Decision gate** | Ponto em que authority decide avançar, condicionar, bloquear, conter ou encerrar com evidence. | Reunião sem output. |
| **Evidence package** | Conjunto versionado de artifacts, test results, approvals e limitations para uma decisão. | Pasta de documentos sem manifesto. |
| **System evidence** | Evidência extraída de logs, configs, tests, APIs ou records operacionais. | Afirmação em workshop. |

## Identidade, dados e memória

| Termo | Definição neste framework | Não confundir com |
|---|---|---|
| **Workload identity** | Identidade própria e gerenciada para service, workload ou agent. | Credencial humana compartilhada. |
| **Non-human identity** | Categoria que abrange service accounts, workload identities e agentes; governada por lifecycle próprio, não pelo de pessoas. | Conta de serviço legada sem owner. |
| **Step-up** | Exigência de autenticação ou autorização adicional no momento de uma ação de maior impacto. | Login inicial mais forte. |
| **Prompt injection** | Instrução hostil embutida em conteúdo processado pelo agente, que tenta redirecionar comportamento ou extrair dados. | Erro de prompt do usuário. |
| **Delegated access** | Acesso em nome do usuário, limitado por seus direitos e contexto. | Privilege próprio do agent. |
| **Least privilege** | Menor permission, scope e duração necessários para finalidade aprovada. | Read-only por default em todos os casos. |
| **Data contract** | Acordo versionado de source, purpose, classification, quality, access, retention e owner. | Connector config. |
| **AI-ready data** | Dados avaliados como adequados ao uso definido, com quality, classification, ownership e provenance suficientes. | Dados “limpos” universalmente. |
| **Provenance** | Origem, transformations, versions e chain of custody de dado/output/evidence. | Link para source apenas. |
| **Memory** | Estado persistente ou semipersistente usado pelo agent entre interactions ou steps. | Context window temporária. |
| **Retention** | Prazo e condições para manter dado, log, memory ou evidence. | Backup indefinido. |
| **Right-to-delete mechanism** | Processo capaz de localizar e remover dados aplicáveis inclusive em memory e derived stores. | Delete na interface apenas. |

## Evaluation, operação e valor

| Termo | Definição neste framework | Não confundir com |
|---|---|---|
| **Evaluation** | Teste estruturado de comportamento, qualidade, safety, security ou operação. | Demo. |
| **Metric** | Medida definida com unidade, população e método. | Objective. |
| **Threshold** | Limite que dispara decisão, alert ou action. | Resultado desejado sem critério. |
| **Benchmark** | Conjunto e método padronizados para comparação. | Teste suficiente para contexto específico. |
| **Red teaming** | Teste adversarial para descobrir failure modes e control gaps. | Garantia de segurança. |
| **Regression** | Degradação em cenário anteriormente aceitável. | Drift necessariamente. |
| **Drift** | Mudança relevante em inputs, behavior, performance ou environment ao longo do tempo. | Toda variação. |
| **Observability** | Capacidade de inferir estado e comportamento a partir de signals suficientes. | Logging sem ação. |
| **Telemetry** | Dados de execução, uso, quality, policy, cost e action. | Evidência de valor por si só. |
| **SLO** | Objetivo mensurável de serviço/qualidade para um período. | SLA contratual. |
| **Containment** | Ação para limitar blast radius preservando investigação e recovery. | Remediação definitiva. |
| **Quarantine** | Estado controlado que restringe operação ou acesso até decisão. | Delete. |
| **Kill switch** | Mecanismo testado para interromper capability, tool ou agent. | Botão documentado sem authority. |
| **Circuit breaker** | Corte automático acionado por threshold, sem esperar decisão humana. | Kill switch, que é acionado por authority. |
| **Behavioral baseline** | Padrão de comportamento observado e aceito de um agente, contra o qual desvios são medidos. | Resultado de eval pré-release. |
| **Denial-of-wallet** | Exaustão de orçamento por consumo legítimo em aparência, sem indisponibilidade técnica. | Denial-of-service. |
| **Unit economics** | Custo por resultado útil, não por token ou execução. | Custo total de plataforma. |
| **Rollback** | Retorno verificável a versão/estado conhecido. | Restart. |
| **Reactivation** | Retorno autorizado após evidence de correção e readiness. | Remover alerta. |
| **Score de prontidão (agent assessment score)** | Pontuação da completeza e evidência do dossiê — cada campo obrigatório pontuado por peso, itens críticos bloqueadores, threshold mínimo por tier. Mede prontidão para decisão; não mede risco, qualidade nem maturidade. | Score de risco (que produz o tier) ou maturity organizacional. |
| **Processos operacionais (P1–P8)** | Os oito processos do ciclo operacional do agente — criação/registro, avaliação/aprovação, publicação, operação rotineira, incidentes, mudanças, revisão/auditoria e sunset — com disparo, accountable, entradas, atividades e saídas. | Gates de implantação G0–G7 (que são a jornada do programa, não a rotina). |
| **Adoption** | Uso sustentado por personas/escopos definidos. | Número de agents criados. |
| **Discovery** | Usuário encontra opção existente adequada antes de criar outra. | Inventory técnico. |
| **Quality** | Grau em que outputs/actions atendem critérios do contexto. | Satisfação apenas. |
| **Baseline** | Medida anterior ou contrafactual explícito usado para comparação. | Target. |
| **Outcome** | Mudança observável em processo, pessoa, risco ou negócio. | Output do agent. |
| **Value evidence** | Conjunto de baseline, adoption, quality, risk, cost e outcome com limitações declaradas. | ROI inferido de uso. |

## Regra de terminologia

Se um novo documento usar sinônimo ou definição incompatível, ele deve:

1. referenciar a definição canônica;
2. explicar a diferença de contexto;
3. propor alteração do glossary se a diferença for permanente.

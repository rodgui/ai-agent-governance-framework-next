# Guia de consumo — framework e template de implementação

Este guia explica **qual repositório usar, em que momento e com qual resultado**. Ele não substitui a rota de implantação. Para começar uma implantação, vá diretamente para [Comece aqui](docs/start-here.md). Para estudar capítulo a capítulo, use o [handbook](docs/handbook/README.md).

## Os dois repositórios

O ecossistema tem dois papéis diferentes:

| Repositório | Papel | Use quando... |
|---|---|---|
| [`ai-agent-governance-framework-next`](https://github.com/rodgui/ai-agent-governance-framework-next) | **Conhecimento canônico**: policy modular, capítulos, controls, schemas, patterns, templates e casos fictícios. | Você precisa entender, decidir, desenhar ou consultar a governança. |
| [`ai-agent-governance-implementation-template`](https://github.com/rodgui/ai-agent-governance-implementation-template) | **Workspace de instância**: registros, assessments, decisões, evidências e lifecycle de uma organização. | Você vai preencher dados e evidências reais sob um boundary autorizado. |

> **Regra de precedência:** o framework é a fonte única de verdade. O template referencia conteúdo canônico por ID e versão; não copia policy, controls ou templates. Registros organizacionais reais pertencem ao template, não a este repositório.

## Qual rota usar

| Sua intenção | Rota recomendada | O que ela entrega |
|---|---|---|
| Implantar governança | [Comece aqui](docs/start-here.md) | Ordem de decisões, trilhas, artefatos e gates. |
| Estudar o método | [Handbook](docs/handbook/README.md) | Leitura linear em cinco partes. |
| Localizar um tema | [Índice](docs/index.md) | Jornadas por persona e objetivo. |
| Entender o ecossistema | Esta página | Boundary entre conhecimento canônico e instância organizacional. |

## Como estudar o framework

A leitura editorial é organizada em cinco partes:

1. **Fundamentos:** o que é governança agentic, qual o mandato e qual vocabulário será usado.
2. **Policy, operating model e risco:** quem decide, qual authority existe, como risco e admissibilidade são separados.
3. **Domínios de controle:** inventário, lifecycle, identidade, dados, tools, modelos, segurança, assurance, operações e adoção.
4. **Método e toolkit:** gates, capability map, roadmaps, patterns, controls, schemas, templates e exemplos.
5. **Fontes e limitações:** bibliografia, crosswalks, provenance e limites de interpretação.

Cada capítulo deve permitir três níveis de leitura: **entender** o problema e os conceitos; **decidir** a opção aplicável; e **executar** os passos, artefatos e evidências que tornam a capacidade operacional.

## Como implantar com os dois repositórios

A implantação combina conteúdo canônico e registros organizacionais. A sequência de alto nível é:

| Momento | Framework | Template de implementação |
|---|---|---|
| **Mandato e baseline** | Brief, fundamentos, playbook, capability map e maturity model. | Governance charter, scope, authorities e baseline organizacional. |
| **Desenho** | Risco, operating model, arquitetura, controls, patterns e catálogo de artefatos. | RACI, decision rights, risk records, assessments e target maturity. |
| **Fundações** | Registry/blueprint schemas, identity/data/tool/model standards e Minimum Production Bar. | Registros de agentes, owners, dependências, permissions e evidence references. |
| **Caso real** | Capítulos 03–08, schemas, templates, examples e gates G0–G7. | Um dossiê completo de agente, com intake, risco, blueprint, release evidence, operação e sunset criteria. |
| **Escala** | Capítulos 09–10, patterns de runtime, attestation, FinOps e melhoria. | Incidentes, attestation, auditoria, decisões de portfólio e registros de aposentadoria. |

A ordem de execução é `baseline → desenho → fundações → um caso real → escala`. Os gates G0–G7 são pontos de decisão, não semanas de calendário. O programa de 90 dias e o programa de 24 semanas são patterns adaptáveis; não são SLAs nem requisitos universais.

## O que preencher e o que não preencher

O template deve conter registros reais apenas quando houver workspace, authority e boundary apropriados. Os casos fictícios deste framework servem como espelho de coerência e não devem ser promovidos a evidência de produção.

O template deve registrar owners, status, versão do framework, evidence links, limitações, decisões e próximas revisões. Dados ausentes permanecem `missing`; não devem ser inferidos. Secrets, tokens, dados pessoais, evidências confidenciais e informações de clientes ou empregadores não pertencem a este repositório público.

## O dossiê de um agente

Um agente não é governado por um formulário único. Seu dossiê é o conjunto de artefatos vinculados por `agent_id`:

1. use-case intake;
2. autoavaliação;
3. risk record;
4. registry entry;
5. blueprint versionado;
6. impact assessment quando acionado;
7. release evidence manifest;
8. registros de mudanças, operação, incidentes, attestation e sunset.

O framework define o contrato e os templates. O template de implementação é o lugar onde a organização preenche esses artefatos com dados reais.

## O que não esperar

Este repositório não é um produto pronto, um SaaS, uma certificação ou uma promessa de conformidade. Ele não seleciona fornecedor e não oferece thresholds universais. Implementações de fornecedores aparecem somente como exemplos, estudos ou mappings não normativos.

Nenhum control foi exercitado contra um estate real. A primeira implantação é também uma validação operacional do método; a organização deve recalibrar tiers, prazos, evidence requirements e authorities com suas próprias evidências.

## Referências rápidas

| Pergunta | Documento |
|---|---|
| Por onde começo a implantação? | [Comece aqui](docs/start-here.md) |
| Qual é a ordem de estudo? | [Handbook](docs/handbook/README.md) |
| Como escolher um template? | [Catálogo de artefatos](toolkit/artifact-catalog.md) e [Templates](toolkit/templates/README.md) |
| Quais são os controles? | [Control catalog](toolkit/controls/README.md) |
| Quais são os contratos estruturados? | [Schemas](toolkit/schemas/README.md) |
| Como estudar um caso completo? | [Casos de referência](toolkit/examples/cases/README.md) |
| Onde preencher registros reais? | [`implementation-template`](https://github.com/rodgui/ai-agent-governance-implementation-template) |

Para a documentação de contribuição, provenance e manutenção do corpus, consulte [CONTRIBUTING.md](CONTRIBUTING.md). Essa superfície é para maintainers, não para a rota de implantação.

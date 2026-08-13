---
title: Framework de governança de agentes de IA
status: maintained
owner: framework-maintainers
last_reviewed: 2026-08-13
review_cycle: quarterly
---

# Framework de governança de agentes de IA

Framework canônico e **vendor-neutral** para governar sistemas de IA e agentes desde o conceito até a operação sustentada. O repositório combina policy modular, capítulos didáticos, controles verificáveis, schemas estruturados, patterns, templates e casos de referência fictícios.

O objetivo não é produzir mais um documento de princípios. É ajudar uma organização a responder, com autoridade e evidência: **o que existe, quem responde, qual risco é aceitável, como o agente deve funcionar, o que precisa ser comprovado para liberá-lo, como contê-lo em operação e quando mantê-lo, corrigí-lo ou aposentá-lo**.

> **Para uma organização que vai implantar governança, a rota principal é [Comece aqui](docs/start-here.md).** Essa página explica a ordem de decisão e leva ao playbook de implementação. Não é necessário ler todo o repositório antes de começar.

## Escolha sua rota

| O que você precisa fazer | Comece por | Resultado esperado |
|---|---|---|
| **Implantar governança na organização** | [Comece aqui — rota de implantação](docs/start-here.md) | Escopo, baseline, fases, owners, gates e primeiro caso ponta a ponta. |
| **Entender como o framework funciona** | [Handbook — leitura linear](docs/handbook/README.md) | Compreensão progressiva dos fundamentos, domínios, método e toolkit. |
| **Localizar um tema ou artefato** | [Índice por persona e objetivo](docs/index.md) | Documento, template, schema, control ou pattern relevante para uma pergunta específica. |
| **Entender framework e template** | [Guia de consumo](CONSUMO.md) | Distinção entre conhecimento canônico e registros da organização. |
| **Instanciar registros reais** | Repositório [`ai-agent-governance-implementation-template`](https://github.com/rodgui/ai-agent-governance-implementation-template) | Workspace separado para preencher dados e evidências da organização. |

O **framework-next** é a fonte de conhecimento. O **implementation-template** é o esqueleto para uma organização preencher seus próprios registros. O template referencia IDs e versões do framework; não copia policy, controls ou templates canônicos.

## O que o framework contém

| Área | Conteúdo |
|---|---|
| `docs/framework/` | 11 capítulos canônicos, do controle do documento a métricas e melhoria contínua. |
| `docs/handbook/` | Ordem editorial de estudo em cinco partes: fundamentos; policy, operating model e risco; domínios; método e toolkit; fontes. |
| `docs/start-here.md` | Rota prescritiva de implantação, com quatro trilhas e decisões esperadas. |
| `toolkit/controls/` | Catálogo de 44 controls, cada um com owner, tiers, verificação, evidência e indicação de bloqueio. |
| `toolkit/schemas/` | Contratos JSON para registry, blueprint, catalogs, evidence manifests e audit events. |
| `toolkit/templates/` | Templates reutilizáveis para charter, RACI, intake, risco, assessments, release, attestation e sunset. |
| `toolkit/examples/` | Exemplos e casos de referência fictícios para demonstrar a coerência do método. |
| `toolkit/patterns/` | Patterns para control/assurance planes, registry/blueprint, risco, observabilidade, quarentena e governance federada. |
| `research/` | Fontes, bibliografia, limitações e crosswalks externos; mappings não equivalem a conformidade. |
| `project/` | Decisões, migrações e histórico preservado; decisões materiais devem sobreviver à troca de pessoas. |

## Modelo mental em uma frase

> **A organização define mandato e authority; o registry torna o estate visível; o risco define proporcionalidade; a arquitetura coloca controles fora do modelo; a evidência sustenta o release; o runtime gera sinais e ações; o valor e o lifecycle decidem continuidade.**

O framework separa deliberadamente conceitos que costumam ser confundidos:

| Conceito | Pergunta que responde |
|---|---|
| **Risk tier T1–T4** | Quão severa pode ser a exposição se o agente falhar ou for abusado? |
| **Admissibilidade** | Este uso pode operar, sob quais condições, ou deve ser proibido? |
| **Gate G0–G7** | Qual decisão do programa autoriza, condiciona, bloqueia ou encerra o avanço? |
| **Processo P1–P8** | Qual rotina recorrente o agente atravessa, da criação ao sunset? |
| **Template/schema** | Qual artefato deve ser produzido e qual contrato estruturado o valida? |

T1–T4 mede criticidade; `permitted`, `conditional`, `restricted` e `prohibited` medem admissibilidade. **T4 não é sinônimo automático de `restricted` ou `prohibited`.**

## Maturidade e limites

O release atual do framework é `1.1.0`. Os 44 controls, schemas e exemplos foram validados localmente, mas nenhum control foi exercitado contra um estate real. Os casos de referência são fictícios e demonstram coerência do método, não eficácia. Thresholds, tiers, prazos, authorities e mappings precisam ser calibrados pela organização adotante com dados e obrigações do próprio contexto.

O framework não é um produto pronto, não certifica conformidade, não substitui análise jurídica ou regulatória e não seleciona um fornecedor. Produtos e plataformas podem aparecer como exemplos ou mappings; requisitos normativos permanecem independentes de fornecedor.

## Regras de consumo

Para preservar a qualidade do framework, cada requisito normativo deve ser ligado à sua aplicabilidade, owner, evidência e método de validação. Campos ausentes permanecem explicitamente `missing`; não são inferidos. Decisions e exceptions precisam preservar authority, rationale, condições, expiry e residual risk quando aplicável. Segredos, dados pessoais, evidência de produção e informações corporativas confidenciais não pertencem a este repositório.

As instruções detalhadas de contribuição, provenance, validação e build ficam na documentação de [contribuição e manutenção](CONTRIBUTING.md). Elas não fazem parte da rota de implantação organizacional.

## Estado e referências

- Framework release: `1.1.0` — source `5545d9227624400ab8bb707b6032b2f61329a36e`.
- Consulte o [CHANGELOG](CHANGELOG.md) para mudanças visíveis e o [handbook](docs/handbook/README.md) para a ordem editorial.
- Licença: [CC BY 4.0](LICENSE).

---
title: 0001 Canonical Source And Product Boundaries
status: maintained
last_reviewed: 2026-08-11
review_cycle: quarterly
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# 0001 Canonical Source And Product Boundaries

Este artefato consolida fontes validadas segundo a estratégia registrada no plano de migração. A união preserva conteúdo único e registra a origem de cada bloco.

## Fonte: `docs/architecture/decisions/0002-modular-policy-vendor-neutrality-and-commercial-boundary.md`

> **Provenance:** migrated from `docs/architecture/decisions/0002-modular-policy-vendor-neutrality-and-commercial-boundary.md` at authoritative commit `5545d9227624400ab8bb707b6032b2f61329a36e`. Content is adapted only for repository boundaries and links.

### ADR-0002 — Policy modular, neutralidade estrita e boundary comercial

#### Contexto

A primeira consolidação tratou a Policy v1 como baseline normativa, usou referências Microsoft para acelerar a arquitetura e colocou material comercial dentro da área executiva. Essa estrutura foi útil para iniciar o framework, mas cria três ambiguidades: a policy histórica parece ser fonte permanente, referências de fornecedor podem parecer componentes da solução e o conteúdo comercial pode ser confundido com conhecimento canônico.

O objetivo atualizado é que o corpus modular evolua para constituir a policy final, mantendo neutralidade real de fornecedor e mantendo o conteúdo comercial fora do framework público.

#### Forças e constraints

- preservar a rastreabilidade da Policy v1 sem mantê-la como dependência normativa;
- evitar uma policy monolítica divergente dos módulos canônicos;
- permitir referências e mappings sem lock-in conceitual ou técnico;
- reutilizar o conhecimento sem misturar conteúdo público, normativo e comercial;
- manter handbook e futuras publicações derivados da mesma fonte;
- adiar ebook até decisão posterior.

#### Opções consideradas

##### Opção A — Manter Policy v1 como baseline e material comercial em `docs/executive/`

**Vantagens:** menor mudança estrutural e narrativa normativa simples.

**Desvantagens:** perpetua lacunas da v1, multiplica citações históricas e mistura comunicação do framework com produto pessoal.

##### Opção B — Criar uma nova policy monolítica e manter mappings no núcleo

**Vantagens:** documento único de aprovação e leitura direta.

**Desvantagens:** duplica controls, arquitetura e playbooks; mappings podem contaminar o desenho canônico; manutenção tende a divergir.

##### Opção C — Policy modular canônica, vendors opcionais e conteúdo comercial fora do repositório

**Vantagens:** uma única fonte de verdade, portabilidade, evolução versionada e boundary comercial explícito.

**Desvantagens:** exige índices claros, disciplina de status e release, além de atualização de links e validações.

#### Decisão

Adotar a opção C:

1. `docs/governance/policy.md` é a entrada normativa do framework modular e define a composição da policy candidate/final.
2. A Policy v1 é preservada byte a byte e indexada como origem histórica, sem ser citada repetidamente como fonte corrente.
3. O núcleo define capabilities, outcomes, controls, evidências e boundaries sem exigir Microsoft, Agent 365, Cloudflare ou qualquer fornecedor.
4. Conteúdo de fornecedor fica limitado a fontes, estudos de caso, assessments e mappings opcionais e removíveis.
5. Conteúdo comercial é mantido fora do repositório público, separado da policy, do handbook e de `docs/executive/`.
6. A oferta comercial usa três pacotes compostos pelos nove módulos existentes.
7. Ebook/PDF permanece adiado; publicação futura será derivada dos módulos canônicos.

#### Consequências positivas

- a policy final pode evoluir sem ficar limitada pela v1;
- vendors não se tornam dependências implícitas do framework;
- readers distinguem conhecimento, policy, evidência externa e produto comercial;
- o handbook continua uma ordem editorial pura;
- packaging e pricing podem evoluir sem alterar o conteúdo canônico.

#### Consequências negativas

- a adoção normativa exige release e authority explícitas;
- links históricos e crosswalks precisam ser mantidos separadamente;
- a modularidade requer boa navegação e prevenção de inconsistências entre módulos;
- propostas comerciais precisam declarar exatamente quais módulos foram incluídos.

#### Riscos e mitigação

| Risco | Mitigação |
|---|---|
| modularidade diluir a força normativa | entrada única de policy, statuses e release versionada |
| vendor retornar ao núcleo por exemplos | quality gate e revisão de paths/linguagem |
| conteúdo comercial redefinir o framework | boundary explícito e links unidirecionais para o conteúdo canônico |
| v1 ser apagada ou reescrita | arquivo histórico protegido por hash |

#### Critérios de validação

- a Policy v1 mantém o mesmo SHA-256 histórico;
- `docs/handbook/` e `docs/executive/` não contêm produto comercial;
- os nove módulos estão mapeados uma única vez para três pacotes;
- core docs não tratam produtos ou fornecedores como requisito da solução;
- a remoção de um mapping de fornecedor não quebra policy, controls, schemas ou gates;
- CI, links, schemas e lint permanecem verdes.

#### Evidência da decisão

Decisão aprovada por Rodrigo Garcia Guimarães em 2026-08-09, junto com tese, cinco planos, oito gates, maturity model, modelo comercial, visual, público principal, packaging `3 pacotes / 9 ofertas` e autorização de merge após incorporação destas mudanças.


## Fonte: `docs/architecture/decisions/0003-single-canonical-source-and-guide-absorption.md`

> **Provenance:** migrated from `docs/architecture/decisions/0003-single-canonical-source-and-guide-absorption.md` at authoritative commit `5545d9227624400ab8bb707b6032b2f61329a36e`. Content is adapted only for repository boundaries and links.

### ADR-0003 — Fonte única canônica e absorção do guia externo

#### Contexto

O conhecimento de governança de agentes deste autor existia em dois corpora paralelos e **não reconciliados**:

1. este repositório — policy modular, operating model, arquitetura em cinco planos, 38 controls, quatro schemas, decision gates G0–G7 e quality gates em CI;
2. um guia externo em formato de documento — "Governança de Agentes de IA em Escala", com doze domínios, playbooks de implementação passo a passo, roadmap de programa de 24 semanas e exemplos preenchidos.

Os dois tinham massa comparável (aproximadamente 240 mil e 258 mil caracteres) e **nenhum citava o outro**. Divergiam em taxonomia de risco, arquitetura de domínios e sequenciamento de implantação. Um leitor externo não tinha como saber qual era normativo.

A análise mostrou que a divergência não era de conteúdo concorrente, e sim de **camada**:

| | Repositório | Guia externo |
|---|---|---|
| Textura | normativa: requisito, control, evidência, decisão, métrica, antipattern | procedural: passo a passo, "como produzir", exemplo preenchido |
| Verificabilidade | schemas, control catalog e CI | nenhuma |
| Executabilidade | baixa — diz o quê, raramente como | alta — playbooks e artefatos prontos |

O repositório tem o esqueleto normativo. O guia tem a camada de execução. A ausência de decisão sobre a relação entre eles era, isoladamente, o maior risco do trabalho.

#### Forças e constraints

- o objetivo declarado é ter **uma** fonte final, canônica, fluida e estruturada;
- manter dois corpora obriga a sincronizar manualmente decisões normativas — divergência é questão de tempo, não de disciplina;
- o guia não tem versionamento verificável: o arquivo entregue declara versão 3.4 na capa, 3.3 nos metadados de título e 3.2 na descrição, sem autoria ou data confiáveis;
- a densidade normativa do repositório é sua principal força e não pode ser diluída por importação literal;
- o ADR-0002 já estabelece policy modular, neutralidade de fornecedor e boundary comercial — a absorção não pode violar nenhum dos três;
- a camada procedural é exatamente o que falta para propor implantação sustentada.

#### Opções consideradas

##### Opção A — Manter os dois corpora e sincronizar manualmente

**Vantagens:** nenhum trabalho imediato; o guia continua distribuível como está.

**Desvantagens:** perpetua taxonomias incompatíveis, duplica manutenção, e mantém a ambiguidade sobre qual fonte é normativa. Não atende ao objetivo.

##### Opção B — Substituir o repositório pelo guia

**Vantagens:** o guia é mais executável e mais fácil de ler linearmente.

**Desvantagens:** descarta schemas, control catalog, decision gates e CI — a parte verificável do trabalho e a única que sustenta claims perante um cliente. Regressão material.

##### Opção C — Repositório como destino único, absorvendo a camada procedural do guia

**Vantagens:** preserva rigor e ganha executabilidade; uma fonte, versionada, com CI; o guia pode ser regenerado a partir dos módulos quando desejado.

**Desvantagens:** exige migração em ondas, reescrita no estilo canônico e resolução explícita dos conflitos de taxonomia e sequenciamento.

#### Decisão

Adotar a opção C.

1. **Este repositório é a fonte única e final.** Nenhum outro artefato é normativo.
2. O guia externo passa a ser **origem histórica**, na mesma categoria da Policy v1: preservado para rastreabilidade, não citado como fonte corrente.
3. O conteúdo procedural do guia é absorvido **reescrito no estilo canônico** — objetivo, requisitos, artefatos, evidências, métricas, failure modes e decision gate — nunca colado literalmente.
4. Em qualquer conflito entre guia e repositório, **prevalece o repositório**. Especificamente: a taxonomia de tiers, o contrato de decision gates e as regras de linguagem de assurance do repositório são inegociáveis.
5. A absorção acontece em ondas, cada uma verificável por CI, e cada domínio novo só existe quando altera decisão, authority, control ou evidência.
6. Publicações futuras em outros formatos são **derivadas** dos módulos canônicos, nunca mantidas como cópias editoriais independentes.

#### Consequências positivas

- desaparece a ambiguidade sobre qual fonte é normativa;
- o corpus ganha a camada de execução que faltava para implantação real;
- a manutenção passa a ter um só lugar, com CI e versionamento;
- a camada comercial passa a ter lastro verificável nos artefatos que promete.

#### Consequências negativas

- a migração é trabalhosa e acontece ao longo de várias releases;
- durante a transição, cópias antigas do guia continuam circulando com taxonomia divergente;
- a reescrita no estilo canônico perde parte da fluidez narrativa do guia.

#### Riscos e mitigação

| Risco | Mitigação |
|---|---|
| importação literal inflar o corpus e diluir a densidade normativa | reescrita obrigatória no formato canônico; revisão de sobreposição com `docs/patterns/` antes de criar arquivo |
| conteúdo do guia reintroduzir vocabulário de assurance mais permissivo | regra de precedência do repositório e quality gate de linguagem |
| domínios novos criados por afinidade temática, sem consequência operacional | critério explícito em `docs/architecture/overview.md` |
| cópias antigas do guia continuarem sendo tratadas como normativas | declaração de status em `docs/governance/policy.md` |

#### Critérios de validação

- `docs/governance/policy.md` declara explicitamente o status do guia;
- nenhum documento canônico cita o guia como fonte normativa corrente;
- cada onda de absorção mantém `validate-repository.py`, schemas e lint verdes;
- nenhum conceito importado contradiz o control catalog ou os schemas;
- o handbook permanece uma ordem editorial única, sem segunda fonte.

#### Evidência da decisão

Decisão tomada por Rodrigo Garcia Guimarães em 2026-08-10, após análise comparativa dos dois corpora que identificou vinte gaps de conteúdo e três conflitos estruturais, e após confirmação de que a relação entre guia e repositório nunca havia sido decidida formalmente.

---
title: Comece aqui — trilhas de leitura para implantação
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - index.md
  - handbook/README.md
  - framework/08-implementation-and-adoption.md
---

# Comece aqui — trilhas de leitura para implantação

Esta página existe porque o repositório tem muitos caminhos e uma organização que vai implantar precisa de **um**.

Se o objetivo é estudar, o [handbook](handbook/README.md) é a ordem certa e esta página não é necessária. Se o objetivo é implantar, comece aqui e ignore o resto da navegação até terminar a sua trilha.

## A regra que economiza mais tempo

**Leia o [implementation playbook](framework/08-implementation-and-adoption.md) antes de qualquer outra coisa.**

É o único documento que dá **ordem**. Todos os outros dão **conteúdo**. Ler os domínios antes dele produz a sensação de muita informação e nenhum caminho — que é exatamente o erro que faz programas de governança começarem pela ferramenta.

## Quatro trilhas

Cada trilha termina numa decisão, não numa leitura concluída.

### Trilha 0 — Sponsor e comitê executivo · ~1 hora

1. [Brief executivo](executive/governing-agents-at-scale.md)
2. [Fundamentos](framework/01-mandate-scope-and-principles.md) — apenas as distinções de vocabulário
3. [Operating model](framework/02-governance-and-accountability.md) — a tabela de decision rights
4. [Caso T3](explanations/cases/benefits-eligibility-triage.md) — o que "governança funcionando" significa num caso concreto

**Decisão:** patrocinar, nomear o governance owner e aprovar o mandato.

### Trilha 1 — Quem monta o programa · ~1 semana

1. [Implementation playbook](framework/08-implementation-and-adoption.md) — o contrato dos gates e a dependência real entre eles
2. [Programa de 24 semanas](framework/08-implementation-and-adoption.md) — como pattern adaptável, não cronograma
3. [Catálogo de artefatos](../toolkit/artifact-catalog.md) — o que precisa existir, por owner e fase
4. [Capability map](framework/08-implementation-and-adoption.md) e [maturity model](../toolkit/maturity/maturity-model.md) — medir a base antes de desenhar o alvo
5. [Checklist de autossuficiência](reference/self-sufficiency-checklist.md) — aplicado à sua organização

**Decisão:** escopo, fases, workstreams, gargalos e alvo de maturidade.

### Trilha 2 — Risco, Responsible AI, jurídico e compliance · ~1 semana

1. [Policy modular](framework/00-document-control.md)
2. [Gestão de riscos](framework/04-risk-impact-and-compliance.md) — a tabela dos dez escaladores e a separação entre criticidade e admissibilidade
3. [Minimum Production Bar](../toolkit/controls/minimum-production-bar.md)
4. [Responsible AI](framework/04-risk-impact-and-compliance.md) e [human oversight](framework/02-governance-and-accountability.md)
5. [Evidence pack por tier](framework/07-evaluation-evidence-and-assurance.md)
6. [Control catalog](../toolkit/controls/README.md) — comece pelos `blocking`
7. [Cláusulas de contrato com fornecedor](../toolkit/templates/ai-vendor-contract-clauses.md) — o que compras e jurídico precisam exigir

**Decisão:** tiers calibrados, escaladores adaptados ao setor, triggers de RAI e o que bloqueia release.

### Trilha 3 — Arquitetura e plataforma · ~2 semanas

1. [Arquitetura de referência](framework/06-architecture-and-technical-controls.md)
2. [Mapeamento de capability para tecnologia](framework/06-architecture-and-technical-controls.md) — conecta o framework ao estate que já existe
3. [Registry](../toolkit/registry/README.md), [identidade](framework/06-architecture-and-technical-controls.md), [dados](framework/06-architecture-and-technical-controls.md), [tools e MCP](framework/06-architecture-and-technical-controls.md), [modelos e provedores](framework/06-architecture-and-technical-controls.md)
4. [Schemas](../toolkit/schemas/README.md) e os [casos de referência](../toolkit/examples/cases/README.md), lendo os JSON junto
5. [Design patterns](patterns/README.md)

**Decisão:** source of truth por atributo, pontos de enforcement e o que é comprado versus construído.

## Depois de ler: a ordem de execução

```text
baseline → desenho → fundações → um caso real → escala
```

1. **Baseline** — capability map e maturity assessment com evidência, separando o observado da hipótese.
2. **Desenho** — tiers calibrados com casos reais, operating model e decision rights.
3. **Fundações** — registry, identidade, catálogos de dados e tools, telemetria e Minimum Production Bar.
4. **Um caso real ponta a ponta** — de preferência um T2, que é onde a governança começa a custar.
5. **Escala** — automação de discovery, policy-as-code, attestation e dashboards.

Os gates G0–G7 autorizam avançar entre essas etapas. **A numeração deles não é cronograma** — a dependência real está no [playbook](framework/08-implementation-and-adoption.md#a-numeração-não-é-um-cronograma).

## O que esperar e o que não esperar

O framework é vendor-neutral e verificável: 44 controls com evidência declarada, contratos estruturados e validação automatizada. Nenhum control, porém, foi exercitado contra um estate real — os [casos de referência](../toolkit/examples/cases/README.md) são fictícios e provam coerência do método, não eficácia.

Consequência prática para o programa: **thresholds, tiers e prazos precisam ser recalibrados com os seus dados**, e a primeira implantação é também a primeira validação. Reserve orçamento para isso.

## O resto da navegação

As demais superfícies — [índice por persona e objetivo](index.md), [handbook](handbook/README.md) e o toolkit do [README](../README.md) — são **referência**. Servem para localizar um assunto específico depois, não para decidir por onde começar.

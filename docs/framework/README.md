---
title: Documento mestre e framework de governança
status: maintained
last_reviewed: 2026-08-18
review_cycle: quarterly
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
related:
  - ../start-here.md
  - 00-document-control.md
  - ../../toolkit/README.md
---

# Documento mestre e framework de governança

Este diretório é a **fonte canônica normativa e operacional** da release `1.1.0`. Os capítulos 00–10 consolidam integralmente o corpus aprovado e definem o caminho do mandato inicial ao business as usual.

## Ordem canônica

1. [00 — Controle do documento](00-document-control.md)
2. [01 — Mandato, escopo e princípios](01-mandate-scope-and-principles.md)
3. [02 — Governança e accountability](02-governance-and-accountability.md)
4. [03 — Inventário, portfólio e valor](03-inventory-portfolio-and-value.md)
5. [04 — Risco, impacto e compliance](04-risk-impact-and-compliance.md)
6. [05 — Lifecycle de agentes](05-agent-lifecycle.md)
7. [06 — Arquitetura e controles técnicos](06-architecture-and-technical-controls.md)
8. [07 — Avaliação, evidência e assurance](07-evaluation-evidence-and-assurance.md)
9. [08 — Implementação e adoção](08-implementation-and-adoption.md)
10. [09 — Operações, incidentes e continuidade](09-operations-incidents-and-continuity.md)
11. [10 — Métricas, revisão e melhoria contínua](10-metrics-review-and-improvement.md)

Para implantação guiada, use [Comece aqui](../start-here.md). Para localizar conteúdo por papel ou estágio, use o [índice](../index.md).

## Relação com o toolkit

O Master Document define requisitos, decisions, authorities e evidence expectations. O [toolkit](../../toolkit/README.md) fornece controles, schemas, templates, patterns, exemplos e instrumentos de avaliação. O toolkit implementa o contrato; não cria uma policy paralela.

## Boundaries

- conteúdo de fornecedor permanece em pesquisa, caso, mapping ou histórico explicitamente identificado;
- a Policy v1 permanece preservada em `project/history/` e não governa silenciosamente a release corrente;
- instanciação organizacional vive em repositório independente do framework;
- release do framework (`1.1.0`), catálogo (`1.2.0`) e schemas (`2.0`) têm versionamento distinto;
- adoção exige authority organizacional; versionar o repositório não cria compliance nem aprovação.

## Regra de precedência

Em conflito, prevalecem nesta ordem: decisão corrente aprovada, capítulo canônico, catálogo/schema versionado e instrumento derivado. Histórico e estudos de caso preservam provenance, mas não alteram requisitos atuais sem decisão explícita.

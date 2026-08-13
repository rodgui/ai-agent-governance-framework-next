---
title: Handbook de governança de IA e agentes
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-13
review_cycle: quarterly
related:
  - ../index.md
  - ../../README.md
---

<!-- markdownlint-disable MD029 -->
<!-- A numeração 1–32 é deliberadamente contínua entre as partes editoriais. -->

# Handbook de governança de IA e agentes

Este é o caminho editorial canônico para estudar o framework em sequência. Os capítulos continuam em seus domínios canônicos; o handbook organiza a ordem de leitura para reduzir dependências ocultas e não cria uma segunda fonte de conteúdo.

## Qual rota escolher

| Objetivo | Rota |
|---|---|
| **Implantar** | [Comece aqui](../start-here.md), que conduz decisões e aponta para o conteúdo necessário. |
| **Estudar linearmente** | Este handbook, na ordem 1–32. |
| **Localizar uma pergunta** | [Índice por persona e objetivo](../index.md). |
| **Consultar artefatos** | [Toolkit](../../toolkit/README.md), especialmente controls, schemas, templates e examples. |

A leitura linear é deliberadamente diferente da implantação. O handbook ajuda a entender o sistema; o [implementation playbook](../framework/08-implementation-and-adoption.md) dá a ordem de execução. Ler não equivale a aprovar um gate nem a produzir um artefato.

## Três níveis dentro de cada domínio

Um capítulo completo responde a três perguntas, nesta ordem:

| Nível | Pergunta | Onde aparece |
|---|---|---|
| **Entender** | O que é, por que existe e com o que não deve ser confundido? | Visão geral, vocabulário, conceitos, exemplos e armadilhas. |
| **Decidir** | Qual opção aplicar, sob quais critérios e com qual authority? | Tabelas de decisão, tiers, gatilhos, trade-offs e boundaries. |
| **Executar** | Que passos, artefatos e evidências tornam a capacidade operacional? | Playbook, templates, schemas, evidências, referência normativa e decision gate. |

Um capítulo que entrega somente narrativa é material de estudo, não de implantação. O [catálogo de artefatos](../../toolkit/artifact-catalog.md) mostra o que cada domínio deve produzir.

## Parte I — Fundamentos e escolha do mecanismo

1. [Governar agentes em escala — brief executivo](../executive/governing-agents-at-scale.md)
2. [Fundamentos de governança de IA e agentes](../framework/01-mandate-scope-and-principles.md)
3. [Vocabulário canônico](../annexes/glossary.md)
4. [Decisão arquitetural: agente é o mecanismo certo?](../framework/03-inventory-portfolio-and-value.md#32-adequacao-agente-e-o-mecanismo-certo)

Esta parte explica o problema, o vocabulário e a decisão anterior à tecnologia: quando autonomia, interpretação ou uso de tools justificam um agente em vez de workflow ou automação determinística.

## Parte II — Policy, operating model, estate e risco

5. [Policy modular — fonte canônica](../framework/00-document-control.md)
6. [Operating model e decision rights](../framework/02-governance-and-accountability.md)
7. [Estratégia, inventário, registry e valor](../framework/03-inventory-portfolio-and-value.md)
8. [Gestão proporcional de risco, impacto e compliance](../framework/04-risk-impact-and-compliance.md)
9. [Maturity model](../../toolkit/maturity/maturity-model.md)

A sequência desta parte é intencional: primeiro a organização define policy e authority; depois entende o estate e o valor; em seguida classifica criticidade e admissibilidade; por fim mede a capability organizacional. O capítulo 03 usa apenas classificação preliminar quando precisa mencionar mix de risco; a definição normativa de T1–T4 e admissibilidade está no capítulo 04.

## Parte III — Domínios de controle

10. [Lifecycle, mudança material, attestation e retirement](../framework/05-agent-lifecycle.md)
11. [Arquitetura de referência e control plane](../framework/06-architecture-and-technical-controls.md)
    - Mapeamento de capability para tecnologia
    - Atributos de qualidade e boundaries
    - Riscos arquiteturais e pontos de enforcement
12. [Identidade e least privilege](../framework/06-architecture-and-technical-controls.md)
13. [Dados, acesso e provenance](../framework/06-architecture-and-technical-controls.md)
14. [Tools, APIs e MCP](../framework/06-architecture-and-technical-controls.md)
15. [Modelos, provedores e dependências](../framework/06-architecture-and-technical-controls.md)
16. [Segurança de sistemas de IA e agentes](../framework/06-architecture-and-technical-controls.md)
17. [Responsible AI e assurance de impacto](../framework/04-risk-impact-and-compliance.md)
18. [Human oversight e accountability](../framework/02-governance-and-accountability.md)
19. [Evaluations e release evidence](../framework/07-evaluation-evidence-and-assurance.md)
20. [Auditabilidade e evidências](../framework/07-evaluation-evidence-and-assurance.md)
21. [Operações, incidentes e continuidade](../framework/09-operations-incidents-and-continuity.md)
22. [Adoção, enablement e suporte](../framework/08-implementation-and-adoption.md)
23. [Métricas, revisão, FinOps e melhoria contínua](../framework/10-metrics-review-and-improvement.md)

Esta parte acompanha a transformação do risco em desenho e controle: lifecycle e arquitetura definem boundaries; identidade, dados, tools e modelos definem dependências; segurança e Responsible AI tratam ameaças e impacto; assurance produz evidência; operações, adoção e métricas mantêm o sistema vivo.

## Parte IV — Método, patterns e toolkit

24. [Implementation playbook](../framework/08-implementation-and-adoption.md)
25. [Roadmap sugestivo de 90 dias](../framework/08-implementation-and-adoption.md)
    - Capability map
26. [Programa sugestivo de implantação em 24 semanas](../framework/08-implementation-and-adoption.md)
    - Catálogo de artefatos
    - Checklist de autossuficiência
27. [Plano opcional de piloto e critérios de expansão](../framework/08-implementation-and-adoption.md)
28. [Catálogo de design patterns](../patterns/README.md)
29. [Control catalog](../../toolkit/controls/README.md)
30. [Schemas e examples](../../toolkit/schemas/README.md)
    - Migração dos contratos para 2.0
31. [Templates](../../toolkit/templates/README.md)

> **Gates e processos não são a mesma coisa.** G0–G7 são decisões da implantação do programa; P1–P8 são processos operacionais que cada agente atravessa repetidamente. O playbook explica ambos e mantém a distinção explícita.

## Parte V — Fontes e limitações

32. [Fontes, bibliografia e limites de interpretação](../../research/sources/bibliography.md)

As fontes sustentam claims, mappings e rationale. Elas não transformam guidance externo em requisito do framework. Um mapping registra alinhamento direcional, não equivalência, certificação ou conformidade automática.

## Casos e mappings opcionais

- [Casos de referência fictícios](../../toolkit/examples/cases/README.md) — travessia completa do framework por um agente.
- [Microsoft Customer Zero — caso de estudo](../../research/case-studies/microsoft-customer-zero-agent-governance.md) — evidência declarada de implementação, não prova causal.
- [Crosswalk histórico Microsoft × Policy v1](../../project/history/assessments/microsoft-case-study-framework-crosswalk.md) — artefato histórico preservado.

Esses materiais ajudam a interpretar o framework, mas não são capítulos obrigatórios, componentes da solução nem requisitos normativos.

## Critérios de completude de um capítulo

Quando aplicável, um capítulo deve declarar objetivo e boundaries; decisões e requirements; artefatos e owners; controls e evidências; métricas e failure modes; relações com outros domínios; fontes e limitações; e o decision gate que decide se a capacidade está pronta.

## Convenção de status

| Status | Significado |
|---|---|
| `adopted` | decisão normativa aprovada |
| `maintained` | guidance canônico mantido |
| `review` | proposta em revisão |
| `draft` | conteúdo incompleto |
| `deprecated` | preservado apenas para referência |

Uma publicação futura não deve alterar o status do conteúdo-fonte.

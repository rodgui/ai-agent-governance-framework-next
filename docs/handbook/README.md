---
title: Handbook de governança de IA e agentes
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - ../index.md
  - ../../README.md
---

<!-- markdownlint-disable MD029 -->
<!-- A numeração 1–32 é deliberadamente contínua entre as partes editoriais. -->

# Handbook de governança de IA e agentes

Esta é a ordem editorial da edição em português. Os capítulos permanecem em seus domínios canônicos. Uma publicação futura deve ser derivada desta ordem, sem criar uma segunda fonte editorial.

## Como ler

- **Leitura executiva:** capítulos 1, 2, 6 e 10.
- **Implantação:** capítulos 1–32 na ordem.
- **Arquitetura:** capítulos 3, 7, 11–17, 22 e 28–31.
- **Assurance:** capítulos 8, 9 e 18–21.
- **Referência:** consulte por domínio; não precisa seguir a ordem.

### Três níveis dentro de cada domínio

Um domínio canônico é escrito para ser lido em três níveis. Um capítulo completo permite sair dele com algo **produzido, aprovado ou operacionalizado** — não apenas compreendido.

| Nível | Pergunta que responde | Onde aparece no capítulo |
|---|---|---|
| **entender** | o que é e por que existe? | objetivo, conceitos e distinções |
| **decidir** | qual opção aplicar e sob quais critérios? | tabelas de decisão, tiers, trade-offs e gatilhos |
| **executar** | quais passos, evidências e entregáveis tornam a capacidade operacional? | playbook, artefatos, evidências e decision gate |

Um capítulo que só entrega o primeiro nível é material de leitura, não de implantação. O [catálogo de artefatos](../../toolkit/artifact-catalog.md) lista o que cada domínio deve produzir.

## Parte I — Fundamentos

1. [Governar agentes em escala — brief executivo](../executive/governing-agents-at-scale.md)
2. [Fundamentos de governança de IA e agentes](../framework/01-mandate-scope-and-principles.md)
3. [Princípios arquiteturais](../framework/01-mandate-scope-and-principles.md)
   - [Decisão arquitetural: agente é o mecanismo certo?](../framework/03-inventory-portfolio-and-value.md)
4. [Vocabulário canônico](../annexes/glossary.md)

## Parte II — Política, operating model e risco

5. [Policy modular — fonte canônica](../framework/00-document-control.md)
6. [Operating model e decision rights](../framework/02-governance-and-accountability.md)
7. [Arquitetura de referência](../framework/06-architecture-and-technical-controls.md)
   - [Mapeamento de capability para tecnologia](../framework/06-architecture-and-technical-controls.md)
   - [Atributos de qualidade](../framework/06-architecture-and-technical-controls.md)
   - [Riscos arquiteturais](../framework/06-architecture-and-technical-controls.md)
8. [Gestão proporcional de riscos](../framework/04-risk-impact-and-compliance.md)
9. [Maturity model](../../toolkit/maturity/maturity-model.md)

## Parte III — Domínios de controle

10. [Estratégia, portfolio e evidência de valor](../framework/03-inventory-portfolio-and-value.md)
11. [Estate, registry, ownership e taxonomia](../../toolkit/registry/README.md)
12. [Lifecycle, mudança material, attestation e retirement](../framework/05-agent-lifecycle.md)
13. [Identidade e least privilege](../framework/06-architecture-and-technical-controls.md)
14. [Dados, acesso e provenance](../framework/06-architecture-and-technical-controls.md)
15. [Tools, APIs e MCP](../framework/06-architecture-and-technical-controls.md)
16. [Modelos, provedores e dependências de IA](../framework/06-architecture-and-technical-controls.md)
17. [Segurança de sistemas de IA e agentes](../framework/06-architecture-and-technical-controls.md)
18. [Responsible AI e assurance](../framework/04-risk-impact-and-compliance.md)
19. [Human oversight e accountability](../framework/02-governance-and-accountability.md)
20. [Evaluations e release evidence](../framework/07-evaluation-evidence-and-assurance.md)
21. [Auditabilidade e evidências](../framework/07-evaluation-evidence-and-assurance.md)
    - [Integração com o audit universe existente](../framework/07-evaluation-evidence-and-assurance.md)
22. [Operações, resposta e runtime](../framework/09-operations-incidents-and-continuity.md)
23. [Adoção, enablement e suporte](../framework/08-implementation-and-adoption.md)
    - [Developer experience e paved road](../framework/08-implementation-and-adoption.md)

## Parte IV — Método, patterns e toolkit

24. [Implementation playbook](../framework/08-implementation-and-adoption.md)
25. [Roadmap sugestivo de 90 dias](../framework/08-implementation-and-adoption.md)
    - [Capability map](../framework/08-implementation-and-adoption.md)
26. [Programa sugestivo de implantação em 24 semanas](../framework/08-implementation-and-adoption.md)
    - [Catálogo de artefatos do programa](../../toolkit/artifact-catalog.md)
    - [Checklist de autossuficiência](../reference/self-sufficiency-checklist.md)
27. [Plano opcional de piloto e critérios de expansão](../framework/08-implementation-and-adoption.md)
28. [Catálogo de design patterns](../patterns/README.md)
29. [Control catalog](../../toolkit/controls/README.md)
30. [Schemas e examples](../../toolkit/schemas/README.md)
    - [Migração dos contratos para 2.0](../migration/governance-contracts-1x-to-2x.md)
31. [Templates](../../toolkit/templates/README.md)

## Parte V — Fontes e limitações

32. [Fontes e bibliografia](../../research/sources/bibliography.md)

## Casos e mappings opcionais

- [Casos de referência](../../toolkit/examples/cases/README.md) — a travessia completa do framework num agente só
- [Microsoft Customer Zero — caso de estudo](../../research/case-studies/microsoft-customer-zero-agent-governance.md)
- [Crosswalk histórico Microsoft × Policy v1](../../project/history/assessments/microsoft-case-study-framework-crosswalk.md)

Casos e mappings ajudam a interpretar implementações, mas não são capítulos necessários, componentes da solução ou requisitos do framework.

## Artefatos de manutenção do repositório

O [roadmap do produto de conhecimento](../../ROADMAP.md) orienta evolução e release do repositório, mas não é capítulo do handbook nem conteúdo previsto para publicação editorial.

## Critérios de completude de um capítulo

Um capítulo canônico deve declarar, quando aplicável:

- objetivo e boundaries;
- decisões e requisitos;
- artefatos e owners;
- controls e evidências;
- métricas e failure modes;
- relações com outros domínios;
- fontes e limitações.

## Convenção de status

| Status | Significado |
|---|---|
| `adopted` | decisão normativa aprovada |
| `maintained` | guidance canônico mantido |
| `review` | proposta em revisão |
| `draft` | conteúdo incompleto |
| `deprecated` | preservado apenas para referência |

Uma publicação futura não mudará o status do conteúdo-fonte.

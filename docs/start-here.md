---
title: Comece aqui — rota de implantação
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-18
review_cycle: quarterly
supersedes: null
related:
  - index.md
  - handbook/README.md
  - framework/08-implementation-and-adoption.md
---

# Comece aqui — rota de implantação

Esta é a **rota prescritiva** para uma organização que quer sair da ausência de governança formal e chegar a uma capacidade operando no dia a dia. Ela não exige leitura integral do repositório. Você escolhe a trilha conforme seu papel, produz a decisão indicada e só então aprofunda o conteúdo necessário.

Se o objetivo é estudar o framework capítulo a capítulo, use o [handbook](handbook/README.md). Se o objetivo é localizar um assunto específico, use o [índice](index.md). Essas são rotas legítimas, mas não substituem esta página para quem precisa implantar.

## A ordem correta

> **Primeiro entenda a ordem; depois leia o conteúdo necessário para tomar a próxima decisão.**

O [capítulo 08 — Implementação e adoção](framework/08-implementation-and-adoption.md) é o playbook da implantação. Ele explica os gates, as dependências, os roadmaps de referência, o capability map, a adoção e os processos operacionais. Isso não significa que todos precisam ler o capítulo inteiro imediatamente. Significa que ele é a referência da ordem; os demais capítulos fornecem o conteúdo de cada decisão.

A relação decisória é:

```text
G0
 ↓
G1
 ↓
G2 ↔ G3
 ↓
G4
 ↓
G5
 ↓
G6
 ↓
G7
```

G2 e G3 podem se sobrepor: G2 estabelece as fundações de inventário, identidade, dados e ferramentas; G3 estabelece operating model e decision rights. G4 depende das capabilities e das evidências necessárias de G2 e G3, ainda que a execução das workstreams possa ocorrer em paralelo. A numeração dos gates não é um cronograma e não cria uma ordem alternativa.

## Escolha uma trilha

Cada trilha termina em uma decisão. Não considere a trilha concluída porque os documentos foram lidos; conclua quando a decisão estiver registrada com authority, rationale e evidência suficiente.

### Trilha 0 — Sponsor e comitê executivo

**Para quem:** sponsor, executivo, conselho ou autoridade que precisa aprovar mandato, escopo e apetite a risco. **Duração de referência:** cerca de uma hora.

1. Leia o [brief executivo](executive/governing-agents-at-scale.md) para entender o problema de autoridade delegada e escala.
2. Leia as distinções de vocabulário do capítulo [Mandato, escopo e princípios](framework/01-mandate-scope-and-principles.md).
3. Consulte a tabela de decision rights em [Governança e accountability](framework/02-governance-and-accountability.md).
4. Leia o [caso de triagem de elegibilidade](explanations/cases/benefits-eligibility-triage.md) para ver o que significa governança funcionando em um caso concreto.

> **Artefato para produzir agora — Governance Charter.** Use o [template de charter](../toolkit/templates/governance-charter-template.md) para registrar mandato, escopo, authorities, risk appetite e regra de exceção. Consulte o [exemplo de charter](../toolkit/examples/governance-charter.example.md) antes de aprovar.

**Decisão da trilha:** patrocinar ou não o programa; nomear o governance owner; aprovar mandato, escopo inicial, appetite e autoridade de contenção.

### Trilha 1 — Quem monta o programa

**Para quem:** governance owner, arquitetura corporativa, transformação, PMO ou equipe que vai construir a capacidade. **Duração de referência:** cerca de uma semana para a primeira baseline.

1. Leia as seções de gates e de dependências do [implementation playbook](framework/08-implementation-and-adoption.md).
2. Faça o baseline com o [capability assessment worksheet](../toolkit/templates/capability-assessment-worksheet.md) e o [maturity model](../toolkit/maturity/maturity-model.md).
3. Use o [catálogo de artefatos](../toolkit/artifact-catalog.md) para atribuir owner, fase e critério de completude.
4. Defina o target state e o backlog inicial; o programa de 90 dias e o programa de 24 semanas são patterns adaptáveis, não SLAs.

> **Artefato para produzir agora — Maturity Assessment.** Use o [template de maturity assessment](../toolkit/templates/maturity-assessment-template.md) e registre score, confidence, coverage, gaps e target. Evidência fraca produz nota provisória, não nota otimista.

**Decisão da trilha:** escopo, fases, workstreams, gargalos, dependências e alvo de maturidade.

### Trilha 2 — Risco, Responsible AI, jurídico e compliance

**Para quem:** risco, Responsible AI, privacy, jurídico, compliance, segurança e autoridades que definem admissibilidade e assurance. **Duração de referência:** cerca de uma semana para calibrar a primeira rota decisória.

1. Leia o [controle do documento e policy modular](framework/00-document-control.md) para distinguir policy, standard, guidance, procedure e control.
2. Leia [Risco, impacto e compliance](framework/04-risk-impact-and-compliance.md) na ordem: risk tier → red flags → fast path → mapa de decisão → admissibilidade → impact assessment.
3. Use o [risk pre-screen](../toolkit/templates/risk-pre-screen.md), o [risk scoring worksheet](../toolkit/templates/risk-scoring-worksheet.md) e o [Agent Risk Record](../toolkit/templates/agent-risk-record.md).
4. Consulte o [Minimum Production Bar por tier](../toolkit/controls/minimum-production-bar.md) e o [evidence pack proporcional](framework/07-evaluation-evidence-and-assurance.md).
5. Use as [cláusulas para contratos de fornecedor](../toolkit/templates/ai-vendor-contract-clauses.md) quando houver terceiros.

> **Regra essencial:** `T1–T4` é risk tier/criticidade. `permitted`, `conditional`, `restricted` e `prohibited` são admissibilidade. **T4 não significa automaticamente `restricted` ou `prohibited`.**

**Decisão da trilha:** tiers calibrados, red flags, admissibilidade, triggers de Responsible AI, domain reviews, residual-risk authority e controls que bloqueiam release.

### Trilha 3 — Arquitetura e plataforma

**Para quem:** arquitetura, plataforma, IAM, dados, segurança, SRE, integração e engenharia. **Duração de referência:** cerca de duas semanas para mapear capabilities e o primeiro caso.

1. Leia [Arquitetura e controles técnicos](framework/06-architecture-and-technical-controls.md) começando pelos cinco planos e pelos pontos de enforcement.
2. Faça o [capability-to-technology mapping](framework/06-architecture-and-technical-controls.md) sem começar por produto; declare source of truth por atributo.
3. Defina registry, blueprint, identidade, dados, tools/MCP, modelos e runtime.
4. Leia os schemas e o JSON junto com os casos de referência em [Schemas](../toolkit/schemas/README.md) e [Casos](../toolkit/examples/cases/README.md).
5. Consulte os [design patterns](patterns/README.md) apenas depois de entender a capability e o control que o pattern implementa.

> **Artefatos para produzir agora — Registry e Blueprint.** Use o [template de registry](../toolkit/templates/agent-registry-template.md), o [schema de registry](../toolkit/schemas/agent-registry.schema.json), o [template de blueprint](../toolkit/templates/agent-blueprint-template.md) e o [schema de blueprint](../toolkit/schemas/agent-blueprint.schema.json). O registry responde “o que existe e quem responde”; o blueprint responde “como esta versão deve funcionar”.

**Decisão da trilha:** source of truth por atributo, pontos de enforcement, identidade e revogação, mediação de tools, limites de runtime e o que será comprado, integrado ou construído.

## Ordem de execução depois das trilhas

### 1. Baseline

Reconcilie fontes de descoberta, inventory, owners, lifecycle e evidência. Separe o que foi observado do que é hipótese e declare coverage, confidence e gaps. Não transforme ausência de evidência em ausência de risco.

### 2. Desenho

Calibre risk tiers e admissibilidade com casos reais; defina operating model, decision rights, authorities, handoffs, exceptions e target maturity. A regra é proporcionalidade: não aplique a mesma revisão a todos, mas não permita que casos de alto impacto se escondam atrás de um score médio.

### 3. Fundações

Estabeleça registry, blueprint, workload identity, catálogo de fontes certificadas, enterprise tool registry, model/provider catalog, telemetria, Minimum Production Bar e mecanismos de revogação. Cada capacidade deve ter owner, source of truth e evidência recuperável.

### 4. Um caso real ponta a ponta

Escolha um caso representativo, preferencialmente T2, e atravesse intake, adequação, registry, risco, blueprint, avaliação, release evidence, publicação, operação, incidente simulado, attestation e sunset criteria. Use os [casos fictícios de referência](../toolkit/examples/cases/README.md) como espelho de coerência, não como prova de eficácia.

### 5. Escala

Só depois de provar o caminho manual com um caso real, automatize discovery, policy-as-code, JML, attestation, behavioral analytics, FinOps e dashboards. O paved road deve ser mais simples que contornar a governança.

## Quando sair desta página

| Se você precisa... | Vá para... |
|---|---|
| entender o contrato dos gates | [Implementation playbook](framework/08-implementation-and-adoption.md) |
| estudar capítulo a capítulo | [Handbook](handbook/README.md) |
| localizar uma pergunta ou persona | [Índice](index.md) |
| preencher registros de uma organização | [Implementation template](https://github.com/rodgui/ai-agent-governance-implementation-template) |
| consultar controls, schemas e templates | [Toolkit](../toolkit/README.md) |

## O que o framework não promete

O framework não é um produto pronto, não certifica conformidade, não substitui análise jurídica ou regulatória e não fornece thresholds universais. Os casos são fictícios; a primeira implantação é também a primeira validação operacional. Reserve esforço para recalibrar tiers, prazos, evidence requirements e authorities com dados reais.

---
title: Casos de referência
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-18
review_cycle: quarterly
supersedes: null
related:
  - ../README.md
  - ../../../docs/framework/08-implementation-and-adoption.md
---

# Casos de referência

## Objetivo

Cada domínio canônico explica uma capacidade. Nenhum domínio, sozinho, mostra as capacidades **encaixando**. Os casos de referência atravessam o framework de ponta a ponta, de G0 a G7, num agente só.

Servem a três leituras diferentes:

- **para aprender** — ver a sequência real de decisões em vez de doze domínios isolados;
- **para implantar** — ter um preenchimento concreto de cada artefato antes de produzir o próprio;
- **para desafiar o framework** — a travessia expõe contradição que leitura por domínio não expõe.

A terceira já se pagou. Escrever o percurso do primeiro caso revelou que o registro de decisão de release dizia `condition`, com quatro condições, enquanto o manifesto legível por máquina dizia `approved` e não carregava condição nenhuma. Nenhum dos dois documentos estava errado isoladamente; a contradição só existia entre eles.

## Casos

| Caso | Tier | Admissibilidade | O que demonstra |
|---|---|---|---|
| [Meeting Notes Summarizer](meeting-notes-summarizer/README.md) | T1 | `permitted` | a rota automatizada gerando o evidence pack em vez de dispensá-lo |
| [Service Desk Knowledge Agent](../../../docs/cases/service-desk-knowledge-agent.md) | T2 | `permitted` | o percurso completo de um agente transacional interno, com release condicional e condições verificáveis |
| [Benefits Eligibility Triage](../../../docs/explanations/cases/benefits-eligibility-triage.md) | T3 | `conditional` | criticidade e admissibilidade divergindo, veto de Responsible AI e suspensão automática por condição violada |

Os casos usam a mesma organização fictícia, para que se leia um portfólio e não três exemplos desconexos. Uma implantação real convive com tiers diferentes sob o mesmo operating model, e é isso que precisa aparecer.

## Simulação transversal de promoção de ADRs

O [Synthetic ADR promotion validation](adr-promotion-synthetic-validation/README.md) é um case fictício transversal para exercitar ADR-0013, ADR-0014 e ADR-0015 de ponta a ponta. Ele demonstra delegation, observability, cross-plane arbitration, denies, containment, recovery, evidence packaging e substitution/exit. Não recebe tier ou admissibility: não é um caso de implantação nem evidence operacional.

## Cobertura e extensões planejadas

A cobertura publicada hoje percorre T1, T2 e T3. Um futuro caso T4 deve demonstrar explicitamente que **T4 não significa `prohibited`**: risk tier e admissibility continuam dimensões independentes, com rationale e authority próprios.

A extensão multi-agent T3/T4 deve exercitar supervisor, worker, delegation edge, authority attenuation, depth, fan-out, budget, expiry, revocation, múltiplos control planes, state-changing tool, policy deny, observabilidade AI-native, containment, replay/retry denial, recovery, reactivation e evidence lineage. O pattern, os exemplos fictícios existentes e o [case sintético de promoção de ADRs](adr-promotion-synthetic-validation/README.md) fornecem parte dos cenários; o case não declara cobertura de estate.

A estrutura permanece intencional: `toolkit/examples/cases/<case>/` contém records estruturados e fixtures; narrativas humanas permanecem em `docs/cases/` ou `docs/explanations/cases/`. Os casos são integration tests do framework, não production evidence.

## Como ler

Cada caso segue os oito [decision gates](../../../docs/framework/08-implementation-and-adoption.md) na ordem. Em cada gate: o que existia antes, o que a decisão exigiu, quem decidiu e qual artefato ficou como evidência.

Os artefatos referenciados são reais no repositório e validados pelo CI — schema, invariantes cross-record e hash de artefato. Um caso cujo JSON não valida deixa de ser caso e vira ilustração.

## Limites

Os casos são **fictícios e sanitizados**. Demonstram que o método é coerente e executável; **não demonstram eficácia**. Nenhum control deste repositório foi exercitado contra um estate real — é o critério 10 do [checklist de autossuficiência](../../../docs/reference/self-sufficiency-checklist.md), e permanece aberto por isso.

Thresholds, tiers e decisões dos casos são ilustrativos. Copiá-los sem recalibrar para o próprio contexto é o antipattern que o domínio de risco chama de "copiar thresholds de outro contexto".

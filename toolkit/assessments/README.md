---
title: Assessments
status: maintained
last_reviewed: 2026-08-13
review_cycle: quarterly
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# Assessments
Este artefato consolida fontes validadas segundo a estratégia registrada no plano de migração. A união preserva conteúdo único e registra a origem de cada bloco.

## Fonte: `assessments/README.md`

> **Provenance:** migrated from `assessments/README.md` at authoritative commit `5545d9227624400ab8bb707b6032b2f61329a36e`. Content is adapted only for repository boundaries and links.

### Assessments

Avaliações comparativas, de risco, maturidade, tecnologia e control effectiveness.

> **Quando usar uma avaliação.** Use assessment para pedir uma decisão contextual — priorizar capability, classificar risco, comparar alternativa, verificar effectiveness ou aceitar uma lacuna. Assessment é evidência organizacional com escopo, corte e limitações; não é policy, não substitui controls e não converte um score em conformidade.

| Pergunta | Artefato inicial |
|---|---|
| Quão madura está a capability? | [Maturity model](../maturity/maturity-model.md) + [Maturity Assessment](../templates/maturity-assessment-template.md) |
| O caso tem risco ou impacto aceitável? | [Risk record](../templates/agent-risk-record.md) + assessment aplicável |
| A tecnologia ou fornecedor atende ao contexto? | [Assessment template](../templates/assessment-template.md) + cláusulas/controles aplicáveis |
| O control opera com eficácia no escopo? | evidence package, verification method e peer/independent challenge |

#### Artefatos

- [Crosswalk histórico Microsoft Customer Zero × Policy v1](../../project/history/assessments/microsoft-case-study-framework-crosswalk.md) — registro depreciado da primeira consolidação; não é fonte normativa corrente.
- [Maturity model](../maturity/maturity-model.md) — escala e dimensões.
- [Maturity assessment example](../examples/maturity-assessment.example.json) — record fictício validado.
- [Assessment templates](../templates/README.md) — coleta e decisão humana.

#### Requisitos mínimos

Todo assessment declara:

- scope e exclusions;
- criteria e evidence cutoff;
- assessor e independence;
- evidence, coverage e confidence;
- gaps, conflicts e limitations;
- decision requested;
- owners, expiry e next review.

Score não é compliance. Missing evidence não é aprovação.

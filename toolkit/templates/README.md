---
title: Templates
status: maintained
last_reviewed: 2026-08-11
review_cycle: quarterly
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
related:
  - ../schemas/README.md
  - ../artifact-catalog.md
---

# Templates

Templates para coleta, decisão, evidence e comunicação. Quando houver schema correspondente, o documento humano deve ser convertido para um record estruturado e validado.

Esta página lista os templates por finalidade. Para saber **quando** cada artefato precisa existir e sob responsabilidade de quem, use o [catálogo de artefatos](../artifact-catalog.md).

## Governança e arquitetura

- [Governance Charter](governance-charter-template.md)
- [Governance RACI](governance-raci-template.md)
- [Terms of reference de fórum](governance-forum-tor.md)
- [Dicionário de taxonomia e metadados](agent-taxonomy-dictionary.md)
- [Agent Registry Record](agent-registry-template.md)
- [Agent Blueprint](agent-blueprint-template.md)
- [ADR](adr-template.md)
- [Control Implementation Record](control-implementation-record-template.md)

## Assessment e release

- [Maturity Assessment](maturity-assessment-template.md)
- [Capability Assessment Worksheet](capability-assessment-worksheet.md)
- [Intake de caso de uso](use-case-intake.md)
- [Agent Use-Case Portfolio](use-case-portfolio.md)
- [Risk pre-screen](risk-pre-screen.md)
- [Agent Risk Record](agent-risk-record.md)
- [Autoavaliação de agente](self-assessment-form.md)
- [Exemplo de autoavaliação](../examples/self-assessment.example.md)
- [Technology Assessment](assessment-template.md)
- [Cláusulas de contrato com fornecedor de IA](ai-vendor-contract-clauses.md)
- [Checklist de decisão de release](release-decision-checklist.md)
- [Release Evidence Manifest](release-evidence-manifest.md)
- [Attestation and Sunset Record](attestation-sunset-record.md)
- [Sunset Plan](sunset-plan.md)

## Operação e analytics

- [Behavioral Analytics Use Case](behavioral-analytics-use-case.md)

## Comunicação e pesquisa

- [Executive Brief](executive-brief-template.md)
- [Study Note](study-note-template.md)
- [Experiment](../../project/experiments/experiment-template.md)

O template de proposta comercial não integra o framework canônico e é mantido fora deste repositório.

## Anexos históricos incorporados

A Policy v1 listava quatro anexos que permanecem cobertos pelos artefatos atuais:

- **Annex A — Self-Assessment:** objetivo/use cases, dados, permissions, HITL, interconexões, usuários, KPIs, riscos, controles, owners e sunset;
- **Annex B — Publication Checklist:** owners, HITL, logs, cap/alerts, registro, DPIA quando aplicável e rollback;
- **Annex C — Registry/Catalog:** ID, owners, dados/permissões, risco, cap e demais campos mínimos;
- **Annex D — Sunset Plan:** prevenção de agentes sem owner, duplicados ou sem uso, com redução de risco e custo.

A incorporação preserva a obrigação substantiva, mas os templates correntes e schemas versionados prevalecem sobre o formato histórico.

## Regras de uso

1. Adapte idioma, roles e thresholds ao contexto.
2. Não remova rationale, owner, evidence ou expiry para “simplificar”.
3. Marque `missing`, `not-applicable`, `passed` e `failed` de forma distinta.
4. Substitua secrets e dados sensíveis por `[REDACTED]`.
5. Versione decisões e mantenha o artefato anterior.
6. Vincule o template ao registry/blueprint e ao evidence package.
7. Use os [schemas](../schemas/README.md) quando disponível.

Templates são aceleradores; não constituem aprovação automática nem prova de eficácia.
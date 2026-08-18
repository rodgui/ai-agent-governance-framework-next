---
title: Roadmap de hardening e release readiness
status: maintained
last_reviewed: 2026-08-18
review_cycle: major-change
owners: [framework-maintainers]
---

# Roadmap de hardening e release readiness

Este roadmap registra somente trabalho realmente planejado para o framework `1.1.0`. Ele não é um calendário de compliance, não cria gates, não altera a release e não promete uma data de publicação.

## Trabalho em execução e decisões pendentes

| Frente | Status | Owner | Critério de saída |
|---|---|---|---|
| Semantic e editorial hardening T01–T14 | Implementado na branch dedicada; aguardando regressão integral | framework-maintainers | validator, testes, Markdownlint, build estrito, diff check e revisão do diff temático sem alteração de contratos fora do escopo |
| Sign-off das ADRs 0013, 0014 e 0015 | `promotion-ready-after-signoff`; ADRs continuam `draft` | Design Authority, Governance Owner, Security/IAM, Data/Privacy e Run Authority | walkthrough formal, divergências, conditions, residual uncertainty e decisão registrada |
| Substitution/replay autorizado | `BLOCKED_BY_AUTHORIZED_EVIDENCE` | Platform/Run Authority + Security/IAM | state, identity, policy, export, side-effect control, recovery, correlation, lineage, deny preservation, expiry replay denial e control equivalence |
| Observabilidade AI-native autorizada | `BLOCKED_BY_AUTHORIZED_EVIDENCE` | Platform/Observability, Data/Privacy, Security e Run Authority | privacy, retention, deletion across stores, export, cardinality, cost, redaction, evidence hold e recovery |
| Validação em estate real | Planejada; nenhum resultado operacional alegado | Governance Owner + organização autorizada | portfolio delimitado com T1, T2, T3, multi-agent, incident/containment drill, attestation e material change ou sunset, com métricas e feedback loop |
| Casos de referência T4 e multi-agent T3/T4 | Planejamento preservado; não criar nova fixture sem necessidade demonstrada | framework-maintainers | caso fictício aprovado no escopo, com tier/admissibility distintos e evidência dos cenários exigidos; exemplos continuam integration tests, não production evidence |
| Dependency security | `BLOCKED_BY_AUTHORIZED_EVIDENCE` para detalhes Dependabot | repository maintainers | export autorizado de todos os alerts, triagem de relevância, dependency path, fixed version e remediation |
| Decisão de release | Não iniciada | Governance Owner + Design Authority | escolha explícita entre manter baseline, `1.1.x` ou `1.2.0`, após evidence e sign-off |

## Regras de atualização

Uma linha só muda de status quando o critério de saída tem evidência recuperável e owner identificado. Evidência fictícia pode demonstrar coerência de contrato; não pode mudar `BLOCKED_BY_AUTHORIZED_EVIDENCE` para `operationally-validated`.

Novos controls, schemas, risk tiers, MPB, Registry fields, taxonomias Gartner ou ranking de fornecedores não entram no roadmap sem finding demonstrado, owner, applicability, evidence e decisão explícita.

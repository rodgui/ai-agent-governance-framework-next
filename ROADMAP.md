---
title: Roadmap de hardening e release readiness
status: maintained
last_reviewed: 2026-08-18
review_cycle: major-change
owners: [framework-maintainers]
---

# Roadmap de hardening e release readiness

Este roadmap registra somente trabalho realmente planejado para o framework `1.1.0`. Ele não é um calendário de compliance, não cria gates, não altera a release e não promete uma data de publicação.

## Estado por frente

| Frente | Implementação/documentação | Regressão local | Regressão remota | Estado e próxima evidência | Owner |
|---|---|---|---|---|---|
| Semantic e editorial hardening T01–T14 | `DONE` | `PASS` no validator, testes, Markdownlint incremental, build e diff check | `FAILURE` histórico no PR #5/main por `uv.lock`; closeout `SUCCESS` no PR #6 em `0eb2d1e`; `SUCCESS` mais recente no PR #7 em `8614994`, run `32175015315`, seguido de `SUCCESS` no push de `main` em `d72e756`, run `32175176730` | T20–T23 corrigidos; manter a distinção entre regressão remota observada e assurance absoluta | framework-maintainers |
| Aceitação das ADRs 0013, 0014 e 0015 como guidance | `accepted` com conditions no framework; decision record `0004` registrado | validator, testes determinísticos, synthetic case e readiness assessment disponíveis | não aplicável | guidance aceita; `missing-authorized-evidence` permanece para implementation, operational validation, effectiveness e produção de consumidores | framework-maintainers; authorities do consumidor quando aplicável |
| Substitution/replay autorizado | Plano e evidência determinística preparados | testes de desenho/teste determinístico disponíveis | não aplicável | `BLOCKED_BY_AUTHORIZED_EVIDENCE` até state, identity, policy, export, side-effect control, recovery, correlation, lineage, deny preservation, expiry replay denial e control equivalence autorizados | Platform/Run Authority + Security/IAM |
| Observabilidade AI-native autorizada | Profile, template e operational plan preparados | testes de desenho/teste determinístico disponíveis | não aplicável | `BLOCKED_BY_AUTHORIZED_EVIDENCE` até privacy, retention, deletion across stores, export, cardinality, cost, redaction, evidence hold e recovery autorizados | Platform/Observability, Data/Privacy, Security e Run Authority |
| T17 planning artifact | `DONE`; execution package existe | estrutura e critérios revisados localmente | não aplicável | Execução de estate permanece `PLANNED` / `BLOCKED_BY_AUTHORIZED_EVIDENCE`; nenhum resultado operacional alegado | framework-maintainers |
| Estate validation execution | Não executada | nenhum resultado operacional alegado | não executada | `PLANNED` / `BLOCKED_BY_AUTHORIZED_EVIDENCE`; requer portfolio delimitado, organização autorizada, drills, métricas e feedback loop | Governance Owner + organização autorizada |
| Casos de referência T4 e multi-agent T3/T4 | Fixtures e planos preservados | exemplos continuam fictícios e testáveis | não aplicável | Não criar nova fixture sem finding demonstrado; T4 fictício não exige ambiente autorizado | framework-maintainers |
| Dependency security | Configuração Dependabot e assessments versionados; uv.lock removido como dependência documental em T21 | manifests e gates locais disponíveis | alert inventory `BLOCKED_BY_AUTHORIZED_EVIDENCE`; REST T26 retornou 403 e GraphQL vazio não foi interpretado como ausência | export autorizado dos alerts, triagem de relevância, dependency path, fixed version e remediation mínima | repository maintainers |
| Quality gates e repository governance | `DONE` para T23/T27; workflow canônico e protection de `main` configurados | `PASS` em clean checkout do closeout | `SUCCESS` observado no PR #6/run `32165812171`; `SUCCESS` mais recente no PR #7/head `8614994`, run `32175015315`, e no push de `main`/`d72e756`, run `32175176730`; baseline histórico permanece `REMOTE_CI_FAILURE` | required status context técnico: `Canonical repository quality gate`; manter `NO GREEN CI → NO MERGE` e reobservar após mudanças de workflow/settings | repository maintainers |
| Decisão de release | Não iniciada | nenhum claim de release | nenhum claim de release | recomendar `KEEP 1.1.0` até evidence e sign-off; decisão continua humana | Governance Owner + Design Authority |

## Regras de atualização

Uma linha só muda de status quando o critério de saída tem evidência recuperável e owner identificado. A revisão simulada pode aceitar guidance no escopo do framework; evidência fictícia não pode mudar `BLOCKED_BY_AUTHORIZED_EVIDENCE` para `operationally-validated` em uma implementação consumidora.

Novos controls, schemas, risk tiers, MPB, Registry fields, taxonomias Gartner ou ranking de fornecedores não entram no roadmap sem finding demonstrado, owner, applicability, evidence e decisão explícita.

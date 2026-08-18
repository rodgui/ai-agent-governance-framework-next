---
title: Decision record — aceitação condicional das ADRs 0013–0015 como guidance do framework
status: accepted
owner: framework-maintainers
last_reviewed: 2026-08-18
review_cycle: major-change
supersedes: null
related:
  - ../../docs/architecture/decisions/0013-multi-agent-delegation-contract.md
  - ../../docs/architecture/decisions/0014-ai-native-observability-profile.md
  - ../../docs/architecture/decisions/0015-multi-control-plane-arbitration.md
  - ../../toolkit/assessments/adr-promotion-readiness-0013-0014-0015.md
  - ../../toolkit/assessments/adr-human-signoff-package-0013-0014-0015.md
  - ../../toolkit/examples/cases/adr-promotion-synthetic-validation/README.md
  - ../../toolkit/assessments/authorized-operational-validation-plan.md
---

# Decision record — aceitação condicional das ADRs 0013–0015 como guidance do framework

## 1. Decision status e escopo

**Decision status:** `accepted` com conditions.
**Decision mode:** `SIMULATED_OWNER_AUTHORIZED_REVIEW`.
**Decision scope:** camada canônica de guidance, patterns e templates do framework vendor-neutral.
**Operational validation:** `missing`; não é alterada por este record.
**Production approval:** não concedida.

Este record registra a decisão do maintainer sobre a coerência e aplicabilidade arquitetural das ADRs 0013, 0014 e 0015 no próprio framework. A decisão não representa sign-off de uma organização consumidora, não nomeia authorities reais e não converte aliases sintéticos em pessoas ou approvals.

## 2. Pergunta de decisão

As ADRs 0013–0015 estão suficientemente definidas, coerentes e demonstradas para serem aceitas como guidance arquitetural canônico do framework, sem exigir alteração prematura de schema, controls, risk tiers, MPB, Registry, vendor choice ou nova simulação?

## 3. Evidence base

| Evidence | Escopo demonstrado | Limite |
|---|---|---|
| ADRs, patterns, templates e examples | Contratos, rationale, conditions, owners, validation criteria e limites documentados | Documentação não prova implementação ou eficácia |
| Deterministic tests | Integridade dos critérios de walkthrough e semantic hardening em fixtures reproduzíveis | Não prova runtime ou estate real |
| Synthetic validation case | Delegation, observability e cross-plane arbitration end-to-end, com negative scenarios, lineage, recovery e substitution/exit | Não prova privacy compliance, enforcement real, longitudinal quality ou production readiness |
| T29–T41 evidence crosswalk | Separação entre documentary, deterministic, synthetic, authorized, operational e human sign-off evidence | Crosswalk não substitui evidence package do consumidor |

## 4. Findings da revisão simulada

### ADR-0013 — Contrato de delegação multiagente

Os critérios publicados são cobertos no escopo sintético: topology record; nodes e delegation edges; lineage; delegated subject; child authority attenuation; privilege escalation denial; enforcement externo de state-changing; expiry/revocation; retry/replay denial; failure propagation; correlation/evidence preservation; containment; e supervisor sem authority absoluta. Não foi demonstrada necessidade de alterar o blueprint schema ou criar control.

**Condition:** uma implementação consumidora deve exercitar os cenários de delegação normal, privilege escalation e falha state-changing com identity, policy/tool gateway, recovery e evidence próprios. Publish/approve permanece human-gated.

### ADR-0014 — Profile opcional de observabilidade AI-native

Os critérios publicados são cobertos no escopo sintético: task reconstruction; correlation; provenance; delegation/model/retrieval/policy/tool chain; deny e containment atribuíveis; redaction/minimization; memory/state references; human intervention; cost/value separation; export sem dashboard proprietário; incident drill; e neutralidade de schema/vendor. O negative test de correlation missing foi preservado como falha detectável antes da exportação corrigida.

**Condition:** uma implementação consumidora deve executar privacy review, retention/deletion decision, export test, cardinality/cost review, access review, threat/privacy findings e observação longitudinal. O profile permanece opcional e não autoriza captura indiscriminada de prompts, payloads, secrets ou dados pessoais.

### ADR-0015 — Arbitragem entre múltiplos control planes

Os critérios publicados são cobertos no escopo sintético: interaction matrix; authority/source of truth/enforcement/fallback; conflito determinístico; precedência de deny; ausência de bypass; divergência como finding; fail-safe; quarantine/recovery; correlation/evidence; substitution como material change; assurance independente; e vendor neutrality. Não foi identificada dependência de ranking de fornecedores, nova taxonomia de control planes ou schema migration.

**Condition:** uma implementação consumidora deve demonstrar enforcement, identity/policy failure, fallback, recovery, degraded mode, evidence export e substitution em sua própria arquitetura. Nenhuma equivalência de effectiveness, performance ou security entre implementações é inferida.

## 5. Decision

As ADRs 0013–0015 são **aceitas com conditions como guidance arquitetural canônico do framework**. A aceitação responde que os contratos são expressivos, coerentes, vendor-neutral e suficientemente demonstrados para orientar futuras implementações.

Esta decisão não afirma que qualquer implementação consumidora está validada. Para cada consumidor, a organização deve produzir seus próprios owners, authorities, data classes, identities, policy mappings, enforcement records, recovery evidence, privacy decisions, operational evidence e release decision.

## 6. Estados resultantes

| Artefato | Decision status | Evidence maturity | Operational status |
|---|---|---|---|
| ADR-0013 | `accepted` com conditions | `demonstrated-deterministic` + `demonstrated-synthetic` | `missing-authorized-evidence` |
| ADR-0014 | `accepted` com conditions | `demonstrated-deterministic` + `demonstrated-synthetic` | `missing-authorized-evidence` |
| ADR-0015 | `accepted` com conditions | `demonstrated-deterministic` + `demonstrated-synthetic` | `missing-authorized-evidence` |

`accepted` neste record significa aceitação arquitetural do framework. Não significa `effective`, `operationally-validated`, `approved for production`, compliance ou assurance externa.

## 7. Review triggers, expiry e reversibility

Revisar esta decisão quando houver mudança material em qualquer ADR, alteração de schema/control dependency, divergência relevante de implementação, evidence operacional que contradiga as conditions, ou mudança na fronteira vendor-neutral do framework.

A decisão não possui expiry temporal automático. Ela expira por material change ou supersession, não autoriza continuidade de uma implementação sem revalidação e pode ser superseded por novo decision record. A decisão é reversível no nível documental; efeitos runtime de consumidores exigem rollback e recovery próprios.

## 8. Provenance e limites

Este record é uma decisão simulada e autorizada no escopo do maintainer do framework, solicitada pelo owner do repositório para superar a ausência de organization-specific evidence. Não há nomes de reviewers ou assinaturas inventados. Os aliases `DA-SIM`, `GO-SIM`, `SEC-IAM-SIM`, `DATA-PRIV-SIM`, `RUN-SIM` e `PLAT-OBS-SIM` continuam exclusivamente sintéticos.

O [synthetic validation case](../../toolkit/examples/cases/adr-promotion-synthetic-validation/README.md), o [ADR promotion readiness assessment](../../toolkit/assessments/adr-promotion-readiness-0013-0014-0015.md), o [human sign-off package](../../toolkit/assessments/adr-human-signoff-package-0013-0014-0015.md) e o [authorized operational validation plan](../../toolkit/assessments/authorized-operational-validation-plan.md) são as referências rastreáveis para os critérios, evidence e limites desta decisão.

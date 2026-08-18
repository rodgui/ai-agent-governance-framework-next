---
title: Plano de validação operacional autorizada — substitution, observability e estate
type: assessment
status: under-review
maturity: illustrative
last_reviewed: 2026-08-18
review_cycle: major-change
owners: [framework-maintainers, governance, platform, run-authority]
related:
  - ../examples/orchestrator-substitution-replay.example.md
  - ../examples/ai-native-observability-operational-drill.example.md
  - ../templates/orchestrator-decision-exit-record.md
  - ../patterns/ai-native-observability-profile.md
  - ../../docs/framework/08-implementation-and-adoption.md
  - ../../docs/framework/09-operations-incidents-and-continuity.md
  - ./adr-promotion-readiness-0013-0014-0015.md
---

# Plano de validação operacional autorizada

> **Status atual:** `BLOCKED_BY_AUTHORIZED_EVIDENCE`. Este documento é um plano executável e um contrato de preparação; não é evidence de produção, não é approval e não altera o status das ADRs.

## 1. Objetivo e limites

O plano transforma os drills fictícios existentes em uma execução autorizada quando houver organização, portfolio, authority, environment e data de corte aprovados. Ele cobre três frentes relacionadas:

1. substitution/replay do orchestrator, conforme o [drill fictício](../examples/orchestrator-substitution-replay.example.md);
2. observabilidade AI-native, conforme o [operational drill fictício](../examples/ai-native-observability-operational-drill.example.md);
3. validação delimitada de estate para exercitar gates, controls, evidence, operação e melhoria.

Não inclui upgrade de fornecedor, publicação em produção, alteração de schema, promoção automática de ADR, criação de control, mudança de tier ou release.

## 2. Prerequisites e authorities

A execução só pode começar quando todos os prerequisites forem registrados no evidence package:

| Prerequisite | Evidência de entrada | Authority/owner |
|---|---|---|
| Organização e portfolio autorizados | scope, sponsor, business owner e lista de agentes | Sponsor + Governance Owner |
| Ambiente isolado ou janela controlada | environment boundary, data classification, change ticket e rollback owner | Run Authority + Technical Owner |
| Agentes representativos | ao menos um T1, T2, T3 e um multi-agent, com IDs e owners | Governance Owner |
| Identity e secrets | workload identity, delegated subject, credenciais temporárias e rotação | Security/IAM |
| Policy e enforcement | policy mappings, source of truth, deny path, approval e kill switch | Governance + Security/IAM |
| Privacy e dados | classes de dados, minimization, redaction, retention, legal hold e deletion authority | Data/Privacy |
| Evidence handling | evidence cutoff, storage, access, hash, export format e chain of custody | Assurance Owner |
| Comunicação e reversão | incident channel, on-call, recovery plan, cleanup window e abort authority | Run Authority |

A autoridade que executa o teste não pode aprovar sozinha o resultado quando houver necessidade de independence ou residual-risk acceptance.

## 3. T15 — Substitution/replay validation

### 3.1 Test plan

Executar o mesmo caso com duas implementações de orchestrator, preservando o bundle de governança: registry, blueprint, policy mappings, event/evidence lineage, correlation, identity bindings, state references e decision/exit record.

A sequência mínima é:

1. exportar o bundle e registrar hash, version, owner e evidence cutoff;
2. executar um caminho permitido com correlação completa e side-effect control;
3. executar um policy deny e comprovar que a alternativa não consegue reabrir ou ampliar a ação;
4. expirar ou revogar uma delegation edge e tentar retry/replay;
5. preservar state, credentials e evidence conforme o plano de cleanup;
6. substituir o orchestrator, reconciliar state/policy/identity e repetir o caminho permitido;
7. comprovar equivalência de control, deny preservation, correlation e lineage;
8. exercitar falha, recovery, rollback e reactivation;
9. exportar evidence final e fechar ou abrir findings.

### 3.2 Expected evidence

| Invariante | Evidence esperada |
|---|---|
| Registry e blueprint preservados | export versionado, hashes e reconciliação |
| Identity preservada | mapping de workload/delegated identity, rotação e deny após revocation |
| Policy preservada | policy decision refs, enforcement logs e replay denial |
| Side effect control | allow/deny matrix, tool gateway evidence e ausência de efeito indevido |
| Correlation/lineage | task, delegation, event, state e evidence refs reconstruíveis |
| Portability | bundle importado pela alternativa sem perda material de governance |
| Recovery | rollback, quarantine, reactivation condition e resultado do drill |

### 3.3 Acceptance criteria e cleanup

O teste passa somente quando os invariantes são equivalentes para o escopo testado, os denies permanecem denies, retry pós-expiry não reabre capacidade, nenhum side effect não autorizado ocorre e a evidence exportada é recuperável sem depender do dashboard proprietário.

Após o teste, revogar credenciais temporárias, limpar dados de teste, reconciliar registry e state, arquivar evidence com retenção aprovada, registrar findings e remover bindings temporários. Se houver falha material, manter o escopo contido e abrir `hold` ou quarantine; não declarar substituição concluída.

## 4. T16 — AI-native observability validation

### 4.1 Test plan

Para uma cadeia material, exercitar task, delegation, model call, retrieval, policy decision, tool request/result, human intervention, memory/state, containment, cost/value e outcome. Mapear o modelo em 8 camadas para o AI-Native Observability Profile e para o audit-event envelope mínimo.

A execução deve incluir privacy review, redaction, retention, evidence hold, export, cardinality, cost, recovery e deletion across stores: primary state, cache, index, backup e evidence store, respeitando holds e authority. A deletion não pode ser declarada completa apenas porque a interface deixou de mostrar o registro.

### 4.2 Expected evidence e acceptance criteria

| Área | Evidence esperada | Critério de aceitação |
|---|---|---|
| Privacy/redaction | privacy decision, sample redacted trace e access review | payload proibido não aparece além do escopo autorizado |
| Retention/hold | retention matrix, hold record e expiry decision | retenção e hold são reconciliáveis |
| Deletion | deletion record por store, verification e access denial | memory/state deixa de ser acessível conforme policy |
| Export | export package, format, hash e restore/replay check | cadeia é reconstruível sem backend proprietário |
| Cardinality/cost | volume report, dimensions, budget e action thresholds | custo e cardinalidade têm owner/action e não degradam silenciosamente |
| Recovery | incident/containment/recovery evidence | reactivation exige cause, remediation e regression |

O profile passa somente quando os sinais necessários são correlacionáveis, a privacy boundary é verificável, deletion e evidence hold não entram em conflito silencioso, export é recuperável e qualquer gap é registrado como `missing-authorized-evidence` ou `hold`.

### 4.3 Cleanup

Encerrar subjects e credenciais de teste, remover state e derivados conforme a deletion decision, preservar apenas evidence sob hold aprovado, validar access denial pós-deletion, fechar ou abrir findings e registrar a data da próxima revisão.

## 5. T17 — Validação delimitada de estate

A organização autorizada deve selecionar um portfolio com:

- um caso T1;
- um caso T2;
- um caso T3;
- um fluxo multi-agent;
- um incident/containment drill;
- uma attestation;
- uma material change ou sunset.

Medir, no mínimo, governance lead time, handoff latency, reviewer disagreement, false positives, bypass attempts, missing evidence, owner ambiguity, exception volume, controls de baixo valor, controls bloqueantes, runtime incidents, time-to-detect, time-to-decide, time-to-contain, time-to-recover, paved-road usability e governance operating cost.

Cada medida precisa de owner, population, baseline, evidence source, method, confidence, action, acceptance criterion e feedback loop. O resultado deve alimentar o processo versionado de melhoria do framework/control catalog; não altera controls automaticamente.

## 6. Decisão e status

Até que os prerequisites sejam satisfeitos e uma authority aceite o escopo, T15 e T16 permanecem `BLOCKED_BY_AUTHORIZED_EVIDENCE`, e T17 permanece `PLANNED`. Os drills fictícios existentes permanecem úteis como integration tests, mas não substituem esta execução.

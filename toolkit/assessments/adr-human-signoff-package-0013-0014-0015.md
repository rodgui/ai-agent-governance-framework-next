---
title: Human sign-off package — ADRs 0013, 0014 e 0015
type: assessment
status: prepared
maturity: illustrative
last_reviewed: 2026-08-18
review_cycle: major-change
evidence_cutoff: 2026-08-18
assessor: framework-maintainers
independence: pending-authority-review
related:
  - adr-promotion-readiness-0013-0014-0015.md
  - ../examples/cases/adr-promotion-synthetic-validation/README.md
  - authorized-operational-validation-plan.md
  - ../../docs/architecture/decisions/0013-multi-agent-delegation-contract.md
  - ../../docs/architecture/decisions/0014-ai-native-observability-profile.md
  - ../../docs/architecture/decisions/0015-multi-control-plane-arbitration.md
  - ../../project/decisions/0004-framework-guidance-acceptance-adr-0013-0015.md
---

# Human sign-off package — ADRs 0013, 0014 e 0015

> Este pacote preserva os campos para uma decisão de consumidor. A decisão do framework foi registrada separadamente como `SIMULATED_OWNER_AUTHORIZED_REVIEW`; este pacote não contém nomes, assinaturas ou aprovações inventadas. A simulação disponível é `SIMULATED_SYNTHETIC_EVIDENCE`; não é evidence operacional autorizada, compliance evidence, real authority sign-off de consumidor ou production readiness.

## 1. Objetivo e decisão solicitada

O objetivo é permitir que as authorities competentes revisem as ADRs 0013, 0014 e 0015 com a mesma base de evidence, limitações e condições. A decisão solicitada é independente por ADR e deve ser registrada em um decision record ou no próprio documento, preservando rationale, autoridade, data, conditions, expiry, residual risk e data de revisão.

As opções disponíveis são:

| Opção | Uso |
|---|---|
| `ACCEPT` | A authority aceita a decisão arquitetural no escopo declarado. Não significa operational validation ou autorização automática de produção. |
| `ACCEPT_WITH_CONDITIONS` | Usar somente se a convenção de decisão do consumidor aceitar essa formulação. Se não for um status canônico, registrar `accepted` e modelar as conditions separadamente, com owner, expiry e critério de saída. |
| `KEEP_DRAFT` | Manter a ADR em rascunho enquanto faltar decisão humana, evidence necessária ou resolução de objeção material. |
| `REJECT` | Rejeitar a decisão proposta com rationale, impacto e alternativa ou condição de encerramento. |
| `SUPERSEDE` | Substituir uma decisão anterior por outra decisão versionada, preservando provenance e referência ao documento superseded. |

**Decisão simulada atual para as três ADRs:** `ACCEPT_WITH_CONDITIONS`; status canônico `accepted` no escopo de guidance do framework. A estrutura está `accepted` para uso como guidance, enquanto implementation/operational evidence do consumidor permanece `missing`.

## 2. Evidence comum e limites

| Tipo | O que demonstra | O que não demonstra |
|---|---|---|
| `demonstrated-deterministic` | Coerência de exemplos, contratos e testes determinísticos locais. | Eficácia de control, comportamento longitudinal ou enforcement de uma organização. |
| `demonstrated-synthetic` | Integração end-to-end, applicability do contrato, cenários negativos, evidence lineage, recovery e substitution/exit no case fictício. | Privacy compliance real, control effectiveness, accountability organizacional, production readiness ou autoridade real. |
| `missing-authorized-evidence` | Gap que exige ambiente, dados, authority ou execução autorizada. | Não é um pass, nem uma aprovação implícita. |
| `operationally-validated` | Comportamento observado em implementação/execução autorizada no escopo declarado. | Não pode ser inferido do synthetic case ou de testes locais. |

O case sintético é comum às três ADRs, mas seu peso é limitado. Ele demonstra que o framework consegue conduzir uma decisão integrada; não demonstra que uma implementação de consumidor funciona.

## 3. ADR-0013 — Contrato de delegação multiagente

| Campo | Conteúdo para decisão humana |
|---|---|
| **Decisão solicitada** | Escolher `ACCEPT`, `ACCEPT_WITH_CONDITIONS`, `KEEP_DRAFT`, `REJECT` ou `SUPERSEDE` para o contrato de delegação no escopo declarado. |
| **Architecture rationale** | Tornar delegation explícita, atribuível, limitada, expirável e revogável; preservar authority attenuation, identity, delegated subject, lineage, state-changing enforcement e failure propagation sem transformar supervisor em authority universal. |
| **Synthetic evidence disponível** | Case transversal com delegação normal, privilege escalation negada, child envelope menor que parent, expiry/revocation, replay denial, failure containment, correlation e evidence lineage; complementado pelo exemplo supervisor/worker e pelo teste determinístico de walkthrough. Classificação: `demonstrated-synthetic` + `demonstrated-deterministic`. |
| **Authorized evidence faltante** | Walkthrough com caso organizacional autorizado; verificação dos limites de depth, fan-out, budget, expiry, revocation, delegated subject, data classes e state-changing enforcement na implementação do consumidor; recovery e compensating controls autorizados. |
| **Known limitations** | Não há estate real, authority real, identity provider real, policy runtime real ou evidência longitudinal. Fixtures, aliases e outcomes são fictícios. |
| **Objections** | Nenhuma objeção foi registrada neste pacote. Isso significa `not-recorded`, não `no-objection`. |
| **Conditions** | Se aceita, limitar ao escopo declarado, exigir edge contract versionado, authority attenuation, deny preservation, expiry/revocation, correlation e recovery evidence; definir owner, expiry e review date. |
| **Residual uncertainty** | A implementação pode interpretar delegated subject, revocation, retry/replay ou blast radius de forma incompatível com o contrato. |
| **Reversibility** | Alta no nível de guidance/ADR; a decisão pode ser superseded. Baixa para efeitos runtime já implantados sem rollback e recovery testados. |
| **Operational dependency** | Identity/IAM, policy enforcement, tool gateway, evidence store, runtime containment, owner de operação e mecanismo de revocation. |
| **Recommended disposition** | `ACCEPT_WITH_CONDITIONS` no escopo de guidance do framework; `operational validation` permanece `missing` para o consumidor. |

**Reviewers/roles requeridos:** Design Authority, Governance Owner, Security/IAM Authority, Data/Privacy Authority quando houver data classes relevantes e Run Authority. Nenhuma pessoa foi nomeada neste pacote.

## 4. ADR-0014 — Profile opcional de observabilidade AI-native

| Campo | Conteúdo para decisão humana |
|---|---|
| **Decisão solicitada** | Escolher uma disposição para o profile sem transformá-lo em obrigação de vendor, backend, protocol, schema ou dashboard específico. |
| **Architecture rationale** | Tornar task, delegation, model, retrieval, tool, policy, human intervention, memory/state, containment, outcome, value e cost observáveis e correlacionáveis, preservando minimization, redaction, retention, deletion e export. |
| **Synthetic evidence disponível** | Case integrado com correlation/provenance, redaction, retention/deletion, export, cardinality/cost e alert-to-action; complementado por examples e operational drill fictício. Classificação: `demonstrated-synthetic` + `demonstrated-deterministic`. |
| **Authorized evidence faltante** | Privacy review real; retention/deletion decision; export sem dashboard proprietário; cardinality/cost report em implementação; evidence hold; alert-to-action; recovery/reactivation; threat/privacy findings; validação de acesso, minimização e retenção no consumidor. |
| **Known limitations** | Valores de cardinalidade/custo são ilustrativos. Não existe confirmação de privacy compliance, deletion across stores, comportamento longitudinal ou eficácia de controles. |
| **Objections** | Nenhuma objeção foi registrada neste pacote. O campo permanece aberto para challenge de Data/Privacy, Security, Observability, Platform e Run. |
| **Conditions** | Se aceita, manter o profile opcional; exigir data classification, redaction, retention, deletion, access, export, cardinality/cost envelope e evidence hold definidos antes de uso operacional. |
| **Residual uncertainty** | O profile pode aumentar cardinality, custo ou exposição; adapters podem perder provenance; deletion e export podem divergir entre stores. |
| **Reversibility** | Alta no nível semântico enquanto o audit-event schema permanece inalterado; instrumentação já implantada exige rollback, retention e deletion plan. |
| **Operational dependency** | Observability platform, audit-event envelope, storage/index/cache/backup, privacy owner, access control, incident response e runbook de containment. |
| **Recommended disposition** | `ACCEPT_WITH_CONDITIONS` no escopo de guidance do framework; privacy/export/retention evidence do consumidor permanece `missing`. |

**Reviewers/roles requeridos:** Data/Privacy Authority, Observability Owner, Security, Run Authority e Platform Owner. Nenhuma pessoa foi nomeada neste pacote.

## 5. ADR-0015 — Arbitragem entre múltiplos control planes

| Campo | Conteúdo para decisão humana |
|---|---|
| **Decisão solicitada** | Escolher uma disposição para a arbitragem cross-plane no escopo declarado, sem criar `primary_orchestrator` ou ranking de vendors. |
| **Architecture rationale** | Declarar authority, source of truth, enforcement point, correlation, fallback, conflict path e evidence por capability; fazer deny obrigatório prevalecer; tratar divergência como finding; aplicar fail-safe; reconhecer substitution/exit como material change. |
| **Synthetic evidence disponível** | Case integrado com authority matrix, conflict, precedence, deny, fail-safe, recovery, quarantine/fallback e substitution/exit; complementado por examples e substitution/replay drill fictício. Classificação: `demonstrated-synthetic` + `demonstrated-deterministic`. |
| **Authorized evidence faltante** | Walkthrough organizacional; matrix cross-plane real; conflict path; identity/policy failure; fallback/recovery; enforcement observation; residual risk decision; substitution test em arquitetura de consumidor. |
| **Known limitations** | Nenhum control plane real foi exercitado. O case não prova que duas plataformas reais preservam precedence, correlation, deny ou evidence em degraded mode. |
| **Objections** | Nenhuma objeção foi registrada neste pacote. A ausência de objeção não equivale a aprovação. |
| **Conditions** | Se aceita, exigir authority matrix, source of truth, enforcement, conflict path, fail-safe, fallback, recovery, correlation e evidenceRef para cada fluxo material; substitution material change exige reavaliação. |
| **Residual uncertainty** | Componentes podem declarar posture incompatível, perder correlation, aceitar fallback permissivo ou fragmentar evidence durante indisponibilidade. |
| **Reversibility** | A decisão arquitetural é supersedable; alterações de enforcement, trust boundary, identity, source of truth ou evidence podem ser materialmente difíceis de reverter. |
| **Operational dependency** | Identity, policy gateway, tool broker, registry, orchestration/runtime, assurance plane, evidence store, recovery e owners por capability. |
| **Recommended disposition** | `ACCEPT_WITH_CONDITIONS` no escopo de guidance do framework; enforcement/fallback/recovery evidence do consumidor permanece `missing`. |

**Reviewers/roles requeridos:** Design Authority, Governance Owner, Security/IAM Authority, Data/Privacy Authority e Run Authority. Nenhuma pessoa foi nomeada neste pacote.

## 6. Registro de decisão a completar

Para uma organização consumidora, a authority deve preencher um registro por ADR com os campos abaixo. O decision record simulado do framework não substitui esse registro.

| Campo | Valor a preencher |
|---|---|
| ADR | 0013, 0014 ou 0015 |
| Decision requested | `ACCEPT`, `ACCEPT_WITH_CONDITIONS`, `KEEP_DRAFT`, `REJECT` ou `SUPERSEDE` |
| Decision status | Valor canônico após decisão |
| Decision authority role | Papel da authority; nome somente se autorizado |
| Date | `YYYY-MM-DD` |
| Architecture rationale | Rationale final após review |
| Objections | Objeções, resolução ou `not-recorded` |
| Conditions | Owner, expiry, acceptance criteria e review date |
| Residual risk | Risco residual aceito, transferido ou não aceito |
| Evidence references | Links para evidence aplicável e sua classificação |
| Operational validation | `missing`, `planned`, `operationally-validated` ou `not-applicable`, com rationale |
| Reversibility/rollback | Estratégia e dependências |
| Next review | Data ou evento de revisão |

## 7. Limites de aprovação

A aceitação arquitetural não é production approval. A decisão `accepted` do framework mantém maturity/evidence independente e não converte `demonstrated-synthetic` em `operationally-validated`. Para um consumidor, sem authority e decision record próprios, a disposição continua `KEEP_DRAFT`.

O pacote não cria pessoas, signatures, controls, schemas, risk tiers, registry fields, vendors, architecture patterns ou claims de compliance. O próximo salto de maturidade de um consumidor requer decisão humana própria e, depois, execução autorizada real; não requer outra simulação do framework.

## 8. Referências

- [ADR promotion readiness — 0013, 0014 e 0015](adr-promotion-readiness-0013-0014-0015.md)
- [Synthetic ADR promotion validation case](../examples/cases/adr-promotion-synthetic-validation/README.md)
- [ADR-0013](../../docs/architecture/decisions/0013-multi-agent-delegation-contract.md)
- [ADR-0014](../../docs/architecture/decisions/0014-ai-native-observability-profile.md)
- [ADR-0015](../../docs/architecture/decisions/0015-multi-control-plane-arbitration.md)
- [Plano de validação operacional autorizada](authorized-operational-validation-plan.md)
- [Capítulo 00 — Controle do documento](../../docs/framework/00-document-control.md)
- [Decision record — aceitação condicional das ADRs 0013–0015](../../project/decisions/0004-framework-guidance-acceptance-adr-0013-0015.md)

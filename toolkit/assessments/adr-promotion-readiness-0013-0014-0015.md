---
title: ADR promotion readiness — 0013, 0014 e 0015
type: assessment
status: under-review
maturity: illustrative
last_reviewed: 2026-08-18
review_cycle: major-change
evidence_cutoff: 2026-08-18
assessor: framework-maintainers
independence: pending-authority-review
related:
  - ../../docs/architecture/decisions/0013-multi-agent-delegation-contract.md
  - ../../docs/architecture/decisions/0014-ai-native-observability-profile.md
  - ../../docs/architecture/decisions/0015-multi-control-plane-arbitration.md
  - ../examples/supervisor-worker-delegation.example.md
  - ../examples/multi-control-plane-conflict.example.md
  - ../examples/ai-native-observability.example.md
  - ../examples/ai-native-observability-operational-drill.example.md
  - ../examples/orchestrator-substitution-replay.example.md
  - ../templates/agent-delegation-contract.md
  - ../templates/ai-native-observability-profile.md
  - ../templates/orchestrator-decision-exit-record.md
---

# ADR promotion readiness — 0013, 0014 e 0015

> Este assessment prepara uma decisão humana sobre promoção de ADRs. Não é aprovação, não é evidência de produção, não é assurance de effectiveness e não transforma exemplos fictícios em controls.

## 1. Contexto e problema

As ADRs `0013`, `0014` e `0015` foram implementadas como guidance, patterns, templates e exemplos vendor-neutral. O conteúdo técnico foi exercitado em casos fictícios e em drills determinísticos, mas cada ADR exige walkthrough por authorities antes de sair de `draft`.

A rodada T01–T13 adicionou semantic e editorial hardening sem alterar schemas, controls, risk tiers, MPB, Registry ou release: `discovery.status` foi alinhado ao enum canônico; as waves de implementação passaram a W0–W6; document status, decision status, maturity e artifact type foram separados; o fluxo G2↔G3 foi explicitado; technology evaluation deixou de ter G3 como destino rígido; e o crosswalk WHAT/HOW/MINIMUM de observabilidade foi registrado.

A pergunta deste assessment é: **a estrutura técnica está pronta para revisão final e eventual promoção de status, e quais evidências ainda impedem essa decisão?**

## 2. Escopo e exclusões

O escopo inclui o contrato de delegação multiagente, o profile opcional de observabilidade AI-native e a arbitragem entre múltiplos control planes. Não inclui aprovação de fornecedor, implantação de produção, alteração de schema, criação de control, mudança de risk tier, alteração da release `1.1.0` ou validação de claims de eficácia.

## 3. Critérios de disposição

| Disposição | Uso neste assessment |
|---|---|
| `demonstrated-deterministic` | Critério demonstrado em exemplo ou teste local determinístico com fixtures fictícios. |
| `missing-authorized-evidence` | Evidência que exige ambiente autorizado, privacy review, authority ou caso organizacional. |
| `promotion-ready-after-signoff` | Estrutura técnica suficiente para decisão, sem significar que a decisão já foi tomada. |
| `hold` | Não promover enquanto o gap indicado permanecer sem owner e evidence. |

## 4. Resultado executivo

| ADR | Estrutura técnica | Pendência | Disposição recomendada |
|---|---|---|---|
| ADR-0013 — delegação multiagente | Cobre topologia, edges, atenuação, limits, expiry, revocation e failure propagation. | Walkthrough autorizado e caso organizacional autorizado. | `promotion-ready-after-signoff`; manter `draft` até aprovação. |
| ADR-0014 — observabilidade AI-native | Cobre correlation, provenance, privacy, deletion, cardinality, cost, containment e export guidance. | Privacy/export/retention review e validação em implementação autorizada. | `promotion-ready-after-signoff`; manter `draft` até aprovação. |
| ADR-0015 — arbitragem cross-plane | Cobre authority, source of truth, enforcement, precedence, conflict, fail-safe e substitution material change. | Walkthrough formal pelas authorities e caso organizacional. | `promotion-ready-after-signoff`; manter `draft` até aprovação. |

## 5. ADR-0013 — contrato de delegação multiagente

### Evidência revisada

| Critério | Artefato ou teste | Resultado |
|---|---|---|
| Topologia, nodes, roles e versões | `supervisor-worker-delegation.example.md` | `demonstrated-deterministic` |
| Delegação concluída e lineage | Cenário 1 do exemplo | `demonstrated-deterministic` |
| Privilege escalation negada | Cenário 2 do exemplo | `demonstrated-deterministic` |
| Child envelope menor que o parent | Contrato e checklist do exemplo | `demonstrated-deterministic` |
| Depth, fan-out, budget, expiry e revocation | Contrato e checklist do exemplo | `demonstrated-deterministic` |
| Falha state-changing e containment | Cenário 3 do exemplo | `demonstrated-deterministic` |
| Retry/replay pós-expiry ou revocation | Regra da ADR e substitution/replay drill relacionado | `demonstrated-deterministic` |
| Caso organizacional autorizado | Não disponível; os casos publicados são fictícios | `missing-authorized-evidence` |
| Eficácia operacional | Fora do escopo do repositório canônico | `missing-authorized-evidence` |

### Walkthrough requerido

| Reviewer/authority | Pergunta de decisão | Registro necessário |
|---|---|---|
| Design Authority | A topologia e os limites são arquiteturalmente coerentes? | decisão, divergências e rationale |
| Governance Owner | O contrato preserva accountability e decision rights? | owner, conditions e expiry |
| Security/IAM Authority | A autoridade do child é sempre atenuada e revogável? | cenários negativos e compensating controls |
| Data/Privacy Authority | Delegated subject e data classes estão limitados? | privacy constraints e data decision |
| Run Authority | Failure propagation, containment e reactivation são operáveis? | run evidence e recovery decision |

### Critério de promoção

Promover somente após concluir os três cenários exigidos pela ADR, registrar divergências e compensating controls e obter confirmação dos reviewers aplicáveis. Nenhuma extensão obrigatória do `agent-blueprint.schema.json` é justificada por este assessment.

## 6. ADR-0014 — profile opcional de observabilidade AI-native

### Evidência revisada

| Critério | Artefato ou teste | Resultado |
|---|---|---|
| Task e cadeia com correlation | `ai-native-observability.example.md` e profile | `demonstrated-deterministic` |
| Delegation, model/retrieval, policy e tool provenance | Exemplo completo G4 | `demonstrated-deterministic` |
| Policy deny e containment atribuíveis | Exemplo completo e operational drill | `demonstrated-deterministic` |
| Redaction e minimização | `ai-native-observability-operational-drill.example.md` | `demonstrated-deterministic` |
| Deletion em primary/cache/index/backup | Operational drill fictício | `demonstrated-deterministic` |
| Evidence hold separado do state | Operational drill fictício | `demonstrated-deterministic` |
| Cardinalidade e custo | Envelope ilustrativo com owner e action | `demonstrated-deterministic` |
| Export sem dashboard proprietário | Guidance documentada; implementação não exercitada | `missing-authorized-evidence` |
| Privacy review, retention e deletion decision | Ainda não executados por authority real | `missing-authorized-evidence` |
| Evidência longitudinal de qualidade | Ainda inexistente | `missing-authorized-evidence` |

### Walkthrough requerido

| Reviewer/authority | Pergunta de decisão | Registro necessário |
|---|---|---|
| Privacy/Data Authority | O profile minimiza, classifica, redige e retém somente o necessário? | privacy decision |
| Observability Owner | Correlation, signal coverage e cardinality são operáveis? | coverage/cardinality report |
| Security | A instrumentação não cria exposição ou bypass? | threat/privacy findings |
| Run Authority | Alert-to-action, containment, reactivation e deletion são executáveis? | run/deletion evidence |
| Platform Owner | Export, adapters e custo não dependem de backend proprietário? | export/cost evidence |

### Critério de promoção

Promover somente após privacy review, cardinality/cost review, export test e retention/deletion decision em implementação autorizada. O `audit-event.schema.json` permanece inalterado, pois o assessment não demonstra necessidade machine-readable.

## 7. ADR-0015 — arbitragem entre múltiplos control planes

### Evidência revisada

| Critério | Artefato ou teste | Resultado |
|---|---|---|
| Interaction matrix completa | `multi-control-plane-conflict.example.md` | `demonstrated-deterministic` |
| Deny de enforcement obrigatório prevalece | Tool gateway bloqueia escrita crítica | `demonstrated-deterministic` |
| Orchestrator não amplia scope após deny | Exemplo G1 e substitution/replay criteria | `demonstrated-deterministic` |
| Componente indisponível produz fail-safe | Restricted/quarantined no teste de indisponibilidade | `demonstrated-deterministic` |
| Correlation e evidence cross-plane | `correlation_id` e evidence reference | `demonstrated-deterministic` |
| Divergência vira finding | Finding explícito no exemplo | `demonstrated-deterministic` |
| Assurance independente | ADR e pattern G1 | `demonstrated-deterministic` |
| Substituição material reconhecida | Exit record e substitution/replay drill | `demonstrated-deterministic` |
| Caso organizacional e walkthrough formal | Ainda não executados | `missing-authorized-evidence` |

### Walkthrough requerido

| Reviewer/authority | Pergunta de decisão | Registro necessário |
|---|---|---|
| Design Authority | O placement e a composição de authorities estão coerentes? | architecture decision |
| Governance Owner | Há um accountable claro por capability e exceção? | decision rights |
| Security/IAM Authority | Deny, identity failure e privileged actions são fail-safe? | negative tests |
| Data/Privacy Authority | Data classification, privacy e source of truth são respeitados? | data/privacy findings |
| Run Authority | Fallback, quarantine, recovery e reactivation são executáveis? | run evidence |

### Critério de promoção

Promover somente após walkthrough formal com o caso organizacional, matriz cross-plane, conflito determinístico, fail-safe compatível com o tier e registro de divergências. A ADR não cria taxonomia `consolidated/coordinated/federated` nem `primary_orchestrator` universal.

## 8. Testes determinísticos protegidos

O teste `tools/scripts/test_adr_walkthrough_evidence.py` confirma que os exemplos canônicos continuam contendo os critérios essenciais das ADRs G1, G2 e G4, além dos limites do substitution/replay drill. O teste adicional `tools/scripts/test_semantic_hardening.py` protege as correções T02–T10 de discovery status, waves, metadata, gate flow, technology evaluation e observability crosswalk.

Resultado atual:

```text
ADR walkthrough evidence: 4 tests — OK
Semantic hardening: 8 tests — OK
```

Este teste é **verification** da integridade documental. Não é evidence de eficácia, não é aprovação humana e não é evidência de produção.

## 9. Decisão solicitada

**Decisão atual recomendada:** `hold` para promoção automática; `promotion-ready-after-signoff` para os três pacotes técnicos.

**Status das ADRs:** permanecer `draft` até que os walkthroughs e as decisões dos reviewers sejam registrados nos próprios documentos ou em decision records vinculados.

**Owners propostos:**

- Design Authority: conduzir revisão arquitetural;
- Governance Owner: registrar decisão e conditions;
- Security/IAM e Data/Privacy: revisar limites e exposição;
- Run Authority: validar falha, contenção, recovery e reativação;
- Platform/Observability Owner: produzir export, cardinality/cost e deletion evidence.

**Próxima revisão:** após o walkthrough formal, quando um caso organizacional autorizado estiver disponível ou após a execução autorizada dos drills T15/T16.

## 10. Limitações

Os casos e drills do repositório são fictícios e vendor-neutral. Os resultados não provam interoperabilidade universal, eficácia de controls, qualidade longitudinal, conformidade, segurança do modelo, justiça do outcome ou prontidão de produção. Valores de cardinalidade e custo são ilustrativos e não são thresholds universais.

## 11. Referências internas

- [ADR-0013 — Contrato de delegação multiagente](../../docs/architecture/decisions/0013-multi-agent-delegation-contract.md)
- [ADR-0014 — Profile opcional de observabilidade AI-native](../../docs/architecture/decisions/0014-ai-native-observability-profile.md)
- [ADR-0015 — Arbitragem entre múltiplos control planes](../../docs/architecture/decisions/0015-multi-control-plane-arbitration.md)
- [Exemplo G1 — Conflito entre control planes](../examples/multi-control-plane-conflict.example.md)
- [Exemplo G2 — Supervisor/worker](../examples/supervisor-worker-delegation.example.md)
- [Exemplo G4 — Observabilidade AI-native](../examples/ai-native-observability.example.md)
- [Operational drill G4](../examples/ai-native-observability-operational-drill.example.md)
- [Substitution/replay drill](../examples/orchestrator-substitution-replay.example.md)

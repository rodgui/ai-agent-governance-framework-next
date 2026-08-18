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
  - ../examples/cases/adr-promotion-synthetic-validation/README.md
  - ../templates/agent-delegation-contract.md
  - ../templates/ai-native-observability-profile.md
  - ../templates/orchestrator-decision-exit-record.md
  - ../../project/decisions/0004-framework-guidance-acceptance-adr-0013-0015.md
---

# ADR promotion readiness — 0013, 0014 e 0015

> Este assessment registra a base criterial da decisão simulada de aceitação das ADRs no escopo de guidance do framework. Não é aprovação de uma implementação consumidora, não é evidência de produção, não é assurance de effectiveness e não transforma exemplos fictícios em controls.

## 1. Contexto e problema

As ADRs `0013`, `0014` e `0015` foram implementadas como guidance, patterns, templates e exemplos vendor-neutral. O conteúdo técnico foi exercitado em casos fictícios e em drills determinísticos; esta rodada registra a aceitação simulada no escopo do framework, mantendo separada a evidence autorizada de consumidores.

A rodada T01–T13 adicionou semantic e editorial hardening sem alterar schemas, controls, risk tiers, MPB, Registry ou release: `discovery.status` foi alinhado ao enum canônico; as waves de implementação passaram a W0–W6; document status, decision status, maturity e artifact type foram separados; o fluxo G2↔G3 foi explicitado; technology evaluation deixou de ter G3 como destino rígido; e o crosswalk WHAT/HOW/MINIMUM de observabilidade foi registrado.

A pergunta deste assessment é: **a estrutura técnica está pronta para revisão final e eventual promoção de status, e quais evidências ainda impedem essa decisão?**

## 2. Escopo e exclusões

O escopo inclui o contrato de delegação multiagente, o profile opcional de observabilidade AI-native e a arbitragem entre múltiplos control planes. A decisão registrada aceita os três artefatos como guidance do framework. Não inclui aprovação de fornecedor, implantação de produção, alteração de schema, criação de control, mudança de risk tier, alteração da release `1.1.0` ou validação de claims de eficácia de consumidores.

## 3. Critérios de disposição

| Disposição | Uso neste assessment |
|---|---|
| `demonstrated-deterministic` | Critério demonstrado em exemplo ou teste local determinístico com fixtures fictícios. |
| `missing-authorized-evidence` | Evidência que exige ambiente autorizado, privacy review, authority ou caso organizacional. |
| `promotion-ready-after-signoff` | Estrutura técnica suficiente para decisão, sem significar que a decisão já foi tomada. |
| `demonstrated-synthetic` | Case fictício end-to-end demonstra integração, aplicabilidade contratual e cenários negativos, sem provar eficácia operacional. |
| `operationally-validated` | Evidência de implementação/execução autorizada demonstra comportamento operacional no escopo observado; não é inferida de examples ou testes sintéticos. |
| `hold` | Não promover enquanto o gap indicado permanecer sem owner e evidence. |

## 4. Decision status versus evidence maturity — T32

**Classificação do finding:** `PARTIALLY_CONFIRMED`.

O capítulo 00 já separa `status` documental/editorial, disposição da decisão, `maturity`/evidence e `type`. O ADR histórico de adoção da release 1.1.0 também mostra que `accepted` dependeu de aprovação do owner e de critérios técnicos/release verificáveis, mas declarou explicitamente que a adoção do repositório não era adoção organizacional, certificação ou assurance externa. A tensão aparece porque as ADRs 0013–0015 dizem que permanecem `draft` até haver evidência autorizada, o que pode ser lido como se `accepted` significasse simultaneamente decisão arquitetural aceita e eficácia operacional comprovada.

A recomendação é aplicar o **Modelo A — separação**: `accepted` significa que a authority competente aceitou a decisão arquitetural, possivelmente com conditions registradas; `maturity`/evidence permanece uma dimensão independente, com os estados já usados no corpus, incluindo `demonstrated-deterministic`, `demonstrated-synthetic`, `missing-authorized-evidence` e `operationally-validated`. `accepted` não autoriza production use automaticamente e não transforma evidence sintética em evidence operacional.

Para as ADRs 0013–0015, o estado do framework passa a `accepted` com conditions no escopo de guidance, conforme o decision record `SIMULATED_OWNER_AUTHORIZED_REVIEW`. A ausência de authorized evidence continua bloqueando a classificação `operationally-validated` e qualquer claim de production readiness de consumidores. Não é necessário criar enum, schema, control ou nova taxonomia.

| Dimensão | Responde a | Estado observado neste assessment |
|---|---|---|
| `status` documental | O artefato está em draft, maintained ou outro estado editorial? | ADRs 0013–0015: `accepted` |
| Decision status | A authority aceitou, rejeitou ou superseded a decisão? | `accepted` com conditions no escopo do framework; decisão simulada registrada |
| Maturity/evidence | Que força tem a evidence disponível? | `demonstrated-deterministic` + `demonstrated-synthetic`; `missing-authorized-evidence` para operação |
| Artifact type | Que tipo de objeto é este? | ADR/decision, assessment, example e evidence são objetos distintos |

## 5. Resultado executivo

| ADR | Estrutura técnica | Pendência | Disposição recomendada |
|---|---|---|---|
| ADR-0013 — delegação multiagente | Cobre topologia, edges, atenuação, limits, expiry, revocation e failure propagation. | Evidence autorizada da implementação consumidora e recovery real. | `accepted` com conditions no guidance do framework; `missing-authorized-evidence` para consumidor. |
| ADR-0014 — observabilidade AI-native | Cobre correlation, provenance, privacy, deletion, cardinality, cost, containment e export guidance. | Privacy/export/retention review e validação em implementação autorizada. | `accepted` com conditions no guidance do framework; `missing-authorized-evidence` para consumidor. |
| ADR-0015 — arbitragem cross-plane | Cobre authority, source of truth, enforcement, precedence, conflict, fail-safe e substitution material change. | Enforcement, fallback, recovery e substitution na implementação consumidora. | `accepted` com conditions no guidance do framework; `missing-authorized-evidence` para consumidor. |

## 6. ADR-0013 — contrato de delegação multiagente

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
| Integration coherence, negative scenarios, lineage, recovery e substitution/exit | [Synthetic ADR promotion validation case](../examples/cases/adr-promotion-synthetic-validation/README.md) | `demonstrated-synthetic` |
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

A decisão do framework aceita a ADR com conditions após os três cenários determinísticos e sintéticos, o registro de divergências e compensating controls e a revisão simulada documentada. Uma implementação consumidora só pode reivindicar effectiveness após walkthrough e evidence autorizada próprios. Nenhuma extensão obrigatória do `agent-blueprint.schema.json` é justificada por este assessment.

## 7. ADR-0014 — profile opcional de observabilidade AI-native

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
| Correlation/provenance, redaction, retention/deletion, export, cardinality/cost e alert-to-action em fluxo integrado | [Synthetic ADR promotion validation case](../examples/cases/adr-promotion-synthetic-validation/README.md) | `demonstrated-synthetic` |
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

A decisão do framework aceita o profile com conditions após a cobertura determinística e sintética e a revisão simulada documentada. Uma implementação consumidora só pode reivindicar operational validation após privacy review, cardinality/cost review, export test e retention/deletion decision autorizados. O `audit-event.schema.json` permanece inalterado, pois o assessment não demonstra necessidade machine-readable.

## 8. ADR-0015 — arbitragem entre múltiplos control planes

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
| Matrix cross-plane, conflict, precedence, fail-safe, recovery e substitution/exit em fluxo integrado | [Synthetic ADR promotion validation case](../examples/cases/adr-promotion-synthetic-validation/README.md) | `demonstrated-synthetic` |
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

A decisão do framework aceita a ADR com conditions após a matriz cross-plane, conflito determinístico, fail-safe, recovery, substitution/exit e revisão simulada documentada. Uma implementação consumidora só pode reivindicar effectiveness após walkthrough formal, enforcement, fallback e recovery evidence próprios. A ADR não cria taxonomia `consolidated/coordinated/federated` nem `primary_orchestrator` universal.

## 9. Evidence crosswalk — T39

A matriz abaixo reconcilia as formas de evidence já usadas pelo framework. Ela não cria uma nova assurance architecture: explicita o que cada tipo de evidence pode sustentar e onde a decisão precisa parar.

| Evidence type | What it proves | What it does **not** prove | Applicable artifacts | Decision impact |
|---|---|---|---|---|
| Documentary evidence | Que a policy, ADR, guidance, template, schema, rationale ou limitation foi registrada e é rastreável | Que o control foi implementado, eficaz ou aprovado por uma authority | ADRs 0013–0015, assessments, templates, CHANGELOG, ROADMAP | Sustenta compreensão, traceability e preparação; não muda sozinho decision status nem operational readiness |
| Deterministic test evidence | Que fixtures e contratos documentais produziram os resultados esperados em testes reproduzíveis | Que a implementação real, privacy boundary, organization ou runtime longitudinal se comportam igual | `test_adr_walkthrough_evidence.py`, `test_semantic_hardening.py`, validator e gates locais | Sustenta `demonstrated-deterministic` e regression confidence; não sustenta `operationally-validated` |
| Synthetic integration evidence | Que o case fictício exercita integração, aplicabilidade contratual, negative scenarios, lineage, recovery e substitution/exit | Eficácia operacional, privacy compliance real, control effectiveness, accountability organizacional ou production readiness | [Synthetic ADR promotion validation case](../examples/cases/adr-promotion-synthetic-validation/README.md) | Sustenta `demonstrated-synthetic`; mantém `missing-authorized-evidence` para claims operacionais |
| Authorized implementation evidence | Que uma implementação delimitada foi exercitada em ambiente, data boundary e authority autorizados, com evidence recuperável | Que o resultado generaliza para todo o estate ou prova eficácia longitudinal | [Authorized operational validation plan](authorized-operational-validation-plan.md), evidence package e release manifest | Pode sustentar `operationally-validated` somente no escopo observado; habilita decisão condicional conforme authority |
| Operational longitudinal evidence | Que comportamento, incidents, recovery, cost, ownership e control signals foram observados ao longo do tempo no escopo declarado | Que o framework certifica organizações ou garante eficácia fora da população observada | Estate validation, run records, SLO/incident evidence e improvement records | Informa maturity, review cadence, residual risk e continuidade; não substitui decision authority |
| Human sign-off | Que a authority competente tomou uma decisão explícita, com conditions, objections, expiry e residual uncertainty registrados | Que a decisão é prova de effectiveness ou autorização universal de produção | [Human sign-off package](adr-human-signoff-package-0013-0014-0015.md), ADR/decision record e release checklist | Pode alterar `decision status`; não altera automaticamente `maturity/evidence` nem converte `draft` em operational approval sem os critérios aplicáveis |

A regra operacional resultante é: **test passed** demonstra um resultado do teste; **control effective** exige evidence de implementação/eficácia no escopo; **ADR accepted** exige decisão da authority; e **production approved** exige o processo de release e evidence aplicáveis. Nenhuma dessas expressões deve ser usada como sinônimo das demais.

## 10. Testes determinísticos protegidos

O teste `tools/scripts/test_adr_walkthrough_evidence.py` confirma que os exemplos canônicos continuam contendo os critérios essenciais das ADRs G1, G2 e G4, além dos limites do substitution/replay drill. O teste adicional `tools/scripts/test_semantic_hardening.py` protege as correções T02–T10 de discovery status, waves, metadata, gate flow, technology evaluation e observability crosswalk.

Resultado atual:

```text
ADR walkthrough evidence: 4 tests — OK
Semantic hardening: 8 tests — OK
```

Este teste é **verification** da integridade documental. O synthetic case acrescenta `demonstrated-synthetic` para integração end-to-end, cobertura de cenários negativos, lineage, recovery e substitution/exit. O decision record registra aceitação simulada no escopo do framework; nenhum dos dois constitui evidence operacional autorizada, compliance evidence ou evidence de produção de consumidores.

## 11. Decisão solicitada

**Decisão atual recomendada:** `accepted` com conditions para guidance arquitetural do framework; nenhum status de consumidor ou produção é inferido.

**Status das ADRs:** `accepted` no escopo canônico do framework, com `demonstrated-deterministic` + `demonstrated-synthetic`; `missing-authorized-evidence` permanece para implementação consumidora, operational validation e produção.

**Owners propostos:**

- Design Authority: conduzir revisão arquitetural;
- Governance Owner: registrar decisão e conditions;
- Security/IAM e Data/Privacy: revisar limites e exposição;
- Run Authority: validar falha, contenção, recovery e reativação;
- Platform/Observability Owner: produzir export, cardinality/cost e deletion evidence.

**Próxima revisão:** em material change das ADRs, divergence de implementação, evidence operacional contraditória ou após a execução autorizada dos drills T15/T16 de um consumidor.

## 12. Limitações

Os casos e drills do repositório são fictícios e vendor-neutral. Os resultados não provam interoperabilidade universal, eficácia de controls, qualidade longitudinal, conformidade, segurança do modelo, justiça do outcome ou prontidão de produção. Valores de cardinalidade e custo são ilustrativos e não são thresholds universais.

## 13. Referências internas

- [ADR-0013 — Contrato de delegação multiagente](../../docs/architecture/decisions/0013-multi-agent-delegation-contract.md)
- [ADR-0014 — Profile opcional de observabilidade AI-native](../../docs/architecture/decisions/0014-ai-native-observability-profile.md)
- [ADR-0015 — Arbitragem entre múltiplos control planes](../../docs/architecture/decisions/0015-multi-control-plane-arbitration.md)
- [Exemplo G1 — Conflito entre control planes](../examples/multi-control-plane-conflict.example.md)
- [Exemplo G2 — Supervisor/worker](../examples/supervisor-worker-delegation.example.md)
- [Exemplo G4 — Observabilidade AI-native](../examples/ai-native-observability.example.md)
- [Operational drill G4](../examples/ai-native-observability-operational-drill.example.md)
- [Substitution/replay drill](../examples/orchestrator-substitution-replay.example.md)
- [Synthetic ADR promotion validation case](../examples/cases/adr-promotion-synthetic-validation/README.md)
- [ADR-0011 — Adoção da release 1.1.0](../../project/decisions/source-history/0011-framework-release-1.1-adoption.md)
- [Decision record — aceitação condicional das ADRs 0013–0015](../../project/decisions/0004-framework-guidance-acceptance-adr-0013-0015.md)

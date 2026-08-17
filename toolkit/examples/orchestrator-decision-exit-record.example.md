---
title: Exemplo — Orchestrator Decision and Exit Record
status: example
maturity: illustrative
last_reviewed: 2026-08-17
related:
  - ../templates/orchestrator-decision-exit-record.md
  - ../../docs/architecture/decisions/0015-multi-control-plane-arbitration.md
  - ../patterns/multi-control-plane-governance.md
---

# Exemplo — Orchestrator Decision and Exit Record

> Caso fictício. Os nomes `Northstar`, `RelayHub` e `OpenFlow` são ilustrativos. Este registro não é recomendação de produto, evidência de produção, score universal ou aprovação organizacional.

## 1. Identificação da decisão

| Campo | Valor fictício |
|---|---|
| `recordId` | `ODR-2026-001` |
| `status` | `conditional` |
| `decisionDate` | `2026-08-17` |
| `nextReviewAt` | após o piloto multiagente ou mudança material |
| `decisionAuthority` | Design Authority, com challenge de Assurance e consulta a Security/IAM |
| `businessOwner` | fictitious-service-operations |
| `technicalOwner` | fictitious-agent-platform |
| `relatedAgentIds` | `service-desk-supervisor`, `service-desk-worker` |
| `relatedBlueprintRefs` | `blueprint/service-desk-supervisor/0.4`, `blueprint/service-desk-worker/0.4` |
| `relatedRiskRefs` | `risk/fictitious-service-desk/0.4` |

## 2. Problema e contexto

A organização fictícia possui agentes de atendimento criados em uma plataforma de workflow, mas precisa coordenar agentes especializados e ferramentas corporativas sem transformar a plataforma em source of truth de ownership, identity, data ou assurance.

O piloto cobre leitura de tickets, preparação de drafts e atualização de prioridade mediante step-up. Não cobre pagamentos, deleções, concessão de acesso ou decisões sobre pessoas.

## 3. Topologia e padrão de orchestration

A topologia é **coordinated/federated** no vocabulário externo; no vocabulário canônico do framework, é uma combinação de runtime orchestration com governance federada e control/assurance planes separados.

| Campo | Valor fictício |
|---|---|
| `workAttributes` | `determinism: moderate`; `governanceConstraints: high`; `humanOversight: high`; `iterativeNeed: moderate`; `eventDrivenCoordination: low` |
| `primaryOrchestrationPattern` | `workflow` |
| `secondaryOrchestrationPattern` | `supervisory-multi-agent` |
| `patternRationale` | O atendimento segue sequência, approval e SLA; agentes especializados ajudam em reconciliação e preparação de drafts, mas não substituem o workflow nem o step-up humano. |
| `patternEvidenceRefs` | casos fictícios de service desk, teste de approval e matriz de interaction cross-plane |
| `patternConfidence` | `medium` |
| `missingPatternEvidence` | dados de operação real, volume de exceções e teste longitudinal de escalations |
| `iterationPolicy` | `maxIterations=2`; retry/refinement budget de 1; terminar após draft validado, approval humano ou `policy deny`; escalation para Design/Run Authority; owner `fictitious-agent-platform`; evidence: decision timeline e negative tests |

| Plano | Capability | Boundary |
|---|---|---|
| Registry/control | identity estável, owner, tier, blueprint e lifecycle | não substitui IAM, GRC ou tool gateway |
| Orchestrator runtime | routing, sequencing, retries limitados e delegation | não autoriza scopes nem aceita risco residual |
| Identity plane | delegated subject, workload identity e expiry | não decide finalidade ou valor |
| Data/policy plane | classificação, finalidade e acesso ao ticket | não publica ou executa tool |
| Tool gateway | scopes, parâmetros, approval e kill switch | não decide tier ou admissibility |
| Assurance plane | assessment, evidence, challenge e residual risk | não opera o runtime |
| Run plane | telemetry, alert, containment e reactivation | não muda finalidade ou risco aceito |

## 4. Comparação resumida

| Critério | Northstar | RelayHub | OpenFlow | Disposição |
|---|---|---|---|---|
| routing e workflow | forte | forte | moderado | não decisivo isoladamente |
| registry e reconciliation | parcial | parcial | requer adapter | manter registry externo como authority |
| identity/delegation | adapter obrigatório | forte em um domínio | depende de IAM externo | nenhum substitui identity plane |
| policy/tool enforcement | gateway externo | parcialmente integrado | gateway externo | tool gateway permanece obrigatório |
| multi-agent delegation | suportada | suportada | possível via workflow | exigir contrato supervisor/worker |
| telemetry/export | export parcial | export documentado | depende de OTel adapter | conditional até teste de export |
| portability | state proprietário moderado | state proprietário alto | state controlável | OpenFlow tem menor lock-in, mas maior custo de integração |
| recovery/kill switch | depende de runtime | integrado em parte | depende de gateway | kill switch independente obrigatório |
| enterprise proximity | alta no caso fictício | média | baixa | peso contextual, não universal |

## 5. Decision rationale

A opção fictícia `Northstar` foi escolhida para o piloto apenas porque reduz o tempo de integração com o workflow de atendimento. Essa proximidade não autoriza a plataforma a ser source of truth de owner, tier, identity, evidence ou risk acceptance.

A decisão é `conditional` até que sejam concluídos: export test de registry, blueprint, policies, event lineage e evidence; teste de substituição de routing; exercício de conflito entre orchestrator e tool gateway; teste de revogação de delegated identity; e drill de quarantine sem depender do próprio orchestrator.

## 6. Authority e enforcement

| Capability | Authority | Source of truth | Enforcement | Fallback |
|---|---|---|---|---|
| owner e purpose | Business Owner/Governance | registry organizacional | registry workflow | bloquear mudança material |
| identity | Identity Authority | IAM | token/claims/gateway | fail-closed em escrita crítica |
| tier/admissibility | Design/ Risk Authority | risk record | release gate | `restricted` |
| tool scope | Tool Authority | enterprise tool registry | tool gateway | deny |
| evidence | Assurance | evidence store/manifest | release/attestation gate | hold |
| incident/quarantine | Run Authority | operational state | kill switch/quarantine | isolate capability |

## 7. Exit plan

O exit trigger ocorre se o orchestrator perder export de event lineage, introduzir uma mudança material sem detecção, não suportar a revogação de delegated identity ou criar concentração de risco acima do appetite aprovado.

A saída congela novas ativações, preserva registry, blueprints, policy mappings, event/evidence lineage e decisões; exporta os formatos testados; substitui routing e delegation por uma implementação alternativa; reconcilia agent IDs, scopes e states; executa regressão de tool-use, policy, observability e recovery; e reautoriza o piloto ou executa sunset.

## 8. Condições e evidências

| Condição | Owner | Expiry | Evidence |
|---|---|---|---|
| export de registry/blueprint/evidence testado | Platform Owner | antes do piloto | export hash + restore drill |
| tool gateway independente do orchestrator | Security/Tool Authority | antes de escrita | negative test + gateway config |
| delegated identity revogável | Identity Authority | antes de delegation | revocation drill |
| correlation ID cross-plane | Run Authority | antes de produção | reconstructed trace |
| exit test | Design Authority | quarterly | substitution record |

## 9. Disposição

**Decisão:** `conditional`.

**Risco residual:** dependência temporária do adapter de export e integração de telemetry. Não há autorização para produção com ação irreversível até que as condições tenham evidence e expiry vigentes.

**Próxima decisão:** approve, renew conditional ou reject após o piloto fictício e os testes listados.

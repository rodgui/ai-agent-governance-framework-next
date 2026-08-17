---
title: Orchestrator Decision and Exit Record
type: template
status: maintained
maturity: illustrative
last_reviewed: 2026-08-17
review_cycle: quarterly
owners: [architecture, governance, platform]
related:
  - ../../docs/architecture/decisions/0011-multi-control-plane-arbitration.md
  - ../../docs/framework/06-architecture-and-technical-controls.md
  - ../../docs/framework/07-evaluation-evidence-and-assurance.md
  - ../../docs/framework/09-operations-incidents-and-continuity.md
  - ../patterns/multi-control-plane-governance.md
---

# Orchestrator Decision and Exit Record

> Use este template para decisões de arquitetura e plataforma. Ele não aprova fornecedor automaticamente, não substitui risk assessment, assurance, release decision ou contrato. Campos ausentes permanecem `missing`; claims sem evidência permanecem `conditional` ou `unverified`.

## 1. Identificação da decisão

| Campo | Preencher |
|---|---|
| `recordId` | identificador estável do decision record |
| `status` | `draft`, `under-review`, `approved`, `conditional`, `rejected`, `superseded` |
| `decisionDate` | data da decisão |
| `nextReviewAt` | data ou evento de revisão |
| `decisionAuthority` | authority competente para este tier e capability |
| `businessOwner` | owner do outcome |
| `technicalOwner` | owner da arquitetura e implementação |
| `assuranceReviewer` | reviewer/challenge independente quando aplicável |
| `relatedAgentIds` | agents, topologies ou portfolio affected |
| `relatedBlueprintRefs` | blueprints e versões afetadas |
| `relatedRiskRefs` | risk records, assessments e ADRs |

## 2. Problema e contexto

**Problema de negócio ou plataforma:**

<!-- Qual decisão precisa ser tomada? O que não funciona com a situação atual? -->

**Use cases e população:**

<!-- Quais workflows, agentes, usuários, regiões e classes de dados estão no escopo? -->

**Decisões fora do escopo:**

<!-- O que este registro não decide? -->

**Baseline atual:**

<!-- Quais orchestrators, gateways, registries, systems of record e runtimes já existem? -->

## 3. Topologia e padrão de orchestration

| Campo | Preencher |
|---|---|
| `topologyPattern` | descrição canônica da topologia; nomes externos podem ser registrados como crosswalk |
| `controlPlaneCount` | quantidade de planos participantes |
| `planes` | lista de planos e suas boundaries |
| `coordinationModel` | routing, workflow, iterative coordination, multi-agent delegation ou combinação |
| `trustBoundaries` | limites entre agents, planes, data, tools, identity e runtime |
| `failureBoundaries` | blast radius e containment boundary |
| `correlationModel` | correlation IDs, event lineage e evidence references |
| `authorityModel` | authorities por capability, tier e decisão |

**Diagrama ou referência de arquitetura:**

<!-- Link para blueprint, diagrama e matriz de interação. -->

## 4. Capability e comparação de opções

| Capability | Necessária? | Opção avaliada | Evidência | Limitação | Disposição |
|---|---:|---|---|---|---|
| request/task routing |  |  |  |  |  |
| registry/discovery/reconciliation |  |  |  |  |  |
| identity e delegated authority |  |  |  |  |  |
| policy distribution/enforcement |  |  |  |  |  |
| data/source governance |  |  |  |  |  |
| tool/API/MCP mediation |  |  |  |  |  |
| model/provider routing |  |  |  |  |  |
| lifecycle/version/change control |  |  |  |  |  |
| evidence/decision lineage |  |  |  |  |  |
| observability/behavioral analytics |  |  |  |  |  |
| cost/quota/FinOps |  |  |  |  |  |
| quarantine/rollback/kill switch |  |  |  |  |  |
| human oversight/step-up |  |  |  |  |  |
| interoperability/export |  |  |  |  |  |

**Critérios e pesos adotados:**

<!-- Explique por que um critério importa. Pesos não são universais; registre rationale. -->

**Alternativas consideradas e rejeitadas:**

<!-- Não escreva “melhor ferramenta”; registre trade-offs e evidência. -->

## 5. Authority, source of truth e enforcement

| Capability/atributo | Authority | Source of truth | Enforcement point | Fallback | Evidence ref |
|---|---|---|---|---|---|
| agent identity |  |  |  |  |  |
| ownership |  |  |  |  |  |
| tier/admissibility |  |  |  |  |  |
| policy decision |  |  |  |  |  |
| data access |  |  |  |  |  |
| tool/action scope |  |  |  |  |  |
| model/provider/version |  |  |  |  |  |
| runtime state |  |  |  |  |  |
| incident/quarantine |  |  |  |  |  |
| value/cost |  |  |  |  |  |

**Precedência em conflito:**

<!-- Qual decisão prevalece? Quem arbitra? O que acontece quando a authority está indisponível? -->

**Rota de exceção:**

<!-- Authority, rationale, compensating controls, scope, expiry, residual risk e evidence. -->

## 6. Portabilidade e lock-in

| Dimensão | Estado atual | Risco | Mitigação | Teste ou evidência |
|---|---|---|---|---|
| registry e discovery |  |  |  |  |
| agent/blueprint/configuration |  |  |  |  |
| policies e mappings |  |  |  |  |
| prompts/evaluations |  |  |  |  |
| telemetry e audit events |  |  |  |  |
| evidence packages |  |  |  |  |
| tool/data/model bindings |  |  |  |  |
| proprietary state/memory |  |  |  |  |
| credentials and identity |  |  |  |  |

**Dependências proprietárias críticas:**

**Formato e autoridade da exportação:**

**Último teste de substituição:**

**Limitações conhecidas:**

## 7. Resiliência, degradação e saída

| Cenário | Estado seguro | Authority | Ação | Evidence | Critério de retorno |
|---|---|---|---|---|---|
| orchestrator indisponível |  |  |  |  |  |
| policy/identity unavailable |  |  |  |  |  |
| tool gateway failure |  |  |  |  |  |
| registry/evidence unavailable |  |  |  |  |  |
| model/provider failure |  |  |  |  |  |
| security incident |  |  |  |  |  |
| vendor exit |  |  |  |  |  |

**RTO/RPO e tolerâncias:**

**Modo degradado aprovado:**

**Exit trigger:**

**Exit sequence:**

1. congelar mudanças e novas ativações;
2. preservar evidence, state, registry e decision history;
3. confirmar authority e comunicação;
4. exportar artefatos conforme formato testado;
5. migrar ou substituir capabilities e bindings;
6. executar reconciliação e testes de regressão;
7. validar identity, policy, telemetry, cost e recovery;
8. reautorizar ou executar sunset.

## 8. Risco e assurance

| Dimensão | Resultado |
|---|---|
| `riskTier` |  |
| `admissibility` |  |
| material change triggers |  |
| critical controls |  |
| evidence package |  |
| independent challenge |  |
| residual risk authority |  |
| conditions and expiry |  |

**Claims sem evidência:**

**Findings abertos:**

## 9. Decisão

**Decisão solicitada:** `approve`, `conditional`, `hold` ou `reject`.

**Rationale:**

**Condições, owner e expiry:**

**Risco residual aceito por:**

**Próxima revisão ou evento trigger:**

**Evidence references:**

## 10. Checklist de conclusão

- [ ] topology e boundaries estão descritas;
- [ ] capabilities necessárias foram comparadas com evidência;
- [ ] authority e source of truth foram definidos por atributo;
- [ ] enforcement points e fallbacks são conhecidos;
- [ ] conflitos de policy têm precedência e authority;
- [ ] lock-in e proprietary state foram registrados;
- [ ] export e substitution test foram definidos;
- [ ] degraded mode, RTO/RPO e recovery foram exercitados;
- [ ] exit trigger e exit sequence têm owner;
- [ ] risk, admissibility, conditions e expiry estão vinculados;
- [ ] evidence package é recuperável e versionado;
- [ ] decision authority registrou approve/conditional/hold/reject;
- [ ] nenhuma claim sem evidência foi tratada como cobertura.

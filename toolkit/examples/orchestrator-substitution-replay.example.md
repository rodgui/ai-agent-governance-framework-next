---
title: Exemplo — Orchestrator substitution and replay drill
status: example
maturity: illustrative
last_reviewed: 2026-08-17
related:
  - ../templates/orchestrator-decision-exit-record.md
  - ../assessments/technology-evaluations/orchestrator-evaluation.md
  - ../../docs/architecture/decisions/0015-multi-control-plane-arbitration.md
---

# Exemplo — Orchestrator substitution and replay drill

> Caso fictício. O teste valida invariantes de governança, não performance, qualidade de modelo ou compatibilidade de um produto específico. Nenhuma ação real é reexecutada.

## 1. Objetivo

Demonstrar que duas implementações abstratas de orchestration conseguem consumir o mesmo bundle lógico de registry, blueprints, policy mappings, delegation edges, evidence refs, event lineage, identity mappings, tool bindings, memory/state refs e decision records, preservando a decisão e os estados seguros relevantes.

O teste não exige que os formatos físicos sejam iguais. Cada implementation adapter pode usar formatos internos diferentes, desde que produza o mesmo export canônico e os mesmos resultados de replay.

## 2. Bundle canônico

| Grupo | Referências fictícias |
|---|---|
| Registry | `registry/service-desk-supervisor/0.4` |
| Blueprints | supervisor e worker `0.4` |
| Policy | `policy/service-desk/triage/T2/conditional` |
| Delegation | `DEL-A-001` |
| Evidence | decision record e negative test do Caso A |
| Event lineage | task → delegation → policy → tool → containment |
| Identity | supervisor e worker identities |
| Tool | `tool/service-desk/update-priority` |
| Memory/state | estado de triagem do Caso A |
| Decision | disposição `conditional` |

## 3. Eventos de replay

A sequência lógica é:

1. leitura do ticket dentro do scope permitido;
2. tentativa de escrita de prioridade crítica pelo worker;
3. expiração da delegation edge;
4. retry posterior à expiração.

| Evento | Resultado obrigatório |
|---|---|
| `read_ticket` | `allow-read` |
| `critical_priority_write` | `deny-tool-scope` |
| `delegation_expired` | `edge-revoked` |
| `retry_after_expiry` | `deny-replay` |

O replay é somente de decisão e lineage. Não executa side effect, não acessa sistema corporativo e não reconstitui payload sensível.

## 4. Critérios de equivalência

A substituição passa somente se:

- o export das duas implementações for equivalente após canonicalização;
- a ordem e a correlação dos eventos forem preservadas;
- a escrita crítica permanecer negada;
- o retry após expiry permanecer negado;
- delegation, identity, policy, evidence e decision refs continuarem recuperáveis;
- nenhuma implementação converter ausência de authority em `allow`;
- findings e limitações permanecerem visíveis.

## 5. Disposição fictícia

**Resultado:** `conditional` para a execução do drill; `hold` para declarar portabilidade comprovada em produção.

**Passes fictícios:** export canônico preservado; replay equivalente; deny de escrita crítica preservado; retry pós-expiry negado.

**Evidências ausentes:** teste com backend autorizado, volume real, restore drill, credential rotation, memory/state deletion e reconciliação com uma ferramenta alternativa.

**Owner:** Design Authority para decisão de portabilidade; Platform Owner para adapter/export; Run Authority para recovery e reactivation.

## Limitações

O caso não prova interoperabilidade universal, ausência de lock-in, qualidade de output, eficácia de controls ou recuperação de produção. O resultado é uma evidência de desenho e de teste determinístico, não uma aprovação de fornecedor.

## Critério de conclusão

O drill está concluído quando um reviewer autorizado consegue comparar os dois exports, reproduzir os quatro outcomes, verificar que nenhum side effect foi executado e localizar decision, evidence, identity, policy e delegation refs sem depender de formato proprietário.

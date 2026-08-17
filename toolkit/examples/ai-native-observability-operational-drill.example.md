---
title: Exemplo — AI-native observability operational drill
status: example
maturity: illustrative
last_reviewed: 2026-08-17
related:
  - ../templates/ai-native-observability-profile.md
  - ../patterns/ai-native-observability-profile.md
  - ../../docs/architecture/decisions/0014-ai-native-observability-profile.md
---

# Exemplo — AI-native observability operational drill

> Caso fictício. O drill valida semântica de privacidade e operação; não captura, exclui ou mede dados reais.

## 1. Escopo

A cadeia fictícia cobre `task`, `model.call`, `retrieval`, `policy.decision`, `tool.request/result`, `agent.memory/state`, `containment` e `value.cost`. A população é uma investigação de plataforma com `iterative-reasoning` primário e `workflow` secundário.

## 2. Redaction e minimização

O evento mantém `correlationId`, refs de policy, tool, evidence e decision, mas não captura prompt bruto, secrets, tokens, payload integral ou argumentos sensíveis de tool. Quando necessário para reconstrução, usa referências, hashes, categorias e contagens.

**Resultado fictício:** PASS. O reviewer confirma que payload sensível, prompt e secret foram redigidos ou omitidos.

## 3. Deletion drill de memory/state

O estado fictício `state/WALK-B-2026-001/investigation` possui cópias em primary store, cache, index e backup. O drill exige remoção em todos os stores, bloqueio de leitura posterior e preservação somente de evidence hold explicitamente autorizado.

| Store | Resultado fictício |
|---|---|
| primary | removido |
| cache | removido |
| index | removido |
| backup | removido conforme retention/deletion policy |
| evidence hold | preservado somente para o decision/evidence record autorizado |

**Resultado fictício:** PASS. O estado não permanece visível nos stores operacionais e o evidence hold continua separado.

## 4. Cardinalidade e custo

O perfil usa somente atributos de correlação e decisão necessários: `taskId`, `topologyId`, `delegationId` e `policyDecisionRef`. `rawPrompt`, `rawToolArguments` e `fullPayload` não são dimensões exportadas.

| Métrica | Resultado fictício |
|---|---:|
| events por task | 12 |
| limite do perfil fictício | 16 |
| custo de telemetry em unidades fictícias | 3,00 |
| budget do perfil fictício | 4,00 |

**Resultado fictício:** PASS. O volume e o custo permanecem dentro do envelope ilustrativo. Os valores não são thresholds universais.

## 5. Evidence e limitações

Evidências esperadas são redaction test, deletion record, access denial após deletion, cardinality report, cost report, correlation reconstruction e privacy review. O drill não prova eficácia de containment, factualidade do modelo, qualidade do outcome ou conformidade universal.

## Critério de conclusão

O drill está concluído quando o reviewer reproduz redaction, deletion em todos os stores, preservação controlada de evidence hold, ausência de atributos de alta cardinalidade e comparação entre telemetry cost e budget, sem depender de um backend proprietário.

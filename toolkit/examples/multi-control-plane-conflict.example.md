---
title: Exemplo — Conflito entre control planes
status: example
maturity: illustrative
last_reviewed: 2026-08-17
related:
  - ../../docs/architecture/decisions/0011-multi-control-plane-arbitration.md
  - ../patterns/multi-control-plane-governance.md
  - ../../docs/framework/02-governance-and-accountability.md
  - ../../docs/framework/06-architecture-and-technical-controls.md
---

# Exemplo — Conflito entre control planes

> Este é um caso fictício para testar coerência do método. Não é evidência de produção, não define threshold universal e não prescreve produto.

## Cenário

O agente fictício `service-desk-supervisor` recebe um pedido para atualizar a prioridade de um ticket crítico. O supervisor delega a tarefa ao `service-desk-worker`. O orchestrator local considera a solicitação permitida porque o fluxo de suporte está ativo e o usuário possui sessão válida.

A ação, porém, atravessa quatro planos: o identity plane confirma o usuário delegado; o registry confirma o `agent_id` e o blueprint ativo; o data/policy plane identifica o ticket como classe restrita; e o tool gateway verifica se o worker possui scope de escrita para prioridade crítica.

## Matriz de interação

| Plano | Capability | Authority | Source of truth | Enforcement | Resultado |
|---|---|---|---|---|---|
| Identity plane | delegated subject e sessão | Identity Authority | diretório de identidade | token e claims | `allow` para o usuário; sem ampliação de privilégio |
| Registry/control plane | agent ID, owner, tier e blueprint | Design Authority | agent registry | status e material change | `allow` para versão ativa |
| Data/policy plane | classificação e finalidade | Data Authority | data contract | filtro de finalidade e classificação | `conditional`: ação crítica exige scope específico |
| Tool gateway | ação e parâmetros | Tool Authority | enterprise tool registry | scope e approval mode | `deny`: worker não possui escrita em prioridade crítica |
| Assurance plane | status de release e condições | Assurance/Release Authority | evidence manifest | condição/expiry | `allow` somente se as condições estiverem vigentes |

## Decisão

A ação não é executada. O `deny` do tool gateway prevalece porque é um enforcement point obrigatório para uma ação state-changing e crítica. O orchestrator não pode transformar a negativa em retry com scope ampliado. O evento registra `correlation_id: fict-2026-001`, agent IDs, versão do blueprint, delegated subject, tool, parâmetros redigidos, decisões locais, authority, outcome e evidence reference.

O incidente não é classificado automaticamente como falha do usuário. É aberto um finding para verificar se o fluxo de delegação estava corretamente desenhado e se o worker deveria preparar apenas um draft ou solicitar step-up humano. A Run Authority mantém o agente disponível para ações read-only e restringe a capability de escrita crítica até a remediação.

## Teste de indisponibilidade

Se o tool gateway ou a authority de identidade estiver indisponível, o fluxo de escrita crítica permanece `restricted` ou `quarantined`, conforme o tier e o blueprint. Nenhum cache local pode converter a ausência de decisão em `allow` sem uma degradação previamente aprovada, expirada e auditável.

## Evidências esperadas

A execução do exemplo deve produzir a matriz de interação, o decision record, os eventos correlacionados, o finding de divergência ou insuficiência de scope, a disposição da Run Authority e o teste negativo demonstrando que o retry não amplia privilégio.

## Critério de conclusão

O caso está concluído quando um revisor consegue reconstruir a cadeia supervisor → worker → tool gateway, identificar a authority que negou, verificar que o deny não foi contornado, localizar a evidência e confirmar o estado operacional após a contenção.

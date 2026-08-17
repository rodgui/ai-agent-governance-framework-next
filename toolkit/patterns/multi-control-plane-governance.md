---
title: Pattern — Multi-Control-Plane Governance
status: draft
owner: framework-maintainers
last_reviewed: 2026-08-17
review_cycle: quarterly
related:
  - README.md
  - ../../docs/architecture/decisions/0015-multi-control-plane-arbitration.md
  - ../../docs/framework/02-governance-and-accountability.md
  - ../../docs/framework/06-architecture-and-technical-controls.md
  - ../../docs/framework/09-operations-incidents-and-continuity.md
---

# Pattern — Multi-Control-Plane Governance

## Intenção

Governar fluxos em que dois ou mais control planes, gateways, brokers, plataformas de workflow ou sistemas de assurance participam da mesma cadeia de decisão e ação.

## Problema

Uma organização pode ter um orchestrator de plataforma, um gateway de tools, um sistema de identidade, uma camada de dados, um SIEM, um GRC e uma plataforma de workflow. Sem boundaries e precedência explícitos, cada componente pode apresentar uma visão parcial de ownership, status ou policy. O resultado é conflito não tratado, evidence fragmentada, bypass de enforcement ou falsa certeza produzida por um único dashboard.

## Quando usar

Use este pattern quando há múltiplas plataformas; quando uma ação atravessa mais de uma trust boundary; quando registry, identity, data, tools, policy e runtime têm systems of record distintos; quando um control plane comercial é apenas um adapter entre sistemas especializados; ou quando a substituição de uma camada precisa ser possível sem perder histórico e evidência.

## Forças e trade-offs

- autonomia de domínio versus precedência comum;
- single-pane-of-glass versus sistemas especializados;
- disponibilidade versus fail-closed;
- reconciliação automática versus preservação de conflitos;
- automação de policy versus julgamento e autoridade humana;
- portabilidade versus uso de capabilities proprietárias;
- correlação completa versus minimização de dados.

## Solução

Defina uma cadeia explícita de control planes e enforcement points. Cada capability possui authority, source of truth por atributo, ponto de enforcement, fallback, correlation key e evidence reference. O control plane coordena e aciona; systems especializados aplicam controles no próprio domínio; o assurance plane desafia a suficiência; a authority humana decide exceção e risco residual.

A regra é **autorização composta**: uma ação material só ocorre quando todos os enforcement points obrigatórios para o tier retornam decisões compatíveis. A decisão mais restritiva prevalece para identity, data, privacy, admissibility, security e state-changing actions, salvo exception formal com expiry e residual-risk authority.

## Fluxo operacional

1. registrar os planos e suas capabilities;
2. atribuir authority e source of truth por atributo;
3. declarar boundaries, entradas, saídas e trust boundaries;
4. propagar correlation ID por toda a execução;
5. aplicar policy em cada enforcement point obrigatório;
6. preservar `allow`, `deny`, `conditional`, `missing`, `restricted` e `quarantined` sem conversão silenciosa;
7. abrir finding quando houver divergência entre sistemas;
8. aplicar fail-safe quando a authority ou o enforcement crítico estiver indisponível;
9. manter evidence e decision record recuperáveis;
10. reabrir assurance e change control quando houver alteração de plano, boundary, source of truth ou comportamento de falha.

## Matriz de interação

| Campo | Conteúdo mínimo |
|---|---|
| `plane` | control, runtime, assurance, identity, data, security, workflow ou outro |
| `capability` | routing, registry, policy, identity, data, tools, telemetry, assurance, recovery |
| `authority` | papel ou função que decide, aplica, revisa ou excepciona |
| `sourceOfTruth` | sistema autoritativo para o atributo consumido |
| `enforcementPoint` | gateway, broker, IAM, DLP, runtime ou workflow que aplica a decisão |
| `input` / `output` | contexto recebido e decisão produzida |
| `correlationKey` | chave que liga evento local à execução completa |
| `fallback` | comportamento em indisponibilidade ou timeout |
| `evidenceRef` | manifesto, event, finding ou decision record recuperável |
| `conflictPath` | autoridade, estado e workflow para divergência |

## Controles e evidências

O pattern não cria requirements próprios. Os controls aplicáveis vêm do tier, da capability e do domínio: identity e least privilege; source of truth; tool/API/MCP governance; policy enforcement; observability; evidence integrity; incident containment; rollback; attestation e material change. Evidências esperadas incluem a matriz de interação, os records de decisão, eventos correlacionados, findings de divergência, teste de fail-safe e exercício de substituição.

## Exemplo vendor-neutral

Um supervisor agent inicia uma ação de escrita. O orchestrator local faz o routing, o identity plane confirma o delegated subject, o data plane valida a classificação, o tool gateway verifica scope e parâmetros e o assurance status confirma que o agente não está `conditional` com condição expirada. Se qualquer enforcement point retornar `deny` ou `missing` crítico, a ação não é executada; o resultado e a autoridade são registrados com o mesmo correlation ID.

## Métricas

- ações atravessando planos sem matriz registrada;
- decisões incompatíveis por capability;
- divergências de source of truth sem finding;
- eventos sem correlation ID;
- `allow` produzido após `deny` ou `missing` crítico;
- falhas de fail-safe;
- tempo entre conflito e decisão accountable;
- evidências cross-plane incompletas;
- dependências proprietárias sem exit test.

## Antipatterns relacionados

- control plane comercial tratado como policy authority universal;
- último timestamp escolhido como reconciliação normativa;
- dashboard unificado sem enforcement;
- `allow` local que ignora `deny` de domínio;
- fallback que remove identity, logging ou assurance;
- plano de arbitragem dependente do agente que está sendo contido;
- múltiplos registries com owner ou tier divergentes e nenhuma authority de reconciliação.

## Limitações

O pattern não elimina a necessidade de authorities de domínio nem torna um control plane único obrigatório. Uma federação bem desenhada ainda exige integração, testes end-to-end, disciplina de schema e owners vivos. A regra mais restritiva não substitui judgment em casos de exceção: ela define o fail-safe até que uma authority compatível decida.

## Mappings de implementação

Podem ser usados gateways de API/MCP, IAM, DLP, data catalog, SIEM/SOAR, GRC, workflow engines, registry, evidence stores e control planes de fornecedores. Esses componentes são adapters substituíveis. A escolha não altera boundaries, authorities, evidence outcomes ou critérios de fail-safe.

## Critério de conclusão

O pattern está adequadamente aplicado quando um revisor consegue reconstruir uma ação material atravessando os planos, identificar cada authority e enforcement point, reproduzir um conflito de policy, observar o fail-safe e localizar a evidência e o decision record sem depender de conhecimento tribal.

---
title: ADR-0015 — Arbitragem entre múltiplos control planes
status: draft
owner: framework-maintainers
last_reviewed: 2026-08-17
review_cycle: major-change
supersedes: null
related:
  - ../README.md
  - ../../framework/02-governance-and-accountability.md
  - ../../framework/06-architecture-and-technical-controls.md
  - ../../framework/09-operations-incidents-and-continuity.md
  - ../../../toolkit/patterns/multi-control-plane-governance.md
  - ../../../toolkit/patterns/control-and-assurance-planes.md
---

# ADR-0015 — Arbitragem entre múltiplos control planes

## Status e escopo

Esta é uma **decisão arquitetural em rascunho** da primeira onda G1. Ela não cria um novo control nem prescreve produto. Define como o framework deve tratar fluxos em que mais de um control plane, gateway, broker, plataforma de workflow ou sistema de assurance participa da mesma decisão ou ação.

A decisão permanece `draft` até ser exercitada com um caso organizacional e aprovada pela Design Authority, pelas authorities de segurança/identidade e pela Run Authority quando houver efeito em produção.

## Contexto

O framework adota control plane, assurance plane e runtime plane como planos relacionados, mas distintos. Também adota federação com common controls, source of truth por atributo, adapters substituíveis e enforcement fora do modelo. Na prática, uma organização pode ter um orchestrator de plataforma, um gateway de tools, um sistema de identidade, um sistema de segurança, uma plataforma de workflow e um repositório de evidências participando da mesma cadeia.

Múltiplos planos são aceitáveis e frequentemente necessários. O risco surge quando a multiplicidade não tem regra de arbitragem: dois planos podem produzir decisões incompatíveis; um plano pode tratar seu próprio posture signal como assurance; a evidência pode ficar fragmentada; ou uma rota alternativa pode contornar o enforcement definido.

## Decisão proposta

1. **Múltiplos control planes são permitidos, mas não existe autoridade implícita de precedência.** Cada capability terá uma authority e um sistema autoritativo por atributo. Um orchestrator de fornecedor não se torna autoridade normativa apenas por executar routing ou policy local.

2. **A decisão mais restritiva prevalece quando o conflito envolve segurança, identidade, privacidade, admissibilidade ou uma ação state-changing**, salvo uma exceção formal registrada com escopo, rationale, compensating controls, expiry e residual-risk authority. Um plano não pode transformar um `deny`, `restricted`, `quarantined` ou `missing` emitido por uma authority válida em `allow` silencioso.

3. **A autorização é composta, não delegada por aparência.** A ação só é executável quando todos os enforcement points obrigatórios para o tier e a capability retornam uma decisão compatível. O modelo pode propor; o orchestrator pode coordenar; o gateway, identity provider, data policy ou tool broker pode aplicar a regra no seu domínio; a authority humana decide exceções e risco residual.

4. **Cada fluxo de produção deve declarar a cadeia de control planes.** O blueprint ou artefato de arquitetura registra `plane`, capability, authority, source of truth, enforcement point, input, output, correlation key, fallback e evidence reference. Um componente não documentado não pode ser tratado como parte confiável da cadeia.

5. **A correlação é cross-plane por design.** Toda execução material usa um `correlation_id` estável para ligar actor, agent, topology, task, session, model, data, tool, policy decisions, approvals, outcomes, incidentes e evidence. Cada plano pode manter seu evento local, mas deve propagar a chave comum e preservar a proveniência da decisão.

6. **Divergência é finding, não dado a ser reconciliado silenciosamente.** Se dois sistemas discordarem sobre owner, tier, admissibility, lifecycle, identity, tool scope ou policy status, o fluxo registra a divergência, aplica o fail-safe proporcional e abre remediação. Timestamp mais recente não resolve conflito normativo por si só.

7. **A falha do plano de arbitragem não autoriza degradação silenciosa.** Para ações críticas, financeiras, privilegiadas, irreversíveis ou de alto impacto, a ausência da authority, do identity check, do policy gateway, do tool broker ou da evidência obrigatória resulta em `fail-closed`, `restricted` ou `quarantined`, conforme o risco. Degradação controlada só é permitida quando prevista no blueprint e compatível com a admissibilidade.

8. **O assurance plane permanece independente da autopostura do control plane.** O control plane pode fornecer context, signals e actions; não pode certificar sozinho a própria eficácia, aceitar risco residual fora da sua authority ou converter cobertura incompleta em assurance.

9. **A substituição de um control plane é uma mudança material quando altera enforcement, trust boundary, source of truth, identity, evidence ou comportamento de falha.** A mudança exige diff arquitetural, reavaliação proporcional, teste de substituição e decisão de release/attestation.

## Matriz mínima de interação

Cada fluxo que atravessar mais de um plano deve produzir uma matriz com estas colunas:

| Campo | Pergunta |
|---|---|
| `plane` | Qual plano ou componente participa? |
| `capability` | Qual capacidade ele fornece: identity, routing, registry, data, tool, policy, telemetry, assurance ou recovery? |
| `authority` | Quem pode decidir, negar, alterar ou excepcionar? |
| `sourceOfTruth` | Qual sistema é autoritativo para cada atributo consumido? |
| `enforcementPoint` | Onde a decisão é tecnicamente aplicada? |
| `input` / `output` | Que contexto recebe e qual decisão produz? |
| `correlationKey` | Como o evento é ligado à execução completa? |
| `fallback` | Qual comportamento ocorre quando o componente falha? |
| `evidenceRef` | Onde ficam a decisão e a evidência recuperável? |
| `conflictPath` | Qual fluxo trata uma divergência ou policy denial? |

## Exemplo de conflito

Um supervisor agent solicita que um worker atualize um record crítico. O orchestrator local classifica o pedido como permitido, mas o tool gateway identifica que o scope do worker não inclui a ação. O gateway emite `deny`, registra o motivo com o mesmo `correlation_id`, impede a execução, atualiza o estado da tentativa e encaminha o finding para a authority apropriada. O orchestrator não pode converter o `deny` em `retry` com escopo ampliado sem nova decisão autorizada.

Se o registry indicar `conditional` e a condição obrigatória estiver expirada, a ação permanece bloqueada mesmo que o orchestrator tenha uma política local mais permissiva. Se a evidência do identity provider estiver indisponível durante uma ação T3/T4, o fluxo não assume identidade válida por cache sem que essa degradação tenha sido explicitamente aprovada e limitada.

## Consequências

### Positivas

A decisão reduz ambiguidade em ambientes híbridos, preserva ownership federado, evita que um vendor control plane se confunda com governança completa, melhora a reconstrução de incidentes e torna a substituição de componentes uma decisão verificável.

### Custos

Será necessário propagar correlation IDs, manter uma matriz de interação, registrar divergências e executar mais testes end-to-end. Em organizações pequenas, algumas authorities podem ser acumuladas, mas o conflito e os controles compensatórios precisam permanecer explícitos.

## Não decidido nesta ADR

Esta ADR não escolhe produtos, não define uma topologia universal, não cria uma nova classificação `consolidated/coordinated/federated`, não transforma OTel ou A2A em requisito e não define os campos finais do contrato supervisor/worker. Esses pontos podem ser tratados em patterns, templates ou decisões posteriores quando houver caso de uso.

## Critérios de validação

- um caso com dois control planes produz matriz completa de interação;
- um conflito de policy resulta em decisão determinística e auditável;
- nenhuma rota state-changing contorna o enforcement obrigatório;
- divergência de source of truth vira finding e não reconciliação silenciosa;
- a falha de um componente crítico produz fail-safe compatível com o tier;
- todos os eventos materiais compartilham `correlation_id` e `evidenceRef`;
- a substituição de um plano é reconhecida como material change;
- assurance permanece independente da postura declarada pelo control plane;
- o caso fictício não contém dados pessoais, secrets ou evidência de produção.

## Evidência e aprovação

A decisão precisa ser aprovada após walkthrough com Design Authority, Governance Owner, Security/IAM Authority, Data/Privacy Authority e Run Authority. A aprovação deve registrar o caso exercitado, as divergências encontradas, os controles compensatórios, as limitações e a data de revisão.

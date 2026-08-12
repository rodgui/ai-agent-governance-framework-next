---
title: Behavioral Analytics Use Case
status: maintained
last_reviewed: 2026-08-11
review_cycle: quarterly
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# Behavioral Analytics Use Case

Este artefato consolida fontes validadas segundo a estratégia registrada no plano de migração. A união preserva conteúdo único e registra a origem de cada bloco.

## Fonte: `docs/operations/behavioral-analytics.md`

> **Provenance:** migrated from `docs/operations/behavioral-analytics.md` at authoritative commit `5545d9227624400ab8bb707b6032b2f61329a36e`. Content is adapted only for repository boundaries and links.

### Behavioral analytics de agentes

#### Objetivo

Detectar quando o comportamento de um agente muda em relação ao que era normal para ele — e converter esse sinal em ação proporcional.

Regra determinística responde "isto é proibido". Behavioral analytics responde "isto é diferente". As duas são necessárias e não se substituem: ação administrativa sem aprovação é **regra**; custo oito vezes acima do p95 histórico é **anomalia**.

#### Unidade de comportamento

Escolha explicitamente o que está sendo perfilado: `agent_id`, agente + usuário, sessão, time ou peer group. Para agentes autônomos, `agent_id` é obrigatório — sem isso não há atribuição.

#### Features observáveis

Chamadas de ferramenta por minuto · ferramentas únicas · proporção de escrita · ações falhas · profundidade de retry · profundidade de cadeia · tokens por sessão · custo por sessão · amplitude de fontes acessadas · uso de privilégio · egress externo · latência · tentativas de contornar aprovação.

Escolha poucas features com significado operacional. Uma feature que ninguém sabe interpretar produz alerta que ninguém trata.

#### Baseline

- **baseline individual** (o agente contra o próprio histórico) evita comparar um agente de alto volume com outro de baixo volume;
- **peer-group baseline** ajuda quando há população suficiente de agentes com função semelhante;
- período inicial em **monitor-only** de no mínimo 30 dias, ou um ciclo operacional que capture sazonalidade;
- combine **desvio relativo com piso absoluto**: "5x o p95" sozinho dispara em um aumento de 1 para 5 chamadas, sem relevância;
- baselines são **versionados por release** do agente. Mudança material pode exigir novo período de aprendizagem.

#### Contexto antes de conclusão

Um desvio isolado pode ser perfeitamente legítimo. Enriqueça o sinal com: tier, janela de mudança ou manutenção, owner, versão do deployment, evento de negócio, risco da ferramenta e classe da fonte de dados.

Anomalia de custo isolada costuma ser aumento legítimo de uso. Anomalia de custo **combinada** com mudança de comportamento de ferramenta e ausência de change record é candidata a incidente.

#### Catálogo inicial de casos

| Caso | Sinal | Contexto a correlacionar | Resposta inicial |
|---|---|---|---|
| runaway loop | chamadas/min e profundidade de retry muito acima do baseline | janela de mudança | throttle + alerta; quarentena em T3 se crítico |
| deriva de privilégio | uso de ferramenta privilegiada nunca vista no histórico | tier e risco da ferramenta | exigir aprovação + investigar |
| anomalia de custo | custo/sessão acima do baseline e do piso absoluto | volume de negócio, versão do modelo | alerta; throttle em T2/T3 |
| expansão de acesso a dados | nova fonte ou aumento de amplitude | autorização vigente e change record | validar autorização + revisar mudança |
| mudança após release | alteração abrupta depois de update de modelo, prompt ou ferramenta | diff de versão | comparar versões; candidato a rollback |
| manipulação de aprovação | eventos repetidos de falha ou bypass de aprovação | histórico do ator | bloquear ação + incidente de segurança |

#### Escala de resposta

`observe` → `alert` → `throttle` → `exigir step-up` → `desabilitar ferramenta` → `quarentena`

Comece com resposta humana para casos novos. Só automatize contenção depois de medir precisão e falsos positivos em casos de alta confiança.

#### Procedimento

1. Escolher um caso observável e útil — runaway loop, pico de custo, primeira ferramenta privilegiada ou acesso a alvo incomum.
2. Definir as features e a unidade de comportamento.
3. Construir baseline individual e, quando útil, de peer group.
4. Rodar monitor-only por período suficiente para capturar sazonalidade.
5. Combinar desvio relativo com piso absoluto.
6. Enriquecer com contexto operacional.
7. Definir resposta por severidade.
8. Medir taxa de falso positivo e incidentes não detectados; ajustar.
9. Versionar regra e baseline — o incidente precisa indicar qual lógica gerou a decisão.

Use o [Behavioral Analytics Use Case](behavioral-analytics-use-case.md) para registrar hipótese, features, privacy boundaries, thresholds, response contract, calibração e sunset. Os sinais podem usar o [audit event envelope](../schemas/audit-event.schema.json) como contrato mínimo.

#### Evidências

- catálogo de casos com features, thresholds e rationale;
- baselines versionados por release;
- período de monitor-only e evidência de calibração;
- decisões automatizadas com a versão da regra que as produziu;
- histórico de tuning com falsos positivos e incidentes correlacionados.

#### Métricas

- casos em monitor-only versus em enforcement;
- taxa de falso positivo por regra;
- incidentes detectados por behavioral analytics versus por outra via;
- tempo entre sinal e ação;
- regras sem revisão dentro do ciclo definido;
- agentes sem baseline válido após mudança material.

#### Failure modes

- automatizar bloqueio com baseline imaturo;
- desvio relativo sem piso absoluto;
- alertar sem contexto e treinar a operação a ignorar;
- baseline global aplicado a agentes de perfis incompatíveis;
- regra não versionada — impossível explicar por que a ação ocorreu;
- tratar analytics como substituto de regra determinística para o que já é proibido.

#### Decision gate

Nenhuma regra de comportamento entra em enforcement automático sem período de monitor-only, medição de falso positivo, piso absoluto declarado e versionamento da regra e do baseline.


## Fonte: `templates/behavioral-analytics-use-case.md`

> **Provenance:** migrated from `templates/behavioral-analytics-use-case.md` at authoritative commit `5545d9227624400ab8bb707b6032b2f61329a36e`. Content is adapted only for repository boundaries and links.

### Behavioral Analytics Use Case

Behavioral analytics só é governança quando um sinal possui owner, threshold, decisão e ação. Use monitor-only até conhecer falsos positivos e efeitos sobre pessoas.

#### Caso

| Campo | Valor |
| --- | --- |
| use case ID | |
| agent population/scope | |
| risk hypothesis | |
| expected behavior | |
| owner | |
| Run Authority | |
| privacy/worker authority | |
| mode | design / monitor-only / enforce |

#### Sinais e features

| Signal/feature | Source | Granularity | Retention | Data class | Known bias/limitation |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Não use conteúdo sensível quando metadado suficiente responder à hipótese. Documente atributos que não podem ser usados para inferência sobre pessoas.

#### Baseline e detecção

| Elemento | Definição |
| --- | --- |
| baseline population/window | |
| peer grouping | |
| threshold/model | |
| minimum sample | |
| seasonality handling | |
| cold-start behavior | |
| confidence requirement | |

#### Decision and response contract

| Severity | Condition | Owner | Automated action | Human decision | SLA | Evidence preserved |
| --- | --- | --- | --- | --- | --- | --- |
| info | | | none | review trend | | |
| warning | | | rate-limit/step-up only if approved | triage | | |
| critical | | | contain according to runbook | Run Authority disposition | | |

#### Calibration

| Período | Alerts | True positives | False positives | Unknown | Missed events | Threshold change |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| | | | | | | |

**Promotion criteria de monitor-only para enforce:**

- [ ] false-positive rate conhecido e aceitável
- [ ] impact assessment concluído quando pessoas podem ser afetadas
- [ ] response action testada e reversível
- [ ] override, appeal e escalation definidos
- [ ] owner e SLA operacionais
- [ ] retention/minimization aprovadas

#### Review e sunset

| Campo | Valor |
| --- | --- |
| effectiveness metric | |
| next review | |
| change triggers | |
| disable/sunset criteria | |
| decision ref | |

**Limitações e usos proibidos:**

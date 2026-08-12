# Template — Ferramenta de classificação de risco (risk scoring worksheet)

Worksheet operacional que transforma o pre-screen em **tier, admissibilidade e rota de reviews**. Aplica as sete dimensões de scoring, os red flags e o impact trigger definidos no [cap. 04](../../docs/framework/04-risk-impact-and-compliance.md). **A lógica normativa vive no capítulo; esta ferramenta executa e registra o resultado.**

> **Calibração antes de usar em escala:** os thresholds e as faixas abaixo são ponto de partida. Calibre com 20–30 casos reais, aprove e versione — como qualquer parâmetro do framework. Depois de calibrado, o scoring automático pode substituir o manual nos casos sem red flags.

## 1. Identificação

- Agent ID:
- Nome do agente:
- Responsável pela classificação:
- Data:
- Versão do modelo de risco aplicada:

## 2. As sete dimensões de scoring

Para cada dimensão, marque a linha que descreve o caso. Pontuação: 0 a 3 por dimensão, **21 pontos possíveis no total** (7 dimensões).

| Dimensão | 0 | 1 | 2 | 3 | Pontos |
|---|---|---|---|---|---|
| **Sensibilidade dos dados** | públicos | internos | confidenciais | restritos/regulatórios | |
| **Autonomia** | assistivo | sugere | executa limitado | planeja/executa autônomo | |
| **Impacto da ação** | leitura | escrita reversível | escrita material | irreversível/alto impacto | |
| **Privilégio** | escopo do usuário | serviço com escopo | elevado | admin/privilegiado | |
| **Alcance** | usuário único | time | corporativo | externo/público | |
| **Conectividade externa** | nenhuma | interna aprovada | externa aprovada | externa aberta/dinâmica | |
| **Criticidade do negócio** | baixa | moderada | importante | crítica | |

**Score total (0–21):**

## 3. Red flags (nunca diluídos pelo score)

Marque os que se aplicam. Qualquer um acionado **impõe a criticidade mínima da tabela** e remove o caso do fast path, independentemente do score total.

| Red flag | Criticidade mínima | Aplicável? |
|---|---|---|
| dados restritos enviados a provedor externo | T4 + admissibilidade `restricted` por padrão | ☐ |
| descoberta irrestrita de tools/MCP externos em runtime | T4 + `restricted` por padrão | ☐ |
| execução de código ou comandos arbitrários | T4 | ☐ |
| deleção irreversível ou mudança destrutiva | T4 | ☐ |
| modificação de identidade, permissão ou secrets | T3 | ☐ |
| acesso privilegiado ou administrativo | T3 | ☐ |
| decisão sobre emprego, crédito, elegibilidade ou acesso a serviço | T3 | ☐ |
| processo safety-critical ou de tecnologia operacional | T3 | ☐ |
| execução de transação financeira material | T3 | ☐ |
| comunicação pública autônoma em escala, sem revisão humana | T3 | ☐ |

## 4. Tier resultante

A regra: **o maior entre o score calculado e a criticidade mínima imposta por red flags.** O red flag é piso, não teto.

| Faixa de score | Tier pelo score | Tier final (com red flags) |
|---|---|---|
| 0–6 | T1 | o maior entre o score e os red flags aplicados |
| 7–12 | T2 | idem |
| 13–18 | T3 | idem |
| 19–21 | T4 (raro; quase sempre há red flag junto) | idem |

**Tier final:** `T___` — **Rationale** (score, dimensões dominantes, red flags aplicados):

## 5. Admissibilidade

`permitted` / `conditional` / `restricted` / `prohibited` — com rationale e, quando `conditional` ou `restricted`, condições, authority e expiry.

- Admissibilidade:
- Condições:
- Authority:
- Expiry:

## 6. Impact trigger (Responsible AI)

O agente influencia **direitos, oportunidades, decisões sobre pessoas, segurança física, comunicação pública ou processo regulado?**

- ☐ Sim → executar [RAI impact assessment](self-assessment-form.md) formal, mesmo em caso tecnicamente simples.
- ☐ Não → registrar o rationale.

## 7. Domain reviews acionadas

Marque apenas as que têm gatilho — review acionada por regra fixa vira fila e morre.

| Review | Gatilho | Acionada? | Owner |
|---|---|---|---|
| Privacidade | dados pessoais/sensíveis | ☐ | |
| Segurança | privilégio elevado, execução de código, secrets | ☐ | |
| Dados | fontes novas ou não certificadas | ☐ | |
| Arquitetura | mudança de pattern, multi-agente | ☐ | |
| Jurídico | obrigação regulatória aplicável | ☐ | |
| Comercial/compras | fornecedor novo ou SaaS com dados | ☐ | |

## 8. Encaminhamento

| Campo | Valor |
|---|---|
| Rota | `fast path` / `padrão` / `formal` |
| Controls obrigatórios (MPB do tier) | |
| RAI impact assessment requerido | sim / não |
| Domain reviews abertas | |
| Gaps com owner e prazo | |
| Próxima ação | |

## 9. Registro

Este worksheet é evidência: arquive com data, responsável e versão do modelo de risco. O resultado final (tier, admissibilidade, decisão) entra no [Agent Risk Record](agent-risk-record.md), no registry e no blueprint — conforme o [mapa de decisão](../../docs/framework/04-risk-impact-and-compliance.md#o-mapa-de-decisão-como-risco-rai-e-aprovação-se-encadeiam).

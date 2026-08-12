# Template — Autoavaliação de agente de IA

Preencha antes de solicitar aprovação de design, release ou mudança material. Respostas sem evidência devem ser marcadas como `missing`, não presumidas como atendidas.

## 1. Identificação e finalidade

- Agent ID:
- Nome:
- Versão do blueprint:
- Business owner:
- Technical owner:
- Finalidade autorizada:
- Usuários e regiões:
- Outcome esperado e métrica:
- Usos explicitamente proibidos:

## 2. Alcance, dados e impacto

- Processos ou direitos afetados:
- Sistemas e integrações:
- Categorias e classificação dos dados:
- Origem, qualidade e retenção dos dados:
- População e volume estimados:
- Impactos sobre pessoas, finanças, operações e reputação:
- Tier de risco proposto e rationale:

## 3. Autonomia, tools e autoridade

Para cada tool ou ação, registre capability, scopes, condição de uso, reversibilidade, approval mode e enforcement técnico.

| Tool/ação | Capability | State-changing | Scopes | Reversível | Aprovação | Gateway/controle |
|---|---|---|---|---|---|---|
| | | | | | | |

- Decision rights aplicáveis:
- Human accountability boundary:
- Segregation of duties:
- Kill switch, quarantine e rollback:
- Ações que o agente não pode executar:

## 4. Controls e evidências

| Control ID | Implementação | Owner | Evidência | Status |
|---|---|---|---|---|
| | | | | `missing` |

- Evidence package:
- Exceptions abertas, owner e expiry:
- Riscos residuais e autoridade de aceitação:

## 5. Evaluation e release

- Testes funcionais e de integração:
- Prompt injection e conteúdo adversarial:
- Exfiltração, acesso indevido e isolamento:
- Qualidade, safety, fairness e human oversight aplicáveis:
- Tool-use, autorização e ações inesperadas:
- Cenários de falha, rollback e recuperação:
- Release evidence e disposition:

## 6. Operação e lifecycle

- Logs, métricas, alertas e retenção:
- Thresholds de containment:
- Incident owner e escalation path:
- Frequência de review e attestation:
- Critérios de suspensão, reativação e sunset:

## 7. Disposition

- Gate solicitado:
- Decisão: `approved` / `conditional` / `rejected` / `expired`
- Decision authority:
- Condições e prazo:
- Evidence refs:

## 8. Score de prontidão (agent assessment score)

O score mede **quão completo e evidenciado** está este dossiê. Ele **não** mede risco (isso é o tier) e **não** mede qualidade do agente (isso é evaluation). A regra normativa está no [cap. 07](../../docs/framework/07-evaluation-evidence-and-assurance.md).

**Como pontuar:** cada item das seções 1–7 vale pontos pelo peso da sua categoria. Preenchido **com evidência recuperável** = pontos cheios. Preenchido **sem evidência** = metade. `missing` = zero. Some os pontos obtidos e divida pelo total possível da categoria; o score final é a média ponderada das categorias.

| Categoria | Itens a pontuar | Peso | Pontos obtidos | Pontos possíveis |
|---|---|---|---|---|
| Identificação e finalidade (seção 1) | cada campo obrigatório | 1 | | |
| Alcance, dados e impacto (seção 2) | cada campo obrigatório | 2 | | |
| Autonomia e autoridade (seção 3) | cada tool/ação + cada campo obrigatório | 2 | | |
| Controls e evidências (seção 4) | cada control com evidência | 2 | | |
| Evaluation e release (seção 5) | cada teste com evidência | 2 | | |
| Operação e lifecycle (seção 6) | cada campo obrigatório | 2 | | |
| **Itens críticos** (qualquer um dos abaixo) | — | 3 | — | — |

**Itens críticos** — `missing` em qualquer um é **bloqueador**, independentemente do score total:

- business owner e technical owner nomeados e vivos;
- classificação dos dados e destino de processamento;
- HITL definido quando há ação state-changing;
- kill switch com owner e método testado;
- testes mínimos (prompt injection, exfiltração, tool-use) com evidência.

**Resultado:**

| Campo | Valor |
|---|---|
| Score de prontidão (0–100) | |
| Bloqueadores ativos (sim/não) | |
| Threshold do tier proposto | T1 ≥ 70 · T2 ≥ 80 · T3 ≥ 90 · T4 = 100 + zero bloqueadores |
| Apto para o gate? (sim/não) | |

**Regra de leitura:** um score abaixo do threshold do tier significa **voltar ao trabalho**, não "aprovar com observações". Um score alto com item crítico `missing` continua **bloqueado**. Um score baixo com bloqueador resolvido sobe na próxima avaliação — o score é um instantâneo datado, não uma nota permanente.

Use a [policy modular](../../docs/framework/00-document-control.md), o [operating model](../../docs/framework/02-governance-and-accountability.md), o [playbook](../../docs/framework/08-implementation-and-adoption.md) e os [schemas](../schemas/README.md) como referências correntes.

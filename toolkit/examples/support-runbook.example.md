# Exemplo de runbook de suporte — Service Desk Knowledge Agent

> Fictício e sanitizado.

## Responsabilidades (ownership)

- Business owner: Example Business Owner
- Technical owner: Example Technical Owner
- Run owner: Example Run Owner

## Sinais e ações

| Sinal | Primeira ação | Escalonamento |
|---|---|---|
| fonte aprovada indisponível | interromper resposta ancorada e informar o analista | Knowledge Owner |
| solicitação de dados proibidos | recusar e registrar sinal de segurança | Security and Data Owner |
| resposta não suportada repetida | colocar a versão afetada em quarentena | Run Authority |
| chamada de ferramenta inesperada | gateway nega, quarentena e preserva evidência | Security and Run Authority |

## Recuperação

1. registrar versão, correlação de sessão e escopo afetado;
2. revogar acesso às ferramentas ou bloquear novas sessões;
3. preservar evidências autorizadas com payload sensível redigido;
4. identificar causa e ação corretiva;
5. executar a suíte de regressão;
6. exigir evidência da Run e Design Authority antes da reativação.

## Fronteiras

Este runbook é ilustrativo e não substitui o processo de incidentes da organização, o modelo de plantão (on-call) ou obrigações legais.

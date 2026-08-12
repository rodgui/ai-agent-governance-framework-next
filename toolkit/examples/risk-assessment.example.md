# Exemplo de avaliação de risco — Service Desk Knowledge Agent

> Fictício e sanitizado. Não é opinião legal, certificação ou aceite de risco real.

## Escopo

- Versão: 1.0
- Usuários pretendidos: analistas internos de service desk
- Capacidades: recuperação aprovada e criação de rascunho
- Proibido: mudanças de sistema, dados pessoais, credenciais e respostas externas não revisadas

## Classificação

| Dimensão | Observação | Classificação |
|---|---|---|
| Dados | conhecimento interno aprovado; sem dados pessoais pretendidos | moderada |
| Capacidade de ação | somente leitura e rascunho; sem mutação de sistema | baixa |
| Alcance | analistas internos de uma unidade operacional | moderado |
| Reversibilidade | sessões podem ser bloqueadas e o blueprint revertido | alta |
| Interconectividade | um gateway e um serviço de recuperação | moderada |

**Tier ilustrativo:** T2.

## Controles obrigatórios

- `AGF-REG-001`
- `AGF-IDN-001`
- `AGF-DAT-001`
- `AGF-EVA-001`
- `AGF-OPS-001`

## Lacunas residuais e decisão

- A autorização do conector deve ser retestada após mudança de fonte de dados.
- Qualquer ferramenta que altere estado ou expansão de usuários externos dispara reavaliação.
- Risco residual: moderado, aceito somente para este escopo fictício e corte de evidências.

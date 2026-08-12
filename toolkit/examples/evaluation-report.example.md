# Exemplo de relatório de avaliação — Service Desk Knowledge Agent

> Fictício e sanitizado. Os resultados demonstram a estrutura do relatório, não o desempenho do modelo.

## Contrato de avaliação

- Versão do blueprint: 1.0
- Corte de evidências: 2026-08-01
- Dataset: 40 perguntas sintéticas de procedimentos internos
- Fatias (slices): consulta rotineira, solicitação ambígua, solicitação de dados proibidos, injeção de prompt e fonte indisponível

## Resultados ilustrativos

| Teste | Threshold | Resultado | Decisão |
|---|---:|---:|---|
| cobertura de citações | ≥ 95% | 97,5% | pass |
| precisão de resposta ancorada | ≥ 90% | 92,5% | pass |
| recusa de dados proibidos | 100% | 100% | pass |
| contenção de injeção de prompt | 100% | 100% | pass |
| abstenção por fonte indisponível | ≥ 95% | 95% | pass |

## Limitações

- Dados sintéticos não representam toda solicitação de produção.
- Nenhum dado pessoal ou credencial de produção foi usado.
- Resultados aprovados aplicam-se somente à versão e configuração avaliadas.

## Descobertas (findings)

- Adicionar caso de regressão para fontes aprovadas conflitantes antes de expansão material.
- Reexecutar após mudança de modelo, conector, contrato de dados ou ferramenta.

# Maturity assessments

Este diretório organiza avaliações de capacidade organizacional baseadas no [`maturity model`](../../maturity/maturity-model.md). Maturidade não mede o risco de um agente e não certifica conformidade.

## Artefatos requeridos

- escopo, unidades, data de corte e versão do método;
- evidence register com referências recuperáveis;
- população, amostra, coverage e limitações;
- score 0–4 por dimensão, rationale e confidence;
- reviewer disposition e conflitos declarados;
- target state, dependências e roadmap aprovado.

Sem evidência suficiente, use o menor nível demonstrado e confidence baixa. Comparações entre períodos só são válidas com método, escopo e coverage compatíveis. O schema e o exemplo canônicos estão em [`../../schemas/maturity-assessment.schema.json`](../../schemas/maturity-assessment.schema.json) e [`../../examples/maturity-assessment.example.json`](../../examples/maturity-assessment.example.json).

> **Migration note:** a origem continha apenas `assessments/maturity-assessments/.gitkeep`; este documento é scaffold operacional novo.

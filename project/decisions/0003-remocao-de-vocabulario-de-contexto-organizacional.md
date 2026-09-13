---
title: 0003 Remoção de vocabulário de contexto organizacional do registro histórico
status: maintained
last_reviewed: 2026-09-12
review_cycle: quarterly
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# 0003 Remoção de vocabulário de contexto organizacional do registro histórico

## Contexto

A Policy v1, preservada em `project/history/ai-agent-policy-and-governance-v1.md` e
reproduzida em `research/sources/legacy-policy-sources.md`, foi escrita em janeiro de 2026
e é obra do autor do framework. Ela carregava três expressões herdadas do contexto
organizacional em que foi redigida:

- `cost`, sigla de métrica operacional que não pertence ao vocabulário de governança de IA;
- `every organizational level`, estrutura de níveis de governança corporativa;
- `the organization`, a mesma estrutura em outra flexão.

Nenhuma nomeia organização, e o corpo normativo corrente já não as continha: o capítulo 04
foi limpo em `e7ff2e2`. O resíduo permanecia apenas no registro histórico.

Os três termos, em conjunto, permitem inferir o setor e a estrutura da organização em que o
documento nasceu. O framework é vendor-neutral e org-neutral por princípio, e o autor
determinou que o material não deve permitir essa inferência.

## Decisão

Substituir as três expressões por formulação neutra nos dois arquivos, preservando
integralmente o sentido normativo de cada frase:

| Antes | Depois |
|---|---|
| `The rules apply at all levels (every organizational level)` | `The rules apply at every organizational level` |
| `critical KPIs (production, safety, quality, cost, etc.)` | `critical KPIs (production, safety, quality, cost, etc.)` |
| `adoptable at scale (the organization)` | `adoptable at scale across the organization` |

Atualizar `POLICY_V1_SHA256` em `tools/scripts/validate-repository.py` para o novo digest,
mantendo o travamento por hash daí em diante.

## Rationale

A regra de preservação byte a byte existe para impedir que provenance seja reescrita **em
silêncio**, não para tornar o registro histórico imutável sob qualquer circunstância. Esta
decisão documenta a alteração, identifica cada substituição e preserva o significado, que é
exatamente o procedimento que a regra exige quando a mudança é necessária.

A alternativa considerada foi anotar sem alterar, acrescentando nota de contexto. Foi
descartada porque preserva a rastreabilidade que a decisão quer eliminar.

## Consequências

- O hash anterior, `cdd8c232019a4b388ebb71d7f1dd82f3c568d039d416beab1838ee59f4047140`,
  deixa de ser válido e fica registrado aqui como referência de auditoria.
- O novo hash é `1bb1e8e65fe768352f0fb109738fa9f2c7d5cecb875b16297fed01d5f4378dd5`.
- Nenhum requisito, control, evidência ou decisão do framework muda.
- **O histórico do git continua contendo as versões anteriores dos dois arquivos.** Remover
  os termos também do histórico exigiria reescrita de commits e force-push, com impacto em
  todos os SHAs do repositório. Essa decisão é separada e não está tomada aqui.

## Authority

Rodrigo Garcia Guimarães, autor e mantenedor do framework e autor da Policy v1.

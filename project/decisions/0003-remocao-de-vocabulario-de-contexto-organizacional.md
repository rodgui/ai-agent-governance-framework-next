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
e é obra do autor do framework.

Uma revisão de rastreabilidade identificou três expressões herdadas do contexto
organizacional em que o documento foi redigido: uma sigla de métrica operacional e duas
formulações de estrutura de níveis de governança corporativa. Nenhuma nomeia organização,
e o corpo normativo corrente já não as continha, tendo sido limpo em `e7ff2e2`. O resíduo
permanecia apenas no registro histórico.

Em conjunto, as três permitiam inferir o contexto de origem do documento. O framework é
vendor-neutral e org-neutral por princípio, e o autor determinou que o material não deve
permitir essa inferência.

## Decisão

Substituir as três expressões por formulação neutra nos dois arquivos, preservando
integralmente o sentido normativo de cada frase. As substituições são verificáveis no diff
do commit que aplica esta decisão e não são reproduzidas aqui, porque reproduzi-las
recriaria a rastreabilidade que a decisão elimina.

Atualizar `POLICY_V1_SHA256` em `tools/scripts/validate-repository.py` para o novo digest,
mantendo o travamento por hash daí em diante.

## Rationale

A regra de preservação byte a byte existe para impedir que provenance seja reescrita **em
silêncio**, não para tornar o registro histórico imutável sob qualquer circunstância. Esta
decisão documenta a alteração, declara a authority e registra o hash anterior, que é o
procedimento que a regra exige quando a mudança é necessária.

A alternativa considerada foi anotar sem alterar, acrescentando nota de contexto ao
arquivo. Foi descartada porque preserva exatamente a rastreabilidade que a decisão quer
eliminar.

## Consequências

- O hash anterior, `cdd8c232019a4b388ebb71d7f1dd82f3c568d039d416beab1838ee59f4047140`,
  deixa de ser válido e fica registrado como referência de auditoria.
- O novo hash é `1bb1e8e65fe768352f0fb109738fa9f2c7d5cecb875b16297fed01d5f4378dd5`.
- Nenhum requisito, control, evidência ou decisão do framework muda.
- **O histórico do git continua contendo as versões anteriores dos dois arquivos**, assim
  como as mensagens de commit e as descrições de pull request da época. Remoção completa
  exigiria reescrita de histórico e force-push, com impacto em todos os SHAs do
  repositório. Essa decisão é separada e não está tomada aqui.

## Authority

Rodrigo Garcia Guimarães, autor e mantenedor do framework e autor da Policy v1.

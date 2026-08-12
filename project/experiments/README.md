---
title: Experiments
status: maintained
last_reviewed: 2026-08-11
review_cycle: quarterly
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# Experiments
Este artefato consolida fontes validadas segundo a estratégia registrada no plano de migração. A união preserva conteúdo único e registra a origem de cada bloco.

## Fonte: `experiments/README.md`

> **Provenance:** migrated from `experiments/README.md` at authoritative commit `5545d9227624400ab8bb707b6032b2f61329a36e`. Content is adapted only for repository boundaries and links.

### Experiments

Área para hipóteses e provas técnicas não canônicas.

#### Regras

1. todo experimento declara hypothesis, scope, owner e expiry;
2. environments e data são não produtivos ou explicitamente autorizados;
3. secrets são proibidos; use `[REDACTED]`;
4. output experimental não é control evidence até revisão e promoção;
5. resultado negativo e limitation são preservados;
6. experimento expirado é arquivado ou removido;
7. promoção exige documentação canônica, tests e decision authority.

Use o [experiment template](experiment-template.md). Experiments não alteram a policy modular, não criam requisito normativo e não constituem endorsement de fornecedor.

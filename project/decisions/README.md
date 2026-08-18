# Architecture Decision Records

Este diretório registra decisões arquiteturais do repositório reconstruído. Decisões históricas continuam no [índice de `source-history`](source-history/README.md) e não governam automaticamente a árvore normalizada.

## Decisões correntes

- [`0001-canonical-source-and-product-boundaries.md`](0001-canonical-source-and-product-boundaries.md) — fonte canônica, neutralidade e separação do conteúdo comercial;
- [`0002-derived-documentation-build-and-publication.md`](0002-derived-documentation-build-and-publication.md) — site derivado e publicação manual fora do Gate 1.
- [`0004-framework-guidance-acceptance-adr-0013-0015.md`](0004-framework-guidance-acceptance-adr-0013-0015.md) — aceitação simulada, condicional e vendor-neutral das ADRs 0013–0015 como guidance do framework; não é operational validation de consumidores.

## Regras

Cada ADR declara contexto, decisão, consequências, relação de supersession e critério verificável. Uma decisão histórica só permanece normativa quando a decisão corrente a incorpora explicitamente. Mudanças de schema, IDs, gates, licenças ou product boundary exigem ADR e validação de migração.

> **Migration note:** o path de origem continha apenas `docs/architecture/decisions/.gitkeep`; este índice é scaffold novo e não atribui conteúdo substantivo ao placeholder.

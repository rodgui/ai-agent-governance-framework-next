# ADR-0002 — Build derivado e publicação manual

- **Status:** Accepted
- **Date:** 2026-08-11
- **Supersedes:** source ADR-0008 only within this reconstructed repository

## Decision

Markdown e contratos estruturados são canônicos. O site é build derivado e reproduzível. Publicação é opcional, manual e exige autorização externa ao Gate 1; workflows locais/PR não criam remote nem publicam.

## Validation

`python tools/build-docs-site.py` deve passar; o script invoca MkDocs em modo `--strict` e não pode modificar o corpus canônico.

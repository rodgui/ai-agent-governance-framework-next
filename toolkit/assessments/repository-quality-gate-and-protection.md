---
title: Repository quality gate and main protection
type: assessment
status: maintained
maturity: observed
last_reviewed: 2026-08-18
review_cycle: quarterly
owners: [repository-maintainers]
related:
  - ../../.github/workflows/quality-gates.yml
  - ../../ROADMAP.md
---

# Repository quality gate and main protection

> **Evidence cutoff:** 2026-08-18. Este assessment registra configuração observada via GitHub API; não é policy de segurança de repositório nem substitui a configuração remota.

## 1. Baseline

Antes do closeout, `main` estava sem branch protection (`HTTP 404: Branch not protected`) e sem rulesets (`[]`). O GitHub Actions tinha dois workflows de PR com job `validate`, e o PR #5 havia sido merged apesar de `Quality gates` remoto em `failure`.

## 2. Fonte canônica do quality gate

O repositório mantém um único workflow canônico: `.github/workflows/quality-gates.yml`. A interface do GitHub exibe o check como **Quality gates / Canonical repository quality gate** (workflow/job), enquanto o check run e o required status context armazenado pelo GitHub usam o nome técnico **Canonical repository quality gate**. O workflow cobre Markdownlint changed files, repository validator, unit/negative/semantic/ADR tests via discovery, Ruff, `py_compile`, MkDocs build, deterministic rendering e `git diff --check`.

O antigo `.github/workflows/validate.yml` foi removido em T23 por duplicar responsabilidade sem adicionar uma capability distinta.

## 3. Configuração remota observada após T27

A branch `main` foi protegida via GitHub API com os seguintes parâmetros:

| Controle | Estado |
|---|---|
| Changes via Pull Request | Obrigatório pelo bloco `required_pull_request_reviews` |
| Required status context | `Canonical repository quality gate` |
| GitHub UI display | `Quality gates / Canonical repository quality gate` |
| Strict required checks | Habilitado; branch deve estar atualizada |
| Required reviewer count | `0`; PR é obrigatório sem criar deadlock de reviewer para repositório de owner único |
| Enforce admins | Habilitado |
| Force push | Bloqueado |
| Deletion de main | Bloqueada |
| Conversation resolution | Obrigatória |
| Required linear history | Não habilitada; não é necessária para o objetivo desta rodada |
| Rulesets | Nenhum; a proteção usa branch protection clássica |
| Automerge | Não habilitado por esta rodada |

O objetivo operacional é **NO GREEN CI → NO MERGE**. A configuração impede o bypass normal por merge sem PR ou sem o check requerido. A efetividade esperada foi reobservada no PR #7, sem transformar essa observação em assurance absoluta da plataforma.

## 4. Evidence observada após o PR #7

| Campo | Observação |
|---|---|
| Pull request | PR #7 — synthetic ADR promotion validation case |
| Head SHA | `86149945f0bfcd6f72eea0819070ace4c0f423a3` |
| Workflow run | `32175015315` — `Quality gates`, evento `pull_request` |
| Check/job | `Canonical repository quality gate` |
| Conclusão | `success` |
| Merge observado | PR #7 merged em `d72e756c6d761058aaa13a3d89fea78971cb2499` |
| Push subsequente em main | Run `32175176730`, `Quality gates`, `success` |
| Enforcement observado | O PR foi merged com o required status context técnico concluído com sucesso; a proteção remota permaneceu ativa no estado descrito acima. |

Esta é evidence observada do enforcement esperado em um PR específico. Ela não demonstra assurance absoluta da plataforma, nem garante comportamento futuro após mudanças de settings, owner, default branch ou workflow.

## 5. Limitações

A proteção remota é state externo ao repositório e deve ser auditada novamente se settings, owner, default branch ou workflow name mudarem. O check só pode ser declarado verde quando o GitHub Actions produzir conclusão `success`; o baseline histórico permanece `REMOTE_CI_FAILURE`.

## References

- [GitHub REST API — Update branch protection](https://docs.github.com/en/rest/branches/branch-protection#update-branch-protection)
- Workflow observado: `.github/workflows/quality-gates.yml`.
- [T22 CHANGELOG evidence](../../CHANGELOG.md)

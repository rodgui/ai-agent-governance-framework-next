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

O repositório mantém um único workflow canônico: `.github/workflows/quality-gates.yml`. O workflow tem o job/check inequívoco **Quality gates / Canonical repository quality gate** e cobre Markdownlint changed files, repository validator, unit/negative/semantic/ADR tests via discovery, Ruff, `py_compile`, MkDocs build, deterministic rendering e `git diff --check`.

O antigo `.github/workflows/validate.yml` foi removido em T23 por duplicar responsabilidade sem adicionar uma capability distinta.

## 3. Configuração remota observada após T27

A branch `main` foi protegida via GitHub API com os seguintes parâmetros:

| Controle | Estado |
|---|---|
| Changes via Pull Request | Obrigatório pelo bloco `required_pull_request_reviews` |
| Required status check | `Quality gates / Canonical repository quality gate` |
| Strict required checks | Habilitado; branch deve estar atualizada |
| Required reviewer count | `0`; PR é obrigatório sem criar deadlock de reviewer para repositório de owner único |
| Enforce admins | Habilitado |
| Force push | Bloqueado |
| Deletion de main | Bloqueada |
| Conversation resolution | Obrigatória |
| Required linear history | Não habilitada; não é necessária para o objetivo desta rodada |
| Rulesets | Nenhum; a proteção usa branch protection clássica |
| Automerge | Não habilitado por esta rodada |

O objetivo operacional é **NO GREEN CI → NO MERGE**. A configuração impede o bypass normal por merge sem PR ou sem o check requerido, mas a efetividade deve ser reobservada em um novo PR com run concluído.

## 4. Limitações

A proteção remota é state externo ao repositório e deve ser auditada novamente se settings, owner, default branch ou workflow name mudarem. O check só pode ser declarado verde quando o GitHub Actions produzir conclusão `success`; o baseline histórico permanece `REMOTE_CI_FAILURE`.

## References

- [GitHub REST API — Update branch protection](https://docs.github.com/en/rest/branches/branch-protection#update-branch-protection)
- [GitHub Actions — quality-gates.yml](../../.github/workflows/quality-gates.yml)
- [T22 CHANGELOG evidence](../../CHANGELOG.md)

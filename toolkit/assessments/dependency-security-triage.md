---
title: Dependency security triage
type: assessment
status: under-review
maturity: illustrative
last_reviewed: 2026-08-18
review_cycle: monthly
owners: [repository-maintainers, security]
related:
  - ../../.github/dependabot.yml
  - ../../requirements-ci.txt
  - ../../requirements-docs.txt
  - ../../pyproject.toml
  - ../../uv.lock
---

# Dependency security triage

> **Status:** `NOT_CONFIRMED` para o detalhe alert-by-alert. O repositório mantém uma configuração mínima de Dependabot, mas a lista detalhada de alertas não pôde ser recuperada com a credencial disponível.

## 1. Escopo

Esta triagem cobre dependências Python e GitHub Actions do repositório `ai-agent-governance-framework-next`. Não aplica upgrades automaticamente, não transforma uma versão disponível em versão aprovada e não declara que um alerta foi corrigido sem evidência reproduzível.

## 2. Manifests e ecosystems identificados

| Ecosystem | Manifestos/configuração | Estratégia |
|---|---|---|
| pip/Python | `pyproject.toml`, `requirements-ci.txt`, `requirements-docs.txt`, `uv.lock` | Dependabot semanal, PRs agrupados, validação completa por família de upgrade |
| GitHub Actions | `.github/workflows/quality-gates.yml`, `validate.yml`, `pages.yml` | Dependabot semanal, PRs agrupados, validação do workflow e dos gates |

O lockfile contém versões resolvidas por marcador de Python; por isso, upgrade de dependência deve considerar a matriz de versões e não somente o ambiente local.

## 3. Exposição conhecida e limite de confirmação

Em uma execução remota anterior na branch default, o GitHub reportou **18 vulnerabilidades Dependabot agregadas: 13 high e 5 moderate**. A página pública de segurança está disponível em [Security / Dependabot](https://github.com/rodgui/ai-agent-governance-framework-next/security/dependabot), mas o endpoint de alertas retornou `HTTP 403 Resource not accessible by integration` para a credencial atual.

Sem package, ecosystem, direct/transitive, GHSA/CVE, affected version, fixed version e dependency path, não é seguro afirmar quais alertas são corrigíveis, exploráveis no escopo deste repositório ou relacionados ao runtime publicado. O número agregado é tratado como **sinal de exposição**, não como inventário suficiente para remediation.

| Item exigido pelo plano | Estado | Owner | Próxima evidência |
|---|---|---|---|
| Package/ecosystem | `NOT_CONFIRMED` | repository maintainers | export Dependabot autorizado |
| Direct/transitive e dependency path | `NOT_CONFIRMED` | repository maintainers | dependency graph + lockfile mapping |
| GHSA/CVE, severity e versions | `NOT_CONFIRMED` | Security | alert export ou Security Advisory |
| Relevância/exploitability | `BLOCKED_BY_AUTHORIZED_EVIDENCE` | Security + maintainers | threat/context review |
| Remediation | `BLOCKED_BY_AUTHORIZED_EVIDENCE` | maintainers | minimum safe upgrade + gates |

## 4. Remediação mínima e critérios

Não executar upgrade indiscriminado nesta rodada. Para cada família de alertas, o maintainer deve selecionar a menor versão segura compatível com os manifests e o lockfile, abrir mudança isolada e executar repository validator, JSON Schema/examples/cross-record tests, negative tests, ADR/semantic tests, unit tests, Ruff, Python compile, Markdownlint, MkDocs, rendering, link validation e `git diff --check`.

Um alerta não corrigido exige reason, exposure, compensating measure, owner, review date/expiry e future target version. A remediação só pode ser marcada como `DONE` quando o alert correspondente estiver fechado ou houver evidência equivalente de mitigação aceita pela authority de segurança.

## 5. Decisão atual

- `.github/dependabot.yml` foi criado para `pip` e `github-actions`, os únicos ecosystems identificados.
- Nenhum upgrade de pacote foi aplicado automaticamente.
- A triagem alert-by-alert permanece `NOT_CONFIRMED` até que uma authority forneça acesso ou export dos alertas.
- A estratégia de atualização está versionada e agrupada para evitar ruído excessivo.

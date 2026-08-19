---
title: Dependabot resolution — no product change
type: assessment
status: under-review
maturity: demonstrated-deterministic
last_reviewed: 2026-08-19
review_cycle: weekly
evidence_cutoff: 2026-08-19
assessor: framework-maintainers
independence: pending-owner-review
related:
  - dependabot-pr-triage.md
  - dependency-security-triage.md
  - ../../requirements-ci.txt
  - ../../pyproject.toml
  - ../../.github/workflows/quality-gates.yml
  - ../../.github/workflows/pages.yml
---

# Dependabot resolution — no product change

> Este assessment registra uma onda local de resolução de Dependabot. A onda preserva o conteúdo normativo, a estrutura documental, os schemas, os controls, os risk tiers, o Registry, o package runtime contract e a funcionalidade do framework.

## 1. Decision scope

A mudança autorizada localmente cobre somente CI/tooling e GitHub Actions. O baseline de runtime permanece `requires-python >=3.9`, `jsonschema>=4.22,<5`, `Pillow>=10,<13` e `PyYAML>=6,<7`. Não foi aceita nenhuma mudança de lower bound de runtime.

A análise alert-by-alert continua `NOT_CONFIRMED`/`BLOCKED_BY_AUTHORIZED_EVIDENCE`; nenhum PR é tratado como security remediation. O fechamento remoto dos PRs e a publicação desta branch são passos separados e requerem aprovação explícita.

## 2. Resolution matrix

| PR | Mudança proposta | Disposição local | Ação preparada |
|---:|---|---|---|
| #1 | Pillow `11.3.0` → `12.3.0` agrupado | Duplicate candidate de #12 | Não incorporar; fechar somente após decisão remota sobre #12. |
| #8 | `actions/setup-python` v5 → v7 | Compatibility review | Aplicar em `quality-gates.yml` e `pages.yml`, preservando comandos e inputs; requer quality gate e pages manual. |
| #9 | `actions/upload-artifact` v4 → v7 | Pages workflow review | Aplicar somente em `pages.yml`; requer execução manual e verificação do artifact. |
| #10 | `actions/checkout` v4 → v7 | Compatibility review | Aplicar em `quality-gates.yml` e `pages.yml`, preservando `fetch-depth: 0`; requer quality gate e pages manual. |
| #11 | Ruff `0.15.10` → `0.16.3` | Tooling migration | Aplicar pin e correções mecânicas de lint; manter `BLE001` justificado no validator e testar a suíte completa. |
| #12 | Pillow `11.3.0` → `12.3.0` isolado | Incompatible with current baseline | Não incorporar: Pillow `12.3.0` exige Python `>=3.10`, enquanto o framework suporta `>=3.9`. |
| #13 | PyYAML lower bound `>=6` → `>=6.0.3` | Unjustified contract change | Não incorporar: nenhum requisito de consumidor, security rationale ou incompatibilidade foi demonstrado. |
| #14 | jsonschema lower bound `>=4.22` → `>=4.26.0` | Incompatible with current baseline | Não incorporar: jsonschema `4.26.0` exige Python `>=3.10`, enquanto o framework suporta `>=3.9`. |

## 3. Ruff migration boundary

O Ruff `0.16.3` expôs findings adicionais em testes e tooling. A correção local foi limitada a alterações mecânicas: substituir `getattr`/`setattr` constantes por acesso direto, organizar imports, aplicar correções autofix seguras, tornar executável o teste que já possuía shebang e registrar `BLE001` no bloco que captura erros heterogêneos da biblioteca de schema.

Nenhum finding foi tratado como alteração de regra normativa. A correção não altera output do validator, schemas, controls ou comportamento do framework; ela permite que o contrato de lint atualizado seja executado sem findings.

## 4. Actions boundary

Os updates para `checkout@v7`, `setup-python@v7` e `upload-artifact@v7` preservam nomes de jobs, permissões, `fetch-depth`, `python-version`, comandos, paths, artifact name e condições de erro. A compatibilidade remota ainda requer quality gate no head rebaseado e execução manual de `pages.yml`; o workflow hospedado não prova compatibilidade universal com self-hosted runners.

## 5. Verification executed locally

| Gate | Resultado |
|---|---|
| Repository validator | PASS — 173 Markdown, 25 JSON, 44 controls, 15 domains |
| Test suite | 82 tests — OK |
| Ruff `0.16.3` | All checks passed |
| Python compile | Passed |
| MkDocs build | Completed; 196 files staged into `site_src` |
| Deterministic rendering | Completed for both infographic outputs |
| `git diff --check` | Passed |

Os worktrees descartáveis dos heads originais reproduziram os bloqueios de #12 e #14 na resolução `uv` para Python 3.9. O head de #13 passou validator, 82 testes, Ruff e compile, mas isso não supre a ausência de rationale para elevar lower bound.

## 6. Preservation assertions

Nenhum arquivo em `docs/`, `project/`, `toolkit/` ou schemas foi modificado por esta onda, exceto este assessment e o índice necessário para navegação. Nenhum ID, anchor, control, threshold, risk tier, Registry field, machine-readable enum ou versão `1.1.0` foi alterado. O package runtime contract permaneceu byte-for-byte igual.

## 7. Remote closeout criteria

Antes de fechar PRs remotamente, o maintainer deve confirmar o seguinte:

| PR | Critério de fechamento |
|---:|---|
| #1 | Fechar como duplicado de #12 com rationale e sem merge. |
| #12 | Fechar/hold por incompatibilidade com Python `>=3.9`, sem alterar `requires-python`. |
| #13 | Fechar/deferir por lower-bound sem rationale de contrato ou segurança. |
| #14 | Fechar/hold por incompatibilidade com Python `>=3.9`, sem alterar `requires-python`. |
| #8–#10 | Manter abertos até o PR desta onda produzir check remoto verde; depois decidir merge isolado ou fechamento como substituído. |
| #11 | Manter aberto até o PR desta onda produzir quality gate verde; depois decidir merge do update de tooling ou fechamento do Dependabot original como substituído. |

## 8. Limitations

Esta onda não inventaria alerts, não fecha security alerts, não prova compatibilidade de consumidores externos, não valida self-hosted runners e não autoriza production release. A decisão de mudar o baseline Python para `>=3.10` permanece fora do escopo e exigiria change proposal separado.

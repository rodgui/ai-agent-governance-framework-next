# Baseline da fonte

## Snapshot autoritativo de migração

| Campo | Valor |
|---|---|
| Repositório GitHub | <https://github.com/rodgui/ai-agent-governance-framework> |
| Branch padrão remoto | `main` |
| Commit autoritativo | `5545d9227624400ab8bb707b6032b2f61329a36e` |
| Seleção | Rodgui selecionou explicitamente GitHub/main depois de a cópia local protegida e o GitHub serem encontrados em commits diferentes. |
| Snapshot de trabalho | `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot` |
| Arquivos rastreados | 216 |
| Manifesto agregado de conteúdo rastreado SHA-256 | `18f6803b7e9404a396f8d9202149c508097af914f26552c538ca964ef7e05063` |
| Status do snapshot | clean |
| Registrado em | `2026-08-11T20:16:34-03:00` |

O snapshot autoritativo foi obtido em um clone separado. O repositório local protegido não foi buscado (fetched), puxado (pulled), verificado (checked out) ou modificado de qualquer forma.

## Repositório local protegido

| Campo | Valor |
|---|---|
| Caminho | `/Users/rodgui/Nox/Projects/ai-agent-governance-framework` |
| Commit baseline | `a1a91ba5675f6e0261b86e2991f2093c59fda276` |
| Arquivos rastreados | 199 |
| Manifesto agregado de conteúdo rastreado SHA-256 | `b08b03c5002abed3e2bebdf691e1e729eb4b01375a6e65a61c681871205c507f` |
| Status baseline | clean |

O commit local protegido difere do commit remoto autoritativo selecionado. Ele é retido apenas como checkout local imutável e não é a autoridade de migração.

## Arquivos de evidência

- `source-manifest.csv`: metadados de arquivo para cada arquivo rastreado no snapshot autoritativo.
- `source-manifest.sha256`: manifesto SHA-256 por arquivo do snapshot autoritativo.
- `protected-local-manifest.sha256`: manifesto SHA-256 por arquivo do checkout local protegido.
- `source-baseline.json`: baseline autoritativo legível por máquina.
- `protected-local-baseline.json`: baseline protegido-local legível por máquina.
- `github-releases.json`: releases visíveis no baseline.
- `git-tags.txt` e `git-history-name-status.txt`: evidência de tags e histórico.

## Verificação final de imutabilidade

A validação final deve recalcular independentemente ambos os manifestos e comparar commit, branch, tags e `git status --porcelain` com este baseline. Qualquer diferença é condição de parada e deve ser reportada em vez de reparada silenciosamente.

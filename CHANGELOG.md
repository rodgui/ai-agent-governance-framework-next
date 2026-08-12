# Changelog

Artefato operacional do framework canônico, mantido sob a release `1.1.0` e o source commit `5545d9227624400ab8bb707b6032b2f61329a36e`.

## 2026-08-12 — Publicação automática do site

- O site de documentação (`aiframework.rodgui.com`) agora é publicado automaticamente a cada 30 minutos por um cron na VPS de hospedagem: `git pull` → build MkDocs → rsync para o docroot.
- O deploy é fail-safe: se o build falhar, o site permanece na versão anterior; nada é sincronizado parcialmente.
- Detalhes operacionais em `tools/README.md` e no script `deploy-framework.sh` hospedado na VPS.

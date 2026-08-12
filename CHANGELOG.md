# Changelog

Artefato operacional do framework canônico, mantido sob a release `1.1.0` e o source commit `5545d9227624400ab8bb707b6032b2f61329a36e`.

## 2026-08-12 — Capítulos 04 e 05 reescritos no formato Manual/Bíblia

- Formato aprovado: narrativa primeiro (visão geral, conceitos, fases com armadilhas comuns),
  contrato normativo condensado em tabela no fim, proveniência removida do corpo
  (marcadores machine-readable preservados), blocos EN traduzidos e integrados,
  duplicatas consolidadas via referência cruzada.
- Cap. 04 (Risco): 26 blocos → 20 obrigações (R1–R20); 6 blocos idênticos de avaliação
  de impacto consolidados; regras de uso, self-assessment e blast radius traduzidos.
- Cap. 05 (Lifecycle): 25 blocos → 22 obrigações (R1–R22); 3 duplicatas consolidadas;
  níveis de autonomia L0–L3 traduzidos e integrados.

## 2026-08-12 — Publicação automática do site

- O site de documentação (`aiframework.rodgui.com`) agora é publicado automaticamente a cada 30 minutos por um cron na VPS de hospedagem: `git pull` → build MkDocs → rsync para o docroot.
- O deploy é fail-safe: se o build falhar, o site permanece na versão anterior; nada é sincronizado parcialmente.
- Detalhes operacionais em `tools/README.md` e no script `deploy-framework.sh` hospedado na VPS.

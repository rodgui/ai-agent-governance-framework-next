# Changelog

Artefato operacional do framework canônico, mantido sob a release `1.1.0` e o source commit `5545d9227624400ab8bb707b6032b2f61329a36e`.

## 2026-08-12 — Capítulos 06–10 reescritos no formato Manual/Bíblia

- Cap. 06 (Arquitetura): 1569→583 linhas; 32 blocos → 25 obrigações; 3 duplicatas consolidadas;
  EN traduzido (Multi-Platform Rule, Platform Approval); playbooks de identidade/dados/modelos/tools/segurança integrados.
- Cap. 07 (Avaliação): 789→336 linhas; 26 blocos → 25 obrigações; evidence pack por tier,
  audit universe e pirâmide de avaliação integrados à narrativa.
- Cap. 08 (Implementação): 1571→329 linhas; 27 blocos → 16 obrigações; 6 fundações idênticas
  consolidadas; gates G0-G7, capability map e roadmaps 90d/24s integrados.
- Cap. 09 (Operações): 553→285 linhas; 23 blocos → 18 obrigações; 3 pares de duplicatas
  consolidadas; incident lifecycle, containment ladder e behavioral analytics integrados.
- Cap. 10 (Métricas): 402→254 linhas; 20 blocos → 19 obrigações; FinOps e KPI/KRI/dashboard integrados.

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

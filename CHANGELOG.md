# Changelog

Artefato operacional do framework canônico, mantido sob a release `1.1.0` e o source commit `5545d9227624400ab8bb707b6032b2f61329a36e`.

## 2026-08-17 — Walkthrough G1/G2/G3/G4: pattern fit e iteration policy

- Dois casos fictícios foram exercitados: `workflow` primary com `supervisory-multi-agent` secondary e `iterative-reasoning` primary com `workflow` secondary.
- O walkthrough confirmou cobertura suficiente para architecture pattern versus orchestration pattern, delegation attenuation, cross-plane arbitration, AI-native observability e exit/missing evidence.
- O G3 recebeu `iterationPolicy` para registrar max iterations, retry/refinement budget, loop termination, escalation trigger, owner e evidence quando `iterative-reasoning` estiver presente.
- O blueprint schema, controls, risk tiers, MPB, registry e release não foram alterados. Substitution, replay, deletion e cardinality/cost drills permanecem evidence gaps.
- Esta entrada descreve alterações locais pendentes de validação, revisão e publicação; não altera, por si só, a release ou a baseline publicada.

## 2026-08-17 — Segunda revisão crítica Gartner: pattern fit e integridade arquitetural

- Corrigida a colisão de namespace: a ADR G1 foi renumerada de `0011` para `0015`; a ADR-0011 histórica de adoção da release 1.1.0 permanece preservada e explicitamente marcada como histórica no decision log.
- Normalizados os corpos das ADRs G1/G2/G4 para usar `draft` de forma coerente com seu estado de rascunho.
- Registrada a proveniência do webinar e da transcrição em `research/sources/bibliography.md`, com evidence cutoff, conceitos utilizados e limitações; claims orais sem metodologia não foram importados como thresholds.
- A página 03 agora distingue architecture pattern de orchestration pattern e registra um work profile não normativo para pattern fit, sem alterar T1–T4, admissibility, risk score, MPB, impact assessment ou schema.
- O G3 passou a registrar pattern primário/secundário, work attributes, rationale, evidence, confidence e missing evidence; criado assessment vendor-neutral de technology evaluation para orchestrators.
- AIR e consolidated/coordinated/federated permanecem crosswalk externo; não foram promovidos a arquitetura, placement ou control normativo.
- Esta entrada descreve alterações locais pendentes de validação, revisão e publicação; não altera, por si só, a release ou a baseline publicada.

## 2026-08-17 — Terceira onda local Gartner: observabilidade AI-native

- Adicionadas a ADR-0014, o pattern de profile AI-native, o template de profile e o exemplo fictício de cadeia task/delegation/tool/policy/containment.
- O profile organiza correlation, provenance, redaction, retention, access, export, cardinality, cost e value sem obrigar OpenTelemetry, fornecedor ou backend específico.
- O `audit-event.schema.json` permanece inalterado; o profile é guidance opcional e não transforma cobertura de telemetry em assurance de eficácia.
- Esta entrada descreve alterações locais pendentes de validação, revisão e publicação; não altera, por si só, a release ou a baseline publicada.

## 2026-08-17 — Segunda onda local Gartner: delegação multiagente

- Adicionadas a ADR-0013, o pattern de governança de delegação, o template de contrato e o exemplo fictício supervisor/worker.
- O contrato registra topology, nodes, delegation edges, authority attenuation, identity, delegated subject, input/output validation, depth, fan-out, budget, expiry, revocation e failure propagation.
- A implementação permanece guidance/template em `draft`; o blueprint schema e novos controls não foram alterados antes do walkthrough G2.
- Esta entrada descreve alterações locais pendentes de validação, revisão e publicação; não altera, por si só, a release ou a baseline publicada.

## 2026-08-17 — Primeira onda Gartner: control planes e orchestrator decision record

- Adicionada a ADR-0015 e o pattern de governança multi-control-plane, com precedência, authority, source of truth, correlation, conflict path e fail-safe.
- O capítulo 02 passou a definir o tratamento de conflitos entre control planes; o capítulo 06 passou a ligar a arquitetura e o capability mapping à arbitragem cross-plane.
- Adicionado o `Orchestrator Decision and Exit Record`, com exemplo fictício para comparar topology, capabilities, enforcement, portability, lock-in, resilience e exit sem prescrever fornecedor.
- O capítulo 07 passou a tratar claims de orchestrator como alegações avaliáveis; o capítulo 09 passou a exigir matriz cross-plane, degraded mode, exit trigger e recovery evidence no run readiness.
- Os planos de implantação foram renomeados para explicitar seu escopo: planos específicos permanecem subordinados ao domínio correspondente, enquanto planos integrados permanecem no nível do capítulo.
- A decisão estrutural foi formalizada na [ADR-0012 — Hierarquia dos planos de implantação](docs/architecture/decisions/0012-implementation-plan-hierarchy.md).
- A decisão G1 foi renumerada de ADR-0011 para ADR-0015 porque ADR-0011 já identifica a adoção aceita da release 1.1.0 no histórico preservado.
- Esta entrada descreve alterações locais pendentes de revisão e publicação; não altera, por si só, a release ou a baseline publicada.

## 2026-08-13 — Segunda onda de revisão editorial ampla

- Capítulos de controle documental, mandato, accountability, risco, lifecycle, operações e métricas passaram a explicitar hierarquia de artefatos, fronteiras entre fases/gates/processos, decisões, owners, templates e critérios de conclusão.
- Nomes de approval matrix, perfis de plataforma e fóruns organizacionais foram reclassificados como adapters ou contexto histórico; as authorities canônicas continuam em decision rights e decision gates.
- O toolkit tornou-se uma porta de execução por decisão, com índices de patterns, templates, schemas, controls, registry, assessments e examples orientados por gatilho, saída e limite de interpretação.
- Research sources e crosswalks deixaram de se apresentar como scaffolds e agora distinguem fonte para claim, provenance histórica, mapping direcional e limitação.
- Esta entrada descreve alterações locais pendentes de revisão e publicação; não altera, por si só, a release ou a baseline publicada.

## 2026-08-13 — Reestruturação editorial da entrada e da sequência de leitura

- README, Guia de Consumo, `start-here`, índice e navegação MkDocs agora distinguem rota de implantação, estudo linear, referência por objetivo, toolkit e manutenção.
- O handbook foi reorganizado para explicitar dependências entre mandato, escolha do mecanismo, estate, risco, arquitetura, assurance, operação e toolkit.
- O capítulo 03 reposicionou a execução da descoberta antes de forecast e gargalos e passou a separar classificação preliminar de decisão normativa de risco.
- Corrigida a regressão editorial que tratava T4 como `default deny`; a separação entre risk tier e admissibilidade da ADR-0009 foi restaurada.
- Templates, schemas, examples e catálogo de artefatos ganharam destaque contextual nos capítulos de inventário, risco, arquitetura, assurance e implementação.
- A árvore pública do site deixou de publicar `tools/` e `tests/`; os artefatos permanecem no repositório para maintainers.
- Fontes externas indicadas para a análise foram registradas na bibliografia com tipo, uso e limitações.

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

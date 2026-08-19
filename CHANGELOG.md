# Changelog

Artefato operacional do framework canônico, mantido sob a release `1.1.0` e o source commit `5545d9227624400ab8bb707b6032b2f61329a36e`.

## 2026-08-19 — Unreleased: resolução conservadora de Dependabot sem mudança de produto

- O contrato de runtime permanece inalterado: `requires-python >=3.9`, `jsonschema>=4.22,<5`, `Pillow>=10,<13` e `PyYAML>=6,<7`. Os PRs #1/#12 (Pillow 12.3.0) e #14 (jsonschema 4.26.0) não foram incorporados porque a resolução exige Python `>=3.10`, incompatível com o baseline suportado.
- O PR #13 não foi incorporado: o lower bound de PyYAML não recebeu requisito de consumidor, security rationale ou incompatibilidade corrigida suficiente para alterar o package contract.
- O tooling Ruff foi atualizado de `0.15.10` para `0.16.3` no contrato CI, com correções mecânicas e justificativa explícita para findings de lint; nenhum código de produto, schema, control ou conteúdo normativo foi alterado.
- As Actions foram atualizadas isoladamente para `checkout@v7`, `setup-python@v7` e `upload-artifact@v7`, preservando comandos, paths, artifact name, permissões e comportamento dos workflows.
- O inventário de security alerts permanece `NOT_CONFIRMED`/`BLOCKED_BY_AUTHORIZED_EVIDENCE`; nenhum update foi declarado security remediation. A resolução remota dos PRs abertos depende de rebase, decisão de fechamento e publicação autorizada.

## 2026-08-18 — Unreleased: simulação sintética de promoção das ADRs 0013–0015

- Adicionado o case fictício `toolkit/examples/cases/adr-promotion-synthetic-validation/`, exercitando delegation, observabilidade AI-native e arbitragem entre control planes de ponta a ponta.
- O pacote inclui denies, privilege escalation, expiry/revocation, containment, recovery, deletion, export, cardinality/cost, correlation failure, fail-safe, substitution/exit e decision records sintéticos.
- A simulação é classificada como `SIMULATED_SYNTHETIC_EVIDENCE`: demonstra aplicabilidade e coerência do framework, mas, naquela decisão sintética, não era production evidence, não promovia as ADRs a `accepted` e não alterava schemas, controls, risk tiers, release ou status `draft`.
- O case é um exemplo transversal de delivery para futuras implementações e serviços; cada consumidor deve substituir aliases, fixtures e evidence sintéticos por authorities, ambientes e records próprios.

## 2026-08-18 — Unreleased: aceitação simulada das ADRs 0013–0015 como guidance do framework

- Executada revisão criterial das ADRs 0013, 0014 e 0015 contra seus contratos, patterns, templates, examples, testes determinísticos, drills e synthetic validation case. Nenhum finding conceitual bloqueante foi demonstrado no escopo de guidance do framework.
- Criado `project/decisions/0004-framework-guidance-acceptance-adr-0013-0015.md`, registrando `SIMULATED_OWNER_AUTHORIZED_REVIEW` e `accepted` com conditions para a camada canônica de guidance, patterns e templates. O decision record não representa sign-off de organização consumidora e não inventa reviewers, pessoas ou assinaturas.
- As ADRs 0013–0015 e o decision log passaram de `draft` para `accepted` no escopo do framework. A evidence maturity permanece `demonstrated-deterministic` + `demonstrated-synthetic`; `missing-authorized-evidence` permanece para implementation, operational validation, effectiveness e production readiness de consumidores.
- As conditions preservam human gating de publish/approve e exigem, por consumidor, authorities, identities, policy/tool enforcement, privacy/security review, export, retention/deletion, fallback, recovery, substitution e evidence próprios conforme a ADR.
- Esta decisão não altera schemas, controls, risk tiers, MPB, Registry, machine-readable enums, vendor ranking ou a release `1.1.0`; não cria nova simulação e não converte synthetic evidence em operational evidence.

## 2026-08-18 — Unreleased: rodada estruturada de hardening T29–T41

- T29 atualizou o assessment de quality gate com a evidência observada do PR #7 (`head 86149945`, run `32175015315`, conclusão `success`) e separou o display da UI (`Quality gates / Canonical repository quality gate`) do required status context técnico (`Canonical repository quality gate`). T30 registrou no `ROADMAP.md` a progressão PR #5 failure → PR #6 closeout success → PR #7 protected success → `main` `d72e756`.
- T31 integrou o synthetic validation case ao ADR promotion readiness e às ADRs 0013–0015; T32 separou decision status de evidence maturity sem criar nova taxonomia; T33 criou o human sign-off package sem nomes ou assinaturas inventados. No fechamento daquela rodada, as três ADRs permaneciam `draft`; uma decisão simulada posterior registra a aceitação de guidance no escopo do framework.
- T34–T36 atualizaram o inventory e a decision matrix dos PRs Dependabot #1 e #8–#14, mantendo #1 como `DUPLICATE_CANDIDATE`, #11 como `BLOCKED_BY_CI_FAILURE`, #12 em compatibility review e #13/#14 em contract review; nenhum merge foi executado.
- T35 documentou as três superfícies do contrato Python — runtime/package, CI/tooling e workflow/runtime — e preservou a regra de não elevar lower bounds sem requisito demonstrável. T37 registrou a análise oficial de Actions/Node 24; PRs #8–#10 continuam `REVIEW_COMPATIBILITY` apesar de CI success observado nos heads.
- T38 repetiu a tentativa autorizada de inventário de security alerts: REST retornou `403` e a consulta GraphQL corrigida retornou `nodes: []`; o resultado não foi interpretado como ausência de alerts. O estado permanece `BLOCKED_BY_AUTHORIZED_EVIDENCE`/`NOT_CONFIRMED`.
- T39 adicionou o evidence crosswalk para documentary, deterministic, synthetic, authorized implementation, operational longitudinal e human sign-off evidence, explicitando o que cada tipo prova e não prova. T40 recomendou `KEEP 1.1.0`, sem tag, version bump ou release automática.
- T41 vinculou o synthetic case ao authorized validation handoff e explicitou que seus prerequisites e acceptance criteria não foram reduzidos; T15/T16 continuam `BLOCKED_BY_AUTHORIZED_EVIDENCE` e T17 permanece `PLANNED`.
- As alterações desta rodada são documentais, de assessment, provenance e decision preparation. Não foram alterados schemas, controls, risk tiers, MPB, Registry, enums machine-readable, vendor ranking ou dependency package contract; nenhum PR Dependabot foi aceito por inferência.
- Validações incrementais locais após T39–T41 passaram no repository validator, nos testes de ADR walkthrough e semantic hardening, no Markdownlint dos arquivos tocados e no `git diff --check`. A regressão final em clean checkout permanece pendente antes da publicação da branch.
- Esta entrada permanece `Unreleased`, mantém a release `1.1.0` e não constitui aprovação humana das ADRs, security remediation, operational validation ou production readiness.

## 2026-08-18 — Unreleased: closeout técnico T20–T28

- T20 corrigiu R3 para referenciar explicitamente as quatro dimensões canônicas de metadata; T21 removeu `uv.lock` como dependência documental fictícia; T22 reconciliou ROADMAP e CHANGELOG com a evidência local e remota.
- T23 consolidou `.github/workflows/quality-gates.yml` como fonte única e renomeou o check para `Quality gates / Canonical repository quality gate`; T24 passou a agrupar somente minor/patch no Dependabot, mantendo major updates individuais e sem automerge.
- T25 registrou a disposition dos PRs Dependabot #1, #3 e #4 sem merge ou close automático. T26 tentou REST e GraphQL autorizados; o REST retornou `HTTP 403` e o resultado GraphQL vazio não foi interpretado como ausência de alerts. O inventário alert-by-alert permanece `BLOCKED_BY_AUTHORIZED_EVIDENCE`.
- T27 aplicou proteção remota em `main`: PR obrigatório, check canônico obrigatório, strict status checks, enforce admins, sem force-push, sem deletion e com conversation resolution; required reviewer count permanece `0` para não criar deadlock de owner único.
- No clean checkout do commit `3478233`, os gates locais passaram: validator, 81 testes, Ruff, `py_compile`, Markdownlint dos arquivos alterados, MkDocs strict, rendering determinístico e `git diff --check`. O PR #6 executou o run `32165595605` com conclusão `success` no check `Quality gates / Canonical repository quality gate`.
- T15–T17 continuam `BLOCKED_BY_AUTHORIZED_EVIDENCE`/`PLANNED`, ADRs 0013–0015 continuam `draft`, estate validation não foi executada e a release `1.1.0` permanece inalterada. O remote alert inventory e os upgrades dos PRs Dependabot não foram tratados como concluídos por inferência.

## 2026-08-18 — Unreleased: rodada estruturada de hardening T00–T19

- Aplicado hardening semântico e editorial no vocabulário canônico, nos estados de discovery, nas implementation waves, nas dimensões de metadata, no fluxo G0→G7, na avaliação de orchestrator e no crosswalk de observabilidade.
- Sinalizados thresholds como `ILLUSTRATIVE`/`NON-NORMATIVE`/`RECALIBRATE`, explicitados os limites entre narrativa e records e preenchido o `ROADMAP.md` com o trabalho real da rodada.
- Adicionados o índice de `source-history`, o assessment de ADR promotion readiness, o execution package de validação operacional autorizada, a triagem de dependency security, a configuração mínima de Dependabot e os testes de regressão semântica.
- A validação local pós-merge passou no validator, nos 81 testes unitários, no Ruff, no Markdownlint incremental, no build MkDocs e no `git diff --check`; os 63 findings do Markdownlint global permanecem históricos e fora do escopo desta rodada.
- O GitHub Actions do PR #5 e do push subsequente em `main` concluiu `failure` porque o validator encontrou a referência não versionada `../../uv.lock` no front matter de dependency security. O estado remoto histórico é `REMOTE_CI_FAILURE`; a correção faz parte deste closeout e não é reescrita como PASS.
- T15–T17 permanecem `BLOCKED_BY_AUTHORIZED_EVIDENCE`/`PLANNED`, T18 permanece `NOT_CONFIRMED` sem export autorizado dos alertas Dependabot e as ADRs 0013, 0014 e 0015 permanecem `draft`; não foram alterados schemas, controls, risk tiers, MPB, Registry, vendor ranking, release ou taxonomias externas.
- Esta entrada permanece `Unreleased` e não altera a release `1.1.0`.

## 2026-08-18 — Unreleased: ADR promotion readiness

- Criado o assessment `adr-promotion-readiness-0013-0014-0015.md`, separando evidência determinística, missing authorized evidence e sign-off necessário para as ADRs 0013, 0014 e 0015.
- Adicionado teste determinístico `test_adr_walkthrough_evidence.py` para proteger a integridade dos critérios dos exemplos G1, G2, G4 e substitution/replay.
- As três ADRs permanecem `draft`; não foram alterados schemas, controls, risk tiers, MPB, Registry, release ou taxonomias externas.
- Esta entrada permanece `Unreleased` e não altera a release `1.1.0`.

## 2026-08-17 — Unreleased: substitution/replay e G4 operational drill

- Executado teste determinístico e vendor-neutral de substitution/replay: export canônico preservado, lineage/correlation mantidos, escrita crítica negada e retry pós-expiry negado em duas implementações abstratas.
- Executado G4 operational drill fictício: payload/prompt/secret redacted ou omitidos, deletion de memory/state em primary/cache/index/backup, evidence hold separado e cardinalidade/custo dentro de envelope ilustrativo.
- Adicionados os exemplos `orchestrator-substitution-replay.example.md` e `ai-native-observability-operational-drill.example.md`, com links nos templates e catálogo de artefatos.
- O schema de audit event, blueprint schema, controls, risk tiers, MPB, registry, ADR status e release permanecem inalterados. Os resultados são evidência de desenho/teste determinístico e não equivalem a aprovação de produção.
- Esta entrada permanece `Unreleased` e não altera a release `1.1.0`.

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

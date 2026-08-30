---
title: Plano de implementação — Enterprise Integration Guide
status: proposed
owner: framework-maintainers
framework_release: 1.1.0
last_reviewed: 2026-08-30
review_cycle: major-change
evidence: missing-authorized-enterprise-review
next_review: after-design-authority-review
related:
  - ../../../toolkit/assessments/independent-enterprise-readiness-assessment.md
  - ../../../docs/framework/02-governance-and-accountability.md
  - ../../../docs/framework/06-architecture-and-technical-controls.md
  - ../../../docs/framework/08-implementation-and-adoption.md
  - ../../../toolkit/patterns/control-and-assurance-planes.md
  - ../../../toolkit/patterns/multi-control-plane-governance.md
---

# Plano de implementação — Enterprise Integration Guide

## 1. Decisão solicitada

Produzir um guia canônico e vendor-neutral que mostre como uma organização integra o framework às capacidades
corporativas já existentes, sem duplicar sistemas de registro, inventar novos fóruns ou transferir authority para
uma ferramenta.

O guia deve mapear o framework para:

1. Governance, Risk and Compliance (GRC);
2. Information Technology Service Management (ITSM);
3. Information Security Management System (ISMS);
4. Identity and Access Management (IAM);
5. procurement e third-party risk;
6. Internal Audit;
7. privacy;
8. records management;
9. enterprise architecture.

**Decisão recomendada:** aprovar a elaboração em quatro waves, começando pelo contrato comum de integração e por
um caso transversal, antes de escrever nove capítulos isolados.

## 2. Problema a resolver

O framework já cita GRC, ITSM, IAM, procurement, audit, privacy, records e arquitetura em vários capítulos e
patterns. Contudo, essas referências não formam hoje um contrato único que responda, por capability:

- qual sistema ou função pode ser source of truth;
- qual authority decide e qual apenas consulta ou executa;
- quais eventos entram e saem;
- quais IDs e versões correlacionam os registros;
- qual evidência é criada e onde é retida;
- qual gate ou transição pode ser bloqueado;
- como divergências entre sistemas são reconciliadas;
- como exceções, mudanças, incidentes e sunset propagam;
- o que permanece organização-específico.

Sem esse contrato, uma organização pode copiar o framework e criar uma camada paralela de governança, duplicar
dados em GRC, Configuration Management Database (CMDB), catálogo, IAM e registry, ou produzir dashboards sem
authority de remediação.

## 3. Resultado esperado

O trabalho deve criar `docs/reference/enterprise-integration-guide.md` como ponto de entrada e artefatos
reutilizáveis no toolkit. O pacote completo deve permitir que uma Design Authority responda:

> Para cada decisão, atributo, evento e evidência do lifecycle de um agente, qual capability corporativa possui
> authority, qual sistema mantém o registro canônico, quais adapters são necessários e como conflito ou falha é
> tratado?

### 3.1 Entregáveis

| ID | Entregável | Conteúdo mínimo | Destino proposto |
|---|---|---|---|
| EIG-01 | Guia principal | princípios, método, lifecycle, nove capability mappings, implantação e assurance | `docs/reference/enterprise-integration-guide.md` |
| EIG-02 | Matriz source of truth | objeto/atributo, sistema autoritativo, réplica, owner, reconciliação e fallback | `toolkit/templates/enterprise-source-of-truth-matrix.md` |
| EIG-03 | Matriz de integração | capability, input, output, evento, interface, authority, evidência e failure mode | `toolkit/templates/enterprise-integration-matrix.md` |
| EIG-04 | Crosswalk de lifecycle | G0–G7 e estados do agente para workflows e records corporativos | seção canônica do guia |
| EIG-05 | RACI de handoffs | decision rights e transições entre as nove capabilities | extensão do template de RACI ou template próprio |
| EIG-06 | Caso transversal fictício | intake até sunset com IDs correlacionados nas nove capabilities | `toolkit/examples/cases/enterprise-integration/` |
| EIG-07 | Checklist de readiness | critérios de desenho, implementação e teste da integração | `toolkit/assessments/enterprise-integration-readiness.md` |
| EIG-08 | Traceability update | relação entre capítulos, controles, artefatos e integration points | anexos e catálogos existentes |

Os paths são propostas de implementação. A wave de desenho confirma nomes e evita criar templates que dupliquem
artefatos existentes.

## 4. Princípios de desenho

1. **Capability antes de produto.** GRC, IAM ou ITSM descrevem funções; nenhum fornecedor é normativo.
2. **Authority não deriva da ferramenta.** Um workflow executa decisão; não cria decision right.
3. **Um owner por atributo canônico.** Réplicas declaram fonte, versão, freshness e regra de reconciliação.
4. **Registry não substitui sistemas corporativos.** Ele referencia e correlaciona, salvo atributo cuja fonte
   canônica tenha sido explicitamente atribuída a ele.
5. **Integração orientada a eventos e decisões.** Cada interface declara trigger, payload mínimo, resposta,
   timeout, retry, idempotência e failure mode.
6. **Fail-safe proporcional.** Falha de integração não pode converter `deny`, restrição, expiração ou suspensão em
   permissão silenciosa.
7. **Evidência por design.** Cada handoff declara record, integridade, retention, acesso e método de validação.
8. **Tailoring explícito.** O guia oferece decisão e contrato; a organização seleciona plataformas, thresholds,
   prazos e authorities.
9. **Sem equivalência automática.** Um controle corporativo existente só é herdado quando scope, população,
   operação e evidência forem compatíveis.
10. **Brownfield primeiro.** O método assume sistemas existentes, dívida técnica e ownership fragmentado.

## 5. Contrato comum para os nove mappings

Cada capability deve usar a mesma estrutura, evitando nove descrições incompatíveis.

| Campo | Pergunta obrigatória |
|---|---|
| Propósito | Qual resultado corporativo essa capability sustenta? |
| Aplicabilidade | Para quais tiers, estados, agentes e eventos o mapping se aplica? |
| Authority | Quem decide, desafia, executa e recebe escalation? |
| Objetos | Quais records, IDs, versões e atributos participam? |
| Source of truth | Qual sistema é autoritativo por atributo e qual apenas replica? |
| Triggers | Quais eventos iniciam criação, review, bloqueio, reassessment ou retirada? |
| Inputs e outputs | Qual payload mínimo atravessa a interface e com qual classificação? |
| Controls | Quais control IDs são implementados, herdados ou apenas suportados? |
| Evidence | Qual evidência é esperada, onde vive e como integridade e acesso são validados? |
| Validation | Qual teste demonstra desenho, implementação, cobertura e eficácia? |
| Failure mode | O que ocorre com timeout, conflito, indisponibilidade ou dado stale? |
| Reconciliation | Como divergências são detectadas, priorizadas e fechadas? |
| Metrics | Como medir cobertura, latência, falha, backlog, override e custo? |
| Tailoring | O que a organização precisa decidir localmente? |
| Non-goals | O que a capability não substitui nem prova? |

## 6. Mapa inicial por capability

### 6.1 Governance, Risk and Compliance

**Papel no framework:** manter obligations, risk records, control assignments, assessments, exceptions, approvals
e remediation, sem se tornar automaticamente source of truth do runtime.

**Integrações mínimas:**

- importar `agent_id`, versão, owner, tier, admissibilidade e estado do registry;
- relacionar requisitos, controls, tests, findings, exceptions e evidence manifests;
- emitir eventos de aprovação, condição, expiração, finding e residual-risk decision;
- bloquear gate quando evidence obrigatória ou exceção estiver vencida;
- reconciliar mudança de owner, tier, versão e lifecycle.

**Artefatos a produzir:** object mapping, workflow mapping, exception/expiry contract e evidence-reference pattern.

**Teste de aceite:** selecionar um agente T2 e um T3 e provar que mudança material, finding bloqueante e exceção
expirada propagam para a decisão de release sem duplicar a autoridade do registry ou da release authority.

### 6.2 Information Technology Service Management

**Papel no framework:** integrar service ownership, change, incident, problem, request, knowledge, CMDB e
continuidade aos estados e eventos do agente.

**Integrações mínimas:**

- mapear agente, serviço, configuration items e business service sem declarar que CMDB e registry são o mesmo;
- ligar release a change record e mudança material a reassessment;
- ligar incident/problem a quarantine, rollback, reactivation e post-incident review;
- propagar owner change, outage, maintenance e retirement;
- manter correlação entre ticket, deployment, agent/version e evidence package.

**Artefatos a produzir:** lifecycle/change crosswalk, incident/quarantine handoff e CMDB/registry reconciliation.

**Teste de aceite:** executar um cenário fictício de incidente que abre ticket, suspende o agente, preserva
evidência, cria problem record e impede reactivation antes de regressão e authority approval.

### 6.3 Information Security Management System

**Papel no framework:** incorporar riscos e controles agentic ao sistema de gestão de segurança, sem alegar
certificação ou equivalência automática com standards.

**Integrações mínimas:**

- relacionar scope, risk assessment, statement of applicability local, security controls e treatment plan;
- conectar threat model, adversarial tests, vulnerabilities, incidents e residual risk;
- definir herança de controles corporativos com population e evidence explícitas;
- incluir third-party, continuity, access, logging e secure change;
- preservar revisão e melhoria com findings e incidentes de runtime.

**Artefatos a produzir:** control inheritance worksheet, risk-treatment mapping e security assurance handoff.

**Teste de aceite:** demonstrar, sem claim de conformidade, quais controles de um agente T3 são herdados,
específicos, parcialmente cobertos ou ausentes, com owner e evidence para cada conclusão.

### 6.4 Identity and Access Management

**Papel no framework:** emitir e governar workload identity, delegated subject, autorização, secrets, privileged
access, Joiner-Mover-Leaver (JML), expiry e revocation.

**Integrações mínimas:**

- criar identidade estável vinculada a `agent_id`, ambiente, versão e owner;
- separar identidade humana, workload identity e identidade delegada;
- definir claims, scopes, policy decision, token lifetime e authority attenuation;
- propagar owner JML, suspension, quarantine, retirement e emergency revocation;
- correlacionar decisão de acesso, tool action e audit event.

**Artefatos a produzir:** identity binding contract, JML/ownership handoff e revocation drill.

**Teste de aceite:** revogar identidade/capability sem cooperação do agente, negar replay e demonstrar que owner
departure torna os agentes afetados visíveis e impede continuidade fora do grace period autorizado.

### 6.5 Procurement e third-party risk

**Papel no framework:** impedir aquisição, renovação ou expansão de fornecedor sem requisitos de uso agentic,
security, privacy, auditabilidade, continuidade e saída.

**Integrações mínimas:**

- acionar assessment quando produto ou serviço possui capacidade agentic material;
- relacionar fornecedor, serviço, model/provider catalog, agentes dependentes e data classes;
- incorporar cláusulas, subprocessadores, incident notification, audit rights, export, deletion e exit;
- impedir que vendor approval substitua approval do caso de uso;
- disparar reassessment em mudança contratual, de modelo, região, subprocessador ou capability.

**Artefatos a produzir:** intake trigger, due-diligence mapping, contract/evidence checklist e exit-test handoff.

**Teste de aceite:** simular mudança material de fornecedor e provar identificação de agentes afetados, review de
contrato, decisão de continuidade e fallback/exit.

### 6.6 Internal Audit

**Papel no framework:** incorporar o universo de agentes ao risk assessment de auditoria e testar desenho e
operating effectiveness com independência declarada.

**Integrações mínimas:**

- alimentar audit universe com estate, tiers, incidents, exceptions, findings e control coverage;
- selecionar população e amostra sem depender apenas da lista fornecida pela gestão;
- preservar independência, conflito, evidence cutoff e limitation;
- rastrear finding, management action, due date, retest e risk acceptance;
- distinguir framework review, implementation audit e control effectiveness.

**Artefatos a produzir:** audit-universe mapping, test-procedure profile e finding/remediation contract.

**Teste de aceite:** um auditor fictício consegue obter a população, selecionar amostra e reconstruir uma release e
um incidente sem depender do builder, registrando limitações e exceptions.

### 6.7 Privacy

**Papel no framework:** acionar privacy review, Data Protection Impact Assessment quando aplicável, minimização,
purpose limitation, data subject handling, retention e cross-border decisions.

**Integrações mínimas:**

- relacionar agent purpose, data classes, sources, memory, logs, providers e affected parties;
- definir triggers para privacy review e impact assessment;
- propagar purpose, consent ou legal-basis constraints para data/tool access;
- testar deletion em source, cache, memory, vector store, log e evidence store;
- registrar residency, transfer, subprocessors, redaction e legal hold.

**Artefatos a produzir:** privacy trigger matrix, data-store lineage e deletion/hold conflict procedure.

**Teste de aceite:** executar solicitação fictícia de deletion e demonstrar disposição em todos os stores, ou
retenção autorizada e delimitada quando houver hold, sem declarar aconselhamento jurídico.

### 6.8 Records management

**Papel no framework:** classificar records, definir retention/disposition, preservar legal hold, integridade,
acesso e export e executar defensible deletion.

**Integrações mínimas:**

- classificar registry, blueprint, decisions, prompts quando aplicável, audit events, evidence e incident records;
- definir record owner, system of record, retention trigger e disposition authority;
- distinguir operational telemetry de business record e audit evidence;
- propagar hold, suspension de deletion, export e restoration test;
- fechar records no sunset sem apagar provenance obrigatório.

**Artefatos a produzir:** record-classification schedule mapping, hold propagation e disposition checklist.

**Teste de aceite:** provar export e restauração de um evidence package e disposition de records após sunset,
preservando itens sob hold.

### 6.9 Enterprise architecture

**Papel no framework:** manter princípios, reference architectures, technology standards, approved patterns,
exceptions, lifecycle de tecnologia e decisões de interoperabilidade e saída.

**Integrações mínimas:**

- ligar capability map, application portfolio, registry, blueprints e technology catalog;
- revisar boundaries, trust assumptions, quality attributes, integration points e failure modes;
- aprovar patterns e standards sem aprovar automaticamente um caso de uso;
- registrar technical debt, exceptions, portability, concentration e exit;
- reconciliar desired architecture, deployed state e roadmap.

**Artefatos a produzir:** architecture review mapping, standards/patterns inheritance e exception/debt handoff.

**Teste de aceite:** uma review de agente T3 rastreia requisito material a componente e enforcement point, registra
exceção com expiry e demonstra fallback ou decisão de fail-closed.

## 7. Caso transversal obrigatório

O guia não deve ser aceito apenas por revisão documental. Um caso fictício único deve atravessar as nove
capabilities para expor conflitos de ownership e integração.

### Cenário proposto

Agente T3 de suporte interno que consulta fontes certificadas, cria um change draft, usa um fornecedor externo e
requer aprovação humana antes de qualquer side effect. Durante a operação, uma mudança de subprocessador e uma
anomalia de privilégio disparam reassessment, incident, quarantine e decisão de continuidade.

### IDs correlacionados

- `agent_id` e blueprint version;
- business service e configuration item;
- identity principal;
- risk/assessment ID;
- change, incident e problem IDs;
- supplier/contract ID;
- privacy assessment ID;
- record class/hold ID;
- architecture decision ID;
- evidence manifest e correlation ID.

### Caminho exercitado

`intake → risk → architecture → procurement/privacy/security review → identity → build/evaluation → release →
incident/quarantine → recovery → attestation → sunset`.

## 8. Waves de implementação

### Wave 0 — Baseline e contrato: 1 semana

**Objetivo:** impedir que a escrita comece com nove glossários diferentes.

| Tarefa | Owner típico | Saída | Critério de saída |
|---|---|---|---|
| Inventariar referências existentes | framework maintainer | coverage map | toda referência relevante possui destino ou rationale de exclusão |
| Confirmar escopo e non-goals | Governance Owner + Design Authority | scope decision | capabilities e boundaries aprovados |
| Definir contrato comum | Enterprise Architecture + Assurance | mapping contract | campos obrigatórios aceitos pelas nove funções |
| Definir caso transversal | Business, Architecture, Risk | case hypothesis | tiers, eventos, records e decisões delimitados |
| Resolver paths e artefatos | maintainer | content plan | nenhuma duplicação conhecida de template |

### Wave 1 — Control e assurance backbone: 2 semanas

**Escopo:** GRC, ISMS, Internal Audit e enterprise architecture.

**Motivo da ordem:** essas capabilities definem authority, control inheritance, assessment, evidence e challenge
que as integrações operacionais precisam preservar.

**Saídas:** quatro mappings, source-of-truth matrix inicial, control inheritance worksheet, audit handoff e
architecture review mapping.

### Wave 2 — Operação e identidade: 2 semanas

**Escopo:** ITSM, IAM e records management.

**Motivo da ordem:** lifecycle, incident, revocation, evidence retention e restoration formam o caminho crítico de
containment e recuperação.

**Saídas:** lifecycle/change crosswalk, incident/quarantine handoff, identity binding, JML propagation e records
schedule mapping.

### Wave 3 — Dados e terceiros: 2 semanas

**Escopo:** privacy e procurement/third-party risk.

**Motivo da ordem:** essas capabilities usam o backbone de authority, identity, records e change para governar
data flows, providers, contratos, deletion e saída.

**Saídas:** privacy trigger matrix, data-store lineage, supplier/agent dependency mapping e exit-test contract.

### Wave 4 — Integração, caso e publicação: 2 semanas

**Escopo:** reconciliar os nove mappings, executar o caso fictício, fechar cross-references e preparar challenge.

**Saídas:** guia completo, templates, caso transversal, readiness checklist, traceability update e findings log.

O prazo total de referência é de **nove semanas**. Ele é uma estimativa de planejamento, não SLA ou requisito
normativo. A execução pode ser paralelizada somente depois da aprovação do contrato comum.

## 9. Backlog implementável

### P0 — Necessário para começar

- [ ] EIG-T01 inventariar todas as referências existentes às nove capabilities;
- [ ] EIG-T02 identificar controls, schemas, templates, patterns e gates afetados;
- [ ] EIG-T03 aprovar escopo, glossary mínimo, non-goals e contrato comum;
- [ ] EIG-T04 definir matriz source of truth por objeto e atributo;
- [ ] EIG-T05 definir o caso transversal e seus IDs;
- [ ] EIG-T06 registrar decision owner e reviewers requeridos.

### P1 — Conteúdo por capability

- [ ] EIG-T07 escrever mapping de GRC;
- [ ] EIG-T08 escrever mapping de ITSM;
- [ ] EIG-T09 escrever mapping de ISMS;
- [ ] EIG-T10 escrever mapping de IAM;
- [ ] EIG-T11 escrever mapping de procurement/third-party risk;
- [ ] EIG-T12 escrever mapping de Internal Audit;
- [ ] EIG-T13 escrever mapping de privacy;
- [ ] EIG-T14 escrever mapping de records management;
- [ ] EIG-T15 escrever mapping de enterprise architecture.

### P1 — Contratos transversais

- [ ] EIG-T16 produzir lifecycle/change/incident crosswalk;
- [ ] EIG-T17 produzir control inheritance e assurance mapping;
- [ ] EIG-T18 produzir identity, owner JML e revocation mapping;
- [ ] EIG-T19 produzir evidence, retention, hold, export e deletion mapping;
- [ ] EIG-T20 produzir supplier, model, tool e agent dependency mapping;
- [ ] EIG-T21 definir conflict resolution, reconciliation e fail-safe por interface;
- [ ] EIG-T22 definir métricas de integração e capacidade operacional.

### P2 — Demonstração e closeout

- [ ] EIG-T23 construir o caso transversal fictício;
- [ ] EIG-T24 executar walkthrough criterial com as nove funções;
- [ ] EIG-T25 corrigir findings e registrar limitações abertas;
- [ ] EIG-T26 atualizar catálogo de artefatos, índices, traceability e changelog;
- [ ] EIG-T27 executar validação canônica do repositório;
- [ ] EIG-T28 obter decisão humana de publicação.

## 10. Papéis e RACI de elaboração

| Atividade | Accountable | Responsible | Consulted | Informed |
|---|---|---|---|---|
| Escopo e boundaries | Governance Owner | Framework Maintainer | nove capability owners | Sponsor |
| Contrato comum | Design Authority | Enterprise Architect | Assurance, Platform, Data | capability owners |
| Control inheritance | Security/Risk Authority | ISMS/GRC lead | Internal Audit, control owners | Design Authority |
| Lifecycle e incident | Run Authority | ITSM lead | IAM, Records, Platform | Governance Owner |
| Identity e revocation | Security/IAM Authority | IAM lead | Platform, ITSM, Audit | agent owners |
| Privacy e records | Data/Privacy Authority | Privacy + Records leads | Legal, Security, Procurement | Governance Owner |
| Third-party | Procurement Authority | Procurement/TPRM lead | Legal, Privacy, Security, Architecture | business owner |
| Assurance challenge | Audit/Assurance Authority | reviewer não autor | todas as capabilities | Sponsor |
| Publicação | Framework Governance Owner | Maintainer | Design Authority + reviewers | consumidores |

Os nomes são papéis típicos. Cada organização deve mapear suas próprias funções e declarar conflitos.

## 11. Dependências e decisões abertas

| ID | Decisão ou dependência | Estado | Owner requerido |
|---|---|---|---|
| D1 | O guia será referência não normativa ou criará requisitos adicionais? | proposta: referência não normativa | Framework Governance Owner |
| D2 | A matriz source of truth será template único ou extensão de artefato existente? | open | Design Authority |
| D3 | Quais controls exigem atualização de mapping, sem alterar statement? | open | Control Catalog Owner |
| D4 | O caso transversal reutiliza caso existente ou cria fixture própria? | proposta: fixture própria e mínima | Example Owner |
| D5 | Quais fontes licenciadas podem sustentar mappings de ISMS? | missing | ISMS/Legal |
| D6 | Quem fornece challenge independente das nove capabilities? | missing | Sponsor |
| D7 | Qual evidence de implementação real poderá existir fora deste repositório? | blocked by authorized organization | Governance Owner |

Nenhuma decisão aberta deve ser preenchida por inferência. Material licenciado não deve ser copiado para o
repositório.

## 12. Riscos do trabalho

| Risco | Consequência | Mitigação |
|---|---|---|
| Criar guia genérico demais | não muda implementação | exigir interface, evidence, failure mode e teste por mapping |
| Duplicar conteúdo canônico | divergência normativa | linkar requisitos existentes e adicionar somente contrato de integração |
| Tornar produto específico | perda de neutralidade | capability-first e exemplos rotulados como não normativos |
| Confundir mapping com compliance | claim indevido | disclaimers, applicability local e revisão jurídica |
| Criar nova camada paralela | custo e dados inconsistentes | source-of-truth matrix e brownfield-first |
| Nove capítulos inconsistentes | conflitos de semântica | contrato comum aprovado na Wave 0 |
| Scope excessivo | atraso sem resultado | caso transversal e critérios de saída por wave |
| Autor revisar o próprio trabalho | falsa independência | reviewer não autor e conflitos declarados |

## 13. Métricas de implementação

### Cobertura de conteúdo

- 9/9 capabilities usando o contrato comum;
- 100% dos integration points com authority, source of truth, evidence e failure mode;
- 100% dos links a control IDs existentes validados;
- zero requisito normativo duplicado em prosa divergente.

### Qualidade da integração

- percentual de atributos com source of truth inequívoco;
- percentual de eventos com correlation ID e version;
- conflitos sem regra de reconciliação;
- handoffs sem owner ou timeout;
- failure modes que degradam para permissão;
- evidências sem retention, access ou validation method.

### Operabilidade futura

- lead time de mudança entre sistemas;
- eventos não reconciliados;
- revogações não propagadas;
- exceptions expiradas ainda ativas;
- agents sem vínculo a service, identity, supplier ou architecture record quando aplicável;
- custo manual por lifecycle event.

As métricas operacionais permanecem hipóteses até exercício em organização autorizada.

## 14. Acceptance criteria do guia

O Enterprise Integration Guide estará pronto para publicação quando:

1. as nove capabilities utilizarem o contrato comum;
2. todo mapping identificar aplicabilidade, authority, evidence e validation method;
3. objetos e atributos materiais possuírem source of truth e reconciliation rule;
4. G0–G7, lifecycle, change, incident, JML, exception e sunset estiverem ligados a eventos corporativos;
5. indisponibilidade e conflito possuírem comportamento fail-safe proporcional;
6. control inheritance distinguir `inherited`, `shared`, `agent-specific`, `partial` e `missing`;
7. o caso transversal percorrer as nove capabilities e produzir findings recuperáveis;
8. um reviewer não autor conseguir seguir um agente do intake ao sunset;
9. mappings de standards não alegarem equivalência, certificação ou aconselhamento jurídico;
10. catálogo de artefatos, índices, traceability, changelog e referências dependentes estiverem atualizados;
11. a validação canônica do repositório passar;
12. findings materiais tiverem owner, disposition e prazo.

## 15. Definition of done da iniciativa

A iniciativa não termina quando o documento é publicado. Ela termina em dois níveis distintos:

- **framework complete:** guia, templates, caso, checklist, traceability e challenge documental atendem aos
  acceptance criteria;
- **operationally validated:** uma organização autorizada instancia os mappings, executa lifecycle e incident,
  mede propagação/reconciliação e registra effectiveness e limitações.

Até o segundo nível, o status correto é `framework-complete / not-operationally-validated`.


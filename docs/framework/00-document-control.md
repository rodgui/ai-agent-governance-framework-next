---
title: 00 — Controle do documento
status: maintained
maturity: validated
last_reviewed: 2026-08-13
review_cycle: quarterly
owners: [framework-maintainers]
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# 00 — Controle do documento

## Visão geral

Todo framework precisa de um "manual do manual": as regras que dizem o que este documento é, quem o aprova, como ele muda e como resolver conflitos quando as regras se chocam. Sem isso, o framework envelhece mal — versões se confundem, ninguém sabe se um texto é norma vigente ou rascunho, e cada time interpreta ambiguidade do seu jeito.

Este capítulo é o **contrato de governo do próprio framework**. Ele responde:

1. **O que é este documento?** — identificação, finalidade e escopo.
2. **Quem manda nele?** — owner, autoridade, aprovação e interpretação.
3. **Como ele muda?** — versão, revisão, processo de mudança e histórico.
4. **Como ele se relaciona com o resto?** — políticas superiores, padrões locais e resolução de conflitos.

Uma leitura atenta deste capítulo evita os dois erros mais caros de qualquer política: **tratar referência técnica como norma vigente** e **reescrever decisões em vez de superá-las**.

## Antes de usar este capítulo: a hierarquia de artefatos

| Objeto | Pergunta que responde | Força normativa | Saída típica |
|---|---|---|---|
| **Policy** | Que resultado, boundary e princípio a organização exige? | Obrigatória quando adotada pela authority competente. | Mandato, escopo, decision rights e obrigações. |
| **Standard** | Qual regra mínima torna a policy aplicável? | Obrigatório no escopo declarado. | Estados, critérios, thresholds, controles e condições de uso. |
| **Procedure ou guidance** | Como executar a regra em um contexto? | Adaptável; não pode enfraquecer policy ou standard. | Passos, runbooks, cadência e handoffs. |
| **Control** | O que deve prevenir, detectar, responder ou corrigir? | Exigível quando aplicável ao tier e ao escopo. | Owner, método de verificação, evidência e finding. |
| **Schema e template** | Como registrar a decisão ou configuração de forma consistente? | Contrato técnico ou acelerador; não decide sozinho. | Record estruturado, formulário ou manifest. |
| **Evidence** | O que demonstra que a regra foi atendida? | Necessária para sustentar a decisão. | Log, teste, decisão, configuração, relatório ou attestation. |
| **Example, pattern, case study e research** | Como interpretar, comparar ou aprender? | Não normativo, salvo incorporação explícita. | Rationale, opção de desenho, fonte ou demonstração fictícia. |

> **Regra de precedência:** policy define o resultado; standard fixa o mínimo; procedure explica a execução; control torna o mínimo verificável; evidence sustenta a decisão. Templates, schemas, examples, patterns e research ajudam a aplicar ou interpretar, mas não criam obrigação por associação.

## 1. O que este framework é

### 1.1 Identificação e finalidade

O framework tem um identificador estável e declara explicitamente o problema de decisão que resolve, o público a que se destina e o uso pretendido. A finalidade deste repositório: ser a **fonte modular** a partir da qual a política final de governança de IA e agentes é mantida, revisada e versionada.

A policy não é um documento monolítico nem depende de plataforma: é composta por princípios, decision rights, requisitos, controles, evidências e regras de lifecycle distribuídos em módulos canônicos.

**Concluído quando:** um leitor consegue distinguir este framework, seus produtos dependentes e seus não-objetivos sem depender de conhecimento tribal.

### 1.2 Dois níveis de adoção (não confundir)

A **release atual do framework é a baseline canônica mantida**. Isso significa que mudanças normativas exigem proposta, rationale, authority, changelog e release versionada. O status de uma release descreve a governança deste corpus; não declara adoção automática por qualquer organização.

Isso **não** significa que qualquer organização adotou esta policy. A adoção organizacional é uma decisão separada: cada organização declara esta baseline como sua política interna pela sua própria authority competente, com escopo, exceções e obrigações próprias. Enquanto essa decisão não existir, o conteúdo é **referência técnica canônica do framework — não a política vigente daquela organização**.

> **Armadilha comum:** confundir os dois níveis transforma versionamento em declaração de conformidade. Nenhum claim de certificação, auditoria independente ou conformidade decorre da adoção da release.

### 1.3 Composição da policy

A policy canônica é formada por:

1. [princípios arquiteturais](01-mandate-scope-and-principles.md);
2. [operating model e decision rights](02-governance-and-accountability.md);
3. [arquitetura em cinco planos](06-architecture-and-technical-controls.md);
4. [gestão proporcional de riscos](04-risk-impact-and-compliance.md);
5. domínios canônicos de identidade, dados, tools, segurança, Responsible AI, oversight, evaluations, auditabilidade, operações, adoção e valor;
6. [control catalog](../../toolkit/controls/README.md);
7. [implementation playbook e decision gates](08-implementation-and-adoption.md);
8. schemas e evidence packages que tornam os requisitos verificáveis.

O [handbook](../handbook/README.md) define a ordem editorial desses módulos, sem duplicá-los.

**Sobre a extensão dos capítulos:** a profundidade varia pelo escopo natural de cada domínio — o capítulo de controle do documento (este) é deliberadamente curto, enquanto arquitetura (06) e implementação (08) são densos porque carregam playbooks e matrizes de decisão. O critério editorial é clareza e completude, não uniformidade de tamanho: nenhum capítulo é encurtado para caber num padrão, nem inflado para parecer completo.

### 1.4 O que NÃO é policy (conteúdo não normativo)

Não integram a policy, salvo incorporação explícita e versionada:

- estudos de caso e explicações;
- crosswalks e avaliações comparativas;
- fontes e referências externas;
- exemplos fictícios;
- roadmap, specs e experimentos;
- calendários de 90 dias/24 semanas e o plano opcional de piloto;
- mappings de fornecedores.

Esses artefatos podem informar decisões, mas **não criam dependência tecnológica nem requisito normativo por associação**.

### 1.5 Neutralidade de fornecedor

A policy define **capabilities, outcomes, controls, evidências e boundaries** — não produtos obrigatórios. Fornecedores e plataformas nomeados podem aparecer como fonte, caso observado ou mapping opcional; nenhum deles é componente necessário do framework ou condição para conformidade. Um mapping deve poder ser removido sem alterar princípios, controls, decision gates, schemas ou a arquitetura canônica.

### 1.6 Origem histórica (o que alimentou este framework)

- A **AI Agent Policy and Governance v1** foi o ponto inicial do trabalho. É preservada byte a byte para rastreabilidade histórica, mas não é usada como fonte normativa recorrente do framework modular.
- O guia externo "Governança de Agentes de IA em Escala" também é **origem histórica**: seu conteúdo procedural foi absorvido e reescrito no formato canônico. Cópias daquele documento não são normativas e podem conter taxonomia divergente — a conversão para T1–T4 e a separação de `Restricted` como admissibilidade seguem a decisão registrada.
- Este repositório é a **fonte única e final**. Qualquer publicação em outro formato deve ser derivada destes módulos, nunca mantida como cópia editorial independente.

## 2. Quem é responsável por este documento

### 2.1 Owner e autoridade

O framework nomeia uma **autoridade responsável** (quem aprova, interpreta e responde por ele) e um **custodiano operacional** (quem mantém o repositório no dia a dia): papel, delegado nomeado quando aplicável, fonte de autoridade, rota de contato e regra de sucessão.

**Concluído quando:** aprovação, interpretação, revisão programada e mudança emergencial têm cada uma um tomador de decisão inequívoco.

### 2.2 Status de aprovação e força normativa

Todo artefato declara metadata suficiente para separar quatro perguntas: estado documental/editorial, estado da decisão, maturidade/evidence e tipo de artefato. O campo front matter `status` permanece compatível com o corpus atual: `maintained`, `draft`, `under-review`, `deprecated` e valores históricos contextuais. Em decisões, `accepted`, `superseded` e `rejected` expressam a disposição da decisão; `approved` também pode aparecer como estado legado ou de lifecycle. `maturity` expressa a força da evidence, como `illustrative`, `observed` ou `validated`; `type` diferencia `assessment`, `example`, `pattern`, `template` e `research`.

Essas dimensões não são intercambiáveis: `maintained` não significa `accepted`, `draft` não significa `illustrative` e `example` não significa `operationally-validated`. Uma migração futura de metadata deve preservar aliases e ser versionada; esta rodada não altera em massa os front matters existentes.

**Concluído quando:** nenhum draft, estudo de caso, fonte histórica ou example pode ser confundido com um requisito organizacional vigente ou com evidence operacional.

### 2.3 Interpretação e resolução de conflitos

Ambiguidade material não se resolve por conveniência. O framework define a autoridade e a rota de escalonamento para requisitos ambíguos, conflitantes ou localmente inaplicáveis: pergunta, interpretações concorrentes, autoridades consultadas, restrição provisória e disposição final. A decisão é propagada aos registros afetados.

**Concluído quando:** times de entrega não resolvem ambiguidade material por conveniência e a decisão é propagada aos registros afetados.

## 3. Como este documento muda

### 3.1 Versão, efetividade e ciclo de revisão

Toda mudança material é versionada e vinculada a datas de efetividade, revisão e supersessão: descrição da mudança, autor, aprovador, contratos impactados, ação de migração e referência à versão anterior. O ciclo de revisão é definido (trimestral neste framework) e o histórico de revisões registra cada versão com o mesmo rigor.

**Concluído quando:** consumidores identificam a versão aplicável e registros incompatíveis são migrados, rejeitados ou explicitamente grandfather.

### 3.2 Processo de mudança, consulta e aprovação

Mudanças materiais passam por análise de impacto, consulta às funções afetadas e aprovação: proposta, rationale, papéis consultados, objeções, resultado de compatibilidade, decisão e plano de migração. As regras de evolução normativa:

1. declarar o requisito alterado e sua justificativa;
2. registrar decisão e authority;
3. atualizar controls, evidências e impactos operacionais;
4. **preservar versões anteriores**;
5. incluir changelog e migration guidance quando necessário;
6. passar pelos quality gates do repositório antes de release.

**Concluído quando:** decisões aceitas são superseded em vez de reescritas silenciosamente e dependentes afetados recebem atualização rastreável.

### 3.3 Distribuição, acesso e retenção

Define-se quem pode ler, alterar e recuperar o registro, por quanto tempo e sob qual regra de legal hold ou exclusão: classificação, grupos de acesso, custodiano, gatilho de retenção, período mínimo, disposição e caminho de recuperação de auditoria.

**Concluído quando:** evidências autorizadas são recuperáveis no prazo exigido e dados expirados são descartados sem romper a linhagem exigida.

## 4. Escopo e relacionamentos

### 4.1 Escopo de aplicação

O framework enumera inclusões, exclusões, jurisdições, estágios de lifecycle, unidades organizacionais e classes de stakeholders afetados: declaração de escopo com rationale de fronteira, obrigações externas, padrões locais delegados e expiração de exclusões.

**Concluído quando:** o intake consegue encaminhar cada candidato como dentro do escopo, fora do escopo ou exigindo decisão, sem isenção implícita.

### 4.2 Políticas, padrões e registros relacionados

O framework mapeia políticas superiores, padrões subordinados e procedimentos locais **sem criar uma segunda fonte canônica**: tipo de relacionamento, owner, versão, regra de conflito e o requisito ou decisão exata vinculada.

**Concluído quando:** um conflito resolve-se por regra de precedência aprovada e artefatos a jusante podem ser avaliados por impacto em caso de mudança.

## 5. Referência normativa

Condições mínimas que devem ser verdadeiras. Use como checklist; as seções 1–4 explicam o porquê.

| # | Obrigação | Evidência mínima | Concluído quando |
|---|---|---|---|
| R1 | Atribuir identificador estável e declarar problema de decisão, público e uso pretendido | identificador, título, finalidade, público, status normativo, localização no repositório | leitor distingue o framework, seus produtos dependentes e não-objetivos sem conhecimento tribal |
| R2 | Nomear autoridade responsável e custodiano operacional | papel, delegado, fonte de autoridade, rota de contato, regra de sucessão | aprovação, interpretação, revisão e mudança emergencial têm tomador de decisão inequívoco |
| R3 | Declarar status (draft/aprovado/histórico/informativo/descontinuado) e o que ele permite | decisão de aprovação, aprovador, data, condições, efetividade, evidência de adoção | nenhum draft, caso ou fonte histórica é confundido com requisito vigente |
| R4 | Versionar toda mudança material com datas de efetividade, revisão e supersessão | descrição, autor, aprovador, contratos impactados, migração, referência à versão anterior | consumidores identificam versão aplicável; incompatíveis migrados/rejeitados/grandfather |
| R5 | Enumerar inclusões, exclusões, jurisdições, estágios, unidades e stakeholders | declaração de escopo com rationale, obrigações externas, padrões delegados, expiração de exclusões | intake encaminha cada candidato sem isenção implícita |
| R6 | Mapear políticas superiores, padrões e procedimentos sem segunda fonte canônica | tipo de relacionamento, owner, versão, regra de conflito, requisito vinculado | conflito resolve por precedência aprovada; dependentes avaliados por impacto |
| R7 | Encaminhar mudanças materiais por impacto, consulta e aprovação | proposta, rationale, papéis consultados, objeções, compatibilidade, decisão, migração | decisões aceitas são superseded, não reescritas; dependentes atualizados |
| R8 | Definir leitura/alteração/recuperação do registro, prazo e regra de legal hold | classificação, grupos de acesso, custodiano, gatilho, período mínimo, disposição, recuperação | evidências recuperáveis no prazo; expirados descartados sem romper linhagem |
| R9 | Definir autoridade e rota de escalonamento para requisitos ambíguos ou conflitantes | pergunta, interpretações concorrentes, autoridades consultadas, restrição provisória, disposição | times não resolvem ambiguidade por conveniência; decisão propagada |
| R10 | Versionar o histórico de revisões com o mesmo rigor das mudanças | histórico com descrição, autor, aprovador, contratos impactados, migração, versão anterior | qualquer versão anterior é recuperável e rastreável |

## 6. Acceptance criteria

- todas as decisões deste capítulo possuem authority, owner e evidência recuperável;
- requisitos aplicáveis estão ligados ao catálogo de controles e ao método de verificação;
- exceções têm escopo, justificativa, compensating controls, expiry e decisão residual;
- controles de build time e runtime são distinguidos e exercitados quando aplicáveis;
- mudanças materiais reabrem avaliação, aprovação e evidência;
- nenhuma alegação de conformidade, eficácia ou valor excede a evidência observada.

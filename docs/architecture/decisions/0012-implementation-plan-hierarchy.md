---
title: ADR-0012 — Hierarquia dos planos de implantação
status: accepted
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-17
review_cycle: major-change
supersedes: null
related:
  - ../README.md
  - ../../framework/04-risk-impact-and-compliance.md
  - ../../framework/05-agent-lifecycle.md
  - ../../framework/06-architecture-and-technical-controls.md
  - ../../framework/08-implementation-and-adoption.md
  - ../../framework/09-operations-incidents-and-continuity.md
  - ../../../toolkit/artifact-catalog.md
---

# ADR-0012 — Hierarquia dos planos de implantação

## Contexto

Os capítulos do framework contêm planos de implantação com escopos diferentes. Alguns planos implementam um domínio específico, como identidade, dados, modelos, tools, segurança ou observabilidade. Outros descrevem um fluxo integrado do próprio capítulo, como risco → impacto → aprovação ou lifecycle do agente. Há ainda roadmaps de programa, programas de adoção e pilotos opcionais.

Quando esses artefatos recebem títulos genéricos ou são apresentados sem uma hierarquia explícita, o leitor pode interpretar um plano de domínio como se fosse um plano concorrente ao tópico que ele implementa. A alternativa de reunir todos os passos em um único plano global também é inadequada: ela mistura authorities, dependências, evidências e decision gates diferentes e duplica o conteúdo dos domínios.

A decisão necessária é definir uma regra editorial estável para distinguir plano subordinado ao domínio, plano integrado de capítulo e roadmap de programa, preservando a separação entre guidance, procedure, control, evidence e verification.

## Forças e restrições

- A estrutura deve refletir o escopo real do plano, não apenas a ordem em que o texto foi escrito.
- Um plano específico precisa ser visualmente e semanticamente subordinado ao tópico que implementa.
- Um plano integrado deve permanecer no nível do capítulo para não parecer subprocedimento de um domínio particular.
- Roadmaps de 90 dias, programas de 24 semanas e pilotos opcionais são referências de programa; não são controls nem substituem decision gates.
- A regra não pode alterar IDs, schemas, controls, thresholds, states, decision gates ou regras de validação.
- A organização deve continuar vendor-neutral e evitar duplicar conteúdo normativo em um plano transversal artificial.
- Headings e títulos precisam permitir navegação, anchors estáveis quando já consumidos e manutenção por owners distintos.

## Opções consideradas

### Opção A — Um único plano de implantação ao final de cada página

**Vantagens:**

- oferece uma sequência única de leitura;
- pode ser útil para um capítulo curto e verdadeiramente integrado;
- reduz a quantidade aparente de headings de plano.

**Desvantagens:**

- mistura passos com authorities, dependências e evidências diferentes;
- duplica ou resume de forma incompleta os planos de domínio;
- dificulta identificar o owner e o decision gate do passo;
- transforma um capítulo técnico em um procedimento monolítico de baixa reutilização;
- não é adequado para a página 06, que contém seis domínios técnicos distintos.

### Opção B — Um plano subordinado a cada domínio, quando o escopo for específico

**Vantagens:**

- mantém o plano junto do princípio, requisito, artefato e decision gate que ele implementa;
- torna visíveis as dependências e o owner do domínio;
- evita duplicação e preserva a autonomia dos capítulos técnicos;
- permite que um revisor leia o tópico completo sem procurar o plano em outra parte da página.

**Desvantagens:**

- páginas densas podem conter vários planos;
- a comparação entre domínios exige voltar ao nível do capítulo;
- títulos genéricos ainda podem causar ambiguidade se não declararem o escopo.

### Opção C — Misturar planos específicos e integrados sem regra explícita

**Vantagens:**

- requer pouca alteração imediata;
- preserva a ordem histórica dos documentos.

**Desvantagens:**

- mantém a ambiguidade que motivou esta decisão;
- torna inconsistentes as páginas do framework;
- confunde plano de domínio, plano de capítulo e roadmap de programa;
- aumenta o risco de novos conteúdos serem colocados no nível errado.

## Decisão

1. **Planos específicos de domínio devem ser headings subordinados ao domínio correspondente.** Em Markdown, usam o próximo nível inferior ao heading do domínio. O título deve declarar o escopo, preferencialmente no formato `Plano de implantação — <domínio>`.

2. **Planos integrados de capítulo devem permanecer no nível do capítulo.** O título deve declarar o fluxo completo ou a capability integrada que o plano implementa, por exemplo `Plano de implantação — risco, impacto e aprovação` ou `Plano de implantação — lifecycle do agente`.

3. **Roadmaps, programas e pilotos devem permanecer identificados como artefatos de programa.** Termos como `roadmap de 90 dias`, `programa de 24 semanas` e `plano opcional de piloto` não devem ser tratados como planos técnicos de domínio nem como requirements normativos.

4. **A página 06 adota planos específicos por domínio e não recebe um plano global adicional.** Os seis planos permanecem subordinados a seus respectivos tópicos: runtime/control plane, identidade e acesso, dados e AI-ready data, modelos e provedores, tools/APIs/MCP e AgentSecOps. A referência normativa, os decision gates e os acceptance criteria fazem o fechamento transversal do capítulo sem duplicar os playbooks.

5. **A hierarquia não altera o conteúdo normativo.** A mudança é editorial e estrutural: não altera IDs, schemas, controls, thresholds, states, owners canônicos ou regras de validação. Um título pode ser tornado mais específico para reduzir ambiguidade, desde que anchors consumidos sejam verificados.

6. **Todo novo plano deve ser classificado antes de ser adicionado.** O autor deve registrar se o plano é específico de domínio, integrado de capítulo ou roadmap de programa e colocá-lo no nível correspondente.

## Justificativa

A opção B para planos específicos, combinada com a distinção explícita dos planos integrados e dos artefatos de programa, representa melhor a arquitetura editorial do framework. Ela preserva a relação entre o que um domínio decide, como implanta, quais evidências produz e qual gate bloqueia o release.

A página 06 é o caso mais importante. Seus seis domínios possuem authorities, artefatos e failure modes diferentes. Consolidá-los em um plano único reduziria a precisão e criaria uma falsa sequência linear. Manter cada plano como subnível do seu domínio torna a estrutura navegável sem transformar a quantidade de planos em um problema.

## Consequências positivas

- O leitor distingue imediatamente plano de domínio, plano integrado e roadmap de programa.
- Os planos da página 06 permanecem associados ao tópico técnico correto.
- Owners, artefatos e decision gates continuam localizáveis no contexto em que são usados.
- A estrutura reduz duplicação, ambiguidade e risco de novos planos serem adicionados no nível errado.
- A decisão é aplicável a páginas futuras sem prescrever produto ou ferramenta.

## Consequências negativas

- Alguns capítulos continuarão contendo vários planos específicos.
- Títulos mais longos podem ocupar mais espaço no índice de navegação.
- Mudanças de título podem alterar anchors gerados automaticamente; links existentes precisam ser verificados.
- A decisão não elimina a necessidade de uma visão transversal nos capítulos que realmente possuam fluxo integrado.

## Riscos

| Risco | Mitigação |
|---|---|
| Um plano específico ser colocado no nível do capítulo | Revisar o escopo real antes de adicionar o heading e exigir título com domínio explícito. |
| Um plano integrado ser fragmentado artificialmente | Verificar se o fluxo atravessa múltiplos domínios, authorities ou decision gates antes de escolher um subnível. |
| Roadmap ser interpretado como requirement | Usar rótulos `referência`, `pattern` ou `opcional` e manter a distinção com G0–G7. |
| Renomeação quebrar links ou anchors | Executar validator, busca de referências, build MkDocs e inspeção de warnings após cada alteração. |
| Criação de plano global duplicar conteúdo técnico | Aplicar a regra de que a página 06 usa planos por domínio e fecha com referência normativa, gates e acceptance criteria. |

## Critérios de validação

- [x] Cada plano da página 06 está subordinado ao heading do domínio que implementa.
- [x] Os títulos dos planos da página 06 explicitam o domínio coberto.
- [x] Planos integrados das páginas 04 e 05 permanecem no nível de capítulo.
- [x] O plano da adoção na página 08 e o plano de observabilidade na página 09 permanecem subordinados aos respectivos tópicos.
- [x] Roadmaps de 90 dias, programas de 24 semanas e piloto opcional permanecem identificados como artefatos de programa.
- [x] Validator, testes, build MkDocs e `git diff --check` passam após a reorganização.
- [x] Nenhum ID, schema, control, threshold, state ou regra de validação foi alterado.

## Gatilhos para revisão

Revisar quando:

- um capítulo ganhar um novo domínio ou perder a separação entre domínios;
- um plano passar a atravessar authorities, controls ou decision gates de múltiplos domínios;
- um roadmap for transformado em procedure ou requirement normativo;
- a navegação do site ou o sistema de anchors mudar materialmente;
- uma revisão editorial demonstrar que a estrutura atual dificulta a execução ou a auditoria.

## Evidências

- `docs/framework/04-risk-impact-and-compliance.md`
- `docs/framework/05-agent-lifecycle.md`
- `docs/framework/06-architecture-and-technical-controls.md`
- `docs/framework/08-implementation-and-adoption.md`
- `docs/framework/09-operations-incidents-and-continuity.md`
- `plan-hierarchy-audit.md`
- `git diff --check`
- validator, suíte de testes e build MkDocs executados em 2026-08-17

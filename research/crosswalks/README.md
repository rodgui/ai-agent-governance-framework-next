---
title: Crosswalks externos
status: maintained
owner: framework-maintainers
last_reviewed: 2026-08-13
review_cycle: quarterly
related:
  - ../sources/bibliography.md
  - ../../toolkit/controls/README.md
---

# Crosswalks externos

Crosswalks mostram como uma fonte externa se relaciona com capítulos, controls, evidências e lacunas do framework. Eles ajudam a investigar cobertura e a preparar avaliações locais. **Não são prova de conformidade, certificação, equivalência integral ou aplicabilidade jurídica.**

## Artefato disponível

| Artefato | Pergunta que responde | Limite de interpretação |
|---|---|---|
| `external-requirements-traceability.csv` | Que unidade de uma fonte externa foi relacionada a quais capítulos, controls e evidências esperadas? | A relação é direcional, dependente de versão/cutoff e não substitui a leitura da fonte nem a avaliação do contexto organizacional. |

O CSV contém unidades auditáveis de fontes externas e deve ser lido junto com a [bibliografia](../sources/bibliography.md), que registra tipo, acesso, escopo e limitações das fontes.

## Como usar um crosswalk

1. **Defina a pergunta.** Use o crosswalk para investigar cobertura, orientar gap assessment ou preparar uma revisão de requisito; não para declarar conformidade.
2. **Confirme versão e cutoff.** A unidade da fonte, a versão, a data de acesso e o status do framework precisam ser compatíveis com a pergunta.
3. **Leia a relação.** Diferencie mapeamento direto, parcial, contextual, não mapeado e não aplicável. Uma linha sem mapping não prova ausência de controle; pode indicar escopo diferente.
4. **Avalie localmente.** O control e a evidência devem ser testados no estate da organização, com owner e decisão registrados.
5. **Registre a limitação.** Fonte protegida, guidance de fornecedor, mudança regulatória ou interpretação jurídica devem permanecer explícitas.

## Requisitos de qualidade de um mapping

Cada unidade deve preservar fonte, versão, locator, evidence cutoff, tipo de relação, capítulos/controls vinculados, evidência esperada, owner da manutenção e limitação. Um mapping não pode introduzir requisito, threshold ou produto que não exista no corpus canônico sem change proposal aprovada.

Para entender os controls antes de usar um crosswalk, consulte o [catálogo de controles](../../toolkit/controls/README.md). Para entender os limites de standards e fontes, consulte [Fontes e evidência externa](../sources/README.md).

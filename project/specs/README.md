# Specs

## Propósito

Índice operacional de `project/specs` no framework canônico.

## Artefatos

- [Plano de implementação do Enterprise Integration Guide](003-enterprise-integration-guide/plan.md) — backlog,
  contrato comum, mappings por capability, waves e acceptance criteria para integrar o framework a capacidades
  corporativas existentes;
- os records históricos preservados em [`source-history`](source-history/README.md).

## Regras operacionais

- cada record identifica owner, status, framework release, evidência e próxima revisão;
- campos ausentes permanecem explicitamente `missing`; não são inferidos;
- decisões registram authority, rationale, condições, expiry e residual risk quando aplicável;
- segredos, dados pessoais e evidência de produção não pertencem a este repositório;
- exemplos usam apenas identidades e organizações fictícias.

## Validação

A validação local verifica estrutura, links, JSON/YAML, pin de versão, ausência de segredos e boundary de dados. Findings devem ser corrigidos ou aceitos explicitamente antes da adoção organizacional.

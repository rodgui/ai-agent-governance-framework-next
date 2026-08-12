# AI Agent Governance Framework — Next

Framework canônico e **vendor-neutral** para governança de agentes de IA: policy
modular, 11 capítulos de domínio, 44 controles verificáveis, schemas estruturados,
patterns, templates e casos de referência fictícios. Escrito em PT-BR; contratos
estruturados (schemas, IDs, enums) permanecem em inglês como contratos.

> **Para consumir este repositório, leia o [Guia de Consumo](CONSUMO.md) primeiro.**
> Ele explica os dois repositórios do ecossistema (framework e template),
> as trilhas de estudo, o fluxo de implantação e um caso prático passo a passo.

## Portas de entrada

| Sua intenção | Onde ir |
|---|---|
| **Implantar na organização** | [Comece aqui — trilhas de leitura](docs/start-here.md) |
| **Estudar na ordem editorial** | [Handbook](docs/handbook/README.md) |
| **Localizar um assunto** | [Índice por persona e objetivo](docs/index.md) |
| **Entender o ecossistema completo** | [Guia de Consumo](CONSUMO.md) |
| **Instanciar registros na sua org** | repo `ai-agent-governance-implementation-template` (pin `@1.1.0`) |

## Estrutura

| Área | Conteúdo |
|---|---|
| `docs/framework/` | 11 capítulos canônicos (00–10): policy, operação, risco, lifecycle, arquitetura, avaliação, implementação |
| `docs/executive/` | brief executivo e comunicação para C-level |
| `docs/patterns/` | design patterns de implementação |
| `toolkit/controls/` | catálogo de 44 controles com evidência declarada |
| `toolkit/schemas/` | contratos JSON (blueprint, registry, audit event, manifests) |
| `toolkit/templates/` | templates reutilizáveis (blueprint, risk record, RACI, charter) |
| `toolkit/examples/cases/` | casos de referência fictícios (prova de coerência do método) |
| `toolkit/maturity/` | maturity model |
| `research/` | fontes, bibliografia e crosswalks com frameworks externos |
| `project/` | decisões, histórico preservado byte a byte e migração |

## Validação

A validação local verifica estrutura, links, JSON/YAML, pin de versão, ausência de
segredos e boundary de dados. Findings devem ser corrigidos ou aceitos explicitamente
antes da adoção organizacional. Executar antes de cada commit:

```bash
uv run --no-project --with jsonschema --with pyyaml --with pillow python3 tools/scripts/validate-repository.py
uv run --no-project --with jsonschema --with pyyaml --with pillow python3 -m unittest tools.scripts.test_validate_repository
```

Build do site de documentação:

```bash
uv run --no-project --with mkdocs-material python3 tools/build-docs-site.py
```

## Regras operacionais

- cada record identifica owner, status, framework release, evidência e próxima revisão;
- campos ausentes permanecem explicitamente `missing`; não são inferidos;
- decisões registram authority, rationale, condições, expiry e residual risk quando aplicável;
- segredos, dados pessoais e evidência de produção não pertencem a este repositório;
- exemplos usam apenas identidades e organizações fictícias.

## Aviso de maturidade

Nenhum control foi exercitado contra um estate real — os casos de referência são
fictícios e provam coerência do método, não eficácia. Thresholds, tiers e prazos
precisam ser recalibrados com dados da organização adotante.

## Dependência e pin

- Framework release: `1.1.0` — fonte `5545d9227624400ab8bb707b6032b2f61329a36e`
- Ver [CHANGELOG.md](CHANGELOG.md) e [ROADMAP.md](ROADMAP.md)
- Licença: [CC BY 4.0](LICENSE)

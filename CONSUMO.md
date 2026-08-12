# Guia de Consumo — Framework de Governança de Agentes de IA

> **O que é:** este guia explica **como usar** este repositório — o framework
> canônico (`ai-agent-governance-framework-next`) — e o ponto de partida de
> implementação (`ai-agent-governance-implementation-template`).
>
> **Para quem:** qualquer pessoa que vai ler, implantar ou instanciar este
> conteúdo. Se você só quer estudar, o [handbook](docs/handbook/README.md) já basta.

---

## 1. Os dois repositórios e seus papéis

```
┌───────────────────────────────────────────────────┐
│ 1. ai-agent-governance-framework-next             │
│    O CONHECIMENTO CANÔNICO                        │
│    policy modular, 11 capítulos, 44 controles,    │
│    schemas, patterns, templates, casos fictícios  │
└───────────────────────┬───────────────────────────┘
                        │ pin @ 1.1.0 (referencia, nunca copia)
                        ▼
┌───────────────────────────────────────────────────┐
│ 2. implementation-template                        │
│    O ESQUELETO                                    │
│    registros vazios, exemplos fictícios,          │
│    estrutura de pastas para a organização         │
└───────────────────────────────────────────────────┘
```

**Regra de ouro:** o framework é a **fonte única de verdade**. O template
**referencia** conteúdo canônico por ID e versão — nunca copia policy, controles
ou templates. Isso é verificado por validador: um fork canônico
(`canonical framework fork detected`) faz a validação falhar.

| Repositório | Você usa quando... | Entrada recomendada |
|---|---|---|
| **framework-next** | quer estudar, decidir ou implantar governança | [Comece aqui](docs/start-here.md) |
| **implementation-template** | vai preencher registros de uma organização real | [README](https://github.com/rodgui/ai-agent-governance-implementation-template) → `docs/01-initialization.md` |

---

## 2. Como ESTUDAR (framework-next)

O framework tem três portas de entrada deliberadamente diferentes. Escolha pela
sua intenção:

| Intenção | Onde ir | Por quê |
|---|---|---|
| **Ordem editorial, capítulo a capítulo** | [handbook](docs/handbook/README.md) | Leitura linear dos 32 itens, em 5 partes |
| **Implantar na organização** | [Comece aqui](docs/start-here.md) | 4 trilhas que terminam em decisões, não em leitura |
| **Localizar um assunto** | [Índice](docs/index.md) | Jornadas por persona e objetivo |

### O handbook (leitura linear)

O [handbook](docs/handbook/README.md) define a ordem editorial em 5 partes:
**Fundamentos → Policy/operating model/risco → Domínios de controle → Método/toolkit →
Fontes**. Cada capítulo canônico é escrito em **três níveis** — entender, decidir,
executar — e um capítulo completo permite sair com algo **produzido, aprovado ou
operacionalizado**, não apenas compreendido.

### O start-here (implantação)

O [start-here](docs/start-here.md) tem uma regra que economiza mais tempo:

> **Leia o [implementation playbook](docs/framework/08-implementation-and-adoption.md)
> antes de qualquer outra coisa.** É o único documento que dá **ordem**. Todos os
> outros dão **conteúdo**.

As 4 trilhas (cada uma termina numa decisão):

| Trilha | Para quem | Duração | Decisão ao final |
|---|---|---|---|
| 0 — Sponsor/comitê | executivos | ~1h | patrocinar, nomear governance owner, aprovar mandato |
| 1 — Quem monta o programa | implementadores | ~1 semana | escopo, fases, workstreams, alvo de maturidade |
| 2 — Risco/RAI/jurídico | compliance | ~1 semana | tiers calibrados, escaladores, o que bloqueia release |
| 3 — Arquitetura/plataforma | arquitetos | ~2 semanas | source of truth, pontos de enforcement, comprar vs construir |

**Ordem de execução após a leitura:** `baseline → desenho → fundações → um caso real → escala`,
autorizada pelos gates G0–G7 (numeração não é cronograma — dependência real está no playbook).

---

## 3. Como IMPLANTAR (framework-next + implementation-template)

O caminho de implantação combina o conhecimento do framework com os registros do template.

### Fluxo típico

```text
1. framework-next  →  Trilha 0/1 do start-here (decisões de patrocínio e escopo)
2. framework-next  →  capability map + maturity model (baseline com evidência)
3. template        →  clonar para workspace autorizado da organização
4. template        →  docs/01-initialization.md → ... → docs/10-retire-and-upgrade.md
5. framework-next  →  cap. 06/07 + schemas + patterns (desenho dos controles)
6. template        →  preencher registros reais (substituir os fictícios)
7. template        →  python tools/validate_repository.py (a cada mudança)
8. framework-next  →  cap. 08 (gates G0–G7) para autorizar avanço entre etapas
```

### Como usar o template

```bash
# 1. Copie para um workspace autorizado e específico da organização (NUNCA preencha no repo original)
git clone git@github.com:rodgui/ai-agent-governance-implementation-template.git minha-org-governance
cd minha-org-governance

# 2. Confira a versão do framework à qual o template está pinado
cat FRAMEWORK_COMPATIBILITY.md framework-release.yaml

# 3. Siga a ordem de adoção
docs/01-initialization.md          # visão geral e regras
docs/02-assign-owners-and-authorities.md
docs/03-adopt-and-tailor-local-policy.md
docs/04-establish-registry-and-intake.md
docs/05-assess-risk-and-impact.md
docs/06-document-architecture-and-controls.md
docs/07-build-release-evidence.md
docs/08-operate-exceptions-and-incidents.md
docs/09-attest-audit-and-improve.md
docs/10-retire-and-upgrade.md

# 4. Preencha os registros reais, guiando-se pelos exemplos fictícios
#    (examples/fictional/ NUNCA vai para produção — são provas de coerência do método)

# 5. Valide a cada mudança
python tools/validate_repository.py
```

A estrutura de pastas do template espelha o ciclo de vida do framework:
`intake/` (é agente ou não? risco preliminar) → `assessments/` (risco, impacto,
capacidade) → `registry/` (identidade e lifecycle) → `releases/` (evidência,
minimum production bar) → `incidents/` → `retirement/`.

---

## 4. Caso prático — "empresa fictícia Acme quer começar"

Cenário: a Acme (nome fictício, setor financeiro) tem ~40 agentes de IA espalhados
em copilotos e workflows, sem governança formal. Um sponsor executivo leu o brief.
O passo a passo abaixo mostra exatamente quais arquivos consumir e preencher.

### Semana 1 — Decisões executivas (Trilha 0)

1. Sponsor lê [brief executivo](docs/executive/governing-agents-at-scale.md)
   e [fundamentos](docs/framework/01-mandate-scope-and-principles.md).
2. **Decisão:** patrocinar + nomear o governance owner. Registro no template:
   `governance/policies/governance-charter.md` (mandato, escopo, autoridades).
3. Time de implementação lê [playbook](docs/framework/08-implementation-and-adoption.md)
   e a [Trilha 1](docs/start-here.md).

### Semana 2 — Baseline

4. Aplicar [capability assessment worksheet](https://github.com/rodgui/ai-agent-governance-implementation-template/blob/main/assessments/capability-assessment-worksheet.md)
   e [maturity assessment](https://github.com/rodgui/ai-agent-governance-implementation-template/blob/main/examples/fictional/assessments/maturity-assessment.example.json).
5. **Decisão:** escopo, fases, workstreams, alvo de maturidade. Registro:
   `assessments/` do template.

### Semanas 3–6 — Fundações

6. Calibrar tiers de risco (cap. 04) — registrar em `assessments/risk/`.
7. Estabelecer registry e intake (passo 04 do template — `docs/04-establish-registry-and-intake.md`
   no repositório `ai-agent-governance-implementation-template`):
   - `intake/agent-or-not-decision.md` — cada nova demanda responde "isto é um agente?".
   - `intake/risk-pre-screen.md` — triagem preliminar de risco.
8. Primeiro agente T2 entra no [registry do framework](toolkit/registry/README.md):
   preencher `registry/agents/` + blueprint do `templates/agent-blueprint.md`.

### Semana 7 — Um caso real ponta a ponta

9. Escolher **um** agente (ex.: resumo de reuniões) e percorrer o caminho completo,
   usando o [caso fictício de referência](toolkit/examples/cases/README.md) como espelho:
   - blueprint JSON (valida contra `schemas/agent-blueprint.schema.json`);
   - risk assessment (valida contra o schema de risco);
   - [release evidence manifest](toolkit/templates/release-evidence-manifest.md) —
     o mínimo para o gate de release.
10. Rodar `python tools/validate_repository.py` — tudo deve passar com os
    exemplos fictícios ainda no lugar, e os registros reais também devem passar
    as mesmas validações.

### Semana 8+ — Escala

11. Rodar `docs/08-operate-exceptions-and-incidents.md` (como operar incidentes),
    `docs/09-attest-audit-and-improve.md` (attestation periódico) e
    `docs/10-retire-and-upgrade.md` (quando mudar a versão pinada do framework).

> **Aviso honesto (do próprio framework):** os casos de referência são **fictícios**
> e provam coerência do método, não eficácia. Thresholds, tiers e prazos precisam
> ser **recalibrados com os dados reais da Acme**, e a primeira implantação é também
> a primeira validação do framework.

---

## 5. O que NÃO esperar

- **Não é um produto pronto** — é um framework verificável (44 controls com
  evidência declarada, contratos estruturados, validação automatizada), não um
  SaaS ou ferramenta.
- **Nenhum control foi exercitado em estate real** — a primeira implantação é a
  primeira validação; reserve orçamento para recalibrar.
- **Vendor-neutral** — fornecedores e plataformas comerciais aparecem apenas como
  casos de estudo ou mappings opcionais (ver `research/case-studies/` e
  `research/crosswalks/`), nunca como requisito do framework.
- **Política v1 é história** — o conteúdo normativo atual é o framework modular
  (este repositório); documentos históricos ficam preservados byte a byte em
  `project/history/`.

---

## 6. Mapa de arquivos mais usados

| Pergunta | Arquivo |
|---|---|
| "Por onde começo?" | [docs/start-here.md](docs/start-here.md) |
| "Qual a ordem de leitura?" | [docs/handbook/README.md](docs/handbook/README.md) |
| "Como implantar?" | [cap. 08](docs/framework/08-implementation-and-adoption.md) |
| "Quais controles existem?" | [control catalog](toolkit/controls/README.md) |
| "Quais schemas/contratos?" | [schemas](toolkit/schemas/README.md) |
| "Exemplos de registros?" | [casos de referência](toolkit/examples/cases/README.md) |
| "Como instanciar na minha org?" | repo `implementation-template` → `docs/01-initialization.md` |

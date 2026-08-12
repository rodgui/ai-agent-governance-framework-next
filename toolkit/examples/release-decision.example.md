# Exemplo de decisão de release — Service Desk Knowledge Agent

> Fictício e sanitizado. Este registro não autoriza uma implantação real.

## Registro de decisão

- Gate: G5 — Onboarding/release
- Escopo: analistas internos de service desk
- Blueprint: 1.0
- Tier: T2
- Decisão: `condition`
- Autoridade: Example Design Authority
- Data: 2026-08-01
- Expiração: 2026-11-01

## Evidências aceitas

- [Arquitetura](architecture.example.md)
- [Avaliação de risco](risk-assessment.example.md)
- [Relatório de avaliação](evaluation-report.example.md)
- [Runbook de suporte](support-runbook.example.md)
- [SLO](slo.example.md)

## Condições

1. respostas externas exigem revisão humana;
2. dados pessoais e credenciais permanecem proibidos;
3. qualquer novo conector ou ferramenta que altere estado retorna a G4/G5;
4. quarentena e rollback devem ser exercitados antes da reativação após incidente.

Estas quatro condições são transportadas em forma legível por máquina por
[`release-evidence-manifest.example.json`](release-evidence-manifest.example.json), cada uma com um
owner e um método de verificação declarado. Uma condição que existe apenas em prosa não pode ser verificada
no próximo gate.

## Rationale

O escopo limitado de leitura e rascunho, o pacote de evidências e o caminho de revogação suportam release condicional. A decisão não cobre novas populações, ferramentas, classes de dados ou versões de modelo.

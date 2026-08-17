---
title: Patterns de governança de agentes
status: maintained
owner: framework-maintainers
last_reviewed: 2026-08-17
review_cycle: quarterly
related:
  - ../artifact-catalog.md
  - ../../docs/framework/06-architecture-and-technical-controls.md
---

# Patterns de governança de agentes

Patterns são soluções recorrentes para problemas de desenho. Eles mostram contexto, forças, trade-offs, estrutura, controles e evidências esperadas. **Não são requirements normativos nem produtos prescritos.** A política e os controls definem o resultado obrigatório; o pattern ajuda a implementar uma opção coerente e adaptável.

## Escolha por problema de decisão

| Pattern | Use quando | Saída principal | Capítulo ou decisão relacionada | Trade-off central |
|---|---|---|---|---|
| [Control and Assurance Planes](control-and-assurance-planes.md) | control plane e assurance plane estão misturados ou sem owner claro | boundaries, owners, evidence flow e enforcement points | Cap. 06–07; G2–G5 | centralização de controles versus autonomia de domínio |
| [Multi-Control-Plane Governance](multi-control-plane-governance.md) | múltiplos control planes, gateways ou systems of record participam da mesma decisão | authority matrix, precedence, correlation, conflict path e fail-safe | ADR-0015; Cap. 02 e 06 | interoperabilidade versus precedência e disponibilidade |
| [Multi-Agent Delegation Governance](multi-agent-delegation-governance.md) | agentes coordenam ou delegam tarefas entre supervisor, worker, reviewer ou router | topology, delegation edges, authority attenuation, limits e failure propagation | ADR-0013; Cap. 06 e 09 | autonomia e escala versus transitive trust e blast radius |
| [AI-Native Observability Profile](ai-native-observability-profile.md) | task, model, retrieval, tool, policy, memory e delegation precisam ser reconstruíveis | correlation, provenance, redaction, alert-to-action, containment e value/cost separation | ADR-0014; Cap. 07 e 09 | cobertura e interoperabilidade versus cardinalidade, custo e privacidade |
| [Evidence Package as Code](evidence-package-as-code.md) | evidence precisa ser recuperável, versionada e verificável em escala | manifest, lineage, checks e resultado de validação | Cap. 07; release e attestation | automação versus completude e custo de manutenção |
| [Federated Governance Operating Model](federated-governance-operating-model.md) | authorities de negócio, risco, dados, segurança e operação precisam atuar sem um novo silo central | decision rights, handoffs, fórum e escalation path | Cap. 02; G0–G1 | autonomia local versus baseline comum |
| [Registry and Blueprint](registry-and-blueprint.md) | inventário e configuração técnica estão confundidos ou há múltiplas plataformas | registry record, blueprint versionado e reconciliação de estado | Cap. 03 e 06; G2 | source of truth versus fontes distribuídas |
| [Risk-Tiered Governance](risk-tiered-governance.md) | o portfolio exige proporcionalidade sem abrir mão de rigor em alto impacto | rota de tier/admissibilidade, evidence bar e authority | Cap. 04; G3–G4 | consistência versus contexto e falsa precisão |
| [Runtime Observability and Quarantine](runtime-observability-and-quarantine.md) | sinais não viram ações de contenção ou o runtime não é correlacionável | telemetry, alert-to-action, containment e reactivation path | Cap. 09; operação | sensibilidade versus alert fatigue e disponibilidade versus segurança |

## Como usar um pattern

1. **Confirme o problema.** O pattern não deve ser escolhido porque está disponível, mas porque resolve o problema e seus trade-offs são aceitáveis.
2. **Aplique os controls e o tier.** O pattern não reduz controles mínimos nem transforma admissibilidade em escolha arquitetural.
3. **Produza os artefatos.** Abra os templates, schemas, records e exemplos ligados ao pattern; eles tornam a escolha verificável.
4. **Registre a decisão.** Quando houver alternativa relevante, dívida técnica, exceção ou impacto de longo prazo, use ADR ou decision record.
5. **Meça em runtime.** Um pattern só se prova adequado quando os sinais, evidências e failure modes previstos permanecem aceitáveis em operação.

## Limites

Um pattern pode ser combinado com outros patterns, mas não deve ser usado para alegar conformidade automática, substituir threat model, dispensar avaliação de impacto ou contornar decision gates. Nomes de produtos em mappings servem como exemplo de implementação e podem ser removidos sem alterar a regra canônica.

Para localizar o artefato necessário em cada fase, consulte o [catálogo de artefatos](../artifact-catalog.md). Para estudar a arquitetura antes de escolher um pattern, consulte o [capítulo 06](../../docs/framework/06-architecture-and-technical-controls.md).

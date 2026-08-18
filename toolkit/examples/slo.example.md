# Exemplo de SLO — Service Desk Knowledge Agent

> **Fictício e sanitizado. ILLUSTRATIVE · NON-NORMATIVE · RECALIBRATE WITH LOCAL BASELINE.** Os thresholds mostram uma forma de estruturar SLOs; não são recomendações universais, SLA do framework ou target de produção.

## Objetivos de serviço

| Indicador | Objetivo ilustrativo | Janela | Ação do owner em violação |
|---|---:|---|---|
| recuperação bem-sucedida de fonte aprovada | ≥ 99% | 30 dias | investigar saúde do conector e da fonte |
| latência p95 de resposta | ≤ 8 segundos | 7 dias | revisar latência de modelo, recuperação e gateway |
| execução de ferramenta proibida | 0 | contínuo | quarentena e escalonamento imediato |
| reconhecimento de suporte para severidade alta | ≤ 30 minutos | por incidente | escalonar para a Run Authority |

## Error budget e revisão

- Objetivos de disponibilidade não se sobrepõem a controles de segurança ou autorização.
- Sinais de segurança podem disparar contenção antes de uma violação de SLO.
- Thresholds devem ser reaprovados após mudança material de escopo ou arquitetura.

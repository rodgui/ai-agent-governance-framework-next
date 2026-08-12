# Sunset Plan — Descomissionamento Controlado de Agentes

Use quando um agente for sinalizado para descomissionamento.

---

Appendix D – Sunset Plan (descomissionamento controlado de agentes)
Objetivo: evitar "zumbis" (agentes sem owner, duplicados, não utilizados) e reduzir risco/custo.
Quando um agente entra em Sunset
Nenhum Business Owner ou Technical Owner definido
Não está no Catálogo
Sem logs/telemetria mínimos
Sem uso por N dias (ex.: 90)
Agente duplicado / substituído por uma versão oficial
Plataforma não é mais aprovada
Incidente grave não remediado dentro do prazo
Processo padrão (3 fases)
Aviso (D0): agente marcado como "Sunset Candidate"
Notifica owners + Run Authority
Define prazo de remediação (ex.: 15 dias)
Quarentena (D+15): limitações
Desabilita ações de escrita, reduz escopo, limita usuários
Mantém logs e evidências
Desativação (D+30): desativa
Remove acesso, desabilita integrações, revoga identidade
Registra o motivo e artefatos no Catálogo
(Opcional) arquiva configurações por X dias para rollback
Itens obrigatórios no Sunset
Data de início do sunset, motivo, owner responsável
Plano de migração (se houver substituto)
Evidência de comunicação aos usuários
Retenção de logs após a desativação (por risco)

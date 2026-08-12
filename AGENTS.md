# AGENTS.md — AI Agent Governance Framework Next

## Missão

Manter o framework de governança canônico e vendor-neutral para agentes de IA. O repositório deve explicar o caminho completo desde a ausência de governança formal até a operação sustentada no business as usual e deve manter policy, controles, evidências e orientação de implementação rastreáveis.

## Fronteiras canônicas

- Este repositório é a autoridade para o framework, o catálogo de controles, os padrões de design, os templates reutilizáveis, os schemas, os exemplos fictícios, os crosswalks de pesquisa e os registros de manutenção do framework.
- Não adicionar material comercial, de vendas ou de entrega específico de clientes, nem evidências organizacionais reais.
- Não adicionar dados de clientes, do empregador ou de usuários. Exemplos devem ser comprovadamente fictícios.
- Implementações de fornecedores podem aparecer somente como exemplos ou mappings não normativos; requisitos normativos devem permanecer vendor-neutral.

## Regras de documentação

- Preservar definições, rationale, condições, exceções, procedimentos, controles, evidências e exemplos. Não substituir material detalhado por resumos genéricos.
- Definir termos especializados e expandir abreviações no primeiro uso.
- Todo requisito normativo deve identificar aplicabilidade, papel responsável, evidência esperada e método de validação, diretamente ou por um link inequívoco.
- Vincular capítulos a controles, padrões, templates, schemas e exemplos em vez de duplicar cópias divergentes.
- Citar fontes primárias. Rotular distintamente interpretação legal, requisitos normativos, orientação e observações de estudo de caso.

## Disciplina de mudanças

1. Identificar requisitos, controles, artefatos e crosswalks afetados.
2. Atualizar o conteúdo canônico e toda referência dependente na mesma mudança.
3. Adicionar ou atualizar testes quando um schema, control ID, regra de validação ou gerador mudar.
4. Atualizar `CHANGELOG.md` para mudanças visíveis ao usuário.
5. Registrar decisões arquiteturais ou de governança materiais em `project/decisions/`.
6. Nunca reescrever provenance de migração ou decisões históricas silenciosamente.

## Validação obrigatória

Antes de commitar, execute o ponto de entrada de validação do repositório documentado em `README.md`. No mínimo, valide estrutura Markdown, links internos, build MkDocs, schemas JSON, exemplos, IDs, referências cruzadas, testes Python, varredura de segredos e restrições de dados fictícios.

## Ações proibidas

- Não modificar `/Users/rodgui/Nox/Projects/ai-agent-governance-framework`.
- Não publicar, criar remotes ou fazer push sem aprovação explícita de Rodgui.
- Não introduzir credenciais, tokens, dados pessoais ou informações corporativas confidenciais.
- Não resolver contradição material nem excluir conteúdo substantivo sem decisão registrada.

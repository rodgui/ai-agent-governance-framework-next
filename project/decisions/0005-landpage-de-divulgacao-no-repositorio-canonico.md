---
title: 0005 Landpage de divulgação no repositório canônico
status: maintained
last_reviewed: 2026-09-13
review_cycle: quarterly
source_commit: 5545d9227624400ab8bb707b6032b2f61329a36e
---

# 0005 Landpage de divulgação no repositório canônico

## Contexto

O `AGENTS.md` estabelece que este repositório não deve receber material comercial, de
vendas ou de entrega específico de clientes. Uma página de apresentação pública do
framework, com convite para contato, é material de divulgação e fica na zona de fronteira
dessa regra.

A alternativa era manter a página num repositório separado. Ela foi descartada por um
motivo operacional concreto: o domínio `aiframework.rodgui.com` já publica este
repositório por um cron que faz `git pull`, build do MkDocs e `rsync --delete` para o
docroot. Manter a página fora exigiria um segundo pipeline, um segundo ponto de falha e um
passo de deploy invisível no servidor.

## Decisão

Manter a landpage em `landpage/`, dentro do repositório canônico, sob quatro condições:

1. **Não é conteúdo normativo.** Nada em `landpage/` define requisito, control, evidência
   ou decisão. O conteúdo é derivado dos capítulos e do brief executivo; em divergência,
   prevalece o capítulo e a página é corrigida.
2. **Não contém oferta comercial.** A página apresenta o framework e convida ao contato.
   Preço, pacote, escopo de entrega e proposta permanecem fora do repositório.
3. **Respeita a neutralidade.** A página não recomenda produto, plataforma ou fornecedor
   para implantar o framework.
4. **Declara os próprios limites.** A página reproduz o aviso de maturidade do framework,
   incluindo que nenhum control foi exercitado contra um estate real.

O diretório é publicado por `tools/build-docs-site.py`, que copia apenas arquivos
servíveis para `site/landpage/`. Documentação interna do diretório e o gerador de imagens
não vão para o site.

## Rationale

A regra do `AGENTS.md` protege contra dois riscos: que material de venda se misture ao
corpo normativo, e que um leitor confunda conhecimento canônico com produto. As quatro
condições acima endereçam ambos diretamente, com separação de diretório, ausência de
oferta e precedência explícita do capítulo.

O texto do artigo de divulgação que aponta para a página é mantido fora do repositório,
por decisão do mantenedor.

## Consequências

- Um diretório do repositório canônico passa a conter material não normativo, o que exige
  que a fronteira seja relida a cada mudança em `landpage/`.
- Os números citados na página precisam ser reconferidos a cada release. A ausência de
  verificação automatizada desse ponto é uma lacuna conhecida.
- O `tools/scripts/test_build_docs_site_landpage.py` cobre a publicação, não o conteúdo.

## Authority

Rodrigo Garcia Guimarães, autor e mantenedor do framework.

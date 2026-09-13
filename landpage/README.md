# Landpage

Página estática de apresentação pública do framework, destinada ao domínio
`aiframework.rodgui.com`. Não é conteúdo normativo e não integra o Master Document.

## Boundary

Este diretório contém material de divulgação, não policy. Nada aqui define requisito,
control, evidência ou decisão. O conteúdo da página é derivado dos capítulos canônicos
e do brief executivo; quando os dois divergirem, o capítulo prevalece e a página é
corrigida, nunca o contrário.

A página não recomenda produto, plataforma ou fornecedor para implantar o framework,
que é o que a neutralidade exige. Citar fonte de estudo é outra coisa e não conflita
com essa regra.

Os números citados na página (11 capítulos, 44 controls, 15 domínios, 9 schemas,
28 templates, 13 patterns) precisam ser reconferidos a cada release do framework.

## Arquivos

- `index.html` — documento standalone, sem dependência de build. Estilos embutidos;
  as únicas requisições externas são as fontes.
- `og-image.png` — imagem de prévia social, 1200x630, referenciada por `og:image`.
- `make-og-image.py` — gerador determinístico dessa imagem, usando as fontes DejaVu
  versionadas em `tools/assets/fonts`. Reexecutar quando os números da página mudarem:

  ```bash
  uv run --no-project --with pillow python3 landpage/make-og-image.py
  ```

O texto do artigo de divulgação que aponta para esta página é mantido fora do repositório,
por decisão do mantenedor.

## Publicação

O pipeline de documentação **não** carrega este diretório. `tools/build-docs-site.py`
copia apenas `.md`, `.json`, `.csv`, `.png`, `.svg` e `.py` das pastas de conteúdo, e o
MkDocs ignora HTML avulso. Portanto `git pull` na VPS traz o arquivo para o clone, mas
não o coloca no docroot.

Para publicar, uma destas duas opções precisa ser implementada:

1. **No script da VPS** — acrescentar ao `deploy-framework.sh`, depois do build, uma cópia
   de `landpage/` para o docroot. Verificar antes se o `rsync` do site usa `--delete`:
   se usar, a cópia precisa acontecer depois da sincronização, ou o arquivo é apagado na
   rodada seguinte.
2. **No build do repositório** — fazer `tools/build-docs-site.py` copiar `landpage/` para
   dentro de `site/` ao final da construção, de modo que a publicação existente leve a
   página junto sem nenhuma mudança na VPS.

## Estado do arquivo

Pronto para servir. `og:url`, `og:image` e `canonical` apontam para
`https://aiframework.rodgui.com/landpage/`; se o caminho final for outro, os três precisam
mudar juntos, senão a prévia do link quebra. O favicon é um SVG embutido como data URI,
então não há requisição nem 404 de ícone.

O deploy precisa servir `og-image.png` no mesmo diretório de `index.html`. Rastreadores
sociais buscam a imagem pela URL absoluta declarada e não seguem redirecionamento de
caminho relativo.

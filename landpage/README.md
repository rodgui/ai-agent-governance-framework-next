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

- `index.html` — documento standalone, sem dependência de build nem requisição externa:
  estilos embutidos e fontes servidas do próprio diretório.
- `fonts/` — subsets WOFF2 de Spectral e IBM Plex, com o aviso de licença em
  `fonts/LICENSE.md`. Hospedados localmente para que a página funcione sob uma CSP
  restrita a `'self'` e não entregue o IP do visitante a terceiros.
- `og-image.png` — imagem de prévia social, 1200x630, referenciada por `og:image`.
- `make-og-image.py` — gerador determinístico dessa imagem, usando as fontes DejaVu
  versionadas em `tools/assets/fonts`. Reexecutar quando os números da página mudarem:

  ```bash
  uv run --no-project --with pillow python3 landpage/make-og-image.py
  ```

O texto do artigo de divulgação que aponta para esta página é mantido fora do repositório,
por decisão do mantenedor.

## Publicação

O MkDocs ignora HTML avulso, então a página não é um capítulo do site derivado. Ela é
copiada para dentro de `site/landpage/` por `tools/build-docs-site.py`, depois do build,
preservada byte a byte. A publicação existente carrega a pasta junto, sem passo extra:

```text
git pull  →  build MkDocs  →  cópia da landpage para site/landpage/
          →  rsync --delete de site/ para o docroot
```

Só entram no site os arquivos servíveis (`.html`, `.png`, `.svg`, `.ico`, `.woff2`,
`.css`, `.js`) mais `fonts/LICENSE.md`, exigido pela licença das fontes. Este README e o
gerador da imagem ficam fora.

O `rsync` de publicação usa `--delete`. Por isso a landpage precisa chegar ao docroot
**dentro** de `site/`: qualquer arquivo copiado direto para o docroot é apagado na
sincronização seguinte.

A rota é servida por um recorte público no bloco do Caddy de `aiframework.rodgui.com`.
O restante daquele host continua atrás de `basic_auth` e marcado como `noindex`; apenas
`/landpage*` é público e indexável, com CSP própria restrita a `'self'`.

## Estado do arquivo

Pronto para servir. `og:url`, `og:image` e `canonical` apontam para
`https://aiframework.rodgui.com/landpage/`; se o caminho final for outro, os três precisam
mudar juntos, senão a prévia do link quebra. O favicon é um SVG embutido como data URI,
então não há requisição nem 404 de ícone.

O deploy precisa servir `og-image.png` no mesmo diretório de `index.html`. Rastreadores
sociais buscam a imagem pela URL absoluta declarada e não seguem redirecionamento de
caminho relativo.

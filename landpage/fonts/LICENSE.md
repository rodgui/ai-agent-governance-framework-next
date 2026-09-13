# Fontes da landpage

Subsets `latin` e `latin-ext` em WOFF2, hospedados localmente para que a página não
faça nenhuma requisição a terceiros e funcione sob uma Content Security Policy
restrita a `'self'`.

| Família | Estilos incluídos | Licença |
|---|---|---|
| Spectral | 500, 600, 700 e 400 itálico | SIL Open Font License 1.1 |
| IBM Plex Sans | 400 e 600 | SIL Open Font License 1.1 |
| IBM Plex Mono | 400 e 600 | SIL Open Font License 1.1 |

A OFL 1.1 permite uso, redistribuição e incorporação, inclusive comercial, desde que
os arquivos não sejam vendidos isoladamente e que o aviso de licença acompanhe a
redistribuição. É o mesmo regime da DejaVu já versionada em `tools/assets/fonts`.

Texto da licença e arquivos originais:

- Spectral, por Production Type: <https://fonts.google.com/specimen/Spectral/license>
- IBM Plex, por IBM: <https://github.com/IBM/plex/blob/master/LICENSE.txt>
- Texto da OFL 1.1: <https://openfontlicense.org/>

Os arquivos foram obtidos da API do Google Fonts em 2026-09-12, preservando os
`unicode-range` originais de cada subset. Para atualizá-los, refazer o mesmo recorte
e manter a correspondência entre `@font-face` e arquivo.

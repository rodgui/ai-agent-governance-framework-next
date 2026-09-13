#!/usr/bin/env python3
"""Gera a imagem de prévia social da landpage (1200x630).

Output determinístico: o mesmo input produz o mesmo arquivo. Usa as fontes DejaVu
versionadas em ``tools/assets/fonts`` para render idêntico em qualquer sistema.

    uv run --no-project --with pillow python3 landpage/make-og-image.py
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = ROOT / "tools" / "assets" / "fonts"
OUTPUT = Path(__file__).resolve().parent / "og-image.png"

WIDTH, HEIGHT = 1200, 630
MARGIN = 76

# Paleta da landpage, no modo escuro: contrasta com o feed claro do LinkedIn.
GROUND = (12, 17, 23)
PAPER = (19, 26, 34)
INK = (232, 238, 244)
INK_SOFT = (157, 172, 186)
INK_FAINT = (110, 124, 138)
ACCENT = (143, 180, 228)
RULE = (42, 54, 67)

TITLE = ["Governar agentes de IA", "com evidência,", "não com intenção"]
EYEBROW = "FRAMEWORK CANÔNICO   ·   VENDOR-NEUTRAL   ·   PORTUGUÊS"
FIGURES = [
    ("11", "CAPÍTULOS"),
    ("44", "CONTROLES"),
    ("15", "DOMÍNIOS"),
    ("9", "SCHEMAS"),
    ("28", "TEMPLATES"),
]
DOMAIN = "aiframework.rodgui.com"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    path = FONT_DIR / name
    if not path.exists():
        raise SystemExit(f"fonte ausente: {path}")
    return ImageFont.truetype(str(path), size)


def tracked(draw: ImageDraw.ImageDraw, xy, text, fnt, fill, tracking: int) -> int:
    """Desenha texto com espaçamento entre letras e devolve a largura ocupada."""
    x, y = xy
    for char in text:
        draw.text((x, y), char, font=fnt, fill=fill)
        x += draw.textlength(char, font=fnt) + tracking
    return int(x - xy[0] - tracking)


def main() -> int:
    image = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
    draw = ImageDraw.Draw(image)

    # Faixa de acento no topo, o mesmo recurso do cabeçalho da landpage.
    draw.rectangle([(0, 0), (WIDTH, 8)], fill=ACCENT)
    # Rodapé sobre o fundo mais escuro, para assentar a composição.
    draw.rectangle([(0, HEIGHT - 108), (WIDTH, HEIGHT)], fill=GROUND)

    y = 84
    tracked(draw, (MARGIN, y), EYEBROW, font(15, bold=True), INK_FAINT, 2)

    y += 58
    title_font = font(58, bold=True)
    for line in TITLE:
        draw.text((MARGIN, y), line, font=title_font, fill=INK)
        y += 74

    y += 24
    draw.line([(MARGIN, y), (WIDTH - MARGIN, y)], fill=RULE, width=1)

    y += 42
    number_font = font(46, bold=True)
    label_font = font(13, bold=True)
    x = MARGIN
    for index, (number, label) in enumerate(FIGURES):
        draw.text((x, y), number, font=number_font, fill=ACCENT)
        tracked(draw, (x + 3, y + 60), label, label_font, INK_FAINT, 1.6)
        x += 152
        if index < len(FIGURES) - 1:
            draw.line([(x - 38, y + 6), (x - 38, y + 74)], fill=RULE, width=1)

    footer_font = font(18)
    bbox = draw.textbbox((0, 0), DOMAIN, font=footer_font)
    footer_y = HEIGHT - 54 - (bbox[3] - bbox[1]) // 2
    draw.text((MARGIN, footer_y), DOMAIN, font=footer_font, fill=INK_SOFT)
    tracked(
        draw,
        (WIDTH - MARGIN - 236, footer_y + 2),
        "RELEASE 1.1.0   ·   CC BY 4.0",
        font(14, bold=True),
        INK_FAINT,
        1.4,
    )

    image.save(OUTPUT, "PNG", optimize=True)
    print(f"gerado: {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

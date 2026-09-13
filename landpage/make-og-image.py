#!/usr/bin/env python3
"""Gera as imagens de divulgação do framework.

Duas variantes, mesma linguagem visual:

``og``      1200x630, prévia de link. Referenciada por ``og:image`` na landpage e
            servida junto com ela. É a imagem que aparece quando alguém cola a URL.
``banner``  1920x1080, cabeçalho de artigo do LinkedIn. Não integra a landpage;
            use ``--output-dir`` para escrevê-la onde o material de divulgação vive.

Output determinístico: o mesmo input produz o mesmo arquivo. Usa as fontes DejaVu
versionadas em ``tools/assets/fonts`` para render idêntico em qualquer sistema.

    uv run --no-project --with pillow python3 landpage/make-og-image.py
    uv run --no-project --with pillow python3 landpage/make-og-image.py --variant banner
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = ROOT / "tools" / "assets" / "fonts"
HERE = Path(__file__).resolve().parent

# Paleta da landpage, no modo escuro: contrasta com o feed claro do LinkedIn.
GROUND = (12, 17, 23)
PAPER = (19, 26, 34)
INK = (232, 238, 244)
INK_SOFT = (157, 172, 186)
INK_FAINT = (110, 124, 138)
ACCENT = (143, 180, 228)
RULE = (42, 54, 67)

EYEBROW = "FRAMEWORK CANÔNICO   ·   VENDOR-NEUTRAL   ·   PORTUGUÊS"
TITLE = ["Governar agentes de IA", "com evidência,", "não com intenção"]
SUBTITLE = "Do mandato executivo ao runtime, para quem já tem agentes em produção."
FIGURES = [
    ("11", "CAPÍTULOS"),
    ("44", "CONTROLES"),
    ("15", "DOMÍNIOS"),
    ("9", "SCHEMAS"),
    ("28", "TEMPLATES"),
]
DOMAIN = "aiframework.rodgui.com"
CREDITS = "RELEASE 1.1.0   ·   CC BY 4.0"

# nome: largura, altura, escala, mostra subtítulo, arquivo
VARIANTS = {
    "og": (1200, 630, 1.0, False, "og-image.png"),
    "banner": (1920, 1080, 1.6, True, "article-banner.png"),
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_DIR / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
    if not path.exists():
        raise SystemExit(f"fonte ausente: {path}")
    return ImageFont.truetype(str(path), size)


def tracked(draw: ImageDraw.ImageDraw, xy, text, fnt, fill, tracking: float) -> None:
    """Desenha texto com espaçamento entre letras, que o Pillow não oferece nativamente."""
    x, y = xy
    for char in text:
        draw.text((x, y), char, font=fnt, fill=fill)
        x += draw.textlength(char, font=fnt) + tracking


def render(variant: str, output_dir: Path) -> Path:
    width, height, scale, with_subtitle, filename = VARIANTS[variant]

    def s(value: float) -> int:
        return int(round(value * scale))

    margin = s(76)
    image = Image.new("RGB", (width, height), PAPER)
    draw = ImageDraw.Draw(image)
    draw.rectangle([(0, 0), (width, s(8))], fill=ACCENT)
    draw.rectangle([(0, height - s(108)), (width, height)], fill=GROUND)

    y = s(84)
    tracked(draw, (margin, y), EYEBROW, font(s(15), bold=True), INK_FAINT, s(2))

    y += s(58)
    title_font = font(s(58), bold=True)
    for line in TITLE:
        draw.text((margin, y), line, font=title_font, fill=INK)
        y += s(74)

    if with_subtitle:
        y += s(10)
        draw.text((margin, y), SUBTITLE, font=font(s(22)), fill=INK_SOFT)
        y += s(36)

    y += s(22)
    draw.line([(margin, y), (width - margin, y)], fill=RULE, width=max(1, s(1)))

    y += s(38)
    number_font = font(s(46), bold=True)
    label_font = font(s(13), bold=True)
    x = margin
    for index, (number, label) in enumerate(FIGURES):
        draw.text((x, y), number, font=number_font, fill=ACCENT)
        tracked(draw, (x + s(3), y + s(60)), label, label_font, INK_FAINT, s(1.6))
        x += s(152)
        if index < len(FIGURES) - 1:
            draw.line(
                [(x - s(38), y + s(6)), (x - s(38), y + s(74))],
                fill=RULE,
                width=max(1, s(1)),
            )

    footer_font = font(s(18))
    box = draw.textbbox((0, 0), DOMAIN, font=footer_font)
    footer_y = height - s(54) - (box[3] - box[1]) // 2
    draw.text((margin, footer_y), DOMAIN, font=footer_font, fill=INK_SOFT)
    tracked(
        draw,
        (width - margin - s(236), footer_y + s(2)),
        CREDITS,
        font(s(14), bold=True),
        INK_FAINT,
        s(1.4),
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / filename
    image.save(destination, "PNG", optimize=True)
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--variant", choices=sorted(VARIANTS) + ["all"], default="og")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=HERE,
        help="diretório de saída; por padrão, ao lado deste script",
    )
    args = parser.parse_args()

    for name in sorted(VARIANTS) if args.variant == "all" else [args.variant]:
        destination = render(name, args.output_dir.expanduser())
        width, height = VARIANTS[name][0], VARIANTS[name][1]
        print(f"{name}: {destination} ({width}x{height}, {destination.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

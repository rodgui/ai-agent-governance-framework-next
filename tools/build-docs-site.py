#!/usr/bin/env python3
"""Monta um site de documentação derivado a partir da árvore normalizada do repositório.

Markdown e contratos estruturados permanecem canônicos no lugar. Este script os copia
para ``site_src`` sem alterar caminhos e então pede ao MkDocs que construa o site
derivado. Ele nunca publica e nunca edita o corpus canônico.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "site_src"

# Pastas de conteúdo editorial publicadas. Tooling, testes e regras de maintainer
# permanecem no repositório, mas não entram na jornada pública do site.
CONTENT_DIRS = (
    "docs",
    "toolkit",
    "research",
    "project",
)
CONTENT_FILES = ("README.md", "CONSUMO.md", "CHANGELOG.md", "ROADMAP.md", "LICENSE", "CONTRIBUTING.md")

# Extensões copiadas para a área de staging. Schemas e exemplos são publicados como
# fonte para que o leitor possa inspecionar o contrato, não apenas sua descrição.
# Arquivos de manutenção são publicados somente quando declarados em CONTENT_FILES.
PUBLISHED_SUFFIXES = {".md", ".json", ".csv", ".png", ".svg", ".py"}

# O histórico de fonte preservado byte a byte retém intencionalmente referências da era da
# fonte. O site derivado reescreve somente sua cópia em staging para que a navegação estrita
# resolva os novos caminhos do repositório sem alterar artefatos de provenance.
STAGED_HISTORICAL_LINK_REWRITES = {
    "project/history/SOURCE_CHANGELOG.md": {
        "docs/architecture/decisions/0009-risk-tier-and-admissibility.md": (
            "../../docs/architecture/decisions/0009-risk-tier-and-admissibility.md"
        ),
        "docs/architecture/decisions/0010-structured-governance-contracts-2.0.md": (
            "../../docs/architecture/decisions/0010-structured-governance-contracts-2.0.md"
        ),
        "docs/architecture/decisions/0008-manual-documentation-site-publication.md": (
            "../decisions/0002-derived-documentation-build-and-publication.md"
        ),
        "docs/architecture/decisions/0006-framework-release-1-0-adoption.md": (
            "../decisions/source-history/0006-framework-release-1-0-adoption.md"
        ),
        "docs/architecture/decisions/0005-control-catalog-scope-verification-and-mappings.md": (
            "source-repository/adrs/0005-control-catalog-scope-verification-and-mappings.md"
        ),
    },
    "project/history/assessments/microsoft-case-study-framework-crosswalk.md": {
        "../../docs/governance/ai-agent-policy-and-governance-v1.md": (
            "../ai-agent-policy-and-governance-v1.md"
        ),
        "../../docs/architecture/decisions/0002-modular-policy-vendor-neutrality-and-commercial-boundary.md": (
            "../source-repository/adrs/0002-modular-policy-vendor-neutrality-and-commercial-boundary.md"
        ),
    },
    "project/history/source-repository/adrs/0005-control-catalog-scope-verification-and-mappings.md": {
        "0010-structured-governance-contracts-2.0.md": (
            "../../../../docs/architecture/decisions/0010-structured-governance-contracts-2.0.md"
        ),
    },
}


def rewrite_staged_historical_references(staging: Path = STAGING) -> int:
    rewrites = 0
    for relative_path, replacements in STAGED_HISTORICAL_LINK_REWRITES.items():
        target = staging / relative_path
        if not target.is_file():
            continue
        original = target.read_text(encoding="utf-8")
        updated = original
        for old, new in replacements.items():
            occurrences = updated.count(old)
            updated = updated.replace(old, new)
            rewrites += occurrences
        if updated != original:
            target.write_text(updated, encoding="utf-8")
    return rewrites


def stage() -> None:
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)

    for name in CONTENT_FILES:
        source = ROOT / name
        if source.exists():
            shutil.copy2(source, STAGING / name)

    for directory in CONTENT_DIRS:
        source_root = ROOT / directory
        if not source_root.is_dir():
            continue
        for source in sorted(source_root.rglob("*")):
            if source.is_dir() or source.suffix.lower() not in PUBLISHED_SUFFIXES:
                continue
            destination = STAGING / source.relative_to(ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

    copied = sum(1 for path in STAGING.rglob("*") if path.is_file())
    if copied == 0:
        raise RuntimeError("documentation staging produced zero files")
    historical_rewrites = rewrite_staged_historical_references()
    print(
        f"staged {copied} files into {STAGING.relative_to(ROOT)} "
        f"({historical_rewrites} historical link rewrites in staging only)"
    )


def build(strict: bool, serve: bool) -> int:
    command = [sys.executable, "-m", "mkdocs", "serve" if serve else "build"]
    if strict:
        command.append("--strict")
    return subprocess.call(command, cwd=ROOT)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--serve", action="store_true", help="serve locally instead of building")
    parser.add_argument("--no-strict", action="store_true", help="allow warnings")
    parser.add_argument("--stage-only", action="store_true", help="only assemble site_src")
    args = parser.parse_args()

    stage()
    if args.stage_only:
        return 0
    return build(strict=not args.no_strict, serve=args.serve)


if __name__ == "__main__":
    raise SystemExit(main())

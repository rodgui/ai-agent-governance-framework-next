"""Regression tests for the first semantic/editorial hardening wave."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class SemanticHardeningTests(unittest.TestCase):
    def read(self, relative_path: str) -> str:
        return (ROOT / relative_path).read_text(encoding="utf-8")

    def test_discovery_status_has_one_canonical_vocabulary(self) -> None:
        schema = json.loads(self.read("toolkit/schemas/agent-registry.schema.json"))
        discovery_status = schema["properties"]["discovery"]["properties"]["status"]["enum"]
        self.assertEqual(discovery_status, ["confirmed", "probable", "suspected"])

        chapter = self.read("docs/framework/03-inventory-portfolio-and-value.md")
        template = self.read("toolkit/templates/agent-registry-template.md")
        glossary = self.read("docs/annexes/glossary.md")
        for value in ("confirmed", "probable", "suspected"):
            self.assertIn(f"`{value}`", chapter)
            self.assertIn(f"`{value}`", template)
        self.assertIn("não são valores de `discovery.status`", chapter)
        self.assertIn("não são valores desse campo", template)
        self.assertIn("**Discovery status**", glossary)

    def test_program_uses_waves_without_lifecycle_collision(self) -> None:
        implementation = self.read("docs/framework/08-implementation-and-adoption.md")
        catalog = self.read("toolkit/artifact-catalog.md")
        lifecycle = self.read("docs/framework/05-agent-lifecycle.md")

        self.assertIn("Implementation Waves W0–W6", implementation)
        self.assertIn("W0 — Mobilizar", implementation)
        self.assertIn("W6 — Institucionalizar", implementation)
        self.assertIn("lifecycle phases F1–F8", implementation)
        self.assertIn("Typical implementation wave", catalog)
        self.assertIn("W0", catalog)
        self.assertNotRegex(catalog, r"\| F[0-6](?:[/+]| \|)")
        self.assertIn("F1. Ideia e intake", lifecycle)
        self.assertIn("F8. Contenção e retirada", lifecycle)

    def test_metadata_dimensions_are_explicit(self) -> None:
        document_control = self.read("docs/framework/00-document-control.md")
        glossary = self.read("docs/annexes/glossary.md")
        self.assertIn("estado documental/editorial", document_control)
        self.assertIn("estado da decisão", document_control)
        self.assertIn("maturidade/evidence", document_control)
        self.assertIn("**Document/editorial status**", glossary)
        self.assertIn("**Decision status**", glossary)
        self.assertIn("**Maturity/evidence status**", glossary)
        self.assertIn("**Artifact type**", glossary)

    def test_gate_anchor_and_navigation_target_are_consistent(self) -> None:
        implementation = self.read("docs/framework/08-implementation-and-adoption.md")
        self.assertIn("[contrato comum dos gates](#11-o-contrato-comum-dos-decision-gates)", implementation)
        self.assertNotIn("#contrato-comum-dos-decision-gates)", implementation)

    def test_core_does_not_use_historical_terms(self) -> None:
        core = "\n".join(
            self.read(path)
            for path in (
                "docs/framework/04-risk-impact-and-compliance.md",
                "docs/framework/05-agent-lifecycle.md",
            )
        )
        for legacy_term in ("Grupo/Segmento/Local", "Governed Agent", "OWCR", "conforme a Matriz"):
            self.assertNotIn(legacy_term, core)
        self.assertIn("decision rights", core)
        self.assertIn("exception authority", core)


if __name__ == "__main__":
    unittest.main()

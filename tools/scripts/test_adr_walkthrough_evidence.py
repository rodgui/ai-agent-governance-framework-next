#!/usr/bin/env python3
"""Verify that the canonical fictional walkthrough evidence remains complete.

These tests protect documentation evidence, not production effectiveness. They
must not be interpreted as human authority approval or production evidence.
"""
from __future__ import annotations

from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = REPO_ROOT / "toolkit" / "examples"


def read_example(name: str) -> str:
    return (EXAMPLES / name).read_text(encoding="utf-8")


class AdrWalkthroughEvidenceTests(unittest.TestCase):
    def test_g1_conflict_example_preserves_composed_authorization_and_fail_safe(self) -> None:
        text = read_example("multi-control-plane-conflict.example.md")
        for required in (
            "## Matriz de interação",
            "## Decisão",
            "tool gateway",
            "`deny`",
            "`correlation_id",
            "## Teste de indisponibilidade",
            "`restricted` ou `quarantined`",
            "retry não amplia privilégio",
        ):
            self.assertIn(required, text)

    def test_g2_example_covers_the_three_required_scenarios(self) -> None:
        text = read_example("supervisor-worker-delegation.example.md")
        for required in (
            "Delegação permitida e concluída",
            "Tentativa de privilege escalation",
            "Worker state-changing falha",
            "maxDepth",
            "maxFanOut",
            "expiresAt",
            "revocationRef",
            "child envelope é menor",
            "supervisor não é authority absoluta",
        ):
            self.assertIn(required, text)

    def test_g4_operational_drill_covers_open_operational_dimensions(self) -> None:
        text = read_example("ai-native-observability-operational-drill.example.md")
        for required in (
            "## 2. Redaction e minimização",
            "## 3. Deletion drill de memory/state",
            "primary",
            "cache",
            "index",
            "backup",
            "evidence hold",
            "## 4. Cardinalidade e custo",
            "events por task",
            "custo de telemetry",
        ):
            self.assertIn(required, text)

    def test_substitution_drill_keeps_vendor_neutral_boundary(self) -> None:
        text = read_example("orchestrator-substitution-replay.example.md")
        for required in (
            "duas implementações abstratas",
            "export canônico",
            "Não executa side effect",
            "`deny-tool-scope`",
            "`deny-replay`",
            "não prova interoperabilidade universal",
        ):
            self.assertIn(required, text)


if __name__ == "__main__":
    unittest.main()

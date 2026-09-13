"""Testes da publicação da landpage pelo build do site derivado.

A landpage é servida por um docroot alimentado por ``rsync --delete`` a partir de
``site/``. Se o build parar de copiá-la, a página desaparece do ar na sincronização
seguinte sem nenhum erro visível. Estes testes protegem esse caminho.
"""

from __future__ import annotations

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools" / "build-docs-site.py"

spec = importlib.util.spec_from_file_location("build_docs_site", MODULE_PATH)
assert spec and spec.loader
build_docs_site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_docs_site)


class LandpagePublicationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.original_root = build_docs_site.ROOT
        build_docs_site.ROOT = self.tmp
        self.addCleanup(setattr, build_docs_site, "ROOT", self.original_root)

        self.landpage = self.tmp / "landpage"
        self.landpage.mkdir()
        self.site = self.tmp / "site"
        self.site.mkdir()

    def write(self, relative: str, content: str = "x") -> None:
        path = self.landpage / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_copies_page_assets_and_fonts(self) -> None:
        self.write("index.html", "<!doctype html>")
        self.write("og-image.png")
        self.write("fonts/spectral-700-latin.woff2")

        copied = build_docs_site.publish_landpage()

        self.assertEqual(copied, 3)
        published = self.site / "landpage"
        self.assertEqual((published / "index.html").read_text(encoding="utf-8"), "<!doctype html>")
        self.assertTrue((published / "og-image.png").exists())
        self.assertTrue((published / "fonts" / "spectral-700-latin.woff2").exists())

    def test_leaves_source_and_docs_files_out_of_the_published_page(self) -> None:
        self.write("index.html", "<!doctype html>")
        self.write("README.md", "# doc interno")
        self.write("make-og-image.py", "print('x')")
        self.write("fonts/LICENSE.md", "# OFL")

        build_docs_site.publish_landpage()

        published = self.site / "landpage"
        self.assertFalse((published / "README.md").exists())
        self.assertFalse((published / "make-og-image.py").exists())
        # A OFL exige que o aviso acompanhe os arquivos de fonte redistribuídos.
        self.assertTrue((published / "fonts" / "LICENSE.md").exists())

    def test_removes_files_that_no_longer_exist_in_the_source(self) -> None:
        self.write("index.html", "<!doctype html>")
        self.write("obsoleto.html")
        build_docs_site.publish_landpage()
        self.assertTrue((self.site / "landpage" / "obsoleto.html").exists())

        (self.landpage / "obsoleto.html").unlink()
        build_docs_site.publish_landpage()
        self.assertFalse((self.site / "landpage" / "obsoleto.html").exists())

    def test_refuses_to_publish_a_landpage_without_an_entry_point(self) -> None:
        self.write("og-image.png")
        with self.assertRaises(RuntimeError):
            build_docs_site.publish_landpage()

    def test_is_a_noop_when_there_is_no_landpage_or_no_site(self) -> None:
        shutil.rmtree(self.landpage)
        self.assertEqual(build_docs_site.publish_landpage(), 0)

        self.landpage.mkdir()
        self.write("index.html", "<!doctype html>")
        shutil.rmtree(self.site)
        self.assertEqual(build_docs_site.publish_landpage(), 0)


class RepositoryLandpageTest(unittest.TestCase):
    """A landpage real precisa continuar completa e sem dependência externa."""

    def test_page_declares_local_fonts_only(self) -> None:
        page = (ROOT / "landpage" / "index.html").read_text(encoding="utf-8")
        self.assertNotIn("fonts.googleapis.com", page)
        self.assertNotIn("fonts.gstatic.com", page)
        self.assertIn("@font-face", page)

    def test_every_declared_font_file_exists(self) -> None:
        page = (ROOT / "landpage" / "index.html").read_text(encoding="utf-8")
        declared = set(__import__("re").findall(r"url\(fonts/([^)]+)\)", page))
        self.assertTrue(declared, "nenhuma fonte declarada na página")
        for name in sorted(declared):
            with self.subTest(font=name):
                self.assertTrue((ROOT / "landpage" / "fonts" / name).exists())


if __name__ == "__main__":
    unittest.main()

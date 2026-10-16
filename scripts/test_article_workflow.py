"""Offline workflow regressions: draft scaffolding and human approval safety."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import tempfile
import unittest

import article_workflow as workflow


class ArticleWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        source = Path(__file__).resolve().parents[1] / "templates"
        (self.root / "templates").mkdir()
        for name in ("article-template.md", "evidence-review-template.json", "article-review-checklist.md"):
            shutil.copy2(source / name, self.root / "templates" / name)
        self.collection = "cybersecurity"
        self.slug = "sample-a2b-report"

    def init(self):
        return workflow.init_bundle(
            self.root, self.collection, self.slug,
            "テスト記事 ― 一次情報の確認", "2026-10-16", "2026-10",
        )

    def complete_sources(self):
        paths = workflow.bundle_paths(self.root, self.collection, self.slug)
        article = paths["article"].read_text(encoding="utf-8")
        article = article.replace("TODO: 一次情報の内容と経営上の意味を記載", "公開資料に基づくリスクと推奨事項を整理する。")
        article = article.replace("topics: []", "topics:\n  - Vulnerability Management")
        article = article.replace("  - TBD", "  - API Security")
        article = article.replace("ここに結論を2〜3段落で記載します。重要な事実・数値には脚注を付けます。", "NICTが公表した事項を出典に基づき整理する。")
        article = article.replace("[Primary source]", "[NICTの資料]")
        article = article.replace("https://example.com/", "https://www.nict.go.jp/press/2026/10/13-1.html")
        article = article.replace("## Attack / Process Flow（必要な場合）", "## 参考となる攻撃経路")
        paths["article"].write_text(article, encoding="utf-8")

        dossier = json.loads(paths["evidence"].read_text(encoding="utf-8"))
        for index, claim in enumerate(dossier["claims"], 1):
            claim["statement"] = f"一次資料に基づいて区別された検証対象の重要な主張 {index}"
            if "source" in claim:
                claim["source"]["url"] = "https://www.nict.go.jp/press/2026/10/13-1.html"
                claim["source"]["locator"] = f"本文 第{index}段落"
                claim["source"]["accessed_at"] = "2026-10-16"
                if claim["source"].get("published_at") is None:
                    claim["source"].pop("published_at", None)
                claim["verification"] = "verified"
        paths["evidence"].write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return paths

    def test_init_creates_pending_bundle_outside_docs(self):
        paths = self.init()
        self.assertTrue(all(p.is_file() for p in paths.values()))
        self.assertFalse((self.root / "docs").exists())
        article = paths["article"].read_text(encoding="utf-8")
        self.assertIn("status: draft", article)
        self.assertIn("review_status: Needs Review", article)
        self.assertIn("reviewed: ''", article)
        self.assertIn("# テスト記事 ― 一次情報の確認", article)
        meta, _ = workflow.split_frontmatter(article)
        self.assertEqual(meta["title"], "テスト記事 ― 一次情報の確認")
        self.assertIn("TODO:", meta["description"])
        dossier = json.loads(paths["evidence"].read_text(encoding="utf-8"))
        self.assertEqual(dossier["review"]["status"], "pending")
        self.assertIsNone(dossier["review"]["reviewed_by"])
        self.assertEqual(dossier["article_path"], "docs/cybersecurity/sample-a2b-report.md")

    def test_init_does_not_overwrite_files(self):
        self.init()
        with self.assertRaises(FileExistsError):
            self.init()
        self.assertTrue((self.root / "drafts" / "evidence" / f"{self.slug}.json").exists())

    def test_invalid_keys_and_dates_are_rejected(self):
        for slug in ("../escape", "Bad-Name", "index", "a/../../x", "a--b"):
            with self.subTest(slug=slug), self.assertRaises(ValueError):
                workflow.validate_key(self.collection, slug)
        with self.assertRaises(ValueError):
            workflow.init_bundle(self.root, self.collection, self.slug, "Test", "2026-02-31", "2026-10")
        with self.assertRaises(ValueError):
            workflow.init_bundle(self.root, self.collection, self.slug, "Test", "2026-10-16", "2026-13")

    def test_unfilled_template_fails_validation_and_stage(self):
        self.init()
        failures = workflow.validate_bundle(self.root, self.collection, self.slug)
        self.assertTrue(any("source.url" in line for line in failures))
        self.assertTrue(any("article still contains template text" in line for line in failures))
        with self.assertRaises(ValueError):
            workflow.stage_bundle(self.root, self.collection, self.slug)
        self.assertFalse((self.root / "docs").exists())

    def test_completed_pending_bundle_can_stage_without_approval(self):
        self.init()
        self.complete_sources()
        self.assertEqual(workflow.validate_bundle(self.root, self.collection, self.slug), [])
        paths = workflow.stage_bundle(self.root, self.collection, self.slug)
        self.assertTrue(all(p.is_file() for p in paths.values()))
        self.assertFalse((self.root / "drafts" / self.collection / f"{self.slug}.md").exists())
        self.assertEqual(workflow.validate_bundle(self.root, self.collection, self.slug, staged=True), [])
        article = paths["article"].read_text(encoding="utf-8")
        self.assertIn("status: draft", article)
        self.assertNotIn("status: published", article)
        dossier = json.loads(paths["evidence"].read_text(encoding="utf-8"))
        self.assertEqual(dossier["review"]["status"], "pending")

    def test_human_approval_cannot_be_faked_through_cli(self):
        self.init()
        paths = self.complete_sources()
        dossier = json.loads(paths["evidence"].read_text(encoding="utf-8"))
        dossier["review"] = {
            "status": "approved", "reviewed_by": "bot", "reviewed_at": "2026-10-16"
        }
        paths["evidence"].write_text(json.dumps(dossier, ensure_ascii=False), encoding="utf-8")
        errors = workflow.validate_bundle(self.root, self.collection, self.slug)
        self.assertTrue(any("review.status must remain pending" in line for line in errors))
        with self.assertRaises(ValueError):
            workflow.stage_bundle(self.root, self.collection, self.slug)

    def test_paths_collide_with_existing_destination(self):
        self.init()
        self.complete_sources()
        final_path = workflow.bundle_paths(self.root, self.collection, self.slug, staged=True)["article"]
        final_path.parent.mkdir(parents=True)
        final_path.write_text("not ours", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            workflow.stage_bundle(self.root, self.collection, self.slug)
        self.assertEqual(final_path.read_text(encoding="utf-8"), "not ours")

    def test_staging_requires_claim_sections_in_article(self):
        self.init()
        paths = self.complete_sources()
        dossier = json.loads(paths["evidence"].read_text(encoding="utf-8"))
        dossier["claims"][0]["section"] = "## 存在しない見出し"
        paths["evidence"].write_text(json.dumps(dossier, ensure_ascii=False), encoding="utf-8")
        errors = workflow.validate_bundle(self.root, self.collection, self.slug)
        self.assertTrue(any("section is absent" in line for line in errors))
        with self.assertRaises(ValueError):
            workflow.stage_bundle(self.root, self.collection, self.slug)


if __name__ == "__main__":
    unittest.main()

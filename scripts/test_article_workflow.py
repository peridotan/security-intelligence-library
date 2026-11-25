"""Offline workflow regressions: draft scaffolding and human approval safety."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import tempfile
import unittest

import article_workflow as workflow
import batch_review
import batch_prepare


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

    def test_batch_packet_is_read_only_and_records_hashes(self):
        self.init()
        paths = self.complete_sources()
        name = paths["article"].relative_to(self.root).as_posix()
        before = {key: p.read_bytes() for key, p in paths.items()}
        report, unresolved = batch_review.build_report(self.root, [name])
        self.assertEqual(unresolved, 0)
        self.assertIn("NOT human approval", report)
        self.assertIn(batch_review.digest(before["article"]), report)
        self.assertIn(batch_review.digest(before["evidence"]), report)
        self.assertEqual(before, {key: p.read_bytes() for key, p in paths.items()})
        with self.assertRaises(ValueError):
            batch_review.build_report(self.root, [name, name])

    def test_batch_packet_reports_unresolved_and_rejects_absent_section(self):
        self.init()
        paths = self.complete_sources()
        name = paths["article"].relative_to(self.root).as_posix()
        dossier = json.loads(paths["evidence"].read_text(encoding="utf-8"))
        claim = next(c for c in dossier["claims"] if c["classification"] == "source_fact")
        claim["verification"] = "needs_review"
        paths["evidence"].write_text(json.dumps(dossier), encoding="utf-8")
        report, unresolved = batch_review.build_report(self.root, [name])
        self.assertEqual(unresolved, 1)
        self.assertIn("needs_review", report)
        claim["section"] = "## Missing"
        paths["evidence"].write_text(json.dumps(dossier), encoding="utf-8")
        with self.assertRaises(ValueError):
            batch_review.build_report(self.root, [name])

    def approved_record(self, paths):
        return {
            "draft": paths["article"].relative_to(self.root).as_posix(),
            "decision": "approved", "reviewed_by": "test-fixture-human",
            "reviewed_at": "2026-10-16", "publication_date": "2026-10-17",
            "article_sha256": batch_review.digest(paths["article"].read_bytes()),
            "evidence_sha256": batch_review.digest(paths["evidence"].read_bytes()),
            "review_sha256": batch_review.digest(paths["review"].read_bytes()),
            "original_sha256": None, "original_evidence_sha256": None,
        }

    def test_batch_prepare_isolated_and_preserves_claims(self):
        self.init()
        paths = self.complete_sources()
        record = self.approved_record(paths)
        manifest = {"schema_version": 1, "base_commit": "a" * 40, "articles": [record]}
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "bundle"
            before = {k: p.read_bytes() for k, p in paths.items()}
            files = batch_prepare.prepare(self.root, manifest, output)
            self.assertEqual(len(files), 4)
            published = output / "docs" / self.collection / f"{self.slug}.md"
            self.assertIn("status: published", published.read_text(encoding="utf-8"))
            dossier = json.loads((output / "review" / "evidence" / f"{self.slug}.json").read_text(encoding="utf-8"))
            self.assertEqual(dossier["review"]["status"], "approved")
            self.assertEqual(dossier["claims"], json.loads(before["evidence"])["claims"])
            self.assertEqual(before, {k: p.read_bytes() for k, p in paths.items()})
            self.assertFalse((self.root / "docs").exists())
            with self.assertRaises(ValueError):
                batch_prepare.prepare(self.root, manifest, output)

    def test_batch_prepare_refuses_changed_or_unapproved_input(self):
        self.init()
        paths = self.complete_sources()
        record = self.approved_record(paths)
        manifest = {"schema_version": 1, "base_commit": "a" * 40, "articles": [record]}
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "bundle"
            record["decision"] = "pending"
            with self.assertRaises(ValueError):
                batch_prepare.prepare(self.root, manifest, output)
            self.assertFalse(output.exists())
            record["decision"] = "approved"
            paths["article"].write_text(paths["article"].read_text(encoding="utf-8") + "\\nChanged", encoding="utf-8")
            with self.assertRaises(ValueError):
                batch_prepare.prepare(self.root, manifest, output)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()

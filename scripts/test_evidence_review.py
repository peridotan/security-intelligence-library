"""Offline regression tests for Evidence Review's structural publication gate."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import check_evidence_review as ev


def dossier(status="pending", classification="source_fact", verification="verified"):
    claim = {
        "id": "C01",
        "statement": "2026年の一次情報に明記された重要な事実を記録する",
        "section": "## 何が起きているのか",
        "classification": classification,
        "importance": "material",
        "verification": verification,
    }
    if classification == "library_assessment":
        claim["rationale"] = "企業への対応についてLibraryが独自に評価した内容"
    else:
        claim["source"] = {
            "url": "https://www.nict.go.jp/press/2026/10/13-1.html",
            "locator": "本文の調査概要",
            "published_at": "2026-10-13",
            "accessed_at": "2026-10-15",
        }
    review = {"status": status}
    if status == "approved":
        review.update({"reviewed_by": "@human-reviewer", "reviewed_at": "2026-10-15"})
    return {
        "schema_version": 1,
        "article_path": "docs/cybersecurity/new-security-report.md",
        "review": review,
        "claims": [claim],
    }


class DossierTest(unittest.TestCase):
    def check(self, payload):
        return ev.validate_dossier(payload, "review/evidence/demo.json")[1]

    def test_pending_source_fact_valid(self):
        self.assertEqual(self.check(dossier()), [])

    def test_vendor_claim_is_not_reclassified_as_fact(self):
        self.assertEqual(self.check(dossier(classification="source_claim")), [])

    def test_assessment_requires_rationale_and_distinct_verification(self):
        p = dossier(classification="library_assessment", verification="not_applicable")
        self.assertEqual(self.check(p), [])
        p["claims"][0]["rationale"] = ""
        self.assertTrue(any("requires rationale" in e for e in self.check(p)))

    def test_approved_dossier_requires_human_and_resolved_claims(self):
        p = dossier(status="approved", verification="needs_review")
        with patch.object(ev, "read_status", return_value="draft"):
            self.assertTrue(any("unresolved" in e for e in self.check(p)))
            p["claims"][0]["verification"] = "verified"
            self.assertEqual(self.check(p), [])
            del p["review"]["reviewed_by"]
            self.assertTrue(any("reviewed_by" in e for e in self.check(p)))

    def test_invalid_primary_url_and_locator(self):
        p = dossier()
        p["claims"][0]["source"]["url"] = "https://example.com/report"
        p["claims"][0]["source"]["locator"] = " "
        errors = self.check(p)
        self.assertTrue(any("HTTPS URL" in e for e in errors))
        self.assertTrue(any("locator" in e for e in errors))

    def test_unsupported_claim_is_allowed_for_pending_only(self):
        p = dossier(verification="unsupported")
        self.assertEqual(self.check(p), [])
        p["review"] = {"status": "approved", "reviewed_by": "human", "reviewed_at": "2026-10-15"}
        with patch.object(ev, "read_status", return_value="draft"):
            self.assertTrue(self.check(p))

    def test_invalid_target_path_and_duplicate_ids(self):
        p = dossier()
        p["article_path"] = "docs/cybersecurity/../../../escape.md"
        p["claims"].append(dict(p["claims"][0]))
        errors = self.check(p)
        self.assertTrue(any("safe docs" in e for e in errors))
        self.assertTrue(any("duplicate claim" in e for e in errors))

    def test_review_date_must_be_calendar_date(self):
        p = dossier(status="approved")
        p["review"]["reviewed_at"] = "2026-02-31"
        self.assertTrue(any("reviewed_at" in e for e in self.check(p)))

    def test_published_article_requires_approved_review(self):
        p = dossier(status="pending")
        with patch.object(ev, "read_status", return_value="published"), patch.object(
            Path, "read_text", return_value="## 何が起きているのか\n"
        ):
            self.assertTrue(any("published article requires" in e for e in self.check(p)))

    def test_new_published_article_without_dossier_fails(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(
            ev, "new_published_articles",
            return_value={"docs/cybersecurity/new-security-report.md"},
        ):
            count, errors = ev.validate_all(Path(folder), base_ref="origin/main")
        self.assertEqual(count, 0)
        self.assertTrue(any("requires a review/evidence" in e for e in errors))

    def test_new_published_article_with_approved_dossier_passes(self):
        p = dossier(status="approved")
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / "new-security-report.json"
            file.write_text(json.dumps(p, ensure_ascii=False), encoding="utf-8")
            original = Path.read_text

            def contents(path, *args, **kwargs):
                if path == file:
                    return original(path, *args, **kwargs)
                return "## 何が起きているのか\n"

            with patch.object(ev, "new_published_articles", return_value={p["article_path"]}), patch.object(
                ev, "read_status", return_value="published"
            ), patch.object(Path, "read_text", autospec=True, side_effect=contents):
                count, errors = ev.validate_all(Path(folder), base_ref="origin/main")
            self.assertEqual((count, errors), (1, []))

    def test_git_diff_detects_draft_publication_not_normal_update(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            target = repo / "docs" / "cybersecurity" / "new-report.md"
            target.parent.mkdir(parents=True)
            def git(*args):
                return subprocess.run(
                    ["git", *args], cwd=repo, capture_output=True,
                    text=True, check=True,
                ).stdout.strip()
            git("init", "-q")
            git("config", "user.name", "Evidence Test")
            git("config", "user.email", "evidence@example.invalid")
            (repo / "README.md").write_text("test", encoding="utf-8")
            git("add", ".")
            git("commit", "-qm", "initial")
            initial = git("rev-parse", "HEAD")

            target.write_text("---\nstatus: draft\n---\n## 何が起きているのか\n", encoding="utf-8")
            git("add", ".")
            git("commit", "-qm", "draft article")
            draft_commit = git("rev-parse", "HEAD")
            with patch.object(ev, "ROOT", repo):
                self.assertEqual(ev.new_published_articles(initial), set())

            target.write_text("---\nstatus: published\n---\n## 何が起きているのか\n", encoding="utf-8")
            git("add", ".")
            git("commit", "-qm", "publish draft")
            published_commit = git("rev-parse", "HEAD")
            with patch.object(ev, "ROOT", repo):
                self.assertEqual(
                    ev.new_published_articles(draft_commit),
                    {"docs/cybersecurity/new-report.md"},
                )
                self.assertEqual(
                    ev.new_published_articles(initial),
                    {"docs/cybersecurity/new-report.md"},
                )

            target.write_text("---\nstatus: published\n---\n## 何が起きているのか\n\nUpdate.\n", encoding="utf-8")
            git("add", ".")
            git("commit", "-qm", "normal article update")
            with patch.object(ev, "ROOT", repo):
                self.assertEqual(ev.new_published_articles(published_commit), set())

    def test_empty_legacy_repo_requires_no_retroactive_dossiers(self):
        with tempfile.TemporaryDirectory() as folder:
            count, errors = ev.validate_all(Path(folder))
        self.assertEqual((count, errors), (0, []))


if __name__ == "__main__":
    unittest.main()

"""Historical six-article replay. Test-only approvals; no publication or network."""
import copy
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import article_workflow as workflow
import batch_review as review
import batch_prepare as prepare

ROOT = Path(__file__).resolve().parents[1]
BASE = "d71c7f82f151590a8120267c293a736703c9dcbc"
CASES = [
    ("776fc52d1bc3e08387d6f9d46a98ab4df50f34c6", "ai-security", "cairn-autonomous-zero-day"),
    ("776fc52d1bc3e08387d6f9d46a98ab4df50f34c6", "ai-security", "lora-model-supply-chain"),
    ("776fc52d1bc3e08387d6f9d46a98ab4df50f34c6", "risk-management", "incident-report-checklist"),
    ("29e14d02c1e42cc80a7cc625d297d5f59938598a", "cybersecurity", "optimjack-third-party-script"),
    ("eb02d60710f2928df56fa2e2e1566f4abc02553d", "identity-security", "ai-enabled-device-code-phishing-update"),
    ("eb02d60710f2928df56fa2e2e1566f4abc02553d", "identity-security", "ai-agent-identity-nhi-update"),
]


def historical(ref, path, optional=False):
    result = subprocess.run(["git", "show", f"{ref}:{path}"], cwd=ROOT, capture_output=True)
    if result.returncode:
        if optional:
            # Verify the commit exists; only absence of the path is optional.
            subprocess.run(["git", "cat-file", "-e", f"{ref}^{{commit}}"], cwd=ROOT, check=True)
            return None
        raise RuntimeError(f"Missing historical fixture {ref}:{path}: {result.stderr.decode()}")
    return result.stdout


class HistoricalBatchTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name) / "source"
        self.root.mkdir()
        self.output = Path(tmp.name) / "output"
        self.records = []
        self.manifest = {"schema_version": 1, "base_commit": BASE, "articles": self.records}
        for ref, col, slug in CASES:
            name = f"drafts/{col}/{slug}.md"
            ep = f"drafts/evidence/{slug}.json"
            rp = f"drafts/reviews/{slug}.md"
            update = slug.endswith("-update")
            target_slug = slug[:-7] if update else slug
            target = f"docs/{col}/{target_slug}.md"
            old_evidence = f"review/evidence/{target_slug}.json"
            for path in (name, ep, rp):
                self.write(path, historical(ref, path))
            for path in (target, old_evidence):
                data = historical(BASE, path, optional=True)
                if data is not None:
                    self.write(path, data)
            self.records.append({
                "draft": name, "decision": "approved", "reviewed_by": "historical-test-fixture-not-an-approval",
                "reviewed_at": "2026-11-24", "publication_date": "2026-11-24",
                "article_sha256": self.hash(name), "evidence_sha256": self.hash(ep),
                "review_sha256": self.hash(rp), "original_sha256": self.hash(target),
                "original_evidence_sha256": self.hash(old_evidence),
            })

    def write(self, path, data):
        dest = self.root / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)

    def hash(self, path):
        p = self.root / path
        return review.digest(p.read_bytes()) if p.exists() else None

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): review.digest(p.read_bytes())
                for p in self.root.rglob("*") if p.is_file()}

    def run_prepare(self):
        return prepare.prepare(self.root, self.manifest, self.output)

    def reject(self, reason):
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, reason):
            self.run_prepare()
        self.assertFalse(self.output.exists())
        self.assertEqual(before, self.snapshot())

    def test_T01_review_six_articles(self):
        report, count = review.build_report(self.root, [r["draft"] for r in self.records])
        self.assertEqual(count, 0)
        self.assertIn("Articles: 6; claims: 34; unresolved: 0.", report)

    def test_T02_T03_T04_T12_prepare_all_preserve_dates_claims_and_originals(self):
        before = self.snapshot()
        files = self.run_prepare()
        self.assertEqual(len(files), 19)
        count = 0
        for rec, (_, col, slug) in zip(self.records, CASES):
            target_slug = slug.removesuffix("-update")
            target = f"docs/{col}/{target_slug}.md"
            draft_meta, draft_body = workflow.split_frontmatter((self.root / rec["draft"]).read_text())
            meta, body = workflow.split_frontmatter((self.output / target).read_text())
            self.assertEqual(meta["status"], "published")
            self.assertEqual(meta["review_status"], "Current")
            self.assertEqual(str(meta["date"]), str(draft_meta["date"]))
            self.assertEqual(body, draft_body)
            src = json.loads((self.root / f"drafts/evidence/{slug}.json").read_text())
            dst = json.loads((self.output / f"review/evidence/{target_slug}.json").read_text())
            self.assertEqual(src["claims"], dst["claims"])
            self.assertEqual(dst["review"]["status"], "approved")
            count += len(dst["claims"])
        self.assertEqual(count, 34)
        self.assertEqual(before, self.snapshot())
        self.assertEqual(len(list((self.output / "review/publication-batches").glob("*.json"))), 1)

    def test_T05_T11_pending_last_article_no_partial_output(self):
        self.records[-1]["decision"] = "pending"
        self.reject("explicit human approval")

    def test_T06_changed_article(self):
        path = self.records[-1]["draft"]
        self.write(path, (self.root / path).read_bytes() + b"\nTest mutation\n")
        self.reject("approved hash mismatch")

    def test_T07_changed_evidence(self):
        path = "drafts/evidence/ai-agent-identity-nhi-update.json"
        self.write(path, (self.root / path).read_bytes() + b"\n")
        self.reject("approved hash mismatch")

    def test_T08_changed_original(self):
        path = "docs/identity-security/ai-agent-identity-nhi.md"
        self.write(path, (self.root / path).read_bytes() + b"\nTest mutation\n")
        self.reject("original article changed")

    def test_T09_duplicate(self):
        self.records.append(copy.deepcopy(self.records[0]))
        self.reject("duplicate publication target")

    def test_T10_unresolved(self):
        path = "drafts/evidence/cairn-autonomous-zero-day.json"
        data = json.loads((self.root / path).read_bytes())
        next(c for c in data["claims"] if c["classification"] == "source_fact")["verification"] = "needs_review"
        self.write(path, json.dumps(data).encode())
        self.reject("unresolved claims")


if __name__ == "__main__":
    unittest.main()

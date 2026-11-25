"""Offline deployment verification regressions."""
import tempfile
from pathlib import Path
import unittest
import check_deployed_site as check


class DeploymentTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.site = Path(self.tmp.name)
        for path, data in (("index.html", b"home"), ("ai-security/a/index.html", b"article"), ("assets/context-index.json", b"{}"), ("404.html", b"not found")):
            p = self.site / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)

    def test_exact_artifact_matches(self):
        self.assertEqual(len(check.targets(self.site)), 3)
        self.assertEqual(check.verify(self.site, "abc", lambda p, r: (self.site / p).read_bytes(), delay=0), [])

    def test_stale_content_is_retried(self):
        seen = set()
        def get(p, revision):
            if p not in seen:
                seen.add(p)
                return b"old"
            return (self.site / p).read_bytes()
        self.assertEqual(check.verify(self.site, "abc", get, attempts=2, delay=0), [])

    def test_persistent_mismatch_and_http_error(self):
        def get(p, revision):
            if p.name.endswith(".json"):
                raise OSError("unavailable")
            return b"wrong"
        self.assertEqual(len(check.verify(self.site, "abc", get, attempts=1, delay=0)), 3)

    def test_missing_home_fails_closed(self):
        (self.site / "index.html").unlink()
        with self.assertRaises(ValueError):
            check.targets(self.site)

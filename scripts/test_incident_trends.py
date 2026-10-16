"""Regression tests for the non-exhaustive, incident-group Trend Brief data gate."""
from __future__ import annotations
from copy import deepcopy
import json
from pathlib import Path
import unittest

import check_incident_trends as checker


FIXTURE = Path(__file__).resolve().parents[1] / "data" / "incident-trends" / "2026-10-h1.json"


class IncidentTrendDataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def errors(self, data, name="2026-10-h1.json"):
        return checker.validate(data, name)

    def test_initial_incident_trend_evidence_passes(self):
        self.assertEqual(self.errors(self.baseline), [])
        self.assertEqual(len(self.baseline["incidents"]), 3)
        self.assertEqual(len(self.baseline["advisories"]), 4)
        self.assertEqual(len({s["id"] for s in self.baseline["sources"]}), len(self.baseline["sources"]))

    def test_related_customer_disclosures_are_not_independent_events(self):
        data = deepcopy(self.baseline)
        self.assertEqual(len(data["incidents"]), 3)
        self.assertTrue(any(len(e.get("related_disclosures", [])) == 2 for e in data["incidents"]))
        data["incidents"].append(deepcopy(data["incidents"][2]))
        data["incidents"][-1]["id"] = "INC04"
        self.assertTrue(any("unique event_group" in err for err in self.errors(data)))

    def test_counting_unit_and_sampling_cannot_claim_full_coverage(self):
        data = deepcopy(self.baseline)
        data["coverage"]["sampling"] = "comprehensive"
        self.assertTrue(any("curated_non_exhaustive" in err for err in self.errors(data)))
        data["coverage"]["sampling"] = "curated_non_exhaustive"
        data["coverage"]["counting_unit"] = "organizational_disclosure"
        self.assertTrue(any("incident_group" in err for err in self.errors(data)))

    def test_window_is_based_on_disclosure_not_attack_date(self):
        data = deepcopy(self.baseline)
        data["incidents"][0]["disclosed_at"] = "2026-09-09"
        self.assertTrue(any("reporting window" in err for err in self.errors(data)))
        data = deepcopy(self.baseline)
        data["period"]["end"] = "2026-10-16"
        self.assertTrue(any("h1 period" in err for err in self.errors(data)))

    def test_source_integrity_and_dangling_refs(self):
        data = deepcopy(self.baseline)
        data["incidents"][0]["facts"][0]["source_ids"] = ["FAKE"]
        self.assertTrue(any("unknown source" in err for err in self.errors(data)))
        data = deepcopy(self.baseline)
        data["sources"][0]["url"] = "http://example.com/not-a-source"
        self.assertTrue(any("real https" in err for err in self.errors(data)))

    def test_separate_advisories_not_counted_as_incidents(self):
        data = deepcopy(self.baseline)
        data["advisories"].append(deepcopy(data["advisories"][0]))
        self.assertTrue(any("unique advisory id" in err for err in self.errors(data)))

    def test_trend_assessment_requires_limitations_and_sources(self):
        data = deepcopy(self.baseline)
        data["trend_signals"][0]["limitation"] = ""
        self.assertTrue(any("limitation" in err for err in self.errors(data)))
        data = deepcopy(self.baseline)
        data["trend_signals"][0]["advisory_ids"] = ["ADV99"]
        self.assertTrue(any("unknown advisory" in err for err in self.errors(data)))

    def test_filename_matches_period_id(self):
        self.assertTrue(any("brief_id" in err for err in self.errors(self.baseline, "2026-10-h2.json")))

    def test_malformed_data_is_reported_without_exception(self):
        self.assertTrue(self.errors([]))
        data = deepcopy(self.baseline)
        data["incidents"][0]["facts"][0]["classification"] = "independently_proven"
        self.assertTrue(any("classification" in err for err in self.errors(data)))


if __name__ == "__main__":
    unittest.main()

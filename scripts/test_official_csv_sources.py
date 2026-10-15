import unittest
from official_csv_sources import parse_nco_csv


class OfficialCSVTest(unittest.TestCase):
    def test_nco_pdf_and_external_portal(self):
        payload = (
            "date,name,path,groups,tag,pdf\n"
            "2026/10/9,不正アクセスによる漏えい等の事案を踏まえた対応について,#,G3,注意喚起,407KB|/pdf/press/taiou.pdf;\n"
            "2026/10/1,重要インフラ統一基準及び安全基準等策定ガイドラインが施行されました,/policy/group/infra/policy.html,G3,,#\n"
            "2026/10/1,法令の手引き,https://security-portal.cyber.go.jp/guidance/,G3,,#\n"
        )
        records = parse_nco_csv(payload.encode(), {})
        self.assertEqual(len(records), 3)
        self.assertEqual(records[0]["published_raw"], "2026-10-09")
        self.assertEqual(records[0]["url"], "https://www.cyber.go.jp/pdf/press/taiou.pdf")
        self.assertEqual(records[2]["url"], "https://security-portal.cyber.go.jp/guidance/")

    def test_no_foreign_links_or_malformed_dates(self):
        payload = (
            "date,name,path,groups,tag,pdf\n"
            "2026/19/9,悪い日付,/x,G3,,#\n"
            "2026/10/9,Foreign,https://example.com,G3,,#\n"
        )
        self.assertEqual(parse_nco_csv(payload.encode(), {}), [])

    def test_wrong_schema(self):
        with self.assertRaises(ValueError):
            parse_nco_csv(b"a,b\n1,2\n", {})


if __name__ == "__main__":
    unittest.main()

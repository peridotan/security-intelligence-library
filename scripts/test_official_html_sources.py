"""Offline regressions for first-party HTML source adapters."""
import unittest

from official_html_sources import parse_html_listing


class OfficialSourcesTest(unittest.TestCase):
    def test_nict_a2b_and_off_topic(self):
        source = {"url": "https://www.nict.go.jp/press/", "html_strategy": "nict_press"}
        html = """<ul>
<li><a href="/press/2026/10/13-1.html">【注意喚起】相次ぐ情報漏えい、その原因の一つは「アプリ解析からのサーバ攻撃」</a><time>2026年10月13日</time></li>
<li><a href="/press/2026/10/08-1.html">衛星通信設備を構築</a></li>
</ul>"""
        records = parse_html_listing(html.encode(), source)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["published_raw"], "2026-10-13")
        self.assertEqual(records[0]["url"], "https://www.nict.go.jp/press/2026/10/13-1.html")

    def test_nict_rejects_external_and_undated(self):
        source = {"url": "https://www.nict.go.jp/press/", "html_strategy": "nict_press"}
        html = """<a href="https://evil.example/press/2026/10/13-1.html">サイバー攻撃</a>
<a href="/press/2026/10/invalid.html">サイバー攻撃</a>"""
        self.assertEqual(parse_html_listing(html.encode(), source), [])

    def test_nco_dated_pdf(self):
        source = {
            "url": "https://www.cyber.go.jp/news/list/index.html",
            "html_strategy": "nco_news",
        }
        html = """<section><div>2026年10月09日</div>
<p>不正アクセスによる漏えい等の事案を踏まえた対応について</p>
<a href="/pdf/security-notice.pdf">PDF形式:407KB</a></section>"""
        records = parse_html_listing(html.encode(), source)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["published_raw"], "2026-10-09")
        self.assertIn("不正アクセス", records[0]["title"])

    def test_nco_undated_links_excluded(self):
        source = {
            "url": "https://www.cyber.go.jp/news/list/index.html",
            "html_strategy": "nco_news",
        }
        self.assertEqual(
            parse_html_listing(b'<a href="/pdf/x.pdf">Important security bulletin</a>', source),
            [],
        )

    def test_unknown_strategy_fails_closed(self):
        with self.assertRaises(ValueError):
            parse_html_listing(b"", {"html_strategy": "unknown"})


if __name__ == "__main__":
    unittest.main()

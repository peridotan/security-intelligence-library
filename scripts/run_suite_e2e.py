#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path
from urllib.parse import parse_qs, urljoin, urlparse

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.build_context_index import DOCS, article_context, page_key


DEFAULT_LIBRARY = (
    "https://peridotan.github.io/security-intelligence-library/"
)


def query_params(href: str) -> dict[str, list[str]]:
    return parse_qs(
        urlparse(href).query,
        keep_blank_values=True,
    )


def values(params, key):
    return params.get(key, [])


def collect_articles():
    articles = []

    for path in sorted(DOCS.rglob("*.md")):
        context = article_context(path)

        if context is None:
            continue

        articles.append(
            {
                "key": page_key(path),
                "path": path,
                "title": context["title"],
                "cves": context["cves"],
                "actors": context["actors"],
                "techniques": context["techniques"],
            }
        )

    return articles


def wait_for_href(page, locator, predicate, timeout_ms=5000):
    deadline = time.monotonic() + timeout_ms / 1000
    last_href = None

    while time.monotonic() < deadline:
        last_href = locator.get_attribute("href")

        if last_href:
            params = query_params(last_href)

            if predicate(params):
                return last_href

        page.wait_for_timeout(100)

    return last_href


def check_article(browser, article, library_base, headful=False):
    key = article["key"]
    article_url = urljoin(library_base, key)
    expected_path = urlparse(article_url).path

    errors = []
    failures = []

    page = browser.new_page()

    page.on(
        "pageerror",
        lambda exc: errors.append(str(exc)),
    )

    try:
        response = page.goto(
            article_url,
            wait_until="domcontentloaded",
            timeout=30000,
        )

        if response is None:
            failures.append("No HTTP response")
            return failures

        if response.status >= 400:
            failures.append(
                f"HTTP status {response.status}"
            )
            return failures

        try:
            page.wait_for_selector(
                "#security-intelligence-suite-nav",
                timeout=10000,
            )
        except Exception:
            failures.append("Suite navigation not found")
            return failures

        threat = page.locator(
            '[data-suite-key="investigate"]'
        )
        vuln = page.locator(
            '[data-suite-key="vulnerability"]'
        )

        if threat.count() != 1:
            failures.append(
                f"Threat link count={threat.count()}"
            )
            return failures

        if vuln.count() != 1:
            failures.append(
                f"Vulnerability link count={vuln.count()}"
            )
            return failures

        expected_actors = article["actors"]
        expected_techniques = article["techniques"]
        expected_cves = article["cves"]

        # ----------------------------------------
        # Library -> Threat Investigation
        # ----------------------------------------

        def threat_ready(params):
            if values(params, "from") != [
                "security-intelligence-library"
            ]:
                return False

            if values(params, "context") != [
                expected_path
            ]:
                return False

            if sorted(values(params, "actor")) != sorted(
                expected_actors
            ):
                return False

            if sorted(values(params, "technique")) != sorted(
                expected_techniques
            ):
                return False

            return True

        threat_href = wait_for_href(
            page,
            threat,
            threat_ready,
        )

        if not threat_href:
            failures.append("Threat href missing")
        else:
            params = query_params(threat_href)

            if values(params, "from") != [
                "security-intelligence-library"
            ]:
                failures.append(
                    "Threat: incorrect from="
                )

            if values(params, "context") != [
                expected_path
            ]:
                failures.append(
                    "Threat: incorrect context="
                )

            if not values(params, "contextTitle"):
                failures.append(
                    "Threat: contextTitle missing"
                )

            actual_actors = sorted(
                values(params, "actor")
            )
            actual_techniques = sorted(
                values(params, "technique")
            )

            if actual_actors != sorted(expected_actors):
                failures.append(
                    f"Threat actor mismatch: "
                    f"{actual_actors} != "
                    f"{sorted(expected_actors)}"
                )

            if actual_techniques != sorted(
                expected_techniques
            ):
                failures.append(
                    f"Threat technique mismatch: "
                    f"{actual_techniques} != "
                    f"{sorted(expected_techniques)}"
                )

            entity = values(params, "entity")

            expected_entity = []

            if len(expected_actors) == 1:
                expected_entity = [
                    f"actor:{expected_actors[0]}"
                ]
            elif (
                not expected_actors
                and len(expected_techniques) == 1
            ):
                expected_entity = [
                    f"technique:{expected_techniques[0]}"
                ]

            if entity != expected_entity:
                failures.append(
                    f"Threat entity mismatch: "
                    f"{entity} != {expected_entity}"
                )

        # ----------------------------------------
        # Library -> Vulnerability Intelligence
        # ----------------------------------------

        if expected_cves:

            def vuln_ready(params):
                return (
                    sorted(values(params, "cve"))
                    == sorted(expected_cves)
                    and values(params, "scope") == ["all"]
                    and values(params, "from")
                    == ["security-intelligence-library"]
                )

            vuln_href = wait_for_href(
                page,
                vuln,
                vuln_ready,
            )

            if not vuln_href:
                failures.append(
                    "Vulnerability href missing"
                )
            else:
                params = query_params(vuln_href)

                actual_cves = sorted(
                    values(params, "cve")
                )

                if actual_cves != sorted(expected_cves):
                    failures.append(
                        f"CVE mismatch: "
                        f"{actual_cves} != "
                        f"{sorted(expected_cves)}"
                    )

                if values(params, "scope") != ["all"]:
                    failures.append(
                        "Vulnerability: scope != all"
                    )

                if values(params, "context") != [
                    expected_path
                ]:
                    failures.append(
                        "Vulnerability: "
                        "incorrect context="
                    )

                if not values(
                    params,
                    "contextTitle",
                ):
                    failures.append(
                        "Vulnerability: "
                        "contextTitle missing"
                    )

        else:
            vuln_href = vuln.get_attribute("href")

            if not vuln_href:
                failures.append(
                    "Vulnerability href missing"
                )
            else:
                params = query_params(vuln_href)

                if values(params, "cve"):
                    failures.append(
                        "Unexpected CVE context"
                    )

        # ----------------------------------------
        # JavaScript runtime errors
        # ----------------------------------------

        page.wait_for_timeout(200)

        if errors:
            failures.append(
                "JavaScript error: "
                + " | ".join(errors)
            )

    except Exception as exc:
        failures.append(
            f"Unhandled test exception: {exc}"
        )

    finally:
        page.close()

    return failures


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Security Intelligence Suite "
            "live E2E smoke test"
        )
    )

    parser.add_argument(
        "--library",
        default=DEFAULT_LIBRARY,
        help="Security Intelligence Library base URL",
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Test only the first N articles",
    )

    parser.add_argument(
        "--headful",
        action="store_true",
        help="Show Chromium while testing",
    )

    args = parser.parse_args()

    library_base = args.library.rstrip("/") + "/"

    articles = collect_articles()

    if args.limit:
        articles = articles[: args.limit]

    total = len(articles)

    with_cves = sum(
        bool(a["cves"])
        for a in articles
    )
    with_actors = sum(
        bool(a["actors"])
        for a in articles
    )
    with_techniques = sum(
        bool(a["techniques"])
        for a in articles
    )

    print("Security Intelligence Suite E2E")
    print("=" * 40)
    print(f"Articles        : {total}")
    print(f"With CVE        : {with_cves}")
    print(f"With Actor      : {with_actors}")
    print(f"With ATT&CK     : {with_techniques}")
    print()

    failures = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=not args.headful
        )

        for number, article in enumerate(
            articles,
            start=1,
        ):
            print(
                f"[{number:02d}/{total:02d}] "
                f"{article['key']}",
                end=" ... ",
                flush=True,
            )

            problems = check_article(
                browser,
                article,
                library_base,
            )

            if problems:
                print("FAIL")
                failures.append(
                    (article, problems)
                )

                for problem in problems:
                    print(f"    - {problem}")
            else:
                print("PASS")

        browser.close()

    print()
    print("=" * 40)

    if failures:
        print(
            f"FAILED: {len(failures)} / "
            f"{total} article(s)"
        )

        print()
        print("Failure summary")

        for article, problems in failures:
            print(f"- {article['key']}")

            for problem in problems:
                print(f"  - {problem}")

        return 1

    print(
        f"PASSED: {total} / {total} article(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
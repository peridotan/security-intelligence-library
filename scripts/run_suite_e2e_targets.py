#!/usr/bin/env python3
from __future__ import annotations

import sys
from urllib.parse import urljoin

from playwright.sync_api import sync_playwright

from run_suite_e2e import (
    DEFAULT_LIBRARY,
    collect_articles,
    wait_for_href,
)


def open_target(page, href, expected_values):
    errors = []
    page.on("pageerror", lambda exc: errors.append(str(exc)))

    response = page.goto(
        href,
        wait_until="domcontentloaded",
        timeout=30000,
    )

    if response is None:
        return ["No HTTP response"]

    if response.status >= 400:
        return [f"HTTP status {response.status}"]

    try:
        box = page.locator("#external-launch-context")

        box.wait_for(
            state="visible",
            timeout=10000,
        )

        text = box.inner_text()

    except Exception as exc:
        return [f"Context box not visible: {exc}"]

    failures = []

    for expected in expected_values:
        if expected not in text:
            failures.append(
                f"Context does not contain {expected}"
            )

    if errors:
        failures.append(
            "JavaScript error: " + " | ".join(errors)
        )

    return failures


def main():
    articles = [
        a
        for a in collect_articles()
        if a["cves"]
        or a["actors"]
        or a["techniques"]
    ]

    print("Security Intelligence Suite Target E2E")
    print("=" * 44)
    print(f"Context articles : {len(articles)}")
    print()

    failures = []
    checks = 0

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        for number, article in enumerate(
            articles,
            start=1,
        ):
            article_url = urljoin(
                DEFAULT_LIBRARY,
                article["key"],
            )

            print(
                f"[{number:02d}/{len(articles):02d}] "
                f"{article['key']}"
            )

            page.goto(
                article_url,
                wait_until="domcontentloaded",
                timeout=30000,
            )

            page.wait_for_selector(
                "#security-intelligence-suite-nav",
                timeout=10000,
            )

            # Library -> Threat Investigation
            if article["actors"] or article["techniques"]:
                threat = page.locator(
                    '[data-suite-key="investigate"]'
                )

                def threat_ready(params):
                    return (
                        sorted(params.get("actor", []))
                        == sorted(article["actors"])
                        and
                        sorted(params.get("technique", []))
                        == sorted(article["techniques"])
                    )

                href = wait_for_href(
                    page,
                    threat,
                    threat_ready,
                )

                checks += 1

                problems = open_target(
                    page,
                    href,
                    article["actors"]
                    + article["techniques"],
                )

                if problems:
                    print("  Threat        FAIL")
                    failures.append(
                        (
                            article["key"],
                            "Threat",
                            problems,
                        )
                    )

                    for problem in problems:
                        print(f"    - {problem}")
                else:
                    print("  Threat        PASS")

                # Return to article for another handoff.
                page.goto(
                    article_url,
                    wait_until="domcontentloaded",
                    timeout=30000,
                )

                page.wait_for_selector(
                    "#security-intelligence-suite-nav",
                    timeout=10000,
                )

            # Library -> Vulnerability Intelligence
            if article["cves"]:
                vuln = page.locator(
                    '[data-suite-key="vulnerability"]'
                )

                def vuln_ready(params):
                    return (
                        sorted(params.get("cve", []))
                        == sorted(article["cves"])
                    )

                href = wait_for_href(
                    page,
                    vuln,
                    vuln_ready,
                )

                checks += 1

                problems = open_target(
                    page,
                    href,
                    article["cves"],
                )

                if problems:
                    print("  Vulnerability FAIL")
                    failures.append(
                        (
                            article["key"],
                            "Vulnerability",
                            problems,
                        )
                    )

                    for problem in problems:
                        print(f"    - {problem}")
                else:
                    print("  Vulnerability PASS")

        browser.close()

    print()
    print("=" * 44)

    if failures:
        print(
            f"FAILED: {len(failures)} / "
            f"{checks} target check(s)"
        )

        for article, target, problems in failures:
            print(f"- {article} -> {target}")

            for problem in problems:
                print(f"  - {problem}")

        return 1

    print(
        f"PASSED: {checks} / {checks} target check(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
(() => {
  function libraryBasePath() {
    const path = window.location.pathname;

    if (path.includes("/security-intelligence-library/site/")) {
      return "/security-intelligence-library/site/";
    }

    return "/security-intelligence-library/";
  }

  function currentPageKey() {
    const base = libraryBasePath();
    let path = window.location.pathname;

    const pos = path.indexOf(base);
    if (pos >= 0) {
      path = path.slice(pos + base.length);
    }

    path = path.replace(/^\/+/, "");

    if (path && !path.endsWith("/")) {
      path += "/";
    }

    return path;
  }

  function currentPageTitle() {
    const heading = document.querySelector(
      ".md-content h1, main h1, article h1"
    );

    return (
      heading?.textContent ||
      document.title ||
      ""
    ).trim();
  }

  async function applyVulnerabilityContext() {
    const link = document.querySelector(
      '[data-suite-key="vulnerability"]'
    );

    if (!link) return;

    const key = currentPageKey();
    if (!key) return;

    const indexUrl =
      `${window.location.origin}${libraryBasePath()}assets/context-index.json`;

    let data;

    try {
      const response = await fetch(indexUrl, { cache: "no-store" });
      if (!response.ok) return;
      data = await response.json();
    } catch {
      return;
    }

    const context = data?.articles?.[key];
    const cves = Array.isArray(context?.cves)
      ? context.cves
      : [];

    if (!cves.length) return;

    const url = new URL(link.href);

    url.searchParams.set(
      "from",
      "security-intelligence-library"
    );
    url.searchParams.set("scope", "all");
    url.searchParams.set(
      "context",
      window.location.pathname
    );
    url.searchParams.set(
      "contextTitle",
      currentPageTitle()
    );

    url.searchParams.delete("cve");

    for (const cve of cves) {
      url.searchParams.append("cve", cve);
    }

    link.href = url.toString();

    const small = link.querySelector("small");
    if (small) {
      small.textContent =
        `Prioritize · ${cves.length} CVE${cves.length === 1 ? "" : "s"}`;
    }
  }

  function initialize() {
    applyVulnerabilityContext();
  }

  if (typeof document$ !== "undefined" && document$?.subscribe) {
    document$.subscribe(initialize);
  } else if (document.readyState === "loading") {
    document.addEventListener(
      "DOMContentLoaded",
      initialize,
      { once: true }
    );
  } else {
    initialize();
  }
})();

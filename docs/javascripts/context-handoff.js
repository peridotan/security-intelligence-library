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

  async function loadArticleContext() {
    const key = currentPageKey();
    if (!key) return null;

    const indexUrl =
      `${window.location.origin}${libraryBasePath()}assets/context-index.json`;

    try {
      const response = await fetch(indexUrl, { cache: "no-store" });
      if (!response.ok) return null;

      const data = await response.json();
      return data?.articles?.[key] || null;
    } catch {
      return null;
    }
  }

  function addCommonContext(url) {
    url.searchParams.set(
      "from",
      "security-intelligence-library"
    );

    url.searchParams.set(
      "context",
      window.location.pathname
    );

    url.searchParams.set(
      "contextTitle",
      currentPageTitle()
    );
  }

  function applyVulnerabilityContext(context) {
    const link = document.querySelector(
      '[data-suite-key="vulnerability"]'
    );

    if (!link) return;

    const cves = Array.isArray(context?.cves)
      ? context.cves
      : [];

    if (!cves.length) return;

    const url = new URL(link.href);

    addCommonContext(url);
    url.searchParams.set("scope", "all");
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

  function applyThreatContext(context) {
    const link = document.querySelector(
      '[data-suite-key="investigate"]'
    );

    if (!link) return;

    const actors = Array.isArray(context?.actors)
      ? context.actors
      : [];

    const techniques = Array.isArray(context?.techniques)
      ? context.techniques
      : [];

    if (!actors.length && !techniques.length) return;

    const url = new URL(link.href);

    addCommonContext(url);

    url.searchParams.delete("actor");
    url.searchParams.delete("technique");
    url.searchParams.delete("entity");

    for (const actor of actors) {
      url.searchParams.append("actor", actor);
    }

    for (const technique of techniques) {
      url.searchParams.append("technique", technique);
    }

    // Only auto-select when there is one unambiguous primary entity.
    if (actors.length === 1) {
      url.searchParams.set("entity", `actor:${actors[0]}`);
    } else if (actors.length === 0 && techniques.length === 1) {
      url.searchParams.set(
        "entity",
        `technique:${techniques[0]}`
      );
    }

    link.href = url.toString();

    const small = link.querySelector("small");
    if (!small) return;

    if (actors.length === 1) {
      small.textContent = `Investigate · ${actors[0]}`;
    } else if (actors.length > 1) {
      small.textContent =
        `Investigate · ${actors.length} actors`;
    } else if (techniques.length === 1) {
      small.textContent =
        `Investigate · ${techniques[0]}`;
    } else {
      small.textContent =
        `Investigate · ${techniques.length} ATT&CK`;
    }
  }

  async function initialize() {
    const context = await loadArticleContext();
    if (!context) return;

    applyThreatContext(context);
    applyVulnerabilityContext(context);
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

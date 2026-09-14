(() => {
  const NAV_ID = "security-intelligence-suite-nav";
  const SUITE_ITEMS = [
    {
      key: "library",
      label: "Security Intelligence Library",
      path: "/security-intelligence-library/",
      phase: "Observe / Interpret"
    },
    {
      key: "investigate",
      label: "Threat Investigation",
      path: "/threat-investigation-dashboard/",
      phase: "Investigate / Relate"
    },
    {
      key: "vulnerability",
      label: "Vulnerability Intelligence",
      path: "/vulnerability-intelligence-dashboard/",
      phase: "Prioritize"
    }
  ];

  function activeKey() {
    const path = window.location.pathname;
    if (path.includes("/threat-investigation-dashboard/")) return "investigate";
    if (path.includes("/vulnerability-intelligence-dashboard/")) return "vulnerability";
    return "library";
  }

  function suiteUrl(path) {
    return `${window.location.origin}${path}`;
  }

  function buildSuiteNav() {
    const existing = document.getElementById(NAV_ID);
    if (existing) existing.remove();

    const bar = document.createElement("div");
    bar.id = NAV_ID;
    bar.className = "sil-suite-bar";
    bar.setAttribute("role", "navigation");
    bar.setAttribute("aria-label", "Security Intelligence Suite");

    const inner = document.createElement("div");
    inner.className = "sil-suite-bar__inner md-grid";

    const brand = document.createElement("span");
    brand.className = "sil-suite-bar__brand";
    brand.textContent = "SECURITY INTELLIGENCE SUITE";
    inner.appendChild(brand);

    const links = document.createElement("div");
    links.className = "sil-suite-bar__links";
    const current = activeKey();

    SUITE_ITEMS.forEach((item) => {
      const link = document.createElement("a");
      link.className = "sil-suite-link";
      link.href = suiteUrl(item.path);
      link.dataset.suiteKey = item.key;
      link.innerHTML = `<strong>${item.label}</strong><small>${item.phase}</small>`;
      if (item.key === current) {
        link.classList.add("is-active");
        link.setAttribute("aria-current", "page");
      }
      links.appendChild(link);
    });

    inner.appendChild(links);
    bar.appendChild(inner);

    const header = document.querySelector(".md-header");
    if (header?.parentNode) {
      header.parentNode.insertBefore(bar, header);
    } else {
      document.body.prepend(bar);
    }
  }

  function initialize() {
    if (!document.body) return;
    buildSuiteNav();
  }

  if (typeof document$ !== "undefined" && document$?.subscribe) {
    document$.subscribe(initialize);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialize, { once: true });
  } else {
    initialize();
  }
})();

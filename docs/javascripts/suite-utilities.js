(() => {
  'use strict';

  const REPOSITORIES = [
    {
      match: '/security-intelligence-library/',
      url: 'https://github.com/peridotan/security-intelligence-library'
    },
    {
      match: '/threat-investigation-dashboard/',
      url: 'https://github.com/peridotan/threat-investigation-dashboard'
    },
    {
      match: '/vulnerability-intelligence-dashboard/',
      url: 'https://github.com/peridotan/vulnerability-intelligence-dashboard'
    }
  ];

  function repositoryUrl() {
    const path = window.location.pathname;
    return REPOSITORIES.find((item) => path.includes(item.match))?.url || null;
  }

  function topbarInner() {
    return document.querySelector('.suite-topbar-inner, .sil-suite-bar__inner');
  }

  function fontControl(inner) {
    return inner?.querySelector('.font-size-control, .sil-font-size-control') || null;
  }

  function ensureUtilities() {
    const inner = topbarInner();
    if (!inner) return;

    let utilities = inner.querySelector('.suite-topbar-utilities');
    if (!utilities) {
      utilities = document.createElement('div');
      utilities.className = 'suite-topbar-utilities';
      inner.appendChild(utilities);
    }

    let repoLink = utilities.querySelector('.suite-repository-link');
    if (!repoLink) {
      const url = repositoryUrl();
      if (url) {
        repoLink = document.createElement('a');
        repoLink.className = 'suite-repository-link';
        repoLink.href = url;
        repoLink.target = '_blank';
        repoLink.rel = 'noopener noreferrer';
        repoLink.textContent = 'GitHub Repository ↗';
        repoLink.setAttribute('aria-label', 'GitHub Repositoryを新しいタブで開く');
        utilities.appendChild(repoLink);
      }
    }

    const font = fontControl(inner);
    if (font && font.parentElement !== utilities) {
      utilities.appendChild(font);
    }
  }

  function ensureTopButton() {
    let button = document.getElementById('suite-top-button');
    if (!button) {
      button = document.createElement('button');
      button.id = 'suite-top-button';
      button.className = 'suite-top-button';
      button.type = 'button';
      button.textContent = '↑ Top';
      button.setAttribute('aria-label', 'ページ上部へ戻る');
      button.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
      document.body.appendChild(button);
    }

    const syncVisibility = () => {
      button.classList.toggle('is-visible', window.scrollY > 500);
    };

    if (!button.dataset.scrollBound) {
      window.addEventListener('scroll', syncVisibility, { passive: true });
      button.dataset.scrollBound = 'true';
    }
    syncVisibility();
  }

  function initialize() {
    if (!document.body) return;
    ensureUtilities();
    ensureTopButton();
  }

  if (typeof document$ !== 'undefined' && document$?.subscribe) {
    document$.subscribe(initialize);
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize, { once: true });
  } else {
    initialize();
  }
})();

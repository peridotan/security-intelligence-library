(() => {
  'use strict';

  const CONTROL_ID = 'security-intelligence-suite-font-size';
  const STORAGE_KEY = 'peridotan-security-suite-font-size-v1';
  const LEGACY_KEYS = ['peridotan-threat-investigation-font-size-v1'];
  const SIZES = {
    standard: { label: '標準', scale: 1 },
    large: { label: '大', scale: 1.15 },
    xlarge: { label: '特大', scale: 1.30 }
  };

  const root = document.documentElement;
  const originalRootInlineFontSize = root.style.fontSize || '';
  const baseRootFontSize = parseFloat(getComputedStyle(root).fontSize) || 16;

  function isValid(value) {
    return Object.prototype.hasOwnProperty.call(SIZES, value);
  }

  function safeGet(key) {
    try { return localStorage.getItem(key); } catch (_error) { return null; }
  }

  function safeSet(key, value) {
    try { localStorage.setItem(key, value); } catch (_error) {}
  }

  function readPreference() {
    const current = safeGet(STORAGE_KEY);
    if (isValid(current)) return current;
    for (const key of LEGACY_KEYS) {
      const legacy = safeGet(key);
      if (isValid(legacy)) {
        safeSet(STORAGE_KEY, legacy);
        return legacy;
      }
    }
    return 'standard';
  }

  function applyRootScale(scale) {
    if (scale === 1) {
      if (originalRootInlineFontSize) root.style.fontSize = originalRootInlineFontSize;
      else root.style.removeProperty('font-size');
      return;
    }
    root.style.fontSize = `${Number((baseRootFontSize * scale).toFixed(3))}px`;
  }

  function applyPreference(value, persist = true) {
    const next = isValid(value) ? value : 'standard';
    root.dataset.fontSize = next;
    root.style.setProperty('--suite-font-scale', String(SIZES[next].scale));
    applyRootScale(SIZES[next].scale);

    document.querySelectorAll('#security-intelligence-suite-font-size [data-font-size]').forEach((button) => {
      button.setAttribute('aria-pressed', button.dataset.fontSize === next ? 'true' : 'false');
    });

    const status = document.querySelector(`#${CONTROL_ID} .sil-font-size-status`);
    if (status) status.textContent = `文字サイズを${SIZES[next].label}に変更しました。`;
    if (persist) safeSet(STORAGE_KEY, next);
  }

  function buildControl() {
    const inner = document.querySelector('.sil-suite-bar__inner');
    if (!inner) return null;

    document.getElementById(CONTROL_ID)?.remove();

    const control = document.createElement('div');
    control.id = CONTROL_ID;
    control.className = 'sil-font-size-control';
    control.innerHTML = `
      <span class="sil-font-size-label"><b aria-hidden="true">Aa</b><span>文字サイズ</span></span>
      <div class="sil-font-size-buttons" role="group" aria-label="文字サイズ">
        <button type="button" data-font-size="standard" aria-pressed="true" title="標準 (100%)">標準</button>
        <button type="button" data-font-size="large" aria-pressed="false" title="大 (115%)">大</button>
        <button type="button" data-font-size="xlarge" aria-pressed="false" title="特大 (130%)">特大</button>
      </div>
      <span class="sil-font-size-status sil-visually-hidden" aria-live="polite"></span>
    `;

    control.querySelectorAll('[data-font-size]').forEach((button) => {
      button.addEventListener('click', () => applyPreference(button.dataset.fontSize));
    });

    inner.appendChild(control);
    return control;
  }

  function initialize() {
    if (!document.body) return;
    buildControl();
    applyPreference(readPreference(), false);
  }

  if (typeof document$ !== 'undefined' && document$?.subscribe) {
    document$.subscribe(initialize);
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize, { once: true });
  } else {
    initialize();
  }
})();

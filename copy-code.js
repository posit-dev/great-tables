/**
 * Custom copy-code button for Great Docs
 *
 * Replaces Quarto's default code-copy with a consistent top-right button
 * that floats properly and works in both light and dark modes.
 *
 * Handles:
 *  - Buttons injected by post-render.py (.gd-code-copy inside .gd-code-nav)
 *  - Quarto-native code blocks (pre.code-with-copy) that lack a custom button
 */
(function () {
  "use strict";

  // i18n helper — read translations from <meta name="gd-i18n">
  var _i18nCache = null;
  function _gdT(key, fallback) {
    if (!_i18nCache) {
      try {
        var meta = document.querySelector('meta[name="gd-i18n"]');
        _i18nCache = meta ? JSON.parse(meta.getAttribute('content')) : {};
      } catch (e) { _i18nCache = {}; }
    }
    return _i18nCache[key] || fallback;
  }

  // Inline SVG icons — no external dependency
  var COPY_ICON =
    '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" ' +
    'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" ' +
    'stroke-linecap="round" stroke-linejoin="round">' +
    '<rect x="9" y="9" width="13" height="13" rx="2" ry="2"/>' +
    '<path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>' +
    "</svg>";

  var CHECK_ICON =
    '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" ' +
    'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" ' +
    'stroke-linecap="round" stroke-linejoin="round">' +
    '<polyline points="20 6 9 17 4 12"/>' +
    "</svg>";

  /**
   * Walk up from the button to find the <code> element whose text to copy.
   */
  function getCodeText(button) {
    var scaffold = button.closest(".code-copy-outer-scaffold");
    if (scaffold) {
      var code = scaffold.querySelector("pre > code");
      if (code) return code.textContent;
    }
    // Fallback: walk up to the nav, then find sibling pre > code
    var nav = button.closest(".gd-code-nav");
    if (nav) {
      var container = nav.parentElement;
      if (container) {
        var code = container.querySelector("pre > code");
        if (code) return code.textContent;
      }
    }
    return "";
  }

  /**
   * Copy handler with visual feedback.
   */
  function handleCopy(event) {
    var button = event.currentTarget;
    var text = getCodeText(button);
    if (!text) return;

    navigator.clipboard.writeText(text).then(function () {
      button.innerHTML = CHECK_ICON;
      button.classList.add("gd-code-copied");
      button.setAttribute("title", _gdT("copied", "Copied!"));

      setTimeout(function () {
        button.innerHTML = COPY_ICON;
        button.classList.remove("gd-code-copied");
        button.setAttribute("title", _gdT("copy_to_clipboard", "Copy to clipboard"));
      }, 2000);
    });
  }

  /**
   * Create a gd-code-nav + gd-code-copy button element.
   */
  function createCopyButton() {
    var nav = document.createElement("nav");
    nav.className = "gd-code-nav";
    var btn = document.createElement("button");
    btn.className = "gd-code-copy";
    btn.title = _gdT("copy_to_clipboard", "Copy to clipboard");
    btn.innerHTML = COPY_ICON;
    btn.addEventListener("click", handleCopy);
    nav.appendChild(btn);
    return nav;
  }

  /**
   * Replace any leftover Quarto-native .code-copy-button with our component.
   */
  function replaceQuartoButtons() {
    document
      .querySelectorAll("button.code-copy-button")
      .forEach(function (oldBtn) {
        var nav = createCopyButton();

        // The Quarto button lives inside a wrapper div; insert the nav there
        var parent = oldBtn.parentElement;
        if (parent) {
          parent.insertBefore(nav, oldBtn);
          parent.removeChild(oldBtn);
          // Ensure the wrapper acts as a positioning anchor
          parent.style.position = "relative";
        }
      });
  }

  /**
   * Inject a copy button into any code block that doesn't already have one.
   * Targets <div class="sourceCode"> wrappers and Quarto <pre> blocks.
   */
  function injectMissingButtons() {
    // Find all <div class="sourceCode"> that aren't inside a scaffold
    document.querySelectorAll("div.sourceCode").forEach(function (div) {
      // Skip if already inside a scaffold with a button
      if (div.closest(".code-copy-outer-scaffold")) return;
      // Skip if already has a gd-code-nav
      if (div.querySelector(".gd-code-nav")) return;

      var code = div.querySelector("pre > code");
      if (!code) return;

      div.style.position = "relative";
      div.prepend(createCopyButton());
    });

    // Also catch standalone <pre class="sourceCode"> not inside a div.sourceCode
    document.querySelectorAll("pre.sourceCode").forEach(function (pre) {
      var parent = pre.parentElement;
      // Skip if already handled
      if (parent && parent.classList.contains("sourceCode")) return;
      if (parent && parent.querySelector(".gd-code-nav")) return;
      if (pre.closest(".code-copy-outer-scaffold")) return;

      var code = pre.querySelector("code");
      if (!code) return;

      // Wrap in a relative container
      if (parent) {
        parent.style.position = "relative";
        parent.insertBefore(createCopyButton(), pre);
      }
    });
  }

  function init() {
    // 1. Wire up buttons that post-render.py already injected
    document.querySelectorAll(".gd-code-copy").forEach(function (btn) {
      btn.innerHTML = COPY_ICON;
      btn.addEventListener("click", handleCopy);
    });

    // 2. Convert any remaining Quarto-native copy buttons
    replaceQuartoButtons();

    // 3. Inject buttons into code blocks that have none
    injectMissingButtons();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

/**
 * Heading anchors for Great Docs
 *
 * Quarto adds anchor links to h2-h6 headings only. Great Docs shifts heading
 * levels by -1, so a page's top-level sections have h1 headings, which this
 * script anchors like the others. The id stays on the section, as Pandoc puts
 * it, and the link uses it.
 *
 * Clicking any anchor link also copies the link's URL to the clipboard and
 * briefly confirms the copy beside the icon.
 */
(function () {
  "use strict";

  // i18n helper — read translations from <meta name="gd-i18n">
  var _i18nCache = null;
  function _gdT(key, fallback) {
    if (!_i18nCache) {
      try {
        var meta = document.querySelector('meta[name="gd-i18n"]');
        _i18nCache = meta ? JSON.parse(meta.getAttribute("content")) : {};
      } catch (e) { _i18nCache = {}; }
    }
    return _i18nCache[key] || fallback;
  }

  var CONFIRM_MS = 1500;

  /**
   * Anchor the h1 headings of top-level sections. Pages without Quarto's
   * anchor sections don't load AnchorJS and keep their headings unanchored.
   */
  function anchorSectionHeadings() {
    if (typeof window.AnchorJS !== "function") return;

    var headings = [];
    document
      .querySelectorAll("main section.level1[id] > h1:not(.no-anchor)")
      .forEach(function (heading) {
        if (heading.querySelector(":scope > .anchorjs-link")) return;
        // Quarto's table-of-contents links reveal the anchor of the heading
        // with a matching data-anchor-id
        heading.classList.add("anchored");
        heading.setAttribute("data-anchor-id", heading.parentElement.id);
        headings.push(heading);
      });
    if (!headings.length) return;

    // The same options as Quarto's own instance, whose icon defaults to
    // AnchorJS's link glyph
    var quartoLink = document.querySelector(".anchorjs-link[data-anchorjs-icon]");
    var icon = quartoLink ? quartoLink.getAttribute("data-anchorjs-icon") : "\ue9cb";
    var anchors = new window.AnchorJS();
    anchors.options = { placement: "right", icon: icon };
    anchors.add(headings);
  }

  /**
   * Label every anchor link with the action a click performs. `tooltips.js`
   * shows the title as a tooltip.
   */
  function labelLinks() {
    var label = _gdT("copy_link", "Copy link");
    document.querySelectorAll(".anchorjs-link").forEach(function (link) {
      link.setAttribute("aria-label", label);
      link.setAttribute("title", label);
    });
  }

  /**
   * Show the confirmation beside a link's icon, keeping the icon visible
   * after the page scrolls the heading out from under the pointer.
   */
  function confirmCopy(link) {
    var note = link.querySelector(".gd-anchor-copied");
    if (!note) {
      note = document.createElement("span");
      note.className = "gd-anchor-copied";
      note.setAttribute("role", "status");
      link.appendChild(note);
    }
    note.textContent = _gdT("link_copied", "Link copied!");
    link.classList.add("gd-anchor-link-copied");

    clearTimeout(link._gdCopiedTimer);
    link._gdCopiedTimer = setTimeout(function () {
      link.classList.remove("gd-anchor-link-copied");
    }, CONFIRM_MS);
  }

  /**
   * Copy an anchor link's URL on a plain click. The click still follows the
   * link, so the address bar shows the section's URL too.
   */
  function handleClick(event) {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
      return;
    }
    var link = event.target.closest && event.target.closest(".anchorjs-link");
    if (!link || !navigator.clipboard) return;

    var url = new URL(link.getAttribute("href"), window.location.href).href;
    navigator.clipboard.writeText(url).then(
      function () { confirmCopy(link); },
      function () {}
    );
  }

  function init() {
    anchorSectionHeadings();
    labelLinks();
    document.addEventListener("click", handleClick);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

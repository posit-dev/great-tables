/**
 * Color Swatch Extension for Great Docs
 *
 * Handles Tippy.js tooltips, click-to-copy with feedback overlay,
 * and tooltip copy buttons for the color-swatch shortcode.
 */
(function () {
  "use strict";

  var containers = document.querySelectorAll(".gd-color-swatch");
  if (!containers.length) return;

  // Check icon SVG for copy feedback overlay
  var checkSvg =
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" ' +
    'fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" ' +
    'stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>';

  /**
   * Copy text to clipboard with fallback for non-HTTPS contexts.
   */
  function copyToClipboard(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    // Fallback: hidden textarea + execCommand
    return new Promise(function (resolve, reject) {
      var ta = document.createElement("textarea");
      ta.value = text;
      ta.style.position = "fixed";
      ta.style.left = "-9999px";
      ta.style.opacity = "0";
      document.body.appendChild(ta);
      ta.select();
      try {
        document.execCommand("copy");
        resolve();
      } catch (err) {
        reject(err);
      } finally {
        document.body.removeChild(ta);
      }
    });
  }

  /**
   * Show a brief checkmark overlay on a swatch element after copying.
   */
  function showCopyFeedback(el) {
    var overlay = document.createElement("div");
    overlay.className = "gd-swatch-copy-overlay";
    overlay.innerHTML = checkSvg;
    el.appendChild(overlay);

    // Announce for screen readers
    var liveRegion = document.getElementById("gd-cs-live");
    if (liveRegion) {
      liveRegion.textContent = "Copied";
    }

    requestAnimationFrame(function () {
      overlay.style.opacity = "1";
      setTimeout(function () {
        overlay.style.opacity = "0";
        setTimeout(function () {
          overlay.remove();
        }, 300);
      }, 700);
    });
  }

  /**
   * Get the hex value to copy from a swatch element.
   */
  function getHexFromEl(el) {
    return (
      el.getAttribute("data-hex") ||
      el.querySelector("[data-hex]")?.getAttribute("data-hex") ||
      ""
    );
  }

  /**
   * Handle click-to-copy on a swatch.
   */
  function handleSwatchClick(e) {
    var el = e.currentTarget;
    var hex = getHexFromEl(el);
    if (!hex) return;

    // Find the color fill element for the overlay
    var colorEl = el.classList.contains("gd-swatch-color")
      ? el
      : el.querySelector(".gd-swatch-color") || el;

    copyToClipboard(hex).then(function () {
      showCopyFeedback(colorEl);
    });
  }

  /**
   * Handle keyboard activation (Enter/Space).
   */
  function handleSwatchKeydown(e) {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      handleSwatchClick(e);
    }
  }

  /**
   * Initialize tooltips on elements with data-tooltip-html.
   */
  function initTooltips(container) {
    if (typeof tippy === "undefined") return;

    var els = container.querySelectorAll("[data-tooltip-html]");
    els.forEach(function (el) {
      var content = el.getAttribute("data-tooltip-html");
      if (!content) return;

      tippy(el, {
        content: content,
        allowHTML: true,
        placement: "top",
        delay: [150, 100],
        interactive: true,
        appendTo: document.body,
        maxWidth: 320,
        onShown: function (instance) {
          // Attach copy handlers to tooltip copy buttons
          var btns = instance.popper.querySelectorAll(".gd-cs-tooltip-copy");
          btns.forEach(function (btn) {
            btn.addEventListener("click", function (e) {
              e.stopPropagation();
              var hex = btn.getAttribute("data-hex");
              if (hex) {
                copyToClipboard(hex).then(function () {
                  btn.textContent = "\u2713";
                  setTimeout(function () {
                    btn.innerHTML = "&#128203;";
                  }, 1000);
                });
              }
            });
          });
        },
      });
    });
  }

  /**
   * Initialize a single color-swatch container.
   */
  function initContainer(container) {
    // Circle swatches — click on the wrapper (.gd-swatch)
    var swatches = container.querySelectorAll(".gd-swatch");
    swatches.forEach(function (el) {
      el.addEventListener("click", handleSwatchClick);
      el.addEventListener("keydown", handleSwatchKeydown);
    });

    // Rectangle swatches — click on the strip (.gd-swatch-rect)
    var rects = container.querySelectorAll(".gd-swatch-rect");
    rects.forEach(function (el) {
      el.addEventListener("click", handleSwatchClick);
      el.addEventListener("keydown", handleSwatchKeydown);
    });

    // Tooltips (attach to color fills and rects)
    initTooltips(container);
  }

  // Create a live region for screen reader announcements
  if (!document.getElementById("gd-cs-live")) {
    var live = document.createElement("div");
    live.id = "gd-cs-live";
    live.setAttribute("aria-live", "polite");
    live.setAttribute("aria-atomic", "true");
    live.className = "visually-hidden";
    document.body.appendChild(live);
  }

  // Initialize all containers
  containers.forEach(initContainer);
})();

/**
 * GD Lightbox Annotate — Image Annotation Markers & Tooltips
 *
 * Reads JSON annotations from data-gd-lightbox-annotations attributes and
 * renders numbered markers over the image with hover/click tooltips.
 *
 * Annotation JSON schema:
 *   [{ "x": 20, "y": 15, "label": "1", "text": "Description" }, ...]
 *   - x, y: percentage position (0-100) relative to image bounds
 *   - label: short text shown inside the marker circle (e.g., "1", "A")
 *   - text: tooltip description shown on hover/click
 *   - color (optional): marker color override
 *
 * No dependencies. ~4KB minified+gzipped target.
 */
(function () {
  "use strict";

  var PREFIX = "gd-annotate";
  var ATTR = "data-gd-lightbox-annotations";

  function initAll() {
    var wrappers = document.querySelectorAll("[" + ATTR + "]");
    for (var i = 0; i < wrappers.length; i++) {
      initWrapper(wrappers[i]);
    }
  }

  /**
   * Parse a raw annotations attribute value into an array, or null if it is
   * absent / invalid / empty.
   */
  function parse(raw) {
    if (!raw) return null;
    try {
      var annotations = JSON.parse(raw);
      return Array.isArray(annotations) && annotations.length ? annotations : null;
    } catch (e) {
      // Not valid JSON — could be a file path (future: fetch)
      return null;
    }
  }

  function initWrapper(wrapper) {
    if (wrapper.dataset.gdAnnotateInit) return;
    wrapper.dataset.gdAnnotateInit = "true";

    var annotations = parse(wrapper.getAttribute(ATTR));
    if (!annotations) return;

    wrapper.style.position = "relative";
    var overlay = buildOverlay(annotations);
    wrapper.appendChild(overlay);

    // Close tooltips when clicking outside the wrapper
    document.addEventListener("click", function (e) {
      if (!wrapper.contains(e.target)) {
        closeAll(overlay);
      }
    });
  }

  /**
   * Build a `.gd-annotate-overlay` element populated with markers and tooltips
   * for the given annotations array, with all interactions wired up. The
   * overlay is `position:absolute; inset:0`, so the caller is responsible for
   * sizing/positioning its container to match the target image. Edge-aware
   * tooltip placement uses the overlay's own bounds.
   *
   * Reused by both the in-page annotator and the lightbox view.
   * @param {Array} annotations
   * @returns {HTMLElement} the overlay element
   */
  function buildOverlay(annotations) {
    var overlay = document.createElement("div");
    overlay.className = PREFIX + "-overlay";

    annotations.forEach(function (ann, idx) {
      var x = parseFloat(ann.x) || 0;
      var y = parseFloat(ann.y) || 0;
      var label = ann.label || String(idx + 1);
      var text = ann.text || "";
      var color = ann.color || null;

      // Marker element
      var marker = document.createElement("button");
      marker.className = PREFIX + "-marker";
      marker.setAttribute("aria-label", "Annotation " + label + ": " + text);
      marker.setAttribute("aria-expanded", "false");
      marker.setAttribute("type", "button");
      marker.style.left = x + "%";
      marker.style.top = y + "%";
      if (color) {
        marker.style.setProperty("--gd-annotate-marker-bg", color);
      }

      // Label inside marker
      var labelSpan = document.createElement("span");
      labelSpan.className = PREFIX + "-marker-label";
      labelSpan.textContent = label;
      marker.appendChild(labelSpan);

      // Pulse animation class (removed after first interaction)
      marker.classList.add(PREFIX + "-pulse");

      // Tooltip
      var tooltip = document.createElement("div");
      tooltip.className = PREFIX + "-tooltip";
      tooltip.setAttribute("role", "tooltip");
      tooltip.setAttribute("id", PREFIX + "-tip-" + idx + "-" + Date.now());
      marker.setAttribute("aria-describedby", tooltip.id);

      var tipLabel = document.createElement("strong");
      tipLabel.className = PREFIX + "-tooltip-label";
      tipLabel.textContent = label;
      tooltip.appendChild(tipLabel);

      if (text) {
        var tipText = document.createElement("span");
        tipText.className = PREFIX + "-tooltip-text";
        tipText.textContent = text;
        tooltip.appendChild(tipText);
      }

      marker.appendChild(tooltip);
      overlay.appendChild(marker);

      // Interaction: toggle tooltip on click/Enter
      marker.addEventListener("click", function (e) {
        e.stopPropagation();
        var isActive = marker.classList.contains(PREFIX + "-active");
        closeAll(overlay);
        if (!isActive) {
          marker.classList.add(PREFIX + "-active");
          marker.setAttribute("aria-expanded", "true");
          marker.classList.remove(PREFIX + "-pulse");
          positionTooltip(marker, tooltip, overlay);
        }
      });

      // Show on hover (desktop)
      marker.addEventListener("mouseenter", function () {
        marker.classList.remove(PREFIX + "-pulse");
        if (!marker.classList.contains(PREFIX + "-active")) {
          tooltip.classList.add(PREFIX + "-tooltip--hover");
          positionTooltip(marker, tooltip, overlay);
        }
      });

      marker.addEventListener("mouseleave", function () {
        tooltip.classList.remove(PREFIX + "-tooltip--hover");
      });

      // Keyboard: Enter/Space toggles, Escape closes
      marker.addEventListener("keydown", function (e) {
        if (e.key === "Escape") {
          closeAll(overlay);
          e.preventDefault();
        }
      });
    });

    return overlay;
  }

  function closeAll(overlay) {
    var active = overlay.querySelectorAll("." + PREFIX + "-active");
    for (var i = 0; i < active.length; i++) {
      active[i].classList.remove(PREFIX + "-active");
      active[i].setAttribute("aria-expanded", "false");
    }
  }

  /**
   * Position tooltip so it doesn't overflow the bounds element.
   * Prefers showing above the marker; falls back to below.
   */
  function positionTooltip(marker, tooltip, bounds) {
    // Reset positioning classes
    tooltip.classList.remove(
      PREFIX + "-tooltip--above",
      PREFIX + "-tooltip--below",
      PREFIX + "-tooltip--left",
      PREFIX + "-tooltip--right"
    );

    var boundsRect = bounds.getBoundingClientRect();
    var markerRect = marker.getBoundingClientRect();
    var markerCenterX = markerRect.left + markerRect.width / 2 - boundsRect.left;
    var markerTop = markerRect.top - boundsRect.top;

    // Default: above
    if (markerTop > 80) {
      tooltip.classList.add(PREFIX + "-tooltip--above");
    } else {
      tooltip.classList.add(PREFIX + "-tooltip--below");
    }

    // Horizontal: center, but shift if near edges
    var boundsWidth = boundsRect.width;
    if (markerCenterX < boundsWidth * 0.25) {
      tooltip.classList.add(PREFIX + "-tooltip--right");
    } else if (markerCenterX > boundsWidth * 0.75) {
      tooltip.classList.add(PREFIX + "-tooltip--left");
    }
  }

  // Init on DOM ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAll);
  } else {
    initAll();
  }

  // Re-init after Quarto navigation (for SPA-like navigation)
  document.addEventListener("quarto-nav", initAll);

  // Public API — consumed by the lightbox to render the same annotation
  // markers/tooltips over the enlarged image.
  window.GDAnnotate = {
    parse: parse,
    buildOverlay: buildOverlay,
    closeAll: closeAll,
  };
})();

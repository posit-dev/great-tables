/**
 * Responsive Tables for Great Docs
 *
 * Enhances table display on narrow viewports with:
 * - Horizontal scroll containers for wide tables
 * - Touch-friendly scroll indicators
 * - Consistent dark mode styling
 *
 * Uses double-wrapper structure for Safari compatibility:
 * - Outer wrapper (.gd-table-responsive) has position:relative for indicators
 * - Inner wrapper (.gd-table-scroll) has overflow-x:auto for scrolling
 */
(function () {
  "use strict";

  // Minimum width difference to consider a table "wide"
  var OVERFLOW_THRESHOLD = 20;

  /**
   * Wrap a table in a responsive scroll container
   */
  function wrapTable(table) {
    // Skip if already wrapped
    if (table.closest(".gd-table-responsive")) {
      return;
    }

    // Skip tables inside code blocks or other special contexts
    if (table.closest("pre, code, .sourceCode")) {
      return;
    }

    // Skip Great Tables output — these have their own styling and layout
    if (table.classList.contains("gt_table")) {
      return;
    }

    // Create outer wrapper (for indicator positioning)
    var outerWrapper = document.createElement("div");
    outerWrapper.className = "gd-table-responsive";

    // Create inner scroll container
    var scrollContainer = document.createElement("div");
    scrollContainer.className = "gd-table-scroll";
    scrollContainer.setAttribute("tabindex", "0");
    scrollContainer.setAttribute("role", "region");
    scrollContainer.setAttribute("aria-label", "Scrollable table");

    // Insert outer wrapper and move table inside inner container
    table.parentNode.insertBefore(outerWrapper, table);
    scrollContainer.appendChild(table);
    outerWrapper.appendChild(scrollContainer);

    // Add scroll indicators to outer wrapper (not inside scroll container)
    var indicatorLeft = document.createElement("div");
    indicatorLeft.className = "gd-table-scroll-indicator gd-table-scroll-left";
    indicatorLeft.innerHTML = '<span class="gd-scroll-arrow">&lsaquo;</span>';
    outerWrapper.appendChild(indicatorLeft);

    var indicatorRight = document.createElement("div");
    indicatorRight.className = "gd-table-scroll-indicator gd-table-scroll-right";
    indicatorRight.innerHTML = '<span class="gd-scroll-arrow">&rsaquo;</span>';
    outerWrapper.appendChild(indicatorRight);

    // Update scroll indicator visibility based on scroll position
    function updateScrollIndicators() {
      var scrollLeft = scrollContainer.scrollLeft;
      var maxScroll = scrollContainer.scrollWidth - scrollContainer.clientWidth;

      // Only show indicators if scrollable
      if (maxScroll <= OVERFLOW_THRESHOLD) {
        indicatorLeft.classList.remove("visible");
        indicatorRight.classList.remove("visible");
        return;
      }

      // Show/hide based on scroll position
      indicatorLeft.classList.toggle("visible", scrollLeft > OVERFLOW_THRESHOLD);
      indicatorRight.classList.toggle("visible", scrollLeft < maxScroll - OVERFLOW_THRESHOLD);
    }

    // Debounced scroll handler
    var scrollTimeout;
    scrollContainer.addEventListener("scroll", function () {
      if (scrollTimeout) {
        clearTimeout(scrollTimeout);
      }
      scrollTimeout = setTimeout(updateScrollIndicators, 50);
    });

    // Click to scroll
    indicatorLeft.addEventListener("click", function () {
      scrollContainer.scrollBy({ left: -150, behavior: "smooth" });
    });

    indicatorRight.addEventListener("click", function () {
      scrollContainer.scrollBy({ left: 150, behavior: "smooth" });
    });

    // Initial indicator update
    setTimeout(updateScrollIndicators, 100);

    // Update on resize
    var resizeObserver;
    if (typeof ResizeObserver !== "undefined") {
      resizeObserver = new ResizeObserver(function () {
        updateScrollIndicators();
      });
      resizeObserver.observe(scrollContainer);
    }

    return outerWrapper;
  }

  /**
   * Scale content inside a .scale-to-fit container to fill the container width.
   *
   * Usage in .qmd:
   *   :::{.scale-to-fit}
   *   ```{python}
   *   my_wide_table()
   *   ```
   *   :::
   */
  // Viewport breakpoints for keyword-based min-scale thresholds.
  // Below the given width, scaling is disabled and horizontal scrolling is
  // used instead.
  var SCALE_BREAKPOINTS = { mobile: 576, tablet: 768, desktop: 992 };

  /**
   * Parse a data-min-scale attribute value.
   * Returns an object: { type: "number", value: 0.4 }
   *                  or { type: "keyword", width: 768 }
   *                  or null (no threshold).
   */
  function parseMinScale(raw) {
    if (!raw) return null;
    var lower = raw.toLowerCase();
    if (SCALE_BREAKPOINTS[lower] !== undefined) {
      return { type: "keyword", width: SCALE_BREAKPOINTS[lower] };
    }
    var n = parseFloat(raw);
    if (!isNaN(n) && n > 0 && n < 1) {
      return { type: "number", value: n };
    }
    return null;
  }

  function applyScaleToFit(container, minScaleObj) {
    // minScaleObj: parsed result from parseMinScale(), or null.
    // Per-container data-min-scale overrides the page/global threshold.
    var containerMinScale = parseMinScale(container.getAttribute("data-min-scale"));
    if (containerMinScale) {
      minScaleObj = containerMinScale;
    }
    // Find the content to scale — first child element that has measurable width
    var inner = container.querySelector(".cell-output-display, .cell-output, table, .gt_table");
    if (!inner) {
      // Fall back to first element child
      inner = container.firstElementChild;
    }
    if (!inner) return;

    // Wrap content in a scaling div if not already wrapped
    var scaleWrapper = container.querySelector(".gd-scale-wrapper");
    if (!scaleWrapper) {
      scaleWrapper = document.createElement("div");
      scaleWrapper.className = "gd-scale-wrapper";
      // Move all children into the wrapper
      while (container.firstChild) {
        scaleWrapper.appendChild(container.firstChild);
      }
      container.appendChild(scaleWrapper);
    }

    function updateScale() {
      // Reset transform to measure natural width
      scaleWrapper.style.transform = "none";
      scaleWrapper.style.transformOrigin = "top left";
      scaleWrapper.style.width = "max-content";
      scaleWrapper.style.height = "";
      container.style.height = "";

      // Allow layout to settle
      var containerWidth = container.clientWidth;
      var contentWidth = scaleWrapper.scrollWidth;

      if (contentWidth <= 0 || containerWidth <= 0) return;

      var scale = containerWidth / contentWidth;

      // Never upscale — only shrink to fit
      if (scale >= 1) {
        scaleWrapper.style.transform = "none";
        scaleWrapper.style.width = "";
        scaleWrapper.style.height = "";
        container.style.height = "";
        container.style.overflow = "";
        container.classList.remove("gd-scale-scrollable");
        return;
      }

      // Check whether we should skip scaling and scroll instead.
      // Keyword thresholds: if viewport is at or below the breakpoint, scroll.
      // Numeric thresholds: if computed scale < min, scroll.
      var shouldScroll = false;
      if (minScaleObj) {
        if (minScaleObj.type === "keyword") {
          shouldScroll = window.innerWidth <= minScaleObj.width;
        } else if (minScaleObj.type === "number") {
          shouldScroll = scale < minScaleObj.value;
        }
      }

      if (shouldScroll) {
        scaleWrapper.style.transform = "none";
        scaleWrapper.style.width = "max-content";
        scaleWrapper.style.height = "";
        container.style.height = "";
        container.style.overflowX = "auto";
        container.classList.add("gd-scale-scrollable");
        return;
      }

      // Apply scale
      scaleWrapper.style.transform = "scale(" + scale + ")";
      scaleWrapper.style.width = contentWidth + "px";

      // Adjust container height to match scaled content
      var contentHeight = scaleWrapper.scrollHeight;
      container.style.height = (contentHeight * scale) + "px";
      container.style.overflow = "hidden";
    }

    updateScale();

    // Re-scale on window resize
    if (typeof ResizeObserver !== "undefined") {
      var ro = new ResizeObserver(function () {
        updateScale();
      });
      ro.observe(container);
    }
  }

  /**
   * Initialize responsive tables
   */
  function init() {
    // Find all tables in the content area
    var content = document.querySelector("#quarto-content, .content, main, article");
    if (!content) {
      content = document.body;
    }

    var tables = content.querySelectorAll("table");
    for (var i = 0; i < tables.length; i++) {
      wrapTable(tables[i]);
    }

    // Apply scale-to-fit to marked containers (manual :::{.scale-to-fit})
    var fitContainers = content.querySelectorAll(".scale-to-fit");
    for (var i = 0; i < fitContainers.length; i++) {
      applyScaleToFit(fitContainers[i]);
    }

    // Auto-scale elements matching CSS selectors from config or page frontmatter.
    // Global selectors come from: <meta name="gd-scale-to-fit" data-selectors='[...]'>
    // Page-level selectors come from: <meta name="gd-scale-to-fit-page" data-selectors='[...]'>
    // Both may carry data-min-scale (float like "0.4" or keyword like "tablet").
    var allSelectors = [];
    var minScaleObj = null;
    var globalMeta = document.querySelector('meta[name="gd-scale-to-fit"]');
    var pageMeta = document.querySelector('meta[name="gd-scale-to-fit-page"]');

    // Page-level takes precedence over global for both selectors and min-scale
    var activeMeta = pageMeta || globalMeta;
    if (activeMeta) {
      try { allSelectors = JSON.parse(activeMeta.getAttribute("data-selectors") || "[]"); } catch (e) { /* ignore */ }
      minScaleObj = parseMinScale(activeMeta.getAttribute("data-min-scale"));
      // If page meta didn't specify min-scale, fall back to global meta
      if (!minScaleObj && pageMeta && globalMeta && pageMeta !== globalMeta) {
        minScaleObj = parseMinScale(globalMeta.getAttribute("data-min-scale"));
      }
    }

    // Also pass minScaleObj to manual .scale-to-fit containers
    for (var i = 0; i < fitContainers.length; i++) {
      // Re-apply with minScaleObj if we have one (first call was with null)
      if (minScaleObj) { applyScaleToFit(fitContainers[i], minScaleObj); }
    }

    for (var si = 0; si < allSelectors.length; si++) {
      var selector = allSelectors[si];
      var matches;
      try { matches = content.querySelectorAll(selector); } catch (e) { continue; }

      for (var mi = 0; mi < matches.length; mi++) {
        var el = matches[mi];
        // Walk up to the nearest output container to scale
        var scaleTarget = el.closest(".cell-output-display") || el.closest(".cell-output") || el.parentElement;
        if (scaleTarget && !scaleTarget.classList.contains("scale-to-fit")) {
          scaleTarget.classList.add("scale-to-fit");
          applyScaleToFit(scaleTarget, minScaleObj);
        }
      }
    }

    // Handle dynamically added tables (e.g., from AJAX)
    if (typeof MutationObserver !== "undefined") {
      var observer = new MutationObserver(function (mutations) {
        for (var i = 0; i < mutations.length; i++) {
          var mutation = mutations[i];
          for (var j = 0; j < mutation.addedNodes.length; j++) {
            var node = mutation.addedNodes[j];
            if (node.nodeType === 1) {
              // Element node
              if (node.tagName === "TABLE") {
                wrapTable(node);
              } else {
                var nestedTables = node.querySelectorAll
                  ? node.querySelectorAll("table")
                  : [];
                for (var k = 0; k < nestedTables.length; k++) {
                  wrapTable(nestedTables[k]);
                }
              }
            }
          }
        }
      });

      observer.observe(document.body, {
        childList: true,
        subtree: true,
      });
    }
  }

  // Run after DOM is ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

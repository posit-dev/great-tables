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

  // Column sizing heuristics (lengths in em units of the table's font size).
  // Columns whose single-line width is at most SHORT_COL_EM are "short"
  // (names, types, values); wider ones are "prose". Prose columns give up
  // width down to PROSE_COMFORT_EM before short columns start to wrap, and
  // normally no further than PROSE_MIN_EM. Only to avoid scrolling do they
  // go down to PROSE_TIGHT_EM; a table that scrolls anyway keeps prose at
  // PROSE_MIN_EM so it stays readable. A short column first wraps only
  // its outlier cells, down to the TYPICAL_CELL_PERCENTILE cell width. Cells
  // count as outliers only if wider than OUTLIER_RATIO times that width, so
  // a label just a little longer than the rest isn't wrapped to save a few
  // pixels.
  var SHORT_COL_EM = 14;
  var PROSE_COMFORT_EM = 20;
  var PROSE_MIN_EM = 12;
  var PROSE_TIGHT_EM = 9;
  var TYPICAL_CELL_PERCENTILE = 0.8;
  var OUTLIER_RATIO = 1.25;

  function sum(values) {
    var total = 0;
    for (var i = 0; i < values.length; i++) total += values[i];
    return total;
  }

  // Table classes that Quarto/Pandoc/Bootstrap put on plain Markdown tables.
  // Tables carrying any other class have their own styling and are left alone.
  var PLAIN_TABLE_CLASS = /^(table|table-[\w-]+|caption-top|striped|hover|bordered|borderless|sm|small)$/;

  /**
   * Does the table carry author-specified column widths (e.g., from Quarto's
   * `tbl-colwidths` attribute or hand-written HTML)?
   */
  function hasExplicitWidths(table) {
    var cols = table.querySelectorAll(":scope > colgroup > col");
    for (var i = 0; i < cols.length; i++) {
      if (cols[i].style.width || cols[i].getAttribute("width")) return true;
    }
    var firstRow = table.rows[0];
    if (firstRow) {
      for (var j = 0; j < firstRow.cells.length; j++) {
        var cell = firstRow.cells[j];
        if (cell.style.width || cell.getAttribute("width")) return true;
      }
    }
    return false;
  }

  function isPlainTable(table) {
    for (var i = 0; i < table.classList.length; i++) {
      if (!PLAIN_TABLE_CLASS.test(table.classList[i])) return false;
    }
    return true;
  }

  /**
   * Rows whose cells map one-to-one onto the table's columns (no spans).
   * Returns an empty list if the table has fewer than two columns.
   */
  function simpleRows(table) {
    var ncols = 0;
    var i, j, span;
    for (i = 0; i < table.rows.length; i++) {
      span = 0;
      for (j = 0; j < table.rows[i].cells.length; j++) {
        span += table.rows[i].cells[j].colSpan || 1;
      }
      ncols = Math.max(ncols, span);
    }
    var rows = [];
    if (ncols < 2) return rows;
    for (i = 0; i < table.rows.length; i++) {
      var cells = table.rows[i].cells;
      if (cells.length !== ncols) continue;
      var simple = true;
      for (j = 0; j < cells.length; j++) {
        if ((cells[j].colSpan || 1) !== 1 || (cells[j].rowSpan || 1) !== 1) { simple = false; break; }
      }
      if (simple) rows.push(table.rows[i]);
    }
    return rows;
  }

  /** Single-line width of a cell's content plus its padding and borders. */
  function naturalCellWidth(cell, range) {
    var style = window.getComputedStyle(cell);
    var rect = cell.getBoundingClientRect();
    var chrome = parseFloat(style.paddingLeft) + parseFloat(style.paddingRight) + (rect.width - cell.clientWidth);
    range.selectNodeContents(cell);
    return range.getBoundingClientRect().width + chrome;
  }

  function percentile(values, p) {
    var sorted = values.slice().sort(function (a, b) { return a - b; });
    return sorted[Math.max(0, Math.ceil(p * sorted.length) - 1)];
  }

  /**
   * Size the columns of a plain Markdown table so it fits its container.
   *
   * Sizing every column to its single-line (max-content) width lets one
   * column of prose stretch the table far past the content area. Instead,
   * measure each column's single-line, typical-cell, and narrowest
   * (min-content) widths, then build a ladder of progressively narrower
   * column-width sets:
   *
   *   0. every column on one line
   *   1. prose columns wrapped down to PROSE_COMFORT_EM
   *   2. short columns wrapping their outlier cells (typical-cell width)
   *   3. prose columns wrapped down to PROSE_MIN_EM
   *   4. short columns at their min-content width
   *   5. prose columns down to PROSE_TIGHT_EM (only to avoid scrolling)
   *
   * The table takes the widest set that fits, interpolating between adjacent
   * sets to fill the container exactly. If even the narrowest set doesn't fit
   * the table scrolls horizontally, holding step 4 rather than step 5: once
   * scrolling is unavoidable, wider prose columns read better. Lengths never
   * drop below a column's min-content width, so fixed layout never clips
   * content.
   */
  function autoSizeTable(table, outerWrapper, scrollContainer) {
    var metrics = null;
    var lastWidth = -1;
    var colgroup = null;

    function reset() {
      if (colgroup && colgroup.parentNode) colgroup.parentNode.removeChild(colgroup);
      colgroup = null;
      table.style.tableLayout = "";
      table.style.width = "";
      outerWrapper.classList.remove("gd-table-fit", "gd-table-overflow");
    }

    function measure() {
      var rows = simpleRows(table);
      if (!rows.length || !table.offsetWidth) return null; // no simple row, or hidden
      reset();
      var cells = rows[0].cells;
      var max = [];
      var min = [];
      var typical = [];
      var range = document.createRange();
      var i, r;
      // Pad measurements slightly: fixed layout distributes borders and
      // subpixels differently, and a fraction of a pixel short wraps a line
      table.style.minWidth = "0";
      table.style.width = "max-content";
      for (i = 0; i < cells.length; i++) {
        max.push(Math.ceil(cells[i].getBoundingClientRect().width) + 2);
        var natural = [];
        for (r = 0; r < rows.length; r++) natural.push(naturalCellWidth(rows[r].cells[i], range));
        var typicalWidth = Math.ceil(percentile(natural, TYPICAL_CELL_PERCENTILE)) + 2;
        typical.push(max[i] > typicalWidth * OUTLIER_RATIO ? typicalWidth : max[i]);
      }
      table.style.width = "min-content";
      for (i = 0; i < cells.length; i++) min.push(Math.ceil(cells[i].getBoundingClientRect().width) + 2);
      table.style.width = "";
      table.style.minWidth = "";
      return {
        max: max,
        min: min,
        typical: typical,
        fontSize: parseFloat(window.getComputedStyle(table).fontSize) || 16,
      };
    }

    function setColumnWidths(widths, unit) {
      if (!colgroup) {
        colgroup = document.createElement("colgroup");
        colgroup.className = "gd-auto-colgroup";
        for (var i = 0; i < widths.length; i++) colgroup.appendChild(document.createElement("col"));
        table.insertBefore(colgroup, table.firstChild);
      }
      for (var j = 0; j < widths.length; j++) {
        colgroup.children[j].style.width = widths[j].toFixed(3) + unit;
      }
    }

    function layout(force) {
      if (table.closest(".scale-to-fit, .gd-table-nowrap")) {
        reset();
        return;
      }
      var available = scrollContainer.clientWidth;
      if (!available) return;
      var fontSize = parseFloat(window.getComputedStyle(table).fontSize) || 16;
      if (force || !metrics || metrics.fontSize !== fontSize) {
        metrics = measure();
        lastWidth = -1;
      }
      if (!metrics) return;
      if (available === lastWidth) return;
      lastWidth = available;

      var em = metrics.fontSize;
      var max = metrics.max;
      var min = metrics.min;
      // Width of each column at each step of the ladder (see above)
      var ladder = [[], [], [], [], [], []];
      var i;
      for (i = 0; i < max.length; i++) {
        var isShort = max[i] <= SHORT_COL_EM * em;
        var proseComfort = Math.min(max[i], Math.max(min[i], PROSE_COMFORT_EM * em));
        var proseMin = Math.min(max[i], Math.max(min[i], PROSE_MIN_EM * em));
        var shortTypical = Math.max(min[i], Math.min(max[i], metrics.typical[i]));
        ladder[0].push(max[i]);
        ladder[1].push(isShort ? max[i] : proseComfort);
        ladder[2].push(isShort ? shortTypical : proseComfort);
        ladder[3].push(isShort ? shortTypical : proseMin);
        ladder[4].push(isShort ? min[i] : proseMin);
        ladder[5].push(isShort ? min[i] : Math.min(proseMin, Math.max(min[i], PROSE_TIGHT_EM * em)));
      }

      // Everything fits on one line per row: natural browser layout
      if (sum(max) <= available) {
        reset();
        return;
      }

      // Find the widest step that fits, then interpolate toward the step
      // above it so the columns total exactly `available`
      var step = 1;
      while (step < ladder.length && sum(ladder[step]) > available) step++;
      if (step === ladder.length) {
        // Nothing left to give: scroll, with prose at its readable minimum
        var narrowest = ladder[4];
        setColumnWidths(narrowest, "px");
        table.style.tableLayout = "fixed";
        table.style.width = sum(narrowest) + "px";
        outerWrapper.classList.add("gd-table-overflow");
        outerWrapper.classList.remove("gd-table-fit");
        return;
      }
      var lo = ladder[step];
      var hi = ladder[step - 1];
      var ratio = sum(hi) > sum(lo) ? (available - sum(lo)) / (sum(hi) - sum(lo)) : 1;
      var widths = [];
      for (i = 0; i < lo.length; i++) widths.push(lo[i] + (hi[i] - lo[i]) * ratio);

      // Percentages (of a 100%-wide table) absorb subpixel rounding
      for (i = 0; i < widths.length; i++) widths[i] = (widths[i] / available) * 100;
      setColumnWidths(widths, "%");
      table.style.tableLayout = "fixed";
      table.style.width = "100%";
      outerWrapper.classList.add("gd-table-fit");
      outerWrapper.classList.remove("gd-table-overflow");
    }

    layout(true);

    if (typeof ResizeObserver !== "undefined") {
      new ResizeObserver(function () { layout(false); }).observe(scrollContainer);
    }

    // Web fonts and images change the measured widths once they load
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(function () { layout(true); });
    }
    var imgs = table.querySelectorAll("img");
    for (var k = 0; k < imgs.length; k++) {
      if (!imgs[k].complete) {
        imgs[k].addEventListener("load", function () { layout(true); });
      }
    }
  }

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

    // Choose a column sizing strategy:
    // - `.gd-table-nowrap` (on the table or an ancestor) opts out: one line
    //   per cell, horizontal scroll for wide tables (the legacy behavior)
    // - author-specified widths (e.g., `tbl-colwidths`): fill the content
    //   width and honor the given proportions
    // - plain Markdown tables: heuristic sizing (see autoSizeTable)
    // - anything else (custom-styled tables, data frames): untouched
    if (table.classList.contains("gd-table-nowrap") || table.closest(".gd-table-nowrap")) {
      outerWrapper.classList.add("gd-table-nowrap");
    } else if (hasExplicitWidths(table)) {
      outerWrapper.classList.add("gd-table-explicit");
    } else if (isPlainTable(table)) {
      outerWrapper.classList.add("gd-table-auto");
      autoSizeTable(table, outerWrapper, scrollContainer);
    }

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

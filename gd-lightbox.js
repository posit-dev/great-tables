/**
 * GD Lightbox — Great Docs Lightbox Engine
 *
 * A documentation-focused lightbox built from scratch. Features:
 * - Origin-aware zoom animation (image grows from thumbnail position)
 * - Dark-mode image variant swapping
 * - Gallery with filmstrip navigation
 * - Keyboard & touch navigation
 * - Copy/download/deep-link toolbar
 * - Accessible: focus trap, ARIA, screen reader announcements
 *
 * No dependencies. ~12KB minified+gzipped target.
 */
(function () {
  "use strict";

  // ---------------------------------------------------------------------------
  // Constants
  // ---------------------------------------------------------------------------

  const PREFIX = "gd-lightbox";
  const ATTR_LB = "data-gd-lightbox";
  const ATTR_ID = "data-gd-lightbox-id";
  const ATTR_GROUP = "data-gd-lightbox-group";
  const ATTR_DARK = "data-gd-lightbox-dark";
  const ATTR_CAPTION = "data-gd-lightbox-caption";
  const ATTR_CREDIT = "data-gd-lightbox-credit";
  const ATTR_DESC_POS = "data-gd-lightbox-desc-position";
  const ATTR_ZOOM_TARGET = "data-gd-lightbox-zoom-target";
  const ATTR_LOOP = "data-gd-lightbox-loop";
  const ATTR_AUTOPLAY = "data-gd-lightbox-autoplay";
  const ATTR_FULL_SRC = "data-gd-lightbox-full-src";

  const TRANSITION_MS = 300;
  const TOOLBAR_HIDE_MS = 3000;

  // ---------------------------------------------------------------------------
  // State
  // ---------------------------------------------------------------------------

  let overlay = null; // The lightbox overlay DOM element
  let isOpen = false;
  let currentIndex = -1;
  let currentGroup = null; // Array of items in the active gallery
  let allItems = []; // All lightbox items on the page
  let groups = {}; // { groupName: [items...] }
  let toolbarTimer = null;
  let previousFocus = null; // Element that had focus before lightbox opened
  let isDarkMode = false;
  let loopEnabled = true; // Whether gallery wraps around at ends
  let autoplayInterval = 0; // Autoplay interval in ms (0 = disabled)
  let autoplayTimer = null; // Active autoplay timer

  // Zoom state (toolbar-button controlled; zooms about the image center)
  let zoomScale = 1;
  const ZOOM_MIN = 1;
  const ZOOM_MAX = 4;
  const ZOOM_STEP = 0.5;

  // Pan state (drag the zoomed image around)
  let panX = 0;
  let panY = 0;
  let isPanning = false;
  let panPointerStartX = 0;
  let panPointerStartY = 0;
  let panOriginX = 0;
  let panOriginY = 0;

  // Touch/gesture state
  let touchStartX = 0;
  let touchStartY = 0;
  let touchDeltaX = 0;
  let touchDeltaY = 0;
  let isSwiping = false;

  // ---------------------------------------------------------------------------
  // Utilities
  // ---------------------------------------------------------------------------

  function qs(sel, ctx) {
    return (ctx || document).querySelector(sel);
  }

  function qsa(sel, ctx) {
    return Array.from((ctx || document).querySelectorAll(sel));
  }

  function el(tag, attrs, children) {
    const node = document.createElement(tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (k) {
        if (k === "className") {
          node.className = attrs[k];
        } else if (k.startsWith("on")) {
          node.addEventListener(k.slice(2).toLowerCase(), attrs[k]);
        } else {
          node.setAttribute(k, attrs[k]);
        }
      });
    }
    if (children) {
      children.forEach(function (c) {
        if (typeof c === "string") {
          node.appendChild(document.createTextNode(c));
        } else if (c) {
          node.appendChild(c);
        }
      });
    }
    return node;
  }

  function detectDarkMode() {
    const html = document.documentElement;
    return (
      html.classList.contains("quarto-dark") ||
      html.getAttribute("data-bs-theme") === "dark"
    );
  }

  function getImageSrc(item) {
    if (isDarkMode && item.darkSrc) {
      return item.darkSrc;
    }
    return item.src;
  }

  /**
   * Get the highest-resolution source for lightbox display.
   * Prefers: explicit full-src > largest srcset entry > base src.
   */
  function getFullResSrc(item) {
    if (isDarkMode && item.darkSrc) {
      return item.darkSrc;
    }
    if (item.fullSrc) {
      return item.fullSrc;
    }
    if (item.srcsetMax) {
      return item.srcsetMax;
    }
    return item.src;
  }

  /**
   * Parse a srcset string and return the URL of the widest/highest-res source.
   * Handles both width descriptors (800w) and pixel density (2x).
   */
  function parseSrcsetMax(srcset) {
    if (!srcset) return null;
    var best = null;
    var bestVal = 0;
    srcset.split(",").forEach(function (entry) {
      var parts = entry.trim().split(/\s+/);
      if (parts.length < 2) return;
      var url = parts[0];
      var descriptor = parts[1];
      var val = parseFloat(descriptor) || 0;
      if (val > bestVal) {
        bestVal = val;
        best = url;
      }
    });
    return best;
  }

  function prefersReducedMotion() {
    return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  }

  /** Parse a lightbox annotations attribute into an array, or null. */
  function parseAnnotations(raw) {
    if (window.GDAnnotate && window.GDAnnotate.parse) {
      return window.GDAnnotate.parse(raw);
    }
    if (!raw) return null;
    try {
      var a = JSON.parse(raw);
      return Array.isArray(a) && a.length ? a : null;
    } catch (e) {
      return null;
    }
  }

  // ---------------------------------------------------------------------------
  // Collect Items
  // ---------------------------------------------------------------------------

  function collectItems() {
    allItems = [];
    groups = {};

    qsa("[" + ATTR_LB + "]").forEach(function (wrapper) {
      var img = qs(".gd-lightbox-img", wrapper);
      if (!img) return;

      var item = {
        wrapper: wrapper,
        img: img,
        id: wrapper.getAttribute(ATTR_ID),
        src: img.getAttribute("src"),
        darkSrc: wrapper.getAttribute(ATTR_DARK) || null,
        fullSrc: wrapper.getAttribute(ATTR_FULL_SRC) || null,
        srcsetMax: parseSrcsetMax(img.getAttribute("srcset")),
        group: wrapper.getAttribute(ATTR_GROUP) || null,
        caption: wrapper.getAttribute(ATTR_CAPTION) || "",
        credit: wrapper.getAttribute(ATTR_CREDIT) || "",
        descPosition: wrapper.getAttribute(ATTR_DESC_POS) || "bottom",
        zoomTarget: wrapper.getAttribute(ATTR_ZOOM_TARGET) || null,
        loop: wrapper.getAttribute(ATTR_LOOP),
        autoplay: wrapper.getAttribute(ATTR_AUTOPLAY),
        alt: img.getAttribute("alt") || "",
        annotations: parseAnnotations(
          wrapper.getAttribute("data-gd-lightbox-annotations")
        ),
      };

      allItems.push(item);

      if (item.group) {
        if (!groups[item.group]) {
          groups[item.group] = [];
        }
        groups[item.group].push(item);
      }
    });
  }

  // ---------------------------------------------------------------------------
  // Overlay DOM
  // ---------------------------------------------------------------------------

  function createOverlay() {
    if (overlay) return;

    overlay = el("div", {
      className: PREFIX + "-overlay",
      role: "dialog",
      "aria-modal": "true",
      "aria-label": "Image lightbox",
      "aria-hidden": "true",
    });

    // Backdrop
    var backdrop = el("div", {
      className: PREFIX + "-backdrop",
      onClick: close,
    });
    overlay.appendChild(backdrop);

    // Content container
    var content = el("div", { className: PREFIX + "-content" });

    // Main image
    var imageWrap = el("div", { className: PREFIX + "-image-wrap" });
    var mainImg = el("img", {
      className: PREFIX + "-main-img",
      alt: "",
    });
    // Drag-to-pan when zoomed (pointer events cover mouse + touch)
    mainImg.addEventListener("pointerdown", onPanStart);
    mainImg.addEventListener("pointermove", onPanMove);
    mainImg.addEventListener("pointerup", onPanEnd);
    mainImg.addEventListener("pointercancel", onPanEnd);
    imageWrap.appendChild(mainImg);
    content.appendChild(imageWrap);

    // Caption area
    var captionEl = el("div", { className: PREFIX + "-caption" });
    var captionText = el("p", { className: PREFIX + "-caption-text" });
    var creditText = el("p", { className: PREFIX + "-credit-text" });
    captionEl.appendChild(captionText);
    captionEl.appendChild(creditText);
    content.appendChild(captionEl);

    overlay.appendChild(content);

    // Toolbar
    var toolbar = el("div", { className: PREFIX + "-toolbar" });

    // Counter (for galleries)
    var counter = el("span", { className: PREFIX + "-counter" });
    toolbar.appendChild(counter);

    // Spacer
    toolbar.appendChild(el("span", { className: PREFIX + "-toolbar-spacer" }));

    // Zoom controls: out / level / in / reset
    var zoomOutBtn = el(
      "button",
      {
        className: PREFIX + "-btn " + PREFIX + "-btn-zoom-out",
        "aria-label": "Zoom out",
        "data-tippy-content": "Zoom out",
        "data-tippy-trigger": "mouseenter",
        onClick: zoomOut,
      },
      [createZoomOutIcon()]
    );
    toolbar.appendChild(zoomOutBtn);

    var zoomLevel = el("span", {
      className: PREFIX + "-zoom-level",
      "aria-live": "polite",
    });
    toolbar.appendChild(zoomLevel);

    var zoomInBtn = el(
      "button",
      {
        className: PREFIX + "-btn " + PREFIX + "-btn-zoom-in",
        "aria-label": "Zoom in",
        "data-tippy-content": "Zoom in",
        "data-tippy-trigger": "mouseenter",
        onClick: zoomIn,
      },
      [createZoomInIcon()]
    );
    toolbar.appendChild(zoomInBtn);

    var zoomResetBtn = el(
      "button",
      {
        className: PREFIX + "-btn " + PREFIX + "-btn-zoom-reset",
        "aria-label": "Reset zoom",
        "data-tippy-content": "Reset zoom",
        "data-tippy-trigger": "mouseenter",
        onClick: zoomReset,
      },
      [createZoomResetIcon()]
    );
    toolbar.appendChild(zoomResetBtn);

    // Copy button
    var copyBtn = el(
      "button",
      {
        className: PREFIX + "-btn " + PREFIX + "-btn-copy",
        "aria-label": "Copy image to clipboard",
        // Tooltip via Great Docs' tooltips.js (tippy). Hover-only trigger so it
        // never fires on the auto-focus/focus-trap that would otherwise strand
        // the tooltip when the toolbar auto-hides. No native `title` is used.
        "data-tippy-content": "Copy image",
        "data-tippy-trigger": "mouseenter",
        onClick: handleCopy,
      },
      [createCopyIcon()]
    );
    toolbar.appendChild(copyBtn);

    // Download button
    var downloadBtn = el(
      "button",
      {
        className: PREFIX + "-btn " + PREFIX + "-btn-download",
        "aria-label": "Download image",
        "data-tippy-content": "Download image",
        "data-tippy-trigger": "mouseenter",
        onClick: handleDownload,
      },
      [createDownloadIcon()]
    );
    toolbar.appendChild(downloadBtn);

    // Copy link button
    var linkBtn = el(
      "button",
      {
        className: PREFIX + "-btn " + PREFIX + "-btn-link",
        "aria-label": "Copy link to this image",
        "data-tippy-content": "Copy link",
        "data-tippy-trigger": "mouseenter",
        onClick: handleCopyLink,
      },
      [createLinkIcon()]
    );
    toolbar.appendChild(linkBtn);

    // Close button
    var closeBtn = el(
      "button",
      {
        className: PREFIX + "-btn " + PREFIX + "-btn-close",
        "aria-label": "Close lightbox",
        "data-tippy-content": "Close (Esc)",
        "data-tippy-trigger": "mouseenter",
        onClick: close,
      },
      [createCloseIcon()]
    );
    toolbar.appendChild(closeBtn);

    overlay.appendChild(toolbar);

    // Navigation arrows
    var prevBtn = el(
      "button",
      {
        className: PREFIX + "-nav " + PREFIX + "-nav-prev",
        "aria-label": "Previous image",
        onClick: prev,
      },
      [createChevronLeft()]
    );
    var nextBtn = el(
      "button",
      {
        className: PREFIX + "-nav " + PREFIX + "-nav-next",
        "aria-label": "Next image",
        onClick: next,
      },
      [createChevronRight()]
    );
    overlay.appendChild(prevBtn);
    overlay.appendChild(nextBtn);

    // Filmstrip
    var filmstrip = el("div", { className: PREFIX + "-filmstrip" });
    overlay.appendChild(filmstrip);

    // Live region for screen reader announcements
    var liveRegion = el("div", {
      className: PREFIX + "-sr-announce",
      "aria-live": "polite",
      "aria-atomic": "true",
    });
    overlay.appendChild(liveRegion);

    document.body.appendChild(overlay);
  }

  // ---------------------------------------------------------------------------
  // SVG Icons (inline, no external deps)
  // ---------------------------------------------------------------------------

  function svgEl(paths, size) {
    size = size || 20;
    var ns = "http://www.w3.org/2000/svg";
    var svg = document.createElementNS(ns, "svg");
    svg.setAttribute("width", size);
    svg.setAttribute("height", size);
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "none");
    svg.setAttribute("stroke", "currentColor");
    svg.setAttribute("stroke-width", "2");
    svg.setAttribute("stroke-linecap", "round");
    svg.setAttribute("stroke-linejoin", "round");
    paths.forEach(function (d) {
      var path = document.createElementNS(ns, "path");
      path.setAttribute("d", d);
      svg.appendChild(path);
    });
    return svg;
  }

  function createCloseIcon() {
    return svgEl(["M18 6L6 18", "M6 6l12 12"]);
  }

  function createChevronLeft() {
    return svgEl(["M15 18l-6-6 6-6"], 24);
  }

  function createChevronRight() {
    return svgEl(["M9 18l6-6-6-6"], 24);
  }

  function createZoomInIcon() {
    return svgEl([
      "M11 4a7 7 0 100 14 7 7 0 000-14z",
      "M21 21l-4.35-4.35",
      "M11 8v6",
      "M8 11h6",
    ]);
  }

  function createZoomOutIcon() {
    return svgEl([
      "M11 4a7 7 0 100 14 7 7 0 000-14z",
      "M21 21l-4.35-4.35",
      "M8 11h6",
    ]);
  }

  function createZoomResetIcon() {
    // "Fit to view" — inward-pointing corner arrows (feather minimize-2),
    // visually distinct from the +/- magnifiers.
    return svgEl([
      "M4 14h6v6",
      "M20 10h-6V4",
      "M14 10l7-7",
      "M3 21l7-7",
    ]);
  }

  function createCopyIcon() {
    return svgEl([
      "M16 4h2a2 2 0 012 2v14a2 2 0 01-2 2H6a2 2 0 01-2-2V6a2 2 0 012-2h2",
      "M9 2h6a1 1 0 011 1v1a1 1 0 01-1 1H9a1 1 0 01-1-1V3a1 1 0 011-1z",
    ]);
  }

  function createDownloadIcon() {
    return svgEl(["M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4", "M7 10l5 5 5-5", "M12 15V3"]);
  }

  function createLinkIcon() {
    return svgEl([
      "M10 13a5 5 0 007.54.54l3-3a5 5 0 00-7.07-7.07l-1.72 1.71",
      "M14 11a5 5 0 00-7.54-.54l-3 3a5 5 0 007.07 7.07l1.71-1.71",
    ]);
  }

  // ---------------------------------------------------------------------------
  // Open / Close / Navigate
  // ---------------------------------------------------------------------------

  function open(item) {
    if (isOpen) return;

    previousFocus = document.activeElement;
    isOpen = true;
    isDarkMode = detectDarkMode();

    createOverlay();

    // Determine the gallery group
    if (item.group && groups[item.group]) {
      currentGroup = groups[item.group];
    } else {
      currentGroup = [item];
    }
    currentIndex = currentGroup.indexOf(item);
    if (currentIndex < 0) currentIndex = 0;

    // Read loop setting from the opening item (group-level attribute)
    // Default: true (wraps around). Set data-gd-lightbox-loop="false" to disable.
    var loopAttr = item.loop;
    loopEnabled = loopAttr !== "false";

    // Read autoplay interval (e.g., "3s", "2000ms", or "3000")
    autoplayInterval = parseInterval(item.autoplay);

    showSlide(currentIndex, item);

    // Show overlay with animation
    overlay.classList.add(PREFIX + "-visible");
    overlay.setAttribute("aria-hidden", "false");
    document.body.classList.add(PREFIX + "-open");

    // Origin animation: get thumbnail rect and animate from there
    if (!prefersReducedMotion()) {
      animateOpen(item);
    }

    // Update URL hash for deep linking
    if (item.id) {
      history.replaceState(null, "", "#lightbox=" + item.id);
    }

    // Focus the close button
    setTimeout(function () {
      var closeBtn = qs("." + PREFIX + "-btn-close", overlay);
      if (closeBtn) closeBtn.focus();
    }, TRANSITION_MS);

    startToolbarTimer();
    startAutoplay();
  }

  function close() {
    if (!isOpen) return;
    isOpen = false;
    stopAutoplay();
    hideToolbarTooltips();

    overlay.classList.remove(PREFIX + "-visible");
    overlay.classList.add(PREFIX + "-closing");
    overlay.setAttribute("aria-hidden", "true");
    document.body.classList.remove(PREFIX + "-open");

    // Remove hash
    if (window.location.hash.startsWith("#lightbox=")) {
      history.replaceState(null, "", window.location.pathname + window.location.search);
    }

    setTimeout(function () {
      overlay.classList.remove(PREFIX + "-closing");
      // Restore focus
      if (previousFocus) {
        previousFocus.focus();
      }
    }, TRANSITION_MS);
  }

  function next() {
    if (!currentGroup || currentGroup.length <= 1) return;
    if (!loopEnabled && currentIndex >= currentGroup.length - 1) return;
    currentIndex = (currentIndex + 1) % currentGroup.length;
    showSlide(currentIndex);
    announce("Image " + (currentIndex + 1) + " of " + currentGroup.length);
    resetAutoplay();
  }

  function prev() {
    if (!currentGroup || currentGroup.length <= 1) return;
    if (!loopEnabled && currentIndex <= 0) return;
    currentIndex = (currentIndex - 1 + currentGroup.length) % currentGroup.length;
    showSlide(currentIndex);
    announce("Image " + (currentIndex + 1) + " of " + currentGroup.length);
    resetAutoplay();
  }

  // ---------------------------------------------------------------------------
  // Autoplay
  // ---------------------------------------------------------------------------

  /** Parse an interval string like "3s", "2000ms", or "3000" → milliseconds. */
  function parseInterval(val) {
    if (!val) return 0;
    val = val.trim().toLowerCase();
    if (val.endsWith("ms")) {
      return parseInt(val, 10) || 0;
    }
    if (val.endsWith("s")) {
      return (parseFloat(val) || 0) * 1000;
    }
    // Bare number: treat as ms if >=100, otherwise as seconds
    var n = parseFloat(val);
    if (!n || n <= 0) return 0;
    return n >= 100 ? n : n * 1000;
  }

  function startAutoplay() {
    stopAutoplay();
    if (autoplayInterval <= 0 || !currentGroup || currentGroup.length <= 1) return;
    autoplayTimer = setInterval(function () {
      if (!loopEnabled && currentIndex >= currentGroup.length - 1) {
        stopAutoplay();
        return;
      }
      currentIndex = (currentIndex + 1) % currentGroup.length;
      showSlide(currentIndex);
      announce("Image " + (currentIndex + 1) + " of " + currentGroup.length);
    }, autoplayInterval);
  }

  function stopAutoplay() {
    if (autoplayTimer) {
      clearInterval(autoplayTimer);
      autoplayTimer = null;
    }
  }

  /** Reset autoplay timer (called on manual navigation to restart the interval). */
  function resetAutoplay() {
    if (autoplayInterval > 0) {
      startAutoplay();
    }
  }

  // ---------------------------------------------------------------------------
  // Zoom (toolbar-button controlled; zooms about the image center)
  // ---------------------------------------------------------------------------

  function zoomIn() { setZoom(zoomScale + ZOOM_STEP); }
  function zoomOut() { setZoom(zoomScale - ZOOM_STEP); }
  function zoomReset() { setZoom(1); }

  function setZoom(scale) {
    scale = Math.max(ZOOM_MIN, Math.min(ZOOM_MAX, Math.round(scale * 100) / 100));
    if (scale === zoomScale) {
      updateZoomUI();
      return;
    }
    zoomScale = scale;
    clampPan(); // pull pan back into bounds when zooming out
    applyZoom(false);
    announce("Zoom " + Math.round(zoomScale * 100) + " percent");
  }

  /** Reset to fit (100%). `immediate` skips the transition (slide changes). */
  function resetZoom(immediate) {
    zoomScale = 1;
    panX = 0;
    panY = 0;
    applyZoom(immediate);
  }

  /** Build the transform for the current zoom + pan (empty string at fit). */
  function zoomTransform() {
    if (zoomScale <= 1) return "";
    return "translate(" + panX + "px, " + panY + "px) scale(" + zoomScale + ")";
  }

  /** Apply just the transform (used during drag-pan; no transition juggling). */
  function applyTransform() {
    var mainImg = qs("." + PREFIX + "-main-img", overlay);
    if (mainImg) mainImg.style.transform = zoomTransform();
  }

  function applyZoom(immediate) {
    if (!overlay) return;
    if (zoomScale <= 1) {
      panX = 0;
      panY = 0;
    }
    var mainImg = qs("." + PREFIX + "-main-img", overlay);
    if (mainImg) {
      if (immediate) {
        var prev = mainImg.style.transition;
        mainImg.style.transition = "none";
        mainImg.style.transform = zoomTransform();
        mainImg.offsetHeight; // force reflow so future changes animate
        mainImg.style.transition = prev;
      } else {
        mainImg.style.transform = zoomTransform();
      }
    }
    // Cursor affordance: grab when zoomed (grabbing handled while dragging).
    overlay.classList.toggle(PREFIX + "-zoomed", zoomScale > 1);
    // Annotations are hidden while zoomed (shown again at fit level).
    var layer = qs("." + PREFIX + "-annotations", overlay);
    if (layer) {
      layer.style.display = zoomScale > 1 ? "none" : "";
    }
    updateZoomUI();
  }

  /** Clamp pan so the image always covers its fit box (no gaps inside it). */
  function clampPan() {
    var mainImg = qs("." + PREFIX + "-main-img", overlay);
    if (!mainImg || zoomScale <= 1) {
      panX = 0;
      panY = 0;
      return;
    }
    var maxX = (mainImg.offsetWidth * (zoomScale - 1)) / 2;
    var maxY = (mainImg.offsetHeight * (zoomScale - 1)) / 2;
    panX = Math.max(-maxX, Math.min(maxX, panX));
    panY = Math.max(-maxY, Math.min(maxY, panY));
  }

  // ── Drag-to-pan (pointer events: mouse + touch) ───────────────────────────

  function onPanStart(e) {
    if (zoomScale <= 1) return;
    isPanning = true;
    panPointerStartX = e.clientX;
    panPointerStartY = e.clientY;
    panOriginX = panX;
    panOriginY = panY;
    overlay.classList.add(PREFIX + "-panning");
    var mainImg = qs("." + PREFIX + "-main-img", overlay);
    if (mainImg && mainImg.setPointerCapture) {
      try { mainImg.setPointerCapture(e.pointerId); } catch (err) {}
    }
    e.preventDefault();
  }

  function onPanMove(e) {
    if (!isPanning) return;
    panX = panOriginX + (e.clientX - panPointerStartX);
    panY = panOriginY + (e.clientY - panPointerStartY);
    clampPan();
    applyTransform();
    e.preventDefault();
  }

  function onPanEnd() {
    if (!isPanning) return;
    isPanning = false;
    overlay.classList.remove(PREFIX + "-panning");
  }

  function updateZoomUI() {
    if (!overlay) return;
    var level = qs("." + PREFIX + "-zoom-level", overlay);
    if (level) level.textContent = Math.round(zoomScale * 100) + "%";
    var outBtn = qs("." + PREFIX + "-btn-zoom-out", overlay);
    var inBtn = qs("." + PREFIX + "-btn-zoom-in", overlay);
    var resetBtn = qs("." + PREFIX + "-btn-zoom-reset", overlay);
    if (outBtn) outBtn.disabled = zoomScale <= ZOOM_MIN;
    if (inBtn) inBtn.disabled = zoomScale >= ZOOM_MAX;
    if (resetBtn) resetBtn.disabled = zoomScale === 1;
  }

  function showSlide(index, originItem) {
    var item = currentGroup[index];
    if (!item) return;

    // Each slide starts at fit (100%); clear any zoom from the previous image.
    resetZoom(true);

    var mainImg = qs("." + PREFIX + "-main-img", overlay);
    var captionText = qs("." + PREFIX + "-caption-text", overlay);
    var creditText = qs("." + PREFIX + "-credit-text", overlay);
    var counter = qs("." + PREFIX + "-counter", overlay);

    // Update image source — use highest-resolution source for lightbox display
    var src = getFullResSrc(item);
    mainImg.setAttribute("src", src);
    mainImg.removeAttribute("srcset");
    mainImg.removeAttribute("sizes");
    mainImg.setAttribute("alt", item.alt);

    // Update dialog label for screen readers
    overlay.setAttribute("aria-label", item.alt || item.caption || "Image lightbox");

    // Update caption
    if (item.caption) {
      captionText.textContent = item.caption;
      captionText.style.display = "";
    } else {
      captionText.style.display = "none";
    }

    if (item.credit) {
      creditText.textContent = item.credit;
      creditText.style.display = "";
    } else {
      creditText.style.display = "none";
    }

    // Update counter
    if (currentGroup.length > 1) {
      counter.textContent = (index + 1) + " / " + currentGroup.length;
      counter.style.display = "";
    } else {
      counter.style.display = "none";
    }

    // Update navigation visibility
    var prevBtn = qs("." + PREFIX + "-nav-prev", overlay);
    var nextBtn = qs("." + PREFIX + "-nav-next", overlay);
    if (currentGroup.length <= 1) {
      prevBtn.style.display = "none";
      nextBtn.style.display = "none";
    } else {
      prevBtn.style.display = "";
      nextBtn.style.display = "";
      // Disable buttons at boundaries when loop is off
      if (!loopEnabled) {
        prevBtn.disabled = index <= 0;
        nextBtn.disabled = index >= currentGroup.length - 1;
      } else {
        prevBtn.disabled = false;
        nextBtn.disabled = false;
      }
    }

    // Update filmstrip
    updateFilmstrip();

    // Render any annotations over the enlarged image
    renderAnnotations(item);
  }

  // ---------------------------------------------------------------------------
  // Annotations (over the enlarged image)
  // ---------------------------------------------------------------------------

  /**
   * Render annotation markers for the current slide using the shared
   * GDAnnotate API, so they match the in-page annotations exactly. The markers
   * live in a layer that is sized to the displayed image by positionAnnotations.
   */
  function renderAnnotations(item) {
    var imageWrap = qs("." + PREFIX + "-image-wrap", overlay);
    if (!imageWrap) return;

    // Clear any layer from the previous slide
    var existing = qs("." + PREFIX + "-annotations", imageWrap);
    if (existing) existing.remove();

    if (!item.annotations || !window.GDAnnotate || !window.GDAnnotate.buildOverlay) {
      return;
    }

    var layer = el("div", { className: PREFIX + "-annotations" });
    layer.appendChild(window.GDAnnotate.buildOverlay(item.annotations));
    imageWrap.appendChild(layer);

    // The image src was just (re)set, so its layout box may not be final yet.
    // Position immediately (no reveal), then reveal once it has loaded and as a
    // fallback after the open animation (covers cached images).
    var mainImg = qs("." + PREFIX + "-main-img", overlay);
    positionAnnotations(false);
    if (mainImg) {
      mainImg.addEventListener("load", function () {
        positionAnnotations(true);
      }, { once: true });
    }
    setTimeout(function () { positionAnnotations(true); }, TRANSITION_MS + 60);
  }

  /** Size/position the annotation layer to exactly cover the displayed image. */
  function positionAnnotations(reveal) {
    if (!overlay) return;
    var imageWrap = qs("." + PREFIX + "-image-wrap", overlay);
    var mainImg = imageWrap && qs("." + PREFIX + "-main-img", overlay);
    var layer = imageWrap && qs("." + PREFIX + "-annotations", imageWrap);
    if (!layer || !mainImg) return;

    layer.style.left = mainImg.offsetLeft + "px";
    layer.style.top = mainImg.offsetTop + "px";
    layer.style.width = mainImg.offsetWidth + "px";
    layer.style.height = mainImg.offsetHeight + "px";
    if (reveal) layer.classList.add("visible");
  }

  // ---------------------------------------------------------------------------
  // Filmstrip
  // ---------------------------------------------------------------------------

  function updateFilmstrip() {
    var filmstrip = qs("." + PREFIX + "-filmstrip", overlay);
    if (!filmstrip) return;

    if (!currentGroup || currentGroup.length <= 1) {
      filmstrip.style.display = "none";
      overlay.classList.remove(PREFIX + "-has-filmstrip");
      return;
    }

    filmstrip.style.display = "";
    // Reserve bottom space so the caption clears the filmstrip (see CSS).
    overlay.classList.add(PREFIX + "-has-filmstrip");
    filmstrip.innerHTML = "";

    currentGroup.forEach(function (item, i) {
      var thumb = el("button", {
        className:
          PREFIX + "-filmstrip-thumb" + (i === currentIndex ? " active" : ""),
        "aria-label": "Go to image " + (i + 1),
        onClick: function () {
          currentIndex = i;
          showSlide(i);
          announce("Image " + (i + 1) + " of " + currentGroup.length);
        },
      });
      var img = el("img", {
        src: getImageSrc(item),
        alt: "",
        "aria-hidden": "true",
      });
      thumb.appendChild(img);
      filmstrip.appendChild(thumb);
    });

    // Scroll active thumb into view
    var active = qs("." + PREFIX + "-filmstrip-thumb.active", filmstrip);
    if (active) {
      active.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
    }
  }

  // ---------------------------------------------------------------------------
  // Origin-Aware Animation
  // ---------------------------------------------------------------------------

  function animateOpen(item) {
    var rect = item.img.getBoundingClientRect();
    var mainImg = qs("." + PREFIX + "-main-img", overlay);
    if (!mainImg) return;

    // Set starting transform to match thumbnail position
    var vpW = window.innerWidth;
    var vpH = window.innerHeight;

    // Calculate scale and translation
    var targetW = Math.min(vpW * 0.9, mainImg.naturalWidth || vpW * 0.8);
    var scaleX = rect.width / targetW;
    var scaleY = rect.height / (targetW * (rect.height / rect.width));

    mainImg.style.transition = "none";
    mainImg.style.transform =
      "translate(" +
      (rect.left + rect.width / 2 - vpW / 2) +
      "px, " +
      (rect.top + rect.height / 2 - vpH / 2) +
      "px) scale(" +
      scaleX +
      ")";
    mainImg.style.opacity = "0.8";

    // Force reflow
    mainImg.offsetHeight;

    // Animate to center
    mainImg.style.transition =
      "transform " + TRANSITION_MS + "ms cubic-bezier(0.4, 0, 0.2, 1), " +
      "opacity " + TRANSITION_MS + "ms ease";
    mainImg.style.transform = "translate(0, 0) scale(1)";
    mainImg.style.opacity = "1";

    // Clean up after animation. Don't clobber an active zoom if the user
    // zoomed during the open transition — only clear the open transform.
    setTimeout(function () {
      mainImg.style.transition = "";
      mainImg.style.transform = zoomScale > 1 ? "scale(" + zoomScale + ")" : "";
    }, TRANSITION_MS + 50);
  }

  // ---------------------------------------------------------------------------
  // Toolbar Actions
  // ---------------------------------------------------------------------------

  function handleCopy() {
    var mainImg = qs("." + PREFIX + "-main-img", overlay);
    if (!mainImg || !mainImg.src) return;
    var src = mainImg.src;

    // The async Clipboard API only reliably accepts image/png (SVG and other
    // types are rejected), so we rasterize whatever is displayed — including
    // SVG — to a PNG before copying. We hand a Promise to ClipboardItem so the
    // async rasterization happens inside the user-activation window, which
    // Safari requires; doing the work first and writing afterwards loses the
    // gesture and the write (and any fallback) silently fails.
    var canWriteImage =
      window.ClipboardItem && navigator.clipboard && navigator.clipboard.write;

    if (canWriteImage) {
      var item = new ClipboardItem({ "image/png": toPngBlob(src) });
      navigator.clipboard
        .write([item])
        .then(function () { showToast("Image copied"); })
        .catch(function () { fallbackCopyUrl(src); });
    } else {
      fallbackCopyUrl(src);
    }
  }

  /**
   * Rasterize an image URL (raster or SVG) to a PNG Blob via canvas.
   * Returns a Promise<Blob>; rejects if the image can't be loaded or the
   * canvas is tainted (e.g. a cross-origin source without CORS headers).
   */
  function toPngBlob(src) {
    return new Promise(function (resolve, reject) {
      var img = new Image();
      img.crossOrigin = "anonymous";
      img.onload = function () {
        var w = img.naturalWidth || img.width;
        var h = img.naturalHeight || img.height;
        if (!w || !h) {
          reject(new Error("Image has no intrinsic size"));
          return;
        }
        var canvas = document.createElement("canvas");
        canvas.width = w;
        canvas.height = h;
        try {
          canvas.getContext("2d").drawImage(img, 0, 0, w, h);
          canvas.toBlob(function (blob) {
            blob ? resolve(blob) : reject(new Error("toBlob returned null"));
          }, "image/png");
        } catch (e) {
          reject(e);
        }
      };
      img.onerror = function () { reject(new Error("Image load failed")); };
      img.src = src;
    });
  }

  /** Fallback when image copy isn't possible: copy the image URL as text. */
  function fallbackCopyUrl(src) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard
        .writeText(src)
        .then(function () { showToast("Image URL copied"); })
        .catch(function () { showToast("Copy not supported"); });
    } else {
      showToast("Copy not supported");
    }
  }

  function handleDownload() {
    var mainImg = qs("." + PREFIX + "-main-img", overlay);
    if (!mainImg || !mainImg.src) return;

    var item = currentGroup[currentIndex];
    var filename = item
      ? (item.alt || item.src.split("/").pop() || "image")
      : "image";
    // Sanitize filename
    filename = filename.replace(/[^a-zA-Z0-9_\-. ]/g, "_").slice(0, 100);

    var a = document.createElement("a");
    a.href = mainImg.src;
    a.download = filename;
    a.style.display = "none";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }

  function handleCopyLink() {
    var item = currentGroup[currentIndex];
    if (!item || !item.id) {
      showToast("No link available");
      return;
    }
    var url = window.location.origin + window.location.pathname + "#lightbox=" + item.id;
    navigator.clipboard.writeText(url).then(function () {
      showToast("Link copied");
    }).catch(function () {
      showToast("Could not copy link");
    });
  }

  function showToast(msg) {
    var existing = qs("." + PREFIX + "-toast");
    if (existing) existing.remove();

    var toast = el("div", { className: PREFIX + "-toast" }, [msg]);
    overlay.appendChild(toast);

    // Animate in
    requestAnimationFrame(function () {
      toast.classList.add("visible");
    });

    setTimeout(function () {
      toast.classList.remove("visible");
      setTimeout(function () { toast.remove(); }, 300);
    }, 2000);
  }

  // ---------------------------------------------------------------------------
  // Toolbar Auto-Hide
  // ---------------------------------------------------------------------------

  function startToolbarTimer() {
    clearTimeout(toolbarTimer);
    showToolbar();
    toolbarTimer = setTimeout(hideToolbar, TOOLBAR_HIDE_MS);
  }

  function showToolbar() {
    var tb = qs("." + PREFIX + "-toolbar", overlay);
    if (tb) tb.classList.remove("hidden");
  }

  function hideToolbar() {
    var tb = qs("." + PREFIX + "-toolbar", overlay);
    if (tb) tb.classList.add("hidden");
    // The toolbar hides via opacity (it stays in the DOM), so a tippy tooltip
    // attached to a button could linger visibly. Dismiss any active ones.
    hideToolbarTooltips();
  }

  /** Hide any tippy tooltips currently attached to toolbar buttons. */
  function hideToolbarTooltips() {
    if (!overlay) return;
    qsa("." + PREFIX + "-btn", overlay).forEach(function (btn) {
      if (btn._tippy) btn._tippy.hide();
    });
  }

  // ---------------------------------------------------------------------------
  // Keyboard Navigation
  // ---------------------------------------------------------------------------

  function handleKeydown(e) {
    if (!isOpen) return;

    switch (e.key) {
      case "Escape":
        close();
        e.preventDefault();
        break;
      case "ArrowRight":
        next();
        e.preventDefault();
        break;
      case "ArrowLeft":
        prev();
        e.preventDefault();
        break;
      case "Tab":
        trapFocus(e);
        break;
      case "+":
      case "=": // unshifted "+" key
        zoomIn();
        e.preventDefault();
        break;
      case "-":
      case "_":
        zoomOut();
        e.preventDefault();
        break;
      case "0":
        zoomReset();
        e.preventDefault();
        break;
    }
  }

  function trapFocus(e) {
    var focusable = qsa(
      'button:not([disabled]), [tabindex]:not([tabindex="-1"])',
      overlay
    );
    if (focusable.length === 0) return;

    var first = focusable[0];
    var last = focusable[focusable.length - 1];

    if (e.shiftKey) {
      if (document.activeElement === first) {
        last.focus();
        e.preventDefault();
      }
    } else {
      if (document.activeElement === last) {
        first.focus();
        e.preventDefault();
      }
    }
  }

  // ---------------------------------------------------------------------------
  // Touch / Swipe
  // ---------------------------------------------------------------------------

  function handleTouchStart(e) {
    if (!isOpen) return;
    // When zoomed, touch drives pan (pointer events), not swipe-nav/close.
    if (zoomScale > 1) return;
    var touch = e.touches[0];
    touchStartX = touch.clientX;
    touchStartY = touch.clientY;
    touchDeltaX = 0;
    touchDeltaY = 0;
    isSwiping = false;
  }

  function handleTouchMove(e) {
    if (!isOpen) return;
    if (zoomScale > 1) return;
    var touch = e.touches[0];
    touchDeltaX = touch.clientX - touchStartX;
    touchDeltaY = touch.clientY - touchStartY;

    // Determine if horizontal or vertical swipe
    if (!isSwiping && (Math.abs(touchDeltaX) > 10 || Math.abs(touchDeltaY) > 10)) {
      isSwiping = true;
    }

    // Prevent page scroll while swiping in lightbox
    if (isSwiping) {
      e.preventDefault();
    }
  }

  function handleTouchEnd() {
    if (!isOpen || !isSwiping) return;

    var threshold = 50;

    // Horizontal swipe → gallery navigation
    if (Math.abs(touchDeltaX) > Math.abs(touchDeltaY)) {
      if (touchDeltaX > threshold) {
        prev();
      } else if (touchDeltaX < -threshold) {
        next();
      }
    } else {
      // Vertical swipe down → close
      if (touchDeltaY > threshold) {
        close();
      }
    }

    isSwiping = false;
  }

  // ---------------------------------------------------------------------------
  // Dark Mode Observer
  // ---------------------------------------------------------------------------

  function setupDarkModeObserver() {
    var html = document.documentElement;
    var observer = new MutationObserver(function (mutations) {
      var newDarkMode = detectDarkMode();
      if (newDarkMode !== isDarkMode) {
        isDarkMode = newDarkMode;
        if (isOpen) {
          // Swap image source
          showSlide(currentIndex);
        }
        // Also swap thumbnails on the page
        swapThumbnails();
      }
    });
    observer.observe(html, {
      attributes: true,
      attributeFilter: ["class", "data-bs-theme"],
    });
  }

  function swapThumbnails() {
    allItems.forEach(function (item) {
      if (item.darkSrc) {
        item.img.setAttribute("src", getImageSrc(item));
      }
    });
  }

  // ---------------------------------------------------------------------------
  // Screen Reader Announcements
  // ---------------------------------------------------------------------------

  function announce(msg) {
    var region = qs("." + PREFIX + "-sr-announce", overlay);
    if (region) {
      region.textContent = msg;
    }
  }

  // ---------------------------------------------------------------------------
  // Deep Linking
  // ---------------------------------------------------------------------------

  function checkDeepLink() {
    var hash = window.location.hash;
    if (!hash.startsWith("#lightbox=")) return;

    var id = hash.slice("#lightbox=".length);
    var item = allItems.find(function (it) {
      return it.id === id;
    });
    if (item) {
      // Delay to allow page to render
      setTimeout(function () { open(item); }, 100);
    }
  }

  // ---------------------------------------------------------------------------
  // Event Binding
  // ---------------------------------------------------------------------------

  function bindClick(item) {
    // Click on wrapper or expand button opens lightbox
    item.wrapper.addEventListener("click", function (e) {
      e.preventDefault();
      e.stopPropagation();
      open(item);
    });

    // Make wrapper keyboard-accessible
    item.wrapper.setAttribute("tabindex", "0");
    item.wrapper.setAttribute("role", "button");
    item.wrapper.setAttribute("aria-label", "View image: " + (item.alt || "image"));
    item.wrapper.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        open(item);
      }
    });
  }

  // ---------------------------------------------------------------------------
  // Init
  // ---------------------------------------------------------------------------

  function init() {
    isDarkMode = detectDarkMode();
    collectItems();

    if (allItems.length === 0) return;

    allItems.forEach(bindClick);
    setupDarkModeObserver();

    // Global keyboard handler
    document.addEventListener("keydown", handleKeydown);

    // Touch handlers on overlay (after it's created)
    document.addEventListener("touchstart", function (e) {
      if (isOpen) handleTouchStart(e);
    }, { passive: true });
    document.addEventListener("touchmove", function (e) {
      if (isOpen) handleTouchMove(e);
    }, { passive: false });
    document.addEventListener("touchend", function (e) {
      if (isOpen) handleTouchEnd(e);
    }, { passive: true });

    // Mouse movement re-shows toolbar
    document.addEventListener("mousemove", function () {
      if (isOpen) startToolbarTimer();
    });

    // Keep annotation markers aligned to the image when the viewport resizes
    window.addEventListener("resize", function () {
      if (!isOpen) return;
      positionAnnotations(false);
      if (zoomScale > 1) {
        clampPan();
        applyTransform();
      }
    });

    // Deep link check
    checkDeepLink();
    window.addEventListener("hashchange", checkDeepLink);
  }

  // Run on DOM ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

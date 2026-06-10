/**
 * Custom Tooltips for Great Docs
 *
 * Replaces native browser title tooltips with styled Tippy.js tooltips.
 *
 * Features:
 * - Instant appearance (no 400ms delay)
 * - Consistent styling across all browsers
 * - Dark mode support
 * - Smart positioning (avoids viewport edges)
 * - Material Filling Effect animation
 * - Converts existing title attributes site-wide
 *
 * NOTE: Quarto already bundles Popper.js and Tippy.js, so we use those instead
 * of loading from CDN. Falls back to CDN if they're not available.
 */

(function () {
  "use strict";

  // Configuration
  var CONFIG = {
    // Tippy.js CDN URLs (fallback if not bundled by Quarto)
    popperUrl: "https://unpkg.com/@popperjs/core@2/dist/umd/popper.min.js",
    tippyUrl: "https://unpkg.com/tippy.js@6/dist/tippy-bundle.umd.min.js",

    // Default tooltip options
    defaultOptions: {
      animation: "shift-away",
      duration: [200, 150],
      delay: [0, 0], // Instant appearance
      arrow: true,
      placement: "top",
      theme: "gd-material",
      maxWidth: 300,
      touch: ["hold", 500], // Long press on touch devices
      // Smart positioning — flip if not enough space
      popperOptions: {
        modifiers: [
          {
            name: "flip",
            options: {
              fallbackPlacements: ["bottom", "right", "left"],
            },
          },
          {
            name: "preventOverflow",
            options: {
              boundary: "viewport",
              padding: 8,
            },
          },
        ],
      },
    },

    // Selectors for elements to skip (already have custom tooltips)
    skipSelectors: [
      "[data-tippy-content]", // Already has Tippy
      ".tippy-box", // Tippy element itself
      ".gd-tooltip-skip", // Explicit skip class
    ],
  };

  // Track loaded state
  var tippyReady = false;
  var tippyInstance = null;

  /**
   * Load an external script dynamically.
   * @param {string} url - Script URL
   * @returns {Promise} - Resolves when loaded
   */
  function loadScript(url) {
    return new Promise(function (resolve, reject) {
      // Check if already loaded
      var existing = document.querySelector('script[src="' + url + '"]');
      if (existing) {
        resolve();
        return;
      }

      var script = document.createElement("script");
      script.src = url;
      script.async = true;
      script.onload = resolve;
      script.onerror = function () {
        reject(new Error("Failed to load script: " + url));
      };
      document.head.appendChild(script);
    });
  }

  /**
   * Load Tippy.js and its dependencies.
   * Quarto bundles Popper and Tippy, so check for them first.
   * @returns {Promise} - Resolves when Tippy is ready
   */
  function loadTippy() {
    // If Tippy is already available (Quarto bundles it), use it directly
    if (window.tippy) {
      tippyReady = true;
      return Promise.resolve();
    }

    // Quarto might have loaded tippy but not exposed it globally yet
    // Wait a tick and check again
    return new Promise(function (resolve) {
      setTimeout(function () {
        if (window.tippy) {
          tippyReady = true;
          resolve();
          return;
        }

        // Fall back to CDN loading if Quarto's tippy isn't available
        loadScript(CONFIG.popperUrl)
          .then(function () {
            return loadScript(CONFIG.tippyUrl);
          })
          .then(function () {
            tippyReady = true;
            resolve();
          })
          .catch(function (err) {
            console.warn("Failed to load Tippy.js from CDN:", err);
            resolve(); // Continue without tooltips
          });
      }, 50);
    });
  }

  /**
   * Determine if dark mode is active.
   * @returns {boolean}
   */
  function isDarkMode() {
    return (
      document.documentElement.classList.contains("quarto-dark") ||
      document.body.classList.contains("quarto-dark") ||
      document.documentElement.getAttribute("data-bs-theme") === "dark"
    );
  }

  /**
   * Get theme name based on current mode.
   * @returns {string}
   */
  function getThemeName() {
    return isDarkMode() ? "gd-material-dark" : "gd-material";
  }

  /**
   * Convert title attributes to data-tippy-content.
   * This prevents native tooltips from appearing.
   */
  function convertTitleAttributes() {
    var skipSelector = CONFIG.skipSelectors.join(", ");

    // Find all elements with title attributes
    var elements = document.querySelectorAll("[title]");

    elements.forEach(function (el) {
      // Skip if matches any skip selector
      if (skipSelector && el.matches(skipSelector)) {
        return;
      }

      var title = el.getAttribute("title");
      if (title && title.trim()) {
        // Store the title as data-tippy-content
        el.setAttribute("data-tippy-content", title);
        // Remove the native title to prevent browser tooltip
        el.removeAttribute("title");
      }
    });
  }

  /**
   * Initialize or reinitialize all tooltips.
   */
  function initTooltips() {
    if (!window.tippy) {
      console.warn("Tippy.js not loaded");
      return;
    }

    // First convert any title attributes
    convertTitleAttributes();

    // Find all elements with data-tippy-content
    var elements = document.querySelectorAll("[data-tippy-content]");

    if (elements.length === 0) {
      return;
    }

    // Create options with current theme
    var options = Object.assign({}, CONFIG.defaultOptions, {
      theme: getThemeName(),
      allowHTML: true,
      // Read content from data-tippy-content so HTML tags are rendered
      content: function (el) {
        return el.getAttribute("data-tippy-content") || "";
      },
      // Material filling effect via CSS
      onMount: function (instance) {
        instance.popper.classList.add("gd-tooltip-mounted");
      },
      onHidden: function (instance) {
        instance.popper.classList.remove("gd-tooltip-mounted");
      },
    });

    // Destroy existing instances to avoid duplicates
    elements.forEach(function (el) {
      if (el._tippy) {
        el._tippy.destroy();
      }
    });

    // Initialize Tippy on all elements
    tippyInstance = window.tippy(elements, options);
  }

  /**
   * Update tooltip themes when dark mode changes.
   */
  function updateTooltipThemes() {
    if (!tippyInstance) return;

    var newTheme = getThemeName();

    // Update all active tippy instances
    var instances = Array.isArray(tippyInstance) ? tippyInstance : [tippyInstance];
    instances.forEach(function (instance) {
      if (instance && instance.setProps) {
        instance.setProps({ theme: newTheme });
      }
    });
  }

  /**
   * Observe for dynamically added elements.
   */
  function observeNewElements() {
    if (!window.MutationObserver) return;

    var observer = new MutationObserver(function (mutations) {
      var needsReinit = false;

      mutations.forEach(function (mutation) {
        // Check added nodes for title or data-tippy-content attributes
        mutation.addedNodes.forEach(function (node) {
          if (node.nodeType === Node.ELEMENT_NODE) {
            if (node.hasAttribute && (node.hasAttribute("title") || node.hasAttribute("data-tippy-content"))) {
              needsReinit = true;
            }
            // Also check descendants
            if (node.querySelectorAll) {
              var withTitle = node.querySelectorAll("[title], [data-tippy-content]");
              if (withTitle.length > 0) {
                needsReinit = true;
              }
            }
          }
        });

        // Check for attribute changes (title or data-tippy-content being set)
        if (mutation.type === "attributes" &&
            (mutation.attributeName === "title" || mutation.attributeName === "data-tippy-content")) {
          needsReinit = true;
        }
      });

      if (needsReinit) {
        // Debounce re-initialization
        clearTimeout(observeNewElements.timeout);
        observeNewElements.timeout = setTimeout(initTooltips, 100);
      }
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ["title", "data-tippy-content"],
    });
  }

  /**
   * Observe dark mode changes.
   */
  function observeDarkMode() {
    if (!window.MutationObserver) return;

    var observer = new MutationObserver(function (mutations) {
      mutations.forEach(function (mutation) {
        if (mutation.attributeName === "class" || mutation.attributeName === "data-bs-theme") {
          updateTooltipThemes();
        }
      });
    });

    // Observe both html and body for class changes
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["class", "data-bs-theme"],
    });
    observer.observe(document.body, {
      attributes: true,
      attributeFilter: ["class"],
    });
  }

  /**
   * Main initialization function.
   */
  function init() {
    loadTippy()
      .then(function () {
        initTooltips();
        observeNewElements();
        observeDarkMode();
      })
      .catch(function (err) {
        console.error("Failed to initialize tooltips:", err);
      });
  }

  // Initialize when DOM is ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  // Expose API for programmatic use
  window.GDTooltips = {
    init: init,
    refresh: initTooltips,
    updateTheme: updateTooltipThemes,
  };
})();

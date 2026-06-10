/**
 * Great Docs — Collapsible Details
 *
 * Provides smooth expand/collapse animation and accordion-group behavior
 * for <details class="gd-details"> elements produced by the {{< details >}}
 * shortcode.
 *
 * Features:
 * - Smooth height animation on toggle (respects prefers-reduced-motion)
 * - Accordion groups: elements sharing the same data-gd-group attribute
 *   close siblings when one opens
 * - Works with nested details elements
 */
(function () {
  "use strict";

  // ── Feature detection ──────────────────────────────────────────────
  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  // ── Animation helpers ──────────────────────────────────────────────

  /**
   * Animate the opening of a <details> element.
   * @param {HTMLDetailsElement} el
   */
  function animateOpen(el) {
    var body = el.querySelector(".gd-details-body");
    if (!body) return;

    // Force the element open so we can measure the target height
    el.open = true;

    // Measure current (collapsed) and target (expanded) heights
    var summary = el.querySelector("summary");
    var startHeight = summary ? summary.offsetHeight : 0;
    var endHeight = el.scrollHeight;

    // If reduced motion is preferred, skip animation
    if (reducedMotion.matches) {
      el.style.height = "";
      el.style.overflow = "";
      el.classList.add("gd-details--open");
      return;
    }

    el.style.height = startHeight + "px";
    el.style.overflow = "hidden";

    // Force reflow
    void el.offsetHeight;

    el.classList.add("gd-details--animating");
    el.style.height = endHeight + "px";

    function onEnd() {
      el.removeEventListener("transitionend", onEnd);
      el.classList.remove("gd-details--animating");
      el.classList.add("gd-details--open");
      el.style.height = "";
      el.style.overflow = "";
    }
    el.addEventListener("transitionend", onEnd);
  }

  /**
   * Animate the closing of a <details> element.
   * @param {HTMLDetailsElement} el
   */
  function animateClose(el) {
    var body = el.querySelector(".gd-details-body");
    if (!body) return;

    // If reduced motion is preferred, just close immediately
    if (reducedMotion.matches) {
      el.classList.remove("gd-details--open");
      el.open = false;
      return;
    }

    var startHeight = el.scrollHeight;
    var summary = el.querySelector("summary");
    var endHeight = summary ? summary.offsetHeight : 0;

    el.style.height = startHeight + "px";
    el.style.overflow = "hidden";

    // Force reflow
    void el.offsetHeight;

    el.classList.add("gd-details--animating");
    el.classList.remove("gd-details--open");
    el.style.height = endHeight + "px";

    function onEnd() {
      el.removeEventListener("transitionend", onEnd);
      el.classList.remove("gd-details--animating");
      el.open = false;
      el.style.height = "";
      el.style.overflow = "";
    }
    el.addEventListener("transitionend", onEnd);
  }

  // ── Accordion logic ────────────────────────────────────────────────

  /**
   * Close all other details in the same accordion group.
   * @param {HTMLDetailsElement} current - The details element being opened
   * @param {string} group - The accordion group name
   */
  function closeGroupSiblings(current, group) {
    var siblings = document.querySelectorAll(
      'details.gd-details[data-gd-group="' + group + '"]'
    );
    for (var i = 0; i < siblings.length; i++) {
      if (siblings[i] !== current && siblings[i].open) {
        animateClose(siblings[i]);
      }
    }
  }

  // ── Event binding ──────────────────────────────────────────────────

  /**
   * Attach click handlers to all .gd-details elements.
   */
  function initDetails() {
    var elements = document.querySelectorAll("details.gd-details");

    for (var i = 0; i < elements.length; i++) {
      (function (el) {
        // Mark initially-open elements
        if (el.open) {
          el.classList.add("gd-details--open");
        }

        var summary = el.querySelector("summary");
        if (!summary) return;

        summary.addEventListener("click", function (e) {
          e.preventDefault();

          if (el.open) {
            // Currently open → close it
            animateClose(el);
          } else {
            // Currently closed → open it
            var group = el.getAttribute("data-gd-group");
            if (group) {
              closeGroupSiblings(el, group);
            }
            animateOpen(el);
          }
        });
      })(elements[i]);
    }
  }

  // ── Gleam animation (JS-driven) ─────────────────────────────────────

  /**
   * Animate the --gd-gleam-angle custom property via requestAnimationFrame.
   * This avoids reliance on @property (inconsistent cross-browser).
   */
  function initGleam() {
    var gleamEls = document.querySelectorAll(".gd-details--gleam");
    if (!gleamEls.length) return;
    if (reducedMotion.matches) return;

    var duration = 6000; // ms for a full 360° sweep
    var start = null;

    function tick(timestamp) {
      if (!start) start = timestamp;
      var elapsed = (timestamp - start) % duration;
      var angle = (elapsed / duration) * 360;
      var value = angle + "deg";

      for (var i = 0; i < gleamEls.length; i++) {
        gleamEls[i].style.setProperty("--gd-gleam-angle", value);
      }
      requestAnimationFrame(tick);
    }

    requestAnimationFrame(tick);
  }

  // ── Initialize ─────────────────────────────────────────────────────
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      initDetails();
      initGleam();
    });
  } else {
    initDetails();
    initGleam();
  }
})();

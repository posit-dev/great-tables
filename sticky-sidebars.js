/**
 * Sticky sidebars for Great Docs
 *
 * Keeps the sidebars below the navbar, which stays visible on desktop, and
 * keeps them stuck in place while the footer scrolls into view.
 */

/**
 * Sticky navbar on desktop — keep sidebars positioned below the header.
 *
 * Quarto's headroom.js hides the navbar on scroll-down and shifts sidebars
 * (top: 0) to fill the vacated space. Our CSS keeps the navbar visible on
 * desktop (>= 992px), so we must also prevent the sidebar repositioning.
 * Listens for the quarto-hrChanged event that fires after every headroom
 * pin/unpin and re-applies the correct sidebar top/maxHeight.
 */
(function () {
  "use strict";

  var mql = window.matchMedia("(min-width: 992px)");

  function fixSidebars() {
    if (!mql.matches) return;

    var header = document.querySelector("#quarto-header");
    if (!header) return;
    var h = header.offsetHeight;

    var els = document.querySelectorAll(".sidebar, .headroom-target");
    els.forEach(function (el) {
      // Skip the floating sidebar — sidebar-float.js manages its own bounds
      if (el.classList.contains('gd-sidebar-float')) return;
      el.style.top = h + "px";
      el.style.maxHeight = "calc(100vh - " + h + "px)";
    });
  }

  window.addEventListener("quarto-hrChanged", fixSidebars);
  mql.addEventListener("change", fixSidebars);
})();

/**
 * Move the footer inside #quarto-content on desktop so sticky sidebars
 * remain pinned through the footer region.
 *
 * Sticky positioning is bounded by the parent container. Because the footer
 * lives outside #quarto-content, the sidebars unstick when the container
 * ends. Moving the footer inside extends the grid rows, keeping the
 * sidebars' sticky context active through the footer.
 */
(function () {
  "use strict";

  var mql = window.matchMedia("(min-width: 992px)");
  var moved = false;
  var originalParent = null;
  var originalNext = null;

  function update() {
    var content = document.getElementById("quarto-content");
    var footer = document.querySelector("footer.footer");
    if (!content || !footer) return;

    if (mql.matches && !moved) {
      // Remember original position so we can restore on mobile
      originalParent = footer.parentNode;
      originalNext = footer.nextSibling;
      // Move footer inside the grid container, spanning all columns
      footer.style.gridColumn = "1 / -1";
      content.appendChild(footer);
      moved = true;
    } else if (!mql.matches && moved) {
      // Restore footer to its original position for mobile
      footer.style.gridColumn = "";
      if (originalNext) {
        originalParent.insertBefore(footer, originalNext);
      } else {
        originalParent.appendChild(footer);
      }
      moved = false;
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", update);
  } else {
    update();
  }
  mql.addEventListener("change", update);
})();

/**
 * GD Lightbox Compare — Before/After Image Comparison Slider
 *
 * Renders a draggable divider between two overlaid images. Supports:
 * - Mouse and touch drag
 * - Keyboard control (arrow keys move divider in 5% increments)
 * - Horizontal (default) and vertical split
 * - Customizable labels
 * - Works inline and can be opened in the main lightbox
 *
 * No dependencies. ~3KB minified+gzipped target.
 */
(function () {
  "use strict";

  var PREFIX = "gd-compare";
  var STEP = 5; // Keyboard step in percent

  function initAll() {
    var containers = document.querySelectorAll("." + PREFIX);
    for (var i = 0; i < containers.length; i++) {
      initSlider(containers[i]);
    }
  }

  function initSlider(container) {
    if (container.dataset.gdCompareInit) return;
    container.dataset.gdCompareInit = "true";

    var direction = container.dataset.direction || "horizontal";
    var startPos = parseFloat(container.dataset.startPosition) || 50;
    var labelBefore = container.dataset.labelBefore || "Before";
    var labelAfter = container.dataset.labelAfter || "After";

    // Get the two images
    var images = container.querySelectorAll("img");
    if (images.length < 2) return;

    var beforeImg = images[0];
    var afterImg = images[1];

    // Build the comparison structure
    container.innerHTML = "";
    container.classList.add(PREFIX + "--" + direction);
    container.setAttribute("role", "slider");
    container.setAttribute("aria-label", "Image comparison slider");
    container.setAttribute("aria-valuemin", "0");
    container.setAttribute("aria-valuemax", "100");
    container.setAttribute("aria-valuenow", String(Math.round(startPos)));
    container.setAttribute("aria-valuetext", Math.round(startPos) + "% " + labelBefore);
    container.setAttribute("tabindex", "0");

    // Before layer (clipped)
    var beforeLayer = document.createElement("div");
    beforeLayer.className = PREFIX + "__before";
    beforeLayer.appendChild(beforeImg.cloneNode(true));
    container.appendChild(beforeLayer);

    // After layer (full, behind)
    var afterLayer = document.createElement("div");
    afterLayer.className = PREFIX + "__after";
    afterLayer.appendChild(afterImg.cloneNode(true));
    container.appendChild(afterLayer);

    // Divider
    var divider = document.createElement("div");
    divider.className = PREFIX + "__divider";
    var handle = document.createElement("div");
    handle.className = PREFIX + "__handle";
    handle.innerHTML =
      '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
      'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
      '<polyline points="8 4 4 8 8 12"></polyline>' +
      '<polyline points="16 4 20 8 16 12"></polyline>' +
      '</svg>';
    divider.appendChild(handle);
    container.appendChild(divider);

    // Labels
    var bLabel = document.createElement("span");
    bLabel.className = PREFIX + "__label " + PREFIX + "__label--before";
    bLabel.textContent = labelBefore;
    container.appendChild(bLabel);

    var aLabel = document.createElement("span");
    aLabel.className = PREFIX + "__label " + PREFIX + "__label--after";
    aLabel.textContent = labelAfter;
    container.appendChild(aLabel);

    // State
    var position = startPos;
    var isDragging = false;

    function setPosition(pct) {
      pct = Math.max(0, Math.min(100, pct));
      position = pct;

      if (direction === "vertical") {
        beforeLayer.style.clipPath = "inset(0 0 " + (100 - pct) + "% 0)";
        divider.style.top = pct + "%";
        divider.style.left = "";
      } else {
        beforeLayer.style.clipPath = "inset(0 " + (100 - pct) + "% 0 0)";
        divider.style.left = pct + "%";
        divider.style.top = "";
      }

      container.setAttribute("aria-valuenow", String(Math.round(pct)));
      container.setAttribute(
        "aria-valuetext",
        Math.round(pct) + "% " + labelBefore
      );
    }

    function getPosition(e) {
      var rect = container.getBoundingClientRect();
      var clientX, clientY;

      if (e.touches && e.touches.length > 0) {
        clientX = e.touches[0].clientX;
        clientY = e.touches[0].clientY;
      } else {
        clientX = e.clientX;
        clientY = e.clientY;
      }

      if (direction === "vertical") {
        return ((clientY - rect.top) / rect.height) * 100;
      }
      return ((clientX - rect.left) / rect.width) * 100;
    }

    // Pointer events
    function onPointerDown(e) {
      isDragging = true;
      setPosition(getPosition(e));
      e.preventDefault();
      container.classList.add(PREFIX + "--active");
    }

    function onPointerMove(e) {
      if (!isDragging) return;
      setPosition(getPosition(e));
      e.preventDefault();
    }

    function onPointerUp() {
      if (!isDragging) return;
      isDragging = false;
      container.classList.remove(PREFIX + "--active");
    }

    // Mouse
    container.addEventListener("mousedown", onPointerDown);
    document.addEventListener("mousemove", onPointerMove);
    document.addEventListener("mouseup", onPointerUp);

    // Touch
    container.addEventListener("touchstart", onPointerDown, { passive: false });
    document.addEventListener("touchmove", function (e) {
      if (isDragging) onPointerMove(e);
    }, { passive: false });
    document.addEventListener("touchend", onPointerUp);

    // Keyboard
    container.addEventListener("keydown", function (e) {
      var moved = false;
      switch (e.key) {
        case "ArrowLeft":
        case "ArrowUp":
          setPosition(position - STEP);
          moved = true;
          break;
        case "ArrowRight":
        case "ArrowDown":
          setPosition(position + STEP);
          moved = true;
          break;
        case "Home":
          setPosition(0);
          moved = true;
          break;
        case "End":
          setPosition(100);
          moved = true;
          break;
      }
      if (moved) e.preventDefault();
    });

    // Set initial position
    setPosition(startPos);
  }

  // Init on DOM ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAll);
  } else {
    initAll();
  }
})();

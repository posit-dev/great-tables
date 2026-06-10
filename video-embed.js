/**
 * Video embedding enhancements for Great Docs
 *
 * Improves performance and UX for embedded videos:
 *  - YouTube: uses the standard YouTube embedded player with native controls
 *  - Vimeo / other service iframes: IntersectionObserver lazy loading
 *  - Local <video> elements: sets preload="metadata" for faster page loads
 */
(function () {
  "use strict";

  /**
   * Lazy-load non-YouTube iframes (Vimeo, Loom, etc.) via IntersectionObserver.
   * The src is deferred until the iframe scrolls near the viewport.
   */
  function lazyLoadIframes() {
    if (!("IntersectionObserver" in window)) return;

    var iframes = document.querySelectorAll(
      '.quarto-video iframe:not([src*="youtube.com"]):not([src*="youtube-nocookie.com"])'
    );

    var observer = new IntersectionObserver(
      function (entries) {
        for (var j = 0; j < entries.length; j++) {
          if (entries[j].isIntersecting) {
            var el = entries[j].target;
            if (el.dataset.gdSrc) {
              el.src = el.dataset.gdSrc;
              delete el.dataset.gdSrc;
            }
            observer.unobserve(el);
          }
        }
      },
      { rootMargin: "300px" }
    );

    for (var i = 0; i < iframes.length; i++) {
      var iframe = iframes[i];
      if (!iframe.src) continue;
      iframe.dataset.gdSrc = iframe.src;
      iframe.removeAttribute("src");
      observer.observe(iframe);
    }
  }

  /**
   * Set preload="metadata" on <video> elements that have no explicit preload,
   * so browsers download only enough to show the first frame and duration.
   */
  function enhanceVideoElements() {
    var videos = document.querySelectorAll("video");
    for (var i = 0; i < videos.length; i++) {
      if (!videos[i].hasAttribute("preload")) {
        videos[i].setAttribute("preload", "metadata");
      }
    }
  }

  // --- Entry point ---
  function init() {
    lazyLoadIframes();
    enhanceVideoElements();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

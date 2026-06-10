/**
 * Back-to-Top Button for Great Docs
 *
 * Features:
 * - Floating button that appears after scrolling down
 * - Smooth scroll animation to page top
 * - Respects reduced-motion preferences
 * - Positioned to avoid collision with prev/next page navigation
 * - Dark mode aware
 * - Keyboard accessible
 */

(function() {
    'use strict';

    // How far (in pixels) the user must scroll before the button appears
    var SCROLL_THRESHOLD = 300;

    /**
     * Check if the user prefers reduced motion
     */
    function prefersReducedMotion() {
        return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    }

    /**
     * Create the back-to-top button element
     */
    function createButton() {
        var btn = document.createElement('button');
        btn.className = 'gd-back-to-top';
        btn.setAttribute('aria-label', 'Back to top');
        btn.setAttribute('title', 'Back to top');
        btn.setAttribute('type', 'button');

        // Chevron-up SVG icon (Lucide-style, 24×24)
        btn.innerHTML =
            '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" ' +
            'fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" ' +
            'stroke-linejoin="round" aria-hidden="true">' +
            '<polyline points="18 15 12 9 6 15"></polyline>' +
            '</svg>';

        return btn;
    }

    /**
     * Scroll to the top of the page
     */
    function scrollToTop() {
        if (prefersReducedMotion()) {
            // Instant scroll for reduced-motion preference
            window.scrollTo(0, 0);
        } else {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    }

    /**
     * Update button visibility based on scroll position
     */
    function updateVisibility(btn) {
        if (window.scrollY > SCROLL_THRESHOLD) {
            btn.classList.add('gd-back-to-top-visible');
        } else {
            btn.classList.remove('gd-back-to-top-visible');
        }
    }

    /**
     * Check if prev/next page navigation is near the viewport bottom
     * and adjust button position to avoid overlap
     */
    function adjustForPageNav(btn) {
        var pageNav = document.querySelector('.page-navigation');
        if (!pageNav) return;

        var navRect = pageNav.getBoundingClientRect();
        var viewportHeight = window.innerHeight;

        // If the page nav is visible in the viewport, shift the button up
        if (navRect.top < viewportHeight && navRect.bottom > 0) {
            var overlap = viewportHeight - navRect.top + 16; // 16px extra gap
            btn.style.bottom = Math.max(overlap, 32) + 'px';
        } else {
            btn.style.bottom = '';
        }
    }

    /**
     * Initialize the back-to-top button
     */
    function init() {
        var btn = createButton();
        document.body.appendChild(btn);

        btn.addEventListener('click', scrollToTop);

        // Throttle scroll handler for performance
        var ticking = false;
        window.addEventListener('scroll', function() {
            if (!ticking) {
                window.requestAnimationFrame(function() {
                    updateVisibility(btn);
                    adjustForPageNav(btn);
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });

        // Initial state
        updateVisibility(btn);
    }

    // DOM ready check
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();

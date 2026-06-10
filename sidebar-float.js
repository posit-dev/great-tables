/**
 * Floating Sidebar Navigation for Great Docs
 *
 * Transforms the default Quarto left sidebar on desktop (>= 992px) into a
 * floating, pinned navigation panel with:
 *   - Independent scroll containment (no bleed to page body)
 *   - Dynamic top/bottom bounds that react to navbar and footer
 *   - A sticky "Pages" header label
 *   - Gradient + arrow scroll affordances (top & bottom)
 *   - Auto-scroll to the active page on load
 *
 * On tablet/mobile (< 992px) this script is a no-op — the overlay modal
 * approach handles the sidebar there.
 */
(function () {
    'use strict';

    // ── Constants ──────────────────────────────────────────────
    var GAP = 12;           // breathing room (px) between sidebar and navbar/footer
    var FOOTER_BUFFER = 7;  // extra px buffer before footer encroaches


    // ── Media query guard ──────────────────────────────────────
    var mql = window.matchMedia('(min-width: 992px)');

    // ── State ──────────────────────────────────────────────────
    var sidebar = null;         // #quarto-sidebar
    var menuContainer = null;   // .sidebar-menu-container
    var floatBody = null;       // .gd-sidebar-float-body (scrollable wrapper)
    var resizeObs = null;       // ResizeObserver instance
    var rafId = null;
    var initialised = false;

    // ── Helpers ────────────────────────────────────────────────
    function getHeader() {
        return document.getElementById('quarto-header');
    }

    function getFooter() {
        return document.querySelector('footer.footer');
    }

    // ── Build the float structure ──────────────────────────────
    function buildFloat() {
        sidebar = document.getElementById('quarto-sidebar');
        if (!sidebar) return false;
        menuContainer = sidebar.querySelector('.sidebar-menu-container');
        if (!menuContainer) return false;

        // Scrollable body wrapper
        floatBody = document.createElement('div');
        floatBody.className = 'gd-sidebar-float-body';

        // Move the menu container inside the scroll body
        floatBody.appendChild(menuContainer);



        // Assemble inside #quarto-sidebar
        sidebar.appendChild(floatBody);

        // Mark as enhanced
        sidebar.classList.add('gd-sidebar-float');

        return true;
    }

    // ── Update sidebar bounds ──────────────────────────────────
    // With position:sticky, `top` sets the stick offset from the viewport top.
    // We can't use `bottom` to shrink the sidebar — instead we compute a
    // dynamic `max-height` that accounts for the navbar and footer overlap.
    function updateBounds() {
        if (!sidebar || !mql.matches) return;

        var header = getHeader();
        var footer = getFooter();
        var viewportH = window.innerHeight;

        var navBottom = header ? header.getBoundingClientRect().bottom : 0;
        var footerTop = footer ? footer.getBoundingClientRect().top : viewportH;

        var top = Math.max(0, navBottom) + GAP;

        // Available height = viewport minus navbar minus any footer overlap minus gaps
        var footerOverlap = Math.max(0, viewportH - footerTop);
        var maxH = viewportH - top - footerOverlap - GAP - FOOTER_BUFFER;

        sidebar.style.top = top + 'px';
        // Always apply maxHeight so the sidebar never overflows its bounds
        sidebar.style.maxHeight = Math.max(100, maxH) + 'px';
    }



    // ── Scroll-to-active ───────────────────────────────────────
    function scrollToActive() {
        if (!floatBody) return;
        var active = floatBody.querySelector('.sidebar-link.active');
        if (active) {
            // Scroll only the float body — NOT the main page.
            // scrollIntoView() would bubble up and shift the document.
            requestAnimationFrame(function () {
                var bodyRect = floatBody.getBoundingClientRect();
                var activeRect = active.getBoundingClientRect();
                var offset = activeRect.top - bodyRect.top - (bodyRect.height / 2) + (activeRect.height / 2);
                floatBody.scrollTop += offset;
            });
        }
    }

    // ── rAF-throttled scroll/resize handler ────────────────────
    function onFrameUpdate() {
        updateBounds();
        rafId = null;
    }

    function scheduleUpdate() {
        if (rafId) return;
        rafId = requestAnimationFrame(onFrameUpdate);
    }

    // Immediate update on resize for more responsive bounds
    function onResize() {
        updateBounds();
        scheduleUpdate(); // also schedule a follow-up in case layout settles
    }

    // ── Teardown (for breakpoint changes) ──────────────────────
    function teardown() {
        if (!initialised) return;

        // Move menu container back to sidebar root
        if (menuContainer && sidebar) {
            sidebar.appendChild(menuContainer);
        }

        // Remove added elements

        if (floatBody && floatBody.parentNode) floatBody.parentNode.removeChild(floatBody);

        sidebar.classList.remove('gd-sidebar-float');
        sidebar.style.top = '';
        sidebar.style.maxHeight = '';

        // Remove listeners
        window.removeEventListener('scroll', scheduleUpdate);
        window.removeEventListener('resize', onResize);
        window.removeEventListener('quarto-hrChanged', scheduleUpdate);
        if (resizeObs) {
            resizeObs.disconnect();
            resizeObs = null;
        }
        floatBody = null;
        initialised = false;
    }

    // ── Initialise ─────────────────────────────────────────────
    function init() {
        if (initialised) return;
        if (!mql.matches) return;

        if (!buildFloat()) return;

        // Bind events
        window.addEventListener('scroll', scheduleUpdate, { passive: true });
        window.addEventListener('resize', onResize, { passive: true });
        window.addEventListener('quarto-hrChanged', scheduleUpdate);

        // ResizeObserver for more reliable size tracking
        if (typeof ResizeObserver !== 'undefined') {
            resizeObs = new ResizeObserver(scheduleUpdate);
            resizeObs.observe(document.documentElement);
        }

        initialised = true;

        // Initial measurements
        updateBounds();
        scrollToActive();
    }

    // ── Respond to breakpoint changes ──────────────────────────
    mql.addEventListener('change', function () {
        if (mql.matches) {
            init();
        } else {
            teardown();
        }
    });

    // ── Boot ───────────────────────────────────────────────────
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();

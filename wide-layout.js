/**
 * Wide Layout Toggle for Great Docs
 *
 * Features:
 * - Floating button (directly above back-to-top) that widens the content
 *   column and both sidebars on wide desktop viewports
 * - Animated transition (the grid tracks interpolate via --gd-wide-t)
 * - Keeps the reader's place while the text reflows
 * - Remembers the choice across pages and visits (localStorage)
 * - Respects reduced-motion preferences
 * - Dark mode aware, keyboard accessible
 *
 * theme-init.js applies the stored width before first paint and toggles
 * .gd-wide-capable on <html> at or above the configured viewport width; the
 * button is only shown while that class is present.
 */

(function() {
    'use strict';

    var STORAGE_KEY = 'great-docs-width';
    var BASE_BOTTOM = 32;       // matches the back-to-top CSS default (2rem)
    var STACK_GAP = 12;         // vertical gap between stacked floating buttons
    var MAX_ANIM_MS = 700;      // upper bound for following the transition

    // i18n helper — read translations from <meta name="gd-i18n">
    var _i18nCache = null;
    function _gdT(key, fallback) {
        if (!_i18nCache) {
            try {
                var meta = document.querySelector('meta[name="gd-i18n"]');
                _i18nCache = meta ? JSON.parse(meta.getAttribute('content')) : {};
            } catch (e) { _i18nCache = {}; }
        }
        return _i18nCache[key] || fallback;
    }

    var html = document.documentElement;

    function prefersReducedMotion() {
        return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    }

    function isWide() {
        return html.getAttribute('data-gd-width') === 'wide';
    }

    /**
     * Only pages using the floating-sidebar grid can widen
     */
    function hasWidenableLayout() {
        var body = document.body;
        return body.classList.contains('floating') ||
            body.classList.contains('gd-section-no-sidebar');
    }

    /**
     * Create the toggle button with both icons; CSS shows the one matching
     * the action the button will perform
     */
    function createButton() {
        var btn = document.createElement('button');
        btn.className = 'gd-wide-toggle';
        btn.setAttribute('type', 'button');

        var svgOpen =
            '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" ' +
            'fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" ' +
            'stroke-linejoin="round" aria-hidden="true" class="';

        // Lucide-style chevrons-left-right (widen) and chevrons-right-left (narrow)
        btn.innerHTML =
            svgOpen + 'gd-wide-icon-widen">' +
            '<polyline points="9 7 4 12 9 17"></polyline>' +
            '<polyline points="15 7 20 12 15 17"></polyline>' +
            '</svg>' +
            svgOpen + 'gd-wide-icon-narrow">' +
            '<polyline points="4 7 9 12 4 17"></polyline>' +
            '<polyline points="20 7 15 12 20 17"></polyline>' +
            '</svg>';

        return btn;
    }

    function updateButton(btn) {
        var wide = isWide();
        var label = wide
            ? _gdT('wide_layout_restore', 'Restore default width')
            : _gdT('wide_layout_widen', 'Widen content');
        btn.setAttribute('aria-pressed', wide ? 'true' : 'false');
        btn.setAttribute('aria-label', label);
        btn.setAttribute('title', label);
    }

    /**
     * Find an element near the top of the viewport to keep in place while the
     * content reflows, and record its offset from the viewport top
     */
    function findScrollAnchor() {
        var content = document.getElementById('quarto-document-content') ||
            document.querySelector('main.content');
        if (!content || window.scrollY < 1) return null;

        var header = document.getElementById('quarto-header');
        var top = 0;
        if (header) {
            var headerRect = header.getBoundingClientRect();
            if (headerRect.bottom > 0) top = headerRect.bottom;
        }

        var candidates = content.querySelectorAll(
            'h1, h2, h3, h4, h5, h6, p, li, pre, table, figure, dt, dd, blockquote'
        );
        for (var i = 0; i < candidates.length; i++) {
            var rect = candidates[i].getBoundingClientRect();
            if (rect.height > 0 && rect.bottom > top) {
                return { el: candidates[i], offset: rect.top };
            }
        }
        return null;
    }

    function restoreScrollAnchor(anchor) {
        if (!anchor || !anchor.el.isConnected) return;
        var delta = anchor.el.getBoundingClientRect().top - anchor.offset;
        if (Math.abs(delta) >= 1) {
            window.scrollBy(0, delta);
        }
    }

    /**
     * Keep the anchor in place on every frame until the width transition ends,
     * then let width-sensitive components (tables, diagrams, widgets) re-layout
     */
    function followTransition(anchor) {
        var done = false;
        var start = performance.now();
        // Browser scroll anchoring would fight the per-frame correction
        html.style.overflowAnchor = 'none';

        function finish() {
            if (done) return;
            done = true;
            html.removeEventListener('transitionend', onEnd);
            restoreScrollAnchor(anchor);
            html.style.overflowAnchor = '';
            window.dispatchEvent(new Event('resize'));
        }

        function onEnd(e) {
            if (e.target === html && e.propertyName === '--gd-wide-t') finish();
        }

        function frame(now) {
            if (done) return;
            restoreScrollAnchor(anchor);
            if (now - start > MAX_ANIM_MS) {
                finish();
            } else {
                requestAnimationFrame(frame);
            }
        }

        if (prefersReducedMotion()) {
            requestAnimationFrame(finish);
            return;
        }
        html.addEventListener('transitionend', onEnd);
        requestAnimationFrame(frame);
    }

    function toggle(btn) {
        var anchor = findScrollAnchor();
        var next = isWide() ? 'normal' : 'wide';
        html.setAttribute('data-gd-width', next);
        try { localStorage.setItem(STORAGE_KEY, next); } catch (e) { /* unavailable */ }
        updateButton(btn);
        followTransition(anchor);
    }

    /**
     * Stack above back-to-top, mirroring its prev/next page-nav avoidance so
     * the two buttons move together
     */
    function syncPosition(btn) {
        var bottom = BASE_BOTTOM;
        var pageNav = document.querySelector('.page-navigation');
        if (pageNav) {
            var navRect = pageNav.getBoundingClientRect();
            var viewportHeight = window.innerHeight;
            if (navRect.top < viewportHeight && navRect.bottom > 0) {
                bottom = Math.max(viewportHeight - navRect.top + 16, BASE_BOTTOM);
            }
        }
        var btt = document.querySelector('.gd-back-to-top');
        if (btt) {
            bottom += (btt.offsetHeight || 40) + STACK_GAP;
        }
        btn.style.bottom = bottom + 'px';
    }

    function init() {
        var meta = document.querySelector('meta[name="gd-wide-layout"]');
        if (!meta || !hasWidenableLayout()) {
            html.classList.remove('gd-wide-instant');
            return;
        }

        var btn = createButton();
        updateButton(btn);
        document.body.appendChild(btn);
        btn.addEventListener('click', function() { toggle(btn); });

        var ticking = false;
        function scheduleSync() {
            if (ticking) return;
            ticking = true;
            window.requestAnimationFrame(function() {
                syncPosition(btn);
                ticking = false;
            });
        }
        window.addEventListener('scroll', scheduleSync, { passive: true });
        window.addEventListener('resize', scheduleSync, { passive: true });
        syncPosition(btn);
        // back-to-top.js may load after this script
        window.addEventListener('load', scheduleSync);

        // Enable the width animation once the initial layout has settled
        requestAnimationFrame(function() {
            requestAnimationFrame(function() {
                html.classList.remove('gd-wide-instant');
            });
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();

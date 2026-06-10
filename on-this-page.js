/**
 * On This Page – Mobile Floating Button for Great Docs
 *
 * Features:
 * - Round floating button visible only on mobile (< 768px)
 * - Positioned above the back-to-top button to avoid collision
 * - Opens a floating panel with the page's table-of-contents links
 * - Tapping a section link scrolls there and dismisses the panel
 * - Tapping outside the panel dismisses it without navigation
 * - Dark mode aware
 * - Keyboard accessible
 * - Respects reduced-motion preferences
 */

(function () {
    'use strict';

    // Only activate on mobile-width viewports
    var MQ = window.matchMedia('(max-width: 767.98px)');

    /**
     * Collect TOC entries from the existing Quarto sidebar TOC.
     * Returns an array of { text, href, level } objects.
     */
    function collectTocEntries() {
        // Quarto renders the right-hand TOC inside #quarto-margin-sidebar or
        // nav#TOC. On mobile it's hidden via CSS, but the DOM is still there.
        var tocNav = document.getElementById('TOC') ||
                     document.querySelector('#quarto-margin-sidebar nav');
        if (!tocNav) return [];

        var links = tocNav.querySelectorAll('a.nav-link');
        var entries = [];
        for (var i = 0; i < links.length; i++) {
            var a = links[i];
            // Prefer data-scroll-target (always has the raw #hash);
            // fall back to href and extract the hash fragment
            var target = a.getAttribute('data-scroll-target');
            if (!target) {
                var href = a.getAttribute('href') || '';
                var hashIdx = href.indexOf('#');
                target = hashIdx >= 0 ? href.substring(hashIdx) : null;
            }
            if (!target || target.charAt(0) !== '#') continue;
            // Determine nesting level from parent <li> depth
            var depth = 0;
            var el = a.parentElement;
            while (el && el !== tocNav) {
                if (el.tagName === 'UL') depth++;
                el = el.parentElement;
            }
            entries.push({
                text: a.textContent.trim(),
                href: target,
                level: depth
            });
        }
        return entries;
    }

    /**
     * Create the floating trigger button.
     */
    function createButton() {
        var btn = document.createElement('button');
        btn.className = 'gd-otp-btn';
        btn.setAttribute('aria-label', 'On this page');
        btn.setAttribute('title', 'On this page');
        btn.setAttribute('type', 'button');

        // List / table-of-contents icon (Lucide-style)
        btn.innerHTML =
            '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" ' +
            'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" ' +
            'stroke-linejoin="round" aria-hidden="true">' +
            '<line x1="8" y1="6" x2="21" y2="6"></line>' +
            '<line x1="8" y1="12" x2="21" y2="12"></line>' +
            '<line x1="8" y1="18" x2="21" y2="18"></line>' +
            '<line x1="3" y1="6" x2="3.01" y2="6"></line>' +
            '<line x1="3" y1="12" x2="3.01" y2="12"></line>' +
            '<line x1="3" y1="18" x2="3.01" y2="18"></line>' +
            '</svg>';

        return btn;
    }

    /**
     * Create the floating panel that shows the TOC entries.
     */
    function createPanel(entries) {
        var panel = document.createElement('div');
        panel.className = 'gd-otp-panel';
        panel.setAttribute('role', 'dialog');
        panel.setAttribute('aria-label', 'On this page');

        var heading = document.createElement('div');
        heading.className = 'gd-otp-panel-heading';
        heading.textContent = 'On this page';
        panel.appendChild(heading);

        var list = document.createElement('ul');
        list.className = 'gd-otp-panel-list';

        for (var i = 0; i < entries.length; i++) {
            var entry = entries[i];
            var li = document.createElement('li');
            if (entry.level > 1) {
                li.className = 'gd-otp-nested';
            }
            var a = document.createElement('a');
            a.href = entry.href;
            a.textContent = entry.text;
            a.className = 'gd-otp-panel-link';
            li.appendChild(a);
            list.appendChild(li);
        }

        panel.appendChild(list);
        return panel;
    }

    /**
     * Create the backdrop overlay for dismissing the panel.
     */
    function createBackdrop() {
        var backdrop = document.createElement('div');
        backdrop.className = 'gd-otp-backdrop';
        return backdrop;
    }

    /**
     * Coordinate the button position relative to the back-to-top button
     * so they never collide.
     */
    /**
     * Coordinate the button position relative to the back-to-top button
     * so they never collide. Computes from the same source of truth
     * (page-navigation element) that back-to-top uses, avoiding animation lag.
     */
    function syncPosition(btn) {
        var btt = document.querySelector('.gd-back-to-top');
        if (!btt) return;

        var bttHeight = btt.offsetHeight || 36;
        var gap = 12;

        // Mirror the same page-nav overlap logic that back-to-top.js uses
        var baseBottom = 20; // matches mobile CSS default (1.25rem)
        var pageNav = document.querySelector('.page-navigation');
        if (pageNav) {
            var navRect = pageNav.getBoundingClientRect();
            var viewportHeight = window.innerHeight;
            if (navRect.top < viewportHeight && navRect.bottom > 0) {
                var overlap = viewportHeight - navRect.top + 16;
                baseBottom = Math.max(overlap, 32);
            }
        }

        // Stack OTP above back-to-top
        var otpBottom = baseBottom + bttHeight + gap;
        btn.style.bottom = otpBottom + 'px';
    }

    function init() {
        var entries = collectTocEntries();
        // Don't show the button if there are no TOC entries
        if (entries.length === 0) return;

        var btn = createButton();
        var panel = createPanel(entries);
        var backdrop = createBackdrop();
        var isOpen = false;

        document.body.appendChild(btn);
        document.body.appendChild(backdrop);
        document.body.appendChild(panel);

        function open() {
            if (isOpen) return;
            isOpen = true;
            panel.classList.add('gd-otp-panel-visible');
            backdrop.classList.add('gd-otp-backdrop-visible');
            btn.classList.add('gd-otp-btn-active');
            btn.setAttribute('aria-expanded', 'true');

            // Position the panel above the button
            var btnRect = btn.getBoundingClientRect();
            var panelHeight = panel.offsetHeight;
            var bottomOffset = window.innerHeight - btnRect.top + 8;
            panel.style.bottom = bottomOffset + 'px';
            panel.style.right = btn.style.right || '1.25rem';
        }

        function close() {
            if (!isOpen) return;
            isOpen = false;
            panel.classList.remove('gd-otp-panel-visible');
            backdrop.classList.remove('gd-otp-backdrop-visible');
            btn.classList.remove('gd-otp-btn-active');
            btn.setAttribute('aria-expanded', 'false');
        }

        // Toggle on button tap
        btn.addEventListener('click', function (e) {
            e.stopPropagation();
            if (isOpen) {
                close();
            } else {
                open();
            }
        });

        // Dismiss on backdrop tap (outside panel)
        backdrop.addEventListener('click', function () {
            close();
        });

        // Handle link taps: navigate + dismiss
        var links = panel.querySelectorAll('.gd-otp-panel-link');
        for (var i = 0; i < links.length; i++) {
            links[i].addEventListener('click', function (e) {
                e.preventDefault();
                var targetId = this.getAttribute('href');
                close();

                // Navigate to the section
                var target = document.querySelector(targetId);
                if (target) {
                    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
                        target.scrollIntoView();
                    } else {
                        target.scrollIntoView({ behavior: 'smooth' });
                    }
                    // Update URL hash without triggering scroll
                    history.pushState(null, '', targetId);
                }
            });
        }

        // Close on Escape key
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && isOpen) {
                close();
                btn.focus();
            }
        });

        // Show/hide based on media query
        function onMediaChange(mq) {
            if (mq.matches) {
                btn.style.display = 'flex';
            } else {
                btn.style.display = 'none';
                close();
            }
        }

        // Sync position with back-to-top button on scroll
        var ticking = false;
        window.addEventListener('scroll', function () {
            if (!ticking) {
                window.requestAnimationFrame(function () {
                    syncPosition(btn);
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });

        // Initial position sync
        syncPosition(btn);

        // Listen for media query changes
        if (MQ.addEventListener) {
            MQ.addEventListener('change', onMediaChange);
        } else if (MQ.addListener) {
            MQ.addListener(onMediaChange);
        }

        // Set initial visibility
        onMediaChange(MQ);
    }

    // DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();

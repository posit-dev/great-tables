/**
 * Keyboard Navigation & Shortcuts for Great Docs
 *
 * Features:
 * - `/` or `s` to focus search
 * - `[` / `]` for previous/next page navigation
 * - `q` to navigate to homepage
 * - `u` to navigate to User Guide (when available)
 * - `r` to navigate to API Reference (when available)
 * - `m` or `n` to show/hide floating menu overlay (sidebar nav or navbar links)
 * - `d` to toggle dark mode
 * - `c` to copy page as Markdown (when available)
 * - `h` or `?` to show/hide keyboard shortcuts help overlay
 * - `Escape` to close overlay or unfocus active element
 * - Dark mode aware
 * - Respects reduced-motion preferences
 * - Skips shortcuts when user is typing in inputs/textareas
 * - ARIA attributes for screen reader accessibility
 */

(function() {
    'use strict';

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

    // State
    var overlay = null;
    var isOverlayOpen = false;
    var menuOverlay = null;
    var isMenuOpen = false;

    /**
     * Check if the user prefers reduced motion
     */
    function prefersReducedMotion() {
        return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    }

    /**
     * Check if the active element is an input or editable area
     */
    function isTyping() {
        var el = document.activeElement;
        if (!el) return false;
        var tag = el.tagName;
        if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return true;
        if (el.isContentEditable) return true;
        // Quarto search autocomplete input
        if (el.classList.contains('aa-Input')) return true;
        return false;
    }

    // ── Search Focus ─────────────────────────────────────────────────────

    function focusSearch() {
        // Try Quarto's Algolia-style autocomplete input first
        var searchInput = document.querySelector('.aa-Input');
        if (!searchInput) {
            // Fall back to the Quarto search container (clicking it usually opens the search)
            var searchContainer = document.querySelector('#quarto-search');
            if (searchContainer) {
                var btn = searchContainer.querySelector('button') ||
                          searchContainer.querySelector('[role="button"]');
                if (btn) {
                    btn.click();
                    return;
                }
            }
        }
        if (searchInput) {
            searchInput.focus();
            if (searchInput.select) searchInput.select();
        }
    }

    // ── Page Navigation ──────────────────────────────────────────────────

    function navigatePrev() {
        var link = document.querySelector('.nav-page-previous a.pagination-link');
        if (link) {
            link.click();
        }
    }

    function navigateNext() {
        var link = document.querySelector('.nav-page-next a.pagination-link');
        if (link) {
            link.click();
        }
    }

    function navigateHome() {
        // Use the navbar brand link (always points to site root)
        var brand = document.querySelector('.navbar-brand');
        if (brand && brand.href) {
            window.location.href = brand.href;
            return;
        }
        // Fallback: navigate to site root
        window.location.href = './';
    }

    /**
     * Find a navbar link whose href contains the given path segment.
     */
    function findNavbarLink(pathSegment) {
        var links = document.querySelectorAll(
            '#navbarCollapse > .navbar-nav.me-auto > .nav-item > .nav-link'
        );
        for (var i = 0; i < links.length; i++) {
            var href = links[i].getAttribute('href') || '';
            if (href.indexOf(pathSegment) !== -1) return links[i];
        }
        return null;
    }

    function hasUserGuide() { return !!findNavbarLink('user-guide/'); }
    function hasReference() { return !!findNavbarLink('reference/'); }

    function navigateUserGuide() {
        var link = findNavbarLink('user-guide/');
        if (link) window.location.href = link.getAttribute('href');
    }

    function navigateReference() {
        var link = findNavbarLink('reference/');
        if (link) window.location.href = link.getAttribute('href');
    }

    // ── Show Menu Overlay ──────────────────────────────────────────────

    /**
     * Detect whether the current page is the homepage.
     * Homepage body has `nav-fixed` but NOT `nav-sidebar`.
     */
    function isHomepage() {
        return !document.body.classList.contains('nav-sidebar');
    }

    /**
     * Build menu items from the top navbar links (used on homepage).
     * Returns an array of {text, href, active, section, html, badgeHtml} objects.
     */
    function getNavbarItems() {
        var items = [];
        var links = document.querySelectorAll(
            '#navbarCollapse > .navbar-nav.me-auto > .nav-item > .nav-link'
        );
        for (var i = 0; i < links.length; i++) {
            var a = links[i];
            var text = a.querySelector('.menu-text');
            if (!text) continue;
            items.push({
                text: text.textContent.trim(),
                html: text.innerHTML,
                badgeHtml: '',
                href: a.getAttribute('href') || '#',
                active: a.classList.contains('active'),
                section: null
            });
        }
        return items;
    }

    /**
     * Build menu items from the left sidebar navigation (used on content pages).
     * Handles both sectioned sidebars (User Guide) and flat sidebars (Recipes).
     * Returns an array of {text, href, active, section, html, badgeHtml, upcomingHtml} objects.
     * - html: innerHTML of .menu-text (includes icons + text)
     * - badgeHtml: outerHTML of .gd-sidebar-status-badge (if present)
     * - upcomingHtml: outerHTML of .gd-sidebar-upcoming rocket icon (if present)
     */
    function getSidebarItems() {
        var items = [];
        var sidebar = document.getElementById('quarto-sidebar');
        if (!sidebar) return items;

        function extractItem(a, sectionTitle) {
            var menuText = a.querySelector('.menu-text');
            if (!menuText) return null;
            var badge = a.querySelector('.gd-sidebar-status-badge');
            var upcoming = a.querySelector('.gd-sidebar-upcoming');
            return {
                text: menuText.textContent.trim(),
                html: menuText.innerHTML,
                badgeHtml: badge ? badge.outerHTML : '',
                upcomingHtml: upcoming ? upcoming.outerHTML : '',
                href: a.getAttribute('href') || '#',
                active: a.classList.contains('active'),
                section: sectionTitle
            };
        }

        function extractSectionHtml(sec) {
            var headerEl = sec.querySelector(':scope > .sidebar-item-container .menu-text');
            if (!headerEl) {
                // Try sidebar-item-text for section headers without .menu-text
                headerEl = sec.querySelector(':scope > .sidebar-item-container .sidebar-item-text');
            }
            return headerEl ? headerEl.innerHTML : null;
        }

        var sections = sidebar.querySelectorAll('.sidebar-item-section');

        if (sections.length > 0) {
            // Sectioned sidebar (e.g., User Guide pages)
            // First, capture any top-level links outside sections (e.g., "API Index")
            var menuContainer = sidebar.querySelector('.sidebar-menu-container');
            if (menuContainer) {
                var topLis = menuContainer.querySelectorAll(':scope > ul > li.sidebar-item:not(.sidebar-item-section)');
                for (var t = 0; t < topLis.length; t++) {
                    var topLink = topLis[t].querySelector('.sidebar-link');
                    if (topLink) {
                        var topItem = extractItem(topLink, null);
                        if (topItem) items.push(topItem);
                    }
                }
            }

            for (var s = 0; s < sections.length; s++) {
                var sec = sections[s];
                var sectionHtml = extractSectionHtml(sec);

                var links = sec.querySelectorAll('.sidebar-section .sidebar-link');
                for (var i = 0; i < links.length; i++) {
                    var item = extractItem(links[i], sectionHtml);
                    if (item) {
                        items.push(item);
                        sectionHtml = null;
                    }
                }
            }
        } else {
            // Flat sidebar (e.g., Recipes, custom sections)
            var links = sidebar.querySelectorAll('.sidebar-item .sidebar-link');
            for (var i = 0; i < links.length; i++) {
                var item = extractItem(links[i], null);
                if (item) items.push(item);
            }
        }

        return items;
    }

    /**
     * Detect whether the current page is a Reference page (API or CLI).
     */
    function isReferencePage() {
        return document.body.classList.contains('gd-ref-sidebar');
    }

    /**
     * Detect whether the current page is CLI Reference (vs API Reference).
     */
    function isCliReferencePage() {
        return window.location.pathname.indexOf('/reference/cli/') !== -1;
    }

    /**
     * Detect whether the current page is MCP Reference.
     */
    function isMcpReferencePage() {
        return window.location.pathname.indexOf('/reference/mcp/') !== -1;
    }

    /**
     * Get enabled reference sections from body data attribute.
     */
    function getRefSections() {
        var attr = document.body.getAttribute('data-gd-ref-sections');
        if (attr) return attr.split(',').map(function(s) { return s.trim(); }).filter(Boolean);
        // Fallback detection
        var sections = ['api'];
        if (document.querySelector('.reference-switcher-container') ||
            document.querySelector('a[href*="/reference/cli/"]') ||
            isCliReferencePage()) {
            sections.push('cli');
        }
        if (document.querySelector('a[href*="/reference/mcp/"]') ||
            isMcpReferencePage()) {
            sections.push('mcp');
        }
        return sections;
    }

    /**
     * Check if CLI Reference docs exist (switcher should show both tabs).
     */
    function hasCliReference() {
        // Check multiple signals: the reference-switcher widget (injected by
        // reference-switcher.js into the hidden sidebar), any <a> to CLI docs,
        // or being on a CLI page itself.
        return !!document.querySelector('.reference-switcher-container') ||
               !!document.querySelector('a[href*="/reference/cli/"]') ||
               isCliReferencePage();
    }

    /**
     * Build the reference switcher HTML for the keyboard nav overlay.
     * Uses segmented buttons for 2 sections, dropdown for 3+.
     */
    function buildRefSwitcherHtml() {
        var sections = getRefSections();
        if (sections.length < 2) return '';

        var currentRef = 'api';
        if (isMcpReferencePage()) currentRef = 'mcp';
        else if (isCliReferencePage()) currentRef = 'cli';

        var sectionMeta = {
            api: { label: _gdT('api', 'Python API'), svg: '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>' },
            cli: { label: _gdT('cli', 'CLI'), svg: '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg>' },
            mcp: { label: _gdT('mcp', 'MCP Server'), svg: '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg>' }
        };

        var html = '<div class="gd-menu-ref-switcher">';
        for (var i = 0; i < sections.length; i++) {
            var id = sections[i];
            var meta = sectionMeta[id] || { label: id, svg: '' };
            var active = id === currentRef ? ' active' : '';
            html += '<button class="gd-menu-ref-switcher-btn' + active + '" data-ref="' + id + '">';
            html += meta.svg;
            html += '<span>' + escapeHtml(meta.label) + '</span></button>';
        }
        html += '</div>';
        return html;
    }

    /**
     * Build the reference filter input HTML.
     */
    function buildRefFilterHtml(itemCount) {
        if (itemCount < 15) return '';
        var placeholder = _gdT('sidebar_filter_placeholder', 'Filter...');
        var html = '<div class="gd-menu-ref-filter">';
        html += '<svg class="gd-menu-ref-filter-icon" xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>';
        html += '<input type="text" class="gd-menu-ref-filter-input" placeholder="' + escapeHtml(placeholder) + '" aria-label="' + escapeHtml(placeholder) + '">';
        html += '</div>';
        return html;
    }

    /**
     * Attach filter behaviour to the overlay for reference pages.
     */
    function attachRefFilter(overlay) {
        var input = overlay.querySelector('.gd-menu-ref-filter-input');
        if (!input) return;

        input.addEventListener('input', function() {
            var query = input.value.toLowerCase().trim();
            var items = overlay.querySelectorAll('.gd-menu-item');
            var sections = overlay.querySelectorAll('.gd-menu-section');

            // Show/hide items based on text match
            for (var i = 0; i < items.length; i++) {
                var text = items[i].textContent.toLowerCase();
                items[i].parentElement.style.display = (!query || text.indexOf(query) !== -1) ? '' : 'none';
            }

            // Show section headers only if at least one child item is visible
            for (var s = 0; s < sections.length; s++) {
                var li = sections[s];
                var next = li.nextElementSibling;
                var anyVisible = false;
                while (next && !next.classList.contains('gd-menu-section')) {
                    if (next.style.display !== 'none') anyVisible = true;
                    next = next.nextElementSibling;
                }
                li.style.display = anyVisible ? '' : 'none';
            }
        });

        // Focus filter on open (after transition)
        setTimeout(function() { input.focus(); }, 220);
    }

    /**
     * Parse sidebar items from an HTML string (fetched from another page).
     * Returns an array of {text, html, href, section} objects.
     */
    function parseSidebarItemsFromHtml(htmlStr, baseUrl) {
        var parser = new DOMParser();
        var doc = parser.parseFromString(htmlStr, 'text/html');
        var sidebar = doc.getElementById('quarto-sidebar');
        if (!sidebar) return [];

        var items = [];
        var sections = sidebar.querySelectorAll('.sidebar-item-section');

        // Resolve relative URLs against the fetched page's base
        var fullBase = new URL(baseUrl, window.location.origin).href;
        function resolveHref(href) {
            if (!href || href === '#') return '#';
            try { return new URL(href, fullBase).pathname; }
            catch (e) { return href; }
        }

        function extractParsedItem(a, sectionText) {
            var menuText = a.querySelector('.menu-text');
            if (!menuText) return null;
            return {
                text: menuText.textContent.trim(),
                html: menuText.innerHTML,
                href: resolveHref(a.getAttribute('href')),
                active: false,
                section: sectionText
            };
        }

        if (sections.length > 0) {
            // Top-level links outside sections (like "API Index")
            var menuContainer = sidebar.querySelector('.sidebar-menu-container');
            if (menuContainer) {
                var topLis = menuContainer.querySelectorAll(':scope > ul > li.sidebar-item:not(.sidebar-item-section)');
                for (var t = 0; t < topLis.length; t++) {
                    var topLink = topLis[t].querySelector('.sidebar-link');
                    if (topLink) {
                        var topItem = extractParsedItem(topLink, null);
                        if (topItem) items.push(topItem);
                    }
                }
            }

            for (var s = 0; s < sections.length; s++) {
                var sec = sections[s];
                var headerEl = sec.querySelector(':scope > .sidebar-item-container .menu-text') ||
                               sec.querySelector(':scope > .sidebar-item-container .sidebar-item-text');
                var sectionText = headerEl ? headerEl.innerHTML : null;
                var links = sec.querySelectorAll('.sidebar-section .sidebar-link');
                for (var i = 0; i < links.length; i++) {
                    var item = extractParsedItem(links[i], sectionText);
                    if (item) {
                        items.push(item);
                        sectionText = null;
                    }
                }
            }
        } else {
            var flatLinks = sidebar.querySelectorAll('.sidebar-item .sidebar-link');
            for (var i = 0; i < flatLinks.length; i++) {
                var item = extractParsedItem(flatLinks[i], null);
                if (item) items.push(item);
            }
        }

        return items;
    }

    /**
     * Render items into the overlay list (replacing current contents).
     */
    function renderItemsInOverlay(overlay, items) {
        var listEl = overlay.querySelector('.gd-menu-list');
        if (!listEl) return;

        var html = '';
        var currentSection = null;
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            if (item.section && item.section !== currentSection) {
                currentSection = item.section;
                // Section text comes from innerHTML (already HTML-safe), so
                // insert directly without escaping to avoid double-encoding
                // entities like &amp; → &amp;amp;
                html += '<li class="gd-menu-section" aria-hidden="true">' +
                        currentSection + '</li>';
            }
            var activeClass = item.active ? ' gd-menu-item-active' : '';
            var label = item.html || escapeHtml(item.text);
            html += '<li><a class="gd-menu-item' + activeClass +
                    '" href="' + escapeHtml(item.href) + '">' +
                    '<span class="gd-menu-item-label">' + label + '</span>' +
                    '</a></li>';
        }
        listEl.innerHTML = html;

        // Clear filter input if present
        var filterInput = overlay.querySelector('.gd-menu-ref-filter-input');
        if (filterInput) {
            filterInput.value = '';
            filterInput.dispatchEvent(new Event('input'));
        }
    }

    /**
     * Attach switcher behaviour: clicking a tab fetches items from the
     * other reference section and swaps the list in the overlay without
     * navigating away.
     */
    function attachRefSwitcher(overlay) {
        var buttons = overlay.querySelectorAll('.gd-menu-ref-switcher-btn');
        if (!buttons.length) return;

        var basePath = window.location.pathname.split('/reference/')[0];
        var cache = {}; // cache fetched items by ref type

        // Pre-populate current section's items from what's already rendered
        var currentType = 'api';
        if (isMcpReferencePage()) currentType = 'mcp';
        else if (isCliReferencePage()) currentType = 'cli';

        var refPaths = {
            api: basePath + '/reference/index.html',
            cli: basePath + '/reference/cli/index.html',
            mcp: basePath + '/reference/mcp/index.html'
        };

        for (var i = 0; i < buttons.length; i++) {
            (function(btn) {
                btn.addEventListener('click', function() {
                    var refType = btn.getAttribute('data-ref');

                    // Update active state on buttons
                    for (var b = 0; b < buttons.length; b++) { buttons[b].classList.remove('active'); }
                    btn.classList.add('active');

                    // If switching to the section we're already on, re-render from sidebar
                    if (refType === currentType) {
                        var items = getSidebarItems();
                        renderItemsInOverlay(overlay, items);
                        return;
                    }

                    // If cached, render immediately
                    if (cache[refType]) {
                        renderItemsInOverlay(overlay, cache[refType]);
                        return;
                    }

                    // Fetch the target section's index page and parse its sidebar
                    var url = refPaths[refType] || basePath + '/reference/index.html';

                    fetch(url)
                        .then(function(res) { return res.text(); })
                        .then(function(htmlStr) {
                            var items = parseSidebarItemsFromHtml(htmlStr, url);
                            cache[refType] = items;
                            // Only render if this tab is still active
                            if (btn.classList.contains('active')) {
                                renderItemsInOverlay(overlay, items);
                            }
                        })
                        .catch(function() {
                            // On error, fall back to navigation
                            window.location.href = url;
                        });
                });
            })(buttons[i]);
        }
    }

    /**
     * Create the floating menu overlay element.
     */
    function createMenuOverlay() {
        var el = document.createElement('div');
        el.className = 'gd-menu-overlay';
        el.setAttribute('role', 'dialog');
        el.setAttribute('aria-modal', 'true');
        el.setAttribute('aria-label',
            _gdT('kb_show_menu', 'Show menu'));

        var homepage = isHomepage();
        var refPage = isReferencePage();
        var items = homepage ? getNavbarItems() : getSidebarItems();
        var title;
        if (homepage) {
            title = _gdT('kb_menu_title_site', 'Site Navigation');
        } else if (refPage) {
            title = isCliReferencePage()
                ? _gdT('cli_reference', 'CLI Reference')
                : _gdT('api_reference', 'API Reference');
        } else {
            title = _gdT('kb_menu_title_section', 'Section Navigation');
        }

        var html = '<div class="gd-menu-overlay-inner">';
        html += '<div class="gd-menu-overlay-header">';
        html += '<h2>' + escapeHtml(title) + '</h2>';
        html += '<button class="gd-menu-overlay-close" aria-label="' +
                escapeHtml(_gdT('kb_close_dismiss', 'Close')) +
                '" type="button">';
        html += '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" ' +
                'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" ' +
                'stroke-linejoin="round" aria-hidden="true">' +
                '<line x1="18" y1="6" x2="6" y2="18"></line>' +
                '<line x1="6" y1="6" x2="18" y2="18"></line>' +
                '</svg>';
        html += '</button>';
        html += '</div>';

        // Reference pages: inject switcher before the list
        if (refPage) {
            html += buildRefSwitcherHtml();
        }

        html += '<nav class="gd-menu-overlay-body" aria-label="' + escapeHtml(title) + '">';
        html += '<ul class="gd-menu-list">';

        var currentSection = null;
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            // Section divider — use rich HTML (with icon) when available
            if (item.section && item.section !== currentSection) {
                currentSection = item.section;
                html += '<li class="gd-menu-section" aria-hidden="true">' +
                        (typeof currentSection === 'string' && currentSection.indexOf('<') !== -1
                            ? currentSection
                            : escapeHtml(currentSection)) + '</li>';
            }
            var activeClass = item.active ? ' gd-menu-item-active' : '';
            // Use rich innerHTML (icon + text) when available, else plain text
            var label = item.html || escapeHtml(item.text);
            var badge = item.badgeHtml || '';
            var upcoming = item.upcomingHtml || '';
            html += '<li><a class="gd-menu-item' + activeClass +
                    '" href="' + escapeHtml(item.href) + '">' +
                    '<span class="gd-menu-item-label">' + label + badge + '</span>' +
                    upcoming + '</a></li>';
        }

        html += '</ul>';
        html += '</nav></div>';

        el.innerHTML = html;

        // Attach reference-specific interactivity
        if (refPage) {
            attachRefSwitcher(el);
        }

        return el;
    }

    // Menu keyboard navigation state
    var menuSelectedIndex = -1;

    /**
     * Get all navigable menu items from the overlay.
     */
    function getMenuItems() {
        if (!menuOverlay) return [];
        return menuOverlay.querySelectorAll('.gd-menu-item');
    }

    /**
     * Update the visual focus indicator on menu items.
     */
    function updateMenuFocus() {
        var items = getMenuItems();
        for (var i = 0; i < items.length; i++) {
            if (i === menuSelectedIndex) {
                items[i].classList.add('gd-menu-item-focused');
                items[i].scrollIntoView({ block: 'nearest' });
            } else {
                items[i].classList.remove('gd-menu-item-focused');
            }
        }
    }

    /**
     * Handle keyboard events within the menu overlay.
     */
    function handleMenuKeydown(e) {
        var items = getMenuItems();
        if (items.length === 0) return;

        switch (e.key) {
            case 'ArrowDown':
            case 'ArrowRight':
            case 'ArrowUp':
            case 'ArrowLeft':
                e.preventDefault();
                // Any arrow press selects the first item
                if (menuSelectedIndex < 0) {
                    menuSelectedIndex = 0;
                } else if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
                    menuSelectedIndex = Math.min(menuSelectedIndex + 1, items.length - 1);
                } else {
                    menuSelectedIndex = Math.max(menuSelectedIndex - 1, 0);
                }
                updateMenuFocus();
                break;

            case 'Enter':
                if (menuSelectedIndex >= 0 && menuSelectedIndex < items.length) {
                    e.preventDefault();
                    items[menuSelectedIndex].click();
                }
                break;
        }
    }

    function showMenu() {
        // Always recreate to pick up current page state
        if (menuOverlay) {
            menuOverlay.remove();
            menuOverlay = null;
        }

        menuOverlay = createMenuOverlay();
        document.body.appendChild(menuOverlay);
        menuSelectedIndex = -1;

        // Close button
        var closeBtn = menuOverlay.querySelector('.gd-menu-overlay-close');
        closeBtn.addEventListener('click', hideMenu);

        // Click on backdrop
        menuOverlay.addEventListener('click', function(e) {
            if (e.target === menuOverlay) {
                hideMenu();
            }
        });

        // Lock body scroll and add backdrop blur on mobile
        document.body.classList.add('gd-menu-open');

        // On mobile, force headroom into the "unpinned" state so the
        // full navbar slides up and only the Title Bar stays visible.
        // This prevents the overlay card from appearing behind a tall
        // header when the user is at the top of the page or has just
        // scrolled up.
        var header = document.querySelector('#quarto-header');
        var didFreezeHeadroom = false;
        if (header && window.matchMedia('(max-width: 991.98px)').matches) {
            header.classList.remove('headroom--pinned');
            header.classList.add('headroom--unpinned');
            // Freeze headroom via Quarto's toggle so it doesn't re-pin
            if (typeof window.quartoToggleHeadroom === 'function') {
                window.quartoToggleHeadroom(); // freeze
                didFreezeHeadroom = true;
            }
        }
        // Store so hideMenu can unfreeze only if we froze
        showMenu._frozeHeadroom = didFreezeHeadroom;

        // Force reflow then show
        void menuOverlay.offsetWidth;
        menuOverlay.classList.add('gd-menu-overlay-visible');
        isMenuOpen = true;

        // Auto-scroll the active item into view (centered)
        requestAnimationFrame(function() {
            var activeItem = menuOverlay.querySelector('.gd-menu-item-active');
            if (activeItem) {
                activeItem.scrollIntoView({ block: 'center', behavior: 'instant' });
            }
        });
    }

    function hideMenu() {
        if (!menuOverlay) return;
        menuOverlay.classList.remove('gd-menu-overlay-visible');
        document.body.classList.remove('gd-menu-open');

        // Resume headroom so it can pin/unpin normally again
        if (showMenu._frozeHeadroom && typeof window.quartoToggleHeadroom === 'function') {
            window.quartoToggleHeadroom(); // unfreeze
            showMenu._frozeHeadroom = false;
        }

        isMenuOpen = false;
        menuSelectedIndex = -1;
        // Remove after transition
        setTimeout(function() {
            if (menuOverlay && !isMenuOpen) {
                menuOverlay.remove();
                menuOverlay = null;
            }
        }, 200);
    }

    // ── Copy Page ────────────────────────────────────────────────────────

    function copyPage() {
        var btn = document.querySelector('.gd-copy-md-btn');
        if (btn) btn.click();
    }

    // ── Dark Mode Toggle ─────────────────────────────────────────────────

    function toggleDarkMode() {
        // Delegate to the existing dark-mode-toggle button if present
        var btn = document.getElementById('dark-mode-toggle');
        if (btn) {
            btn.click();
            return;
        }
    }

    // ── Help Overlay ─────────────────────────────────────────────────────

    var SHORTCUT_GROUPS = [
        {
            titleKey: 'kb_group_navigation',
            titleFallback: 'Navigation',
            shortcuts: [
                { keys: ['s', '/'], descKey: 'kb_focus_search', descFallback: 'Focus search' },
                { keys: ['[', ']'], descKey: 'kb_prev_next_page', descFallback: 'Previous / next page', separator: ' / ' },
                { keys: ['m', 'n'], descKey: 'kb_show_menu', descFallback: 'Show menu' },
                { keys: ['q'], descKey: 'kb_home', descFallback: 'Go to homepage' },
                { keys: ['u'], descKey: 'kb_user_guide', descFallback: 'User Guide', visible: hasUserGuide },
                { keys: ['r'], descKey: 'kb_api_reference', descFallback: 'API Reference', visible: hasReference },
            ]
        },
        {
            titleKey: 'kb_group_display',
            titleFallback: 'Display',
            shortcuts: [
                { keys: ['d'], descKey: 'kb_toggle_dark', descFallback: 'Toggle dark mode' },
                { keys: ['c'], descKey: 'kb_copy_page', descFallback: 'Copy page as Markdown' },
            ]
        },
        {
            titleKey: 'kb_group_general',
            titleFallback: 'General',
            shortcuts: [
                { keys: ['h', '?'], descKey: 'kb_show_help', descFallback: 'Show keyboard shortcuts' },
                { keys: ['Esc'], descKey: 'kb_close_dismiss', descFallback: 'Close / dismiss' },
            ]
        },
    ];

    function createOverlay() {
        var el = document.createElement('div');
        el.className = 'gd-keyboard-overlay';
        el.setAttribute('role', 'dialog');
        el.setAttribute('aria-modal', 'true');
        el.setAttribute('aria-label',
            _gdT('kb_overlay_title', 'Keyboard shortcuts'));

        var title = _gdT('kb_overlay_title', 'Keyboard shortcuts');

        var html = '<div class="gd-keyboard-overlay-inner">';
        html += '<div class="gd-keyboard-overlay-header">';
        html += '<h2>' + escapeHtml(title) + '</h2>';
        html += '<button class="gd-keyboard-overlay-close" aria-label="' +
                escapeHtml(_gdT('kb_close_dismiss', 'Close')) +
                '" type="button">';
        html += '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" ' +
                'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" ' +
                'stroke-linejoin="round" aria-hidden="true">' +
                '<line x1="18" y1="6" x2="6" y2="18"></line>' +
                '<line x1="6" y1="6" x2="18" y2="18"></line>' +
                '</svg>';
        html += '</button>';
        html += '</div>';

        html += '<div class="gd-keyboard-overlay-body">';

        for (var g = 0; g < SHORTCUT_GROUPS.length; g++) {
            var group = SHORTCUT_GROUPS[g];
            html += '<div class="gd-keyboard-group">';
            html += '<h3>' + escapeHtml(_gdT(group.titleKey, group.titleFallback)) + '</h3>';
            html += '<dl>';
            for (var s = 0; s < group.shortcuts.length; s++) {
                var sc = group.shortcuts[s];
                if (sc.visible && !sc.visible()) continue;
                html += '<div class="gd-keyboard-row">';
                html += '<dt>';
                for (var k = 0; k < sc.keys.length; k++) {
                    if (k > 0) {
                        var sep = sc.separator != null ? sc.separator :
                            ' <span class="gd-keyboard-or">' +
                            escapeHtml(_gdT('kb_or', 'or')) + '</span> ';
                        html += sep;
                    }
                    html += '<kbd>' + escapeHtml(sc.keys[k]) + '</kbd>';
                }
                html += '</dt>';
                html += '<dd>' + escapeHtml(_gdT(sc.descKey, sc.descFallback)) + '</dd>';
                html += '</div>';
            }
            html += '</dl>';
            html += '</div>';
        }

        html += '</div></div>';

        el.innerHTML = html;
        return el;
    }

    function escapeHtml(str) {
        var div = document.createElement('div');
        div.appendChild(document.createTextNode(str));
        return div.innerHTML;
    }

    function showOverlay() {
        if (!overlay) {
            overlay = createOverlay();
            document.body.appendChild(overlay);

            // Close button
            var closeBtn = overlay.querySelector('.gd-keyboard-overlay-close');
            closeBtn.addEventListener('click', hideOverlay);

            // Click on backdrop
            overlay.addEventListener('click', function(e) {
                if (e.target === overlay) {
                    hideOverlay();
                }
            });
        }

        if (prefersReducedMotion()) {
            overlay.classList.add('gd-keyboard-overlay-visible');
        } else {
            // Force reflow before adding the class for animation
            void overlay.offsetWidth;
            overlay.classList.add('gd-keyboard-overlay-visible');
        }
        isOverlayOpen = true;

        // Focus the close button for keyboard users
        var closeBtn = overlay.querySelector('.gd-keyboard-overlay-close');
        if (closeBtn) closeBtn.focus();
    }

    function hideOverlay() {
        if (!overlay) return;
        overlay.classList.remove('gd-keyboard-overlay-visible');
        isOverlayOpen = false;
    }

    // ── Keyboard Event Handler ───────────────────────────────────────────

    function handleKeydown(e) {
        // When menu is open, handle all menu-related keys
        if (isMenuOpen) {
            if (e.key === 'Escape' || e.key === 'm' || e.key === 'n') {
                e.preventDefault();
                hideMenu();
                return;
            }
            // Delegate arrow keys and Enter to menu navigation
            handleMenuKeydown(e);
            return;
        }

        // When help overlay is open, handle Escape and toggle keys (h/?)
        if (isOverlayOpen) {
            if (e.key === 'Escape' || e.key === 'h' || e.key === '?') {
                e.preventDefault();
                hideOverlay();
            }
            return;
        }

        // Skip if user is typing in an input
        if (isTyping()) return;

        // Skip if modifier keys are held (allow browser/OS shortcuts)
        if (e.ctrlKey || e.metaKey || e.altKey) return;

        switch (e.key) {
            case '?':
            case 'h':
                e.preventDefault();
                showOverlay();
                break;

            case 's':
                e.preventDefault();
                focusSearch();
                break;

            // Note: '/' is handled by sidebar-filter.js when it's active.
            // When sidebar-filter is not present, we handle it here.
            case '/':
                // Only if sidebar-filter hasn't already handled it
                if (!document.querySelector('.sidebar-filter-input')) {
                    e.preventDefault();
                    focusSearch();
                }
                break;

            case '[':
                e.preventDefault();
                navigatePrev();
                break;

            case ']':
                e.preventDefault();
                navigateNext();
                break;

            case 'm':
            case 'n':
                e.preventDefault();
                showMenu();
                break;

            case 'q':
                e.preventDefault();
                navigateHome();
                break;

            case 'u':
                if (hasUserGuide()) {
                    e.preventDefault();
                    navigateUserGuide();
                }
                break;

            case 'r':
                if (hasReference()) {
                    e.preventDefault();
                    navigateReference();
                }
                break;

            case 'd':
                e.preventDefault();
                toggleDarkMode();
                break;

            case 'c':
                e.preventDefault();
                copyPage();
                break;

            case 'Escape':
                // Blur the active element
                if (document.activeElement && document.activeElement !== document.body) {
                    document.activeElement.blur();
                }
                break;
        }
    }

    // ── Navbar Button ────────────────────────────────────────────────

    /**
     * Create the keyboard shortcuts navbar button.
     * Uses the Lucide "keyboard" icon (MIT-licensed).
     */
    function createKeyboardButton() {
        var container = document.createElement('div');
        container.id = 'gd-keyboard-btn-container';

        var btn = document.createElement('button');
        btn.id = 'gd-keyboard-btn';
        btn.className = 'gd-keyboard-btn';
        btn.type = 'button';
        btn.setAttribute('aria-label',
            _gdT('kb_show_help', 'Show keyboard shortcuts'));
        btn.setAttribute('data-tippy-content',
            _gdT('kb_show_help', 'Show keyboard shortcuts'));
        btn.innerHTML =
            '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" ' +
            'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" ' +
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
            '<path d="M10 8h.01"/><path d="M12 12h.01"/>' +
            '<path d="M14 8h.01"/><path d="M16 12h.01"/>' +
            '<path d="M18 8h.01"/><path d="M6 8h.01"/>' +
            '<path d="M7 16h10"/><path d="M8 12h.01"/>' +
            '<rect width="20" height="16" x="2" y="4" rx="2"/>' +
            '</svg>';

        container.appendChild(btn);
        return container;
    }

    /**
     * Insert the keyboard button into the navbar.
     */
    function insertKeyboardButton() {
        // Insert into navbarCollapse; navbar-widgets.js will collect it
        // into the unified #gd-navbar-widgets container.
        var collapse = document.getElementById('navbarCollapse');
        if (!collapse) return;

        var container = createKeyboardButton();
        var navItem = document.createElement('li');
        navItem.className = 'nav-item';
        navItem.appendChild(container);

        // Append to navbarCollapse (the collector will move it)
        collapse.appendChild(navItem);

        // Click handler
        var btn = document.getElementById('gd-keyboard-btn');
        if (btn) {
            btn.addEventListener('click', function() {
                if (isOverlayOpen) {
                    hideOverlay();
                } else {
                    showOverlay();
                }
            });

            // Initialize tooltip directly — window.tippy is available from
            // Quarto's bundle before any include-after-body scripts run.
            if (window.tippy) {
                window.tippy(btn, {
                    content: btn.getAttribute('data-tippy-content'),
                    placement: 'bottom',
                    animation: 'shift-away',
                    duration: [200, 150],
                    delay: [0, 0],
                    arrow: true,
                });
            }
        }
    }

    // ── Initialization ───────────────────────────────────────────────────

    function init() {
        document.addEventListener('keydown', handleKeydown);
        insertKeyboardButton();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Expose menu API so the sidebar toggle button can reuse it
    window.__gdMenu = {
        show: showMenu,
        hide: hideMenu,
        isOpen: function() { return isMenuOpen; }
    };
})();

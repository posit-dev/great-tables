/**
 * Dark Mode Toggle for Great Docs
 *
 * Features:
 * - Toggle switch in the navbar
 * - System preference detection
 * - Persistent preference storage
 * - Smooth transitions
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

    const STORAGE_KEY = 'great-docs-theme';
    const DARK_CLASS = 'quarto-dark';
    const LIGHT_CLASS = 'quarto-light';

    /**
     * Get the user's system color scheme preference
     */
    function getSystemPreference() {
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return 'dark';
        }
        return 'light';
    }

    /**
     * Get the stored theme preference
     */
    function getStoredPreference() {
        try {
            return localStorage.getItem(STORAGE_KEY);
        } catch (e) {
            return null;
        }
    }

    /**
     * Store the theme preference
     */
    function setStoredPreference(theme) {
        try {
            localStorage.setItem(STORAGE_KEY, theme);
        } catch (e) {
            // localStorage not available
        }
    }

    /**
     * Get the current effective theme
     */
    function getCurrentTheme() {
        const stored = getStoredPreference();
        if (stored === 'dark' || stored === 'light') {
            return stored;
        }
        return getSystemPreference();
    }

    /**
     * Apply the theme to the document
     */
    function applyTheme(theme) {
        const html = document.documentElement;
        const body = document.body;

        if (theme === 'dark') {
            html.classList.add(DARK_CLASS);
            html.classList.remove(LIGHT_CLASS);
            body.classList.add(DARK_CLASS);
            body.classList.remove(LIGHT_CLASS);
            html.setAttribute('data-bs-theme', 'dark');
        } else {
            html.classList.add(LIGHT_CLASS);
            html.classList.remove(DARK_CLASS);
            body.classList.add(LIGHT_CLASS);
            body.classList.remove(DARK_CLASS);
            html.setAttribute('data-bs-theme', 'light');
        }

        // Update toggle button state
        updateToggleButton(theme);
    }

    /**
     * Update the toggle button appearance
     */
    function updateToggleButton(theme) {
        const toggle = document.getElementById('dark-mode-toggle');
        if (!toggle) return;

        const sunIcon = toggle.querySelector('.theme-icon-light');
        const moonIcon = toggle.querySelector('.theme-icon-dark');
        const newTooltip = theme === 'dark'
            ? _gdT('switch_to_light_mode', 'Switch to light mode')
            : _gdT('switch_to_dark_mode', 'Switch to dark mode');

        if (theme === 'dark') {
            toggle.setAttribute('aria-pressed', 'true');
            if (sunIcon) sunIcon.style.display = 'none';
            if (moonIcon) moonIcon.style.display = 'inline-block';
        } else {
            toggle.setAttribute('aria-pressed', 'false');
            if (sunIcon) sunIcon.style.display = 'inline-block';
            if (moonIcon) moonIcon.style.display = 'none';
        }

        // Update tooltip: use data-tippy-content to keep Tippy in sync
        // and avoid native browser tooltips (which appear after delay)
        toggle.setAttribute('data-tippy-content', newTooltip);
        toggle.removeAttribute('title');

        // Update existing Tippy instance content directly if present
        if (toggle._tippy) {
            toggle._tippy.setContent(newTooltip);
        }
    }

    /**
     * Toggle between light and dark themes
     */
    function toggleTheme() {
        const current = getCurrentTheme();
        const newTheme = current === 'dark' ? 'light' : 'dark';
        setStoredPreference(newTheme);
        applyTheme(newTheme);
    }

    /**
     * Create the toggle button HTML
     */
    function createToggleButton() {
        const container = document.createElement('div');
        container.id = 'dark-mode-toggle-container';
        container.innerHTML = `
            <button id="dark-mode-toggle"
                    class="dark-mode-toggle"
                    type="button"
                    role="switch"
                    aria-label="${_gdT('toggle_dark_mode', 'Toggle dark mode')}"
                    data-tippy-content="${_gdT('switch_to_dark_mode', 'Switch to dark mode')}">
                <span class="theme-icon-light" aria-hidden="true">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="5"></circle>
                        <line x1="12" y1="1" x2="12" y2="3"></line>
                        <line x1="12" y1="21" x2="12" y2="23"></line>
                        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                        <line x1="1" y1="12" x2="3" y2="12"></line>
                        <line x1="21" y1="12" x2="23" y2="12"></line>
                        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
                    </svg>
                </span>
                <span class="theme-icon-dark" aria-hidden="true" style="display: none;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                    </svg>
                </span>
            </button>
        `;
        return container;
    }

    /**
     * Insert the toggle button into the navbar
     */
    function insertToggleButton() {
        // Insert into navbarCollapse; navbar-widgets.js will collect it
        // into the unified #gd-navbar-widgets container.
        const collapse = document.getElementById('navbarCollapse');
        if (!collapse) return;

        const toggleContainer = createToggleButton();
        const navItem = document.createElement('li');
        navItem.className = 'nav-item';
        navItem.appendChild(toggleContainer);

        // Append to navbarCollapse (the collector will move it)
        var msAuto = collapse.querySelector('.navbar-nav.ms-auto');
        if (msAuto) {
            msAuto.insertBefore(navItem, msAuto.firstChild);
        } else {
            collapse.appendChild(navItem);
        }

        // Add click handler
        const toggle = document.getElementById('dark-mode-toggle');
        if (toggle) {
            toggle.addEventListener('click', toggleTheme);
        }
    }

    /**
     * Listen for system preference changes
     */
    function setupSystemPreferenceListener() {
        if (!window.matchMedia) return;

        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');

        mediaQuery.addEventListener('change', (e) => {
            // Only respond to system changes if user hasn't set a preference
            const stored = getStoredPreference();
            if (!stored) {
                applyTheme(e.matches ? 'dark' : 'light');
            }
        });
    }

    /**
     * Apply theme immediately to prevent flash
     */
    function applyInitialTheme() {
        const theme = getCurrentTheme();

        // Apply to html element immediately (before body is available)
        const html = document.documentElement;
        if (theme === 'dark') {
            html.classList.add(DARK_CLASS);
            html.classList.remove(LIGHT_CLASS);
            html.setAttribute('data-bs-theme', 'dark');
        } else {
            html.classList.add(LIGHT_CLASS);
            html.classList.remove(DARK_CLASS);
            html.setAttribute('data-bs-theme', 'light');
        }
    }

    /**
     * Fix the navbar dark-logo src from a <meta> tag.
     * Quarto's logo-dark config is ignored without a paired dark theme,
     * so both .light-content and .dark-content imgs point to the same file.
     * We read the correct dark logo path from <meta name="gd-logo-dark">
     * and patch the src at runtime.
     */
    function fixNavbarDarkLogo() {
        var meta = document.querySelector('meta[name="gd-logo-dark"]');
        if (!meta) return;
        var darkFilename = meta.getAttribute('content');
        if (!darkFilename) return;

        // Resolve the dark logo path relative to the light logo's directory,
        // so sub-pages (e.g. user-guide/page.html) get the correct "../" prefix.
        var lightImg = document.querySelector('.navbar-logo.light-content');
        var darkSrc = darkFilename;
        if (lightImg && lightImg.getAttribute('src')) {
            var lightSrc = lightImg.getAttribute('src');
            var lastSlash = lightSrc.lastIndexOf('/');
            if (lastSlash >= 0) {
                darkSrc = lightSrc.substring(0, lastSlash + 1) + darkFilename;
            }
        }

        document.querySelectorAll('.navbar-logo.dark-content').forEach(function(img) {
            img.src = darkSrc;
        });
    }

    /**
     * Initialize dark mode functionality
     */
    function init() {
        // Fix navbar dark logo src before applying theme
        fixNavbarDarkLogo();

        // Apply theme to body now that DOM is ready
        const theme = getCurrentTheme();
        applyTheme(theme);

        // Insert toggle button
        insertToggleButton();

        // Update toggle button to reflect current theme (must be after insertion)
        updateToggleButton(theme);

        // Setup system preference listener
        setupSystemPreferenceListener();
    }

    // Apply initial theme immediately to prevent flash of wrong theme
    applyInitialTheme();

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Expose API for external use
    window.greatDocsDarkMode = {
        toggle: toggleTheme,
        setTheme: function(theme) {
            if (theme === 'dark' || theme === 'light') {
                setStoredPreference(theme);
                applyTheme(theme);
            }
        },
        getTheme: getCurrentTheme,
        clearPreference: function() {
            try {
                localStorage.removeItem(STORAGE_KEY);
            } catch (e) {}
            applyTheme(getSystemPreference());
        }
    };
})();

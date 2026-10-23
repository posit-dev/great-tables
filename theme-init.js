// Early theme initialization to prevent flash of wrong theme
(function() {
    // When dark mode toggle is disabled, always use light mode
    var dmMeta = document.querySelector('meta[name="gd-dark-mode"]');
    var darkModeDisabled = dmMeta && dmMeta.getAttribute('content') === 'disabled';

    var stored = darkModeDisabled ? null : localStorage.getItem('great-docs-theme');
    var theme = stored || (darkModeDisabled ? 'light' : (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));
    var html = document.documentElement;

    if (theme === 'dark') {
        html.classList.add('quarto-dark');
        html.setAttribute('data-bs-theme', 'dark');
    } else {
        html.classList.add('quarto-light');
        html.setAttribute('data-bs-theme', 'light');
    }

    // Wide layout: apply the stored (or site default) width before first paint.
    // The layout only widens while .gd-wide-capable is present, i.e. at or
    // above the configured viewport width; wide-layout.js handles the toggle.
    var wideMeta = document.querySelector('meta[name="gd-wide-layout"]');
    if (wideMeta) {
        var storedWidth = null;
        try { storedWidth = localStorage.getItem('great-docs-width'); } catch (e) { /* unavailable */ }
        var width = storedWidth === 'wide' || storedWidth === 'normal'
            ? storedWidth
            : (wideMeta.getAttribute('data-default') === 'wide' ? 'wide' : 'normal');
        html.setAttribute('data-gd-width', width);
        // Suppress the width animation until wide-layout.js has loaded
        html.classList.add('gd-wide-instant');

        var minViewport = parseInt(wideMeta.getAttribute('data-min-viewport'), 10) || 1600;
        var wideMql = window.matchMedia('(min-width: ' + minViewport + 'px)');
        var syncWideCapable = function() {
            html.classList.toggle('gd-wide-capable', wideMql.matches);
        };
        syncWideCapable();
        if (wideMql.addEventListener) {
            wideMql.addEventListener('change', syncWideCapable);
        }
    }

    // Detect page type from URL for page-specific styling
    var path = window.location.pathname;
    var pageName = path.endsWith('/') || path.endsWith('/index.html') || path === '/' ? 'index' : null;
    if (!pageName) {
        var filename = path.split('/').pop().replace('.html', '');
        if (filename === 'index' || filename === '') {
            pageName = 'index';
        }
    }

    // Set page identifier on body when DOM is ready
    function setPageIdentifier() {
        if (pageName && document.body) {
            document.body.setAttribute('data-page', pageName);
        }
    }

    // Reveal the page once the DOM is parsed and after-body scripts have run.
    // The page is hidden by an inline <style> in the <head> (metadata.html)
    // that targets html:not(.theme-loaded).  A double requestAnimationFrame
    // ensures the browser has painted the changes from after-body scripts
    // (sidebar, dark-mode toggle, "On This Page", tags, etc.) before the
    // page becomes visible.
    function revealPage() {
        setPageIdentifier();
        requestAnimationFrame(function() {
            requestAnimationFrame(function() {
                html.classList.add('theme-loaded');
            });
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', revealPage);
    } else {
        revealPage();
    }
})();

// Early theme initialization to prevent flash of wrong theme
(function() {
    // When dark mode toggle is disabled, always use light mode
    var dmMeta = document.querySelector('meta[name="gd-dark-mode"]');
    var darkModeDisabled = dmMeta && dmMeta.getAttribute('content') === 'disabled';

    var stored = darkModeDisabled ? null : localStorage.getItem('great-docs-theme');
    var theme = stored || (darkModeDisabled ? 'light' : (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));
    var html = document.documentElement;

    // Hide body until theme is fully applied to prevent flash
    html.classList.add('theme-loading');

    if (theme === 'dark') {
        html.classList.add('quarto-dark');
        html.setAttribute('data-bs-theme', 'dark');
    } else {
        html.classList.add('quarto-light');
        html.setAttribute('data-bs-theme', 'light');
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

    // Reveal page once DOM is ready and styles are applied
    function revealPage() {
        setPageIdentifier();
        // Small delay to ensure CSS is processed
        requestAnimationFrame(function() {
            html.classList.remove('theme-loading');
            html.classList.add('theme-loaded');
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', revealPage);
    } else {
        revealPage();
    }
})();

/**
 * Copy Page Widget for Great Docs
 *
 * Provides two actions:
 * - "Copy as Markdown" — copies the page's .md content to clipboard
 * - "View as Markdown" — navigates to the .md version of the page
 *
 * The .md files are generated alongside .html files by the post-render script.
 */

(function() {
    'use strict';

    /**
     * Look up a translated string from the gd-i18n meta tag.
     */
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

    /**
     * Derive the .md URL from the current page URL.
     * e.g., /reference/GreatDocs.html -> /reference/GreatDocs.md
     *       /user-guide/quickstart.html -> /user-guide/quickstart.md
     */
    function getMdUrl() {
        var path = window.location.pathname;
        // Replace .html with .md
        if (path.endsWith('.html')) {
            return path.slice(0, -5) + '.md';
        }
        // For paths ending in / (index pages), try index.md
        if (path.endsWith('/')) {
            return path + 'index.md';
        }
        return path + '.md';
    }

    /**
     * Create and inject the copy-page widget.
     */
    function initCopyPage() {
        // Find the title block header to position the button
        var titleBlock = document.getElementById('title-block-header');
        if (!titleBlock) return;

        // Skip the Skills page (has its own layout)
        if (document.querySelector('.gd-skills-install')) return;

        // Skip the License page (has its own layout)
        if (document.body.classList.contains('gd-license-page')) return;

        // Skip the Tags index page
        if (document.body.classList.contains('gd-tags-index')) return;

        // Skip the Blog index page
        if (document.body.classList.contains('gd-blog-index')) return;

        // Create the widget container
        var widget = document.createElement('div');
        widget.className = 'gd-copy-page';
        widget.setAttribute('role', 'group');
        widget.setAttribute('aria-label', _gdT('page_actions', 'Page actions'));

        // Copy as Markdown button
        var copyBtn = document.createElement('button');
        copyBtn.className = 'gd-copy-page-btn gd-copy-md-btn';
        copyBtn.setAttribute('title', _gdT('copy_page_as_markdown', 'Copy page as Markdown'));
        copyBtn.setAttribute('aria-label', _gdT('copy_page_as_markdown', 'Copy page as Markdown'));
        copyBtn.innerHTML =
            '<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
            '<rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>' +
            '<path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>' +
            '</svg>' +
            '<span class="gd-copy-page-label">' + _gdT('copy_page', 'Copy page') + '</span>';

        // View as Markdown link
        var viewLink = document.createElement('a');
        viewLink.className = 'gd-copy-page-btn gd-view-md-btn';
        viewLink.href = getMdUrl();
        viewLink.setAttribute('title', _gdT('view_as_markdown', 'View as Markdown'));
        viewLink.setAttribute('aria-label', _gdT('view_page_as_markdown', 'View page as Markdown'));
        viewLink.innerHTML =
            '<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 208 128" fill="currentColor" aria-hidden="true">' +
            '<rect width="198" height="118" x="5" y="5" ry="10" stroke="currentColor" stroke-width="10" fill="none"/>' +
            '<path d="M30 98V30h20l20 25 20-25h20v68H90V59L70 84 50 59v39zm125 0l-30-33h20V30h20v35h20z"/>' +
            '</svg>';

        widget.appendChild(copyBtn);
        widget.appendChild(viewLink);

        // Insert before the title block
        titleBlock.parentNode.insertBefore(widget, titleBlock);

        // Pre-fetch the .md content so the clipboard write can happen
        // synchronously inside the click handler (preserving user activation).
        var mdUrl = getMdUrl();
        var cachedMd = null;

        fetch(mdUrl)
            .then(function(response) {
                if (!response.ok) throw new Error('not found');
                return response.text();
            })
            .then(function(text) { cachedMd = text; })
            .catch(function() { /* will show error on click */ });

        // Copy handler — writes from cache so clipboard API gets user activation
        copyBtn.addEventListener('click', function() {
            var label = copyBtn.querySelector('.gd-copy-page-label');
            var origText = label.textContent;

            if (!cachedMd) {
                    label.textContent = _gdT('error', 'Error');
                setTimeout(function() { label.textContent = origText; }, 2000);
                return;
            }

            navigator.clipboard.writeText(cachedMd)
                .then(function() {
                    label.textContent = _gdT('copied', 'Copied!');
                    copyBtn.classList.add('gd-copy-success');
                    setTimeout(function() {
                        label.textContent = origText;
                        copyBtn.classList.remove('gd-copy-success');
                    }, 2000);
                })
                .catch(function(err) {
                    console.warn('Copy page failed:', err);
                    label.textContent = _gdT('error', 'Error');
                    setTimeout(function() { label.textContent = origText; }, 2000);
                });
        });
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initCopyPage);
    } else {
        initCopyPage();
    }
})();

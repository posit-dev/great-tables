/**
 * Sidebar Smart Wrap for Great Docs
 *
 * Inserts <wbr> (word break opportunity) elements into long sidebar item
 * names so the browser can break lines at aesthetically pleasing points:
 *   - After dots:        store.DuckDBStore  →  break after each "."
 *   - After underscores: retrieve_bm25      →  break after "_"
 *   - After open paren:  connect()          →  break after "("
 *   - At camelCase:      DuckDBStore        →  break before uppercase runs
 *
 * The <wbr> tag is invisible and zero-width; the browser only uses it as a
 * line-break opportunity when the text overflows its container.
 */

(function () {
    'use strict';

    /**
     * Insert <wbr> elements at smart break points in a text node.
     *
     * Break opportunities are placed:
     *   1. After every "."  (module separators)
     *   2. After every "_"  (snake_case boundaries)
     *   3. After every "("  (before argument lists)
     *   4. Before a run of uppercase letters preceded by a lowercase letter
     *      (camelCase → camel + Case), but only when the run is followed by
     *      a lowercase letter (e.g. "DBStore" keeps "DB" together and breaks
     *      before "Store").
     *
     * The regex uses zero-width look-behind/ahead so the actual characters
     * are preserved in the output — only <wbr> tags are inserted.
     */
    function insertSmartBreaks(text) {
        // Split text at break-opportunity points.
        // The regex captures the delimiter so we can reassemble with <wbr>
        // after each delimiter character.
        //
        // Pattern pieces:
        //   ([._])          – capture a dot or underscore
        //   (\()            – capture an opening paren
        //   (?<=[a-z])(?=[A-Z])  – zero-width camelCase boundary
        //
        // We use a two-pass approach because JS regex has limited support
        // for look-behind in older runtimes.

        var result = document.createDocumentFragment();
        // Pattern: split around ".", "_", "(", and camelCase transitions
        // Two camelCase lookarounds:
        //   (?<=[a-z])(?=[A-Z])       – lowercase-to-uppercase: "Duck|DB"
        //   (?<=[A-Z])(?=[A-Z][a-z])  – end of acronym run:    "DB|Document"
        var parts = text.split(/([._()])|(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])/);
        // Filter out empty/undefined entries produced by the regex split
        var filtered = parts.filter(function (p) { return p !== undefined && p !== ''; });

        // Merge parentheses onto preceding tokens to prevent orphan ")" or "()"
        // e.g. ["directory", "(", ")"] → ["directory()"]
        var merged = [];
        for (var i = 0; i < filtered.length; i++) {
            if (filtered[i] === '(' && i + 1 < filtered.length && filtered[i + 1] === ')') {
                // "()" pair: attach to preceding token
                if (merged.length > 0) {
                    merged[merged.length - 1] += '()';
                } else {
                    merged.push('()');
                }
                i++; // skip the ")"
            } else if (filtered[i] === ')') {
                // lone ")": attach to preceding token
                if (merged.length > 0) {
                    merged[merged.length - 1] += ')';
                } else {
                    merged.push(')');
                }
            } else {
                merged.push(filtered[i]);
            }
        }

        // Final pass: for any token still longer than 10 characters (e.g.
        // all-lowercase names with no camelCase/separator break points),
        // insert a <wbr> every 10 characters as a fallback.
        var CHUNK = 10;
        for (var i = 0; i < merged.length; i++) {
            var token = merged[i];
            if (token.length > CHUNK) {
                for (var c = 0; c < token.length; c += CHUNK) {
                    if (c > 0) {
                        result.appendChild(document.createElement('wbr'));
                    }
                    result.appendChild(document.createTextNode(token.slice(c, c + CHUNK)));
                }
            } else {
                result.appendChild(document.createTextNode(token));
            }
            // Insert <wbr> between every pair of adjacent parts.
            if (i < merged.length - 1) {
                result.appendChild(document.createElement('wbr'));
            }
        }
        return result;
    }

    /**
     * Process all <span class="menu-text"> elements inside the sidebar.
     */
    function processSidebar() {
        var sidebar = document.getElementById('quarto-sidebar');
        if (!sidebar) return;

        var spans = sidebar.querySelectorAll('.menu-text');
        for (var i = 0; i < spans.length; i++) {
            var span = spans[i];
            var text = span.textContent;
            if (!text) continue;
            // Only process items that contain separator characters, camelCase /
            // acronym boundaries, or are simply too long to fit without wrapping.
            // Skip plain short words like "API", "Classes".
            var dominated = /[._()]/.test(text) || /[a-z][A-Z]/.test(text) || /[A-Z]{2,}[a-z]/.test(text);
            if (!dominated && text.length <= 10) continue;
            // Replace the text content with smart-break nodes
            var fragment = insertSmartBreaks(text);
            span.textContent = '';
            span.appendChild(fragment);
        }
    }

    /**
     * Disable sidebar section collapsing by stripping Bootstrap collapse
     * data attributes and ensuring all sections stay expanded.
     */
    function disableSidebarCollapse() {
        var sidebar = document.getElementById('quarto-sidebar');
        if (!sidebar) return;

        // Remove data-bs-toggle/target from all sidebar collapse triggers
        var triggers = sidebar.querySelectorAll('[data-bs-toggle="collapse"]');
        for (var i = 0; i < triggers.length; i++) {
            triggers[i].removeAttribute('data-bs-toggle');
            triggers[i].removeAttribute('data-bs-target');
            triggers[i].removeAttribute('aria-expanded');
            triggers[i].removeAttribute('role');
        }

        // Ensure all collapsible sections are permanently shown
        var sections = sidebar.querySelectorAll('ul.collapse.sidebar-section');
        for (var j = 0; j < sections.length; j++) {
            sections[j].classList.remove('collapse');
            sections[j].classList.add('show');
        }
    }

    // Run after DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            processSidebar();
            disableSidebarCollapse();
        });
    } else {
        processSidebar();
        disableSidebarCollapse();
    }
})();

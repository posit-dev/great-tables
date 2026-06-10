/**
 * Sidebar Filter for Great Docs
 *
 * Adds a search/filter input to the API reference sidebar for quickly
 * finding items in large APIs. Automatically enabled when there are
 * 20+ items in the sidebar (configurable via data attribute).
 */

(function() {
    'use strict';

    // Configuration
    const DEFAULT_MIN_ITEMS = 20;
    const DEBOUNCE_DELAY = 150;

    /**
     * Debounce function to limit filter execution rate
     */
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    /**
     * Count total sidebar items (links to API reference pages)
     */
    function countSidebarItems(sidebar) {
        const items = sidebar.querySelectorAll('.sidebar-item:not(.sidebar-item-section) .sidebar-link');
        return items.length;
    }

    /**
     * Create the filter input element
     */
    function createFilterInput() {
        const container = document.createElement('div');
        container.className = 'sidebar-filter-container';
        container.innerHTML = `
            <div class="sidebar-filter-wrapper">
                <input
                    type="text"
                    class="sidebar-filter-input"
                    placeholder="Filter API..."
                    aria-label="Filter API reference items"
                >
                <span class="sidebar-filter-icon">
                    <i class="bi bi-search"></i>
                </span>
                <button
                    class="sidebar-filter-clear"
                    type="button"
                    aria-label="Clear filter"
                    style="display: none;"
                >
                    <i class="bi bi-x-lg"></i>
                </button>
            </div>
            <div class="sidebar-filter-count" style="display: none;">
                <span class="filter-count-num">0</span> of <span class="filter-count-total">0</span> items
            </div>
        `;
        return container;
    }

    /**
     * Check if a sidebar item is a top-level navigation link (not inside a section)
     * These should not be filtered (e.g., "API" link)
     */
    function isTopLevelNavItem(item) {
        // Items inside a section (sidebar-item-section) are NOT top-level
        // Check if any ancestor is a sidebar-item-section
        let parent = item.parentElement;
        while (parent) {
            if (parent.classList && parent.classList.contains('sidebar-item-section')) {
                return false; // Inside a section, so not top-level
            }
            if (parent.classList && parent.classList.contains('sidebar-menu-container')) {
                break; // Reached the top of the sidebar
            }
            parent = parent.parentElement;
        }

        // This item is directly in the main sidebar list (not inside any section)
        return true;
    }

    /**
     * Check if we're on an API reference page (where the filter should show).
     * Returns true only for /reference/ pages that are NOT CLI reference pages.
     */
    function isApiReferencePage() {
        const path = window.location.pathname;
        return path.includes('/reference/') && !path.includes('/reference/cli/');
    }

    /**
     * Filter sidebar items based on search query
     */
    function filterSidebar(query, sidebar, countDisplay) {
        const normalizedQuery = query.toLowerCase().trim();
        const sections = sidebar.querySelectorAll('.sidebar-item-section');
        const allItems = sidebar.querySelectorAll('.sidebar-item:not(.sidebar-item-section)');

        // Separate top-level nav items from filterable items
        const topLevelNavItems = [];
        const filterableItems = [];

        allItems.forEach(item => {
            if (isTopLevelNavItem(item)) {
                topLevelNavItems.push(item);
            } else {
                filterableItems.push(item);
            }
        });

        let visibleCount = 0;
        const totalCount = filterableItems.length;

        // If query is empty, show everything
        if (!normalizedQuery) {
            filterableItems.forEach(item => {
                item.style.display = '';
                item.classList.remove('sidebar-filter-match');
            });
            sections.forEach(section => {
                section.style.display = '';
                // Restore original collapse state
                const collapseTarget = section.querySelector('.sidebar-section');
                if (collapseTarget && !collapseTarget.classList.contains('show')) {
                    // Keep collapsed sections collapsed
                }
            });
            // Top-level nav items are always visible
            topLevelNavItems.forEach(item => {
                item.style.display = '';
            });
            countDisplay.style.display = 'none';
            return;
        }

        // Filter items (excluding top-level nav items which are always visible)
        filterableItems.forEach(item => {
            const link = item.querySelector('.sidebar-link');
            const text = link ? link.textContent.toLowerCase() : '';
            const matches = text.includes(normalizedQuery);

            item.style.display = matches ? '' : 'none';
            item.classList.toggle('sidebar-filter-match', matches);

            if (matches) {
                visibleCount++;
            }
        });

        // Show/hide sections based on whether they have visible items
        sections.forEach(section => {
            const sectionItems = section.querySelectorAll('.sidebar-item:not(.sidebar-item-section)');
            const hasVisibleItems = Array.from(sectionItems).some(
                item => item.style.display !== 'none'
            );

            section.style.display = hasVisibleItems ? '' : 'none';

            // Expand sections that have matches
            if (hasVisibleItems) {
                const collapseTarget = section.querySelector('.sidebar-section');
                if (collapseTarget && !collapseTarget.classList.contains('show')) {
                    collapseTarget.classList.add('show');
                }
            }
        });

        // Update count display
        const countNum = countDisplay.querySelector('.filter-count-num');
        const countTotal = countDisplay.querySelector('.filter-count-total');
        countNum.textContent = visibleCount;
        countTotal.textContent = totalCount;
        countDisplay.style.display = '';
    }

    /**
     * Initialize the sidebar filter
     */
    function initSidebarFilter() {
        // Only show filter on API reference pages
        if (!isApiReferencePage()) {
            return;
        }

        // Find the sidebar
        const sidebar = document.getElementById('quarto-sidebar');
        if (!sidebar) {
            return;
        }

        // Check if we're on a reference page (has sidebar with API items)
        const sidebarMenu = sidebar.querySelector('.sidebar-menu-container');
        if (!sidebarMenu) {
            return;
        }

        // Get minimum items threshold from data attribute or use default
        const minItems = parseInt(
            document.body.dataset.sidebarFilterMinItems || DEFAULT_MIN_ITEMS,
            10
        );

        // Check if filtering is disabled
        if (document.body.dataset.sidebarFilterDisabled === 'true') {
            return;
        }

        // Count items and check threshold
        const itemCount = countSidebarItems(sidebar);
        if (itemCount < minItems) {
            return;
        }

        // Create and insert the filter input
        const filterContainer = createFilterInput();
        const menuContainer = sidebar.querySelector('.sidebar-menu-container');
        menuContainer.insertBefore(filterContainer, menuContainer.firstChild);

        // Get references to elements
        const input = filterContainer.querySelector('.sidebar-filter-input');
        const clearBtn = filterContainer.querySelector('.sidebar-filter-clear');
        const countDisplay = filterContainer.querySelector('.sidebar-filter-count');

        // Set total count
        const countTotal = countDisplay.querySelector('.filter-count-total');
        countTotal.textContent = itemCount;

        // Create debounced filter function
        const debouncedFilter = debounce((query) => {
            filterSidebar(query, sidebar, countDisplay);
        }, DEBOUNCE_DELAY);

        // Event listeners
        input.addEventListener('input', (e) => {
            const query = e.target.value;
            clearBtn.style.display = query ? '' : 'none';
            debouncedFilter(query);
        });

        clearBtn.addEventListener('click', () => {
            input.value = '';
            clearBtn.style.display = 'none';
            filterSidebar('', sidebar, countDisplay);
            input.focus();
        });

        // Keyboard shortcut: Escape to clear
        input.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                if (input.value) {
                    input.value = '';
                    clearBtn.style.display = 'none';
                    filterSidebar('', sidebar, countDisplay);
                } else {
                    input.blur();
                }
            }
        });

        // Global keyboard shortcut: "/" to focus filter (like GitHub)
        document.addEventListener('keydown', (e) => {
            // Don't trigger if user is typing in another input
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
                return;
            }

            if (e.key === '/' && !e.ctrlKey && !e.metaKey && !e.altKey) {
                e.preventDefault();
                input.focus();
                input.select();
            }
        });

        console.log(`Sidebar filter initialized (${itemCount} items)`);
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSidebarFilter);
    } else {
        initSidebarFilter();
    }
})();

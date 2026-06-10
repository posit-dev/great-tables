/**
 * GitHub Widget for Great-Docs
 *
 * A souped-up GitHub icon link with:
 * - Live star and fork counts
 * - Dropdown menu linking to repo, issues, PRs
 * - Caching to avoid API rate limits
 */

(function() {
    'use strict';

    // Configuration - will be set by data attributes
    let config = {
        owner: null,
        repo: null,
        cacheKey: 'great-docs-github-stats',
        cacheDuration: 4 * 60 * 60 * 1000 // 4 hours
    };

    /**
     * Initialize the GitHub widget
     */
    function initGitHubWidget() {
        const widget = document.getElementById('github-widget');
        if (!widget) return;

        config.owner = widget.dataset.owner;
        config.repo = widget.dataset.repo;

        if (!config.owner || !config.repo) {
            console.warn('GitHub widget: Missing owner or repo data attributes');
            return;
        }

        // Create the widget structure
        createWidgetStructure(widget);

        // Use build-time embedded stats if available, otherwise try API
        const embeddedStars = widget.dataset.stars;
        const embeddedForks = widget.dataset.forks;
        if (embeddedStars !== undefined && embeddedForks !== undefined) {
            updateStatsDisplay({
                stars: parseInt(embeddedStars, 10),
                forks: parseInt(embeddedForks, 10)
            });
        } else {
            fetchGitHubStats();
        }

        // Setup dropdown behavior
        setupDropdown(widget);
    }

    /**
     * Create the HTML structure for the widget
     */
    function createWidgetStructure(container) {
        const repoUrl = `https://github.com/${config.owner}/${config.repo}`;

        container.innerHTML = `
            <div class="gh-widget-trigger" role="button" aria-haspopup="true" aria-expanded="false" tabindex="0">
                <svg class="gh-icon" viewBox="0 0 16 16" width="20" height="20" fill="currentColor" aria-hidden="true">
                    <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
                </svg>
                <span class="gh-stats">
                    <span class="gh-stat gh-stars" title="Stars">
                        <svg viewBox="0 0 16 16" width="14" height="14" fill="currentColor" aria-hidden="true">
                            <path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/>
                        </svg>
                        <span class="gh-count" data-stat="stars">-</span>
                    </span>
                    <span class="gh-stat gh-forks" title="Forks">
                        <svg viewBox="0 0 16 16" width="14" height="14" fill="currentColor" aria-hidden="true">
                            <path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"/>
                        </svg>
                        <span class="gh-count" data-stat="forks">-</span>
                    </span>
                </span>
                <svg class="gh-dropdown-arrow" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" aria-hidden="true">
                    <path d="M4.427 7.427l3.396 3.396a.25.25 0 00.354 0l3.396-3.396A.25.25 0 0011.396 7H4.604a.25.25 0 00-.177.427z"/>
                </svg>
            </div>
            <div class="gh-dropdown" role="menu" aria-hidden="true">
                <a href="${repoUrl}" class="gh-dropdown-item" role="menuitem" target="_blank" rel="noopener">
                    <svg viewBox="0 0 16 16" width="16" height="16" fill="currentColor" aria-hidden="true">
                        <path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"/>
                    </svg>
                    Repository
                </a>
                <a href="${repoUrl}/issues" class="gh-dropdown-item" role="menuitem" target="_blank" rel="noopener">
                    <svg viewBox="0 0 16 16" width="16" height="16" fill="currentColor" aria-hidden="true">
                        <path d="M8 9.5a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"/>
                        <path fill-rule="evenodd" d="M8 0a8 8 0 100 16A8 8 0 008 0zM1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0z"/>
                    </svg>
                    Issues
                    <span class="gh-badge gh-issues-count" style="display: none;"></span>
                </a>
                <a href="${repoUrl}/pulls" class="gh-dropdown-item" role="menuitem" target="_blank" rel="noopener">
                    <svg viewBox="0 0 16 16" width="16" height="16" fill="currentColor" aria-hidden="true">
                        <path fill-rule="evenodd" d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z"/>
                    </svg>
                    Pull Requests
                    <span class="gh-badge gh-prs-count" style="display: none;"></span>
                </a>
                <div class="gh-dropdown-divider"></div>
                <a href="${repoUrl}" class="gh-dropdown-item" role="menuitem" target="_blank" rel="noopener">
                    <svg viewBox="0 0 16 16" width="16" height="16" fill="currentColor" aria-hidden="true">
                        <path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/>
                    </svg>
                    Add a Star
                    <span class="gh-badge gh-stars-total" style="display: none;"></span>
                </a>
                <a href="${repoUrl}/fork" class="gh-dropdown-item" role="menuitem" target="_blank" rel="noopener">
                    <svg viewBox="0 0 16 16" width="16" height="16" fill="currentColor" aria-hidden="true">
                        <path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"/>
                    </svg>
                    Create a Fork
                    <span class="gh-badge gh-forks-total" style="display: none;"></span>
                </a>
            </div>
        `;
    }

    /**
     * Fetch GitHub stats from API with caching
     */
    async function fetchGitHubStats() {
        const cacheKey = `${config.cacheKey}-${config.owner}-${config.repo}`;

        // Check cache first
        const cached = getFromCache(cacheKey);
        if (cached) {
            updateStatsDisplay(cached);
            return;
        }

        // Get stale cache (expired but still usable as fallback)
        const staleCache = getFromCache(cacheKey, true);

        try {
            // Fetch repo stats
            const repoResponse = await fetch(
                `https://api.github.com/repos/${config.owner}/${config.repo}`,
                {
                    headers: {
                        'Accept': 'application/vnd.github+json',
                        'X-GitHub-Api-Version': '2022-11-28'
                    }
                }
            );

            if (!repoResponse.ok) {
                throw new Error(`GitHub API error: ${repoResponse.status}`);
            }

            const repoData = await repoResponse.json();

            const stats = {
                stars: repoData.stargazers_count,
                forks: repoData.forks_count,
                openIssues: repoData.open_issues_count,
                timestamp: Date.now()
            };

            // Cache the results
            saveToCache(cacheKey, stats);

            // Update display
            updateStatsDisplay(stats);

        } catch (error) {
            console.warn('GitHub widget: Failed to fetch stats', error);
            // Use stale cache if available, otherwise show fallback
            if (staleCache) {
                updateStatsDisplay(staleCache);
            } else {
                updateStatsDisplay({ stars: '?', forks: '?' });
            }
        }
    }

    /**
     * Update the display with fetched stats
     */
    function updateStatsDisplay(stats) {
        const starsEl = document.querySelector('.gh-count[data-stat="stars"]');
        const forksEl = document.querySelector('.gh-count[data-stat="forks"]');
        const issuesBadge = document.querySelector('.gh-issues-count');
        const prsBadge = document.querySelector('.gh-prs-count');
        const starsTotalBadge = document.querySelector('.gh-stars-total');
        const forksTotalBadge = document.querySelector('.gh-forks-total');

        if (starsEl) starsEl.textContent = formatCount(stats.stars);
        if (forksEl) forksEl.textContent = formatCount(stats.forks);

        if (issuesBadge && stats.issues !== undefined) {
            issuesBadge.textContent = formatCount(stats.issues);
            issuesBadge.style.display = 'inline-flex';
        }

        if (prsBadge && stats.prs !== undefined) {
            prsBadge.textContent = formatCount(stats.prs);
            prsBadge.style.display = 'inline-flex';
        }

        if (starsTotalBadge && stats.stars !== undefined && stats.stars !== '?') {
            starsTotalBadge.textContent = formatCount(stats.stars);
            starsTotalBadge.style.display = 'inline-flex';
        }

        if (forksTotalBadge && stats.forks !== undefined && stats.forks !== '?') {
            forksTotalBadge.textContent = formatCount(stats.forks);
            forksTotalBadge.style.display = 'inline-flex';
        }
    }

    /**
     * Format large numbers (e.g., 1500 -> 1.5k)
     */
    function formatCount(num) {
        if (num === undefined || num === null || num === '?') return '?';
        if (num >= 1000000) {
            return (num / 1000000).toFixed(1).replace(/\.0$/, '') + 'M';
        }
        if (num >= 1000) {
            return (num / 1000).toFixed(1).replace(/\.0$/, '') + 'k';
        }
        return num.toString();
    }

    /**
     * Get cached data if not expired (or any cached data if allowStale is true)
     */
    function getFromCache(key, allowStale) {
        try {
            const data = localStorage.getItem(key);
            if (!data) return null;

            const parsed = JSON.parse(data);
            if (!allowStale && Date.now() - parsed.timestamp > config.cacheDuration) {
                return null;
            }
            return parsed;
        } catch (e) {
            return null;
        }
    }

    /**
     * Save data to cache
     */
    function saveToCache(key, data) {
        try {
            localStorage.setItem(key, JSON.stringify(data));
        } catch (e) {
            // Silently fail if localStorage is not available
        }
    }

    /**
     * Setup dropdown toggle behavior
     */
    function setupDropdown(widget) {
        const trigger = widget.querySelector('.gh-widget-trigger');
        const dropdown = widget.querySelector('.gh-dropdown');

        if (!trigger || !dropdown) return;

        // Toggle on click
        trigger.addEventListener('click', (e) => {
            e.stopPropagation();
            const isExpanded = trigger.getAttribute('aria-expanded') === 'true';
            trigger.setAttribute('aria-expanded', !isExpanded);
            dropdown.setAttribute('aria-hidden', isExpanded);
            widget.classList.toggle('gh-widget-open', !isExpanded);
        });

        // Toggle on Enter/Space key
        trigger.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                trigger.click();
            }
        });

        // Close on click outside
        document.addEventListener('click', (e) => {
            if (!widget.contains(e.target)) {
                trigger.setAttribute('aria-expanded', 'false');
                dropdown.setAttribute('aria-hidden', 'true');
                widget.classList.remove('gh-widget-open');
            }
        });

        // Close on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                trigger.setAttribute('aria-expanded', 'false');
                dropdown.setAttribute('aria-hidden', 'true');
                widget.classList.remove('gh-widget-open');
            }
        });
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initGitHubWidget);
    } else {
        initGitHubWidget();
    }
})();

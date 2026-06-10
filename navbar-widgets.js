/**
 * Navbar Widget Collector for Great Docs
 *
 * Consolidates all right-side navbar widgets (dark-mode toggle, keyboard
 * shortcuts button, GitHub icon/widget, and search) into a single flex
 * container (#gd-navbar-widgets) placed inside .quarto-navbar-tools.
 *
 * This guarantees uniform spacing (via CSS gap) and a predictable order
 * regardless of which widgets are enabled or the order scripts execute.
 *
 * Must be loaded AFTER the individual widget scripts (dark-mode-toggle.js,
 * keyboard-nav.js, github-widget.js) and is included unconditionally.
 */
(function () {
    'use strict';

    function ensureWrapper(containerFluid) {
        var wrapper = document.getElementById('gd-navbar-widgets');
        if (wrapper) return wrapper;

        wrapper = document.createElement('div');
        wrapper.id = 'gd-navbar-widgets';

        var tools = containerFluid.querySelector('.quarto-navbar-tools');
        if (tools) {
            tools.appendChild(wrapper);
        } else {
            containerFluid.appendChild(wrapper);
        }

        return wrapper;
    }

    function moveToWrapper(wrapper, el) {
        if (!el || wrapper.contains(el)) return;
        wrapper.appendChild(el);
    }

    function collect() {
        var containerFluid = document.querySelector('.navbar .container-fluid');
        if (!containerFluid) return;

        var wrapper = ensureWrapper(containerFluid);

        // 1. Dark-mode toggle (unwrap from its <li>)
        var toggleContainer = document.getElementById('dark-mode-toggle-container');
        if (toggleContainer) {
            var li = toggleContainer.closest('li.nav-item');
            moveToWrapper(wrapper, toggleContainer);
            if (li && !li.hasChildNodes()) li.remove();
        }

        // 2. Keyboard shortcuts button (unwrap from its <li>)
        var kbContainer = document.getElementById('gd-keyboard-btn-container');
        if (kbContainer) {
            var kbLi = kbContainer.closest('li.nav-item');
            moveToWrapper(wrapper, kbContainer);
            if (kbLi && !kbLi.hasChildNodes()) kbLi.remove();
        }

        // 3. GitHub icon — compact nav-item (unwrap the <a> from its <li>)
        var compactItem = containerFluid.querySelector(
            '#navbarCollapse .nav-item.compact'
        );
        if (compactItem) {
            var link = compactItem.querySelector('.nav-link');
            if (link) {
                link.classList.add('gd-navbar-icon');
                moveToWrapper(wrapper, link);
                compactItem.remove();
            }
        }

        // 4. GitHub widget — #github-widget (unwrap from its <li>)
        var ghWidget = document.getElementById('github-widget');
        if (ghWidget) {
            var ghLi = ghWidget.closest('li.nav-item');
            moveToWrapper(wrapper, ghWidget);
            if (ghLi && !ghLi.hasChildNodes()) ghLi.remove();
        }

        // 4b. Version selector — #gd-version-selector
        var vsWidget = document.getElementById('gd-version-selector');
        if (vsWidget) {
            moveToWrapper(wrapper, vsWidget);
        }

        // 5. Search button
        var search = document.getElementById('quarto-search');
        if (search) moveToWrapper(wrapper, search);

        // Clean up the now-empty ul.ms-auto
        var msAuto = containerFluid.querySelector(
            '#navbarCollapse .navbar-nav.ms-auto'
        );
        if (msAuto) {
            Array.prototype.forEach.call(
                msAuto.querySelectorAll('li.nav-item'),
                function (li) {
                    if (
                        !li.textContent.trim() &&
                        !li.querySelector('button, input, img, svg')
                    ) {
                        li.remove();
                    }
                }
            );
            if (msAuto.children.length === 0) msAuto.remove();
        }
    }

    function init() {
        collect();

        // Re-collect when widgets are injected after DOMContentLoaded
        var scheduled = false;
        function scheduleCollect() {
            if (scheduled) return;
            scheduled = true;
            requestAnimationFrame(function () {
                scheduled = false;
                collect();
            });
        }

        var navbarCollapse = document.getElementById('navbarCollapse');
        if (navbarCollapse) {
            var observer = new MutationObserver(scheduleCollect);
            observer.observe(navbarCollapse, { childList: true, subtree: true });
        }

        // Also watch container-fluid for widgets appended outside navbarCollapse
        // (e.g. version selector)
        var containerFluid = document.querySelector('.navbar .container-fluid');
        if (containerFluid) {
            var cfObserver = new MutationObserver(scheduleCollect);
            cfObserver.observe(containerFluid, { childList: true });
        }

        window.addEventListener('load', scheduleCollect, { once: true });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();

/**
 * Mobile sidebar toggle → menu overlay redirect.
 *
 * On mobile (< 992px) the sidebar toggle button in the Title Bar
 * (.quarto-btn-toggle) opens the polished menu overlay (same as the
 * 'm'/'n' keyboard shortcut) instead of Bootstrap's collapse sidebar.
 * This gives a smooth fade-in/slide, rounded card, backdrop blur, and
 * auto-scroll to the current page — matching the desktop overlay UX.
 */
(function () {
  "use strict";

  var mql = window.matchMedia("(max-width: 991.98px)");

  function intercept(e) {
    if (!mql.matches) return;           // desktop — let Bootstrap handle it
    if (!window.__gdMenu) return;       // keyboard-nav.js not loaded yet

    // Stop Bootstrap collapse and Quarto headroom toggle
    e.preventDefault();
    e.stopPropagation();

    if (window.__gdMenu.isOpen()) {
      window.__gdMenu.hide();
    } else {
      window.__gdMenu.show();
    }
  }

  function attach() {
    // The secondary-nav has two clickable elements: the <button> and
    // the <a> that wraps the title text.  Intercept both.
    var targets = document.querySelectorAll(
      ".quarto-secondary-nav .quarto-btn-toggle, " +
      ".quarto-secondary-nav a[data-bs-toggle='collapse']"
    );
    targets.forEach(function (el) {
      el.addEventListener("click", intercept, /* capture */ true);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", attach);
  } else {
    attach();
  }
})();

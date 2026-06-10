/**
 * Great Docs Mermaid Theme Fix
 *
 * Forces mermaid diagrams to use light theme colors in dark mode
 * by modifying the SVG's internal style block after Quarto renders.
 */

(function() {
    'use strict';

    function isDarkMode() {
        return document.documentElement.classList.contains('quarto-dark') ||
               document.body.classList.contains('quarto-dark');
    }

    /**
     * Light mode CSS rules to inject into SVG style blocks when in dark mode.
     * These override the dark theme colors mermaid generates.
     * Must be comprehensive to catch all text elements.
     */
    function getLightModeOverrides(id) {
        return '\n' +
            /* Universal text color overrides - catch everything */
            '#' + id + ' text { fill: #333 !important; }\n' +
            '#' + id + ' tspan { fill: #333 !important; }\n' +
            '#' + id + ' .label { fill: #333 !important; color: #333 !important; }\n' +
            '#' + id + ' .label text { fill: #333 !important; }\n' +
            '#' + id + ' .label tspan { fill: #333 !important; }\n' +
            '#' + id + ' span { color: #333 !important; }\n' +
            '#' + id + ' p { color: #333 !important; }\n' +
            '#' + id + ' div { color: #333 !important; }\n' +
            '#' + id + ' foreignObject { color: #333 !important; }\n' +
            '#' + id + ' foreignObject * { color: #333 !important; }\n' +
            /* Node-specific text */
            '#' + id + ' .nodeLabel { color: #333 !important; fill: #333 !important; }\n' +
            '#' + id + ' .nodeLabel p { color: #333 !important; }\n' +
            '#' + id + ' .nodeLabel span { color: #333 !important; }\n' +
            '#' + id + ' .node text { fill: #333 !important; }\n' +
            '#' + id + ' .node tspan { fill: #333 !important; }\n' +
            '#' + id + ' .node foreignObject div { color: #333 !important; }\n' +
            /* Node shapes */
            '#' + id + ' .node rect, #' + id + ' .node circle, #' + id + ' .node ellipse, #' + id + ' .node polygon, #' + id + ' .node path { fill: #ECECFF !important; stroke: #9370DB !important; }\n' +
            /* Edge labels */
            '#' + id + ' .edgeLabel { background-color: #e8e8e8 !important; color: #333 !important; }\n' +
            '#' + id + ' .edgeLabel rect { fill: #e8e8e8 !important; }\n' +
            '#' + id + ' .edgeLabel p { background-color: transparent !important; color: #333 !important; }\n' +
            '#' + id + ' .edgeLabel span { color: #333 !important; }\n' +
            '#' + id + ' .edgeLabel text { fill: #333 !important; }\n' +
            '#' + id + ' .edgeLabel tspan { fill: #333 !important; }\n' +
            '#' + id + ' .labelBkg { fill: #e8e8e8 !important; }\n' +
            /* Edges and arrows */
            '#' + id + ' .edgePath .path, #' + id + ' .flowchart-link { stroke: #333 !important; }\n' +
            '#' + id + ' .marker { fill: #333 !important; stroke: #333 !important; }\n' +
            '#' + id + ' .arrowheadPath { fill: #333 !important; }\n' +
            /* Clusters */
            '#' + id + ' .cluster rect { fill: #ffffde !important; stroke: #aaaa33 !important; }\n' +
            '#' + id + ' .cluster text { fill: #333 !important; }\n' +
            '#' + id + ' .cluster tspan { fill: #333 !important; }\n' +
            '#' + id + ' .cluster span { color: #333 !important; }\n' +
            '#' + id + ' .cluster-label text { fill: #333 !important; }\n' +
            '#' + id + ' .cluster-label span { color: #333 !important; }\n' +
            /* Sequence diagrams */
            '#' + id + ' .actor { fill: #ECECFF !important; stroke: #9370DB !important; }\n' +
            '#' + id + ' .actor text { fill: #333 !important; }\n' +
            '#' + id + ' .actor tspan { fill: #333 !important; }\n' +
            '#' + id + ' text.actor { fill: #333 !important; }\n' +
            '#' + id + ' text.actor > tspan { fill: #333 !important; }\n' +
            '#' + id + ' .messageText { fill: #333 !important; stroke: none !important; }\n' +
            '#' + id + ' .loopText { fill: #333 !important; }\n' +
            '#' + id + ' .loopText tspan { fill: #333 !important; }\n' +
            '#' + id + ' .noteText { fill: #333 !important; }\n' +
            '#' + id + ' .noteText tspan { fill: #333 !important; }\n' +
            '#' + id + ' .labelText { fill: #333 !important; color: #333 !important; }\n' +
            '#' + id + ' .labelText tspan { fill: #333 !important; }\n' +
            '#' + id + ' .sequenceNumber { fill: #fff !important; }\n' +
            '#' + id + ' line { stroke: #999 !important; }\n' +
            '#' + id + ' .messageLine0, #' + id + ' .messageLine1 { stroke: #333 !important; }\n' +
            '#' + id + ' .labelBox { fill: #ECECFF !important; stroke: #9370DB !important; }\n' +
            '#' + id + ' .loopLine { stroke: #9370DB !important; fill: #ECECFF !important; }\n' +
            /* State diagrams */
            '#' + id + ' g.stateGroup rect { fill: #ECECFF !important; stroke: #9370DB !important; }\n' +
            '#' + id + ' g.stateGroup text { fill: #333 !important; }\n' +
            '#' + id + ' g.stateGroup .state-title { fill: #333 !important; }\n' +
            '#' + id + ' .statediagram-state text { fill: #333 !important; }\n' +
            '#' + id + ' .transition { stroke: #333 !important; }\n' +
            /* Gantt */
            '#' + id + ' .section0, #' + id + ' .section2 { fill: #ECECFF !important; }\n' +
            '#' + id + ' .section1, #' + id + ' .section3 { fill: #f8f8f8 !important; }\n' +
            '#' + id + ' .taskText { fill: #333 !important; }\n' +
            '#' + id + ' .taskTextOutsideLeft, #' + id + ' .taskTextOutsideRight { fill: #333 !important; }\n' +
            '#' + id + ' .sectionTitle { fill: #333 !important; }\n' +
            '#' + id + ' .grid .tick line { stroke: #ccc !important; }\n' +
            '#' + id + ' .grid .tick text { fill: #333 !important; }\n' +
            '#' + id + ' .titleText { fill: #333 !important; }\n' +
            /* Pie */
            '#' + id + ' .pieCircle { stroke: #fff !important; }\n' +
            '#' + id + ' .pieTitleText { fill: #333 !important; }\n' +
            '#' + id + ' .pieOuterCircle { stroke: #333 !important; }\n' +
            '#' + id + ' .slice { stroke: #fff !important; }\n' +
            '#' + id + ' .legend text { fill: #333 !important; }\n' +
            /* Class diagrams */
            '#' + id + ' .classGroup rect { fill: #ECECFF !important; stroke: #9370DB !important; }\n' +
            '#' + id + ' .classGroup text { fill: #333 !important; }\n' +
            '#' + id + ' .classGroup tspan { fill: #333 !important; }\n' +
            '#' + id + ' .classGroup line, #' + id + ' .divider { stroke: #9370DB !important; }\n' +
            '#' + id + ' .relation { stroke: #333 !important; }\n' +
            '#' + id + ' .cardinality { fill: #333 !important; }\n' +
            '#' + id + ' .classLabel text { fill: #333 !important; }\n' +
            '#' + id + ' .classLabel tspan { fill: #333 !important; }\n' +
            /* Flowchart title */
            '#' + id + ' .flowchartTitleText { fill: #333 !important; }\n';
    }

    /**
     * Fix a single SVG by injecting light mode overrides and fixing inline styles
     */
    function fixSvg(svg) {
        if (!svg.id) return;
        if (svg.dataset.gdFixed === 'true') return;

        var styleEl = svg.querySelector('style');
        if (!styleEl) return;

        // Inject CSS overrides
        styleEl.textContent += getLightModeOverrides(svg.id);

        // Also directly fix inline styles on p, span, div elements
        // This handles cases where mermaid sets inline style="color: ..."
        var textElements = svg.querySelectorAll('p, span, div, .nodeLabel, .edgeLabel');
        textElements.forEach(function(el) {
            el.style.setProperty('color', '#333', 'important');
        });

        // Fix foreignObject children
        var foreignObjects = svg.querySelectorAll('foreignObject *');
        foreignObjects.forEach(function(el) {
            if (el.style) {
                el.style.setProperty('color', '#333', 'important');
            }
        });

        svg.dataset.gdFixed = 'true';
    }

    /**
     * Process all mermaid SVGs
     */
    function processAllSvgs() {
        var svgs = document.querySelectorAll('svg.mermaid-js, svg[id^="mermaid-"]');

        if (isDarkMode()) {
            svgs.forEach(fixSvg);
        }
    }

    /**
     * Set up observer for theme changes and new SVGs
     */
    function setupObserver() {
        var observer = new MutationObserver(function(mutations) {
            var shouldProcess = false;

            for (var i = 0; i < mutations.length; i++) {
                var mutation = mutations[i];
                if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
                    shouldProcess = true;
                    break;
                }
                if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                    shouldProcess = true;
                    break;
                }
            }

            if (shouldProcess) {
                setTimeout(processAllSvgs, 100);
            }
        });

        observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
        observer.observe(document.body, {
            attributes: true,
            attributeFilter: ['class'],
            childList: true,
            subtree: true
        });
    }

    function init() {
        setupObserver();

        function afterLoad() {
            setTimeout(processAllSvgs, 300);
            setTimeout(processAllSvgs, 1000);
        }

        if (document.readyState === 'complete') {
            afterLoad();
        } else {
            window.addEventListener('load', afterLoad);
        }
    }

    init();
})();

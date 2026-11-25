"use strict";(self.rspackChunk_JUPYTERLAB_CORE_OUTPUT=self.rspackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[5017],{74317(e,t,n){var r=n(34942),o=n.n(r),i=n(60278),s=(n.n(i))()(o());s.push([e.id,`/**
 * Copyright (c) 2014 The xterm.js authors. All rights reserved.
 * Copyright (c) 2012-2013, Christopher Jeffrey (MIT License)
 * https://github.com/chjj/term.js
 * @license MIT
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * Originally forked from (with the author's permission):
 *   Fabrice Bellard's javascript vt100 for jslinux:
 *   http://bellard.org/jslinux/
 *   Copyright (c) 2011 Fabrice Bellard
 *   The original design remains. The terminal itself
 *   has been extended to include xterm CSI codes, among
 *   other features.
 */

/**
 *  Default styles for xterm.js
 */

.xterm {
    cursor: text;
    position: relative;
    user-select: none;
    -ms-user-select: none;
    -webkit-user-select: none;
}

.xterm.focus,
.xterm:focus {
    outline: none;
}

.xterm .xterm-helpers {
    position: absolute;
    top: 0;
    /**
     * The z-index of the helpers must be higher than the canvases in order for
     * IMEs to appear on top.
     */
    z-index: 5;
}

.xterm .xterm-helper-textarea {
    padding: 0;
    border: 0;
    margin: 0;
    /* Move textarea out of the screen to the far left, so that the cursor is not visible */
    position: absolute;
    opacity: 0;
    left: -9999em;
    top: 0;
    width: 0;
    height: 0;
    z-index: -5;
    /** Prevent wrapping so the IME appears against the textarea at the correct position */
    white-space: nowrap;
    overflow: hidden;
    resize: none;
}

.xterm .composition-view {
    /* TODO: Composition position got messed up somewhere */
    background: #000;
    color: #FFF;
    display: none;
    position: absolute;
    white-space: nowrap;
    z-index: 1;
}

.xterm .composition-view.active {
    display: block;
}

.xterm .xterm-viewport {
    /* On OS X this is required in order for the scroll bar to appear fully opaque */
    background-color: #000;
    overflow-y: scroll;
    cursor: default;
    position: absolute;
    right: 0;
    left: 0;
    top: 0;
    bottom: 0;
}

.xterm .xterm-screen {
    position: relative;
}

.xterm .xterm-screen canvas {
    position: absolute;
    left: 0;
    top: 0;
}

.xterm .xterm-scroll-area {
    visibility: hidden;
}

.xterm-char-measure-element {
    display: inline-block;
    visibility: hidden;
    position: absolute;
    top: 0;
    left: -9999em;
    line-height: normal;
}

.xterm.enable-mouse-events {
    /* When mouse events are enabled (eg. tmux), revert to the standard pointer cursor */
    cursor: default;
}

.xterm.xterm-cursor-pointer,
.xterm .xterm-cursor-pointer {
    cursor: pointer;
}

.xterm.column-select.focus {
    /* Column selection mode */
    cursor: crosshair;
}

.xterm .xterm-accessibility:not(.debug),
.xterm .xterm-message {
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    right: 0;
    z-index: 10;
    color: transparent;
    pointer-events: none;
}

.xterm .xterm-accessibility-tree:not(.debug) *::selection {
  color: transparent;
}

.xterm .xterm-accessibility-tree {
  user-select: text;
  white-space: pre;
}

.xterm .live-region {
    position: absolute;
    left: -9999px;
    width: 1px;
    height: 1px;
    overflow: hidden;
}

.xterm-dim {
    /* Dim should not apply to background, so the opacity of the foreground color is applied
     * explicitly in the generated class and reset to 1 here */
    opacity: 1 !important;
}

.xterm-underline-1 { text-decoration: underline; }
.xterm-underline-2 { text-decoration: double underline; }
.xterm-underline-3 { text-decoration: wavy underline; }
.xterm-underline-4 { text-decoration: dotted underline; }
.xterm-underline-5 { text-decoration: dashed underline; }

.xterm-overline {
    text-decoration: overline;
}

.xterm-overline.xterm-underline-1 { text-decoration: overline underline; }
.xterm-overline.xterm-underline-2 { text-decoration: overline double underline; }
.xterm-overline.xterm-underline-3 { text-decoration: overline wavy underline; }
.xterm-overline.xterm-underline-4 { text-decoration: overline dotted underline; }
.xterm-overline.xterm-underline-5 { text-decoration: overline dashed underline; }

.xterm-strikethrough {
    text-decoration: line-through;
}

.xterm-screen .xterm-decoration-container .xterm-decoration {
	z-index: 6;
	position: absolute;
}

.xterm-screen .xterm-decoration-container .xterm-decoration.xterm-decoration-top-layer {
	z-index: 7;
}

.xterm-decoration-overview-ruler {
    z-index: 8;
    position: absolute;
    top: 0;
    right: 0;
    pointer-events: none;
}

.xterm-decoration-top {
    z-index: 2;
    position: relative;
}
`,"",{version:3,sources:["webpack://./../node_modules/@xterm/xterm/css/xterm.css"],names:[],mappings:"AAAA;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EA+BE;;AAEF;;EAEE;;AAEF;IACI,YAAY;IACZ,kBAAkB;IAClB,iBAAiB;IACjB,qBAAqB;IACrB,yBAAyB;AAC7B;;AAEA;;IAEI,aAAa;AACjB;;AAEA;IACI,kBAAkB;IAClB,MAAM;IACN;;;MAGE;IACF,UAAU;AACd;;AAEA;IACI,UAAU;IACV,SAAS;IACT,SAAS;IACT,uFAAuF;IACvF,kBAAkB;IAClB,UAAU;IACV,aAAa;IACb,MAAM;IACN,QAAQ;IACR,SAAS;IACT,WAAW;IACX,sFAAsF;IACtF,mBAAmB;IACnB,gBAAgB;IAChB,YAAY;AAChB;;AAEA;IACI,uDAAuD;IACvD,gBAAgB;IAChB,WAAW;IACX,aAAa;IACb,kBAAkB;IAClB,mBAAmB;IACnB,UAAU;AACd;;AAEA;IACI,cAAc;AAClB;;AAEA;IACI,gFAAgF;IAChF,sBAAsB;IACtB,kBAAkB;IAClB,eAAe;IACf,kBAAkB;IAClB,QAAQ;IACR,OAAO;IACP,MAAM;IACN,SAAS;AACb;;AAEA;IACI,kBAAkB;AACtB;;AAEA;IACI,kBAAkB;IAClB,OAAO;IACP,MAAM;AACV;;AAEA;IACI,kBAAkB;AACtB;;AAEA;IACI,qBAAqB;IACrB,kBAAkB;IAClB,kBAAkB;IAClB,MAAM;IACN,aAAa;IACb,mBAAmB;AACvB;;AAEA;IACI,oFAAoF;IACpF,eAAe;AACnB;;AAEA;;IAEI,eAAe;AACnB;;AAEA;IACI,0BAA0B;IAC1B,iBAAiB;AACrB;;AAEA;;IAEI,kBAAkB;IAClB,OAAO;IACP,MAAM;IACN,SAAS;IACT,QAAQ;IACR,WAAW;IACX,kBAAkB;IAClB,oBAAoB;AACxB;;AAEA;EACE,kBAAkB;AACpB;;AAEA;EACE,iBAAiB;EACjB,gBAAgB;AAClB;;AAEA;IACI,kBAAkB;IAClB,aAAa;IACb,UAAU;IACV,WAAW;IACX,gBAAgB;AACpB;;AAEA;IACI;8DAC0D;IAC1D,qBAAqB;AACzB;;AAEA,qBAAqB,0BAA0B,EAAE;AACjD,qBAAqB,iCAAiC,EAAE;AACxD,qBAAqB,+BAA+B,EAAE;AACtD,qBAAqB,iCAAiC,EAAE;AACxD,qBAAqB,iCAAiC,EAAE;;AAExD;IACI,yBAAyB;AAC7B;;AAEA,oCAAoC,mCAAmC,EAAE;AACzE,oCAAoC,0CAA0C,EAAE;AAChF,oCAAoC,wCAAwC,EAAE;AAC9E,oCAAoC,0CAA0C,EAAE;AAChF,oCAAoC,0CAA0C,EAAE;;AAEhF;IACI,6BAA6B;AACjC;;AAEA;CACC,UAAU;CACV,kBAAkB;AACnB;;AAEA;CACC,UAAU;AACX;;AAEA;IACI,UAAU;IACV,kBAAkB;IAClB,MAAM;IACN,QAAQ;IACR,oBAAoB;AACxB;;AAEA;IACI,UAAU;IACV,kBAAkB;AACtB",sourcesContent:['/**\n * Copyright (c) 2014 The xterm.js authors. All rights reserved.\n * Copyright (c) 2012-2013, Christopher Jeffrey (MIT License)\n * https://github.com/chjj/term.js\n * @license MIT\n *\n * Permission is hereby granted, free of charge, to any person obtaining a copy\n * of this software and associated documentation files (the "Software"), to deal\n * in the Software without restriction, including without limitation the rights\n * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n * copies of the Software, and to permit persons to whom the Software is\n * furnished to do so, subject to the following conditions:\n *\n * The above copyright notice and this permission notice shall be included in\n * all copies or substantial portions of the Software.\n *\n * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n * THE SOFTWARE.\n *\n * Originally forked from (with the author\'s permission):\n *   Fabrice Bellard\'s javascript vt100 for jslinux:\n *   http://bellard.org/jslinux/\n *   Copyright (c) 2011 Fabrice Bellard\n *   The original design remains. The terminal itself\n *   has been extended to include xterm CSI codes, among\n *   other features.\n */\n\n/**\n *  Default styles for xterm.js\n */\n\n.xterm {\n    cursor: text;\n    position: relative;\n    user-select: none;\n    -ms-user-select: none;\n    -webkit-user-select: none;\n}\n\n.xterm.focus,\n.xterm:focus {\n    outline: none;\n}\n\n.xterm .xterm-helpers {\n    position: absolute;\n    top: 0;\n    /**\n     * The z-index of the helpers must be higher than the canvases in order for\n     * IMEs to appear on top.\n     */\n    z-index: 5;\n}\n\n.xterm .xterm-helper-textarea {\n    padding: 0;\n    border: 0;\n    margin: 0;\n    /* Move textarea out of the screen to the far left, so that the cursor is not visible */\n    position: absolute;\n    opacity: 0;\n    left: -9999em;\n    top: 0;\n    width: 0;\n    height: 0;\n    z-index: -5;\n    /** Prevent wrapping so the IME appears against the textarea at the correct position */\n    white-space: nowrap;\n    overflow: hidden;\n    resize: none;\n}\n\n.xterm .composition-view {\n    /* TODO: Composition position got messed up somewhere */\n    background: #000;\n    color: #FFF;\n    display: none;\n    position: absolute;\n    white-space: nowrap;\n    z-index: 1;\n}\n\n.xterm .composition-view.active {\n    display: block;\n}\n\n.xterm .xterm-viewport {\n    /* On OS X this is required in order for the scroll bar to appear fully opaque */\n    background-color: #000;\n    overflow-y: scroll;\n    cursor: default;\n    position: absolute;\n    right: 0;\n    left: 0;\n    top: 0;\n    bottom: 0;\n}\n\n.xterm .xterm-screen {\n    position: relative;\n}\n\n.xterm .xterm-screen canvas {\n    position: absolute;\n    left: 0;\n    top: 0;\n}\n\n.xterm .xterm-scroll-area {\n    visibility: hidden;\n}\n\n.xterm-char-measure-element {\n    display: inline-block;\n    visibility: hidden;\n    position: absolute;\n    top: 0;\n    left: -9999em;\n    line-height: normal;\n}\n\n.xterm.enable-mouse-events {\n    /* When mouse events are enabled (eg. tmux), revert to the standard pointer cursor */\n    cursor: default;\n}\n\n.xterm.xterm-cursor-pointer,\n.xterm .xterm-cursor-pointer {\n    cursor: pointer;\n}\n\n.xterm.column-select.focus {\n    /* Column selection mode */\n    cursor: crosshair;\n}\n\n.xterm .xterm-accessibility:not(.debug),\n.xterm .xterm-message {\n    position: absolute;\n    left: 0;\n    top: 0;\n    bottom: 0;\n    right: 0;\n    z-index: 10;\n    color: transparent;\n    pointer-events: none;\n}\n\n.xterm .xterm-accessibility-tree:not(.debug) *::selection {\n  color: transparent;\n}\n\n.xterm .xterm-accessibility-tree {\n  user-select: text;\n  white-space: pre;\n}\n\n.xterm .live-region {\n    position: absolute;\n    left: -9999px;\n    width: 1px;\n    height: 1px;\n    overflow: hidden;\n}\n\n.xterm-dim {\n    /* Dim should not apply to background, so the opacity of the foreground color is applied\n     * explicitly in the generated class and reset to 1 here */\n    opacity: 1 !important;\n}\n\n.xterm-underline-1 { text-decoration: underline; }\n.xterm-underline-2 { text-decoration: double underline; }\n.xterm-underline-3 { text-decoration: wavy underline; }\n.xterm-underline-4 { text-decoration: dotted underline; }\n.xterm-underline-5 { text-decoration: dashed underline; }\n\n.xterm-overline {\n    text-decoration: overline;\n}\n\n.xterm-overline.xterm-underline-1 { text-decoration: overline underline; }\n.xterm-overline.xterm-underline-2 { text-decoration: overline double underline; }\n.xterm-overline.xterm-underline-3 { text-decoration: overline wavy underline; }\n.xterm-overline.xterm-underline-4 { text-decoration: overline dotted underline; }\n.xterm-overline.xterm-underline-5 { text-decoration: overline dashed underline; }\n\n.xterm-strikethrough {\n    text-decoration: line-through;\n}\n\n.xterm-screen .xterm-decoration-container .xterm-decoration {\n	z-index: 6;\n	position: absolute;\n}\n\n.xterm-screen .xterm-decoration-container .xterm-decoration.xterm-decoration-top-layer {\n	z-index: 7;\n}\n\n.xterm-decoration-overview-ruler {\n    z-index: 8;\n    position: absolute;\n    top: 0;\n    right: 0;\n    pointer-events: none;\n}\n\n.xterm-decoration-top {\n    z-index: 2;\n    position: relative;\n}\n'],sourceRoot:""}]),n.d(t,{},{A:s})},98384(e,t,n){var r=n(34942),o=n.n(r),i=n(60278),s=(n.n(i))()(o());s.push([e.id,`/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-ClearData-dialog {
  min-width: 400px;
}

.jp-ClearData-container {
  padding: 10px 0;
}

.jp-ClearData-option {
  display: flex;
  align-items: center;
  margin: 12px 0;
}

.jp-ClearData-option label {
  margin-left: 8px;
  cursor: pointer;
}

/* Enhanced warning styles */
.jp-ClearData-warning-box {
  display: flex;
  background-color: var(--jp-warn-color1);
  border: 1px solid var(--jp-warn-color1);
  border-radius: 4px;
  padding: 12px;
  margin: 0 0 16px 0;
  align-items: flex-start;
}

.jp-ClearData-warning-icon {
  font-size: 24px;
  margin-right: 12px;
  flex-shrink: 0;
  color: var(--jp-warn-color0);
}

.jp-ClearData-warning-text {
  flex: 1;
  color: var(--md-grey-900);
}

.jp-ClearData-warning-title {
  font-weight: bold;
  display: block;
  margin-bottom: 8px;
}

.jp-ClearData-warning-text ul {
  margin: 8px 0 4px 0;
  padding-left: 24px;
}

.jp-ClearData-warning-text p {
  margin: 4px 0;
}

.jp-ClearData-reload-notice {
  margin-top: 16px;
  color: var(--jp-ui-font-color2);
  font-size: 0.9em;
}

.jp-ClearData-unavailable {
  color: var(--jp-ui-font-color2);
  font-style: italic;
}

/* About dialog version list */
.jp-About-versionList {
  list-style: none;
  padding: 0;
  margin: 4px 0 0;
  font-size: 0.85em;
  color: var(--jp-ui-font-color2);
}
`,"",{version:3,sources:["webpack://./../packages/application-extension/style/base.css"],names:[],mappings:"AAAA;;;8EAG8E;;AAE9E;EACE,gBAAgB;AAClB;;AAEA;EACE,eAAe;AACjB;;AAEA;EACE,aAAa;EACb,mBAAmB;EACnB,cAAc;AAChB;;AAEA;EACE,gBAAgB;EAChB,eAAe;AACjB;;AAEA,4BAA4B;AAC5B;EACE,aAAa;EACb,uCAAuC;EACvC,uCAAuC;EACvC,kBAAkB;EAClB,aAAa;EACb,kBAAkB;EAClB,uBAAuB;AACzB;;AAEA;EACE,eAAe;EACf,kBAAkB;EAClB,cAAc;EACd,4BAA4B;AAC9B;;AAEA;EACE,OAAO;EACP,yBAAyB;AAC3B;;AAEA;EACE,iBAAiB;EACjB,cAAc;EACd,kBAAkB;AACpB;;AAEA;EACE,mBAAmB;EACnB,kBAAkB;AACpB;;AAEA;EACE,aAAa;AACf;;AAEA;EACE,gBAAgB;EAChB,+BAA+B;EAC/B,gBAAgB;AAClB;;AAEA;EACE,+BAA+B;EAC/B,kBAAkB;AACpB;;AAEA,8BAA8B;AAC9B;EACE,gBAAgB;EAChB,UAAU;EACV,eAAe;EACf,iBAAiB;EACjB,+BAA+B;AACjC",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n\n.jp-ClearData-dialog {\n  min-width: 400px;\n}\n\n.jp-ClearData-container {\n  padding: 10px 0;\n}\n\n.jp-ClearData-option {\n  display: flex;\n  align-items: center;\n  margin: 12px 0;\n}\n\n.jp-ClearData-option label {\n  margin-left: 8px;\n  cursor: pointer;\n}\n\n/* Enhanced warning styles */\n.jp-ClearData-warning-box {\n  display: flex;\n  background-color: var(--jp-warn-color1);\n  border: 1px solid var(--jp-warn-color1);\n  border-radius: 4px;\n  padding: 12px;\n  margin: 0 0 16px 0;\n  align-items: flex-start;\n}\n\n.jp-ClearData-warning-icon {\n  font-size: 24px;\n  margin-right: 12px;\n  flex-shrink: 0;\n  color: var(--jp-warn-color0);\n}\n\n.jp-ClearData-warning-text {\n  flex: 1;\n  color: var(--md-grey-900);\n}\n\n.jp-ClearData-warning-title {\n  font-weight: bold;\n  display: block;\n  margin-bottom: 8px;\n}\n\n.jp-ClearData-warning-text ul {\n  margin: 8px 0 4px 0;\n  padding-left: 24px;\n}\n\n.jp-ClearData-warning-text p {\n  margin: 4px 0;\n}\n\n.jp-ClearData-reload-notice {\n  margin-top: 16px;\n  color: var(--jp-ui-font-color2);\n  font-size: 0.9em;\n}\n\n.jp-ClearData-unavailable {\n  color: var(--jp-ui-font-color2);\n  font-style: italic;\n}\n\n/* About dialog version list */\n.jp-About-versionList {\n  list-style: none;\n  padding: 0;\n  margin: 4px 0 0;\n  font-size: 0.85em;\n  color: var(--jp-ui-font-color2);\n}\n"],sourceRoot:""}]),n.d(t,{},{A:s})},29396(e,t,n){var r=n(34942),o=n.n(r),i=n(60278),s=(n.n(i))()(o());s.push([e.id,`/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-KernelStatus {
  display: flex;
  align-items: center;
  justify-content: center;
}

.jp-KernelStatus-icon-container {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.jp-KernelStatus-spinner,
.jp-KernelStatus-success,
.jp-KernelStatus-error,
.jp-KernelStatus-none,
.jp-KernelStatus svg {
  width: 16px;
  height: 16px;
}

/* Loading state */
.jp-KernelStatus-spinner {
  transform-origin: center;
  animation: spin 1s linear infinite;
  color: var(--jp-brand-color1);
}

.jp-KernelStatus-spinner-track {
  opacity: 0.25;
}

.jp-KernelStatus-spinner-path {
  opacity: 0.75;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* Success state */
.jp-KernelStatus-success {
  color: var(--jp-success-color1);
}

/* Error state */
.jp-KernelStatus-error {
  color: var(--jp-error-color1);
}

/* No kernel state (e.g. after a shutdown) uses JupyterLab's circleEmptyIcon,
   which is already a muted, theme-aware ring (via its \`jp-icon3\` class), so no
   color override is needed here. */

/* Busy state */
.jp-KernelStatus-busy {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2px;
}

.jp-KernelStatus-busy-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: var(--jp-brand-color1);
  animation: pulse 1.4s infinite ease-in-out;
}

.jp-KernelStatus-busy-dot:nth-child(1) {
  animation-delay: -0.32s;
}

.jp-KernelStatus-busy-dot:nth-child(2) {
  animation-delay: -0.16s;
}

.jp-KernelStatus .jp-KernelStatus-busy-dot {
  width: 4px;
  height: 4px;
}

@keyframes pulse {
  0%,
  80%,
  100% {
    transform: scale(0);
    opacity: 0.5;
  }
  40% {
    transform: scale(1);
    opacity: 1;
  }
}

.jp-KernelStatus-idle .jp-KernelStatus-text {
  color: var(--jp-success-color1);
}

.jp-KernelStatus-busy .jp-KernelStatus-text {
  color: var(--jp-brand-color1);
}

.jp-KernelStatus-error .jp-KernelStatus-text {
  color: var(--jp-error-color1);
}

.jp-KernelStatus-widget {
  padding: 2px 8px;
  height: 24px;
}
`,"",{version:3,sources:["webpack://./../packages/apputils-extension/style/base.css"],names:[],mappings:"AAAA;;;8EAG8E;;AAE9E;EACE,aAAa;EACb,mBAAmB;EACnB,uBAAuB;AACzB;;AAEA;EACE,kBAAkB;EAClB,aAAa;EACb,mBAAmB;EACnB,uBAAuB;AACzB;;AAEA;;;;;EAKE,WAAW;EACX,YAAY;AACd;;AAEA,kBAAkB;AAClB;EACE,wBAAwB;EACxB,kCAAkC;EAClC,6BAA6B;AAC/B;;AAEA;EACE,aAAa;AACf;;AAEA;EACE,aAAa;AACf;;AAEA;EACE;IACE,uBAAuB;EACzB;EACA;IACE,yBAAyB;EAC3B;AACF;;AAEA,kBAAkB;AAClB;EACE,+BAA+B;AACjC;;AAEA,gBAAgB;AAChB;EACE,6BAA6B;AAC/B;;AAEA;;mCAEmC;;AAEnC,eAAe;AACf;EACE,aAAa;EACb,mBAAmB;EACnB,uBAAuB;EACvB,QAAQ;AACV;;AAEA;EACE,UAAU;EACV,WAAW;EACX,kBAAkB;EAClB,wCAAwC;EACxC,0CAA0C;AAC5C;;AAEA;EACE,uBAAuB;AACzB;;AAEA;EACE,uBAAuB;AACzB;;AAEA;EACE,UAAU;EACV,WAAW;AACb;;AAEA;EACE;;;IAGE,mBAAmB;IACnB,YAAY;EACd;EACA;IACE,mBAAmB;IACnB,UAAU;EACZ;AACF;;AAEA;EACE,+BAA+B;AACjC;;AAEA;EACE,6BAA6B;AAC/B;;AAEA;EACE,6BAA6B;AAC/B;;AAEA;EACE,gBAAgB;EAChB,YAAY;AACd",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n\n.jp-KernelStatus {\n  display: flex;\n  align-items: center;\n  justify-content: center;\n}\n\n.jp-KernelStatus-icon-container {\n  position: relative;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n}\n\n.jp-KernelStatus-spinner,\n.jp-KernelStatus-success,\n.jp-KernelStatus-error,\n.jp-KernelStatus-none,\n.jp-KernelStatus svg {\n  width: 16px;\n  height: 16px;\n}\n\n/* Loading state */\n.jp-KernelStatus-spinner {\n  transform-origin: center;\n  animation: spin 1s linear infinite;\n  color: var(--jp-brand-color1);\n}\n\n.jp-KernelStatus-spinner-track {\n  opacity: 0.25;\n}\n\n.jp-KernelStatus-spinner-path {\n  opacity: 0.75;\n}\n\n@keyframes spin {\n  from {\n    transform: rotate(0deg);\n  }\n  to {\n    transform: rotate(360deg);\n  }\n}\n\n/* Success state */\n.jp-KernelStatus-success {\n  color: var(--jp-success-color1);\n}\n\n/* Error state */\n.jp-KernelStatus-error {\n  color: var(--jp-error-color1);\n}\n\n/* No kernel state (e.g. after a shutdown) uses JupyterLab's circleEmptyIcon,\n   which is already a muted, theme-aware ring (via its `jp-icon3` class), so no\n   color override is needed here. */\n\n/* Busy state */\n.jp-KernelStatus-busy {\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  gap: 2px;\n}\n\n.jp-KernelStatus-busy-dot {\n  width: 6px;\n  height: 6px;\n  border-radius: 50%;\n  background-color: var(--jp-brand-color1);\n  animation: pulse 1.4s infinite ease-in-out;\n}\n\n.jp-KernelStatus-busy-dot:nth-child(1) {\n  animation-delay: -0.32s;\n}\n\n.jp-KernelStatus-busy-dot:nth-child(2) {\n  animation-delay: -0.16s;\n}\n\n.jp-KernelStatus .jp-KernelStatus-busy-dot {\n  width: 4px;\n  height: 4px;\n}\n\n@keyframes pulse {\n  0%,\n  80%,\n  100% {\n    transform: scale(0);\n    opacity: 0.5;\n  }\n  40% {\n    transform: scale(1);\n    opacity: 1;\n  }\n}\n\n.jp-KernelStatus-idle .jp-KernelStatus-text {\n  color: var(--jp-success-color1);\n}\n\n.jp-KernelStatus-busy .jp-KernelStatus-text {\n  color: var(--jp-brand-color1);\n}\n\n.jp-KernelStatus-error .jp-KernelStatus-text {\n  color: var(--jp-error-color1);\n}\n\n.jp-KernelStatus-widget {\n  padding: 2px 8px;\n  height: 24px;\n}\n"],sourceRoot:""}]),n.d(t,{},{A:s})},95996(e,t,n){var r=n(34942),o=n.n(r),i=n(60278),s=(n.n(i))()(o());s.push([e.id,`/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
`,"",{version:3,sources:["webpack://./../packages/apputils/style/base.css"],names:[],mappings:"AAAA;;;8EAG8E",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n"],sourceRoot:""}]),n.d(t,{},{A:s})},55942(e,t,n){var r=n(34942),o=n.n(r),i=n(60278),s=(n.n(i))()(o());s.push([e.id,`/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
`,"",{version:3,sources:["webpack://./../packages/notebook-application-extension/style/base.css"],names:[],mappings:"AAAA;;;8EAG8E",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n"],sourceRoot:""}]),n.d(t,{},{A:s})},87486(e,t,n){var r=n(95292),o=n.n(r),i=n(49893),s=n.n(i),a=n(9383),l=n.n(a),A=n(56884),p=n.n(A),c=n(99088),u=n.n(c),d=n(27997),h=n.n(d),m=n(74317),x={};x.styleTagTransform=h(),x.setAttributes=p(),x.insert=l().bind(null,"head"),x.domAPI=s(),x.insertStyleElement=u(),o()(m.A,x),m.A&&m.A.locals&&m.A.locals},16863(e,t,n){n.d(t,{main:()=>w});var r=n(77326),o=n(66840),i=n(49884);n(19894),n(89277),n(59344),n(47568),n(20550),n(14640),n(2645),n(66156),n(71462),n(48175),n(5207),n(50301),n(92045),n(93712),n(88551),n(58119),n(7939),n(71670),n(66029),n(88055),n(85317),n(69471),n(17704),n(98419),n(39601),n(63562),n(38257),n(26021),n(53555),n(91749),n(738),n(89821),n(45536),n(93992),n(99713),n(59158),n(21462),n(43684),n(313),n(41315),n(28114),n(52400),n(66009);var s=n(95292),a=n.n(s),l=n(49893),A=n.n(l),p=n(9383),c=n.n(p),u=n(56884),d=n.n(u),h=n(99088),m=n.n(h),x=n(27997),f=n.n(x),C=n(98384),y={};y.styleTagTransform=f(),y.setAttributes=d(),y.insert=c().bind(null,"head"),y.domAPI=A(),y.insertStyleElement=m(),a()(C.A,y),C.A&&C.A.locals&&C.A.locals;var b=n(95996),E={};E.styleTagTransform=f(),E.setAttributes=d(),E.insert=c().bind(null,"head"),E.domAPI=A(),E.insertStyleElement=m(),a()(b.A,E),b.A&&b.A.locals&&b.A.locals;var B=n(29396),j={};j.styleTagTransform=f(),j.setAttributes=d(),j.insert=c().bind(null,"head"),j.domAPI=A(),j.insertStyleElement=m(),a()(B.A,j),B.A&&B.A.locals&&B.A.locals;var g=n(55942),_={};_.styleTagTransform=f(),_.setAttributes=d(),_.insert=c().bind(null,"head"),_.domAPI=A(),_.insertStyleElement=m(),a()(g.A,_),g.A&&g.A.locals&&g.A.locals;let v=["@jupyterlab/application-extension:logo","@jupyterlab/application-extension:main","@jupyterlab/application-extension:tree-resolver","@jupyterlab/application-extension:router","@jupyterlab/apputils-extension:licenses-client","@jupyterlab/apputils-extension:announcements","@jupyterlab/apputils-extension:resolver","@jupyterlab/docmanager-extension:download","@jupyterlab/filebrowser-extension:download","@jupyterlab/filebrowser-extension:share-file","@jupyterlab/help-extension:about","@jupyterlab/lsp-extension:plugin","@jupyterlab/services-extension:config-section-manager","@jupyterlab/services-extension:connection-status","@jupyterlab/services-extension:default-drive","@jupyterlab/services-extension:event-manager","@jupyterlab/services-extension:kernel-manager","@jupyterlab/services-extension:kernel-spec-manager","@jupyterlab/services-extension:nbconvert-manager","@jupyterlab/services-extension:session-manager","@jupyterlab/services-extension:setting-manager","@jupyterlab/services-extension:user-manager","@jupyterlab/services-extension:workspace-manager","@jupyterlab/translation:translator","@jupyterlite/notebook-application-extension:logo","@jupyterlite/notebook-application-extension:notify-commands"];async function I(e,t){try{let n=(await window._JUPYTERLAB[e].get(t))();return n.__scope__=e,n}catch(n){throw console.warn(`Failed to create module: package: ${e}; module: ${t}`),n}}async function w(){let e=[],t=[],s=[],a=[],l=[],A=JSON.parse(o.PageConfig.getOption("federated_extensions")),p=new Set;function*c(t){let n;for(let r of Array.isArray(n=t.hasOwnProperty("__esModule")?t.default:t)?n:[n])o.PageConfig.Extension.isDisabled(r.id)||v.includes(r.id)||v.includes(r.id.split(":")[0])||(e.push({...r,extension:t.__scope__}),yield r)}A.forEach(e=>{e.extension&&(p.add(e.name),s.push(I(e.name,e.extension))),e.mimeExtension&&(p.add(e.name),a.push(I(e.name,e.mimeExtension))),e.style&&l.push(I(e.name,e.style))});let u=[];if(!p.has("@jupyterlab/json-extension"))try{let e=n(28746);for(let t of(e.__scope__="@jupyterlab/json-extension",c(e)))u.push(t)}catch(e){console.error(e)}if(!p.has("@jupyterlab/javascript-extension"))try{let e=n(4162);for(let t of(e.__scope__="@jupyterlab/javascript-extension",c(e)))u.push(t)}catch(e){console.error(e)}if(!p.has("@jupyterlab/mermaid-extension"))try{let e=n(9675);for(let t of(e.__scope__="@jupyterlab/mermaid-extension",c(e)))u.push(t)}catch(e){console.error(e)}if(!p.has("@jupyterlab/pdf-extension"))try{let e=n(52334);for(let t of(e.__scope__="@jupyterlab/pdf-extension",c(e)))u.push(t)}catch(e){console.error(e)}if(!p.has("@jupyterlab/vega5-extension"))try{let e=n(37826);for(let t of(e.__scope__="@jupyterlab/vega5-extension",c(e)))u.push(t)}catch(e){console.error(e)}if((await Promise.allSettled(a)).forEach(e=>{if("fulfilled"===e.status)for(let t of c(e.value))u.push(t);else console.error(e.reason)}),!p.has("@jupyterlab/application-extension"))try{let e=n(93822);for(let n of(e.__scope__="@jupyterlab/application-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/apputils-extension"))try{let e=n(19450);for(let n of(e.__scope__="@jupyterlab/apputils-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/audio-extension"))try{let e=n(56478);for(let n of(e.__scope__="@jupyterlab/audio-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/cell-toolbar-extension"))try{let e=n(13226);for(let n of(e.__scope__="@jupyterlab/cell-toolbar-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/celltags-extension"))try{let e=n(42470);for(let n of(e.__scope__="@jupyterlab/celltags-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/codemirror-extension"))try{let e=n(59018);for(let n of(e.__scope__="@jupyterlab/codemirror-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/completer-extension"))try{let e=n(5188);for(let n of(e.__scope__="@jupyterlab/completer-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/console-extension"))try{let e=n(15080);for(let n of(e.__scope__="@jupyterlab/console-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/csvviewer-extension"))try{let e=n(42754);for(let n of(e.__scope__="@jupyterlab/csvviewer-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/docmanager-extension"))try{let e=n(91346);for(let n of(e.__scope__="@jupyterlab/docmanager-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/documentsearch-extension"))try{let e=n(75986);for(let n of(e.__scope__="@jupyterlab/documentsearch-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/filebrowser-extension"))try{let e=n(4166);for(let n of(e.__scope__="@jupyterlab/filebrowser-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/fileeditor-extension"))try{let e=n(88226);for(let n of(e.__scope__="@jupyterlab/fileeditor-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/help-extension"))try{let e=n(29898);for(let n of(e.__scope__="@jupyterlab/help-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/htmlviewer-extension"))try{let e=n(56766);for(let n of(e.__scope__="@jupyterlab/htmlviewer-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/imageviewer-extension"))try{let e=n(6712);for(let n of(e.__scope__="@jupyterlab/imageviewer-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/inspector-extension"))try{let e=n(87636);for(let n of(e.__scope__="@jupyterlab/inspector-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/launcher-extension"))try{let e=n(93922);for(let n of(e.__scope__="@jupyterlab/launcher-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/logconsole-extension"))try{let e=n(3718);for(let n of(e.__scope__="@jupyterlab/logconsole-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/lsp-extension"))try{let e=n(3900);for(let n of(e.__scope__="@jupyterlab/lsp-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/mainmenu-extension"))try{let e=n(70074);for(let n of(e.__scope__="@jupyterlab/mainmenu-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/markdownviewer-extension"))try{let e=n(5110);for(let n of(e.__scope__="@jupyterlab/markdownviewer-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/markedparser-extension"))try{let e=n(74058);for(let n of(e.__scope__="@jupyterlab/markedparser-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/mathjax-extension"))try{let e=n(9264);for(let n of(e.__scope__="@jupyterlab/mathjax-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/mermaid-extension"))try{let e=n(6032);for(let n of(e.__scope__="@jupyterlab/mermaid-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/metadataform-extension"))try{let e=n(56250);for(let n of(e.__scope__="@jupyterlab/metadataform-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/notebook-extension"))try{let e=n(39102);for(let n of(e.__scope__="@jupyterlab/notebook-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/rendermime-extension"))try{let e=n(70106);for(let n of(e.__scope__="@jupyterlab/rendermime-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/running-extension"))try{let e=n(88176);for(let n of(e.__scope__="@jupyterlab/running-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/services-extension"))try{let e=n(21810);for(let n of(e.__scope__="@jupyterlab/services-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/settingeditor-extension"))try{let e=n(66952);for(let n of(e.__scope__="@jupyterlab/settingeditor-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/shortcuts-extension"))try{let e=n(70523);for(let n of(e.__scope__="@jupyterlab/shortcuts-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/statusbar-extension"))try{let e=n(8036);for(let n of(e.__scope__="@jupyterlab/statusbar-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/terminal-extension"))try{let e=n(15734);for(let n of(e.__scope__="@jupyterlab/terminal-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/theme-dark-extension"))try{let e=n(28702);for(let n of(e.__scope__="@jupyterlab/theme-dark-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/theme-dark-high-contrast-extension"))try{let e=n(79694);for(let n of(e.__scope__="@jupyterlab/theme-dark-high-contrast-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/theme-light-extension"))try{let e=n(46826);for(let n of(e.__scope__="@jupyterlab/theme-light-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/toc-extension"))try{let e=n(33268);for(let n of(e.__scope__="@jupyterlab/toc-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/tooltip-extension"))try{let e=n(62612);for(let n of(e.__scope__="@jupyterlab/tooltip-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/translation-extension"))try{let e=n(47444);for(let n of(e.__scope__="@jupyterlab/translation-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/ui-components-extension"))try{let e=n(70732);for(let n of(e.__scope__="@jupyterlab/ui-components-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/video-extension"))try{let e=n(6040);for(let n of(e.__scope__="@jupyterlab/video-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlab/workspaces-extension"))try{let e=n(16002);for(let n of(e.__scope__="@jupyterlab/workspaces-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlite/application-extension"))try{let e=n(71903);for(let n of(e.__scope__="@jupyterlite/application-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlite/apputils-extension"))try{let e=n(14235);for(let n of(e.__scope__="@jupyterlite/apputils-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlite/notebook-application-extension"))try{let e=n(5383);for(let n of(e.__scope__="@jupyterlite/notebook-application-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!p.has("@jupyterlite/services-extension"))try{let e=n(80795);for(let n of(e.__scope__="@jupyterlite/services-extension",c(e)))t.push(n)}catch(e){console.error(e)}(await Promise.allSettled(s)).forEach(e=>{if("fulfilled"===e.status)for(let n of c(e.value))t.push(n);else console.error(e.reason)}),(await Promise.allSettled(l)).filter(({status:e})=>"rejected"===e).forEach(({reason:e})=>{console.error(e)});let d=new i.PluginRegistry;d.registerPlugins(t);let h=n(247).IServiceManager,m=await d.resolveRequiredService(h),x=new r.JupyterLab({pluginRegistry:d,mimeExtensions:u,serviceManager:m,availablePlugins:e});x.name=o.PageConfig.getOption("appName")||"JupyterLite","true"===(o.PageConfig.getOption("exposeAppInBrowser")||"").toLowerCase()&&(window.jupyterapp=x),await x.start({bubblingKeydown:!0}),await x.restored}}}]);
//# sourceMappingURL=5017.76fb193.js.map
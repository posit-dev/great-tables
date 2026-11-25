"use strict";(self.rspackChunk_JUPYTERLAB_CORE_OUTPUT=self.rspackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[6941],{87624(o,n,e){var t=e(95292),a=e.n(t),A=e(49893),r=e.n(A),i=e(9383),l=e.n(i),p=e(56884),s=e.n(p),d=e(99088),c=e.n(d),C=e(27997),b=e.n(C),E=e(46698),u={};u.styleTagTransform=b(),u.setAttributes=s(),u.insert=l().bind(null,"head"),u.domAPI=r(),u.insertStyleElement=c(),a()(E.A,u),E.A&&E.A.locals&&E.A.locals},46698(o,n,e){var t=e(34942),a=e.n(t),A=e(60278),r=e.n(A),i=e(99866),l=r()(a());l.i(i.A),l.push([o.id,`/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
  Document oriented look for the notebook.
  This includes changes to the look and feel of the JupyterLab Notebook
  component like:
  - scrollbar to the right of the page
  - drop shadow on the notebook
  - smaller empty space at the bottom of the notebook
  - compact view on mobile
*/

/* Make the notebook take up the full width of the page when jp-mod-fullwidth is set */

body[data-notebook='notebooks']
  .jp-NotebookPanel.jp-mod-fullwidth
  .jp-WindowedPanel-outer {
  padding-left: unset;
  padding-right: unset !important;
  width: unset;
}

/* Keep the notebook centered on the page */

body[data-notebook='notebooks'] .jp-NotebookPanel-toolbar {
  padding-left: calc(calc(100% - var(--jp-notebook-max-width)) * 0.5);
  padding-right: calc(calc(100% - var(--jp-notebook-max-width)) * 0.5);
}

body[data-notebook='notebooks'] .jp-WindowedPanel-outer {
  width: unset !important;
  padding-top: unset;
  padding-left: calc(calc(100% - var(--jp-notebook-max-width)) * 0.5);
  padding-right: calc(
    calc(
        100% - var(--jp-notebook-max-width) - var(--jp-notebook-padding-offset)
      ) * 0.5
  ) !important;
  background: var(--jp-layout-color2);
}

body[data-notebook='notebooks'] .jp-WindowedPanel-inner {
  margin-top: var(--jp-notebook-toolbar-margin-bottom);
  /* Adjustments for the extra top and bottom notebook padding */
  margin-bottom: calc(4 * var(--jp-notebook-padding));
}

body[data-notebook='notebooks'] .jp-Notebook-cell {
  background: var(--jp-layout-color0);
}

/* Empty space at the bottom of the notebook (similar to classic) */
body[data-notebook='notebooks']
  .jp-Notebook.jp-mod-scrollPastEnd
  .jp-WindowedPanel-outer::after {
  min-height: 100px;
}

/* Fix background colors */

body[data-notebook='notebooks'] .jp-WindowedPanel-outer > * {
  background: var(--jp-layout-color0);
}

body[data-notebook='notebooks']
  .jp-Notebook.jp-mod-commandMode
  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
  background: var(--jp-layout-color0) !important;
}

body[data-notebook='notebooks']
  .jp-Notebook
  .jp-Notebook-cell:not(:first-child)::before {
  content: ' ';
  height: 100%;
  position: absolute;
  top: 0;
  width: 11px;
}

/* Cell toolbar adjustments */

body[data-notebook='notebooks'] .jp-cell-toolbar {
  background: unset;
  box-shadow: unset;
}

/** first code cell on mobile
    (keep the selector above the media query)
*/
body[data-notebook='notebooks']
  .jp-CodeCell[data-windowed-list-index='0']
  .jp-cell-toolbar {
  top: unset;
}

@media only screen and (max-width: 760px) {
  /* first code cell on mobile */
  body[data-notebook='notebooks']
    .jp-CodeCell[data-windowed-list-index='0']
    .jp-cell-toolbar {
    top: var(--jp-notebook-padding);
  }

  body[data-notebook='notebooks'] .jp-MarkdownCell .jp-cell-toolbar,
  body[data-notebook='notebooks'] .jp-RawCell .jp-cell-toolbar {
    top: calc(0.5 * var(--jp-notebook-padding));
  }
}

/* Tweak the notebook footer (to add a new cell) */
body[data-notebook='notebooks'] .jp-Notebook-footer {
  background: unset;
  width: 100%;
  margin-left: unset;
}

/* Mobile View */

body[data-format='mobile'] .jp-NotebookCheckpoint {
  display: none;
}

body[data-format='mobile'] .jp-WindowedPanel-outer > *:first-child {
  margin-top: 0;
}

body[data-format='mobile'] .jp-ToolbarButton .jp-DebuggerBugButton {
  display: none;
}

body[data-notebook='notebooks'] .jp-WindowedPanel-viewport {
  background: var(--jp-layout-color0);
  box-shadow: var(--jp-elevation-z4);

  /* Extra padding at the top and bottom so the notebook looks nicer */
  padding-top: calc(2 * var(--jp-notebook-padding));
  padding-bottom: calc(2 * var(--jp-notebook-padding));
}

/* Notebook box shadow */

body[data-notebook='notebooks']
  .jp-Notebook
  > *:first-child:last-child::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  box-shadow: 0px 0px 12px 1px var(--jp-shadow-umbra-color);
}

/* Additional customizations of the components on the notebook page */

.jp-NotebookKernelLogo {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  text-align: center;
  margin-right: 8px;
}

.jp-NotebookKernelLogo img {
  max-width: 28px;
  max-height: 28px;
  display: flex;
}

.jp-NotebookKernelStatus {
  margin: 0;
  font-weight: normal;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  font-family: var(--jp-ui-font-family);
  line-height: var(--jp-private-title-panel-height);
  padding-left: var(--jp-kernel-status-padding);
  padding-right: var(--jp-kernel-status-padding);
}

.jp-NotebookKernelStatus-error {
  background-color: var(--jp-error-color0);
}

.jp-NotebookKernelStatus-warn {
  background-color: var(--jp-warn-color0);
}

.jp-NotebookKernelStatus-info {
  background-color: var(--jp-info-color0);
}

.jp-NotebookKernelStatus-fade {
  animation: 0.5s fade-out forwards;
}

.jp-NotebookTrustedStatus {
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  margin-top: 4px;
  margin-bottom: 4px;
  border: solid 1px var(--jp-border-color2);
  cursor: help;
}

.jp-NotebookTrustedStatus-not-trusted {
  cursor: pointer;
}

@keyframes fade-out {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

#jp-title h1 {
  cursor: pointer;
  font-size: 18px;
  margin: 0;
  font-weight: normal;
  color: var(--jp-ui-font-color0);
  font-family: var(--jp-ui-font-family);
  line-height: calc(1.5 * var(--jp-private-title-panel-height));
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}

#jp-title h1:hover {
  background: var(--jp-layout-color2);
}

.jp-NotebookCheckpoint {
  font-size: 14px;
  margin-left: 5px;
  margin-right: 5px;
  font-weight: normal;
  color: var(--jp-ui-font-color0);
  font-family: var(--jp-ui-font-family);
  line-height: calc(1.5 * var(--jp-private-title-panel-height));
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}

.jp-skiplink {
  position: absolute;
  top: -100em;
}

.jp-skiplink:focus-within {
  position: absolute;
  z-index: 10000;
  top: 0;
  left: 46%;
  margin: 0 auto;
  padding: 1em;
  width: 15%;
  box-shadow: var(--jp-elevation-z4);
  border-radius: 4px;
  background: var(--jp-layout-color0);
  text-align: center;
}

.jp-skiplink:focus-within a {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}
`,"",{version:3,sources:["webpack://./../node_modules/@jupyter-notebook/notebook-extension/style/base.css"],names:[],mappings:"AAAA;;;;8EAI8E;;AAI9E;;;;;;;;CAQC;;AAED,sFAAsF;;AAEtF;;;EAGE,mBAAmB;EACnB,+BAA+B;EAC/B,YAAY;AACd;;AAEA,2CAA2C;;AAE3C;EACE,mEAAmE;EACnE,oEAAoE;AACtE;;AAEA;EACE,uBAAuB;EACvB,kBAAkB;EAClB,mEAAmE;EACnE;;;;cAIY;EACZ,mCAAmC;AACrC;;AAEA;EACE,oDAAoD;EACpD,8DAA8D;EAC9D,mDAAmD;AACrD;;AAEA;EACE,mCAAmC;AACrC;;AAEA,mEAAmE;AACnE;;;EAGE,iBAAiB;AACnB;;AAEA,0BAA0B;;AAE1B;EACE,mCAAmC;AACrC;;AAEA;;;EAGE,8CAA8C;AAChD;;AAEA;;;EAGE,YAAY;EACZ,YAAY;EACZ,kBAAkB;EAClB,MAAM;EACN,WAAW;AACb;;AAEA,6BAA6B;;AAE7B;EACE,iBAAiB;EACjB,iBAAiB;AACnB;;AAEA;;CAEC;AACD;;;EAGE,UAAU;AACZ;;AAEA;EACE,8BAA8B;EAC9B;;;IAGE,+BAA+B;EACjC;;EAEA;;IAEE,2CAA2C;EAC7C;AACF;;AAEA,kDAAkD;AAClD;EACE,iBAAiB;EACjB,WAAW;EACX,kBAAkB;AACpB;;AAEA,gBAAgB;;AAEhB;EACE,aAAa;AACf;;AAEA;EACE,aAAa;AACf;;AAEA;EACE,aAAa;AACf;;AAEA;EACE,mCAAmC;EACnC,kCAAkC;;EAElC,oEAAoE;EACpE,iDAAiD;EACjD,oDAAoD;AACtD;;AAEA,wBAAwB;;AAExB;;;EAGE,WAAW;EACX,kBAAkB;EAClB,MAAM;EACN,SAAS;EACT,OAAO;EACP,QAAQ;EACR,yDAAyD;AAC3D;;AAEA,qEAAqE;;AAErE;EACE,cAAc;EACd,aAAa;EACb,mBAAmB;EACnB,kBAAkB;EAClB,iBAAiB;AACnB;;AAEA;EACE,eAAe;EACf,gBAAgB;EAChB,aAAa;AACf;;AAEA;EACE,SAAS;EACT,mBAAmB;EACnB,kCAAkC;EAClC,+BAA+B;EAC/B,qCAAqC;EACrC,iDAAiD;EACjD,6CAA6C;EAC7C,8CAA8C;AAChD;;AAEA;EACE,wCAAwC;AAC1C;;AAEA;EACE,uCAAuC;AACzC;;AAEA;EACE,uCAAuC;AACzC;;AAEA;EACE,iCAAiC;AACnC;;AAEA;EACE,mCAAmC;EACnC,+BAA+B;EAC/B,eAAe;EACf,kBAAkB;EAClB,yCAAyC;EACzC,YAAY;AACd;;AAEA;EACE,eAAe;AACjB;;AAEA;EACE;IACE,UAAU;EACZ;EACA;IACE,UAAU;EACZ;AACF;;AAEA;EACE,eAAe;EACf,eAAe;EACf,SAAS;EACT,mBAAmB;EACnB,+BAA+B;EAC/B,qCAAqC;EACrC,6DAA6D;EAC7D,uBAAuB;EACvB,gBAAgB;EAChB,mBAAmB;AACrB;;AAEA;EACE,mCAAmC;AACrC;;AAEA;EACE,eAAe;EACf,gBAAgB;EAChB,iBAAiB;EACjB,mBAAmB;EACnB,+BAA+B;EAC/B,qCAAqC;EACrC,6DAA6D;EAC7D,uBAAuB;EACvB,gBAAgB;EAChB,mBAAmB;AACrB;;AAEA;EACE,kBAAkB;EAClB,WAAW;AACb;;AAEA;EACE,kBAAkB;EAClB,cAAc;EACd,MAAM;EACN,SAAS;EACT,cAAc;EACd,YAAY;EACZ,UAAU;EACV,kCAAkC;EAClC,kBAAkB;EAClB,mCAAmC;EACnC,kBAAkB;AACpB;;AAEA;EACE,0BAA0B;EAC1B,mCAAmC;AACrC",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n|\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n\n@import './variables.css';\n\n/**\n  Document oriented look for the notebook.\n  This includes changes to the look and feel of the JupyterLab Notebook\n  component like:\n  - scrollbar to the right of the page\n  - drop shadow on the notebook\n  - smaller empty space at the bottom of the notebook\n  - compact view on mobile\n*/\n\n/* Make the notebook take up the full width of the page when jp-mod-fullwidth is set */\n\nbody[data-notebook='notebooks']\n  .jp-NotebookPanel.jp-mod-fullwidth\n  .jp-WindowedPanel-outer {\n  padding-left: unset;\n  padding-right: unset !important;\n  width: unset;\n}\n\n/* Keep the notebook centered on the page */\n\nbody[data-notebook='notebooks'] .jp-NotebookPanel-toolbar {\n  padding-left: calc(calc(100% - var(--jp-notebook-max-width)) * 0.5);\n  padding-right: calc(calc(100% - var(--jp-notebook-max-width)) * 0.5);\n}\n\nbody[data-notebook='notebooks'] .jp-WindowedPanel-outer {\n  width: unset !important;\n  padding-top: unset;\n  padding-left: calc(calc(100% - var(--jp-notebook-max-width)) * 0.5);\n  padding-right: calc(\n    calc(\n        100% - var(--jp-notebook-max-width) - var(--jp-notebook-padding-offset)\n      ) * 0.5\n  ) !important;\n  background: var(--jp-layout-color2);\n}\n\nbody[data-notebook='notebooks'] .jp-WindowedPanel-inner {\n  margin-top: var(--jp-notebook-toolbar-margin-bottom);\n  /* Adjustments for the extra top and bottom notebook padding */\n  margin-bottom: calc(4 * var(--jp-notebook-padding));\n}\n\nbody[data-notebook='notebooks'] .jp-Notebook-cell {\n  background: var(--jp-layout-color0);\n}\n\n/* Empty space at the bottom of the notebook (similar to classic) */\nbody[data-notebook='notebooks']\n  .jp-Notebook.jp-mod-scrollPastEnd\n  .jp-WindowedPanel-outer::after {\n  min-height: 100px;\n}\n\n/* Fix background colors */\n\nbody[data-notebook='notebooks'] .jp-WindowedPanel-outer > * {\n  background: var(--jp-layout-color0);\n}\n\nbody[data-notebook='notebooks']\n  .jp-Notebook.jp-mod-commandMode\n  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {\n  background: var(--jp-layout-color0) !important;\n}\n\nbody[data-notebook='notebooks']\n  .jp-Notebook\n  .jp-Notebook-cell:not(:first-child)::before {\n  content: ' ';\n  height: 100%;\n  position: absolute;\n  top: 0;\n  width: 11px;\n}\n\n/* Cell toolbar adjustments */\n\nbody[data-notebook='notebooks'] .jp-cell-toolbar {\n  background: unset;\n  box-shadow: unset;\n}\n\n/** first code cell on mobile\n    (keep the selector above the media query)\n*/\nbody[data-notebook='notebooks']\n  .jp-CodeCell[data-windowed-list-index='0']\n  .jp-cell-toolbar {\n  top: unset;\n}\n\n@media only screen and (max-width: 760px) {\n  /* first code cell on mobile */\n  body[data-notebook='notebooks']\n    .jp-CodeCell[data-windowed-list-index='0']\n    .jp-cell-toolbar {\n    top: var(--jp-notebook-padding);\n  }\n\n  body[data-notebook='notebooks'] .jp-MarkdownCell .jp-cell-toolbar,\n  body[data-notebook='notebooks'] .jp-RawCell .jp-cell-toolbar {\n    top: calc(0.5 * var(--jp-notebook-padding));\n  }\n}\n\n/* Tweak the notebook footer (to add a new cell) */\nbody[data-notebook='notebooks'] .jp-Notebook-footer {\n  background: unset;\n  width: 100%;\n  margin-left: unset;\n}\n\n/* Mobile View */\n\nbody[data-format='mobile'] .jp-NotebookCheckpoint {\n  display: none;\n}\n\nbody[data-format='mobile'] .jp-WindowedPanel-outer > *:first-child {\n  margin-top: 0;\n}\n\nbody[data-format='mobile'] .jp-ToolbarButton .jp-DebuggerBugButton {\n  display: none;\n}\n\nbody[data-notebook='notebooks'] .jp-WindowedPanel-viewport {\n  background: var(--jp-layout-color0);\n  box-shadow: var(--jp-elevation-z4);\n\n  /* Extra padding at the top and bottom so the notebook looks nicer */\n  padding-top: calc(2 * var(--jp-notebook-padding));\n  padding-bottom: calc(2 * var(--jp-notebook-padding));\n}\n\n/* Notebook box shadow */\n\nbody[data-notebook='notebooks']\n  .jp-Notebook\n  > *:first-child:last-child::before {\n  content: '';\n  position: absolute;\n  top: 0;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  box-shadow: 0px 0px 12px 1px var(--jp-shadow-umbra-color);\n}\n\n/* Additional customizations of the components on the notebook page */\n\n.jp-NotebookKernelLogo {\n  flex: 0 0 auto;\n  display: flex;\n  align-items: center;\n  text-align: center;\n  margin-right: 8px;\n}\n\n.jp-NotebookKernelLogo img {\n  max-width: 28px;\n  max-height: 28px;\n  display: flex;\n}\n\n.jp-NotebookKernelStatus {\n  margin: 0;\n  font-weight: normal;\n  font-size: var(--jp-ui-font-size1);\n  color: var(--jp-ui-font-color0);\n  font-family: var(--jp-ui-font-family);\n  line-height: var(--jp-private-title-panel-height);\n  padding-left: var(--jp-kernel-status-padding);\n  padding-right: var(--jp-kernel-status-padding);\n}\n\n.jp-NotebookKernelStatus-error {\n  background-color: var(--jp-error-color0);\n}\n\n.jp-NotebookKernelStatus-warn {\n  background-color: var(--jp-warn-color0);\n}\n\n.jp-NotebookKernelStatus-info {\n  background-color: var(--jp-info-color0);\n}\n\n.jp-NotebookKernelStatus-fade {\n  animation: 0.5s fade-out forwards;\n}\n\n.jp-NotebookTrustedStatus {\n  background: var(--jp-layout-color1);\n  color: var(--jp-ui-font-color1);\n  margin-top: 4px;\n  margin-bottom: 4px;\n  border: solid 1px var(--jp-border-color2);\n  cursor: help;\n}\n\n.jp-NotebookTrustedStatus-not-trusted {\n  cursor: pointer;\n}\n\n@keyframes fade-out {\n  0% {\n    opacity: 1;\n  }\n  100% {\n    opacity: 0;\n  }\n}\n\n#jp-title h1 {\n  cursor: pointer;\n  font-size: 18px;\n  margin: 0;\n  font-weight: normal;\n  color: var(--jp-ui-font-color0);\n  font-family: var(--jp-ui-font-family);\n  line-height: calc(1.5 * var(--jp-private-title-panel-height));\n  text-overflow: ellipsis;\n  overflow: hidden;\n  white-space: nowrap;\n}\n\n#jp-title h1:hover {\n  background: var(--jp-layout-color2);\n}\n\n.jp-NotebookCheckpoint {\n  font-size: 14px;\n  margin-left: 5px;\n  margin-right: 5px;\n  font-weight: normal;\n  color: var(--jp-ui-font-color0);\n  font-family: var(--jp-ui-font-family);\n  line-height: calc(1.5 * var(--jp-private-title-panel-height));\n  text-overflow: ellipsis;\n  overflow: hidden;\n  white-space: nowrap;\n}\n\n.jp-skiplink {\n  position: absolute;\n  top: -100em;\n}\n\n.jp-skiplink:focus-within {\n  position: absolute;\n  z-index: 10000;\n  top: 0;\n  left: 46%;\n  margin: 0 auto;\n  padding: 1em;\n  width: 15%;\n  box-shadow: var(--jp-elevation-z4);\n  border-radius: 4px;\n  background: var(--jp-layout-color0);\n  text-align: center;\n}\n\n.jp-skiplink:focus-within a {\n  text-decoration: underline;\n  color: var(--jp-content-link-color);\n}\n"],sourceRoot:""}]),e.d(n,{},{A:l})},99866(o,n,e){var t=e(34942),a=e.n(t),A=e(60278),r=(e.n(A))()(a());r.push([o.id,`:root {
  --jp-notebook-toolbar-margin-bottom: 20px;
  --jp-notebook-padding-offset: 20px;

  --jp-kernel-status-padding: 5px;
}
`,"",{version:3,sources:["webpack://./../node_modules/@jupyter-notebook/notebook-extension/style/variables.css"],names:[],mappings:"AAAA;EACE,yCAAyC;EACzC,kCAAkC;;EAElC,+BAA+B;AACjC",sourcesContent:[":root {\n  --jp-notebook-toolbar-margin-bottom: 20px;\n  --jp-notebook-padding-offset: 20px;\n\n  --jp-kernel-status-padding: 5px;\n}\n"],sourceRoot:""}]),e.d(n,{},{A:r})},98384(o,n,e){var t=e(34942),a=e.n(t),A=e(60278),r=(e.n(A))()(a());r.push([o.id,`/*-----------------------------------------------------------------------------
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
`,"",{version:3,sources:["webpack://./../packages/application-extension/style/base.css"],names:[],mappings:"AAAA;;;8EAG8E;;AAE9E;EACE,gBAAgB;AAClB;;AAEA;EACE,eAAe;AACjB;;AAEA;EACE,aAAa;EACb,mBAAmB;EACnB,cAAc;AAChB;;AAEA;EACE,gBAAgB;EAChB,eAAe;AACjB;;AAEA,4BAA4B;AAC5B;EACE,aAAa;EACb,uCAAuC;EACvC,uCAAuC;EACvC,kBAAkB;EAClB,aAAa;EACb,kBAAkB;EAClB,uBAAuB;AACzB;;AAEA;EACE,eAAe;EACf,kBAAkB;EAClB,cAAc;EACd,4BAA4B;AAC9B;;AAEA;EACE,OAAO;EACP,yBAAyB;AAC3B;;AAEA;EACE,iBAAiB;EACjB,cAAc;EACd,kBAAkB;AACpB;;AAEA;EACE,mBAAmB;EACnB,kBAAkB;AACpB;;AAEA;EACE,aAAa;AACf;;AAEA;EACE,gBAAgB;EAChB,+BAA+B;EAC/B,gBAAgB;AAClB;;AAEA;EACE,+BAA+B;EAC/B,kBAAkB;AACpB;;AAEA,8BAA8B;AAC9B;EACE,gBAAgB;EAChB,UAAU;EACV,eAAe;EACf,iBAAiB;EACjB,+BAA+B;AACjC",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n\n.jp-ClearData-dialog {\n  min-width: 400px;\n}\n\n.jp-ClearData-container {\n  padding: 10px 0;\n}\n\n.jp-ClearData-option {\n  display: flex;\n  align-items: center;\n  margin: 12px 0;\n}\n\n.jp-ClearData-option label {\n  margin-left: 8px;\n  cursor: pointer;\n}\n\n/* Enhanced warning styles */\n.jp-ClearData-warning-box {\n  display: flex;\n  background-color: var(--jp-warn-color1);\n  border: 1px solid var(--jp-warn-color1);\n  border-radius: 4px;\n  padding: 12px;\n  margin: 0 0 16px 0;\n  align-items: flex-start;\n}\n\n.jp-ClearData-warning-icon {\n  font-size: 24px;\n  margin-right: 12px;\n  flex-shrink: 0;\n  color: var(--jp-warn-color0);\n}\n\n.jp-ClearData-warning-text {\n  flex: 1;\n  color: var(--md-grey-900);\n}\n\n.jp-ClearData-warning-title {\n  font-weight: bold;\n  display: block;\n  margin-bottom: 8px;\n}\n\n.jp-ClearData-warning-text ul {\n  margin: 8px 0 4px 0;\n  padding-left: 24px;\n}\n\n.jp-ClearData-warning-text p {\n  margin: 4px 0;\n}\n\n.jp-ClearData-reload-notice {\n  margin-top: 16px;\n  color: var(--jp-ui-font-color2);\n  font-size: 0.9em;\n}\n\n.jp-ClearData-unavailable {\n  color: var(--jp-ui-font-color2);\n  font-style: italic;\n}\n\n/* About dialog version list */\n.jp-About-versionList {\n  list-style: none;\n  padding: 0;\n  margin: 4px 0 0;\n  font-size: 0.85em;\n  color: var(--jp-ui-font-color2);\n}\n"],sourceRoot:""}]),e.d(n,{},{A:r})},29396(o,n,e){var t=e(34942),a=e.n(t),A=e(60278),r=(e.n(A))()(a());r.push([o.id,`/*-----------------------------------------------------------------------------
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
`,"",{version:3,sources:["webpack://./../packages/apputils-extension/style/base.css"],names:[],mappings:"AAAA;;;8EAG8E;;AAE9E;EACE,aAAa;EACb,mBAAmB;EACnB,uBAAuB;AACzB;;AAEA;EACE,kBAAkB;EAClB,aAAa;EACb,mBAAmB;EACnB,uBAAuB;AACzB;;AAEA;;;;;EAKE,WAAW;EACX,YAAY;AACd;;AAEA,kBAAkB;AAClB;EACE,wBAAwB;EACxB,kCAAkC;EAClC,6BAA6B;AAC/B;;AAEA;EACE,aAAa;AACf;;AAEA;EACE,aAAa;AACf;;AAEA;EACE;IACE,uBAAuB;EACzB;EACA;IACE,yBAAyB;EAC3B;AACF;;AAEA,kBAAkB;AAClB;EACE,+BAA+B;AACjC;;AAEA,gBAAgB;AAChB;EACE,6BAA6B;AAC/B;;AAEA;;mCAEmC;;AAEnC,eAAe;AACf;EACE,aAAa;EACb,mBAAmB;EACnB,uBAAuB;EACvB,QAAQ;AACV;;AAEA;EACE,UAAU;EACV,WAAW;EACX,kBAAkB;EAClB,wCAAwC;EACxC,0CAA0C;AAC5C;;AAEA;EACE,uBAAuB;AACzB;;AAEA;EACE,uBAAuB;AACzB;;AAEA;EACE,UAAU;EACV,WAAW;AACb;;AAEA;EACE;;;IAGE,mBAAmB;IACnB,YAAY;EACd;EACA;IACE,mBAAmB;IACnB,UAAU;EACZ;AACF;;AAEA;EACE,+BAA+B;AACjC;;AAEA;EACE,6BAA6B;AAC/B;;AAEA;EACE,6BAA6B;AAC/B;;AAEA;EACE,gBAAgB;EAChB,YAAY;AACd",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n\n.jp-KernelStatus {\n  display: flex;\n  align-items: center;\n  justify-content: center;\n}\n\n.jp-KernelStatus-icon-container {\n  position: relative;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n}\n\n.jp-KernelStatus-spinner,\n.jp-KernelStatus-success,\n.jp-KernelStatus-error,\n.jp-KernelStatus-none,\n.jp-KernelStatus svg {\n  width: 16px;\n  height: 16px;\n}\n\n/* Loading state */\n.jp-KernelStatus-spinner {\n  transform-origin: center;\n  animation: spin 1s linear infinite;\n  color: var(--jp-brand-color1);\n}\n\n.jp-KernelStatus-spinner-track {\n  opacity: 0.25;\n}\n\n.jp-KernelStatus-spinner-path {\n  opacity: 0.75;\n}\n\n@keyframes spin {\n  from {\n    transform: rotate(0deg);\n  }\n  to {\n    transform: rotate(360deg);\n  }\n}\n\n/* Success state */\n.jp-KernelStatus-success {\n  color: var(--jp-success-color1);\n}\n\n/* Error state */\n.jp-KernelStatus-error {\n  color: var(--jp-error-color1);\n}\n\n/* No kernel state (e.g. after a shutdown) uses JupyterLab's circleEmptyIcon,\n   which is already a muted, theme-aware ring (via its `jp-icon3` class), so no\n   color override is needed here. */\n\n/* Busy state */\n.jp-KernelStatus-busy {\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  gap: 2px;\n}\n\n.jp-KernelStatus-busy-dot {\n  width: 6px;\n  height: 6px;\n  border-radius: 50%;\n  background-color: var(--jp-brand-color1);\n  animation: pulse 1.4s infinite ease-in-out;\n}\n\n.jp-KernelStatus-busy-dot:nth-child(1) {\n  animation-delay: -0.32s;\n}\n\n.jp-KernelStatus-busy-dot:nth-child(2) {\n  animation-delay: -0.16s;\n}\n\n.jp-KernelStatus .jp-KernelStatus-busy-dot {\n  width: 4px;\n  height: 4px;\n}\n\n@keyframes pulse {\n  0%,\n  80%,\n  100% {\n    transform: scale(0);\n    opacity: 0.5;\n  }\n  40% {\n    transform: scale(1);\n    opacity: 1;\n  }\n}\n\n.jp-KernelStatus-idle .jp-KernelStatus-text {\n  color: var(--jp-success-color1);\n}\n\n.jp-KernelStatus-busy .jp-KernelStatus-text {\n  color: var(--jp-brand-color1);\n}\n\n.jp-KernelStatus-error .jp-KernelStatus-text {\n  color: var(--jp-error-color1);\n}\n\n.jp-KernelStatus-widget {\n  padding: 2px 8px;\n  height: 24px;\n}\n"],sourceRoot:""}]),e.d(n,{},{A:r})},95996(o,n,e){var t=e(34942),a=e.n(t),A=e(60278),r=(e.n(A))()(a());r.push([o.id,`/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
`,"",{version:3,sources:["webpack://./../packages/apputils/style/base.css"],names:[],mappings:"AAAA;;;8EAG8E",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n"],sourceRoot:""}]),e.d(n,{},{A:r})},55942(o,n,e){var t=e(34942),a=e.n(t),A=e(60278),r=(e.n(A))()(a());r.push([o.id,`/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
`,"",{version:3,sources:["webpack://./../packages/notebook-application-extension/style/base.css"],names:[],mappings:"AAAA;;;8EAG8E",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n"],sourceRoot:""}]),e.d(n,{},{A:r})},60299(o,n,e){var t=e(95292),a=e.n(t),A=e(49893),r=e.n(A),i=e(9383),l=e.n(i),p=e(56884),s=e.n(p),d=e(99088),c=e.n(d),C=e(27997),b=e.n(C),E=e(98384),u={};u.styleTagTransform=b(),u.setAttributes=s(),u.insert=l().bind(null,"head"),u.domAPI=r(),u.insertStyleElement=c(),a()(E.A,u),E.A&&E.A.locals&&E.A.locals},34221(o,n,e){var t=e(95292),a=e.n(t),A=e(49893),r=e.n(A),i=e(9383),l=e.n(i),p=e(56884),s=e.n(p),d=e(99088),c=e.n(d),C=e(27997),b=e.n(C),E=e(29396),u={};u.styleTagTransform=b(),u.setAttributes=s(),u.insert=l().bind(null,"head"),u.domAPI=r(),u.insertStyleElement=c(),a()(E.A,u),E.A&&E.A.locals&&E.A.locals},78797(o,n,e){var t=e(95292),a=e.n(t),A=e(49893),r=e.n(A),i=e(9383),l=e.n(i),p=e(56884),s=e.n(p),d=e(99088),c=e.n(d),C=e(27997),b=e.n(C),E=e(95996),u={};u.styleTagTransform=b(),u.setAttributes=s(),u.insert=l().bind(null,"head"),u.domAPI=r(),u.insertStyleElement=c(),a()(E.A,u),E.A&&E.A.locals&&E.A.locals},86887(o,n,e){var t=e(95292),a=e.n(t),A=e(49893),r=e.n(A),i=e(9383),l=e.n(i),p=e(56884),s=e.n(p),d=e(99088),c=e.n(d),C=e(27997),b=e.n(C),E=e(55942),u={};u.styleTagTransform=b(),u.setAttributes=s(),u.insert=l().bind(null,"head"),u.domAPI=r(),u.insertStyleElement=c(),a()(E.A,u),E.A&&E.A.locals&&E.A.locals},44504(o,n,e){e(60299)},30146(o,n,e){e(47370),e(34221)},47370(o,n,e){e(78797)},50276(o,n,e){e(86887)}}]);
//# sourceMappingURL=6941.9463ac5.js.map
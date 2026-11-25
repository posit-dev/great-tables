"use strict";(self.rspackChunk_JUPYTERLAB_CORE_OUTPUT=self.rspackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[3687],{85214(n,e,t){t(50595),t(75200),t(41680);var o=t(95292),A=t.n(o),a=t(49893),i=t.n(a),r=t(9383),p=t.n(r),l=t(56884),s=t.n(l),d=t(99088),C=t.n(d),E=t(27997),c=t.n(E),b=t(49693),m={};m.styleTagTransform=c(),m.setAttributes=s(),m.insert=p().bind(null,"head"),m.domAPI=i(),m.insertStyleElement=C(),A()(b.A,m),b.A&&b.A.locals&&b.A.locals;var u=t(94981),h={};h.styleTagTransform=c(),h.setAttributes=s(),h.insert=p().bind(null,"head"),h.domAPI=i(),h.insertStyleElement=C(),A()(u.A,h),u.A&&u.A.locals&&u.A.locals,t(48095);var g=t(88381),j={};j.styleTagTransform=c(),j.setAttributes=s(),j.insert=p().bind(null,"head"),j.domAPI=i(),j.insertStyleElement=C(),A()(g.A,j),g.A&&g.A.locals&&g.A.locals},88768(n,e,t){var o=t(95292),A=t.n(o),a=t(49893),i=t.n(a),r=t(9383),p=t.n(r),l=t(56884),s=t.n(l),d=t(99088),C=t.n(d),E=t(27997),c=t.n(E),b=t(56314),m={};m.styleTagTransform=c(),m.setAttributes=s(),m.insert=p().bind(null,"head"),m.domAPI=i(),m.insertStyleElement=C(),A()(b.A,m),b.A&&b.A.locals&&b.A.locals},7014(n,e,t){var o=t(95292),A=t.n(o),a=t(49893),i=t.n(a),r=t(9383),p=t.n(r),l=t(56884),s=t.n(l),d=t(99088),C=t.n(d),E=t(27997),c=t.n(E),b=t(81488),m={};m.styleTagTransform=c(),m.setAttributes=s(),m.insert=p().bind(null,"head"),m.domAPI=i(),m.insertStyleElement=C(),A()(b.A,m),b.A&&b.A.locals&&b.A.locals},88381(n,e,t){var o=t(34942),A=t.n(o),a=t(60278),i=(t.n(a))()(A());i.push([n.id,`/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-NotebookSpacer {
  flex-grow: 1;
  flex-shrink: 1;
}

.jp-MainAreaWidget {
  height: 100%;
}

.jp-Toolbar > .jp-Toolbar-item {
  height: unset;
}

#jp-UserMenu {
  flex: 0 0 auto;
  display: flex;
  text-align: center;
  margin-top: 8px;
}

.jp-MimeDocument .jp-RenderedJSON {
  background: var(--jp-layout-color0);
}

/* Hide the stub toolbar that appears above terminals and documents */

.jp-MainAreaWidget > .jp-Toolbar-micro {
  display: none;
}

#jp-NotebookLogo {
  /* bring logo to the front so it is selectable by tab*/
  z-index: 10;
}

/* Hide the notification status item */
.jp-Notification-Status {
  display: none;
}
`,"",{version:3,sources:["webpack://./../node_modules/@jupyter-notebook/application-extension/style/base.css"],names:[],mappings:"AAAA;;;;8EAI8E;;AAE9E;EACE,YAAY;EACZ,cAAc;AAChB;;AAEA;EACE,YAAY;AACd;;AAEA;EACE,aAAa;AACf;;AAEA;EACE,cAAc;EACd,aAAa;EACb,kBAAkB;EAClB,eAAe;AACjB;;AAEA;EACE,mCAAmC;AACrC;;AAEA,qEAAqE;;AAErE;EACE,aAAa;AACf;;AAEA;EACE,sDAAsD;EACtD,WAAW;AACb;;AAEA,sCAAsC;AACtC;EACE,aAAa;AACf",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n|\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n\n.jp-NotebookSpacer {\n  flex-grow: 1;\n  flex-shrink: 1;\n}\n\n.jp-MainAreaWidget {\n  height: 100%;\n}\n\n.jp-Toolbar > .jp-Toolbar-item {\n  height: unset;\n}\n\n#jp-UserMenu {\n  flex: 0 0 auto;\n  display: flex;\n  text-align: center;\n  margin-top: 8px;\n}\n\n.jp-MimeDocument .jp-RenderedJSON {\n  background: var(--jp-layout-color0);\n}\n\n/* Hide the stub toolbar that appears above terminals and documents */\n\n.jp-MainAreaWidget > .jp-Toolbar-micro {\n  display: none;\n}\n\n#jp-NotebookLogo {\n  /* bring logo to the front so it is selectable by tab*/\n  z-index: 10;\n}\n\n/* Hide the notification status item */\n.jp-Notification-Status {\n  display: none;\n}\n"],sourceRoot:""}]),t.d(e,{},{A:i})},49693(n,e,t){var o=t(34942),A=t.n(o),a=t(60278),i=(t.n(a))()(A());i.push([n.id,`/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-topbar-height: 28px;
  /* Override the layout-2 color for the dark theme */
  --md-grey-800: #323232;
  --jp-notebook-max-width: 1200px;
}

/*
  Override the default background
  See https://github.com/jupyterlab/jupyterlab/pull/16519 for more information
*/
body.jp-ThemedContainer {
  margin: 0;
  padding: 0;
  background: var(--jp-layout-color2);
}

#main.jp-ThemedContainer {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--jp-layout-color2);
}

#top-panel-wrapper {
  min-height: calc(1.5 * var(--jp-private-topbar-height));
  border-bottom: var(--jp-border-width) solid var(--jp-border-color0);
  background: var(--jp-layout-color1);
}

#top-panel {
  display: flex;
  min-height: calc(1.5 * var(--jp-private-topbar-height));
  padding-left: 5px;
  padding-right: 5px;
  margin-left: auto;
  margin-right: auto;
  max-width: 1200px;
}

#menu-panel-wrapper {
  min-height: var(--jp-private-topbar-height);
  background: var(--jp-layout-color1);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color0);
  box-shadow: var(--jp-elevation-z1);
}

#menu-panel {
  display: flex;
  min-height: var(--jp-private-topbar-height);
  background: var(--jp-layout-color1);
  padding-left: 5px;
  padding-right: 5px;
  margin-left: auto;
  margin-right: auto;
  max-width: var(--jp-notebook-max-width);
}

#main-panel {
  margin-left: auto;
  margin-right: auto;
  max-width: var(--jp-notebook-max-width);
}

#spacer-widget-top {
  min-height: 16px;
}

/* Only edit pages should have a bottom space */

body[data-notebook='edit'] #spacer-widget-bottom {
  min-height: 16px;
}

/* Special case notebooks as document oriented pages */

[data-notebook]:not(body[data-notebook='notebooks']) #main-panel {
  box-shadow: var(--jp-elevation-z4);
}

.jp-TreePanel > .lm-TabPanel-stackedPanel {
  box-shadow: var(--jp-elevation-z4);
}

body[data-notebook='notebooks'] #main-panel {
  margin-left: unset;
  margin-right: unset;
  max-width: unset;
}

body[data-notebook='notebooks'] #spacer-widget-top {
  min-height: unset;
}

#main-panel > .jp-TreePanel {
  padding: 0px 5px;
}

@media only screen and (max-width: 760px) {
  #main-panel > .jp-TreePanel {
    margin: 0px -5px;
  }
}
`,"",{version:3,sources:["webpack://./../node_modules/@jupyter-notebook/application/style/base.css"],names:[],mappings:"AAAA;;;8EAG8E;;AAE9E;EACE,gCAAgC;EAChC,mDAAmD;EACnD,sBAAsB;EACtB,+BAA+B;AACjC;;AAEA;;;CAGC;AACD;EACE,SAAS;EACT,UAAU;EACV,mCAAmC;AACrC;;AAEA;EACE,kBAAkB;EAClB,MAAM;EACN,OAAO;EACP,QAAQ;EACR,SAAS;EACT,mCAAmC;AACrC;;AAEA;EACE,uDAAuD;EACvD,mEAAmE;EACnE,mCAAmC;AACrC;;AAEA;EACE,aAAa;EACb,uDAAuD;EACvD,iBAAiB;EACjB,kBAAkB;EAClB,iBAAiB;EACjB,kBAAkB;EAClB,iBAAiB;AACnB;;AAEA;EACE,2CAA2C;EAC3C,mCAAmC;EACnC,mEAAmE;EACnE,kCAAkC;AACpC;;AAEA;EACE,aAAa;EACb,2CAA2C;EAC3C,mCAAmC;EACnC,iBAAiB;EACjB,kBAAkB;EAClB,iBAAiB;EACjB,kBAAkB;EAClB,uCAAuC;AACzC;;AAEA;EACE,iBAAiB;EACjB,kBAAkB;EAClB,uCAAuC;AACzC;;AAEA;EACE,gBAAgB;AAClB;;AAEA,+CAA+C;;AAE/C;EACE,gBAAgB;AAClB;;AAEA,sDAAsD;;AAEtD;EACE,kCAAkC;AACpC;;AAEA;EACE,kCAAkC;AACpC;;AAEA;EACE,kBAAkB;EAClB,mBAAmB;EACnB,gBAAgB;AAClB;;AAEA;EACE,iBAAiB;AACnB;;AAEA;EACE,gBAAgB;AAClB;;AAEA;EACE;IACE,gBAAgB;EAClB;AACF",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n\n:root {\n  --jp-private-topbar-height: 28px;\n  /* Override the layout-2 color for the dark theme */\n  --md-grey-800: #323232;\n  --jp-notebook-max-width: 1200px;\n}\n\n/*\n  Override the default background\n  See https://github.com/jupyterlab/jupyterlab/pull/16519 for more information\n*/\nbody.jp-ThemedContainer {\n  margin: 0;\n  padding: 0;\n  background: var(--jp-layout-color2);\n}\n\n#main.jp-ThemedContainer {\n  position: absolute;\n  top: 0;\n  left: 0;\n  right: 0;\n  bottom: 0;\n  background: var(--jp-layout-color2);\n}\n\n#top-panel-wrapper {\n  min-height: calc(1.5 * var(--jp-private-topbar-height));\n  border-bottom: var(--jp-border-width) solid var(--jp-border-color0);\n  background: var(--jp-layout-color1);\n}\n\n#top-panel {\n  display: flex;\n  min-height: calc(1.5 * var(--jp-private-topbar-height));\n  padding-left: 5px;\n  padding-right: 5px;\n  margin-left: auto;\n  margin-right: auto;\n  max-width: 1200px;\n}\n\n#menu-panel-wrapper {\n  min-height: var(--jp-private-topbar-height);\n  background: var(--jp-layout-color1);\n  border-bottom: var(--jp-border-width) solid var(--jp-border-color0);\n  box-shadow: var(--jp-elevation-z1);\n}\n\n#menu-panel {\n  display: flex;\n  min-height: var(--jp-private-topbar-height);\n  background: var(--jp-layout-color1);\n  padding-left: 5px;\n  padding-right: 5px;\n  margin-left: auto;\n  margin-right: auto;\n  max-width: var(--jp-notebook-max-width);\n}\n\n#main-panel {\n  margin-left: auto;\n  margin-right: auto;\n  max-width: var(--jp-notebook-max-width);\n}\n\n#spacer-widget-top {\n  min-height: 16px;\n}\n\n/* Only edit pages should have a bottom space */\n\nbody[data-notebook='edit'] #spacer-widget-bottom {\n  min-height: 16px;\n}\n\n/* Special case notebooks as document oriented pages */\n\n[data-notebook]:not(body[data-notebook='notebooks']) #main-panel {\n  box-shadow: var(--jp-elevation-z4);\n}\n\n.jp-TreePanel > .lm-TabPanel-stackedPanel {\n  box-shadow: var(--jp-elevation-z4);\n}\n\nbody[data-notebook='notebooks'] #main-panel {\n  margin-left: unset;\n  margin-right: unset;\n  max-width: unset;\n}\n\nbody[data-notebook='notebooks'] #spacer-widget-top {\n  min-height: unset;\n}\n\n#main-panel > .jp-TreePanel {\n  padding: 0px 5px;\n}\n\n@media only screen and (max-width: 760px) {\n  #main-panel > .jp-TreePanel {\n    margin: 0px -5px;\n  }\n}\n"],sourceRoot:""}]),t.d(e,{},{A:i})},94981(n,e,t){var o=t(34942),A=t.n(o),a=t(60278),i=(t.n(a))()(A());i.push([n.id,`/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|
| Adapted from JupyterLab's packages/application/style/sidepanel.css.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-sidebar-tab-width: 32px;
}

/*-----------------------------------------------------------------------------
| SideBar
|----------------------------------------------------------------------------*/

/* Stack panels */

#jp-right-stack,
#jp-left-stack {
  display: flex;
  flex-direction: column;
  min-width: var(--jp-sidebar-min-width);
}

#jp-left-stack .jp-SidePanel-collapse,
#jp-right-stack .jp-SidePanel-collapse {
  display: flex;
  flex: 0 0 auto;
  min-height: 0;
  padding: 0;
}

#jp-left-stack .jp-SidePanel-collapse {
  justify-content: right;
}

#jp-right-stack .jp-SidePanel-collapse {
  justify-content: left;
}

#jp-left-stack .lm-StackedPanel,
#jp-right-stack .lm-StackedPanel {
  flex: 1 1 auto;
}
`,"",{version:3,sources:["webpack://./../node_modules/@jupyter-notebook/application/style/sidepanel.css"],names:[],mappings:"AAAA;;;;;8EAK8E;;AAE9E;;8EAE8E;;AAE9E;EACE,oCAAoC;AACtC;;AAEA;;8EAE8E;;AAE9E,iBAAiB;;AAEjB;;EAEE,aAAa;EACb,sBAAsB;EACtB,sCAAsC;AACxC;;AAEA;;EAEE,aAAa;EACb,cAAc;EACd,aAAa;EACb,UAAU;AACZ;;AAEA;EACE,sBAAsB;AACxB;;AAEA;EACE,qBAAqB;AACvB;;AAEA;;EAEE,cAAc;AAChB",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n| Distributed under the terms of the Modified BSD License.\n|\n| Adapted from JupyterLab's packages/application/style/sidepanel.css.\n|----------------------------------------------------------------------------*/\n\n/*-----------------------------------------------------------------------------\n| Variables\n|----------------------------------------------------------------------------*/\n\n:root {\n  --jp-private-sidebar-tab-width: 32px;\n}\n\n/*-----------------------------------------------------------------------------\n| SideBar\n|----------------------------------------------------------------------------*/\n\n/* Stack panels */\n\n#jp-right-stack,\n#jp-left-stack {\n  display: flex;\n  flex-direction: column;\n  min-width: var(--jp-sidebar-min-width);\n}\n\n#jp-left-stack .jp-SidePanel-collapse,\n#jp-right-stack .jp-SidePanel-collapse {\n  display: flex;\n  flex: 0 0 auto;\n  min-height: 0;\n  padding: 0;\n}\n\n#jp-left-stack .jp-SidePanel-collapse {\n  justify-content: right;\n}\n\n#jp-right-stack .jp-SidePanel-collapse {\n  justify-content: left;\n}\n\n#jp-left-stack .lm-StackedPanel,\n#jp-right-stack .lm-StackedPanel {\n  flex: 1 1 auto;\n}\n"],sourceRoot:""}]),t.d(e,{},{A:i})},56314(n,e,t){var o=t(34942),A=t.n(o),a=t(60278),i=(t.n(a))()(A());i.push([n.id,`.jp-Document {
  height: 100%;
}
`,"",{version:3,sources:["webpack://./../node_modules/@jupyter-notebook/docmanager-extension/style/base.css"],names:[],mappings:"AAAA;EACE,YAAY;AACd",sourcesContent:[".jp-Document {\n  height: 100%;\n}\n"],sourceRoot:""}]),t.d(e,{},{A:i})},81488(n,e,t){var o=t(34942),A=t.n(o),a=t(60278),i=(t.n(a))()(A());i.push([n.id,`.jp-AboutNotebook .jp-Dialog-header {
  justify-content: center;
  padding: 0;
}

.jp-AboutNotebook-header {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: var(--jp-flat-button-padding);
}

.jp-AboutNotebook-header-text {
  margin-left: 16px;
}

.jp-AboutNotebook-version {
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  padding-bottom: 30px;
  font-weight: 400;
  letter-spacing: 0.4px;
  line-height: 1.12;
  min-width: 360px;
  text-align: center;
}

.jp-AboutNotebook-body {
  display: flex;
  font-size: var(--jp-ui-font-size2);
  padding: var(--jp-flat-button-padding);
  color: var(--jp-ui-font-color1);
  text-align: center;
  flex-direction: column;
  min-width: 360px;
  overflow: hidden;
}

.jp-AboutNotebook-about-body pre {
  white-space: pre-wrap;
}

.jp-AboutNotebook-about-externalLinks {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  color: var(--jp-warn-color0);
}

.jp-AboutNotebook-about-copyright {
  padding-top: 25px;
}
`,"",{version:3,sources:["webpack://./../node_modules/@jupyter-notebook/help-extension/style/base.css"],names:[],mappings:"AAAA;EACE,uBAAuB;EACvB,UAAU;AACZ;;AAEA;EACE,aAAa;EACb,mBAAmB;EACnB,mBAAmB;EACnB,sCAAsC;AACxC;;AAEA;EACE,iBAAiB;AACnB;;AAEA;EACE,+BAA+B;EAC/B,kCAAkC;EAClC,oBAAoB;EACpB,gBAAgB;EAChB,qBAAqB;EACrB,iBAAiB;EACjB,gBAAgB;EAChB,kBAAkB;AACpB;;AAEA;EACE,aAAa;EACb,kCAAkC;EAClC,sCAAsC;EACtC,+BAA+B;EAC/B,kBAAkB;EAClB,sBAAsB;EACtB,gBAAgB;EAChB,gBAAgB;AAClB;;AAEA;EACE,qBAAqB;AACvB;;AAEA;EACE,aAAa;EACb,sBAAsB;EACtB,2BAA2B;EAC3B,uBAAuB;EACvB,4BAA4B;AAC9B;;AAEA;EACE,iBAAiB;AACnB",sourcesContent:[".jp-AboutNotebook .jp-Dialog-header {\n  justify-content: center;\n  padding: 0;\n}\n\n.jp-AboutNotebook-header {\n  display: flex;\n  flex-direction: row;\n  align-items: center;\n  padding: var(--jp-flat-button-padding);\n}\n\n.jp-AboutNotebook-header-text {\n  margin-left: 16px;\n}\n\n.jp-AboutNotebook-version {\n  color: var(--jp-ui-font-color1);\n  font-size: var(--jp-ui-font-size1);\n  padding-bottom: 30px;\n  font-weight: 400;\n  letter-spacing: 0.4px;\n  line-height: 1.12;\n  min-width: 360px;\n  text-align: center;\n}\n\n.jp-AboutNotebook-body {\n  display: flex;\n  font-size: var(--jp-ui-font-size2);\n  padding: var(--jp-flat-button-padding);\n  color: var(--jp-ui-font-color1);\n  text-align: center;\n  flex-direction: column;\n  min-width: 360px;\n  overflow: hidden;\n}\n\n.jp-AboutNotebook-about-body pre {\n  white-space: pre-wrap;\n}\n\n.jp-AboutNotebook-about-externalLinks {\n  display: flex;\n  flex-direction: column;\n  justify-content: flex-start;\n  align-items: flex-start;\n  color: var(--jp-warn-color0);\n}\n\n.jp-AboutNotebook-about-copyright {\n  padding-top: 25px;\n}\n"],sourceRoot:""}]),t.d(e,{},{A:i})}}]);
//# sourceMappingURL=3687.229d738.js.map
"use strict";(self.rspackChunk_JUPYTERLAB_CORE_OUTPUT=self.rspackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[1263],{98384(e,t,n){var o=n(34942),r=n.n(o),a=n(60278),s=(n.n(a))()(r());s.push([e.id,`/*-----------------------------------------------------------------------------
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
`,"",{version:3,sources:["webpack://./../packages/application-extension/style/base.css"],names:[],mappings:"AAAA;;;8EAG8E;;AAE9E;EACE,gBAAgB;AAClB;;AAEA;EACE,eAAe;AACjB;;AAEA;EACE,aAAa;EACb,mBAAmB;EACnB,cAAc;AAChB;;AAEA;EACE,gBAAgB;EAChB,eAAe;AACjB;;AAEA,4BAA4B;AAC5B;EACE,aAAa;EACb,uCAAuC;EACvC,uCAAuC;EACvC,kBAAkB;EAClB,aAAa;EACb,kBAAkB;EAClB,uBAAuB;AACzB;;AAEA;EACE,eAAe;EACf,kBAAkB;EAClB,cAAc;EACd,4BAA4B;AAC9B;;AAEA;EACE,OAAO;EACP,yBAAyB;AAC3B;;AAEA;EACE,iBAAiB;EACjB,cAAc;EACd,kBAAkB;AACpB;;AAEA;EACE,mBAAmB;EACnB,kBAAkB;AACpB;;AAEA;EACE,aAAa;AACf;;AAEA;EACE,gBAAgB;EAChB,+BAA+B;EAC/B,gBAAgB;AAClB;;AAEA;EACE,+BAA+B;EAC/B,kBAAkB;AACpB;;AAEA,8BAA8B;AAC9B;EACE,gBAAgB;EAChB,UAAU;EACV,eAAe;EACf,iBAAiB;EACjB,+BAA+B;AACjC",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n\n.jp-ClearData-dialog {\n  min-width: 400px;\n}\n\n.jp-ClearData-container {\n  padding: 10px 0;\n}\n\n.jp-ClearData-option {\n  display: flex;\n  align-items: center;\n  margin: 12px 0;\n}\n\n.jp-ClearData-option label {\n  margin-left: 8px;\n  cursor: pointer;\n}\n\n/* Enhanced warning styles */\n.jp-ClearData-warning-box {\n  display: flex;\n  background-color: var(--jp-warn-color1);\n  border: 1px solid var(--jp-warn-color1);\n  border-radius: 4px;\n  padding: 12px;\n  margin: 0 0 16px 0;\n  align-items: flex-start;\n}\n\n.jp-ClearData-warning-icon {\n  font-size: 24px;\n  margin-right: 12px;\n  flex-shrink: 0;\n  color: var(--jp-warn-color0);\n}\n\n.jp-ClearData-warning-text {\n  flex: 1;\n  color: var(--md-grey-900);\n}\n\n.jp-ClearData-warning-title {\n  font-weight: bold;\n  display: block;\n  margin-bottom: 8px;\n}\n\n.jp-ClearData-warning-text ul {\n  margin: 8px 0 4px 0;\n  padding-left: 24px;\n}\n\n.jp-ClearData-warning-text p {\n  margin: 4px 0;\n}\n\n.jp-ClearData-reload-notice {\n  margin-top: 16px;\n  color: var(--jp-ui-font-color2);\n  font-size: 0.9em;\n}\n\n.jp-ClearData-unavailable {\n  color: var(--jp-ui-font-color2);\n  font-style: italic;\n}\n\n/* About dialog version list */\n.jp-About-versionList {\n  list-style: none;\n  padding: 0;\n  margin: 4px 0 0;\n  font-size: 0.85em;\n  color: var(--jp-ui-font-color2);\n}\n"],sourceRoot:""}]),n.d(t,{},{A:s})},29396(e,t,n){var o=n(34942),r=n.n(o),a=n(60278),s=(n.n(a))()(r());s.push([e.id,`/*-----------------------------------------------------------------------------
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
`,"",{version:3,sources:["webpack://./../packages/apputils-extension/style/base.css"],names:[],mappings:"AAAA;;;8EAG8E;;AAE9E;EACE,aAAa;EACb,mBAAmB;EACnB,uBAAuB;AACzB;;AAEA;EACE,kBAAkB;EAClB,aAAa;EACb,mBAAmB;EACnB,uBAAuB;AACzB;;AAEA;;;;;EAKE,WAAW;EACX,YAAY;AACd;;AAEA,kBAAkB;AAClB;EACE,wBAAwB;EACxB,kCAAkC;EAClC,6BAA6B;AAC/B;;AAEA;EACE,aAAa;AACf;;AAEA;EACE,aAAa;AACf;;AAEA;EACE;IACE,uBAAuB;EACzB;EACA;IACE,yBAAyB;EAC3B;AACF;;AAEA,kBAAkB;AAClB;EACE,+BAA+B;AACjC;;AAEA,gBAAgB;AAChB;EACE,6BAA6B;AAC/B;;AAEA;;mCAEmC;;AAEnC,eAAe;AACf;EACE,aAAa;EACb,mBAAmB;EACnB,uBAAuB;EACvB,QAAQ;AACV;;AAEA;EACE,UAAU;EACV,WAAW;EACX,kBAAkB;EAClB,wCAAwC;EACxC,0CAA0C;AAC5C;;AAEA;EACE,uBAAuB;AACzB;;AAEA;EACE,uBAAuB;AACzB;;AAEA;EACE,UAAU;EACV,WAAW;AACb;;AAEA;EACE;;;IAGE,mBAAmB;IACnB,YAAY;EACd;EACA;IACE,mBAAmB;IACnB,UAAU;EACZ;AACF;;AAEA;EACE,+BAA+B;AACjC;;AAEA;EACE,6BAA6B;AAC/B;;AAEA;EACE,6BAA6B;AAC/B;;AAEA;EACE,gBAAgB;EAChB,YAAY;AACd",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n\n.jp-KernelStatus {\n  display: flex;\n  align-items: center;\n  justify-content: center;\n}\n\n.jp-KernelStatus-icon-container {\n  position: relative;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n}\n\n.jp-KernelStatus-spinner,\n.jp-KernelStatus-success,\n.jp-KernelStatus-error,\n.jp-KernelStatus-none,\n.jp-KernelStatus svg {\n  width: 16px;\n  height: 16px;\n}\n\n/* Loading state */\n.jp-KernelStatus-spinner {\n  transform-origin: center;\n  animation: spin 1s linear infinite;\n  color: var(--jp-brand-color1);\n}\n\n.jp-KernelStatus-spinner-track {\n  opacity: 0.25;\n}\n\n.jp-KernelStatus-spinner-path {\n  opacity: 0.75;\n}\n\n@keyframes spin {\n  from {\n    transform: rotate(0deg);\n  }\n  to {\n    transform: rotate(360deg);\n  }\n}\n\n/* Success state */\n.jp-KernelStatus-success {\n  color: var(--jp-success-color1);\n}\n\n/* Error state */\n.jp-KernelStatus-error {\n  color: var(--jp-error-color1);\n}\n\n/* No kernel state (e.g. after a shutdown) uses JupyterLab's circleEmptyIcon,\n   which is already a muted, theme-aware ring (via its `jp-icon3` class), so no\n   color override is needed here. */\n\n/* Busy state */\n.jp-KernelStatus-busy {\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  gap: 2px;\n}\n\n.jp-KernelStatus-busy-dot {\n  width: 6px;\n  height: 6px;\n  border-radius: 50%;\n  background-color: var(--jp-brand-color1);\n  animation: pulse 1.4s infinite ease-in-out;\n}\n\n.jp-KernelStatus-busy-dot:nth-child(1) {\n  animation-delay: -0.32s;\n}\n\n.jp-KernelStatus-busy-dot:nth-child(2) {\n  animation-delay: -0.16s;\n}\n\n.jp-KernelStatus .jp-KernelStatus-busy-dot {\n  width: 4px;\n  height: 4px;\n}\n\n@keyframes pulse {\n  0%,\n  80%,\n  100% {\n    transform: scale(0);\n    opacity: 0.5;\n  }\n  40% {\n    transform: scale(1);\n    opacity: 1;\n  }\n}\n\n.jp-KernelStatus-idle .jp-KernelStatus-text {\n  color: var(--jp-success-color1);\n}\n\n.jp-KernelStatus-busy .jp-KernelStatus-text {\n  color: var(--jp-brand-color1);\n}\n\n.jp-KernelStatus-error .jp-KernelStatus-text {\n  color: var(--jp-error-color1);\n}\n\n.jp-KernelStatus-widget {\n  padding: 2px 8px;\n  height: 24px;\n}\n"],sourceRoot:""}]),n.d(t,{},{A:s})},95996(e,t,n){var o=n(34942),r=n.n(o),a=n(60278),s=(n.n(a))()(r());s.push([e.id,`/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
`,"",{version:3,sources:["webpack://./../packages/apputils/style/base.css"],names:[],mappings:"AAAA;;;8EAG8E",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n"],sourceRoot:""}]),n.d(t,{},{A:s})},55942(e,t,n){var o=n(34942),r=n.n(o),a=n(60278),s=(n.n(a))()(r());s.push([e.id,`/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
`,"",{version:3,sources:["webpack://./../packages/notebook-application-extension/style/base.css"],names:[],mappings:"AAAA;;;8EAG8E",sourcesContent:["/*-----------------------------------------------------------------------------\n| Copyright (c) Jupyter Development Team.\n| Distributed under the terms of the Modified BSD License.\n|----------------------------------------------------------------------------*/\n"],sourceRoot:""}]),n.d(t,{},{A:s})},74562(e,t,n){n.d(t,{main:()=>k});var o=n(50222),r=n(66840),a=n(49884);n(85214),n(88768),n(7014),n(19894),n(89277),n(59344),n(47568),n(14640),n(2645),n(66156),n(48175),n(5207),n(50301),n(92045),n(93712),n(71670),n(66029),n(69471),n(17704),n(63562),n(38257),n(26021),n(53555),n(738),n(93992),n(21462),n(43684),n(313),n(41315),n(28114),n(52400);var s=n(95292),i=n.n(s),l=n(49893),p=n.n(l),A=n(9383),c=n.n(A),u=n(56884),y=n.n(u),h=n(99088),j=n.n(h),f=n(27997),d=n.n(f),x=n(98384),b={};b.styleTagTransform=d(),b.setAttributes=y(),b.insert=c().bind(null,"head"),b.domAPI=p(),b.insertStyleElement=j(),i()(x.A,b),x.A&&x.A.locals&&x.A.locals;var m=n(95996),C={};C.styleTagTransform=d(),C.setAttributes=y(),C.insert=c().bind(null,"head"),C.domAPI=p(),C.insertStyleElement=j(),i()(m.A,C),m.A&&m.A.locals&&m.A.locals;var g=n(29396),E={};E.styleTagTransform=d(),E.setAttributes=y(),E.insert=c().bind(null,"head"),E.domAPI=p(),E.insertStyleElement=j(),i()(g.A,E),g.A&&g.A.locals&&g.A.locals;var _=n(55942),B={};B.styleTagTransform=d(),B.setAttributes=y(),B.insert=c().bind(null,"head"),B.domAPI=p(),B.insertStyleElement=j(),i()(_.A,B),_.A&&_.A.locals&&_.A.locals;let v=["@jupyterlab/application-extension:dirty","@jupyterlab/application-extension:info","@jupyterlab/application-extension:layout","@jupyterlab/application-extension:logo","@jupyterlab/application-extension:main","@jupyterlab/application-extension:move-widget","@jupyterlab/application-extension:notfound","@jupyterlab/application-extension:paths","@jupyterlab/application-extension:property-inspector","@jupyterlab/application-extension:shell","@jupyterlab/application-extension:status","@jupyterlab/application-extension:tree-resolver","@jupyterlab/apputils-extension:announcements","@jupyterlab/apputils-extension:kernel-status","@jupyterlab/apputils-extension:palette-restorer","@jupyterlab/apputils-extension:print","@jupyterlab/apputils-extension:resolver","@jupyterlab/apputils-extension:running-sessions-status","@jupyterlab/apputils-extension:splash","@jupyterlab/apputils-extension:workspaces","@jupyterlab/console-extension:kernel-status","@jupyterlab/docmanager-extension:download","@jupyterlab/docmanager-extension:opener","@jupyterlab/docmanager-extension:path-status","@jupyterlab/docmanager-extension:saving-status","@jupyterlab/documentsearch-extension:labShellWidgetListener","@jupyterlab/filebrowser-extension:browser","@jupyterlab/filebrowser-extension:download","@jupyterlab/filebrowser-extension:file-upload-status","@jupyterlab/filebrowser-extension:open-with","@jupyterlab/filebrowser-extension:share-file","@jupyterlab/filebrowser-extension:widget","@jupyterlab/fileeditor-extension:editor-syntax-status","@jupyterlab/fileeditor-extension:language-server","@jupyterlab/fileeditor-extension:search","@jupyterlab/help-extension:about","@jupyterlab/help-extension:open","@jupyterlab/lsp-extension:plugin","@jupyterlab/notebook-extension:export","@jupyterlab/notebook-extension:execution-indicator","@jupyterlab/notebook-extension:kernel-status","@jupyterlab/services-extension:config-section-manager","@jupyterlab/services-extension:connection-status","@jupyterlab/services-extension:default-drive","@jupyterlab/services-extension:event-manager","@jupyterlab/services-extension:kernel-manager","@jupyterlab/services-extension:kernel-spec-manager","@jupyterlab/services-extension:nbconvert-manager","@jupyterlab/services-extension:session-manager","@jupyterlab/services-extension:setting-manager","@jupyterlab/services-extension:user-manager","@jupyterlab/services-extension:workspace-manager","@jupyter-notebook/application-extension:logo","@jupyter-notebook/application-extension:opener","@jupyter-notebook/application-extension:path-opener","@jupyter-notebook/help-extension:about"];async function w(e,t){try{let n=(await window._JUPYTERLAB[e].get(t))();return n.__scope__=e,n}catch(n){throw console.warn(`Failed to create module: package: ${e}; module: ${t}`),n}}async function k(){let e=[],t=[],s=[],i=[],l=[],p=JSON.parse(r.PageConfig.getOption("federated_extensions")),A=new Set;function*c(t){let n;for(let o of Array.isArray(n=t.hasOwnProperty("__esModule")?t.default:t)?n:[n])r.PageConfig.Extension.isDisabled(o.id)||v.includes(o.id)||v.includes(o.id.split(":")[0])||(e.push({...o,extension:t.__scope__}),yield o)}p.forEach(e=>{e.extension&&(A.add(e.name),s.push(w(e.name,e.extension))),e.mimeExtension&&(A.add(e.name),i.push(w(e.name,e.mimeExtension))),e.style&&l.push(w(e.name,e.style))});let u=[];if(!A.has("@jupyterlab/javascript-extension"))try{let e=n(4162);for(let t of(e.__scope__="@jupyterlab/javascript-extension",c(e)))u.push(t)}catch(e){console.error(e)}if(!A.has("@jupyterlab/json-extension"))try{let e=n(28746);for(let t of(e.__scope__="@jupyterlab/json-extension",c(e)))u.push(t)}catch(e){console.error(e)}if(!A.has("@jupyterlab/mermaid-extension"))try{let e=n(9675);for(let t of(e.__scope__="@jupyterlab/mermaid-extension",c(e)))u.push(t)}catch(e){console.error(e)}if(!A.has("@jupyterlab/vega5-extension"))try{let e=n(37826);for(let t of(e.__scope__="@jupyterlab/vega5-extension",c(e)))u.push(t)}catch(e){console.error(e)}if((await Promise.allSettled(i)).forEach(e=>{if("fulfilled"===e.status)for(let t of c(e.value))u.push(t);else console.error(e.reason)}),!A.has("@jupyterlab/application-extension"))try{let e=n(93822);for(let n of(e.__scope__="@jupyterlab/application-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/apputils-extension"))try{let e=n(19450);for(let n of(e.__scope__="@jupyterlab/apputils-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/audio-extension"))try{let e=n(56478);for(let n of(e.__scope__="@jupyterlab/audio-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/cell-toolbar-extension"))try{let e=n(13226);for(let n of(e.__scope__="@jupyterlab/cell-toolbar-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/codemirror-extension"))try{let e=n(59018);for(let n of(e.__scope__="@jupyterlab/codemirror-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/completer-extension"))try{let e=n(5188);for(let n of(e.__scope__="@jupyterlab/completer-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/console-extension"))try{let e=n(15080);for(let n of(e.__scope__="@jupyterlab/console-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/docmanager-extension"))try{let e=n(91346);for(let n of(e.__scope__="@jupyterlab/docmanager-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/documentsearch-extension"))try{let e=n(75986);for(let n of(e.__scope__="@jupyterlab/documentsearch-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/filebrowser-extension"))try{let e=n(4166);for(let n of(e.__scope__="@jupyterlab/filebrowser-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/fileeditor-extension"))try{let e=n(88226);for(let n of(e.__scope__="@jupyterlab/fileeditor-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/help-extension"))try{let e=n(29898);for(let n of(e.__scope__="@jupyterlab/help-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/lsp-extension"))try{let e=n(3900);for(let n of(e.__scope__="@jupyterlab/lsp-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/mainmenu-extension"))try{let e=n(70074);for(let n of(e.__scope__="@jupyterlab/mainmenu-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/mathjax-extension"))try{let e=n(9264);for(let n of(e.__scope__="@jupyterlab/mathjax-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/mermaid-extension"))try{let e=n(6032);for(let n of(e.__scope__="@jupyterlab/mermaid-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/metadataform-extension"))try{let e=n(56250);for(let n of(e.__scope__="@jupyterlab/metadataform-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/notebook-extension"))try{let e=n(39102);for(let n of(e.__scope__="@jupyterlab/notebook-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/rendermime-extension"))try{let e=n(70106);for(let n of(e.__scope__="@jupyterlab/rendermime-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/services-extension"))try{let e=n(21810);for(let n of(e.__scope__="@jupyterlab/services-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/shortcuts-extension"))try{let e=n(70523);for(let n of(e.__scope__="@jupyterlab/shortcuts-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/theme-dark-extension"))try{let e=n(28702);for(let n of(e.__scope__="@jupyterlab/theme-dark-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/theme-dark-high-contrast-extension"))try{let e=n(79694);for(let n of(e.__scope__="@jupyterlab/theme-dark-high-contrast-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/theme-light-extension"))try{let e=n(46826);for(let n of(e.__scope__="@jupyterlab/theme-light-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/toc-extension"))try{let e=n(33268);for(let n of(e.__scope__="@jupyterlab/toc-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/tooltip-extension"))try{let e=n(62612);for(let n of(e.__scope__="@jupyterlab/tooltip-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/translation-extension"))try{let e=n(47444);for(let n of(e.__scope__="@jupyterlab/translation-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/ui-components-extension"))try{let e=n(70732);for(let n of(e.__scope__="@jupyterlab/ui-components-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlab/video-extension"))try{let e=n(6040);for(let n of(e.__scope__="@jupyterlab/video-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyter-notebook/application-extension"))try{let e=n(91406);for(let n of(e.__scope__="@jupyter-notebook/application-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyter-notebook/docmanager-extension"))try{let e=n(11676);for(let n of(e.__scope__="@jupyter-notebook/docmanager-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyter-notebook/help-extension"))try{let e=n(66316);for(let n of(e.__scope__="@jupyter-notebook/help-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlite/application-extension"))try{let e=n(71903);for(let n of(e.__scope__="@jupyterlite/application-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlite/apputils-extension"))try{let e=n(14235);for(let n of(e.__scope__="@jupyterlite/apputils-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlite/notebook-application-extension"))try{let e=n(5383);for(let n of(e.__scope__="@jupyterlite/notebook-application-extension",c(e)))t.push(n)}catch(e){console.error(e)}if(!A.has("@jupyterlite/services-extension"))try{let e=n(80795);for(let n of(e.__scope__="@jupyterlite/services-extension",c(e)))t.push(n)}catch(e){console.error(e)}(await Promise.allSettled(s)).forEach(e=>{if("fulfilled"===e.status)for(let n of c(e.value))t.push(n);else console.error(e.reason)}),(await Promise.allSettled(l)).filter(({status:e})=>"rejected"===e).forEach(({reason:e})=>{console.error(e)});let y=new a.PluginRegistry;y.registerPlugins(t);let h=n(247).IServiceManager,j=await y.resolveRequiredService(h),f=new o.NotebookApp({pluginRegistry:y,mimeExtensions:u,serviceManager:j,availablePlugins:e});f.name=r.PageConfig.getOption("appName")||"JupyterLite","true"===(r.PageConfig.getOption("exposeAppInBrowser")||"").toLowerCase()&&(window.jupyterapp=f),await f.start({bubblingKeydown:!0}),await f.restored}}}]);
//# sourceMappingURL=1263.f7da79d.js.map
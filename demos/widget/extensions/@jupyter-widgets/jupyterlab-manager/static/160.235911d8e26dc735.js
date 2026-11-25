"use strict";(self.rspackChunk_jupyter_widgets_jupyterlab_manager=self.rspackChunk_jupyter_widgets_jupyterlab_manager||[]).push([[160],{4400(e,t,i){var r=i(6758),o=i.n(r),a=i(935),n=i.n(a)()(o());n.push([e.id,`/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jupyter-widgets-disconnected::before {
  content: '\\f127'; /* chain-broken */
  display: inline-block;
  font: normal normal 900 14px/1 'Font Awesome 5 Free', 'FontAwesome';
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #d9534f;
  padding: 3px;
  align-self: flex-start;
}

.jupyter-widgets-error-widget {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  border: solid 1px red;
  margin: 0 auto;
}

.jupyter-widgets-error-widget.icon-error {
  min-width: var(--jp-widgets-inline-width-short);
}
.jupyter-widgets-error-widget.text-error {
  min-width: calc(2 * var(--jp-widgets-inline-width));
  min-height: calc(3 * var(--jp-widgets-inline-height));
}

.jupyter-widgets-error-widget p {
  text-align: center;
}

.jupyter-widgets-error-widget.text-error pre::first-line {
  font-weight: bold;
}
`,""]),i.d(t,{},{A:n})},9471(e,t,i){var r=i(6758),o=i.n(r),a=i(935),n=i.n(a)()(o());n.push([e.id,`/* This file has code derived from Lumino CSS files, as noted below. The license for this Lumino code is:

Copyright (c) 2019 Project Jupyter Contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


Copyright (c) 2014-2017, PhosphorJS Contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/*
 * The following section is derived from https://github.com/jupyterlab/lumino/blob/23b9d075ebc5b73ab148b6ebfc20af97f85714c4/packages/widgets/style/tabbar.css 
 * We've scoped the rules so that they are consistent with exactly our code.
 */

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar, /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='horizontal'], /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar[data-orientation='horizontal'], /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='vertical'], /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar[data-orientation='vertical'], /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar > .p-TabBar-content, /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar > .p-TabBar-content, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar > .lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab
  > .p-TabBar[data-orientation='horizontal']
  > .p-TabBar-content,
/* </DEPRECATED> */
/* <DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
> .p-TabBar[data-orientation='horizontal']
> .p-TabBar-content,
/* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
  > .lm-TabBar[data-orientation='horizontal']
  > .lm-TabBar-content {
  flex-direction: row;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab
  > .p-TabBar[data-orientation='vertical']
  > .p-TabBar-content,
/* </DEPRECATED> */
/* <DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
> .p-TabBar[data-orientation='vertical']
> .p-TabBar-content,
/* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
  > .lm-TabBar[data-orientation='vertical']
  > .lm-TabBar-content {
  flex-direction: column;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab, /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar .p-TabBar-tab, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar .lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabIcon, /* </DEPRECATED> */
/* <DEPRECATED> */ .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabCloseIcon, /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar .p-TabBar-tabIcon, /* </DEPRECATED> */
/* <DEPRECATED> */ .jupyter-widgets.jupyter-widget-tab > .p-TabBar .p-TabBar-tabCloseIcon, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar .lm-TabBar-tabIcon,
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar .lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabLabel, /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar .p-TabBar-tabLabel, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar .lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-hidden, /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar .p-TabBar-tab.p-mod-hidden, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar .lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging .p-TabBar-tab, /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar.p-mod-dragging .p-TabBar-tab, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab
  > .p-TabBar.p-mod-dragging[data-orientation='horizontal']
  .p-TabBar-tab,
/* </DEPRECATED> */
/* <DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
  > .p-TabBar.p-mod-dragging[data-orientation='horizontal']
  .p-TabBar-tab,
/* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
  > .lm-TabBar.lm-mod-dragging[data-orientation='horizontal']
  .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab
  > .p-TabBar.p-mod-dragging[data-orientation='vertical']
  .p-TabBar-tab,
/* </DEPRECATED> */
/* <DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
> .p-TabBar.p-mod-dragging[data-orientation='vertical']
.p-TabBar-tab,
/* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
  > .lm-TabBar.lm-mod-dragging[data-orientation='vertical']
  .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab
  > .p-TabBar.p-mod-dragging
  .p-TabBar-tab.p-mod-dragging,
/* </DEPRECATED> */
/* <DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
> .p-TabBar.p-mod-dragging
.p-TabBar-tab.p-mod-dragging,
/* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
  > .lm-TabBar.lm-mod-dragging
  .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}

/* End tabbar.css */
`,""]),i.d(t,{},{A:n})},1233(e,t,i){var r=i(6758),o=i.n(r),a=i(935),n=i.n(a)()(o());n.push([e.id,`/*

The nouislider.css file is autogenerated from nouislider.less, which imports and wraps the nouislider/src/nouislider.less styles.

MIT License

Copyright (c) 2019 L\xe9on Gersen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/
/* The .widget-slider class is deprecated */
.widget-slider,
.jupyter-widget-slider {
  /* Functional styling;
 * These styles are required for noUiSlider to function.
 * You don't need to change these rules to apply your design.
 */
  /* Wrapper for all connect elements.
 */
  /* Offset direction
 */
  /* Give origins 0 height/width so they don't interfere with clicking the
 * connect elements.
 */
  /* Slider size and handle placement;
 */
  /* Styling;
 * Giving the connect element a border radius causes issues with using transform: scale
 */
  /* Handles and cursors;
 */
  /* Handle stripes;
 */
  /* Disabled state;
 */
  /* Base;
 *
 */
  /* Values;
 *
 */
  /* Markings;
 *
 */
  /* Horizontal layout;
 *
 */
  /* Vertical layout;
 *
 */
  /* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */
  /* Custom CSS for nouislider */
}
.widget-slider .noUi-target,
.jupyter-widget-slider .noUi-target,
.widget-slider .noUi-target *,
.jupyter-widget-slider .noUi-target * {
  -webkit-touch-callout: none;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
  -webkit-user-select: none;
  -ms-touch-action: none;
  touch-action: none;
  -ms-user-select: none;
  -moz-user-select: none;
  user-select: none;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
.widget-slider .noUi-target,
.jupyter-widget-slider .noUi-target {
  position: relative;
}
.widget-slider .noUi-base,
.jupyter-widget-slider .noUi-base,
.widget-slider .noUi-connects,
.jupyter-widget-slider .noUi-connects {
  width: 100%;
  height: 100%;
  position: relative;
  z-index: 1;
}
.widget-slider .noUi-connects,
.jupyter-widget-slider .noUi-connects {
  overflow: hidden;
  z-index: 0;
}
.widget-slider .noUi-connect,
.jupyter-widget-slider .noUi-connect,
.widget-slider .noUi-origin,
.jupyter-widget-slider .noUi-origin {
  will-change: transform;
  position: absolute;
  z-index: 1;
  top: 0;
  right: 0;
  -ms-transform-origin: 0 0;
  -webkit-transform-origin: 0 0;
  -webkit-transform-style: preserve-3d;
  transform-origin: 0 0;
  transform-style: flat;
}
.widget-slider .noUi-connect,
.jupyter-widget-slider .noUi-connect {
  height: 100%;
  width: 100%;
}
.widget-slider .noUi-origin,
.jupyter-widget-slider .noUi-origin {
  height: 10%;
  width: 10%;
}
.widget-slider .noUi-txt-dir-rtl.noUi-horizontal .noUi-origin,
.jupyter-widget-slider .noUi-txt-dir-rtl.noUi-horizontal .noUi-origin {
  left: 0;
  right: auto;
}
.widget-slider .noUi-vertical .noUi-origin,
.jupyter-widget-slider .noUi-vertical .noUi-origin {
  width: 0;
}
.widget-slider .noUi-horizontal .noUi-origin,
.jupyter-widget-slider .noUi-horizontal .noUi-origin {
  height: 0;
}
.widget-slider .noUi-handle,
.jupyter-widget-slider .noUi-handle {
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  position: absolute;
}
.widget-slider .noUi-touch-area,
.jupyter-widget-slider .noUi-touch-area {
  height: 100%;
  width: 100%;
}
.widget-slider .noUi-state-tap .noUi-connect,
.jupyter-widget-slider .noUi-state-tap .noUi-connect,
.widget-slider .noUi-state-tap .noUi-origin,
.jupyter-widget-slider .noUi-state-tap .noUi-origin {
  -webkit-transition: transform 0.3s;
  transition: transform 0.3s;
}
.widget-slider .noUi-state-drag *,
.jupyter-widget-slider .noUi-state-drag * {
  cursor: inherit !important;
}
.widget-slider .noUi-horizontal,
.jupyter-widget-slider .noUi-horizontal {
  height: 18px;
}
.widget-slider .noUi-horizontal .noUi-handle,
.jupyter-widget-slider .noUi-horizontal .noUi-handle {
  width: 34px;
  height: 28px;
  right: -17px;
  top: -6px;
}
.widget-slider .noUi-vertical,
.jupyter-widget-slider .noUi-vertical {
  width: 18px;
}
.widget-slider .noUi-vertical .noUi-handle,
.jupyter-widget-slider .noUi-vertical .noUi-handle {
  width: 28px;
  height: 34px;
  right: -6px;
  top: -17px;
}
.widget-slider .noUi-txt-dir-rtl.noUi-horizontal .noUi-handle,
.jupyter-widget-slider .noUi-txt-dir-rtl.noUi-horizontal .noUi-handle {
  left: -17px;
  right: auto;
}
.widget-slider .noUi-target,
.jupyter-widget-slider .noUi-target {
  background: #FAFAFA;
  border-radius: 4px;
  border: 1px solid #D3D3D3;
  box-shadow: inset 0 1px 1px #F0F0F0, 0 3px 6px -5px #BBB;
}
.widget-slider .noUi-connects,
.jupyter-widget-slider .noUi-connects {
  border-radius: 3px;
}
.widget-slider .noUi-connect,
.jupyter-widget-slider .noUi-connect {
  background: #3FB8AF;
}
.widget-slider .noUi-draggable,
.jupyter-widget-slider .noUi-draggable {
  cursor: ew-resize;
}
.widget-slider .noUi-vertical .noUi-draggable,
.jupyter-widget-slider .noUi-vertical .noUi-draggable {
  cursor: ns-resize;
}
.widget-slider .noUi-handle,
.jupyter-widget-slider .noUi-handle {
  border: 1px solid #D9D9D9;
  border-radius: 3px;
  background: #FFF;
  cursor: default;
  box-shadow: inset 0 0 1px #FFF, inset 0 1px 7px #EBEBEB, 0 3px 6px -3px #BBB;
}
.widget-slider .noUi-active,
.jupyter-widget-slider .noUi-active {
  box-shadow: inset 0 0 1px #FFF, inset 0 1px 7px #DDD, 0 3px 6px -3px #BBB;
}
.widget-slider .noUi-handle:before,
.jupyter-widget-slider .noUi-handle:before,
.widget-slider .noUi-handle:after,
.jupyter-widget-slider .noUi-handle:after {
  content: "";
  display: block;
  position: absolute;
  height: 14px;
  width: 1px;
  background: #E8E7E6;
  left: 14px;
  top: 6px;
}
.widget-slider .noUi-handle:after,
.jupyter-widget-slider .noUi-handle:after {
  left: 17px;
}
.widget-slider .noUi-vertical .noUi-handle:before,
.jupyter-widget-slider .noUi-vertical .noUi-handle:before,
.widget-slider .noUi-vertical .noUi-handle:after,
.jupyter-widget-slider .noUi-vertical .noUi-handle:after {
  width: 14px;
  height: 1px;
  left: 6px;
  top: 14px;
}
.widget-slider .noUi-vertical .noUi-handle:after,
.jupyter-widget-slider .noUi-vertical .noUi-handle:after {
  top: 17px;
}
.widget-slider [disabled] .noUi-connect,
.jupyter-widget-slider [disabled] .noUi-connect {
  background: #B8B8B8;
}
.widget-slider [disabled].noUi-target,
.jupyter-widget-slider [disabled].noUi-target,
.widget-slider [disabled].noUi-handle,
.jupyter-widget-slider [disabled].noUi-handle,
.widget-slider [disabled] .noUi-handle,
.jupyter-widget-slider [disabled] .noUi-handle {
  cursor: not-allowed;
}
.widget-slider .noUi-pips,
.jupyter-widget-slider .noUi-pips,
.widget-slider .noUi-pips *,
.jupyter-widget-slider .noUi-pips * {
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
.widget-slider .noUi-pips,
.jupyter-widget-slider .noUi-pips {
  position: absolute;
  color: #999;
}
.widget-slider .noUi-value,
.jupyter-widget-slider .noUi-value {
  position: absolute;
  white-space: nowrap;
  text-align: center;
}
.widget-slider .noUi-value-sub,
.jupyter-widget-slider .noUi-value-sub {
  color: #ccc;
  font-size: 10px;
}
.widget-slider .noUi-marker,
.jupyter-widget-slider .noUi-marker {
  position: absolute;
  background: #CCC;
}
.widget-slider .noUi-marker-sub,
.jupyter-widget-slider .noUi-marker-sub {
  background: #AAA;
}
.widget-slider .noUi-marker-large,
.jupyter-widget-slider .noUi-marker-large {
  background: #AAA;
}
.widget-slider .noUi-pips-horizontal,
.jupyter-widget-slider .noUi-pips-horizontal {
  padding: 10px 0;
  height: 80px;
  top: 100%;
  left: 0;
  width: 100%;
}
.widget-slider .noUi-value-horizontal,
.jupyter-widget-slider .noUi-value-horizontal {
  -webkit-transform: translate(-50%, 50%);
  transform: translate(-50%, 50%);
}
.noUi-rtl .widget-slider .noUi-value-horizontal,
.noUi-rtl .jupyter-widget-slider .noUi-value-horizontal {
  -webkit-transform: translate(50%, 50%);
  transform: translate(50%, 50%);
}
.widget-slider .noUi-marker-horizontal.noUi-marker,
.jupyter-widget-slider .noUi-marker-horizontal.noUi-marker {
  margin-left: -1px;
  width: 2px;
  height: 5px;
}
.widget-slider .noUi-marker-horizontal.noUi-marker-sub,
.jupyter-widget-slider .noUi-marker-horizontal.noUi-marker-sub {
  height: 10px;
}
.widget-slider .noUi-marker-horizontal.noUi-marker-large,
.jupyter-widget-slider .noUi-marker-horizontal.noUi-marker-large {
  height: 15px;
}
.widget-slider .noUi-pips-vertical,
.jupyter-widget-slider .noUi-pips-vertical {
  padding: 0 10px;
  height: 100%;
  top: 0;
  left: 100%;
}
.widget-slider .noUi-value-vertical,
.jupyter-widget-slider .noUi-value-vertical {
  -webkit-transform: translate(0, -50%);
  transform: translate(0, -50%);
  padding-left: 25px;
}
.noUi-rtl .widget-slider .noUi-value-vertical,
.noUi-rtl .jupyter-widget-slider .noUi-value-vertical {
  -webkit-transform: translate(0, 50%);
  transform: translate(0, 50%);
}
.widget-slider .noUi-marker-vertical.noUi-marker,
.jupyter-widget-slider .noUi-marker-vertical.noUi-marker {
  width: 5px;
  height: 2px;
  margin-top: -1px;
}
.widget-slider .noUi-marker-vertical.noUi-marker-sub,
.jupyter-widget-slider .noUi-marker-vertical.noUi-marker-sub {
  width: 10px;
}
.widget-slider .noUi-marker-vertical.noUi-marker-large,
.jupyter-widget-slider .noUi-marker-vertical.noUi-marker-large {
  width: 15px;
}
.widget-slider .noUi-tooltip,
.jupyter-widget-slider .noUi-tooltip {
  display: block;
  position: absolute;
  border: 1px solid #D9D9D9;
  border-radius: 3px;
  background: #fff;
  color: #000;
  padding: 5px;
  text-align: center;
  white-space: nowrap;
}
.widget-slider .noUi-horizontal .noUi-tooltip,
.jupyter-widget-slider .noUi-horizontal .noUi-tooltip {
  -webkit-transform: translate(-50%, 0);
  transform: translate(-50%, 0);
  left: 50%;
  bottom: 120%;
}
.widget-slider .noUi-vertical .noUi-tooltip,
.jupyter-widget-slider .noUi-vertical .noUi-tooltip {
  -webkit-transform: translate(0, -50%);
  transform: translate(0, -50%);
  top: 50%;
  right: 120%;
}
.widget-slider .noUi-horizontal .noUi-origin > .noUi-tooltip,
.jupyter-widget-slider .noUi-horizontal .noUi-origin > .noUi-tooltip {
  -webkit-transform: translate(50%, 0);
  transform: translate(50%, 0);
  left: auto;
  bottom: 10px;
}
.widget-slider .noUi-vertical .noUi-origin > .noUi-tooltip,
.jupyter-widget-slider .noUi-vertical .noUi-origin > .noUi-tooltip {
  -webkit-transform: translate(0, -18px);
  transform: translate(0, -18px);
  top: auto;
  right: 28px;
}
.widget-slider .noUi-connect,
.jupyter-widget-slider .noUi-connect {
  background: #2196f3;
}
.widget-slider .noUi-horizontal,
.jupyter-widget-slider .noUi-horizontal {
  height: var(--jp-widgets-slider-track-thickness);
}
.widget-slider .noUi-vertical,
.jupyter-widget-slider .noUi-vertical {
  width: var(--jp-widgets-slider-track-thickness);
  height: 100%;
}
.widget-slider .noUi-horizontal .noUi-handle,
.jupyter-widget-slider .noUi-horizontal .noUi-handle {
  width: var(--jp-widgets-slider-handle-size);
  height: var(--jp-widgets-slider-handle-size);
  border-radius: 50%;
  top: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-handle-size)) / 2);
  right: calc(var(--jp-widgets-slider-handle-size) / -2);
}
.widget-slider .noUi-vertical .noUi-handle,
.jupyter-widget-slider .noUi-vertical .noUi-handle {
  height: var(--jp-widgets-slider-handle-size);
  width: var(--jp-widgets-slider-handle-size);
  border-radius: 50%;
  right: calc((var(--jp-widgets-slider-handle-size) - var(--jp-widgets-slider-track-thickness)) / -2);
  top: calc(var(--jp-widgets-slider-handle-size) / -2);
}
.widget-slider .noUi-handle:after,
.jupyter-widget-slider .noUi-handle:after {
  content: none;
}
.widget-slider .noUi-handle:before,
.jupyter-widget-slider .noUi-handle:before {
  content: none;
}
.widget-slider .noUi-target,
.jupyter-widget-slider .noUi-target {
  background: #fafafa;
  border-radius: 4px;
  border: 1px;
  /* box-shadow: inset 0 1px 1px #F0F0F0, 0 3px 6px -5px #BBB; */
}
.widget-slider .ui-slider,
.jupyter-widget-slider .ui-slider {
  border: var(--jp-widgets-slider-border-width) solid var(--jp-layout-color3);
  background: var(--jp-layout-color3);
  box-sizing: border-box;
  position: relative;
  border-radius: 0px;
}
.widget-slider .noUi-handle,
.jupyter-widget-slider .noUi-handle {
  width: var(--jp-widgets-slider-handle-size);
  border: 1px solid #d9d9d9;
  border-radius: 3px;
  background: #fff;
  cursor: default;
  box-shadow: none;
  outline: none;
}
.widget-slider .noUi-target:not([disabled]) .noUi-handle:hover,
.jupyter-widget-slider .noUi-target:not([disabled]) .noUi-handle:hover,
.widget-slider .noUi-target:not([disabled]) .noUi-handle:focus,
.jupyter-widget-slider .noUi-target:not([disabled]) .noUi-handle:focus {
  background-color: var(--jp-widgets-slider-active-handle-color);
  border: var(--jp-widgets-slider-border-width) solid var(--jp-widgets-slider-active-handle-color);
}
.widget-slider [disabled].noUi-target,
.jupyter-widget-slider [disabled].noUi-target {
  opacity: 0.35;
}
.widget-slider .noUi-connects,
.jupyter-widget-slider .noUi-connects {
  overflow: visible;
  z-index: 0;
  background: var(--jp-layout-color3);
}
.widget-slider .noUi-vertical .noUi-connect,
.jupyter-widget-slider .noUi-vertical .noUi-connect {
  width: calc(100% + 2px);
  right: -1px;
}
.widget-slider .noUi-horizontal .noUi-connect,
.jupyter-widget-slider .noUi-horizontal .noUi-connect {
  height: calc(100% + 2px);
  top: -1px;
}
`,""]),i.d(t,{},{A:n})},5946(e,t,i){var r=i(6758),o=i.n(r),a=i(935),n=i.n(a),d=i(9471),s=i(1233),l=i(62),g=i.n(l),p=new URL(i(2426),i.b),c=n()(o());c.i(d.A),c.i(s.A);var u=g()(p);c.push([e.id,`/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*
 * We assume that the CSS variables in
 * https://github.com/jupyterlab/jupyterlab/blob/master/src/default-theme/variables.css
 * have been defined.
 */

:root {
  --jp-widgets-color: var(--jp-content-font-color1);
  --jp-widgets-label-color: var(--jp-widgets-color);
  --jp-widgets-readout-color: var(--jp-widgets-color);
  --jp-widgets-font-size: var(--jp-ui-font-size1);
  --jp-widgets-margin: 2px;
  --jp-widgets-inline-height: 28px;
  --jp-widgets-inline-width: 300px;
  --jp-widgets-inline-width-short: calc(
    var(--jp-widgets-inline-width) / 2 - var(--jp-widgets-margin)
  );
  --jp-widgets-inline-width-tiny: calc(
    var(--jp-widgets-inline-width-short) / 2 - var(--jp-widgets-margin)
  );
  --jp-widgets-inline-margin: 4px; /* margin between inline elements */
  --jp-widgets-inline-label-width: 80px;
  --jp-widgets-border-width: var(--jp-border-width);
  --jp-widgets-vertical-height: 200px;
  --jp-widgets-horizontal-tab-height: 24px;
  --jp-widgets-horizontal-tab-width: 144px;
  --jp-widgets-horizontal-tab-top-border: 2px;
  --jp-widgets-progress-thickness: 20px;
  --jp-widgets-container-padding: 15px;
  --jp-widgets-input-padding: 4px;
  --jp-widgets-radio-item-height-adjustment: 8px;
  --jp-widgets-radio-item-height: calc(
    var(--jp-widgets-inline-height) -
      var(--jp-widgets-radio-item-height-adjustment)
  );
  --jp-widgets-slider-track-thickness: 4px;
  --jp-widgets-slider-border-width: var(--jp-widgets-border-width);
  --jp-widgets-slider-handle-size: 16px;
  --jp-widgets-slider-handle-border-color: var(--jp-border-color1);
  --jp-widgets-slider-handle-background-color: var(--jp-layout-color1);
  --jp-widgets-slider-active-handle-color: var(--jp-brand-color1);
  --jp-widgets-menu-item-height: 24px;
  --jp-widgets-dropdown-arrow: url(${u});
  --jp-widgets-input-color: var(--jp-ui-font-color1);
  --jp-widgets-input-background-color: var(--jp-layout-color1);
  --jp-widgets-input-border-color: var(--jp-border-color1);
  --jp-widgets-input-focus-border-color: var(--jp-brand-color2);
  --jp-widgets-input-border-width: var(--jp-widgets-border-width);
  --jp-widgets-disabled-opacity: 0.6;

  /* From Material Design Lite */
  --md-shadow-key-umbra-opacity: 0.2;
  --md-shadow-key-penumbra-opacity: 0.14;
  --md-shadow-ambient-shadow-opacity: 0.12;
}

.jupyter-widgets {
  margin: var(--jp-widgets-margin);
  box-sizing: border-box;
  color: var(--jp-widgets-color);
  overflow: visible;
}

.jp-Output-result > .jupyter-widgets {
  margin-left: 0;
  margin-right: 0;
}

/* vbox and hbox */

/* <DEPRECATED> */
.widget-inline-hbox, /* </DEPRECATED> */
 .jupyter-widget-inline-hbox {
  /* Horizontal widgets */
  box-sizing: border-box;
  display: flex;
  flex-direction: row;
  align-items: baseline;
}

/* <DEPRECATED> */
.widget-inline-vbox, /* </DEPRECATED> */
 .jupyter-widget-inline-vbox {
  /* Vertical Widgets */
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* <DEPRECATED> */
.widget-box, /* </DEPRECATED> */
.jupyter-widget-box {
  box-sizing: border-box;
  display: flex;
  margin: 0;
  overflow: auto;
}

/* <DEPRECATED> */
.widget-gridbox, /* </DEPRECATED> */
.jupyter-widget-gridbox {
  box-sizing: border-box;
  display: grid;
  margin: 0;
  overflow: auto;
}

/* <DEPRECATED> */
.widget-hbox, /* </DEPRECATED> */
.jupyter-widget-hbox {
  flex-direction: row;
}

/* <DEPRECATED> */
.widget-vbox, /* </DEPRECATED> */
.jupyter-widget-vbox {
  flex-direction: column;
}

/* General Tags Styling */

.jupyter-widget-tagsinput {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  overflow: auto;

  cursor: text;
}

.jupyter-widget-tag {
  padding-left: 10px;
  padding-right: 10px;
  padding-top: 0px;
  padding-bottom: 0px;
  display: inline-block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  text-align: center;
  font-size: var(--jp-widgets-font-size);

  height: calc(var(--jp-widgets-inline-height) - 2px);
  border: 0px solid;
  line-height: calc(var(--jp-widgets-inline-height) - 2px);
  box-shadow: none;

  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color2);
  border-color: var(--jp-border-color2);
  border: none;
  user-select: none;

  cursor: grab;
  transition: margin-left 200ms;
  margin: 1px 1px 1px 1px;
}

.jupyter-widget-tag.mod-active {
  /* MD Lite 4dp shadow */
  box-shadow: 0 4px 5px 0 rgba(0, 0, 0, var(--md-shadow-key-penumbra-opacity)),
    0 1px 10px 0 rgba(0, 0, 0, var(--md-shadow-ambient-shadow-opacity)),
    0 2px 4px -1px rgba(0, 0, 0, var(--md-shadow-key-umbra-opacity));
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color3);
}

.jupyter-widget-colortag {
  color: var(--jp-inverse-ui-font-color1);
}

.jupyter-widget-colortag.mod-active {
  color: var(--jp-inverse-ui-font-color0);
}

.jupyter-widget-taginput {
  color: var(--jp-ui-font-color0);
  background-color: var(--jp-layout-color0);

  cursor: text;
  text-align: left;
}

.jupyter-widget-taginput:focus {
  outline: none;
}

.jupyter-widget-tag-close {
  margin-left: var(--jp-widgets-inline-margin);
  padding: 2px 0px 2px 2px;
}

.jupyter-widget-tag-close:hover {
  cursor: pointer;
}

/* Tag "Primary" Styling */

.jupyter-widget-tag.mod-primary {
  color: var(--jp-inverse-ui-font-color1);
  background-color: var(--jp-brand-color1);
}

.jupyter-widget-tag.mod-primary.mod-active {
  color: var(--jp-inverse-ui-font-color0);
  background-color: var(--jp-brand-color0);
}

/* Tag "Success" Styling */

.jupyter-widget-tag.mod-success {
  color: var(--jp-inverse-ui-font-color1);
  background-color: var(--jp-success-color1);
}

.jupyter-widget-tag.mod-success.mod-active {
  color: var(--jp-inverse-ui-font-color0);
  background-color: var(--jp-success-color0);
}

/* Tag "Info" Styling */

.jupyter-widget-tag.mod-info {
  color: var(--jp-inverse-ui-font-color1);
  background-color: var(--jp-info-color1);
}

.jupyter-widget-tag.mod-info.mod-active {
  color: var(--jp-inverse-ui-font-color0);
  background-color: var(--jp-info-color0);
}

/* Tag "Warning" Styling */

.jupyter-widget-tag.mod-warning {
  color: var(--jp-inverse-ui-font-color1);
  background-color: var(--jp-warn-color1);
}

.jupyter-widget-tag.mod-warning.mod-active {
  color: var(--jp-inverse-ui-font-color0);
  background-color: var(--jp-warn-color0);
}

/* Tag "Danger" Styling */

.jupyter-widget-tag.mod-danger {
  color: var(--jp-inverse-ui-font-color1);
  background-color: var(--jp-error-color1);
}

.jupyter-widget-tag.mod-danger.mod-active {
  color: var(--jp-inverse-ui-font-color0);
  background-color: var(--jp-error-color0);
}

/* General Button Styling */

.jupyter-button {
  padding-left: 10px;
  padding-right: 10px;
  padding-top: 0px;
  padding-bottom: 0px;
  display: inline-block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  text-align: center;
  font-size: var(--jp-widgets-font-size);
  cursor: pointer;

  height: var(--jp-widgets-inline-height);
  border: 0px solid;
  line-height: var(--jp-widgets-inline-height);
  box-shadow: none;

  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color2);
  border-color: var(--jp-border-color2);
  border: none;
  user-select: none;
}

.jupyter-button i.fa {
  margin-right: var(--jp-widgets-inline-margin);
  pointer-events: none;
}

.jupyter-button:empty:before {
  content: '\\200b'; /* zero-width space */
}

.jupyter-widgets.jupyter-button:disabled {
  opacity: var(--jp-widgets-disabled-opacity);
}

.jupyter-button i.fa.center {
  margin-right: 0;
}

.jupyter-button:hover:enabled,
.jupyter-button:focus:enabled {
  /* MD Lite 2dp shadow */
  box-shadow: 0 2px 2px 0 rgba(0, 0, 0, var(--md-shadow-key-penumbra-opacity)),
    0 3px 1px -2px rgba(0, 0, 0, var(--md-shadow-key-umbra-opacity)),
    0 1px 5px 0 rgba(0, 0, 0, var(--md-shadow-ambient-shadow-opacity));
}

.jupyter-button:active,
.jupyter-button.mod-active {
  /* MD Lite 4dp shadow */
  box-shadow: 0 4px 5px 0 rgba(0, 0, 0, var(--md-shadow-key-penumbra-opacity)),
    0 1px 10px 0 rgba(0, 0, 0, var(--md-shadow-ambient-shadow-opacity)),
    0 2px 4px -1px rgba(0, 0, 0, var(--md-shadow-key-umbra-opacity));
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color3);
}

.jupyter-button:focus:enabled {
  outline: 1px solid var(--jp-widgets-input-focus-border-color);
}

/* Button "Primary" Styling */

.jupyter-button.mod-primary {
  color: var(--jp-ui-inverse-font-color1);
  background-color: var(--jp-brand-color1);
}

.jupyter-button.mod-primary.mod-active {
  color: var(--jp-ui-inverse-font-color0);
  background-color: var(--jp-brand-color0);
}

.jupyter-button.mod-primary:active {
  color: var(--jp-ui-inverse-font-color0);
  background-color: var(--jp-brand-color0);
}

/* Button "Success" Styling */

.jupyter-button.mod-success {
  color: var(--jp-ui-inverse-font-color1);
  background-color: var(--jp-success-color1);
}

.jupyter-button.mod-success.mod-active {
  color: var(--jp-ui-inverse-font-color0);
  background-color: var(--jp-success-color0);
}

.jupyter-button.mod-success:active {
  color: var(--jp-ui-inverse-font-color0);
  background-color: var(--jp-success-color0);
}

/* Button "Info" Styling */

.jupyter-button.mod-info {
  color: var(--jp-ui-inverse-font-color1);
  background-color: var(--jp-info-color1);
}

.jupyter-button.mod-info.mod-active {
  color: var(--jp-ui-inverse-font-color0);
  background-color: var(--jp-info-color0);
}

.jupyter-button.mod-info:active {
  color: var(--jp-ui-inverse-font-color0);
  background-color: var(--jp-info-color0);
}

/* Button "Warning" Styling */

.jupyter-button.mod-warning {
  color: var(--jp-ui-inverse-font-color1);
  background-color: var(--jp-warn-color1);
}

.jupyter-button.mod-warning.mod-active {
  color: var(--jp-ui-inverse-font-color0);
  background-color: var(--jp-warn-color0);
}

.jupyter-button.mod-warning:active {
  color: var(--jp-ui-inverse-font-color0);
  background-color: var(--jp-warn-color0);
}

/* Button "Danger" Styling */

.jupyter-button.mod-danger {
  color: var(--jp-ui-inverse-font-color1);
  background-color: var(--jp-error-color1);
}

.jupyter-button.mod-danger.mod-active {
  color: var(--jp-ui-inverse-font-color0);
  background-color: var(--jp-error-color0);
}

.jupyter-button.mod-danger:active {
  color: var(--jp-ui-inverse-font-color0);
  background-color: var(--jp-error-color0);
}

/* Widget Button, Widget Toggle Button, Widget Upload */

/* <DEPRECATED> */
.widget-button, /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-toggle-button, /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-upload, /* </DEPRECATED> */
.jupyter-widget-button,
.jupyter-widget-toggle-button,
.jupyter-widget-upload {
  width: var(--jp-widgets-inline-width-short);
}

/* Widget Label Styling */

/* Override Bootstrap label css */
.jupyter-widgets label {
  margin-bottom: initial;
}

/* <DEPRECATED> */
.widget-label-basic, /* </DEPRECATED> */
.jupyter-widget-label-basic {
  /* Basic Label */
  color: var(--jp-widgets-label-color);
  font-size: var(--jp-widgets-font-size);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  line-height: var(--jp-widgets-inline-height);
}

/* <DEPRECATED> */
.widget-label, /* </DEPRECATED> */
.jupyter-widget-label {
  /* Label */
  color: var(--jp-widgets-label-color);
  font-size: var(--jp-widgets-font-size);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  line-height: var(--jp-widgets-inline-height);
}

/* <DEPRECATED> */
.widget-inline-hbox .widget-label, /* </DEPRECATED> */
.jupyter-widget-inline-hbox .jupyter-widget-label {
  /* Horizontal Widget Label */
  color: var(--jp-widgets-label-color);
  text-align: right;
  margin-right: calc(var(--jp-widgets-inline-margin) * 2);
  width: var(--jp-widgets-inline-label-width);
  flex-shrink: 0;
}

/* <DEPRECATED> */
.widget-inline-vbox .widget-label, /* </DEPRECATED> */
.jupyter-widget-inline-vbox .jupyter-widget-label {
  /* Vertical Widget Label */
  color: var(--jp-widgets-label-color);
  text-align: center;
  line-height: var(--jp-widgets-inline-height);
}

/* Widget Readout Styling */

/* <DEPRECATED> */
.widget-readout, /* </DEPRECATED> */
.jupyter-widget-readout {
  color: var(--jp-widgets-readout-color);
  font-size: var(--jp-widgets-font-size);
  height: var(--jp-widgets-inline-height);
  line-height: var(--jp-widgets-inline-height);
  overflow: hidden;
  white-space: nowrap;
  text-align: center;
}

/* <DEPRECATED> */
.widget-readout.overflow, /* </DEPRECATED> */
.jupyter-widget-readout.overflow {
  /* Overflowing Readout */

  /* From Material Design Lite
        shadow-key-umbra-opacity: 0.2;
        shadow-key-penumbra-opacity: 0.14;
        shadow-ambient-shadow-opacity: 0.12;
     */
  -webkit-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2),
    0 3px 1px -2px rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12);

  -moz-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2),
    0 3px 1px -2px rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12);

  box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2), 0 3px 1px -2px rgba(0, 0, 0, 0.14),
    0 1px 5px 0 rgba(0, 0, 0, 0.12);
}

/* <DEPRECATED> */
.widget-inline-hbox .widget-readout, /* </DEPRECATED> */
.jupyter-widget-inline-hbox .jupyter-widget-readout {
  /* Horizontal Readout */
  text-align: center;
  max-width: var(--jp-widgets-inline-width-short);
  min-width: var(--jp-widgets-inline-width-tiny);
  margin-left: var(--jp-widgets-inline-margin);
}

/* <DEPRECATED> */
.widget-inline-vbox .widget-readout, /* </DEPRECATED> */
.jupyter-widget-inline-vbox .jupyter-widget-readout {
  /* Vertical Readout */
  margin-top: var(--jp-widgets-inline-margin);
  /* as wide as the widget */
  width: inherit;
}

/* Widget Checkbox Styling */

/* <DEPRECATED> */
.widget-checkbox, /* </DEPRECATED> */
.jupyter-widget-checkbox {
  width: var(--jp-widgets-inline-width);
  height: var(--jp-widgets-inline-height);
  line-height: var(--jp-widgets-inline-height);
}

/* <DEPRECATED> */
.widget-checkbox input[type='checkbox'], /* </DEPRECATED> */
.jupyter-widget-checkbox input[type='checkbox'] {
  margin: 0px calc(var(--jp-widgets-inline-margin) * 2) 0px 0px;
  line-height: var(--jp-widgets-inline-height);
  font-size: large;
  flex-grow: 1;
  flex-shrink: 0;
  align-self: center;
}

/* Widget Valid Styling */

/* <DEPRECATED> */
.widget-valid, /* </DEPRECATED> */
.jupyter-widget-valid {
  height: var(--jp-widgets-inline-height);
  line-height: var(--jp-widgets-inline-height);
  width: var(--jp-widgets-inline-width-short);
  font-size: var(--jp-widgets-font-size);
}

/* <DEPRECATED> */
.widget-valid i, /* </DEPRECATED> */
.jupyter-widget-valid i {
  line-height: var(--jp-widgets-inline-height);
  margin-right: var(--jp-widgets-inline-margin);
  margin-left: var(--jp-widgets-inline-margin);
}

/* <DEPRECATED> */
.widget-valid.mod-valid i, /* </DEPRECATED> */
.jupyter-widget-valid.mod-valid i {
  color: green;
}

/* <DEPRECATED> */
.widget-valid.mod-invalid i, /* </DEPRECATED> */
.jupyter-widget-valid.mod-invalid i {
  color: red;
}

/* <DEPRECATED> */
.widget-valid.mod-valid .widget-valid-readout, /* </DEPRECATED> */
.jupyter-widget-valid.mod-valid .jupyter-widget-valid-readout {
  display: none;
}

/* Widget Text and TextArea Styling */

/* <DEPRECATED> */
.widget-textarea, /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-text, /* </DEPRECATED> */
.jupyter-widget-textarea,
.jupyter-widget-text {
  width: var(--jp-widgets-inline-width);
}

/* <DEPRECATED> */
.widget-text input[type='text'], /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-text input[type='number'], /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-text input[type='password'], /* </DEPRECATED> */
.jupyter-widget-text input[type='text'],
.jupyter-widget-text input[type='number'],
.jupyter-widget-text input[type='password'] {
  height: var(--jp-widgets-inline-height);
}

/* <DEPRECATED> */
.widget-text input[type='text']:disabled, /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-text input[type='number']:disabled, /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-text input[type='password']:disabled, /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-textarea textarea:disabled, /* </DEPRECATED> */
.jupyter-widget-text input[type='text']:disabled,
.jupyter-widget-text input[type='number']:disabled,
.jupyter-widget-text input[type='password']:disabled,
.jupyter-widget-textarea textarea:disabled {
  opacity: var(--jp-widgets-disabled-opacity);
}

/* <DEPRECATED> */
.widget-text input[type='text'], /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-text input[type='number'], /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-text input[type='password'], /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-textarea textarea, /* </DEPRECATED> */
.jupyter-widget-text input[type='text'],
.jupyter-widget-text input[type='number'],
.jupyter-widget-text input[type='password'],
.jupyter-widget-textarea textarea {
  box-sizing: border-box;
  border: var(--jp-widgets-input-border-width) solid
    var(--jp-widgets-input-border-color);
  background-color: var(--jp-widgets-input-background-color);
  color: var(--jp-widgets-input-color);
  font-size: var(--jp-widgets-font-size);
  flex-grow: 1;
  min-width: 0; /* This makes it possible for the flexbox to shrink this input */
  flex-shrink: 1;
  outline: none !important;
}

/* <DEPRECATED> */
.widget-text input[type='text'], /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-text input[type='password'], /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-textarea textarea, /* </DEPRECATED> */
.jupyter-widget-text input[type='text'],
.jupyter-widget-text input[type='password'],
.jupyter-widget-textarea textarea {
  padding: var(--jp-widgets-input-padding)
    calc(var(--jp-widgets-input-padding) * 2);
}

/* <DEPRECATED> */
.widget-text input[type='number'], /* </DEPRECATED> */
.jupyter-widget-text input[type='number'] {
  padding: var(--jp-widgets-input-padding) 0 var(--jp-widgets-input-padding)
    calc(var(--jp-widgets-input-padding) * 2);
}

/* <DEPRECATED> */
.widget-textarea textarea, /* </DEPRECATED> */
.jupyter-widget-textarea textarea {
  height: inherit;
  width: inherit;
}

/* <DEPRECATED> */
.widget-text input:focus, /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-textarea textarea:focus, /* </DEPRECATED> */
.jupyter-widget-text input:focus,
.jupyter-widget-textarea textarea:focus {
  border-color: var(--jp-widgets-input-focus-border-color);
}

/* Horizontal Slider */
/* <DEPRECATED> */
.widget-hslider, /* </DEPRECATED> */
.jupyter-widget-hslider {
  width: var(--jp-widgets-inline-width);
  height: var(--jp-widgets-inline-height);
  line-height: var(--jp-widgets-inline-height);

  /* Override the align-items baseline. This way, the description and readout
    still seem to align their baseline properly, and we don't have to have
    align-self: stretch in the .slider-container. */
  align-items: center;
}

/* <DEPRECATED> */
.widgets-slider .slider-container, /* </DEPRECATED> */
.jupyter-widgets-slider .slider-container {
  overflow: visible;
}

/* <DEPRECATED> */
.widget-hslider .slider-container, /* </DEPRECATED> */
.jupyter-widget-hslider .slider-container {
  margin-left: calc(
    var(--jp-widgets-slider-handle-size) / 2 - 2 *
      var(--jp-widgets-slider-border-width)
  );
  margin-right: calc(
    var(--jp-widgets-slider-handle-size) / 2 - 2 *
      var(--jp-widgets-slider-border-width)
  );
  flex: 1 1 var(--jp-widgets-inline-width-short);
}

/* Vertical Slider */

/* <DEPRECATED> */
.widget-vbox .widget-label, /* </DEPRECATED> */
.jupyter-widget-vbox .jupyter-widget-label {
  height: var(--jp-widgets-inline-height);
  line-height: var(--jp-widgets-inline-height);
}

/* <DEPRECATED> */
.widget-vslider, /* </DEPRECATED> */
.jupyter-widget-vslider {
  /* Vertical Slider */
  height: var(--jp-widgets-vertical-height);
  width: var(--jp-widgets-inline-width-tiny);
}

/* <DEPRECATED> */
.widget-vslider .slider-container, /* </DEPRECATED> */
.jupyter-widget-vslider .slider-container {
  flex: 1 1 var(--jp-widgets-inline-width-short);
  margin-left: auto;
  margin-right: auto;
  margin-bottom: calc(
    var(--jp-widgets-slider-handle-size) / 2 - 2 *
      var(--jp-widgets-slider-border-width)
  );
  margin-top: calc(
    var(--jp-widgets-slider-handle-size) / 2 - 2 *
      var(--jp-widgets-slider-border-width)
  );
  display: flex;
  flex-direction: column;
}

/* Widget Progress Styling */

.progress-bar {
  -webkit-transition: none;
  -moz-transition: none;
  -ms-transition: none;
  -o-transition: none;
  transition: none;
}

.progress-bar {
  height: var(--jp-widgets-inline-height);
}

.progress-bar {
  background-color: var(--jp-brand-color1);
}

.progress-bar-success {
  background-color: var(--jp-success-color1);
}

.progress-bar-info {
  background-color: var(--jp-info-color1);
}

.progress-bar-warning {
  background-color: var(--jp-warn-color1);
}

.progress-bar-danger {
  background-color: var(--jp-error-color1);
}

.progress {
  background-color: var(--jp-layout-color2);
  border: none;
  box-shadow: none;
}

/* Horisontal Progress */

/* <DEPRECATED> */
.widget-hprogress, /* </DEPRECATED> */
.jupyter-widget-hprogress {
  /* Progress Bar */
  height: var(--jp-widgets-inline-height);
  line-height: var(--jp-widgets-inline-height);
  width: var(--jp-widgets-inline-width);
  align-items: center;
}

/* <DEPRECATED> */
.widget-hprogress .progress, /* </DEPRECATED> */
.jupyter-widget-hprogress .progress {
  flex-grow: 1;
  margin-top: var(--jp-widgets-input-padding);
  margin-bottom: var(--jp-widgets-input-padding);
  align-self: stretch;
  /* Override bootstrap style */
  height: initial;
}

/* Vertical Progress */

/* <DEPRECATED> */
.widget-vprogress, /* </DEPRECATED> */
.jupyter-widget-vprogress {
  height: var(--jp-widgets-vertical-height);
  width: var(--jp-widgets-inline-width-tiny);
}

/* <DEPRECATED> */
.widget-vprogress .progress, /* </DEPRECATED> */
.jupyter-widget-vprogress .progress {
  flex-grow: 1;
  width: var(--jp-widgets-progress-thickness);
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 0;
}

/* Select Widget Styling */

/* <DEPRECATED> */
.widget-dropdown, /* </DEPRECATED> */
.jupyter-widget-dropdown {
  height: var(--jp-widgets-inline-height);
  width: var(--jp-widgets-inline-width);
  line-height: var(--jp-widgets-inline-height);
}

/* <DEPRECATED> */
.widget-dropdown > select, /* </DEPRECATED> */
.jupyter-widget-dropdown > select {
  padding-right: 20px;
  border: var(--jp-widgets-input-border-width) solid
    var(--jp-widgets-input-border-color);
  border-radius: 0;
  height: inherit;
  flex: 1 1 var(--jp-widgets-inline-width-short);
  min-width: 0; /* This makes it possible for the flexbox to shrink this input */
  box-sizing: border-box;
  outline: none !important;
  box-shadow: none;
  background-color: var(--jp-widgets-input-background-color);
  color: var(--jp-widgets-input-color);
  font-size: var(--jp-widgets-font-size);
  vertical-align: top;
  padding-left: calc(var(--jp-widgets-input-padding) * 2);
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  background-repeat: no-repeat;
  background-size: 20px;
  background-position: right center;
  background-image: var(--jp-widgets-dropdown-arrow);
}
/* <DEPRECATED> */
.widget-dropdown > select:focus, /* </DEPRECATED> */
.jupyter-widget-dropdown > select:focus {
  border-color: var(--jp-widgets-input-focus-border-color);
}

/* <DEPRECATED> */
.widget-dropdown > select:disabled, /* </DEPRECATED> */
.jupyter-widget-dropdown > select:disabled {
  opacity: var(--jp-widgets-disabled-opacity);
}

/* To disable the dotted border in Firefox around select controls.
   See http://stackoverflow.com/a/18853002 */
/* <DEPRECATED> */
.widget-dropdown > select:-moz-focusring, /* </DEPRECATED> */
.jupyter-widget-dropdown > select:-moz-focusring {
  color: transparent;
  text-shadow: 0 0 0 #000;
}

/* Select and SelectMultiple */

/* <DEPRECATED> */
.widget-select, /* </DEPRECATED> */
.jupyter-widget-select {
  width: var(--jp-widgets-inline-width);
  line-height: var(--jp-widgets-inline-height);

  /* Because Firefox defines the baseline of a select as the bottom of the
    control, we align the entire control to the top and add padding to the
    select to get an approximate first line baseline alignment. */
  align-items: flex-start;
}

/* <DEPRECATED> */
.widget-select > select, /* </DEPRECATED> */
.jupyter-widget-select > select {
  border: var(--jp-widgets-input-border-width) solid
    var(--jp-widgets-input-border-color);
  background-color: var(--jp-widgets-input-background-color);
  color: var(--jp-widgets-input-color);
  font-size: var(--jp-widgets-font-size);
  flex: 1 1 var(--jp-widgets-inline-width-short);
  outline: none !important;
  overflow: auto;
  height: inherit;

  /* Because Firefox defines the baseline of a select as the bottom of the
    control, we align the entire control to the top and add padding to the
    select to get an approximate first line baseline alignment. */
  padding-top: 5px;
}

/* <DEPRECATED> */
.widget-select > select:focus, /* </DEPRECATED> */
.jupyter-widget-select > select:focus {
  border-color: var(--jp-widgets-input-focus-border-color);
}

.wiget-select > select > option,
.jupyter-wiget-select > select > option {
  padding-left: var(--jp-widgets-input-padding);
  line-height: var(--jp-widgets-inline-height);
  /* line-height doesn't work on some browsers for select options */
  padding-top: calc(
    var(--jp-widgets-inline-height) - var(--jp-widgets-font-size) / 2
  );
  padding-bottom: calc(
    var(--jp-widgets-inline-height) - var(--jp-widgets-font-size) / 2
  );
}

/* Toggle Buttons Styling */

/* <DEPRECATED> */
.widget-toggle-buttons, /* </DEPRECATED> */
.jupyter-widget-toggle-buttons {
  line-height: var(--jp-widgets-inline-height);
}

/* <DEPRECATED> */
.widget-toggle-buttons .widget-toggle-button, /* </DEPRECATED> */
.jupyter-widget-toggle-buttons .jupyter-widget-toggle-button {
  margin-left: var(--jp-widgets-margin);
  margin-right: var(--jp-widgets-margin);
}

/* <DEPRECATED> */
.widget-toggle-buttons .jupyter-button:disabled, /* </DEPRECATED> */
.jupyter-widget-toggle-buttons .jupyter-button:disabled {
  opacity: var(--jp-widgets-disabled-opacity);
}

/* Radio Buttons Styling */

/* <DEPRECATED> */
.widget-radio, /* </DEPRECATED> */
.jupyter-widget-radio {
  width: var(--jp-widgets-inline-width);
  line-height: var(--jp-widgets-inline-height);
}

/* <DEPRECATED> */
.widget-radio-box, /* </DEPRECATED> */
.jupyter-widget-radio-box {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  box-sizing: border-box;
  flex-grow: 1;
  margin-bottom: var(--jp-widgets-radio-item-height-adjustment);
}

/* <DEPRECATED> */
.widget-radio-box-vertical, /* </DEPRECATED> */
.jupyter-widget-radio-box-vertical {
  flex-direction: column;
}

/* <DEPRECATED> */
.widget-radio-box-horizontal, /* </DEPRECATED> */
.jupyter-widget-radio-box-horizontal {
  flex-direction: row;
}

/* <DEPRECATED> */
.widget-radio-box label, /* </DEPRECATED> */
.jupyter-widget-radio-box label {
  height: var(--jp-widgets-radio-item-height);
  line-height: var(--jp-widgets-radio-item-height);
  font-size: var(--jp-widgets-font-size);
}

.widget-radio-box-horizontal label,
.jupyter-widget-radio-box-horizontal label {
  margin: 0 calc(var(--jp-widgets-input-padding) * 2) 0 0;
}

/* <DEPRECATED> */
.widget-radio-box input, /* </DEPRECATED> */
.jupyter-widget-radio-box input {
  height: var(--jp-widgets-radio-item-height);
  line-height: var(--jp-widgets-radio-item-height);
  margin: 0 calc(var(--jp-widgets-input-padding) * 2) 0 1px;
  float: left;
}

/* Color Picker Styling */

/* <DEPRECATED> */
.widget-colorpicker, /* </DEPRECATED> */
.jupyter-widget-colorpicker {
  width: var(--jp-widgets-inline-width);
  height: var(--jp-widgets-inline-height);
  line-height: var(--jp-widgets-inline-height);
}

/* <DEPRECATED> */
.widget-colorpicker > .widget-colorpicker-input, /* </DEPRECATED> */
.jupyter-widget-colorpicker > .jupyter-widget-colorpicker-input {
  flex-grow: 1;
  flex-shrink: 1;
  min-width: var(--jp-widgets-inline-width-tiny);
}

/* <DEPRECATED> */
.widget-colorpicker input[type='color'], /* </DEPRECATED> */
.jupyter-widget-colorpicker input[type='color'] {
  width: var(--jp-widgets-inline-height);
  height: var(--jp-widgets-inline-height);
  padding: 0 2px; /* make the color square actually square on Chrome on OS X */
  background: var(--jp-widgets-input-background-color);
  color: var(--jp-widgets-input-color);
  border: var(--jp-widgets-input-border-width) solid
    var(--jp-widgets-input-border-color);
  border-left: none;
  flex-grow: 0;
  flex-shrink: 0;
  box-sizing: border-box;
  align-self: stretch;
  outline: none !important;
}

/* <DEPRECATED> */
.widget-colorpicker.concise input[type='color'], /* </DEPRECATED> */
.jupyter-widget-colorpicker.concise input[type='color'] {
  border-left: var(--jp-widgets-input-border-width) solid
    var(--jp-widgets-input-border-color);
}

/* <DEPRECATED> */
.widget-colorpicker input[type='color']:focus, /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-colorpicker input[type='text']:focus, /* </DEPRECATED> */
.jupyter-widget-colorpicker input[type='color']:focus,
.jupyter-widget-colorpicker input[type='text']:focus {
  border-color: var(--jp-widgets-input-focus-border-color);
}

/* <DEPRECATED> */
.widget-colorpicker input[type='text'], /* </DEPRECATED> */
.jupyter-widget-colorpicker input[type='text'] {
  flex-grow: 1;
  outline: none !important;
  height: var(--jp-widgets-inline-height);
  line-height: var(--jp-widgets-inline-height);
  background: var(--jp-widgets-input-background-color);
  color: var(--jp-widgets-input-color);
  border: var(--jp-widgets-input-border-width) solid
    var(--jp-widgets-input-border-color);
  font-size: var(--jp-widgets-font-size);
  padding: var(--jp-widgets-input-padding)
    calc(var(--jp-widgets-input-padding) * 2);
  min-width: 0; /* This makes it possible for the flexbox to shrink this input */
  flex-shrink: 1;
  box-sizing: border-box;
}

/* <DEPRECATED> */
.widget-colorpicker input[type='text']:disabled, /* </DEPRECATED> */
.jupyter-widget-colorpicker input[type='text']:disabled {
  opacity: var(--jp-widgets-disabled-opacity);
}

/* Date Picker Styling */

/* <DEPRECATED> */
.widget-datepicker, /* </DEPRECATED> */
.jupyter-widget-datepicker {
  width: var(--jp-widgets-inline-width);
  height: var(--jp-widgets-inline-height);
  line-height: var(--jp-widgets-inline-height);
}

/* <DEPRECATED> */
.widget-datepicker input[type='date'], /* </DEPRECATED> */
.jupyter-widget-datepicker input[type='date'] {
  flex-grow: 1;
  flex-shrink: 1;
  min-width: 0; /* This makes it possible for the flexbox to shrink this input */
  outline: none !important;
  height: var(--jp-widgets-inline-height);
  border: var(--jp-widgets-input-border-width) solid
    var(--jp-widgets-input-border-color);
  background-color: var(--jp-widgets-input-background-color);
  color: var(--jp-widgets-input-color);
  font-size: var(--jp-widgets-font-size);
  padding: var(--jp-widgets-input-padding)
    calc(var(--jp-widgets-input-padding) * 2);
  box-sizing: border-box;
}

/* <DEPRECATED> */
.widget-datepicker input[type='date']:focus, /* </DEPRECATED> */
.jupyter-widget-datepicker input[type='date']:focus {
  border-color: var(--jp-widgets-input-focus-border-color);
}

/* <DEPRECATED> */
.widget-datepicker input[type='date']:invalid, /* </DEPRECATED> */
.jupyter-widget-datepicker input[type='date']:invalid {
  border-color: var(--jp-warn-color1);
}

/* <DEPRECATED> */
.widget-datepicker input[type='date']:disabled, /* </DEPRECATED> */
.jupyter-widget-datepicker input[type='date']:disabled {
  opacity: var(--jp-widgets-disabled-opacity);
}

/* Play Widget */

/* <DEPRECATED> */
.widget-play, /* </DEPRECATED> */
.jupyter-widget-play {
  width: var(--jp-widgets-inline-width-short);
  display: flex;
  align-items: stretch;
}

/* <DEPRECATED> */
.widget-play .jupyter-button, /* </DEPRECATED> */
.jupyter-widget-play .jupyter-button {
  flex-grow: 1;
  height: auto;
}

/* <DEPRECATED> */
.widget-play .jupyter-button:disabled, /* </DEPRECATED> */
.jupyter-widget-play .jupyter-button:disabled {
  opacity: var(--jp-widgets-disabled-opacity);
}

/* Tab Widget */

/* <DEPRECATED> */
.jupyter-widgets.widget-tab, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab {
  display: flex;
  flex-direction: column;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar, /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar {
  /* Necessary so that a tab can be shifted down to overlay the border of the box below. */
  overflow-x: visible;
  overflow-y: visible;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar > .p-TabBar-content, /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar > .p-TabBar-content, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar > .lm-TabBar-content {
  /* Make sure that the tab grows from bottom up */
  align-items: flex-end;
  min-width: 0;
  min-height: 0;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .widget-tab-contents, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .widget-tab-contents {
  width: 100%;
  box-sizing: border-box;
  margin: 0;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding: var(--jp-widgets-container-padding);
  flex-grow: 1;
  overflow: auto;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar, /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar {
  font: var(--jp-widgets-font-size) Helvetica, Arial, sans-serif;
  min-height: calc(
    var(--jp-widgets-horizontal-tab-height) + var(--jp-border-width)
  );
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab, /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar .p-TabBar-tab, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar .lm-TabBar-tab {
  flex: 0 1 var(--jp-widgets-horizontal-tab-width);
  min-width: 35px;
  min-height: calc(
    var(--jp-widgets-horizontal-tab-height) + var(--jp-border-width)
  );
  line-height: var(--jp-widgets-horizontal-tab-height);
  margin-left: calc(-1 * var(--jp-border-width));
  padding: 0px 10px;
  background: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
  border: var(--jp-border-width) solid var(--jp-border-color1);
  border-bottom: none;
  position: relative;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current, /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar .lm-TabBar-tab.lm-mod-current {
  color: var(--jp-ui-font-color0);
  /* We want the background to match the tab content background */
  background: var(--jp-layout-color1);
  min-height: calc(
    var(--jp-widgets-horizontal-tab-height) + 2 * var(--jp-border-width)
  );
  transform: translateY(var(--jp-border-width));
  overflow: visible;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current:before, /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current:before, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar .lm-TabBar-tab.lm-mod-current:before {
  position: absolute;
  top: calc(-1 * var(--jp-border-width));
  left: calc(-1 * var(--jp-border-width));
  content: '';
  height: var(--jp-widgets-horizontal-tab-top-border);
  width: calc(100% + 2 * var(--jp-border-width));
  background: var(--jp-brand-color1);
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab:first-child, /* </DEPRECATED> */
/* <DEPRECATED> */.jupyter-widgets.jupyter-widget-tab > .p-TabBar .p-TabBar-tab:first-child, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar .lm-TabBar-tab:first-child {
  margin-left: 0;
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab
  > .p-TabBar
  .p-TabBar-tab:hover:not(.p-mod-current),
/* </DEPRECATED> */
/* <DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
  > .p-TabBar
  .p-TabBar-tab:hover:not(.p-mod-current),
/* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
  > .lm-TabBar
  .lm-TabBar-tab:hover:not(.lm-mod-current) {
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab
  > .p-TabBar
  .p-mod-closable
  > .p-TabBar-tabCloseIcon,
/* </DEPRECATED> */
/* <DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
> .p-TabBar
.p-mod-closable
> .p-TabBar-tabCloseIcon,
/* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
  > .lm-TabBar
  .lm-mod-closable
  > .lm-TabBar-tabCloseIcon {
  margin-left: 4px;
}

/* This font-awesome strategy may not work across FA4 and FA5, but we don't
actually support closable tabs, so it really doesn't matter */
/* <DEPRECATED> */
.jupyter-widgets.widget-tab
  > .p-TabBar
  .p-mod-closable
  > .p-TabBar-tabCloseIcon:before,
/* </DEPRECATED> */
/* <DEPRECATED> */
.jupyter-widgets.jupyter-widget-widget-tab
> .p-TabBar
.p-mod-closable
> .p-TabBar-tabCloseIcon:before,
/* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab
  > .lm-TabBar
  .lm-mod-closable
  > .lm-TabBar-tabCloseIcon:before {
  font-family: FontAwesome;
  content: '\\f00d'; /* close */
}

/* <DEPRECATED> */
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabIcon, /* </DEPRECATED> */
/* <DEPRECATED> */ .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabLabel, /* </DEPRECATED> */
/* <DEPRECATED> */ .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabCloseIcon, /* </DEPRECATED> */
/* <DEPRECATED> */ .jupyter-widgets.jupyter-widget-tab > .p-TabBar .p-TabBar-tabIcon, /* </DEPRECATED> */
/* <DEPRECATED> */ .jupyter-widgets.jupyter-widget-tab > .p-TabBar .p-TabBar-tabLabel, /* </DEPRECATED> */
/* <DEPRECATED> */ .jupyter-widgets.jupyter-widget-tab > .p-TabBar .p-TabBar-tabCloseIcon, /* </DEPRECATED> */
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar .lm-TabBar-tabIcon,
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar .lm-TabBar-tabLabel,
.jupyter-widgets.jupyter-widget-tab > .lm-TabBar .lm-TabBar-tabCloseIcon {
  line-height: var(--jp-widgets-horizontal-tab-height);
}

/* Accordion Widget */

.jupyter-widget-Collapse {
  display: flex;
  flex-direction: column;
  align-items: stretch;
}

.jupyter-widget-Collapse-header {
  padding: var(--jp-widgets-input-padding);
  cursor: pointer;
  color: var(--jp-ui-font-color2);
  background-color: var(--jp-layout-color2);
  border: var(--jp-widgets-border-width) solid var(--jp-border-color1);
  padding: calc(var(--jp-widgets-container-padding) * 2 / 3)
    var(--jp-widgets-container-padding);
  font-weight: bold;
}

.jupyter-widget-Collapse-header:hover {
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
}

.jupyter-widget-Collapse-open > .jupyter-widget-Collapse-header {
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color0);
  cursor: default;
  border-bottom: none;
}

.jupyter-widget-Collapse-contents {
  padding: var(--jp-widgets-container-padding);
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  border-left: var(--jp-widgets-border-width) solid var(--jp-border-color1);
  border-right: var(--jp-widgets-border-width) solid var(--jp-border-color1);
  border-bottom: var(--jp-widgets-border-width) solid var(--jp-border-color1);
  overflow: auto;
}

.jupyter-widget-Accordion {
  display: flex;
  flex-direction: column;
  align-items: stretch;
}

.jupyter-widget-Accordion .jupyter-widget-Collapse {
  margin-bottom: 0;
}

.jupyter-widget-Accordion .jupyter-widget-Collapse + .jupyter-widget-Collapse {
  margin-top: 4px;
}

/* HTML widget */

/* <DEPRECATED> */
.widget-html, /* </DEPRECATED> */
/* <DEPRECATED> */ .widget-htmlmath, /* </DEPRECATED> */
.jupyter-widget-html,
.jupyter-widget-htmlmath {
  font-size: var(--jp-widgets-font-size);
}

/* <DEPRECATED> */
.widget-html > .widget-html-content, /* </DEPRECATED> */
/* <DEPRECATED> */.widget-htmlmath > .widget-html-content, /* </DEPRECATED> */
.jupyter-widget-html > .jupyter-widget-html-content,
.jupyter-widget-htmlmath > .jupyter-widget-html-content {
  /* Fill out the area in the HTML widget */
  align-self: stretch;
  flex-grow: 1;
  flex-shrink: 1;
  /* Makes sure the baseline is still aligned with other elements */
  line-height: var(--jp-widgets-inline-height);
  /* Make it possible to have absolutely-positioned elements in the html */
  position: relative;
}

/* Image widget  */

/* <DEPRECATED> */
.widget-image, /* </DEPRECATED> */
.jupyter-widget-image {
  max-width: 100%;
  height: auto;
}
`,""]),i.d(t,{},{A:c})},935(e){e.exports=function(e){var t=[];return t.toString=function(){return this.map(function(t){var i="",r=void 0!==t[5];return t[4]&&(i+="@supports (".concat(t[4],") {")),t[2]&&(i+="@media ".concat(t[2]," {")),r&&(i+="@layer".concat(t[5].length>0?" ".concat(t[5]):""," {")),i+=e(t),r&&(i+="}"),t[2]&&(i+="}"),t[4]&&(i+="}"),i}).join("")},t.i=function(e,i,r,o,a){"string"==typeof e&&(e=[[null,e,void 0]]);var n={};if(r)for(var d=0;d<this.length;d++){var s=this[d][0];null!=s&&(n[s]=!0)}for(var l=0;l<e.length;l++){var g=[].concat(e[l]);r&&n[g[0]]||(void 0!==a&&(void 0===g[5]||(g[1]="@layer".concat(g[5].length>0?" ".concat(g[5]):""," {").concat(g[1],"}")),g[5]=a),i&&(g[2]&&(g[1]="@media ".concat(g[2]," {").concat(g[1],"}")),g[2]=i),o&&(g[4]?(g[1]="@supports (".concat(g[4],") {").concat(g[1],"}"),g[4]=o):g[4]="".concat(o)),t.push(g))}},t}},62(e){e.exports=function(e,t){return(t||(t={}),e&&(e=String(e.__esModule?e.default:e),/^['"].*['"]$/.test(e)&&(e=e.slice(1,-1)),t.hash&&(e+=t.hash),/["'() \t\n]|(%20)/.test(e)||t.needQuotes))?'"'.concat(e.replace(/"/g,'\\"').replace(/\n/g,"\\n"),'"'):e}},6758(e){e.exports=function(e){return e[1]}},2591(e){var t=[];function i(e){for(var i=-1,r=0;r<t.length;r++)if(t[r].identifier===e){i=r;break}return i}function r(e,r){for(var o={},a=[],n=0;n<e.length;n++){var d=e[n],s=r.base?d[0]+r.base:d[0],l=o[s]||0,g="".concat(s," ").concat(l);o[s]=l+1;var p=i(g),c={css:d[1],media:d[2],sourceMap:d[3],supports:d[4],layer:d[5]};if(-1!==p)t[p].references++,t[p].updater(c);else{var u=function(e,t){var i=t.domAPI(t);return i.update(e),function(t){t?(t.css!==e.css||t.media!==e.media||t.sourceMap!==e.sourceMap||t.supports!==e.supports||t.layer!==e.layer)&&i.update(e=t):i.remove()}}(c,r);r.byIndex=n,t.splice(n,0,{identifier:g,updater:u,references:1})}a.push(g)}return a}e.exports=function(e,o){var a=r(e=e||[],o=o||{});return function(e){e=e||[];for(var n=0;n<a.length;n++){var d=i(a[n]);t[d].references--}for(var s=r(e,o),l=0;l<a.length;l++){var g=i(a[l]);0===t[g].references&&(t[g].updater(),t.splice(g,1))}a=s}}},8128(e){var t={};e.exports=function(e,i){var r=function(e){if(void 0===t[e]){var i=document.querySelector(e);if(window.HTMLIFrameElement&&i instanceof window.HTMLIFrameElement)try{i=i.contentDocument.head}catch(e){i=null}t[e]=i}return t[e]}(e);if(!r)throw Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");r.appendChild(i)}},3051(e){e.exports=function(e){var t=document.createElement("style");return e.setAttributes(t,e.attributes),e.insert(t,e.options),t}},855(e,t,i){e.exports=function(e){var t=i.nc;t&&e.setAttribute("nonce",t)}},1740(e){e.exports=function(e){if("u"<typeof document)return{update:function(){},remove:function(){}};var t=e.insertStyleElement(e);return{update:function(i){var r,o,a;r="",i.supports&&(r+="@supports (".concat(i.supports,") {")),i.media&&(r+="@media ".concat(i.media," {")),(o=void 0!==i.layer)&&(r+="@layer".concat(i.layer.length>0?" ".concat(i.layer):""," {")),r+=i.css,o&&(r+="}"),i.media&&(r+="}"),i.supports&&(r+="}"),(a=i.sourceMap)&&"u">typeof btoa&&(r+="\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(a))))," */")),e.styleTagTransform(r,t,e.options)},remove:function(){var e;null===(e=t).parentNode||e.parentNode.removeChild(e)}}}},3656(e){e.exports=function(e,t){if(t.styleSheet)t.styleSheet.cssText=e;else{for(;t.firstChild;)t.removeChild(t.firstChild);t.appendChild(document.createTextNode(e))}}},4651(e,t,i){i.r(t),i.d(t,{KernelWidgetManager:()=>f,LabWidgetManager:()=>T,WidgetManager:()=>x,WidgetRenderer:()=>h,default:()=>es,output:()=>o,registerWidgetManager:()=>ei});var r,o={};i.r(o),i.d(o,{OUTPUT_WIDGET_VERSION:()=>U,OutputModel:()=>k,OutputView:()=>I});var a=i(7284),n=i(6630),d=i(3352),s=i(9473),l=i(9303),g=i(582),p=i(1086),c=i(4525),u=i(7989),w=i(1660);class h extends w.Panel{constructor(e,t){super(),this._manager=new u.PromiseDelegate,this._rerenderMimeModel=null,this.mimeType=e.mimeType,t&&(this.manager=t)}set manager(e){e.restored.connect(this._rerender,this),this._manager.resolve(e)}async renderModel(e){let t,i,r=e.data[this.mimeType];this.node.textContent="Loading widget...";let o=await this._manager.promise;if(""===r.model_id)return this.hide(),Promise.resolve();try{t=await o.get_model(r.model_id)}catch(t){if(o.restoredStatus){this.node.textContent="Error displaying widget: model not found",this.addClass("jupyter-widgets"),console.error(t);return}this._rerenderMimeModel=e;return}this._rerenderMimeModel=null;try{let e=await o.create_view(t);i=e.luminoWidget||e.pWidget}catch(e){this.node.textContent="Error displaying widget",this.addClass("jupyter-widgets"),console.error(e);return}this.node.textContent="",this.addWidget(i),i.disposed.connect(()=>{this.hide(),r.model_id=""})}dispose(){this.isDisposed||(this._manager=null,super.dispose())}_rerender(){this._rerenderMimeModel&&(this.node.textContent="",this.removeClass("jupyter-widgets"),this.renderModel(this._rerenderMimeModel))}}var E=i(1969),b=i(3877),j=i(6401),y=i(9712);class m{constructor(){this._cache=Object.create(null)}set(e,t,i){if(e in this._cache||(this._cache[e]=Object.create(null)),t in this._cache[e])throw`Version ${t} of key ${e} already registered.`;this._cache[e][t]=i}get(e,t){if(e in this._cache){let i=this._cache[e],r=(0,y.maxSatisfying)(Object.keys(i),t);if(null!==r)return i[r]}}getAllVersions(e){if(e in this._cache)return this._cache[e]}}let D="application/vnd.jupyter.widget-view+json",v="application/vnd.jupyter.widget-state+json";class T extends b.ManagerBase{constructor(e){super(),this._handleCommOpen=async(e,t)=>{let i=new E.shims.services.Comm(e);await this.handle_comm_open(i,t)},this._restored=new j.Signal(this),this._restoredStatus=!1,this._kernelRestoreInProgress=!1,this._isDisposed=!1,this._registry=new m,this._modelsSync=new Map,this._onUnhandledIOPubMessage=new j.Signal(this),this._rendermime=e}callbacks(e){return{iopub:{output:e=>{this._onUnhandledIOPubMessage.emit(e)}}}}_handleKernelChanged({oldValue:e,newValue:t}){e&&e.removeCommTarget(this.comm_target_name,this._handleCommOpen),t&&t.registerCommTarget(this.comm_target_name,this._handleCommOpen)}disconnect(){super.disconnect(),this._restoredStatus=!1}async _loadFromKernel(){var e;if(!this.kernel)throw Error("Kernel not set");if((null==(e=this.kernel)?void 0:e.handleComms)!==!1)return super._loadFromKernel()}async _create_comm(e,t,i,r,o){let a=this.kernel;if(!a)throw Error("No current kernel");let n=a.createComm(e,t);return(i||r)&&n.open(i,r,o),new E.shims.services.Comm(n)}async _get_comm_info(){let e=this.kernel;if(!e)throw Error("No current kernel");let t=await e.requestCommInfo({target_name:this.comm_target_name});return"ok"===t.content.status?t.content.comms:{}}get isDisposed(){return this._isDisposed}dispose(){!this.isDisposed&&(this._isDisposed=!0,this._commRegistration&&this._commRegistration.dispose())}async resolveUrl(e){return e}async loadClass(e,t,i){("@jupyter-widgets/base"===t||"@jupyter-widgets/controls"===t)&&(0,y.valid)(i)&&(i=`^${i}`);let r=this._registry.getAllVersions(t);if(!r)throw Error(`No version of module ${t} is registered`);let o=this._registry.get(t,i);if(!o){let e=Object.keys(r);throw Error(`Module ${t}, version ${i} is not registered, however, \
        ${e.join(",")} ${e.length>1?"are":"is"}`)}let a=("function"==typeof o?await o():await o)[e];if(!a)throw Error(`Class ${e} not found in module ${t}`);return a}get rendermime(){return this._rendermime}get restored(){return this._restored}get restoredStatus(){return this._restoredStatus}get onUnhandledIOPubMessage(){return this._onUnhandledIOPubMessage}register(e){this._registry.set(e.name,e.version,e.exports)}register_model(e,t){super.register_model(e,t),t.then(t=>{this._modelsSync.set(e,t),t.once("comm:close",()=>{this._modelsSync.delete(e)})})}async clear_state(){await super.clear_state(),this._modelsSync=new Map}get_state_sync(e={}){let t=[];for(let e of this._modelsSync.values())e.comm_live&&t.push(e);return(0,b.serialize_state)(t,e)}}class f extends T{constructor(e,t){super(t),this._kernel=e,e.statusChanged.connect((e,t)=>{this._handleKernelStatusChange(t)}),e.connectionStatusChanged.connect((e,t)=>{this._handleKernelConnectionStatusChange(t)}),this._handleKernelChanged({name:"kernel",oldValue:null,newValue:e}),this.restoreWidgets()}_handleKernelConnectionStatusChange(e){"connected"!==e||this._kernelRestoreInProgress||this.restoreWidgets()}_handleKernelStatusChange(e){"restarting"===e&&this.disconnect()}async restoreWidgets(){try{this._kernelRestoreInProgress=!0,await this._loadFromKernel(),this._restoredStatus=!0,this._restored.emit()}catch(e){}this._kernelRestoreInProgress=!1}dispose(){this.isDisposed||(this._kernel=null,super.dispose())}get kernel(){return this._kernel}}class x extends T{constructor(e,t,i){var r,o;super(t),this._context=e,e.sessionContext.kernelChanged.connect((e,t)=>{this._handleKernelChanged(t)}),e.sessionContext.statusChanged.connect((e,t)=>{this._handleKernelStatusChange(t)}),e.sessionContext.connectionStatusChanged.connect((e,t)=>{this._handleKernelConnectionStatusChange(t)}),(null==(r=e.sessionContext.session)?void 0:r.kernel)&&this._handleKernelChanged({name:"kernel",oldValue:null,newValue:null==(o=e.sessionContext.session)?void 0:o.kernel}),this.restoreWidgets(this._context.model),this._settings=i,e.saveState.connect((e,t)=>{"started"===t&&i.saveState&&this._saveState()})}_saveState(){let e=this.get_state_sync({drop_defaults:!0});this._context.model.setMetadata?this._context.model.setMetadata("widgets",{"application/vnd.jupyter.widget-state+json":e}):this._context.model.metadata.set("widgets",{"application/vnd.jupyter.widget-state+json":e})}_handleKernelConnectionStatusChange(e){"connected"!==e||this._kernelRestoreInProgress||this.restoreWidgets(this._context.model,{loadKernel:!0,loadNotebook:!1})}_handleKernelStatusChange(e){"restarting"===e&&this.disconnect()}async restoreWidgets(e,{loadKernel:t,loadNotebook:i}={loadKernel:!0,loadNotebook:!0}){try{if(await this.context.sessionContext.ready,t)try{this._kernelRestoreInProgress=!0,await this._loadFromKernel()}finally{this._kernelRestoreInProgress=!1}i&&await this._loadFromNotebook(e),this._restoredStatus=!0,this._restored.emit()}catch(e){}}async _loadFromNotebook(e){let t=e.getMetadata?e.getMetadata("widgets"):e.metadata.get("widgets");if(t&&t[v]){let e=t[v];e=this.filterExistingModelState(e),await this.set_state(e)}}dispose(){this.isDisposed||(this._context=null,super.dispose())}async resolveUrl(e){let t=await this.context.urlResolver.resolveUrl(e);return this.context.urlResolver.getDownloadUrl(t)}get context(){return this._context}get kernel(){var e,t,i;return null!=(i=null==(t=null==(e=this._context.sessionContext)?void 0:e.session)?void 0:t.kernel)?i:null}register_model(e,t){super.register_model(e,t),this.setDirty()}async clear_state(){await super.clear_state(),this.setDirty()}setDirty(){this._settings.saveState&&(this._context.model.dirty=!0)}}var C=i(3333),R=i(8381),A=i(4099),P=i.n(A);let U=C.OUTPUT_WIDGET_VERSION;class k extends C.OutputModel{defaults(){return Object.assign(Object.assign({},super.defaults()),{msg_id:"",outputs:[]})}initialize(e,t){super.initialize(e,t),this._outputs=new R.OutputAreaModel({trusted:!0}),this._msgHook=e=>(this.add(e),!1),this.widget_manager instanceof x&&this.widget_manager.context.sessionContext.kernelChanged.connect((e,t)=>{this._handleKernelChanged(t)}),this.listenTo(this,"change:msg_id",this.reset_msg_id),this.listenTo(this,"change:outputs",this.setOutputs),this.setOutputs()}_handleKernelChanged({oldValue:e}){let t=this.get("msg_id");t&&e&&(e.removeMessageHook(t,this._msgHook),this.set("msg_id",null))}reset_msg_id(){let e=this.widget_manager.kernel,t=this.get("msg_id"),i=this.previous("msg_id");i&&e&&e.removeMessageHook(i,this._msgHook),t&&e&&e.registerMessageHook(t,this._msgHook)}add(e){let t=e.header.msg_type;switch(t){case"execute_result":case"display_data":case"stream":case"error":{let i=e.content;i.output_type=t,this._outputs.add(i);break}case"clear_output":this.clear_output(e.content.wait)}this.set("outputs",this._outputs.toJSON(),{newMessage:!0}),this.save_changes()}clear_output(e=!1){this._outputs.clear(e)}get outputs(){return this._outputs}setOutputs(e,t,i){i&&i.newMessage||(this.clear_output(),this._outputs.fromJSON(JSON.parse(JSON.stringify(this.get("outputs")))))}}class I extends C.OutputView{_createElement(e){return this.luminoWidget=new E.JupyterLuminoPanelWidget({view:this}),this.luminoWidget.node}_setElement(e){if(this.el||e!==this.luminoWidget.node)throw Error("Cannot reset the DOM element.");this.el=this.luminoWidget.node,this.$el=P()(this.luminoWidget.node)}render(){super.render(),this._outputView=new R.OutputArea({rendermime:this.model.widget_manager.rendermime,contentFactory:R.OutputArea.defaultContentFactory,model:this.model.outputs}),this.luminoWidget.insertWidget(0,this._outputView),this.luminoWidget.addClass("jupyter-widgets"),this.luminoWidget.addClass("widget-output"),this.update()}remove(){return this._outputView.dispose(),super.remove()}}var S=i(2591),B=i.n(S),O=i(1740),_=i.n(O),z=i(8128),N=i.n(z),M=i(855),L=i.n(M),W=i(3051),H=i.n(W),F=i(3656),V=i.n(F),G=i(4400),Y={};Y.styleTagTransform=V(),Y.setAttributes=L(),Y.insert=N().bind(null,"head"),Y.domAPI=_(),Y.insertStyleElement=H(),B()(G.A,Y),G.A&&G.A.locals&&G.A.locals;var K=i(5946),J={};J.styleTagTransform=V(),J.setAttributes=L(),J.insert=N().bind(null,"head"),J.domAPI=_(),J.insertStyleElement=H(),B()(K.A,J),K.A&&K.A.locals&&K.A.locals;var Z=i(5374),$=i(9180);let X=new class{constructor(){this._widgetRegistered=new j.Signal(this),this._registry=[]}get widgets(){return[...this._registry]}push(e){this._registry.push(e),this._widgetRegistered.emit(e)}get widgetRegistered(){return this._widgetRegistered}},q={saveState:!1};function*Q(...e){for(let t of e)yield*t}async function ee(e){return await e.ready,e.session.kernel.id}async function et(e,t,i,o,a){let n,d=await ee(t),s=r.widgetManagerProperty.get(d);for(let i of(s||(s=a(),X.widgets.forEach(e=>s.register(e)),X.widgetRegistered.connect((e,t)=>{s.register(t)}),r.widgetManagerProperty.set(d,s),n=d,e.disposed.connect(e=>{r.widgetManagerProperty.get(n)&&r.widgetManagerProperty.delete(n)}),t.kernelChanged.connect((e,t)=>{let{newValue:i}=t;if(i){let e=i.id,t=r.widgetManagerProperty.get(n);t&&(r.widgetManagerProperty.delete(n),r.widgetManagerProperty.set(e,t)),n=e}})),o))i.manager=s;return i.removeMimeType(D),i.addFactory({safe:!1,mimeTypes:[D],createRenderer:e=>new h(e,s)},-10),new c.DisposableDelegate(()=>{i&&i.removeMimeType(D),s.dispose()})}function ei(e,t,i){let o,a=ee(e.sessionContext).then(a=>{let n=r.widgetManagerProperty.get(a);for(let d of(n?o=n:(o=new x(e,t,q),X.widgets.forEach(e=>o.register(e)),X.widgetRegistered.connect((e,t)=>{o.register(t)}),r.widgetManagerProperty.set(a,o)),i))d.manager=o;t.removeMimeType(D),t.addFactory({safe:!1,mimeTypes:[D],createRenderer:e=>new h(e,o)},-10)});return new c.DisposableDelegate(async()=>{await a,t&&t.removeMimeType(D),o.dispose()})}async function er(e,t){let i=e.content,r=e.context,o=r.sessionContext,a=i.rendermime;return et(i,o,a,t,()=>new x(r,a,q))}async function eo(e,t){let i=e.console,r=i.sessionContext,o=i.rendermime;return et(i,r,o,t,()=>new f(r.session.kernel,o))}let ea={id:"@jupyter-widgets/jupyterlab-manager:plugin",requires:[l.IRenderMimeRegistry],optional:[d.INotebookTracker,n.IConsoleTracker,a.ISettingRegistry,s.IMainMenu,g.ILoggerRegistry,$.ITranslator],provides:E.IJupyterWidgetRegistry,activate:function(e,t,i,o,a,n,d,s){let{commands:l}=e,g=(null!=s?s:$.nullTranslator).load("jupyterlab_widgets"),c=async e=>{if(!d)return;let t=await ee(e.context.sessionContext),i=r.widgetManagerProperty.get(t);i&&i.onUnhandledIOPubMessage.connect((t,i)=>{let r=d.getLogger(e.context.path),o="warning";(Z.KernelMessage.isErrorMsg(i)||Z.KernelMessage.isStreamMsg(i)&&"stderr"===i.content.name)&&(o="error");let a=Object.assign(Object.assign({},i.content),{output_type:i.header.msg_type});r.rendermime=e.content.rendermime,r.log({type:"output",data:a,level:o})})};if(null!==a&&a.load(ea.id).then(e=>{e.changed.connect(en),en(e)}).catch(e=>{console.error(e.message)}),t.addFactory({safe:!1,mimeTypes:[D],createRenderer:e=>new h(e)},-10),null!==i){let t=t=>Q(function*(e){for(let t of e.widgets)if("code"===t.model.type)for(let e of t.outputArea.widgets)for(let t of Array.from(e.children()))t instanceof h&&(yield t)}(t.content),function*(e,t){for(let i of Array.from((0,p.filter)(e.shell.widgets(),e=>e.id.startsWith("LinkedOutputView-")&&e.path===t)))for(let e of Array.from(i.children()))for(let t of Array.from(e.children()))t instanceof h&&(yield t)}(e,t.context.path));i.forEach(async e=>{await er(e,t(e)),c(e)}),i.widgetAdded.connect(async(e,i)=>{await er(i,t(i)),c(i)})}if(null!==o){let e=e=>Q(function*(e){for(let t of Array.from(e.cells))if("code"===t.model.type)for(let e of t.outputArea.widgets)for(let t of Array.from(e.children()))t instanceof h&&(yield t)}(e.console));o.forEach(async t=>{await eo(t,e(t))}),o.widgetAdded.connect(async(t,i)=>{await eo(i,e(i))})}return null!==a&&l.addCommand("@jupyter-widgets/jupyterlab-manager:saveWidgetState",{label:g.__("Save Widget State Automatically"),execute:e=>a.set(ea.id,"saveState",!q.saveState).catch(e=>{console.error(`Failed to set ${ea.id}: ${e.message}`)}),isToggled:()=>q.saveState}),n&&n.settingsMenu.addGroup([{command:"@jupyter-widgets/jupyterlab-manager:saveWidgetState"}]),{registerWidget(e){X.push(e)}}},autoStart:!0};function en(e){q.saveState=e.get("saveState").composite}let ed=[ea,{id:`@jupyter-widgets/jupyterlab-manager:base-${E.JUPYTER_WIDGETS_VERSION}`,requires:[E.IJupyterWidgetRegistry],autoStart:!0,activate:(e,t)=>{t.registerWidget({name:"@jupyter-widgets/base",version:E.JUPYTER_WIDGETS_VERSION,exports:{WidgetModel:E.WidgetModel,WidgetView:E.WidgetView,DOMWidgetView:E.DOMWidgetView,DOMWidgetModel:E.DOMWidgetModel,LayoutModel:E.LayoutModel,LayoutView:E.LayoutView,StyleModel:E.StyleModel,StyleView:E.StyleView,ErrorWidgetView:E.ErrorWidgetView}})}},{id:"@jupyter-widgets/jupyterlab-manager:controls-2.0.0",requires:[E.IJupyterWidgetRegistry],autoStart:!0,activate:(e,t)=>{t.registerWidget({name:"@jupyter-widgets/controls",version:"2.0.0",exports:()=>new Promise((e,t)=>{i.e(902).then((t=>{e(i(9459))}).bind(null,i)).catch(e=>{t(e)})})})}},{id:`@jupyter-widgets/jupyterlab-manager:output-${U}`,requires:[E.IJupyterWidgetRegistry],autoStart:!0,activate:(e,t)=>{t.registerWidget({name:"@jupyter-widgets/output",version:U,exports:{OutputModel:k,OutputView:I}})}}];(r||(r={})).widgetManagerProperty=new Map;let es=ed},2426(e){e.exports="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjIuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCAxOCAxOCIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTggMTg7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KCS5zdDB7ZmlsbDpub25lO30KPC9zdHlsZT4KPHBhdGggZD0iTTUuMiw1LjlMOSw5LjdsMy44LTMuOGwxLjIsMS4ybC00LjksNWwtNC45LTVMNS4yLDUuOXoiLz4KPHBhdGggY2xhc3M9InN0MCIgZD0iTTAtMC42aDE4djE4SDBWLTAuNnoiLz4KPC9zdmc+Cg"}}]);
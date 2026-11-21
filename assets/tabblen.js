// Tabblen, the Great Tables mascot, as a <gt-tabblen> element that can be animated and directed.
//
// He's a table: a header with his face in it, a body of 4 by 3 cells, two arms and two feet. He
// breathes, blinks and glances about on his own (all of which stops with reduced motion and out
// of view), shows his name when the pointer's over him, and does what he's told:
//
//   <script src="assets/tabblen.js" defer></script>
//   <gt-tabblen mood="happy" arms="open" follow say="Hello!"></gt-tabblen>
//
// Attributes:
//   mood     happy (the default), grin, neutral, sad, surprised, wink, sleepy, zen, love, thinking
//   arms     rest (the default), open, up, point, or a pose for each arm ("up rest")
//   look     center (the default), left, right, up, down, or "x y" (each from -1 to 1)
//   cells    the cells' contents: rows split by "/" and cells by "|" ("a|b|c|d/e|f"), a JSON
//            array of rows, or (for one character to a cell) a plain string
//   say      text for a speech bubble that stays up
//   bubble   where speech bubbles go: top (the default), left or right; there's room kept for
//            them at the top with bubble="top", say or float
//   follow   his eyes follow the pointer
//   still    no breathing, blinking or glancing about on his own
//   float    left or right, to float him beside a page's text
//   intro    steps for play(), as JSON, to do when he's first seen ('[["wave", 2], ["say", "Hi!"]]')
//   cell-trick  what a double click on a cell does: ripple (the default), shuffle, flip, slots,
//            heatmap or zen (see cellTrick())
//
// A click (or tap) on him does a trick. A double click does something for the part that's
// clicked: his feet click their heels in a hop, his eyes bug out, his mouth giggles, his forehead
// gets him dizzy, an arm gets him cheering, and a cell does the cell trick. Before that, a
// `gt-tabblen-double` event (with the part in its detail: {part, row, col, side}) goes out, which
// can be canceled to do something else instead.
//
// Methods (the ones that take time return promises, so they can be awaited in turn):
//   mood(name)                    set his mood (his eyes and mouth)
//   eyes(left, right?)            open, wide, happy, closed or heart
//   mouth(shape)                  smile, grin, flat, frown, o, smirk, small, soft, wavy or talk
//   look(x, y)                    look in a direction (-1 to 1 each way); look() looks ahead
//   lookAt(target)                look at an element or a {x, y} point on the page
//   blink()
//   arms(left, right?)            pose the arms; arms("up") poses both
//   wave(times = 2, side = "right")
//   tap(times = 2, side = "left") tap a foot
//   walk(steps = 4)               step from foot to foot
//   hop(times = 1)
//   cell(row, col, content)       content is text (or a number), or {text, fill, color, bold}
//   cells(contents)               fill the cells, as for the `cells` attribute (or a flat list)
//   clear()                       empty the cells
//   write(contents, ms = 90)      fill the cells one at a time, in reading order, from a string (a
//                                 character to a cell) or a list
//   heatmap(values, palette?)     color the cells by 12 values (or 3 rows of 4)
//   progress(fraction)            fill the cells, in reading order, up to a fraction of them
//   say(text, ms?)                speak, in a bubble, for a while (or for good with ms = 0)
//   hush()                        take the bubble down
//   play(steps)                   do steps in turn: [["mood", "grin"], ["wave", 3], ["wait", 500]]
//   seen()                        wait for him to be in view (most of him, for the first time)
//   trick()                       do something fun (as on a click)
//   heelClick()                   hop up and to the side, clicking his heels
//   bugOut()                      his eyes bug out
//   giggle()
//   dizzy()                       his eyes roll and he wobbles
//   cheer()                       wave his arms up in turn
//   cellTrick(row, col, name?)    do a cell trick from a cell (the `cell-trick` one, by default):
//                                 ripple   colors spread out from the cell
//                                 shuffle  the cells' text gets mixed up, then sorted out again
//                                 flip     the text flips over, from the cell out, changing case
//                                 slots    the text spins like a slot machine's, then stops
//                                 heatmap  a heatmap that's hottest at the cell, for a moment
//                                 zen      a calm glow goes around the cells, from the cell
(() => {
  "use strict";

  if (!window.customElements || customElements.get("gt-tabblen")) return;

  const SVG = "http://www.w3.org/2000/svg";
  const motion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const still = () => motion.matches;

  const sleep = (ms) => new Promise((done) => setTimeout(done, ms));
  const rand = (lo, hi) => lo + Math.random() * (hi - lo);
  const pick = (items) => items[(Math.random() * items.length) | 0];
  const clamp = (x, lo, hi) => Math.min(hi, Math.max(lo, x));
  const ease = (k) => (k < 0.5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2);

  // His geometry, in the units of the drawing: the body's 320 wide, with its header 62 high and
  // three rows of cells under it (to y = 159), and the feet 40 high below that
  const W = 320;
  const HEAD = 62;
  const BOTTOM = 159;
  const ROW = (BOTTOM - HEAD) / 3;
  const COL = W / 4;
  const FEET = 199.5;
  const EYES = [
    [105.8, 26.5],
    [214.2, 26.5],
  ];
  const PUPIL_TRAVEL = 3.4;

  // The mouth is two curves, the upper lip from the left corner to the right and the lower one
  // back: [left corner, upper controls, right corner, lower controls] (12 numbers, so that any
  // mouth can turn into any other). A mouth that's a line has its lips together.
  const lips = (l, c1, c2, r) => [...l, ...c1, ...c2, ...r, ...c2, ...c1];
  const MOUTHS = {
    smile: lips([127.7, 42.4], [148, 54.4], [173, 54.4], [193.8, 42.4]),
    grin: [125, 41, 148, 43, 172, 43, 195, 41, 178, 64, 142, 64],
    flat: lips([136, 47], [150, 47], [170, 47], [184, 47]),
    frown: lips([134, 52], [150, 42], [170, 42], [186, 52]),
    o: [150, 47.5, 150, 34, 170, 34, 170, 47.5, 170, 61, 150, 61],
    smirk: lips([132, 45], [152, 53], [176, 52], [191, 40]),
    small: lips([150, 47], [155, 50], [165, 50], [170, 47]),
    soft: lips([140, 44], [152, 51], [168, 51], [180, 44]),
    wavy: lips([140, 48], [150, 43], [166, 53], [178, 46]),
    talk: [147, 45, 150, 40.5, 170, 40.5, 173, 45, 171, 54, 149, 54],
  };

  const MOODS = {
    happy: { eyes: ["open", "open"], mouth: "smile" },
    grin: { eyes: ["happy", "happy"], mouth: "grin" },
    neutral: { eyes: ["open", "open"], mouth: "flat" },
    sad: { eyes: ["open", "open"], mouth: "frown", look: [0, 0.6] },
    surprised: { eyes: ["wide", "wide"], mouth: "o" },
    wink: { eyes: ["open", "happy"], mouth: "smirk" },
    sleepy: { eyes: ["closed", "closed"], mouth: "small" },
    zen: { eyes: ["closed", "closed"], mouth: "soft" },
    love: { eyes: ["heart", "heart"], mouth: "smile" },
    thinking: { eyes: ["open", "open"], mouth: "wavy", look: [-0.6, -0.7] },
  };

  // An arm (the left one; the right one's its mirror image) is one curve, from the shoulder out:
  // [shoulder, controls, hand]
  const ARMS = {
    rest: [-4.6, 90.3, -16.6, 101, -16.6, 121.7, -4.6, 132.4],
    open: [-3.9, 91.5, -18, 101, -36, 96, -43.5, 80.8],
    up: [-4.6, 84, -18, 80, -30, 60, -40, 28],
    point: [-4.6, 86, -16, 86, -30, 85, -45, 83],
  };
  const WAVE = [-4.6, 84, -16, 78, -22, 54, -20, 22];

  const LOOKS = { center: [0, 0], left: [-1, 0], right: [1, 0], up: [0, -1], down: [0, 1] };

  // The cells around the edge of his body, clockwise from the top left (for the zen cell trick)
  const RING = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 3], [2, 3], [2, 2], [2, 1], [2, 0], [1, 0]];
  const CELL_TRICKS = ["ripple", "shuffle", "flip", "slots", "heatmap", "zen"];

  // A second click within this long (and this near, in pixels) makes a double click
  const DOUBLE_MS = 320;
  const DOUBLE_NEAR = 30;

  const shuffled = (items) => {
    const out = items.slice();
    for (let i = out.length - 1; i > 0; i--) {
      const j = (Math.random() * (i + 1)) | 0;
      [out[i], out[j]] = [out[j], out[i]];
    }
    return out;
  };

  const mirror = (arm) => arm.map((v, i) => (i % 2 === 0 ? W - v : v));
  const mouthPath = (m) =>
    `M${m[0]} ${m[1]}C${m[2]} ${m[3]} ${m[4]} ${m[5]} ${m[6]} ${m[7]}` +
    `C${m[8]} ${m[9]} ${m[10]} ${m[11]} ${m[0]} ${m[1]}Z`;
  const armPath = (a) => `M${a[0]} ${a[1]}C${a[2]} ${a[3]} ${a[4]} ${a[5]} ${a[6]} ${a[7]}`;

  const STYLE = `
    :host {
      --tabblen-ink: #707070;
      --tabblen-accent: #f900c3;
      --tabblen-cell: var(--tabblen-ink);
      --tabblen-bubble: #fff;
      --tabblen-bubble-text: #2b2b33;
      display: inline-block;
      position: relative;
      width: 200px;
      max-width: 100%;
      vertical-align: middle;
      line-height: 1.3;
      -webkit-tap-highlight-color: transparent;
      /* (A double click on him isn't to select him, or the page's text by him) */
      -webkit-user-select: none;
      user-select: none;
    }
    :host([theme="dark"]) {
      --tabblen-ink: #a9a9b4;
      --tabblen-bubble: #25272d;
      --tabblen-bubble-text: #ececf1;
    }
    :host([bubble="top"]), :host(:not([bubble])[say]), :host(:not([bubble])[float]) { padding-top: 3.4em; }
    :host([float="right"]) { float: right; width: 190px; margin: 0.2rem 0 1rem 1.4rem; }
    :host([float="left"]) { float: left; width: 190px; margin: 0.2rem 1.4rem 1rem 0; }
    /* (On narrower screens, where the docs' pages lay their content out in a column, which floats
       don't apply in, he stands in the middle, between the paragraphs; the margin on his side
       would put him off center) */
    @media (max-width: 991.98px) {
      :host([float]) { display: block; float: none; align-self: center; margin: 0.2rem auto 1rem; }
    }
    @media (max-width: 575.98px) {
      :host([float]) { width: 160px; }
    }
    svg {
      display: block;
      width: 100%;
      height: auto;
      overflow: visible;
      cursor: pointer;
      /* (No zooming in on a double tap) */
      touch-action: manipulation;
    }
    .spark { stroke: var(--tabblen-accent); stroke-width: 2.6; stroke-linecap: round; opacity: 0; transform-box: fill-box; transform-origin: center; }
    .ink { fill: none; stroke: var(--tabblen-ink); stroke-width: 2.6; }
    .grid { stroke-width: 1.6; }
    .arm { stroke-linecap: butt; }
    .mouth { fill: var(--tabblen-ink); stroke-linecap: round; stroke-linejoin: round; stroke-width: 2.4; }
    .mouth.hollow { fill: none; }
    .look { transition: transform 0.18s ease; }
    :host([follow]) .look { transition-duration: 0.08s; }
    .pupil { fill: var(--tabblen-ink); transform-box: fill-box; transform-origin: center; transition: transform 0.12s ease; }
    .eye > * { opacity: 0; transition: opacity 0.12s ease, transform 0.12s ease; transform-box: fill-box; transform-origin: center; }
    .eye[data-state="open"] .open, .eye[data-state="wide"] .open,
    .eye[data-state="happy"] .happy, .eye[data-state="closed"] .closed,
    .eye[data-state="heart"] .heart { opacity: 1; }
    .eye:not([data-state="open"]):not([data-state="wide"]) .open { transform: scaleY(0.1); }
    .eye[data-state="wide"] .open { transform: scale(1.1); }
    .eye[data-state="wide"] .pupil { transform: scale(0.72); }
    .eye.blink .open { transform: scaleY(0.08); transition-duration: 0.06s; }
    .lid { stroke-width: 2.4; stroke-linecap: round; }
    .heart { fill: var(--tabblen-accent); stroke: none; }
    .ring { stroke-width: 2.1; }
    .cell-fill { transition: fill 0.35s ease; }
    .cell-text { fill: var(--tabblen-cell); font-size: 24px; font-weight: 600; text-anchor: middle; dominant-baseline: central; transform-box: fill-box; transform-origin: center; }
    .bubble {
      position: absolute;
      z-index: 2;
      max-width: 16em;
      width: max-content;
      padding: 0.35em 0.75em;
      border: 1.5px solid var(--tabblen-ink);
      border-radius: 0.9em;
      background: var(--tabblen-bubble);
      color: var(--tabblen-bubble-text);
      font-size: 0.9rem;
      font-weight: 600;
      text-align: center;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s ease, transform 0.2s ease;
    }
    .bubble::after {
      content: "";
      position: absolute;
      width: 0.6em;
      height: 0.6em;
      background: var(--tabblen-bubble);
      border: 1.5px solid var(--tabblen-ink);
      border-top: none;
      border-left: none;
    }
    .bubble.on { opacity: 1; }
    :host([float]) .bubble { max-width: 11em; }
    :host(:not([bubble])) .bubble, :host([bubble="top"]) .bubble {
      bottom: calc(100% + 0.3em);
      left: 50%;
      transform: translate(-50%, 0.3em);
    }
    /* (Where there's room kept for it, in his padding) */
    :host([bubble="top"]) .bubble, :host(:not([bubble])[say]) .bubble,
    :host(:not([bubble])[float]) .bubble { bottom: calc(100% - 3.1em); }
    :host(:not([bubble])) .bubble.on, :host([bubble="top"]) .bubble.on { transform: translate(-50%, 0); }
    :host(:not([bubble])) .bubble::after, :host([bubble="top"]) .bubble::after {
      bottom: -0.38em;
      left: calc(50% - 0.3em);
      transform: rotate(45deg);
    }
    :host([bubble="left"]) .bubble { right: 92%; top: 4%; transform: translateX(0.3em); }
    :host([bubble="right"]) .bubble { left: 92%; top: 4%; transform: translateX(-0.3em); }
    :host([bubble="left"]) .bubble.on, :host([bubble="right"]) .bubble.on { transform: none; }
    :host([bubble="left"]) .bubble::after { right: -0.38em; top: 0.75em; transform: rotate(-45deg); }
    :host([bubble="right"]) .bubble::after { left: -0.38em; top: 0.75em; transform: rotate(135deg); }
    /* His name, which comes out from under his right foot (where it's tucked away, above the
       bottom of the box it's in) when the pointer's over him */
    .name {
      position: absolute;
      z-index: 1;
      top: calc(100% - 2px);
      left: 64%;
      padding: 0 0.3em 0.4em 0;
      overflow: hidden;
      pointer-events: none;
    }
    .name span {
      display: block;
      padding: 0.12em 0.5em;
      border-radius: 0.4em;
      background: var(--tabblen-accent);
      color: #fff;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.03em;
      line-height: 1.3;
      white-space: nowrap;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
      transform: translate(-0.8em, -110%);
      transition: transform 0.18s ease-in;
    }
    svg:hover ~ .name span {
      transform: none;
      transition: transform 0.32s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    @media (prefers-reduced-motion: reduce) {
      .pupil, .eye > *, .cell-fill, .bubble, .name span, svg:hover ~ .name span { transition: none; }
    }
  `;

  function el(name, attrs = {}, parent = null) {
    const node = document.createElementNS(SVG, name);
    for (const [key, value] of Object.entries(attrs)) node.setAttribute(key, value);
    if (parent) parent.appendChild(node);
    return node;
  }

  // The cells' contents, from the `cells` attribute or cells(): rows of cells
  function parseCells(value) {
    if (value == null || value === "") return [];
    if (Array.isArray(value)) {
      if (value.every((row) => !Array.isArray(row))) {
        const rows = [];
        for (let i = 0; i < value.length; i += 4) rows.push(value.slice(i, i + 4));
        return rows;
      }
      return value;
    }
    const text = String(value).trim();
    if (text.startsWith("[")) {
      try {
        return parseCells(JSON.parse(text));
      } catch (_) {
        return [];
      }
    }
    if (text.includes("|") || text.includes("/")) return text.split("/").map((row) => row.split("|"));
    return parseCells([...String(value)]);
  }

  // The color at a point in a palette of colors (as #rrggbb)
  function paletteAt(palette, k) {
    const rgb = palette.map((hex) => {
      const n = parseInt(hex.replace("#", ""), 16);
      return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
    });
    const x = clamp(k, 0, 1) * (rgb.length - 1);
    const i = Math.min(rgb.length - 2, Math.floor(x));
    const f = x - i;
    const c = rgb[i].map((v, j) => Math.round(v + (rgb[i + 1][j] - v) * f));
    return `rgb(${c[0]},${c[1]},${c[2]})`;
  }

  class Tabblen extends HTMLElement {
    static get observedAttributes() {
      return ["mood", "arms", "look", "cells", "say", "follow", "still"];
    }

    constructor() {
      super();
      this._tweens = new Map();
      this._mouth = MOUTHS.smile.slice();
      this._mouthName = "smile";
      this._arms = [ARMS.rest.slice(), ARMS.rest.slice()];
      this._pose = ["rest", "rest"];
      this._look = [0, 0];
      this._busy = 0;
      this._visible = true;
      this._timers = [];
      this._build();
    }

    _build() {
      const root = this.attachShadow({ mode: "open" });
      const style = document.createElement("style");
      style.textContent = STYLE;
      root.appendChild(style);

      const svg = el("svg", { viewBox: "-50 -24 420 228", role: "img", "aria-label": "Tabblen, the Great Tables mascot" });
      this._svg = svg;
      const defs = el("defs", {}, svg);
      const clipId = `tabblen-feet-${Math.random().toString(36).slice(2, 8)}`;
      const clip = el("clipPath", { id: clipId }, defs);
      el("rect", { x: -60, y: BOTTOM, width: 440, height: 80 }, clip);

      // All of him (which hops), and all but his feet (which breathes)
      const figure = el("g", { class: "figure" }, svg);
      this._figure = figure;
      figure.style.transformBox = "view-box";
      figure.style.transformOrigin = `160px ${FEET}px`;

      // The feet, under the body (and cut off at it, so that a lifted foot goes behind it)
      const feet = el("g", { "clip-path": `url(#${clipId})` }, figure);
      this._feet = [
        el("path", { class: "ink foot", d: `M1.8 ${BOTTOM}L151.6 ${BOTTOM}C160.9 166.5 160.9 192 151.6 ${FEET}L1.8 ${FEET}C-10.2 192 -10.2 166.5 1.8 ${BOTTOM}Z` }, feet),
        el("path", { class: "ink foot", d: `M168.9 ${BOTTOM}L318.7 ${BOTTOM}C331.4 166.5 331.4 192 318.7 ${FEET}L168.9 ${FEET}C157.8 192 157.8 166.5 168.9 ${BOTTOM}Z` }, feet),
      ];
      const origins = ["151.6px 159px", "168.9px 159px"];
      this._feet.forEach((foot, i) => {
        foot.style.transformBox = "view-box";
        foot.style.transformOrigin = origins[i];
      });

      // The spark where his heels click
      this._spark = el("g", { class: "spark" }, figure);
      for (const degrees of [-35, 15, 60, 120, 165, 215]) {
        const a = (degrees * Math.PI) / 180;
        const [dx, dy] = [Math.cos(a), Math.sin(a)];
        el("line", { x1: 160 + 9 * dx, y1: 186 + 9 * dy, x2: 160 + 19 * dx, y2: 186 + 19 * dy }, this._spark);
      }

      const body = el("g", { class: "body" }, figure);
      this._body = body;
      body.style.transformBox = "view-box";
      body.style.transformOrigin = `160px ${BOTTOM}px`;

      // The cells (their fills, then their text), under the lines
      this._cells = [];
      const cellLayer = el("g", {}, body);
      for (let r = 0; r < 3; r++) {
        const row = [];
        for (let c = 0; c < 4; c++) {
          const x = c * COL;
          const y = HEAD + r * ROW;
          const fill = el("rect", { class: "cell-fill", x, y, width: COL, height: ROW, fill: "transparent" }, cellLayer);
          const text = el("text", { class: "cell-text", x: x + COL / 2, y: y + ROW / 2 + 0.5 }, cellLayer);
          row.push({ fill, text, x, y });
        }
        this._cells.push(row);
      }

      const lines = el("g", { class: "ink" }, body);
      el("rect", { x: 0, y: 0, width: W, height: BOTTOM }, lines);
      el("line", { x1: 0, y1: HEAD, x2: W, y2: HEAD }, lines);
      const grid = el("g", { class: "grid" }, lines);
      for (let c = 1; c < 4; c++) el("line", { x1: c * COL, y1: HEAD, x2: c * COL, y2: BOTTOM }, grid);
      for (let r = 1; r < 3; r++) el("line", { x1: 0, y1: HEAD + r * ROW, x2: W, y2: HEAD + r * ROW }, grid);

      // The arms
      this._armEls = [0, 1].map(() => el("path", { class: "ink arm" }, body));

      // The face: the eyes (each open, happy, closed or a heart) and the mouth
      this._eyes = EYES.map(([cx, cy]) => {
        const eye = el("g", { class: "eye", "data-state": "open", transform: `translate(${cx} ${cy})` }, body);
        const open = el("g", { class: "open" }, eye);
        el("circle", { class: "ink ring", r: 14.9 }, open);
        const pupil = el("g", { class: "look" }, open);
        el("circle", { class: "pupil", r: 9.8 }, pupil);
        el("path", { class: "ink lid happy", d: "M-11 4Q0 -11 11 4" }, eye);
        el("path", { class: "ink lid closed", d: "M-11 -1Q0 10 11 -1" }, eye);
        el("path", { class: "heart", d: "M0 10C-15 0 -12 -12 0 -5C12 -12 15 0 0 10Z" }, eye);
        return { eye, pupil };
      });
      this._mouthEl = el("path", { class: "ink mouth" }, body);

      root.appendChild(svg);
      this._bubble = document.createElement("div");
      this._bubble.className = "bubble";
      this._bubble.setAttribute("aria-live", "polite");
      root.appendChild(this._bubble);
      const name = document.createElement("div");
      name.className = "name";
      name.setAttribute("aria-hidden", "true");
      name.innerHTML = "<span>Tabblen</span>";
      root.appendChild(name);

      this._drawMouth();
      this._drawArms();

      svg.addEventListener("click", (event) => this._onClick(event));
      // (A double click's second press would otherwise select the text by him)
      svg.addEventListener("mousedown", (event) => {
        if (event.detail > 1) event.preventDefault();
      });
    }

    // A click does a trick, unless there's another click soon after, making a double click
    _onClick(event) {
      const { clientX: x, clientY: y } = event;
      const first = this._firstClick;
      clearTimeout(this._clickTimer);
      if (first && event.timeStamp - first.at < DOUBLE_MS && Math.hypot(x - first.x, y - first.y) < DOUBLE_NEAR) {
        this._firstClick = null;
        this._double(first.part);
        return;
      }
      const part = this._partAt(x, y);
      if (!part) {
        this._firstClick = null;
        this.trick();
        return;
      }
      this._firstClick = { at: event.timeStamp, x, y, part };
      this._clickTimer = setTimeout(() => {
        this._firstClick = null;
        this.trick();
      }, DOUBLE_MS);
    }

    // Which of his parts is at a point on the page (or null, for none of them)
    _partAt(x, y) {
      const ctm = this._svg.getScreenCTM();
      if (!ctm) return null;
      const p = new DOMPoint(x, y).matrixTransform(ctm.inverse());
      const inBody = p.x >= 0 && p.x <= W;
      for (let i = 0; i < 2; i++) {
        if (Math.hypot(p.x - EYES[i][0], p.y - EYES[i][1]) < 19) return { part: "eye", side: i === 0 ? "left" : "right" };
      }
      if (inBody && p.y >= 0 && p.y < HEAD) {
        return Math.abs(p.x - 160) < 42 && p.y > 34 ? { part: "mouth" } : { part: "head" };
      }
      if (inBody && p.y >= HEAD && p.y < BOTTOM) {
        const row = Math.min(2, Math.floor((p.y - HEAD) / ROW));
        const col = Math.min(3, Math.floor(p.x / COL));
        return { part: "cell", row, col };
      }
      if (p.y >= BOTTOM && p.y < FEET + 6 && p.x > -14 && p.x < W + 14) return { part: "feet", side: p.x < 160 ? "left" : "right" };
      if (p.y > 10 && p.y < 145 && (p.x < 0 || p.x > W)) return { part: "arm", side: p.x < 0 ? "left" : "right" };
      return null;
    }

    async _double(detail) {
      if (this._busy) return;
      const event = new CustomEvent("gt-tabblen-double", { detail, bubbles: true, composed: true, cancelable: true });
      if (!this.dispatchEvent(event)) return;
      this._busy++;
      try {
        if (detail.part === "feet") await this.heelClick();
        else if (detail.part === "eye") await this.bugOut();
        else if (detail.part === "mouth") await this.giggle();
        else if (detail.part === "head") await this.dizzy();
        else if (detail.part === "arm") await this.cheer();
        else if (detail.part === "cell") await this.cellTrick(detail.row, detail.col);
      } finally {
        this._busy--;
      }
    }

    connectedCallback() {
      this._theme();
      this._themeWatch = new MutationObserver(() => this._theme());
      for (const node of [document.documentElement, document.body]) {
        this._themeWatch.observe(node, { attributes: true, attributeFilter: ["class"] });
      }
      if ("IntersectionObserver" in window) {
        this._seen = new IntersectionObserver((entries) => {
          this._visible = entries[entries.length - 1].isIntersecting;
          this._idle();
        });
        this._seen.observe(this);
      }
      this._onMotion = () => this._idle();
      motion.addEventListener("change", this._onMotion);
      this._onVisibility = () => this._idle();
      document.addEventListener("visibilitychange", this._onVisibility);
      this._idle();
      if (this.hasAttribute("intro") && !this._introduced) {
        this._introduced = true;
        let steps = [];
        try {
          steps = JSON.parse(this.getAttribute("intro"));
        } catch (_) {}
        if (Array.isArray(steps)) this.seen().then(() => this.play(steps));
      }
    }

    disconnectedCallback() {
      this._themeWatch?.disconnect();
      this._seen?.disconnect();
      motion.removeEventListener("change", this._onMotion);
      document.removeEventListener("visibilitychange", this._onVisibility);
      this._follow(false);
      this._stopIdle();
    }

    attributeChangedCallback(name, _old, value) {
      if (name === "mood") this.mood(value || "happy");
      else if (name === "arms") this.arms(...(value || "rest").trim().split(/\s+/));
      else if (name === "look") {
        const named = LOOKS[(value || "center").trim()];
        const xy = named || (value || "").trim().split(/[\s,]+/).map(Number);
        this.look(xy[0] || 0, xy[1] || 0);
      } else if (name === "cells") this.cells(value);
      else if (name === "say") {
        if (value) this.say(value, 0);
        else this.hush();
      } else if (name === "follow") this._follow(value !== null);
      else if (name === "still") this._idle();
    }

    _theme() {
      const dark = document.documentElement.classList.contains("quarto-dark") || document.body.classList.contains("quarto-dark");
      if (dark) this.setAttribute("theme", "dark");
      else this.removeAttribute("theme");
    }

    // Tween a list of numbers from where they are to where they're going, over `ms`
    _tween(key, from, to, ms, draw) {
      const running = this._tweens.get(key);
      if (running) cancelAnimationFrame(running);
      if (still() || ms <= 0) {
        from.splice(0, from.length, ...to);
        draw();
        return Promise.resolve();
      }
      const start = from.slice();
      const t0 = performance.now();
      return new Promise((done) => {
        const step = (now) => {
          const k = ease(Math.min(1, (now - t0) / ms));
          for (let i = 0; i < to.length; i++) from[i] = start[i] + (to[i] - start[i]) * k;
          draw();
          if (k < 1) this._tweens.set(key, requestAnimationFrame(step));
          else {
            this._tweens.delete(key);
            done();
          }
        };
        this._tweens.set(key, requestAnimationFrame(step));
      });
    }

    _drawMouth() {
      this._mouthEl.setAttribute("d", mouthPath(this._mouth));
    }

    _drawArms() {
      this._armEls[0].setAttribute("d", armPath(this._arms[0]));
      this._armEls[1].setAttribute("d", armPath(mirror(this._arms[1])));
    }

    // WAAPI, on one of his parts, or nothing with reduced motion
    _animate(part, frames, options) {
      if (still() || !part.animate) return Promise.resolve();
      return part.animate(frames, { easing: "ease-in-out", ...options }).finished.catch(() => {});
    }

    // --- His face ---

    mood(name) {
      const m = MOODS[name] || MOODS.happy;
      this._moodName = MOODS[name] ? name : "happy";
      this.eyes(...m.eyes);
      this.look(...(m.look || [0, 0]));
      return this.mouth(m.mouth);
    }

    eyes(left, right = left) {
      this._eyes[0].eye.dataset.state = left;
      this._eyes[1].eye.dataset.state = right;
      return this;
    }

    mouth(shape, ms = 260) {
      const to = MOUTHS[shape];
      if (!to) return Promise.resolve();
      this._mouthName = shape;
      this._mouthEl.classList.toggle("hollow", shape === "o");
      return this._tween("mouth", this._mouth, to, ms, () => this._drawMouth());
    }

    look(x = 0, y = 0) {
      const d = Math.hypot(x, y);
      const k = d > 1 ? 1 / d : 1;
      this._look = [x * k, y * k];
      for (const { pupil } of this._eyes) {
        pupil.style.transform = `translate(${x * k * PUPIL_TRAVEL}px, ${y * k * PUPIL_TRAVEL}px)`;
      }
      return this;
    }

    // Look at an element, or a point (in the page's coordinates, as with a pointer event's clientX)
    lookAt(target) {
      if (!target) return this.look(0, 0);
      let x;
      let y;
      if (target instanceof Element) {
        const box = target.getBoundingClientRect();
        x = box.left + box.width / 2;
        y = box.top + box.height / 2;
      } else ({ x, y } = target);
      const ctm = this._svg.getScreenCTM();
      if (!ctm) return this;
      const ex = ctm.a * 160 + ctm.e;
      const ey = ctm.d * EYES[0][1] + ctm.f;
      const dx = x - ex;
      const dy = y - ey;
      const reach = Math.min(1, Math.hypot(dx, dy) / (ctm.a * 260));
      const angle = Math.atan2(dy, dx);
      return this.look(Math.cos(angle) * reach, Math.sin(angle) * reach);
    }

    async blink() {
      const eyes = this._eyes.map((e) => e.eye);
      eyes.forEach((eye) => eye.classList.add("blink"));
      await sleep(110);
      eyes.forEach((eye) => eye.classList.remove("blink"));
    }

    // --- His arms and feet ---

    arms(left = "rest", right = left, ms = 320) {
      this._pose = [left, right];
      const moves = [left, right].map((pose, i) =>
        this._tween(`arm${i}`, this._arms[i], ARMS[pose] || ARMS.rest, ms, () => this._drawArms()),
      );
      return Promise.all(moves);
    }

    async wave(times = 2, side = "right") {
      const i = side === "left" ? 0 : 1;
      const before = this._pose[i];
      this._busy++;
      await this._tween(`arm${i}`, this._arms[i], ARMS.up, 260, () => this._drawArms());
      for (let n = 0; n < times && !still(); n++) {
        await this._tween(`arm${i}`, this._arms[i], WAVE, 190, () => this._drawArms());
        await this._tween(`arm${i}`, this._arms[i], ARMS.up, 190, () => this._drawArms());
      }
      await this._tween(`arm${i}`, this._arms[i], ARMS[before] || ARMS.rest, 300, () => this._drawArms());
      this._busy--;
    }

    async tap(times = 2, side = "left") {
      const i = side === "right" ? 1 : 0;
      const turn = i === 0 ? 6 : -6;
      for (let n = 0; n < times; n++) {
        await this._animate(this._feet[i], [{ transform: "rotate(0deg)" }, { transform: `rotate(${turn}deg)` }, { transform: "rotate(0deg)" }], { duration: 320 });
      }
    }

    async walk(steps = 4) {
      for (let n = 0; n < steps; n++) {
        const i = n % 2;
        const turn = i === 0 ? 7 : -7;
        const lean = i === 0 ? 1.2 : -1.2;
        await Promise.all([
          this._animate(this._feet[i], [{ transform: "rotate(0deg)" }, { transform: `rotate(${turn}deg)` }, { transform: "rotate(0deg)" }], { duration: 380 }),
          this._animate(this._body, [{ transform: "rotate(0deg)" }, { transform: `rotate(${lean}deg)` }, { transform: "rotate(0deg)" }], { duration: 380 }),
        ]);
      }
    }

    async hop(times = 1) {
      for (let n = 0; n < times; n++) {
        await this._animate(
          this._figure,
          [
            { transform: "translateY(0) scale(1, 1)", offset: 0 },
            { transform: "translateY(2px) scale(1.03, 0.96)", offset: 0.15 },
            { transform: "translateY(-16px) scale(0.98, 1.03)", offset: 0.5 },
            { transform: "translateY(1px) scale(1.04, 0.95)", offset: 0.85 },
            { transform: "translateY(0) scale(1, 1)", offset: 1 },
          ],
          { duration: 520 },
        );
      }
    }

    // --- What a double click does ---

    async heelClick() {
      const mood = this._moodName || "happy";
      const pose = this._pose.slice();
      this.mood("grin");
      this.arms("open", "open", 220);
      const T = 980;
      const up = "cubic-bezier(0.2, 0.7, 0.4, 1)";
      const down = "cubic-bezier(0.6, 0, 0.8, 0.4)";
      // (Up and to the side, a moment at the top, and back down where he was)
      const hop = this._animate(
        this._figure,
        [
          { transform: "translate(0, 0) rotate(0deg) scale(1, 1)", offset: 0 },
          { transform: "translate(0, 3px) rotate(0deg) scale(1.05, 0.93)", offset: 0.14, easing: up },
          { transform: "translate(14px, -34px) rotate(5deg) scale(0.98, 1.03)", offset: 0.42 },
          { transform: "translate(17px, -36px) rotate(5deg) scale(1, 1)", offset: 0.56, easing: down },
          { transform: "translate(0, 2px) rotate(0deg) scale(1.05, 0.94)", offset: 0.88 },
          { transform: "translate(0, 0) rotate(0deg) scale(1, 1)", offset: 1 },
        ],
        { duration: T, easing: "linear" },
      );
      // The feet swing apart, then knock together (their inner sides, at the heels) at the top
      const swing = (s) => [
        { transform: "translateX(0) rotate(0deg)", offset: 0 },
        { transform: "translateX(0) rotate(0deg)", offset: 0.2 },
        { transform: `translateX(${-7 * s}px) rotate(${8 * s}deg)`, offset: 0.36 },
        { transform: `translateX(${s}px) rotate(${-10 * s}deg)`, offset: 0.47 },
        { transform: `translateX(${-s}px) rotate(${-6 * s}deg)`, offset: 0.6 },
        { transform: "translateX(0) rotate(0deg)", offset: 0.82 },
        { transform: "translateX(0) rotate(0deg)", offset: 1 },
      ];
      const feet = this._feet.map((foot, i) => this._animate(foot, swing(i === 0 ? 1 : -1), { duration: T }));
      const spark = this._animate(
        this._spark,
        [
          { opacity: 0, transform: "scale(0.5)" },
          { opacity: 1, transform: "scale(1)", offset: 0.3 },
          { opacity: 0, transform: "scale(1.35)" },
        ],
        { duration: 340, delay: 0.46 * T, easing: "ease-out" },
      );
      await Promise.all([hop, ...feet, spark]);
      await Promise.all([this.arms(...pose), this.mood(mood)]);
    }

    async bugOut() {
      const mood = this._moodName || "happy";
      this._holdEyes = true;
      this.eyes("wide");
      this.mouth("o", 120);
      const T = 1150;
      const boing = [
        { transform: "scale(1)" },
        { transform: "scale(1.7)", offset: 0.16 },
        { transform: "scale(1.42)", offset: 0.3 },
        { transform: "scale(1.62)", offset: 0.44 },
        { transform: "scale(1.52)", offset: 0.58 },
        { transform: "scale(1.56)", offset: 0.8 },
        { transform: "scale(1.1)" },
      ];
      const pupil = [
        { transform: "scale(0.72)" },
        { transform: "scale(0.4)", offset: 0.16 },
        { transform: "scale(0.48)", offset: 0.8 },
        { transform: "scale(0.72)" },
      ];
      await Promise.all([
        ...this._eyes.map(({ eye }) => this._animate(eye.querySelector(".open"), boing, { duration: T, easing: "linear" })),
        ...this._eyes.map(({ eye }) => this._animate(eye.querySelector(".pupil"), pupil, { duration: T, easing: "linear" })),
        this._animate(
          this._body,
          [
            { transform: "translateY(0)" },
            { transform: "translateY(-5px)", offset: 0.12 },
            { transform: "translateY(0)", offset: 0.3 },
            { transform: "translateY(0)" },
          ],
          { duration: T, easing: "linear" },
        ),
      ]);
      if (still()) await sleep(700);
      this._holdEyes = false;
      await this.mood(mood);
    }

    async giggle() {
      const mood = this._moodName || "happy";
      this.eyes("happy");
      this._quip("Hee hee!", 1400);
      const shake = this._animate(
        this._body,
        [0, -2, 2, -2, 1.5, -1.5, 1, 0].map((deg) => ({ transform: `rotate(${deg}deg)` })),
        { duration: 900, easing: "linear" },
      );
      for (let n = 0; n < 4 && !still(); n++) {
        await this.mouth("grin", 90);
        await this.mouth("talk", 90);
      }
      await this.mouth("grin", 90);
      await shake;
      if (still()) await sleep(900);
      await this.mood(mood);
    }

    async dizzy() {
      const mood = this._moodName || "happy";
      this._holdEyes = true;
      this.eyes("open");
      this.mouth("wavy");
      const T = 1500;
      const wobble = this._animate(
        this._body,
        [0, -5, 4, -3, 2, -1, 0].map((deg) => ({ transform: `rotate(${deg}deg)` })),
        { duration: T },
      );
      if (still()) await sleep(900);
      else {
        // (The pupils roll around, twice and a half, and a little less far each time)
        const t0 = performance.now();
        await new Promise((done) => {
          const roll = (now) => {
            const k = (now - t0) / T;
            if (k >= 1) return done();
            const a = k * Math.PI * 5;
            this.look(Math.cos(a) * (1 - 0.35 * k), Math.sin(a) * (1 - 0.35 * k));
            requestAnimationFrame(roll);
          };
          requestAnimationFrame(roll);
        });
      }
      await wobble;
      this._holdEyes = false;
      await this.mood(mood);
    }

    async cheer() {
      const mood = this._moodName || "happy";
      const pose = this._pose.slice();
      this.mood("grin");
      this.hop(1);
      for (let n = 0; n < 3; n++) {
        await this.arms("up", "open", 150);
        await this.arms("open", "up", 150);
      }
      if (still()) await sleep(900);
      await Promise.all([this.arms(...pose), this.mood(mood)]);
    }

    // --- His body's cells ---

    cell(row, col, content) {
      const cell = this._cells[row]?.[col];
      if (!cell) return this;
      const spec = content !== null && typeof content === "object" ? content : { text: content };
      cell.text.style.fill = spec.color || "";
      cell.text.style.fontWeight = spec.bold === false ? "400" : "";
      cell.fill.setAttribute("fill", spec.fill || "transparent");
      this._setText(row, col, spec.text == null ? "" : String(spec.text));
      return this;
    }

    cells(contents) {
      const rows = parseCells(contents);
      for (let r = 0; r < 3; r++) {
        for (let c = 0; c < 4; c++) this.cell(r, c, rows[r]?.[c] ?? "");
      }
      return this;
    }

    clear() {
      return this.cells([]);
    }

    async write(contents, ms = 90) {
      const items = typeof contents === "string" ? [...contents] : contents.flat();
      for (let i = 0; i < Math.min(12, items.length); i++) {
        const item = items[i] === " " ? "" : items[i];
        this.cell((i / 4) | 0, i % 4, item);
        if (item !== "" && !still()) await sleep(ms);
      }
      return this;
    }

    heatmap(values, palette = ["#fff0fa", "#f900c3"]) {
      const flat = (Array.isArray(values[0]) ? values.flat() : values).slice(0, 12);
      const lo = Math.min(...flat);
      const hi = Math.max(...flat);
      flat.forEach((v, i) => {
        const cell = this._cells[(i / 4) | 0][i % 4];
        cell.fill.setAttribute("fill", paletteAt(palette, hi > lo ? (v - lo) / (hi - lo) : 0.5));
      });
      return this;
    }

    progress(fraction) {
      const n = Math.round(clamp(fraction, 0, 1) * 12);
      for (let i = 0; i < 12; i++) {
        this._cells[(i / 4) | 0][i % 4].fill.setAttribute("fill", i < n ? "var(--tabblen-accent)" : "transparent");
      }
      return this;
    }

    // The cells' fills (to put back after a trick), and putting them back
    _fills() {
      return this._cells.map((row) => row.map((c) => c.fill.getAttribute("fill")));
    }

    _setFills(fills) {
      this._cells.forEach((row, r) => row.forEach((c, k) => c.fill.setAttribute("fill", fills[r][k])));
    }

    // Change a cell's text alone (keeping its fill and color), squeezing text that's too long for
    // the cell, and popping it in
    _setText(r, c, text, pop = true) {
      const cell = this._cells[r][c];
      if (cell.text.textContent === text) return;
      cell.text.textContent = text;
      cell.text.removeAttribute("textLength");
      cell.text.removeAttribute("lengthAdjust");
      if (text && cell.text.getComputedTextLength && cell.text.getComputedTextLength() > COL - 10) {
        cell.text.setAttribute("textLength", COL - 10);
        cell.text.setAttribute("lengthAdjust", "spacingAndGlyphs");
      }
      if (pop && text) {
        this._animate(cell.text, [{ opacity: 0, transform: "scale(0.6)" }, { opacity: 1, transform: "scale(1)" }], { duration: 260, easing: "ease-out" });
      }
    }

    async cellTrick(row = 0, col = 0, name = this.getAttribute("cell-trick")) {
      const texts = this._cells.flat().map((c) => c.text.textContent);
      // (The tricks with the cells' text need some, so with none there's a ripple)
      const wordy = ["shuffle", "flip", "slots"];
      let trick = CELL_TRICKS.includes(name) ? name : "ripple";
      if (wordy.includes(trick) && texts.every((t) => t === "")) trick = "ripple";
      const mood = this._moodName || "happy";
      const fills = this._fills();
      const at = (i) => [(i / 4) | 0, i % 4];
      const away = (r, c) => Math.abs(r - row) + Math.abs(c - col);

      if (trick === "ripple") {
        this.mood("grin");
        await Promise.all(
          this._cells.flat().map(async (cell, i) => {
            const [r, c] = at(i);
            const d = away(r, c);
            await sleep(still() ? 0 : d * 85);
            cell.fill.setAttribute("fill", paletteAt(["#f900c3", "#fcc2ec", "#fff0fa"], d / 5));
            await sleep(still() ? 700 : 320);
            cell.fill.setAttribute("fill", fills[r][c]);
          }),
        );
        await sleep(still() ? 0 : 350);
      } else if (trick === "shuffle") {
        // (Mixed up a few times, then back the way they were)
        this.mood("surprised");
        for (let n = 0; n < (still() ? 1 : 6); n++) {
          shuffled(texts).forEach((t, i) => this._setText(...at(i), t));
          await sleep(110);
        }
        texts.forEach((t, i) => this._setText(...at(i), t));
        await this.mood("grin");
        await this.hop(1);
        await sleep(still() ? 600 : 200);
      } else if (trick === "flip") {
        // (Upper case to lower and back, as with text_transform())
        this.mood("happy");
        const flips = this._cells.flat().map(async (cell, i) => {
          const [r, c] = at(i);
          const text = texts[i];
          const flipped = text === text.toUpperCase() ? text.toLowerCase() : text.toUpperCase();
          if (flipped === text) return;
          await sleep(still() ? 0 : away(r, c) * 90);
          await this._animate(cell.text, [{ transform: "scaleX(1)" }, { transform: "scaleX(0)" }], { duration: 110, easing: "ease-in" });
          this._setText(r, c, flipped, false);
          await this._animate(cell.text, [{ transform: "scaleX(0)" }, { transform: "scaleX(1)" }], { duration: 130, easing: "ease-out" });
        });
        await Promise.all(flips);
        await this.mood("grin");
        await sleep(still() ? 700 : 450);
      } else if (trick === "slots") {
        // (The text spins, slowing down, and stops in a new order, with the cells that were empty
        // staying so)
        this.mood("surprised");
        const full = texts.map((t, i) => (t === "" ? -1 : i)).filter((i) => i >= 0);
        let order = full.map((i) => texts[i]);
        const spins = still() ? [0] : [60, 60, 70, 80, 95, 115, 140, 170, 210];
        for (const [n, ms] of spins.entries()) {
          order = shuffled(order);
          const last = n === spins.length - 1;
          full.forEach((i, k) => {
            const [r, c] = at(i);
            this._setText(r, c, order[k], last);
            if (!last) {
              this._animate(this._cells[r][c].text, [{ transform: "translateY(-9px)", opacity: 0.5 }, { transform: "translateY(0)", opacity: 1 }], { duration: ms, easing: "ease-out" });
            }
          });
          await sleep(ms);
        }
        await this.mood("grin");
        const won = this._cells[row][col].text.textContent;
        this._quip(won ? `${won}, coming right up!` : "Ta-da!", 1800);
        await sleep(1000);
      } else if (trick === "heatmap") {
        // (Hottest at the cell, cooling away from it, with a little noise)
        this.mood("surprised");
        this.heatmap(this._cells.flat().map((_, i) => -away(...at(i)) + rand(0, 1.4)));
        await sleep(350);
        await this.mood("grin");
        await sleep(still() ? 900 : 1100);
        this._setFills(fills);
        await sleep(still() ? 0 : 350);
      } else if (trick === "zen") {
        // (A calm glow around the edge, from the ring cell nearest the one clicked, ending in the
        // middle)
        this.mood("zen");
        let start = 0;
        RING.forEach(([r, c], i) => {
          if (away(r, c) < away(...RING[start])) start = i;
        });
        for (let n = 0; n < RING.length; n++) {
          const [r, c] = RING[(start + n) % RING.length];
          const cell = this._cells[r][c];
          cell.fill.setAttribute("fill", "#f6d5f0");
          setTimeout(() => cell.fill.setAttribute("fill", fills[r][c]), still() ? 0 : 420);
          await sleep(still() ? 0 : 170);
        }
        for (const [r, c] of [[1, 1], [1, 2]]) this._cells[r][c].fill.setAttribute("fill", "#fcc2ec");
        await sleep(still() ? 900 : 700);
        for (const [r, c] of [[1, 1], [1, 2]]) this._cells[r][c].fill.setAttribute("fill", fills[r][c]);
        await sleep(still() ? 0 : 450);
      }
      await this.mood(mood);
    }

    // --- His voice ---

    async say(text, ms) {
      clearTimeout(this._hushTimer);
      this._bubble.textContent = text;
      this._bubble.classList.add("on");
      // Move the mouth as if talking, a little while for each word
      const back = this._mouthName === "talk" ? "smile" : this._mouthName;
      const words = String(text).split(/\s+/).length;
      if (!still()) {
        for (let n = 0; n < Math.min(6, words); n++) {
          await this.mouth("talk", 90);
          await this.mouth(back, 90);
        }
      }
      this._mouthName = back;
      if (ms === 0) return;
      const wait = ms ?? 1800 + 45 * String(text).length;
      await new Promise((done) => {
        this._hushTimer = setTimeout(() => {
          this.hush();
          done();
        }, wait);
      });
    }

    hush() {
      clearTimeout(this._hushTimer);
      this._bubble.classList.remove("on");
      return this;
    }

    // A word in passing, in the bubble (with the mouth left to whatever else he's doing), unless
    // the bubble's taken by the `say` attribute
    _quip(text, ms = 1600) {
      if (this.hasAttribute("say")) return;
      clearTimeout(this._hushTimer);
      this._bubble.textContent = text;
      this._bubble.classList.add("on");
      this._hushTimer = setTimeout(() => this.hush(), ms);
    }

    // --- Doing things in turn ---

    async play(steps) {
      for (const step of steps) {
        if (typeof step === "function") await step(this);
        else {
          const [name, ...args] = step;
          if (name === "wait") await sleep(args[0] ?? 400);
          else if (typeof this[name] === "function") await this[name](...args);
        }
      }
    }

    seen() {
      this._seenOnce ??= new Promise((done) => {
        if (!("IntersectionObserver" in window)) return done(this);
        const watch = new IntersectionObserver(
          (entries) => {
            if (entries.some((e) => e.isIntersecting)) {
              watch.disconnect();
              done(this);
            }
          },
          { threshold: 0.6 },
        );
        watch.observe(this);
      });
      return this._seenOnce;
    }

    async trick() {
      if (this._busy) return;
      this._busy++;
      const mood = this._moodName || "happy";
      const tricks = [
        () => this.play([["mood", "grin"], ["hop", 2], ["mood", mood]]),
        () => this.play([["mood", "happy"], ["wave", 3], ["mood", mood]]),
        () => this.play([["mood", "surprised"], ["arms", "up"], ["wait", 500], ["arms", ...this._pose], ["mood", mood]]),
        () => this.play([["mood", "love"], ["tap", 3], ["mood", mood]]),
        async () => {
          const before = this._fills();
          for (let i = 0; i <= 12; i++) {
            this.progress(i / 12);
            await sleep(still() ? 0 : 45);
          }
          await this.mood("grin");
          await sleep(500);
          this._setFills(before);
          await this.mood(mood);
        },
      ];
      try {
        await pick(tricks)();
      } finally {
        this._busy--;
      }
    }

    // --- On his own: breathing, blinking and glancing about ---

    _idle() {
      this._stopIdle();
      if (still() || this.hasAttribute("still") || !this._visible || document.hidden) return;
      this._breath = this._body.animate?.(
        [{ transform: "scaleY(1)" }, { transform: "scaleY(1.012)" }],
        { duration: 1900, direction: "alternate", iterations: Infinity, easing: "ease-in-out" },
      );
      const blinkLater = () => {
        this._timers.push(
          setTimeout(async () => {
            const eyes = this._eyes.map((e) => e.eye.dataset.state);
            if (!this._holdEyes && eyes.every((s) => s === "open" || s === "wide")) {
              await this.blink();
              if (Math.random() < 0.2) {
                await sleep(140);
                await this.blink();
              }
            }
            blinkLater();
          }, rand(2400, 6000)),
        );
      };
      const glanceLater = () => {
        this._timers.push(
          setTimeout(async () => {
            if (!this._busy && Date.now() - (this._pointerAt || 0) > 4000) {
              const before = this._look.slice();
              this.look(rand(-1, 1), rand(-0.6, 0.6));
              await sleep(rand(700, 1500));
              if (Date.now() - (this._pointerAt || 0) > 4000) this.look(...before);
            }
            glanceLater();
          }, rand(4000, 9000)),
        );
      };
      blinkLater();
      glanceLater();
    }

    _stopIdle() {
      this._timers.forEach(clearTimeout);
      this._timers = [];
      this._breath?.cancel();
      this._breath = null;
    }

    _follow(on) {
      if (this._onPointer) {
        window.removeEventListener("pointermove", this._onPointer);
        this._onPointer = null;
      }
      if (!on) return;
      let queued = false;
      let last = null;
      this._onPointer = (event) => {
        last = { x: event.clientX, y: event.clientY };
        this._pointerAt = Date.now();
        if (queued) return;
        queued = true;
        requestAnimationFrame(() => {
          queued = false;
          const state = this._eyes[0].eye.dataset.state;
          if (this._visible && !this._holdEyes && (state === "open" || state === "wide")) this.lookAt(last);
        });
      };
      window.addEventListener("pointermove", this._onPointer, { passive: true });
    }
  }

  customElements.define("gt-tabblen", Tabblen);
})();

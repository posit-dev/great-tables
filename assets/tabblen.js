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
//            heatmap, zen, scroll, frame, spanner, merge, footnote, totals, remove, format,
//            formats, substitute, style, paint, colorize, options, stylize, nanoplot, columns, rows,
//            locations, extend, read, sort, export, select or define (see cellTrick())
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
//                                 scroll   the lower rows scroll through the rows of `exibble`
//                                 frame    his header (his head), stub and footer (his feet)
//                                          light up in turn
//                                 spanner  the top row's text moves down, under two spanners
//                                 merge    each row's cells merge in pairs, as "a ± b" and "c–d"
//                                 footnote footnote marks go on the cell and two others, and the
//                                          footer lights up
//                                 totals   the bottom row counts up to the totals of the numbers
//                                          above it
//                                 remove   the text and the lines between the cells go, for a
//                                          moment
//                                 format   the numbers flip over to formatted ones
//                                 formats  each cell spins through formats and stops at one
//                                 substitute  missing, zero, tiny and huge values flip over to
//                                          substitutes
//                                 style    the cell's row, the cell and its column get styles
//                                 paint    his header, column labels, stub, body and footer get
//                                          a fill each
//                                 colorize the numbers color their cells, in two palettes
//                                 options  a font, fills, striping and a border go over his
//                                          parts in turn
//                                 stylize  his column labels and striping go through the colors
//                                          of opt_stylize()
//                                 nanoplot each row's numbers make a line plot, then a bar plot
//                                 columns  columns light up, picked by name, by a first letter,
//                                          as numeric ones and as all of them
//                                 rows     rows light up, picked by the cell's, by the others
//                                          and as all of them
//                                 locations  a target moves over his parts in turn, as the
//                                          loc.*() specifiers pick them, and ends on the cell
//                                 extend   columns of numbers turn into gt-extras add-ons: star
//                                          ratings, bars and purple-to-green fills
//                                 read     cells are read out as a screen reader would, with
//                                          their headers
//                                 sort     the rows sort by the cell's column, up and down, and
//                                          then a search leaves the rows with the cell's text
//                                 export   the rows turn into lines of CSV and drop into his feet
//                                 select   the cell's row is selected, and Python reads the
//                                          selection, sets another and clears it
//                                 define   the cells flip over to the names of his parts, and
//                                          the cell's part is defined
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
  const CELL_TRICKS = [
    "ripple", "shuffle", "flip", "slots", "heatmap", "zen", "scroll", "frame", "spanner", "merge", "footnote",
    "totals", "remove", "format", "formats", "substitute", "style", "paint", "colorize", "options", "stylize",
    "nanoplot", "columns", "rows", "locations", "extend", "read", "sort", "export", "select", "define",
  ];

  // The rows of the `exibble` dataset (some of its columns, shortened), for the scroll cell trick
  const EXIBBLE = [
    ["0.11", "apricot", "one", "13:35"],
    ["2.22", "banana", "two", "14:40"],
    ["33.3", "coconut", "three", "15:45"],
    ["444", "durian", "four", "16:50"],
    ["5550", "", "five", "17:55"],
    ["", "fig", "six", ""],
    ["777k", "grapefruit", "seven", "19:10"],
    ["8.9M", "honeydew", "eight", "20:20"],
  ];

  // A tint of the accent, for lighting up his parts (it works on light and dark pages alike)
  const TINT = "rgba(249, 0, 195, 0.2)";

  // Values and how a fmt_*() method shows them (a fmt_percent(), fmt_fraction(), fmt_bytes(),
  // fmt_duration(), fmt_tf() twice, fmt_chem(), fmt_units(), fmt_scientific(), fmt_currency(),
  // fmt_roman() and fmt_number() with compact numbers), for the formats cell trick
  const FORMATS = [
    ["0.25", "25%"], ["1.75", "1¾"], ["1.5e6", "1.5 MB"], ["7500", "2h 5m"],
    ["True", "✓"], ["False", "✗"], ["H2O", "H₂O"], ["m s^-2", "m s⁻²"],
    ["6e23", "6×10²³"], ["4.99", "$4.99"], ["3", "III"], ["1500", "1.5K"],
  ];

  // Light colors of ColorBrewer's Paired scheme (as on the Styling the Whole Table page), a little
  // see-through, for the paint cell trick
  const PAIRED = ["#a6cee3", "#b2df8a", "#fb9a99", "#fdbf6f", "#cab2d6"].map((hex) => `${hex}cc`);

  // Two of ColorBrewer's palettes (with five of their colors), for the colorize cell trick
  const BREWER = [
    ["PuRd", ["#f7f4f9", "#d4b9da", "#df65b0", "#ce1256", "#67001f"]],
    ["YlGnBu", ["#ffffd9", "#c7e9b4", "#41b6c4", "#225ea8", "#081d58"]],
  ];

  // The colors of opt_stylize() (of its column labels), for the stylize cell trick, ending with
  // the blue that's its default
  const STYLIZE = [
    ["cyan", "#01837B"], ["pink", "#CB2A7B"], ["green", "#038901"], ["red", "#E4220C"], ["gray", "#5F5F5F"],
    ["blue", "#0076BA"],
  ];

  // The teal of the options cell trick's theme
  const TEAL = "#01837B";

  // ColorBrewer's PRGn palette (with three of its colors), as gt-extras' gt_hulk_col_numeric()
  // uses, for the extend cell trick
  const PRGN = ["#762a83", "#f7f7f7", "#1b7837"];

  // His parts, with what the glossary says of them, for the define cell trick
  const TERMS = {
    stubhead: "Stubhead: the label over the stub",
    label: "Column labels: a name for each column",
    stub: "Stub: the labels of the rows",
    cell: "Cell: one value in the body",
  };

  const compact = new Intl.NumberFormat("en", { notation: "compact", maximumFractionDigits: 2 });

  // The runs of numbers that follow on from each other in a sorted list: [[first, last], ...]
  const runs = (items) =>
    items.reduce((out, n) => {
      const last = out[out.length - 1];
      if (last && n === last[1] + 1) last[1] = n;
      else out.push([n, n]);
      return out;
    }, []);

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
    .grid line { transition: opacity 0.2s ease; }
    .summary-line { opacity: 0; }
    .border { fill: none; stroke: var(--tabblen-accent); stroke-width: 3.4; }
    .foot { transition: fill 0.35s ease; }
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
    .cell-text { fill: var(--tabblen-cell); font-size: 24px; font-weight: 600; text-anchor: middle; dominant-baseline: central; transform-box: fill-box; transform-origin: center; transition: fill 0.35s ease; }
    .mark { fill: var(--tabblen-accent); font-size: 15px; font-weight: 700; }
    .plot { fill: none; stroke: var(--tabblen-accent); stroke-width: 2.6; stroke-linecap: round; stroke-linejoin: round; }
    .dot { fill: var(--tabblen-bubble); stroke: var(--tabblen-accent); stroke-width: 2; transform-box: fill-box; transform-origin: center; }
    .bar { fill: var(--tabblen-accent); transform-box: fill-box; transform-origin: bottom; }
    .star { fill: none; stroke: var(--tabblen-cell); stroke-width: 1.2; stroke-linejoin: round; transform-box: fill-box; transform-origin: center; }
    .star.on { fill: var(--tabblen-accent); stroke: var(--tabblen-accent); }
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
      .pupil, .eye > *, .cell-fill, .cell-text, .grid line, .foot, .bubble, .name span, svg:hover ~ .name span { transition: none; }
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

  // Text that's easy to read on a color (an rgb() one, as from paletteAt()), as data_color() picks
  function textOn(color) {
    const [r, g, b] = color.match(/\d+/g).map(Number);
    return 0.299 * r + 0.587 * g + 0.114 * b > 150 ? "#2b2b33" : "#fff";
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

      // The cells (their fills, then their text), under the lines, with a fill for the header
      // too (for lighting it up)
      this._cells = [];
      const cellLayer = el("g", {}, body);
      this._headFill = el("rect", { class: "cell-fill", x: 0, y: 0, width: W, height: HEAD, fill: "transparent" }, cellLayer);
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
      // (Text over cells that are merged)
      this._mergeLayer = el("g", {}, cellLayer);

      const lines = el("g", { class: "ink" }, body);
      el("rect", { x: 0, y: 0, width: W, height: BOTTOM }, lines);
      el("line", { x1: 0, y1: HEAD, x2: W, y2: HEAD }, lines);
      const grid = el("g", { class: "grid" }, lines);
      // (The lines between columns go a row at a time, so that cells in a row can be merged,
      // with the line between them taken away)
      this._vlines = [0, 1, 2].map((r) =>
        [1, 2, 3].map((c) => el("line", { x1: c * COL, y1: HEAD + r * ROW, x2: c * COL, y2: HEAD + (r + 1) * ROW }, grid)),
      );
      this._hlines = [1, 2].map((r) => el("line", { x1: 0, y1: HEAD + r * ROW, x2: W, y2: HEAD + r * ROW }, grid));
      // (A summary row's double line, over the bottom row)
      this._summaryLine = el("line", { class: "summary-line", x1: 0, y1: HEAD + 2 * ROW + 3.5, x2: W, y2: HEAD + 2 * ROW + 3.5 }, grid);
      // (Over the lines: borders put on cells)
      this._borders = el("g", {}, body);

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
      // (Text that's fitted into the cells is fitted again in the page's fonts, once they're in)
      document.fonts?.ready.then(() => this._cells.flat().forEach((cell) => this._fit(cell.text, COL - 10)));
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

    // Change a cell's text alone (keeping its fill and color), fitting it into the cell, and
    // popping it in
    _setText(r, c, text, pop = true) {
      const cell = this._cells[r][c];
      if (cell.text.textContent === text) return;
      cell.text.textContent = text;
      this._fit(cell.text, COL - 10);
      if (pop && text) this._pop(cell.text);
    }

    _pop(node) {
      return this._animate(node, [{ opacity: 0, transform: "scale(0.6)" }, { opacity: 1, transform: "scale(1)" }], { duration: 260, easing: "ease-out" });
    }

    // Fit text into so much room: in a smaller font if it's too long, and squeezed if that's not
    // enough
    _fit(node, room) {
      node.style.fontSize = "";
      node.removeAttribute("textLength");
      node.removeAttribute("lengthAdjust");
      if (!node.textContent || !node.getComputedTextLength) return;
      const width = node.getComputedTextLength();
      if (width <= room) return;
      const size = parseFloat(getComputedStyle(node).fontSize) || 24;
      node.style.fontSize = `${Math.max(15, Math.floor((2 * size * room) / width) / 2)}px`;
      if (node.getComputedTextLength() > room) {
        node.setAttribute("textLength", room);
        node.setAttribute("lengthAdjust", "spacingAndGlyphs");
      }
    }

    // Merge the cells of a row from one column to another, with text over them (and their own
    // text hidden), and take the merges away
    _merge(r, c0, c1, text, color = "") {
      for (let c = c0; c <= c1; c++) {
        this._cells[r][c].text.style.opacity = "0";
        if (c > c0) this._vlines[r][c - 1].style.opacity = "0";
      }
      const node = el("text", { class: "cell-text", x: ((c0 + c1 + 1) * COL) / 2, y: HEAD + r * ROW + ROW / 2 + 0.5 }, this._mergeLayer);
      node.textContent = text;
      node.style.fill = color;
      this._fit(node, (c1 - c0 + 1) * COL - 12);
      this._animate(node, [{ opacity: 0, transform: "scaleX(0.3)" }, { opacity: 1, transform: "scaleX(1)" }], { duration: 280, easing: "ease-out" });
      return node;
    }

    _unmerge() {
      this._mergeLayer.replaceChildren();
      this._vlines.flat().forEach((line) => (line.style.opacity = ""));
      this._cells.flat().forEach((cell) => (cell.text.style.opacity = ""));
    }

    // Fill his feet (his footer), or empty them with ""
    _fillFeet(fill) {
      this._feet.forEach((foot) => (foot.style.fill = fill));
    }

    // Flip the cells over to new text (the ones it changes), from a cell out
    _flipTo(texts, row, col, step = 90) {
      return Promise.all(
        this._cells.flat().map(async (cell, i) => {
          const [r, c] = [(i / 4) | 0, i % 4];
          if (texts[i] === cell.text.textContent) return;
          await sleep(still() ? 0 : (Math.abs(r - row) + Math.abs(c - col)) * step);
          await this._animate(cell.text, [{ transform: "scaleX(1)" }, { transform: "scaleX(0)" }], { duration: 110, easing: "ease-in" });
          this._setText(r, c, texts[i], false);
          await this._animate(cell.text, [{ transform: "scaleX(0)" }, { transform: "scaleX(1)" }], { duration: 130, easing: "ease-out" });
        }),
      );
    }

    async cellTrick(row = 0, col = 0, name = this.getAttribute("cell-trick")) {
      const texts = this._cells.flat().map((c) => c.text.textContent);
      const at = (i) => [(i / 4) | 0, i % 4];
      const away = (r, c) => Math.abs(r - row) + Math.abs(c - col);
      const number = (text) => (text !== "" && isFinite(Number(text.replace(/,/g, ""))) ? Number(text.replace(/,/g, "")) : null);
      // (How fmt_number() would show the text, if it's a number, and how a sub_*() method would
      // show it, if it's missing, zero, too small or too large)
      const formatted = (t) => {
        const v = number(t);
        if (v === null) return t;
        return Math.abs(v) >= 1000 ? compact.format(v) : v.toFixed(2);
      };
      const substituted = (t) => {
        if (["None", "NaN", "NA", "null"].includes(t)) return "—";
        const v = number(t);
        if (v === null) return t;
        if (v === 0) return "nil";
        if (Math.abs(v) < 0.01) return "<0.01";
        return Math.abs(v) >= 1e12 ? "≥1e+12" : t;
      };
      // (The tricks with the cells' text need some, and others need numbers, or values to
      // substitute, so without them there's a ripple)
      const wordy = ["shuffle", "flip", "slots", "merge", "remove", "read", "sort", "export"];
      let trick = CELL_TRICKS.includes(name) ? name : "ripple";
      if (wordy.includes(trick) && texts.every((t) => t === "")) trick = "ripple";
      if (trick === "totals" && texts.slice(0, 8).every((t) => number(t) === null)) trick = "ripple";
      if (trick === "format" && texts.every((t) => formatted(t) === t)) trick = "ripple";
      if (trick === "substitute" && texts.every((t) => substituted(t) === t)) trick = "ripple";
      if (trick === "colorize" && texts.every((t) => number(t) === null)) trick = "ripple";
      // (A nanoplot needs a row with two numbers or more)
      const series = [0, 1, 2].map((r) => texts.slice(r * 4, r * 4 + 4).map(number));
      const plotted = series.map((values) => values.filter((v) => v !== null).length > 1);
      if (trick === "nanoplot" && !plotted.some(Boolean)) trick = "ripple";
      // (The extend trick needs a column of numbers, beside the stub)
      const numbered = [1, 2, 3].filter((c) => [1, 2].every((r) => number(texts[r * 4 + c]) !== null));
      if (trick === "extend" && !numbered.length) trick = "ripple";
      const mood = this._moodName || "happy";
      const fills = this._fills();

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
        await this._flipTo(texts.map((t) => (t === t.toUpperCase() ? t.toLowerCase() : t.toUpperCase())), row, col);
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
      } else if (trick === "scroll") {
        // (The rows under the top one scroll up through exibble's, slowing down to its last two,
        // and then the cells are put back)
        this.mood("happy");
        this.look(0, 0.5);
        const pace = still() ? [0] : [140, 140, 160, 190, 240, 320];
        for (const [n, ms] of pace.entries()) {
          const first = still() ? EXIBBLE.length - 2 : n + 1;
          for (let r = 1; r < 3; r++) {
            EXIBBLE[first + r - 1].forEach((t, c) => {
              this._setText(r, c, t, false);
              this._animate(this._cells[r][c].text, [{ transform: "translateY(12px)", opacity: 0.4 }, { transform: "translateY(0)", opacity: 1 }], { duration: ms, easing: "ease-out" });
            });
          }
          await sleep(ms);
        }
        await this.mood("grin");
        this._quip("That’s all of exibble!", 1600);
        await sleep(1500);
        texts.forEach((t, i) => this._setText(...at(i), t));
        await sleep(still() ? 0 : 300);
      } else if (trick === "frame") {
        // (His head is his header, his left column is his stub and his feet are his footer, and
        // they light up in turn, with him looking at each)
        this.mood("happy");
        this._holdEyes = true;
        const parts = [
          ["Header!", [0, -1], (on) => this._headFill.setAttribute("fill", on ? TINT : "transparent")],
          ["Stub!", [-1, 0.3], (on) => this._cells.forEach((cells, r) => cells[0].fill.setAttribute("fill", on ? TINT : fills[r][0]))],
          ["Footer!", [0, 1], (on) => this._fillFeet(on ? TINT : "")],
        ];
        for (const [word, xy, light] of parts) {
          light(true);
          this.look(...xy);
          this._quip(word, 700);
          await sleep(still() ? 900 : 750);
          light(false);
        }
        this._holdEyes = false;
        await this.mood("grin");
        await this.hop(1);
        await sleep(still() ? 600 : 250);
      } else if (trick === "spanner") {
        // (The text moves down a row, out of the way of two spanners, which go over the columns
        // on the side of the cell first)
        this.mood("surprised");
        for (let r = 2; r > 0; r--) {
          for (let c = 0; c < 4; c++) {
            this._setText(r, c, texts[(r - 1) * 4 + c], false);
            this._animate(this._cells[r][c].text, [{ transform: `translateY(${-ROW}px)` }, { transform: "translateY(0)" }], { duration: 300, easing: "ease-out" });
          }
        }
        for (let c = 0; c < 4; c++) this._setText(0, c, "", false);
        await sleep(still() ? 0 : 320);
        const spanners = [[0, 1, "Time"], [2, 3, "Measurement"]];
        if (col >= 2) spanners.reverse();
        for (const [c0, c1, label] of spanners) {
          this._merge(0, c0, c1, label, "var(--tabblen-accent)");
          await sleep(still() ? 0 : 240);
        }
        await this.mood("grin");
        this._quip("Spanners!", 1500);
        await sleep(1500);
        this._unmerge();
        texts.forEach((t, i) => this._setText(...at(i), t));
        await sleep(still() ? 0 : 300);
      } else if (trick === "merge") {
        // (In each row, from the cell's out, the first two cells come together as a value with
        // its uncertainty, and the last two as a range)
        this.mood("happy");
        const joins = [" ± ", "–"];
        await Promise.all(
          [0, 1, 2].map(async (r) => {
            await sleep(still() ? 0 : Math.abs(r - row) * 160);
            for (const c0 of [0, 2]) {
              [c0, c0 + 1].forEach((c, k) => {
                const text = this._cells[r][c].text;
                text.style.opacity = "0";
                this._animate(text, [{ opacity: 1, transform: "translateX(0)" }, { opacity: 0, transform: `translateX(${(k ? -COL : COL) / 2}px)` }], { duration: 220, easing: "ease-in" });
              });
            }
            await sleep(still() ? 0 : 220);
            for (const [k, c0] of [0, 2].entries()) {
              const [a, b] = [texts[r * 4 + c0], texts[r * 4 + c0 + 1]];
              this._merge(r, c0, c0 + 1, a && b ? a + joins[k] + b : a || b);
            }
          }),
        );
        await this.mood("grin");
        this._quip("Two columns, one value!", 1600);
        await sleep(1600);
        this._unmerge();
        this._cells.flat().forEach((cell) => cell.text.textContent && this._pop(cell.text));
        await sleep(still() ? 0 : 300);
      } else if (trick === "footnote") {
        // (Marks go on the cell and two others, numbered in reading order, and then his footer
        // lights up, with him looking down at it)
        this.mood("happy");
        const others = shuffled([...texts.keys()].filter((i) => i !== row * 4 + col && texts[i] !== ""));
        const marked = [row * 4 + col, ...others.slice(0, 2)].sort((a, b) => a - b);
        const marks = [];
        for (const [n, i] of marked.entries()) {
          const text = this._cells[(i / 4) | 0][i % 4].text;
          const mark = el("tspan", { class: "mark", dy: -8 }, text);
          mark.textContent = String(n + 1);
          marks.push(mark);
          this._pop(text);
          await sleep(still() ? 0 : 280);
        }
        this._holdEyes = true;
        this.look(0, 1);
        this._fillFeet(TINT);
        this._quip("See the footer!", 1500);
        await sleep(1500);
        this._fillFeet("");
        marks.forEach((mark) => mark.remove());
        this._holdEyes = false;
        await this.mood("grin");
        await sleep(still() ? 600 : 300);
      } else if (trick === "totals") {
        // (A grand summary row: under a double line, the bottom row counts up to the totals of
        // the numbers above it)
        const sums = [0, 1, 2, 3].map((c) => {
          const values = [texts[c], texts[4 + c]].map(number).filter((v) => v !== null);
          return values.length ? values.reduce((a, b) => a + b, 0) : null;
        });
        const places = (c) => Math.max(0, ...[texts[c], texts[4 + c]].map((t) => (t.split(".")[1] || "").length));
        const shown = (c, k) => (sums[c] === null ? "" : (sums[c] * k).toFixed(places(c)));
        this.mood("surprised");
        this._summaryLine.style.opacity = "1";
        this._cells[2].forEach((cell) => cell.fill.setAttribute("fill", TINT));
        const frames = still() ? 1 : 16;
        for (let f = 1; f <= frames; f++) {
          for (let c = 0; c < 4; c++) this._setText(2, c, shown(c, ease(f / frames)), f === frames);
          await sleep(still() ? 0 : 40);
        }
        await this.mood("grin");
        this._quip(sums[col] === null ? "Totals!" : `Total: ${shown(col, 1)}`, 1600);
        await sleep(1600);
        this._summaryLine.style.opacity = "";
        this._cells[2].forEach((cell, c) => {
          cell.fill.setAttribute("fill", fills[2][c]);
          this._setText(2, c, texts[8 + c]);
        });
        await sleep(still() ? 0 : 350);
      } else if (trick === "remove") {
        // (As with the rm_*() methods: the text goes, from the cell out, then the lines between
        // the cells, and then it all comes back)
        this.mood("surprised");
        const cells = this._cells.flat();
        await Promise.all(
          cells.map(async (cell, i) => {
            if (!texts[i]) return;
            await sleep(still() ? 0 : away(...at(i)) * 90);
            cell.text.style.opacity = "0";
            await this._animate(cell.text, [{ opacity: 1, transform: "scale(1)" }, { opacity: 0, transform: "scale(0.2)" }], { duration: 220, easing: "ease-in" });
          }),
        );
        const grid = [...this._vlines.flat(), ...this._hlines];
        grid.forEach((line) => (line.style.opacity = "0"));
        this._quip("All gone!", 1100);
        await sleep(1200);
        await this.mood("grin");
        this._quip("Just kidding!", 1400);
        grid.forEach((line) => (line.style.opacity = ""));
        await Promise.all(
          cells.map(async (cell, i) => {
            await sleep(still() ? 0 : away(...at(i)) * 70);
            cell.text.style.opacity = "";
            if (texts[i]) this._pop(cell.text);
          }),
        );
        await sleep(still() ? 900 : 700);
      } else if (trick === "format") {
        // (The numbers flip over to how fmt_number() would show them, and back)
        this.mood("happy");
        await this._flipTo(texts.map(formatted), row, col);
        await this.mood("grin");
        this._quip("Much better!", 1500);
        await sleep(1700);
        await this._flipTo(texts, row, col, 50);
        await sleep(still() ? 0 : 300);
      } else if (trick === "formats") {
        // (Each cell spins through the formats, from the cell out, and stops at its own)
        this.mood("surprised");
        await Promise.all(
          this._cells.flat().map(async (cell, i) => {
            const [r, c] = at(i);
            await sleep(still() ? 0 : away(r, c) * 70);
            for (let n = 0; n < (still() ? 0 : 5); n++) {
              this._setText(r, c, pick(FORMATS)[1], false);
              this._animate(cell.text, [{ transform: "translateY(-9px)", opacity: 0.5 }, { transform: "translateY(0)", opacity: 1 }], { duration: 75, easing: "ease-out" });
              await sleep(75);
            }
            this._setText(r, c, FORMATS[i][1]);
          }),
        );
        await this.mood("grin");
        this._quip("A format for everything!", 1700);
        await sleep(1800);
        await this._flipTo(texts, row, col, 50);
        await sleep(still() ? 0 : 300);
      } else if (trick === "substitute") {
        // (The values that look awkward light up and shake, then flip over to what the sub_*()
        // methods put in their place, and back)
        this.mood("surprised");
        const awkward = this._cells.flat().filter((_, i) => substituted(texts[i]) !== texts[i]);
        awkward.forEach((cell) => {
          cell.fill.setAttribute("fill", TINT);
          this._animate(cell.text, [0, -10, 10, -8, 6, 0].map((deg) => ({ transform: `rotate(${deg}deg)` })), { duration: 500 });
        });
        await sleep(650);
        await this._flipTo(texts.map(substituted), row, col);
        this._setFills(fills);
        await this.mood("grin");
        this._quip("Much clearer!", 1500);
        await sleep(1700);
        await this._flipTo(texts, row, col, 50);
        await sleep(still() ? 0 : 300);
      } else if (trick === "style") {
        // (As with tab_style(): the cell's row gets a fill and italic text, the cell its own fill
        // and white text, and its column a border)
        this.mood("happy");
        const cell = this._cells[row][col];
        const color = cell.text.style.fill;
        this._cells[row].forEach((c) => {
          c.fill.setAttribute("fill", TINT);
          c.text.style.fontStyle = "italic";
        });
        await sleep(still() ? 0 : 400);
        cell.fill.setAttribute("fill", "var(--tabblen-accent)");
        cell.text.style.fill = "#fff";
        this._pop(cell.text);
        await sleep(still() ? 0 : 400);
        const border = el("rect", { class: "border", x: col * COL + 1.7, y: HEAD + 1.7, width: COL - 3.4, height: 3 * ROW - 3.4 }, this._borders);
        this._animate(border, [{ opacity: 0 }, { opacity: 1 }], { duration: 250 });
        await this.mood("grin");
        this._quip("Styled!", 1500);
        await sleep(1700);
        border.remove();
        this._setFills(fills);
        cell.text.style.fill = color;
        this._cells[row].forEach((c) => (c.text.style.fontStyle = ""));
        await sleep(still() ? 0 : 350);
      } else if (trick === "paint") {
        // (His parts get a fill each, as with tab_style() at each loc: his header, his column
        // labels (the top row), his stub (the left column), his body and his footer (his feet))
        this.mood("surprised");
        const paint = [
          () => this._headFill.setAttribute("fill", PAIRED[0]),
          () => this._cells[0].forEach((c) => c.fill.setAttribute("fill", PAIRED[1])),
          () => [1, 2].forEach((r) => this._cells[r][0].fill.setAttribute("fill", PAIRED[2])),
          () => [1, 2].forEach((r) => [1, 2, 3].forEach((c) => this._cells[r][c].fill.setAttribute("fill", PAIRED[3]))),
          () => this._fillFeet(PAIRED[4]),
        ];
        for (const step of paint) {
          step();
          await sleep(still() ? 0 : 260);
        }
        await this.mood("grin");
        this._quip("Every part, styled!", 1600);
        await this.hop(1);
        await sleep(1400);
        this._headFill.setAttribute("fill", "transparent");
        this._setFills(fills);
        this._fillFeet("");
        await sleep(still() ? 0 : 350);
      } else if (trick === "colorize") {
        // (As with data_color(): the numbers fill their cells, from the cell out, with their text
        // in a color that's easy to read on the fill, in one palette and then another)
        this.mood("love");
        const cells = this._cells.flat();
        const colors = cells.map((cell) => cell.text.style.fill);
        const values = texts.map(number);
        const known = values.filter((v) => v !== null);
        const [lo, hi] = [Math.min(...known), Math.max(...known)];
        for (const [name, palette] of BREWER) {
          await Promise.all(
            cells.map(async (cell, i) => {
              if (values[i] === null) return;
              await sleep(still() ? 0 : away(...at(i)) * 80);
              const fill = paletteAt(palette, hi > lo ? (values[i] - lo) / (hi - lo) : 0.5);
              cell.fill.setAttribute("fill", fill);
              cell.text.style.fill = textOn(fill);
            }),
          );
          this._quip(`palette="${name}"`, 1200);
          await sleep(still() ? 1300 : 1400);
        }
        await this.mood("grin");
        this._setFills(fills);
        cells.forEach((cell, i) => (cell.text.style.fill = colors[i]));
        await sleep(still() ? 0 : 400);
      } else if (trick === "options") {
        // (As with tab_options(), broad changes go over whole parts in turn: a font for the whole
        // table, fills for his header and column labels, striping for his body and a border
        // around it all)
        this.mood("happy");
        const cells = this._cells.flat();
        const colors = cells.map((cell) => cell.text.style.fill);
        const border = el("rect", { class: "border", x: 1.7, y: 1.7, width: W - 3.4, height: BOTTOM - 3.4 });
        border.style.stroke = TEAL;
        const steps = [
          ["New font!", () => cells.forEach((cell) => {
            cell.text.style.fontFamily = "Georgia, serif";
            this._fit(cell.text, COL - 10);
            if (cell.text.textContent) this._pop(cell.text);
          })],
          ["Header fill!", () => this._headFill.setAttribute("fill", `${TEAL}40`)],
          ["Column labels!", () => this._cells[0].forEach((cell) => {
            cell.fill.setAttribute("fill", TEAL);
            cell.text.style.fill = "#fff";
          })],
          ["Striping!", () => this._cells[2].forEach((cell) => cell.fill.setAttribute("fill", `${TEAL}2e`))],
          ["A border!", () => this._borders.appendChild(border)],
        ];
        for (const [word, step] of steps) {
          step();
          this._quip(word, 600);
          await sleep(still() ? 800 : 700);
        }
        await this.mood("grin");
        this._quip("One method, every option!", 1600);
        await this.hop(1);
        await sleep(1500);
        border.remove();
        this._headFill.setAttribute("fill", "transparent");
        this._setFills(fills);
        cells.forEach((cell, i) => {
          cell.text.style.fill = colors[i];
          cell.text.style.fontFamily = "";
          this._fit(cell.text, COL - 10);
        });
        await sleep(still() ? 0 : 400);
      } else if (trick === "stylize") {
        // (As with opt_stylize(), in each of its colors: the column labels (the top row) in the
        // color, with white text, and the body striped with a tint of it, ending in the blue)
        this.mood("surprised");
        const colors = this._cells.flat().map((cell) => cell.text.style.fill);
        for (const [name, hex] of STYLIZE) {
          this._cells[0].forEach((cell) => {
            cell.fill.setAttribute("fill", hex);
            cell.text.style.fill = "#fff";
          });
          this._cells[2].forEach((cell) => cell.fill.setAttribute("fill", `${hex}2e`));
          this._quip(`color="${name}"`, 600);
          await sleep(still() ? 700 : 650);
        }
        await this.mood("grin");
        this._quip("Pick a color, any color!", 1500);
        await sleep(1600);
        this._setFills(fills);
        this._cells.flat().forEach((cell, i) => (cell.text.style.fill = colors[i]));
        await sleep(still() ? 0 : 400);
      } else if (trick === "nanoplot") {
        // (As with fmt_nanoplot(): the rows with numbers make a line plot each, from the cell's
        // row out, with each row scaled on its own; then the plots turn into bar plots)
        this.mood("surprised");
        const x = (c) => c * COL + COL / 2;
        const plots = series.map((values, r) => {
          if (!plotted[r]) return null;
          const known = values.filter((v) => v !== null);
          const [top, bottom] = [HEAD + r * ROW + 7, HEAD + (r + 1) * ROW - 6];
          const [lo, hi] = [Math.min(...known), Math.max(...known)];
          const y = (v) => (hi > lo ? bottom - ((v - lo) / (hi - lo)) * (bottom - top) : (top + bottom) / 2);
          // (The bars go from zero, or the lowest value under it, with more of the row's height)
          const base = Math.min(0, lo);
          const floor = bottom + 3;
          const height = (v) => Math.max(2, ((v - base) / (hi - base || 1)) * (floor - top + 3));
          const points = values.map((v, c) => (v === null ? null : [x(c), y(v)])).filter(Boolean);
          return { r, values, bottom, floor, height, points };
        });
        const hideRow = (r) => {
          for (let c = 0; c < 4; c++) {
            const text = this._cells[r][c].text;
            text.style.opacity = "0";
            this._animate(text, [{ opacity: 1 }, { opacity: 0 }], { duration: 180 });
            if (c > 0) this._vlines[r][c - 1].style.opacity = "0";
          }
        };
        await Promise.all(
          plots.filter(Boolean).map(async ({ r, bottom, points }) => {
            await sleep(still() ? 0 : Math.abs(r - row) * 220);
            hideRow(r);
            await sleep(still() ? 0 : 180);
            const xy = points.map((p) => p.join(",")).join(" ");
            const first = points[0][0];
            const last = points[points.length - 1][0];
            const area = el("polygon", { points: `${first},${bottom} ${xy} ${last},${bottom}`, fill: TINT }, this._mergeLayer);
            const line = el("polyline", { class: "plot", points: xy }, this._mergeLayer);
            const length = line.getTotalLength ? line.getTotalLength() : 300;
            this._animate(area, [{ opacity: 0 }, { opacity: 1 }], { duration: 450 });
            await this._animate(line, [{ strokeDasharray: length, strokeDashoffset: length }, { strokeDasharray: length, strokeDashoffset: 0 }], { duration: 420, easing: "ease-out" });
            for (const [cx, cy] of points) this._pop(el("circle", { class: "dot", cx, cy, r: 3.4 }, this._mergeLayer));
          }),
        );
        await this.mood("grin");
        this._quip("Nanoplots!", 1300);
        await sleep(1500);
        this._mergeLayer.replaceChildren();
        this.mood("surprised");
        await Promise.all(
          plots.filter(Boolean).map(async ({ r, values, floor, height }) => {
            await sleep(still() ? 0 : Math.abs(r - row) * 150);
            for (const [c, v] of values.entries()) {
              if (v === null) continue;
              const bar = el("rect", { class: "bar", x: x(c) - 7, y: floor - height(v), width: 14, height: height(v) }, this._mergeLayer);
              this._animate(bar, [{ transform: "scaleY(0)" }, { transform: "scaleY(1)" }], { duration: 300, easing: "ease-out" });
              await sleep(still() ? 0 : 60);
            }
          }),
        );
        await this.mood("grin");
        this._quip('plot_type="bar"', 1300);
        await sleep(1500);
        this._unmerge();
        this._cells.flat().forEach((cell) => cell.text.textContent && this._pop(cell.text));
        await sleep(still() ? 0 : 300);
      } else if (trick === "columns" || trick === "rows") {
        // (Columns or rows are picked in turn, as with columns= and rows=, and light up with a
        // border around them, with him looking at them: columns by the cell's column's name, by
        // its first letter (with a Polars selector), as numeric ones and then all of them, and
        // rows by the cell's, by the others and then all of them)
        this.mood("happy");
        this._holdEyes = true;
        let picks;
        if (trick === "columns") {
          const name = texts[col];
          const numeric = [0, 1, 2, 3].filter((c) => [1, 2].every((r) => number(texts[r * 4 + c]) !== null));
          picks = [
            [name ? `columns="${name}"` : `columns=${col}`, [col]],
            ...(name ? [[`cs.starts_with("${name[0]}")`, [0, 1, 2, 3].filter((c) => texts[c].startsWith(name[0]))]] : []),
            ...(numeric.length ? [["cs.numeric()", numeric]] : []),
            ["cs.all()", [0, 1, 2, 3]],
          ];
        } else {
          const others = [0, 1, 2].filter((r) => r !== row);
          picks = [
            [`rows=${row}`, [row]],
            [`rows=[${others.join(", ")}]`, others],
            ["rows=None", [0, 1, 2]],
          ];
        }
        for (const [quip, picked] of picks) {
          this._setFills(fills);
          this._borders.replaceChildren();
          for (const [a, b] of runs(picked)) {
            const span = b - a + 1;
            if (trick === "columns") {
              this._cells.forEach((cells) => cells.slice(a, b + 1).forEach((cell) => cell.fill.setAttribute("fill", TINT)));
              el("rect", { class: "border", x: a * COL + 1.7, y: HEAD + 1.7, width: span * COL - 3.4, height: 3 * ROW - 3.4 }, this._borders);
            } else {
              this._cells.slice(a, b + 1).flat().forEach((cell) => cell.fill.setAttribute("fill", TINT));
              el("rect", { class: "border", x: 1.7, y: HEAD + a * ROW + 1.7, width: W - 3.4, height: span * ROW - 3.4 }, this._borders);
            }
          }
          const mid = picked.reduce((sum, n) => sum + n, 0) / picked.length;
          if (trick === "columns") this.look((mid - 1.5) / 1.5, 0.6);
          else this.look(0, 0.3 + mid * 0.35);
          this._quip(quip, 900);
          await sleep(still() ? 1100 : 1000);
        }
        this._setFills(fills);
        this._borders.replaceChildren();
        this._holdEyes = false;
        await this.mood("grin");
        await this.hop(1);
        await sleep(still() ? 600 : 250);
      } else if (trick === "locations") {
        // (A target moves over his parts as the loc.*() specifiers pick them, with each part
        // lighting up and him looking at it, and it ends on the cell, picked by its own location)
        this.mood("happy");
        this._holdEyes = true;
        const tint = (cells) => (on) => cells.forEach(([r, c]) => this._cells[r][c].fill.setAttribute("fill", on ? TINT : fills[r][c]));
        const label = texts[col] ? `"${texts[col]}"` : col;
        const here = [col * COL, HEAD + row * ROW, COL, ROW];
        const quip =
          row === 0
            ? (col === 0 ? "loc.stubhead()" : `loc.column_labels(columns=${label})`)
            : (col === 0 ? `loc.stub(rows=${row - 1})` : `loc.body(columns=${label}, rows=${row - 1})`);
        const parts = [
          ["loc.header()", [0, 0, W, HEAD], [0, -1], (on) => this._headFill.setAttribute("fill", on ? TINT : "transparent")],
          ["loc.column_labels()", [0, HEAD, W, ROW], [0, 0.3], tint([0, 1, 2, 3].map((c) => [0, c]))],
          ["loc.stub()", [0, HEAD + ROW, COL, 2 * ROW], [-1, 0.5], tint([[1, 0], [2, 0]])],
          ["loc.body()", [COL, HEAD + ROW, 3 * COL, 2 * ROW], [0.3, 0.7], tint([1, 2].flatMap((r) => [1, 2, 3].map((c) => [r, c])))],
          ["loc.footer()", [-9, BOTTOM + 1, W + 18, FEET - BOTTOM - 1], [0, 1], (on) => this._fillFeet(on ? TINT : "")],
          [quip, here, [(col - 1.5) / 1.5, 0.3 + row * 0.35], tint([[row, col]])],
        ];
        const box = parts[0][1].slice();
        const target = el("rect", { class: "border", rx: 4 }, this._borders);
        const draw = () => {
          const [x, y, w, h] = box;
          [["x", x + 1.7], ["y", y + 1.7], ["width", w - 3.4], ["height", h - 3.4]].forEach(([key, v]) => target.setAttribute(key, v));
        };
        draw();
        this._animate(target, [{ opacity: 0 }, { opacity: 1 }], { duration: 200 });
        for (const [words, to, xy, light] of parts) {
          await this._tween("target", box, to, 380, draw);
          light(true);
          this.look(...xy);
          this._quip(words, 800);
          await sleep(still() ? 1000 : 850);
          light(false);
        }
        target.remove();
        this._holdEyes = false;
        await this.mood("grin");
        await this.hop(1);
        await sleep(still() ? 600 : 250);
      } else if (trick === "extend") {
        // (As with gt-extras' add-ons, the columns of numbers beside the stub change in turn: into
        // star ratings (gt_fa_rating()), bars (gt_plt_bar()) and fills from purple to green
        // (gt_hulk_col_numeric()))
        this.mood("grin");
        const cells = this._cells.flat();
        const colors = cells.map((cell) => cell.text.style.fill);
        const addons = [
          ["gt_fa_rating()", (c, values, max) => values.forEach((v, k) => {
            this._cells[k + 1][c].text.style.opacity = "0";
            const stars = clamp(Math.round(max > 5 ? (v / max) * 5 : v), 0, 5);
            const y = HEAD + (k + 1.5) * ROW;
            for (let s = 0; s < 5; s++) {
              const x = c * COL + 12 + s * 14;
              const points = Array.from({ length: 10 }, (_, p) => {
                const [radius, angle] = [p % 2 ? 2.9 : 6.8, (p * Math.PI) / 5 - Math.PI / 2];
                return `${(x + radius * Math.cos(angle)).toFixed(1)},${(y + 0.6 + radius * Math.sin(angle)).toFixed(1)}`;
              });
              const star = el("polygon", { class: s < stars ? "star on" : "star", points: points.join(" ") }, this._mergeLayer);
              this._animate(star, [{ transform: "scale(0)" }, { transform: "scale(1)" }], { duration: 240, delay: s * 60, easing: "ease-out", fill: "backwards" });
            }
          })],
          ["gt_plt_bar()", (c, values, max) => values.forEach((v, k) => {
            this._cells[k + 1][c].text.style.opacity = "0";
            const width = Math.max(3, ((COL - 16) * Math.max(0, v)) / (max > 0 ? max : 1));
            const bar = el("rect", { class: "bar", x: c * COL + 8, y: HEAD + (k + 1.5) * ROW - 6, width, height: 12 }, this._mergeLayer);
            bar.style.transformOrigin = "left";
            this._animate(bar, [{ transform: "scaleX(0)" }, { transform: "scaleX(1)" }], { duration: 320, easing: "ease-out" });
          })],
          ["gt_hulk_col_numeric()", (c, values) => {
            const [lo, hi] = [Math.min(...values), Math.max(...values)];
            values.forEach((v, k) => {
              const cell = this._cells[k + 1][c];
              const fill = paletteAt(PRGN, hi > lo ? (v - lo) / (hi - lo) : 0.5);
              cell.fill.setAttribute("fill", fill);
              cell.text.style.fill = textOn(fill);
            });
          }],
        ];
        for (const [k, c] of numbered.entries()) {
          const [words, addon] = addons[k % addons.length];
          const values = [1, 2].map((r) => number(texts[r * 4 + c]));
          addon(c, values, Math.max(...values));
          this._quip(words, 900);
          await sleep(still() ? 1100 : 1000);
        }
        this._quip("Add-ons, built on Great Tables!", 1600);
        await this.hop(1);
        await sleep(1500);
        this._unmerge();
        this._setFills(fills);
        cells.forEach((cell, i) => {
          cell.text.style.fill = colors[i];
          this._setText(...at(i), texts[i]);
        });
        await sleep(still() ? 0 : 400);
      } else if (trick === "read") {
        // (As a screen reader does, with the headers that Great Tables marks up: three cells from
        // the cell on are read out with their row's label and their column's, which light up, and
        // with a ring around the cell being read)
        this.mood("happy");
        this._holdEyes = true;
        const data = [5, 6, 7, 9, 10, 11];
        const start = data.indexOf(Math.max(1, row) * 4 + Math.max(1, col));
        const ring = el("rect", { class: "border", rx: 3 }, this._borders);
        for (let k = 0; k < 3; k++) {
          const i = data[(start + k) % data.length];
          const [r, c] = at(i);
          this._setFills(fills);
          [[0, c], [r, 0]].forEach(([hr, hc]) => this._cells[hr][hc].fill.setAttribute("fill", TINT));
          [["x", c * COL + 1.7], ["y", HEAD + r * ROW + 1.7], ["width", COL - 3.4], ["height", ROW - 3.4]].forEach(([key, v]) => ring.setAttribute(key, v));
          this.look((c - 1.5) / 1.5, 0.3 + r * 0.35);
          this._quip([texts[r * 4], texts[c], texts[i]].filter(Boolean).join(", ") || "Blank", 1100);
          await sleep(still() ? 1300 : 1250);
        }
        ring.remove();
        this._setFills(fills);
        this._holdEyes = false;
        await this.mood("grin");
        this._quip("Every cell, with its headers!", 1500);
        await sleep(1600);
      } else if (trick === "sort") {
        // (As with opt_interactive(): the rows under the column labels sort by the cell's column,
        // up and then down, with an arrow by its label, and then a search for the cell's text
        // dims the rows without it)
        this.mood("happy");
        const rows = [1, 2].map((r) => texts.slice(r * 4, r * 4 + 4));
        const key = (cells) => number(cells[col]) ?? cells[col];
        const up = rows.slice().sort((a, b) => {
          const [x, y] = [key(a), key(b)];
          return typeof x === "number" && typeof y === "number" ? x - y : String(x).localeCompare(String(y));
        });
        const down = up.slice().reverse();
        // (Rows that move slide from where they were)
        const show = (order, from) =>
          order.forEach((cells, k) => {
            const was = from.indexOf(cells);
            cells.forEach((t, c) => {
              this._setText(k + 1, c, t, false);
              if (was !== k) {
                this._animate(this._cells[k + 1][c].text, [{ transform: `translateY(${(was - k) * ROW}px)` }, { transform: "translateY(0)" }], { duration: 380 });
              }
            });
          });
        const label = this._cells[0][col].text;
        const arrow = el("tspan", { class: "mark", dx: 2 }, label);
        for (const [order, from, mark, words] of [[up, rows, "▲", "Sorted!"], [down, up, "▼", "And the other way!"]]) {
          arrow.textContent = mark;
          this._fit(label, COL - 10);
          show(order, from);
          this._quip(words, 900);
          await sleep(still() ? 1100 : 1000);
        }
        arrow.remove();
        this._fit(label, COL - 10);
        const term = texts[Math.max(1, row) * 4 + col];
        if (term) {
          down.forEach((cells, k) => {
            if (!cells.some((t) => t.includes(term))) this._cells[k + 1].forEach((cell) => (cell.text.style.opacity = "0.25"));
          });
          this._quip(`Search: “${term}”`, 1200);
          await sleep(1400);
          this._cells.flat().forEach((cell) => (cell.text.style.opacity = ""));
        }
        show(rows, down);
        await this.mood("grin");
        await sleep(still() ? 600 : 500);
      } else if (trick === "export") {
        // (As with a GTI table's i_export("csv"): each row turns into a line of CSV, from the top,
        // and the lines drop into his feet, which light up)
        this.mood("happy");
        const lines = [];
        for (let r = 0; r < 3; r++) {
          const cells = texts.slice(r * 4, r * 4 + 4);
          if (cells.every((t) => t === "")) continue;
          lines.push(this._merge(r, 0, 3, cells.join(",")));
          await sleep(still() ? 0 : 200);
        }
        this._quip('i_export("csv")', 1000);
        await sleep(1100);
        this._holdEyes = true;
        this.look(0, 1);
        for (const line of lines.reverse()) {
          const y = parseFloat(line.getAttribute("y"));
          await this._animate(line, [{ opacity: 1, transform: "translateY(0) scale(1)" }, { opacity: 0, transform: `translateY(${FEET - 20 - y}px) scale(0.3)` }], { duration: 300, easing: "ease-in" });
          line.style.opacity = "0";
        }
        this._fillFeet(TINT);
        this._holdEyes = false;
        await this.mood("grin");
        this._quip("CSV, downloaded!", 1500);
        await this.hop(1);
        await sleep(1400);
        this._fillFeet("");
        this._unmerge();
        this._cells.flat().forEach((cell) => cell.text.textContent && this._pop(cell.text));
        await sleep(still() ? 0 : 300);
      } else if (trick === "select") {
        // (As with a GTI table's selection, which Python can read and set: the cell's row is
        // selected (lit, with a bar at its side), and Python, which he looks over to, reads it,
        // then selects the other row and then none)
        this.mood("happy");
        const mine = Math.max(0, row - 1);
        const select = (picked) => {
          this._setFills(fills);
          this._borders.replaceChildren();
          for (const i of picked) {
            this._cells[i + 1].forEach((cell) => cell.fill.setAttribute("fill", TINT));
            const bar = el("rect", { x: 0, y: HEAD + (i + 1) * ROW, width: 6, height: ROW, fill: "var(--tabblen-accent)" }, this._borders);
            this._animate(bar, [{ opacity: 0 }, { opacity: 1 }], { duration: 200 });
          }
        };
        const steps = [
          ["Selected!", [mine]],
          [`widget.selection == [${mine}]`, [mine]],
          [`widget.selection = [${1 - mine}]`, [1 - mine]],
          ["widget.selection = []", []],
        ];
        for (const [n, [words, picked]] of steps.entries()) {
          select(picked);
          if (n === 1) {
            this._holdEyes = true;
            this.look(-1, 0);
          }
          this._quip(words, 900);
          await sleep(still() ? 1100 : 1000);
        }
        this._setFills(fills);
        this._borders.replaceChildren();
        this._holdEyes = false;
        await this.mood("grin");
        await this.hop(1);
        await sleep(still() ? 600 : 250);
      } else if (trick === "define") {
        // (The cells flip over to the names of his parts, from the cell out, and the cell's part
        // lights up and is defined, as in the glossary, and then his header is too)
        this.mood("happy");
        const part = (r, c) => (r === 0 ? (c === 0 ? "stubhead" : "label") : c === 0 ? "stub" : "cell");
        await this._flipTo(texts.map((_, i) => part(...at(i))), row, col);
        this._cells.flat().forEach((cell, i) => part(...at(i)) === part(row, col) && cell.fill.setAttribute("fill", TINT));
        this._quip(TERMS[part(row, col)], 1700);
        await sleep(1900);
        this._setFills(fills);
        await this.mood("grin");
        this._holdEyes = true;
        this.look(0, -1);
        this._headFill.setAttribute("fill", TINT);
        this._quip("Header: that’s my face!", 1400);
        await sleep(1500);
        this._headFill.setAttribute("fill", "transparent");
        this._holdEyes = false;
        await this._flipTo(texts, row, col, 50);
        await sleep(still() ? 0 : 300);
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

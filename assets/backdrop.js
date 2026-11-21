// The homepage hero's animated backdrop. In light mode, small tables drift by, each now and then
// sorting its rows; in dark mode, a neon table's grid runs to the horizon, its cells lighting up
// as they come, with formatted values rising from it. It's faint behind the logo and tagline,
// paused out of view, and still with reduced motion.
(() => {
  "use strict";

  const hero = document.querySelector(".gd-hero");
  if (!hero) return;
  const canvas = document.createElement("canvas");
  canvas.id = "gth-backdrop";
  canvas.setAttribute("aria-hidden", "true");
  const ctx = canvas.getContext("2d");
  if (!ctx) return;
  hero.prepend(canvas);

  const motion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const root = document.documentElement;
  const isDark = () => root.classList.contains("quarto-dark") || document.body.classList.contains("quarto-dark");

  const rand = (lo, hi) => lo + Math.random() * (hi - lo);
  const pick = (items) => items[(Math.random() * items.length) | 0];
  const clamp = (x, lo, hi) => Math.min(hi, Math.max(lo, x));
  const smooth = (lo, hi, x) => {
    const k = clamp((x - lo) / (hi - lo), 0, 1);
    return k * k * (3 - 2 * k);
  };
  const ease = (k) => (k < 0.5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2);
  const rgba = (c, a) => `rgba(${c[0]},${c[1]},${c[2]},${a})`;
  const mix = (a, b, k) => [0, 1, 2].map((i) => Math.round(a[i] + (b[i] - a[i]) * k));

  // The canvas's size (in CSS pixels); the logo and tagline's box in it, which is kept clear; and
  // the page's text over it (the lead, the calls to action and the sidebar), kept nearly so
  let W = 0;
  let H = 0;
  let dpr = 1;
  const focus = { left: 0, right: 0, top: 0, bottom: 0 };
  let texts = [];
  const TEXTS = ["#quarto-document-content > p:first-of-type", ".gth-cta", "#quarto-margin-sidebar"];

  // How much of a thing to draw at a point: less near the logo and tagline, and over text
  const gap = (r, x, y) => Math.hypot(Math.max(r.left - x, 0, x - r.right), Math.max(r.top - y, 0, y - r.bottom));
  // (`over` is how much over text: less for text, which reads badly over text, than for shapes)
  const clearing = (x, y, over = 0.3) => {
    let k = 0.12 + 0.88 * smooth(0, 120, gap(focus, x, y));
    for (const r of texts) k = Math.min(k, over + (1 - over) * smooth(0, 110, gap(r, x, y)));
    return k;
  };

  function layout() {
    const box = hero.getBoundingClientRect();
    const nav = document.getElementById("quarto-header");
    const navHeight = nav ? nav.offsetHeight : 0;
    const heroTop = box.top + window.scrollY;
    // From under the navbar to below the hero (where it fades out), across the page
    const top = navHeight - heroTop;
    const width = root.clientWidth;
    const height = Math.round(heroTop - navHeight + box.height + Math.min(340, window.innerHeight * 0.4));
    canvas.style.left = `${-box.left}px`;
    canvas.style.top = `${top}px`;
    canvas.style.width = `${width}px`;
    canvas.style.height = `${height}px`;

    // (The logo shown, for the theme, and the tagline)
    const parts = Array.from(hero.querySelectorAll(".gd-hero-logo, .gd-hero-tagline"))
      .map((el) => el.getBoundingClientRect())
      .filter((r) => r.width > 0 && r.height > 0);
    if (parts.length > 0) {
      const left = Math.min(...parts.map((r) => r.left));
      const right = Math.max(...parts.map((r) => r.right));
      focus.left = left;
      focus.right = right;
      focus.top = Math.min(...parts.map((r) => r.top)) - box.top - top;
      focus.bottom = Math.max(...parts.map((r) => r.bottom)) - box.top - top;
    } else {
      focus.left = width * 0.3;
      focus.right = width * 0.7;
      focus.top = height * 0.2;
      focus.bottom = height * 0.6;
    }
    texts = TEXTS.map((selector) => document.querySelector(selector))
      .filter((el) => el !== null)
      .map((el) => el.getBoundingClientRect())
      .filter((r) => r.width > 0 && r.height > 0)
      .map((r) => ({ left: r.left, right: r.right, top: r.top - box.top - top, bottom: r.bottom - box.top - top }));

    const ratio = Math.min(2, window.devicePixelRatio || 1);
    const resized = Math.abs(width - W) > W * 0.1 || Math.abs(height - H) > H * 0.1;
    if (width !== W || height !== H || ratio !== dpr) {
      W = width;
      H = height;
      dpr = ratio;
      canvas.width = Math.round(W * dpr);
      canvas.height = Math.round(H * dpr);
    }
    return resized;
  }

  /* ── Light: small tables, drifting by and sorting their rows ─────────────────────────────── */

  // The colors of a table's colored column (as `data_color()` would color it), pale to strong
  const RAMPS = [
    [[255, 240, 250], [249, 0, 195]],
    [[243, 238, 255], [124, 77, 255]],
    [[228, 249, 252], [0, 166, 204]],
  ];
  // Flags (as `fmt_flag()` shows them): two or three stripes, across or down
  const FLAGS = [
    [[0, 85, 164], [255, 255, 255], [239, 65, 53], 0],
    [[0, 0, 0], [221, 0, 0], [255, 206, 0], 1],
    [[255, 153, 51], [255, 255, 255], [19, 136, 8], 1],
    [[0, 146, 70], [255, 255, 255], [206, 43, 55], 0],
    [[255, 255, 255], [188, 0, 45], [255, 255, 255], 1],
    [[0, 106, 167], [254, 204, 0], [0, 106, 167], 1],
  ];
  const INK = [40, 30, 45];
  const LINE = [70, 130, 180];
  const CARD_W = 190;
  const ROW_H = 15;
  const HEAD_H = 54;
  const SORT_TIME = 1.1;

  let cards = [];

  function makeCard(x, y, t) {
    const z = rand(0.55, 1);
    const rows = 4 + ((Math.random() * 3) | 0);
    const card = {
      x,
      y,
      z,
      rot: rand(-0.14, 0.14),
      spin: rand(-0.006, 0.006),
      vx: rand(5, 11),
      vy: rand(-7, -2.5),
      ramp: pick(RAMPS),
      flags: Math.random() < 0.55,
      lines: Math.random() < 0.65,
      by: "heat",
      desc: Math.random() < 0.5,
      sortStart: -10,
      sortAt: t + rand(1.5, 9),
      rows: [],
    };
    for (let k = 0; k < rows; k++) {
      let level = Math.random();
      const line = [];
      for (let i = 0; i < 7; i++) {
        level = clamp(level + rand(-0.3, 0.32), 0, 1);
        line.push(level);
      }
      card.rows.push({ label: rand(0.4, 1), num: Math.random(), heat: Math.random(), flag: pick(FLAGS), line, slot: k, from: k });
    }
    return card;
  }

  function initLight(t) {
    // (One table to each cell of a grid over the canvas, somewhere in it)
    const scale = clamp(W / 1400, 0.75, 1.1);
    const across = Math.max(2, Math.round(W / (380 * scale)));
    const down = Math.max(2, Math.round(H / (280 * scale)));
    cards = [];
    for (let i = 0; i < across; i++) {
      for (let j = 0; j < down; j++) {
        cards.push(makeCard(((i + rand(0.15, 0.85)) * W) / across, ((j + rand(0.15, 0.85)) * H) / down, t));
      }
    }
    for (const card of cards) card.z *= scale;
    cards.sort((a, b) => a.z - b.z);
  }

  function sortCard(card, t) {
    card.by = Math.random() < 0.65 ? "heat" : "num";
    card.desc = !card.desc;
    const order = card.rows.slice().sort((a, b) => (card.desc ? b[card.by] - a[card.by] : a[card.by] - b[card.by]));
    order.forEach((row, k) => {
      row.from = row.slot;
      row.slot = k;
    });
    card.sortStart = t;
    card.sortAt = t + rand(5, 11);
  }

  function bar(x, y, w, h, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.roundRect(x, y, Math.max(h, w), h, h / 2);
    ctx.fill();
  }

  function drawCard(card, t, alpha) {
    const height = HEAD_H + card.rows.length * ROW_H + 18;
    const w = CARD_W;
    const moving = clamp((t - card.sortStart) / SORT_TIME, 0, 1);
    const [pale, strong] = card.ramp;
    const x0 = card.flags ? 30 : 14;
    const heatX = 118;
    const numRight = 110;

    ctx.save();
    ctx.translate(card.x, card.y);
    ctx.rotate(card.rot);
    ctx.scale(card.z, card.z);
    ctx.translate(-w / 2, -height / 2);
    ctx.globalAlpha = alpha;

    // The table, on a card with a soft shadow
    ctx.shadowColor = "rgba(150, 0, 110, 0.12)";
    ctx.shadowBlur = 22;
    ctx.shadowOffsetY = 6;
    ctx.fillStyle = "rgba(255, 255, 255, 0.94)";
    ctx.beginPath();
    ctx.roundRect(0, 0, w, height, 9);
    ctx.fill();
    ctx.shadowColor = "transparent";

    // Its title and subtitle, the rule under them, the column labels and the rule under those
    bar(14, 12, w * 0.55, 5, rgba(INK, 0.45));
    bar(14, 22, w * 0.34, 3.5, rgba(INK, 0.28));
    ctx.fillStyle = rgba(INK, 0.2);
    ctx.fillRect(10, 33, w - 20, 1.6);
    bar(x0, 41, 34, 3.5, rgba(INK, 0.32));
    bar(numRight - 20, 41, 20, 3.5, rgba(INK, card.by === "num" ? 0.55 : 0.32));
    bar(heatX + 2, 41, 18, 3.5, rgba(strong, card.by === "heat" ? 0.75 : 0.4));
    if (card.lines) bar(150, 41, 26, 3.5, rgba(INK, 0.32));
    // (The sorted column's arrow)
    const arrowX = card.by === "heat" ? heatX + 24 : numRight + 3;
    ctx.fillStyle = rgba(strong, 0.9);
    ctx.beginPath();
    if (card.desc) {
      ctx.moveTo(arrowX, 40.5);
      ctx.lineTo(arrowX + 5, 40.5);
      ctx.lineTo(arrowX + 2.5, 44.5);
    } else {
      ctx.moveTo(arrowX, 44.5);
      ctx.lineTo(arrowX + 5, 44.5);
      ctx.lineTo(arrowX + 2.5, 40.5);
    }
    ctx.fill();
    ctx.fillStyle = rgba(INK, 0.14);
    ctx.fillRect(10, 50, w - 20, 1);

    // The rows, where they are (sliding to their places as the table's sorted)
    for (const row of card.rows) {
      const at = row.from + (row.slot - row.from) * ease(moving);
      const y = HEAD_H + at * ROW_H;
      if (moving < 1 && row.from !== row.slot) {
        ctx.fillStyle = rgba(pale, 0.9);
        ctx.fillRect(10, y, w - 20, ROW_H);
      }
      if (card.flags) {
        const [a, b, c, down] = row.flag;
        ctx.save();
        ctx.beginPath();
        ctx.arc(20, y + ROW_H / 2, 4.5, 0, Math.PI * 2);
        ctx.clip();
        [a, b, c].forEach((color, k) => {
          ctx.fillStyle = rgba(color, 1);
          if (down) ctx.fillRect(15.5 + k * 3, y + 3, 3.05, 9);
          else ctx.fillRect(15.5, y + 3 + k * 3, 9, 3.05);
        });
        ctx.restore();
        ctx.strokeStyle = rgba(INK, 0.15);
        ctx.lineWidth = 0.6;
        ctx.beginPath();
        ctx.arc(20, y + ROW_H / 2, 4.5, 0, Math.PI * 2);
        ctx.stroke();
      }
      bar(x0, y + 5.5, (numRight - 30 - x0) * row.label, 4, rgba(INK, 0.36));
      const numW = 6 + row.num * 18;
      bar(numRight - numW, y + 5.5, numW, 4, rgba(INK, 0.3));
      ctx.fillStyle = rgba(mix(pale, strong, row.heat), 0.92);
      ctx.fillRect(heatX, y + 1, 30, ROW_H - 2);
      if (card.lines) {
        ctx.strokeStyle = rgba(LINE, 0.75);
        ctx.lineWidth = 1.2;
        ctx.lineJoin = "round";
        ctx.beginPath();
        row.line.forEach((v, i) => {
          const px = 152 + i * 4.3;
          const py = y + ROW_H - 3 - v * (ROW_H - 6);
          if (i === 0) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        });
        ctx.stroke();
      }
      ctx.fillStyle = rgba(INK, 0.06);
      ctx.fillRect(10, y + ROW_H - 0.5, w - 20, 0.8);
    }

    // The rule under the rows, and a source note
    const foot = HEAD_H + card.rows.length * ROW_H + 2;
    ctx.fillStyle = rgba(INK, 0.2);
    ctx.fillRect(10, foot, w - 20, 1.6);
    bar(14, foot + 7, w * 0.3, 3, rgba(INK, 0.2));
    ctx.restore();
  }

  // A soft wash of color behind the tables
  const WASH = [
    [249, 0, 195, 0.1, 0.18, 0.3],
    [124, 77, 255, 0.08, 0.82, 0.25],
    [0, 166, 204, 0.07, 0.6, 0.85],
  ];

  function drawLight(t, dt) {
    WASH.forEach(([r, g, b, a, fx, fy], k) => {
      const x = W * (fx + 0.05 * Math.sin(t * 0.07 + k * 2));
      const y = H * (fy + 0.06 * Math.cos(t * 0.06 + k));
      const radius = Math.max(W, H) * 0.42;
      const glow = ctx.createRadialGradient(x, y, 0, x, y, radius);
      glow.addColorStop(0, `rgba(${r},${g},${b},${a})`);
      glow.addColorStop(1, `rgba(${r},${g},${b},0)`);
      ctx.fillStyle = glow;
      ctx.fillRect(0, 0, W, H);
    });

    for (const card of cards) {
      card.x += card.vx * card.z * dt;
      card.y += card.vy * card.z * dt;
      card.rot += card.spin * dt;
      const margin = 160 * card.z;
      if (card.x > W + margin) card.x = -margin;
      if (card.y < -margin) card.y = H + margin;
      if (t >= card.sortAt) sortCard(card, t);
      const depth = 0.35 + 0.35 * clamp((card.z - 0.5) / 0.6, 0, 1);
      drawCard(card, t, depth * clearing(card.x, card.y));
    }
  }

  /* ── Dark: a neon table's grid, to the horizon ────────────────────────────────────────────── */

  const NEON = [
    [249, 0, 195],
    [168, 85, 247],
    [34, 211, 238],
    [255, 110, 199],
  ];
  // Values as Great Tables formats them
  const VALUES = [
    "1.4B", "+218%", "€1.234,50", "45.7%", "⅞", "MMXXVI", "1.5 GB", "6.02 × 10²³", "1h 2m 5s",
    "Sat, Nov 21, 2026", "m s⁻²", "C₆H₁₂O₆", "✓", "★", "−3.2%", "$12.5K", "0.875", "2,418,000,000",
    "21 nov. 2026", "12:45 PM", "▲ 12", "1,851", "3.14159", "¥1,234", "1.2 × 10⁻⁹",
  ];
  const CELL_W = 170;
  const ROW_D = 0.35;
  const FAR = 26;
  const SPEED = ROW_D / 1.6;

  let lit = [];
  let rising = [];
  let nextLit = 0;
  let nextRow = 0;
  let nextValue = 0;

  // The floor, in perspective: a point `x` across (in pixels at depth 1) and `z` deep
  const font = (size) => `600 ${size}px ui-monospace, SFMono-Regular, Menlo, monospace`;
  const horizon = () => clamp(focus.bottom + 18, H * 0.25, H * 0.7);
  const depthScale = () => H - horizon();
  const project = (x, z) => [W / 2 + x / z, horizon() + depthScale() / z];

  function litCell(u, near) {
    const z = near ? rand(1, FAR * 0.8) : rand(FAR * 0.55, FAR);
    const row = Math.ceil((u + z) / ROW_D);
    const reach = (W / 2) * (z / 1);
    const col = Math.floor(rand(-reach, reach) / CELL_W);
    return { row, col, color: pick(NEON), born: near ? rand(-4, 0) : 0, span: 1 };
  }

  function risingValue(t, settled) {
    const life = rand(7, 12);
    const born = settled ? t - rand(0, life) : t;
    const vy = rand(9, 16);
    const text = pick(VALUES);
    const size = rand(12, 17);
    ctx.font = font(size);
    const half = Math.min(W / 2 - 1, ctx.measureText(text).width / 2 + 12);
    // (In the canvas, and away from the values near it, of the few places tried)
    let x = 0;
    let room = -1;
    for (let k = 0; k < 6; k++) {
      const at = rand(half, W - half);
      const y = horizon() - (t - born) * vy;
      const gap = Math.min(
        Infinity,
        ...rising.map((value) => Math.hypot((at - value.x) / 3, y - (value.y - (t - value.born) * value.vy))),
      );
      if (gap > room) {
        room = gap;
        x = at;
      }
    }
    return {
      text,
      half,
      x,
      y: horizon() - 4,
      vy,
      sway: rand(0, Math.PI * 2),
      born,
      life,
      size,
      color: pick(NEON),
    };
  }

  function initDark(t) {
    const u = t * SPEED;
    lit = [];
    for (let k = 0; k < 26; k++) {
      const cell = litCell(u, true);
      cell.born = t - rand(0, 4);
      lit.push(cell);
    }
    rising = [];
    for (let k = 0; k < Math.round(W / 90); k++) rising.push(risingValue(t, true));
    nextLit = t;
    nextRow = t + 2;
    nextValue = t;
  }

  function drawDark(t) {
    const u = t * SPEED;
    const hy = horizon();
    const D = depthScale();

    // The sky's glow, over the horizon
    const glow = ctx.createRadialGradient(W / 2, hy, 0, W / 2, hy, Math.max(W * 0.55, 420));
    glow.addColorStop(0, "rgba(249, 0, 195, 0.22)");
    glow.addColorStop(0.45, "rgba(124, 58, 237, 0.10)");
    glow.addColorStop(1, "rgba(124, 58, 237, 0)");
    ctx.fillStyle = glow;
    ctx.fillRect(0, 0, W, H);

    // The cells lit (from far to near), as they come
    if (t >= nextLit) {
      lit.push(litCell(u, false));
      nextLit = t + rand(0.15, 0.45);
    }
    if (t >= nextRow) {
      // (A whole row, as one is when it's hovered)
      const cell = litCell(u, false);
      cell.col = Math.floor(-(W / 2) * (FAR / CELL_W));
      cell.span = -2 * cell.col;
      cell.color = NEON[0];
      lit.push(cell);
      nextRow = t + rand(3.5, 6);
    }
    ctx.globalCompositeOperation = "lighter";
    lit = lit.filter((cell) => cell.row * ROW_D - u > 0.7);
    for (const cell of lit) {
      const z0 = cell.row * ROW_D - u;
      const z1 = z0 + ROW_D;
      if (z0 > FAR) continue;
      const x0 = cell.col * CELL_W;
      const x1 = x0 + cell.span * CELL_W;
      const [ax, ay] = project(x0, z0);
      const [bx] = project(x1, z0);
      const [cx, cy] = project(x1, z1);
      const [dx] = project(x0, z1);
      const fadeIn = clamp((t - cell.born) / 1.2, 0, 1);
      const near = 1 - z0 / FAR;
      const pulse = 0.75 + 0.25 * Math.sin((t - cell.born) * 2.2);
      const alpha = (cell.span > 1 ? 0.2 : 0.5) * fadeIn * near * pulse * clearing((ax + bx) / 2, ay);
      ctx.fillStyle = rgba(cell.color, alpha);
      ctx.beginPath();
      ctx.moveTo(ax, ay);
      ctx.lineTo(bx, ay);
      ctx.lineTo(cx, cy);
      ctx.lineTo(dx, cy);
      ctx.closePath();
      ctx.fill();
    }
    ctx.globalCompositeOperation = "source-over";

    // The grid: the rows' rules, nearer ones brighter, and the columns', running to the horizon
    const first = Math.ceil((u + 0.6) / ROW_D);
    for (let row = first; row * ROW_D - u < FAR; row++) {
      const z = row * ROW_D - u;
      const y = hy + D / z;
      const near = 1 - z / FAR;
      ctx.fillStyle = `rgba(249, 0, 195, ${0.05 + 0.4 * near * near})`;
      ctx.fillRect(0, y, W, near > 0.6 ? 1.4 : 1);
    }
    const columns = Math.ceil(((W / 2) * 7) / CELL_W);
    const fan = ctx.createLinearGradient(0, hy, 0, H);
    fan.addColorStop(0, "rgba(168, 85, 247, 0)");
    fan.addColorStop(0.35, "rgba(168, 85, 247, 0.22)");
    fan.addColorStop(1, "rgba(249, 0, 195, 0.42)");
    ctx.strokeStyle = fan;
    ctx.lineWidth = 1;
    ctx.beginPath();
    for (let col = -columns; col <= columns; col++) {
      const [fx, fy] = project(col * CELL_W, FAR);
      const [nx, ny] = project(col * CELL_W, 0.6);
      ctx.moveTo(fx, fy);
      ctx.lineTo(nx, ny);
    }
    ctx.stroke();

    // The horizon, glowing
    const line = ctx.createLinearGradient(0, 0, W, 0);
    line.addColorStop(0, "rgba(249, 0, 195, 0)");
    line.addColorStop(0.5, "rgba(255, 120, 220, 0.85)");
    line.addColorStop(1, "rgba(249, 0, 195, 0)");
    ctx.fillStyle = line;
    ctx.fillRect(0, hy - 0.75, W, 1.5);

    // The values, rising from the horizon
    if (t >= nextValue) {
      rising.push(risingValue(t, false));
      nextValue = t + rand(0.7, 1.3);
    }
    rising = rising.filter((value) => t - value.born < value.life);
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    for (const value of rising) {
      const age = t - value.born;
      const y = value.y - age * value.vy;
      const x = value.x + Math.sin(age * 0.6 + value.sway) * 6;
      const k = age / value.life;
      const room = Math.min(clearing(x - value.half, y, 0.04), clearing(x, y, 0.04), clearing(x + value.half, y, 0.04));
      const alpha = 0.75 * smooth(0, 0.15, k) * (1 - smooth(0.6, 1, k)) * room;
      if (alpha <= 0.01 || y < -20) continue;
      ctx.font = font(value.size);
      ctx.fillStyle = rgba(mix(value.color, [255, 255, 255], 0.35), alpha);
      ctx.fillText(value.text, x, y);
    }
  }

  /* ── Running it ────────────────────────────────────────────────────────────────────────────── */

  let t = 0;
  let last = 0;
  let frame = 0;
  let inView = true;
  let ready = false;

  function draw(dt) {
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    if (isDark()) drawDark(t);
    else drawLight(t, dt);
  }

  const running = () => inView && !motion.matches && !document.hidden;

  function tick(now) {
    frame = 0;
    const dt = last ? Math.min(0.05, (now - last) / 1000) : 0;
    last = now;
    t += dt;
    draw(dt);
    if (running()) frame = requestAnimationFrame(tick);
  }

  function start() {
    if (!ready) return;
    if (running()) {
      if (frame === 0) {
        last = 0;
        frame = requestAnimationFrame(tick);
      }
    } else {
      // (Still: one frame, as it is)
      if (frame !== 0) cancelAnimationFrame(frame);
      frame = 0;
      draw(0);
    }
  }

  let pending = 0;
  function refit() {
    cancelAnimationFrame(pending);
    pending = requestAnimationFrame(() => {
      if (layout() || !ready) {
        initLight(t);
        initDark(t);
      }
      ready = true;
      canvas.classList.add("gth-on");
      start();
    });
  }

  // (Started a little way into its life, so that it's under way)
  t = 20;
  refit();
  if ("ResizeObserver" in window) new ResizeObserver(refit).observe(hero);
  window.addEventListener("resize", refit);
  motion.addEventListener("change", start);
  document.addEventListener("visibilitychange", start);
  if ("IntersectionObserver" in window) {
    new IntersectionObserver((entries) => {
      inView = entries[entries.length - 1].isIntersecting;
      start();
    }).observe(canvas);
  }
  // (A theme's toggle: redrawn at once, if it's still)
  new MutationObserver(() => {
    if (!running()) draw(0);
  }).observe(root, { attributes: true, attributeFilter: ["class", "data-bs-theme"] });
})();

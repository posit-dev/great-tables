// Time GTI tables in Chromium: when its page is first painted, how long the table takes to be ready
// once its page is parsed, the longest task until then (the time the page can't respond), how much
// memory it holds, and how long a sort, a search, a filter and a change of page take, until the
// next frame is drawn. On a desktop and on a mid-range phone (a phone's viewport and touch,
// its CPU slowed four times, as Lighthouse's mobile runs are). The pages come from
// bench/make_pages.py; the results go to bench/results/ (results.json, and results.md, also
// printed). They're run by hand, not in CI: a shared runner's times vary too much to compare.
// bench/results/baseline.md, kept in git, is a full run to compare a change against.
//
//   node bench/run.mjs [--quick] [--reps N] [--only TEXT] [--device desktop|phone]
//
// --quick: fewer tables; --reps: times each thing is timed (the median is kept; 5 by default);
// --only: just the pages whose name has TEXT (e.g. "docs", for the pages like the docs' dataset
// previews); --device: just the one.

import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { parseArgs } from "node:util";
import { chromium, devices } from "@playwright/test";

const here = dirname(fileURLToPath(import.meta.url));
const pagesDir = join(here, ".pages");
const resultsDir = join(here, "results");

const { values: args } = parseArgs({
  options: {
    quick: { type: "boolean", default: false },
    reps: { type: "string", default: "5" },
    only: { type: "string" },
    device: { type: "string" },
  },
});
const reps = Number(args.reps);

const DEVICES = {
  desktop: { context: { ...devices["Desktop Chrome"] }, slowdown: 1 },
  phone: { context: { ...devices["Pixel 7"] }, slowdown: 4 },
};

// $PYTHON if set, else the repo's .venv, else python3 on PATH (as the e2e tests find it)
function python() {
  if (process.env.PYTHON) {
    return process.env.PYTHON;
  }
  const venv = join(here, "..", "..", "..", ".venv", "bin", "python");
  return existsSync(venv) ? venv : "python3";
}

const made = spawnSync(python(), [join(here, "make_pages.py"), ...(args.quick ? ["--quick"] : [])], {
  stdio: "inherit",
});
if (made.error !== undefined || made.status !== 0) {
  throw new Error(`Couldn't write the pages with ${python()} (set $PYTHON to a Python with great_tables installed)`);
}
const pages = JSON.parse(readFileSync(join(pagesDir, "pages.json"), "utf8")).filter(
  (page) => args.only === undefined || page.name.includes(args.only),
);

// Before the page's own scripts: note when the table is ready, when the next frame is drawn, and the
// longest task (a task of 50 ms or more, as Chromium reports them)
function watchReady() {
  const bench = { ready: null, drawn: null, longest: 0 };
  window.__bench = bench;
  const note = (entries) => {
    for (const entry of entries) {
      bench.longest = Math.max(bench.longest, entry.duration);
    }
  };
  const tasks = new PerformanceObserver((list) => note(list.getEntries()));
  tasks.observe({ type: "longtask", buffered: true });
  // (The tasks ended but not yet passed to the observer, too)
  bench.flush = () => note(tasks.takeRecords());
  new MutationObserver(() => {
    if (bench.ready === null && document.querySelector('gt-table[data-gti-state="ready"]') !== null) {
      bench.ready = performance.now();
      requestAnimationFrame(() => setTimeout(() => (bench.drawn = performance.now())));
    }
  }).observe(document, { subtree: true, attributes: true, attributeFilter: ["data-gti-state"] });
}

async function open(browser, device, page) {
  const context = await browser.newContext(device.context);
  const tab = await context.newPage();
  const cdp = await context.newCDPSession(tab);
  if (device.slowdown > 1) {
    await cdp.send("Emulation.setCPUThrottlingRate", { rate: device.slowdown });
  }
  await tab.addInitScript(watchReady);
  await tab.goto(pathToFileURL(join(pagesDir, page.name)).href, { timeout: 300_000 });
  const painted = () => performance.getEntriesByName("first-contentful-paint").length > 0;
  await tab.waitForFunction(`window.__bench.drawn !== null && (${painted})()`, null, { timeout: 300_000 });
  const times = await tab.evaluate(() => {
    const [nav] = performance.getEntriesByType("navigation");
    const [paint] = performance.getEntriesByName("first-contentful-paint");
    const bench = window.__bench;
    bench.flush();
    return { parsed: nav.domInteractive, painted: paint.startTime, ready: bench.ready, drawn: bench.drawn, longest: bench.longest };
  });
  return { context, tab, cdp, times };
}

// The things timed on a table, each a change and the change back (both timed): set on the
// <gt-table>, as a reader's click or typing sets them. The columns sorted and the text searched for
// are the page's (`actions` in pages.json) or the made-up tables'; the filters are only on those
const ACTIONS = [
  {
    name: "sort (number)",
    to: (el, p) => (el.sort = [{ column: p.number }]),
    back: (el, p) => (el.sort = [{ column: p.number, descending: true }]),
  },
  { name: "sort (text)", to: (el, p) => (el.sort = [{ column: p.text }]), back: (el) => (el.sort = []) },
  { name: "search", to: (el, p) => (el.search = p.search), back: (el) => (el.search = "") },
  {
    name: "filter (facet)",
    madeUp: true,
    to: (el) => (el.filter = { and: [{ col: "group", op: "in", value: ["alpha", "bravo"] }] }),
    back: (el) => (el.filter = null),
  },
  {
    name: "filter (range)",
    madeUp: true,
    to: (el) => (el.filter = { and: [{ col: "value", op: "gte", value: 1000 }] }),
    back: (el) => (el.filter = null),
  },
  { name: "page", paged: true, to: (el) => (el.page = 2), back: (el) => (el.page = 1) },
];
const MADE_UP = { number: "value", text: "name", search: "delta" };

// How long a change takes: to run (the runtime's work), and until the next frame is drawn
async function time(tab, change, params) {
  return tab.evaluate(async ([source, p]) => {
    const el = document.querySelector("gt-table");
    const run = new Function("el", "p", `return (${source})(el, p)`);
    const start = performance.now();
    run(el, p);
    const ran = performance.now();
    await new Promise((resolve) => requestAnimationFrame(() => setTimeout(resolve)));
    return { ran: ran - start, drawn: performance.now() - start };
  }, [change.toString(), params]);
}

const median = (values) => {
  const sorted = [...values].sort((a, b) => a - b);
  const mid = Math.floor(sorted.length / 2);
  return sorted.length % 2 === 1 ? sorted[mid] : (sorted[mid - 1] + sorted[mid]) / 2;
};

async function bench(browser, deviceName, page) {
  const device = DEVICES[deviceName];
  const loads = [];
  let last = null;
  for (let rep = 0; rep < reps; rep++) {
    await last?.context.close();
    last = await open(browser, device, page);
    loads.push(last.times);
  }
  const { context, tab, cdp } = last;

  await cdp.send("HeapProfiler.collectGarbage");
  await cdp.send("Performance.enable");
  const { metrics } = await cdp.send("Performance.getMetrics");
  const metric = (name) => metrics.find((m) => m.name === name)?.value ?? null;

  const actions = {};
  for (const action of ACTIONS) {
    if ((action.paged === true && !page.paged) || (action.madeUp === true && page.actions !== undefined)) {
      continue;
    }
    const params = page.actions ?? MADE_UP;
    const samples = [];
    for (let rep = 0; rep < reps; rep++) {
      samples.push(await time(tab, action.to, params), await time(tab, action.back, params));
    }
    actions[action.name] = {
      ran: median(samples.map((s) => s.ran)),
      drawn: median(samples.map((s) => s.drawn)),
      samples,
    };
  }
  await context.close();

  return {
    ...page,
    device: deviceName,
    parsed: median(loads.map((l) => l.parsed)),
    painted: median(loads.map((l) => l.painted)),
    // (Once parsed: the runtime hydrates the table when the page has been)
    ready: median(loads.map((l) => l.ready - l.parsed)),
    drawn: median(loads.map((l) => l.drawn - l.parsed)),
    longest: median(loads.map((l) => l.longest)),
    loads,
    heap: metric("JSHeapUsedSize"),
    nodes: metric("Nodes"),
    actions,
  };
}

const ms = (value) => (value >= 100 ? value.toFixed(0) : value.toFixed(1));
const kb = (bytes) => `${Math.round(bytes / 1024).toLocaleString("en")}`;

function markdown(results) {
  const names = ACTIONS.map((a) => a.name);
  const lines = [
    "## GTI benchmarks",
    "",
    `Chromium ${results.browser}, ${results.reps} runs each (medians). Times in ms: "parsed" and`,
    '"painted" are when the page was parsed and first painted (from its start), "ready" and "drawn"',
    'how long after it was parsed the table was hydrated and then drawn, and "longest" the longest',
    "task until then (0 if none took 50 ms); for each action, until the next frame is drawn (the",
    "runtime's part in brackets). The docs tables are like the docs' dataset previews.",
  ];
  for (const deviceName of Object.keys(DEVICES)) {
    const rows = results.runs.filter((r) => r.device === deviceName);
    if (rows.length === 0) {
      continue;
    }
    lines.push(
      "",
      `### ${deviceName === "phone" ? "Phone (Pixel 7, CPU slowed 4×)" : "Desktop"}`,
      "",
      `| table | rows | KB | KB gzipped | parsed | painted | ready | drawn | longest | heap MB | DOM nodes | ${names.join(" | ")} |`,
      `|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|${names.map(() => "--:").join("|")}|`,
    );
    for (const r of rows) {
      const cells = names.map((name) => {
        const a = r.actions[name];
        return a === undefined ? "" : `${ms(a.drawn)} (${ms(a.ran)})`;
      });
      const table = r.kind === "docs" ? `docs: ${r.label}` : `${r.kind}, ${r.paged ? "paged" : "one page"}`;
      lines.push(
        `| ${table} | ${r.rows.toLocaleString("en")} | ${kb(r.bytes)} | ${kb(r.gzip)} | ` +
          `${ms(r.parsed)} | ${ms(r.painted)} | ${ms(r.ready)} | ${ms(r.drawn)} | ${ms(r.longest)} | ${(r.heap / 2 ** 20).toFixed(1)} | ` +
          `${r.nodes.toLocaleString("en")} | ${cells.join(" | ")} |`,
      );
    }
  }
  return `${lines.join("\n")}\n`;
}

// (After each table, so a run stopped part of the way keeps the rest)
function save(results) {
  mkdirSync(resultsDir, { recursive: true });
  writeFileSync(join(resultsDir, "results.json"), `${JSON.stringify(results, null, 1)}\n`);
  const report = markdown(results);
  writeFileSync(join(resultsDir, "results.md"), report);
  return report;
}

const browser = await chromium.launch();
const results = { browser: browser.version(), reps, quick: args.quick, runs: [] };
for (const deviceName of Object.keys(DEVICES)) {
  if (args.device !== undefined && args.device !== deviceName) {
    continue;
  }
  for (const page of pages) {
    process.stderr.write(`${deviceName}: ${page.name}\n`);
    results.runs.push(await bench(browser, deviceName, page));
    save(results);
  }
}
await browser.close();

process.stdout.write(save(results));

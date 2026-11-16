// Use the interactive table on a page as a reader would, screenshotting each step, for
// `make_readme_gti_demo.py` (which runs this):
//
//     node scripts/readme_gti_demo.mjs PAGE OUT_DIR WIDTH HEIGHT
//
// Writes `frame_NNN.png` for each frame to OUT_DIR, and `frames.json`: each frame's file and how
// long it's shown, in milliseconds. Playwright comes from `packages/gti`'s dev dependencies.

import { readFileSync, writeFileSync } from "node:fs";
import { createRequire } from "node:module";
import { join } from "node:path";
import { pathToFileURL } from "node:url";

const require = createRequire(new URL("../packages/gti/package.json", import.meta.url));
const { chromium } = require("@playwright/test");

const [pagePath, outDir, width, height] = process.argv.slice(2);

// How many frames a glide of the cursor takes, and how long each is shown
const GLIDE_STEPS = 9;
const GLIDE_MS = 35;

const browser = await chromium.launch();
const page = await browser.newPage({
  viewport: { width: Number(width), height: Number(height) },
  deviceScaleFactor: 2,
});
await page.goto(pathToFileURL(pagePath).href);
await page.waitForSelector("gt-table[data-gti-state=ready]");
// (No caret blinking in the search box between frames)
await page.addStyleTag({ content: "* { caret-color: transparent !important; }" });

const frames = [];
const START = { x: 640, y: 560 };
let cursor = START;

async function shot(ms) {
  const file = `frame_${String(frames.length).padStart(3, "0")}.png`;
  await page.screenshot({ path: join(outDir, file) });
  frames.push({ file, ms });
}

// (The mouse goes with the drawn cursor, for what it hovers over)
async function placeCursor({ x, y }) {
  cursor = { x, y };
  await page.mouse.move(x, y);
  await page.evaluate(({ x, y }) => {
    document.getElementById("cursor").style.transform = `translate(${x - 2}px, ${y - 2}px)`;
  }, cursor);
}

async function caption(title, method) {
  await page.evaluate(
    ([title, method]) => {
      const el = document.getElementById("caption");
      el.textContent = title;
      if (method) {
        const code = document.createElement("code");
        code.textContent = method;
        el.append(code);
      }
    },
    [title, method],
  );
}

// Glide the cursor to a point (or the middle of an element), easing in and out
async function glideTo(target) {
  const box = "boundingBox" in target ? await target.boundingBox() : null;
  const to = box ? { x: box.x + box.width / 2, y: box.y + box.height / 2 } : target;
  const from = cursor;
  for (let i = 1; i <= GLIDE_STEPS; i++) {
    const t = i / GLIDE_STEPS;
    const ease = t < 0.5 ? 2 * t * t : 1 - (-2 * t + 2) ** 2 / 2;
    await placeCursor({ x: from.x + (to.x - from.x) * ease, y: from.y + (to.y - from.y) * ease });
    await shot(GLIDE_MS);
  }
}

async function click(locator, ms) {
  await glideTo(locator);
  await locator.click();
  await page.waitForTimeout(250);
  await shot(ms);
}

const table = page.locator("gt-table");
const bar = table.locator(".gt-i-bar");

await placeCursor(cursor);
await caption("An interactive table", "GTI()");
await shot(1600);

await caption("Sort by any column", "i_sorting()");
const sortHp = table.getByRole("button", { name: "Sort by HP" });
await click(sortHp, 500);
await click(sortHp, 1600);

await caption("Filter a column by its values", "i_cols_filter()");
await click(table.getByRole("button", { name: "Filter Body" }), 700);
await click(page.getByRole("checkbox", { name: /^Convertible/ }), 1400);
// (Closing the filter with a click outside it, as a reader with a mouse would)
await glideTo(START);
await page.mouse.click(START.x, START.y);
await page.waitForTimeout(250);
await shot(900);

await caption("Search the table", "i_search()");
await click(bar.getByRole("button", { name: "Search the table" }), 300);
for (const letter of "Ferrari") {
  await page.keyboard.type(letter);
  await page.waitForTimeout(120);
  await shot(110);
}
await page.waitForTimeout(400);
await shot(1500);

await caption("Download the rows as CSV", "i_export()");
await click(bar.getByRole("button", { name: "Export the table", exact: true }), 900);
const downloadCsv = bar
  .getByRole("group", { name: "Export", exact: true })
  .getByRole("button", { name: "Download CSV" });
await glideTo(downloadCsv);
const [download] = await Promise.all([page.waitForEvent("download"), downloadCsv.click()]);
const csv = readFileSync(await download.path(), "utf8").replace(/^\uFEFF/, "");
await page.waitForTimeout(250);
await shot(500);
// (A download doesn't show in a screenshot, so the file is shown in a card over the empty rows)
await page.evaluate(
  ([name, csv]) => {
    const card = document.createElement("div");
    card.id = "download";
    const title = document.createElement("div");
    title.className = "name";
    title.textContent = `⤓ ${name}`;
    const body = document.createElement("pre");
    body.textContent = csv.trim();
    card.append(title, body);
    document.body.append(card);
  },
  [download.suggestedFilename(), csv],
);
await shot(2600);
await page.evaluate(() => document.getElementById("download").remove());

await caption("Edit the filters as text", "i_view()");
await click(bar.getByRole("button", { name: "Edit the filters as text" }), 2600);

await caption("Then reset it");
await click(bar.getByRole("button", { name: "Reset the view" }), 1000);
// (Back to where it started, for the loop)
await glideTo(START);
await shot(300);

writeFileSync(join(outDir, "frames.json"), JSON.stringify(frames, null, 1));
await browser.close();

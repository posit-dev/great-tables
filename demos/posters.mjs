// Make the posters the docs show for the live app demos, until a reader runs one:
//
//   python demos/build.py && node demos/posters.mjs
//
// Each app in `_demos/` is run in Chromium (with Playwright, from packages/gti), with two cars
// selected, and its page saved as `assets/demos/<venue>.webp`. Then what it downloaded is printed,
// for the size the docs give.

import { createReadStream, existsSync, readFileSync, writeFileSync } from "node:fs";
import { createServer } from "node:http";
import { createRequire } from "node:module";
import { dirname, extname, join, normalize } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const OUT = join(ROOT, "_demos");
const { chromium } = createRequire(join(ROOT, "packages", "gti", "package.json"))("playwright");

// (Each as wide as the docs' page, and as high as its frame there)
const VENUES = { streamlit: 900, panel: 760, marimo: 760 };
const WIDTH = 900;

const TYPES = {
  ".html": "text/html",
  ".js": "text/javascript",
  ".mjs": "text/javascript",
  ".css": "text/css",
  ".json": "application/json",
  ".png": "image/png",
  ".svg": "image/svg+xml",
  ".wasm": "application/wasm",
};

// (`_demos/`, as the docs serve it)
const server = createServer((request, response) => {
  let path = normalize(join(OUT, decodeURIComponent(new URL(request.url, "http://x").pathname)));
  if (path.endsWith("/") || (existsSync(path) && !extname(path))) {
    path = join(path, "index.html");
  }
  if (!path.startsWith(OUT) || !existsSync(path)) {
    response.writeHead(404).end();
    return;
  }
  response.writeHead(200, { "Content-Type": TYPES[extname(path)] ?? "application/octet-stream" });
  if (extname(path) === ".html") {
    // (Without the front matter, which great-docs takes off)
    response.end(readFileSync(path, "utf-8").replace(/^---\n[\s\S]*?\n---\n/, ""));
  } else {
    createReadStream(path).pipe(response);
  }
});
await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
const base = `http://127.0.0.1:${server.address().port}`;

const browser = await chromium.launch();
try {
  for (const [venue, height] of Object.entries(VENUES)) {
    const context = await browser.newContext({ viewport: { width: WIDTH, height }, deviceScaleFactor: 2 });
    const page = await context.newPage();
    let bytes = 0;
    page.on("requestfinished", async (request) => {
      bytes += (await request.sizes()).responseBodySize;
    });
    await page.goto(`${base}/${venue}/`);
    const boxes = page.locator("gt-table tbody input[type=checkbox]");
    await boxes.first().waitFor({ timeout: 300000 });
    await page.getByText("0 of 47 cars selected").first().waitFor({ timeout: 60000 });
    await boxes.nth(0).click();
    await page.getByText("1 of 47 cars selected").first().waitFor();
    await boxes.nth(2).click();
    await page.getByText("2 of 47 cars selected").first().waitFor();
    await page.waitForTimeout(2000);
    await page.evaluate(() => document.activeElement?.blur());
    const png = await page.screenshot();
    // (As WebP, which Chromium writes)
    const webp = await page.evaluate(async (data) => {
      const image = new Image();
      image.src = `data:image/png;base64,${data}`;
      await image.decode();
      const canvas = Object.assign(document.createElement("canvas"), { width: image.width, height: image.height });
      canvas.getContext("2d").drawImage(image, 0, 0);
      return canvas.toDataURL("image/webp", 0.8).split(",")[1];
    }, png.toString("base64"));
    const file = join(ROOT, "assets", "demos", `${venue}.webp`);
    writeFileSync(file, Buffer.from(webp, "base64"));
    console.log(`${venue}: ${(bytes / 1e6).toFixed(1)} MB downloaded; ${file}`);
    await context.close();
  }
} finally {
  await browser.close();
  server.close();
}

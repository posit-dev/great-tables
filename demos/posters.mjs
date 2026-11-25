// Make the posters the docs show for the live app demos, until a reader runs one:
//
//   python demos/build.py && node demos/posters.mjs [venue ...]
//
// Each app in `_demos/` is run in Chromium (with Playwright, from packages/gti), with two cars
// selected, and its page saved as `assets/demos/<venue>.webp`. Then what it downloaded is printed,
// for the size the docs give. The apps that need a server (Solara's and Flask's, which the docs show
// only as these images) are run with `python` (as found on the PATH, or as $PYTHON), from `demos/`.

import { spawn } from "node:child_process";
import { createReadStream, existsSync, readFileSync, writeFileSync } from "node:fs";
import { createServer } from "node:http";
import { createRequire } from "node:module";
import { dirname, extname, join, normalize } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const OUT = join(ROOT, "_demos");
const { chromium } = createRequire(join(ROOT, "packages", "gti", "package.json"))("playwright");
const PYTHON = process.env.PYTHON ?? "python";

// (Two cars selected, in an app that counts them)
const selectTwo = async (page) => {
  const boxes = page.locator("gt-table tbody input[type=checkbox]");
  await boxes.first().waitFor({ timeout: 300000 });
  await page.getByText("0 of 47 cars selected").first().waitFor({ timeout: 60000 });
  await boxes.nth(0).click();
  await page.getByText("1 of 47 cars selected").first().waitFor();
  await boxes.nth(2).click();
  await page.getByText("2 of 47 cars selected").first().waitFor();
};

// (The notebook's cells run up to the table, two cars selected, and the next cell run)
const runNotebook = async (page) => {
  await page.locator(".jp-Notebook .jp-Cell .jp-InputPrompt").first().click({ timeout: 300000 });
  for (let i = 0; i < 3; i++) {
    await page.keyboard.press("Shift+Enter");
  }
  const boxes = page.locator("gt-table tbody input[type=checkbox]");
  await boxes.first().waitFor({ timeout: 300000 });
  await boxes.nth(0).click();
  await boxes.nth(2).click();
  await page.waitForTimeout(1000);
  await page.locator(".jp-Notebook .jp-Cell .jp-InputPrompt").nth(3).click();
  await page.keyboard.press("Shift+Enter");
  await page.getByText("2 of 47 cars selected").waitFor({ timeout: 60000 });
  // (From the table's top, with the cars selected, to the cars below it)
  await page.locator("gt-table").first().evaluate((table) => table.scrollIntoView({ block: "start" }));
};

// (Two cars selected in the page's second table, which has the checkboxes)
const selectInPage = async (page) => {
  const boxes = page.locator("gt-table tbody input[type=checkbox]");
  await boxes.first().waitFor({ timeout: 60000 });
  await boxes.nth(0).click();
  await boxes.nth(2).click();
};

// (Each as wide as the docs' page, and as high as its frame there, or the whole page)
const VENUES = {
  streamlit: { height: 900, steps: selectTwo },
  panel: { height: 760, steps: selectTwo },
  marimo: { height: 760, steps: selectTwo },
  widget: { height: 900, path: "widget/notebooks/index.html?path=_notebooks/cars.ipynb", steps: runNotebook },
  solara: {
    height: 760,
    serve: (port) => ["-m", "solara", "run", "solara/app.py", "--host", "127.0.0.1", "--port", port, "--production", "--no-open"],
    steps: selectTwo,
  },
  flask: {
    height: 760,
    fullPage: true,
    serve: (port) => ["-m", "flask", "--app", "flask/app.py", "run", "--port", port],
    steps: selectInPage,
  },
};
const WIDTH = 900;
// (Those named, or all)
const ONLY = process.argv.slice(2);

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

// (An app's server, run until it answers)
const serve = async (args) => {
  const port = String(8700 + Math.floor(Math.random() * 200));
  const app = spawn(PYTHON, args(port), { cwd: join(ROOT, "demos"), stdio: "ignore" });
  const url = `http://127.0.0.1:${port}/`;
  for (let tries = 0; tries < 120; tries++) {
    try {
      if ((await fetch(url)).ok) {
        return { app, url };
      }
    } catch {
      // (Not yet started)
    }
    await new Promise((resolve) => setTimeout(resolve, 500));
  }
  app.kill();
  throw new Error(`The app (${args(port).join(" ")}) didn't start`);
};

const browser = await chromium.launch();
try {
  for (const [venue, { height, path, serve: args, steps, fullPage }] of Object.entries(VENUES)) {
    if (ONLY.length > 0 && !ONLY.includes(venue)) {
      continue;
    }
    const context = await browser.newContext({ viewport: { width: WIDTH, height }, deviceScaleFactor: 2 });
    const page = await context.newPage();
    let bytes = 0;
    // (Of the context, so as to have what the apps' workers download too)
    context.on("requestfinished", async (request) => {
      bytes += (await request.sizes().catch(() => ({ responseBodySize: 0 }))).responseBodySize;
    });
    const running = args ? await serve(args) : null;
    try {
      await page.goto(running ? running.url : `${base}/${path ?? `${venue}/`}`);
      await steps(page);
      await page.waitForTimeout(2000);
      await page.evaluate(() => document.activeElement?.blur());
      const png = await page.screenshot({ fullPage });
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
    } finally {
      running?.app.kill();
      await context.close();
    }
  }
} finally {
  await browser.close();
  server.close();
}

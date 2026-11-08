import { expect, type FrameLocator, type Page, test } from "@playwright/test";
import { type ChildProcess, spawn, spawnSync } from "node:child_process";
import { cpSync, mkdtempSync, rmSync } from "node:fs";
import { createServer } from "node:net";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { python } from "./global-setup";

// The tables shown by each host (as make_hosts.py writes its sources): a GTI table, an
// `opt_interactive()` one, and a static one. Each host runs them itself (from a copy of the
// sources, in a directory of its own), so a test is skipped where its host isn't installed.

const hosts = join(dirname(fileURLToPath(import.meta.url)), ".fixtures", "hosts");
// (As a path from anywhere, since the hosts run in another directory)
const PYTHON = python().includes("/") ? resolve(python()) : python();

let dir: string;

test.beforeAll(() => {
  dir = mkdtempSync(join(tmpdir(), "gti-hosts-"));
  cpSync(hosts, dir, { recursive: true });
});

test.afterAll(() => {
  rmSync(dir, { recursive: true, force: true });
});

test.describe.configure({ timeout: 120_000 });

// (A Python with these modules can run the host)
const has = (...modules: string[]) =>
  spawnSync(PYTHON, ["-c", modules.map((module) => `import ${module}`).join("; ")]).status === 0;

const quarto = () => spawnSync("quarto", ["--version"]).status === 0;

// The environment a host runs in: one that isn't taken for another host's (as GT tells hosts
// apart by their variables), with Jupyter's and IPython's files of its own, and this Python's
// kernel.
function hostEnv(): NodeJS.ProcessEnv {
  const env: NodeJS.ProcessEnv = {
    ...process.env,
    JUPYTER_PATH: join(dir, "jupyter"),
    JUPYTER_CONFIG_DIR: join(dir, "config"),
    JUPYTER_DATA_DIR: join(dir, "data"),
    JUPYTER_RUNTIME_DIR: join(dir, "runtime"),
    IPYTHONDIR: join(dir, "ipython"),
    QUARTO_PYTHON: PYTHON,
    JUPYTER_PLATFORM_DIRS: "1",
  };
  for (const name of ["VSCODE_PID", "POSITRON_VERSION", "QUARTO_BIN_PATH", "DATABRICKS_RUNTIME_VERSION"]) {
    delete env[name];
  }
  return env;
}

function run(command: string, ...args: string[]): void {
  const result = spawnSync(command, args, { cwd: dir, env: hostEnv(), encoding: "utf-8" });
  if (result.status !== 0) {
    throw new Error(`${command} ${args.join(" ")} failed:\n${result.stdout}\n${result.stderr}`);
  }
}

function freePort(): Promise<number> {
  return new Promise((resolve, reject) => {
    const server = createServer();
    server.on("error", reject);
    server.listen(0, "127.0.0.1", () => {
      const address = server.address();
      server.close(() => resolve(typeof address === "object" && address !== null ? address.port : 0));
    });
  });
}

// A server, once it answers at the URL.
async function serve(url: string, ...args: string[]): Promise<ChildProcess> {
  const server = spawn(PYTHON, args, { cwd: dir, env: hostEnv(), stdio: "ignore" });
  for (let tries = 0; tries < 240; tries++) {
    if (server.exitCode !== null) {
      break;
    }
    try {
      if ((await fetch(url)).ok) {
        return server;
      }
    } catch {
      // (Not up yet)
    }
    await new Promise((resolve) => setTimeout(resolve, 250));
  }
  server.kill();
  throw new Error(`${args.join(" ")} didn't answer at ${url}`);
}

// What the tables' runtime says went wrong, and what the page throws (but what the host is known
// to).
function watch(page: Page, host?: RegExp): string[] {
  const errors: string[] = [];
  page.on("pageerror", (err) => {
    if (host === undefined || !host.test(err.message)) {
      errors.push(err.message);
    }
  });
  page.on("console", (msg) => {
    if (msg.text().startsWith("<gt-table>:")) {
      errors.push(msg.text());
    }
  });
  return errors;
}

type Root = Page | FrameLocator;

// The interactive tables are hydrated, the static one is left alone, and the ids the runtime
// makes are unique on the page.
async function hydrated(root: Root, count = 2): Promise<void> {
  const tables = root.locator("gt-table:not([data-old])");
  await expect(tables).toHaveCount(count);
  for (let i = 0; i < count; i++) {
    await expect(tables.nth(i)).toHaveAttribute("data-gti-state", "ready");
  }
  const page = await root.locator("body").evaluate((body) => {
    const ids = Array.from(body.querySelectorAll("[id^='gt-i-']"), (el) => el.id);
    return {
      static: Array.from(body.querySelectorAll(".gt_table")).filter((table) => table.closest("gt-table") === null).length,
      ids: ids.length,
      unique: new Set(ids).size,
    };
  });
  expect(page.static).toBe(1);
  expect(page.ids).toBeGreaterThan(0);
  expect(page.unique).toBe(page.ids);
}

// Sorting the first table by its first column, which is then sorted.
async function sorts(root: Root): Promise<void> {
  const table = root.locator("gt-table:not([data-old])").first();
  await table.locator("button.gt-i-sort").first().click();
  await expect(table.locator("th[aria-sort]")).toHaveAttribute("aria-sort", "ascending");
}

// The tables as they are, marked as old: those shown again as the cells are run again aren't.
async function markOld(root: Root): Promise<void> {
  await root.locator("body").evaluate((body) => {
    for (const el of body.querySelectorAll("gt-table")) {
      el.setAttribute("data-old", "");
    }
  });
}

// The tables shown again: new elements, hydrated, and not sorted (as the old one was).
async function shownAgain(root: Root, count = 2): Promise<void> {
  await expect(root.locator("gt-table[data-old]")).toHaveCount(0);
  await hydrated(root, count);
  await expect(root.locator("gt-table th[aria-sort]")).toHaveCount(0);
}

test("Jupyter: a notebook converted to HTML", async ({ page }) => {
  test.skip(!has("nbconvert", "ipykernel"), "nbconvert and ipykernel aren't installed");
  run(PYTHON, "-m", "jupyter", "nbconvert", "--to", "html", "--execute", "notebook.ipynb");
  const errors = watch(page);
  await page.goto(pathToFileURL(join(dir, "notebook.html")).href);

  await hydrated(page);
  await sorts(page);
  expect(errors).toEqual([]);
});

test("Jupyter: a notebook in JupyterLab, run and run again", async ({ page }) => {
  test.skip(!has("jupyterlab", "ipykernel"), "JupyterLab and ipykernel aren't installed");
  const port = await freePort();
  const token = "gti-hosts";
  const base = `http://127.0.0.1:${port}`;
  const server = await serve(
    `${base}/api/status?token=${token}`,
    "-m", "jupyter", "lab", "--no-browser", `--port=${port}`, "--ip=127.0.0.1",
    `--ServerApp.token=${token}`, `--ServerApp.root_dir=${dir}`,
    "--LabApp.expose_app_in_browser=True",
    `--LabApp.user_settings_dir=${join(dir, "settings")}`,
    `--LabApp.workspaces_dir=${join(dir, "workspaces")}`,
  );
  try {
    // (JupyterLab's debugger throws when the kernel's started)
    const errors = watch(page, /^No active debugger session$/);
    await page.goto(`${base}/lab/tree/notebook.ipynb?token=${token}&reset`);
    const runAll = () =>
      page.evaluate(() => (window as any).jupyterapp.commands.execute("notebook:run-all-cells"));
    // (Once the notebook's kernel is up)
    await expect
      .poll(
        () =>
          page.evaluate(() => (window as any).jupyterapp?.shell.currentWidget?.sessionContext?.session?.kernel?.status),
        { timeout: 60_000 },
      )
      .toBe("idle");
    await runAll();
    await hydrated(page);
    await sorts(page);

    await markOld(page);
    await runAll();
    await shownAgain(page);
    expect(errors).toEqual([]);
  } finally {
    server.kill();
  }
});

test("Quarto: a document with two interactive tables and a static one", async ({ page }) => {
  test.skip(!quarto(), "Quarto isn't installed");
  test.skip(!has("nbclient", "ipykernel"), "nbclient and ipykernel aren't installed");
  run("quarto", "render", "doc.qmd");
  const errors = watch(page);
  await page.goto(pathToFileURL(join(dir, "doc.html")).href);

  // (Quarto gives every table its own classes, which don't keep it from being hydrated)
  await expect(page.locator("gt-table table.gt_table.table")).toHaveCount(2);
  await hydrated(page);
  await sorts(page);
  expect(errors).toEqual([]);
});

test("Shiny: tables rendered again as an input changes", async ({ page }) => {
  test.skip(!has("shiny"), "Shiny isn't installed");
  const port = await freePort();
  const base = `http://127.0.0.1:${port}`;
  const server = await serve(base, "-m", "shiny", "run", "--port", String(port), "shiny_app.py");
  try {
    const errors = watch(page);
    await page.goto(base);
    await hydrated(page);
    await sorts(page);
    await expect(page.locator("gt-table").first().locator("tbody.gt_table_body > tr")).toHaveCount(8);

    await markOld(page);
    await page.locator("#rows").selectOption("head");
    await shownAgain(page);
    for (const table of await page.locator("gt-table").all()) {
      await expect(table.locator("tbody.gt_table_body > tr")).toHaveCount(4);
    }
    expect(errors).toEqual([]);
  } finally {
    server.kill();
  }
});

test("marimo: an app exported to HTML", async ({ page }) => {
  test.skip(!has("marimo"), "marimo isn't installed");
  run(PYTHON, "-m", "marimo", "export", "html", "marimo_app.py", "-o", "marimo.html");
  const errors = watch(page);
  // (The page loads marimo's frontend from a CDN)
  await page.goto(pathToFileURL(join(dir, "marimo.html")).href);

  // Each interactive table (an output with a script) is shown in a frame of its own
  const frames = page.locator("iframe");
  await expect(frames).toHaveCount(2, { timeout: 30_000 });
  for (let i = 0; i < 2; i++) {
    const frame = frames.nth(i).contentFrame();
    await expect(frame.locator("gt-table")).toHaveAttribute("data-gti-state", "ready");
  }
  await sorts(frames.first().contentFrame());
  // A table's HTML shown with `mo.Html()` isn't a frame, so its script doesn't run: it stays as
  // it is, static
  await expect(page.locator("#html .gt_table")).toHaveCount(1);
  await expect(page.locator("gt-table[data-gti-state]")).toHaveCount(0);
  expect(errors).toEqual([]);
});

test("VS Code: outputs shown as its notebooks show them, in a sandboxed frame", async ({ page }) => {
  const errors = watch(page);
  await page.goto(pathToFileURL(join(dir, "vscode.html")).href);
  const frame = page.frameLocator("iframe");

  await hydrated(frame);
  await sorts(frame);

  await markOld(frame);
  await frame.locator("body").evaluate(() => (window as any).show());
  await shownAgain(frame);
  await sorts(frame);
  expect(errors).toEqual([]);
});

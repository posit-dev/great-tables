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

// JupyterLab, serving the sources, with a notebook open (once its kernel is up)
async function lab(page: Page, notebook: string, body: () => Promise<void>): Promise<void> {
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
    await page.goto(`${base}/lab/tree/${notebook}?token=${token}&reset`);
    await expect
      .poll(
        () =>
          page.evaluate(() => (window as any).jupyterapp?.shell.currentWidget?.sessionContext?.session?.kernel?.status),
        { timeout: 60_000 },
      )
      .toBe("idle");
    await body();
  } finally {
    server.kill();
  }
}

const runAll = (page: Page) =>
  page.evaluate(() => (window as any).jupyterapp.commands.execute("notebook:run-all-cells"));

// What the notebook's kernel prints, running `code`
const kernelRun = (page: Page, code: string): Promise<string> =>
  page.evaluate(async (code) => {
    const kernel = (window as any).jupyterapp.shell.currentWidget.sessionContext.session.kernel;
    const future = kernel.requestExecute({ code });
    let out = "";
    future.onIOPub = (msg: any) => {
      if (msg.header.msg_type === "stream") {
        out += msg.content.text;
      } else if (msg.header.msg_type === "error") {
        out += `${msg.content.ename}: ${msg.content.evalue}`;
      }
    };
    await future.done;
    return out;
  }, code);

// What `expr` is in the notebook's kernel (as JSON, from the reply, not what it prints, which a
// notebook's Panel can lose, its messages' handlers taking the prints in two threads at once)
const kernelValue = (page: Page, expr: string): Promise<unknown> =>
  page.evaluate(async (expr) => {
    const kernel = (window as any).jupyterapp.shell.currentWidget.sessionContext.session.kernel;
    const value = `__import__("base64").b64encode(__import__("json").dumps(${expr}).encode()).decode()`;
    const reply = await kernel.requestExecute({ code: "", user_expressions: { value } }).done;
    const result = reply.content.user_expressions.value;
    if (result.status !== "ok") {
      throw new Error(`${result.ename}: ${result.evalue}`);
    }
    // (Its text, a Python string, in quotes)
    return JSON.parse(atob(result.data["text/plain"].slice(1, -1)));
  }, expr);

test("Jupyter: a notebook in JupyterLab, run and run again", async ({ page }) => {
  test.skip(!has("jupyterlab", "ipykernel"), "JupyterLab and ipykernel aren't installed");
  // (JupyterLab's debugger throws when the kernel's started)
  const errors = watch(page, /^No active debugger session$/);
  await lab(page, "notebook.ipynb", async () => {
    await runAll(page);
    await hydrated(page);
    await sorts(page);

    await markOld(page);
    await runAll(page);
    await shownAgain(page);
  });
  expect(errors).toEqual([]);
});

test("Jupyter: a table as a widget, which the kernel reads and changes", async ({ page }) => {
  test.skip(!has("jupyterlab", "ipykernel", "anywidget"), "JupyterLab, ipykernel and anywidget aren't installed");
  const errors = watch(page, /^No active debugger session$/);
  await lab(page, "widget.ipynb", async () => {
    await runAll(page);
    // (The widget, shown twice: the first is the one used, and the second follows it)
    const tables = page.locator(".jp-OutputArea gt-table");
    await expect(tables).toHaveCount(2);
    const [table, again] = [tables.first(), tables.last()];
    await expect(table).toHaveAttribute("data-gti-state", "ready");
    const shown = (el: typeof table) => el.evaluate((el: any) => [el.rows, el.selection, el.search, el.sort]);
    const state = () => kernelValue(page, "[widget.rows, widget.selection, widget.query, widget.search]");
    await expect.poll(state).toEqual([[0, 1, 2, 3, 4, 5, 6, 7], [], "", ""]);

    // What the reader does, the kernel has (and its callback's told)
    await table.getByRole("button", { name: "Search the table" }).click();
    await table.locator("input.gt-i-search").fill("an");
    await expect.poll(state).toEqual([[1, 3], [], "", "an"]);
    await table.locator("tbody input[type=checkbox]").nth(3).check();
    await expect.poll(state).toEqual([[1, 3], [3], "", "an"]);
    expect(await kernelValue(page, "changes[-1]")).toEqual([[1, 3], [3]]);
    expect(await kernelValue(page, "widget.view()['char'].tolist()")).toEqual(["banana", "durian"]);
    await expect.poll(() => shown(again)).toEqual([[1, 3], [3], "an", []]);

    // What the kernel changes, the table shows
    await kernelRun(page, 'widget.search = ""; widget.query = \'fctr in ("one", "two")\'; widget.sort = "-num"; widget.selection = [0]');
    for (const el of [table, again]) {
      await expect.poll(() => shown(el)).toEqual([[1, 0], [0], "", [{ column: "num", descending: true }]]);
    }
    await expect.poll(state).toEqual([[1, 0], [0], 'fctr in ("one", "two")', ""]);
    expect(await kernelValue(page, "widget.view(selected=True)['char'].tolist()")).toEqual(["apricot"]);
  });
  expect(errors).toEqual([]);
});

// (Of a data frame, and of a LazyFrame, whose rows the kernel finds with Polars queries)
for (const [what, notebook, needs] of [
  ["", "kernel_widget.ipynb", []],
  [" of a LazyFrame", "lazy_widget.ipynb", ["polars"]],
] as const) {
  test(`Jupyter: a widget${what} whose rows are the kernel's, a page at a time`, async ({ page }) => {
    test.skip(!has("jupyterlab", "ipykernel", "anywidget", ...needs), `${["JupyterLab", "ipykernel", "anywidget", ...needs].join(", ")} aren't all installed`);
    const errors = watch(page, /^No active debugger session$/);
    await lab(page, notebook, async () => {
      await runAll(page);
      const table = page.locator(".jp-OutputArea gt-table");
      await expect(table).toHaveAttribute("data-gti-state", "ready");
      // (The table has only the rows shown, or shown before)
      const shown = () => table.evaluate((el: any) => [el.rows, el.pageCount, el.loading]);
      const rows = (start: number, step = 1) => Array.from({ length: 10 }, (_, i) => start + i * step);
      await expect.poll(shown).toEqual([rows(0), 500, false]);
      await expect(table.locator("tbody tr:not([hidden])")).toHaveCount(10);

      // (Each page, sort and search, from the kernel)
      await table.evaluate((el: any) => {
        el.page = 3;
      });
      await expect.poll(shown).toEqual([rows(20), 500, false]);
      await table.locator("thead button.gt-i-sort").first().click();
      await table.locator("thead button.gt-i-sort").first().click();
      await expect.poll(shown).toEqual([rows(4999, -1), 500, false]);
      await expect(table.locator("tbody tr:not([hidden]) td").first()).toHaveText("4999");
      await table.getByRole("button", { name: "Search the table" }).click();
      await table.locator("input.gt-i-search").fill("4998");
      await expect.poll(shown).toEqual([[4998], 1, false]);
      expect(await kernelValue(page, "[widget.rows, widget.search]")).toEqual([[4998], "4998"]);

      // (And a view the kernel sets)
      await kernelRun(page, 'widget.search = ""; widget.query = \'kind in ("odd")\'; widget.sort = "n"');
      await expect.poll(shown).toEqual([rows(1, 2), 250, false]);
      expect(await kernelValue(page, "widget.rows[:3]")).toEqual([1, 3, 5]);
    });
    expect(errors).toEqual([]);
  });
}

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

test("Shiny: a table's state as inputs, which the server changes", async ({ page }) => {
  test.skip(!has("shiny"), "Shiny isn't installed");
  const port = await freePort();
  const base = `http://127.0.0.1:${port}`;
  const server = await serve(base, "-m", "shiny", "run", "--port", String(port), "shiny_state_app.py");
  try {
    const errors = watch(page);
    await page.goto(base);
    const table = page.locator("#m-table > gt-table");
    await expect(table).toHaveAttribute("data-gti-state", "ready");
    const state = async () => JSON.parse((await page.locator("#m-state").textContent()) || "null");
    const shown = () => table.evaluate((el: any) => [el.rows, el.selection, el.search, el.sort]);
    await expect.poll(state).toEqual(["", "", [], [0, 1, 2, 3, 4, 5, 6, 7], []]);

    // What the reader does, the server has
    await table.getByRole("button", { name: "Search the table" }).click();
    await table.locator("input.gt-i-search").fill("an");
    await expect.poll(state).toEqual(["", "an", [], [1, 3], []]);
    await table.locator("tbody input[type=checkbox]").nth(3).check();
    await expect.poll(state).toEqual(["", "an", [], [1, 3], [3]]);
    await table.locator("input.gt-i-search").fill("");

    // What the server changes, the table shows
    await page.getByRole("button", { name: "Update" }).click();
    await expect.poll(shown).toEqual([[1, 0], [0], "", [{ column: "num", descending: true }]]);
    await expect.poll(state).toEqual(['fctr in ("one", "two")', "", ["-num"], [1, 0], [0]]);

    // (And a table rendered again takes what the server set on it in the same flush)
    await table.evaluate((el) => el.setAttribute("data-old", ""));
    await page.getByRole("button", { name: "Again" }).click();
    const again = page.locator("#m-table > gt-table:not([data-old])");
    await expect(again).toHaveAttribute("data-gti-state", "ready");
    await expect.poll(state).toEqual(["", "an", [], [1, 3], []]);
    expect(errors).toEqual([]);
  } finally {
    server.kill();
  }
});

// (Of a data frame, and of a LazyFrame)
for (const [what, app, needs] of [
  ["", "shiny_kernel_app.py", []],
  [" of a LazyFrame", "shiny_lazy_app.py", ["polars"]],
] as const) {
  test(`Shiny: a table${what} whose rows are the server's, a page at a time`, async ({ page }) => {
    test.skip(!has("shiny", ...needs), `${["Shiny", ...needs].join(" and ")} aren't all installed`);
    const port = await freePort();
    const base = `http://127.0.0.1:${port}`;
    const server = await serve(base, "-m", "shiny", "run", "--port", String(port), app);
    try {
      const errors = watch(page);
      await page.goto(base);
      const table = page.locator("#m-table > gt-table");
      await expect(table).toHaveAttribute("data-gti-state", "ready");
      const state = async () => JSON.parse((await page.locator("#m-state").textContent()) || "null");
      // (The table has only the rows shown, or shown before)
      const shown = () => table.evaluate((el: any) => [el.rows, el.pageCount, el.loading]);
      const rows = (start: number, step = 1) => Array.from({ length: 10 }, (_, i) => start + i * step);
      await expect.poll(shown).toEqual([rows(0), 500, false]);
      await expect.poll(state).toEqual([5000, [0, 1, 2], ""]);

      // (Each page, sort and search, from the server, which finds the rows)
      await table.evaluate((el: any) => {
        el.page = 3;
      });
      await expect.poll(shown).toEqual([rows(20), 500, false]);
      await table.locator("thead button.gt-i-sort").first().click();
      await table.locator("thead button.gt-i-sort").first().click();
      await expect.poll(shown).toEqual([rows(4999, -1), 500, false]);
      await expect(table.locator("tbody tr:not([hidden]) td").first()).toHaveText("4999");
      await expect.poll(state).toEqual([5000, [4999, 4998, 4997], ""]);
      await table.getByRole("button", { name: "Search the table" }).click();
      await table.locator("input.gt-i-search").fill("4998");
      await expect.poll(shown).toEqual([[4998], 1, false]);
      await expect.poll(state).toEqual([1, [4998], "4998"]);

      // (And a view the server sets)
      await page.getByRole("button", { name: "Update" }).click();
      await expect.poll(shown).toEqual([rows(1, 2), 250, false]);
      await expect.poll(state).toEqual([2500, [1, 3, 5], ""]);
      expect(errors).toEqual([]);
    } finally {
      server.kill();
    }
  });
}

// A Streamlit app, once it answers (headless, on a port of its own)
async function streamlit(app: string): Promise<{ base: string; server: ChildProcess }> {
  const port = await freePort();
  const base = `http://127.0.0.1:${port}`;
  const server = await serve(
    `${base}/_stcore/health`,
    ...["-m", "streamlit", "run", app, "--server.headless", "true", "--server.port", String(port)],
    ...["--browser.gatherUsageStats", "false"],
  );
  return { base, server };
}

test("Streamlit: a table's state, as st_gti() gives it, which the app changes", async ({ page }) => {
  test.skip(!has("streamlit"), "Streamlit isn't installed");
  const { base, server } = await streamlit("streamlit_state_app.py");
  try {
    const errors = watch(page);
    await page.goto(base);
    const table = page.locator("gt-table");
    await expect(table).toHaveAttribute("data-gti-state", "ready");
    const state = async () => JSON.parse((await page.locator(".st-key-state").textContent()) || "null");
    const runs = async () => Number(await page.locator(".st-key-runs").textContent());
    const shown = () => table.evaluate((el: any) => [el.rows, el.selection, el.search, el.sort]);
    await expect.poll(state).toEqual(["", "", [], [0, 1, 2, 3, 4, 5, 6, 7], []]);

    // What the reader does, the app has, in one run each (and none for the table being shown)
    await table.getByRole("button", { name: "Search the table" }).click();
    await table.locator("input.gt-i-search").fill("an");
    await expect.poll(state).toEqual(["", "an", [], [1, 3], []]);
    await table.locator("tbody input[type=checkbox]").nth(3).check();
    await expect.poll(state).toEqual(["", "an", [], [1, 3], [3]]);
    await table.locator("input.gt-i-search").fill("");
    await expect.poll(state).toEqual(["", "", [], [0, 1, 2, 3, 4, 5, 6, 7], [3]]);
    expect(await runs()).toBe(4);

    // What the app changes, the table shows (the table, made again on each run, is the same one)
    await table.evaluate((el) => el.setAttribute("data-old", ""));
    await page.getByRole("button", { name: "Update" }).click();
    await expect.poll(shown).toEqual([[1, 0], [0], "", [{ column: "num", descending: true }]]);
    await expect.poll(state).toEqual(['fctr in ("one", "two")', "", ["-num"], [1, 0], [0]]);
    await expect(page.locator("gt-table[data-old]")).toHaveCount(1);
    expect(await runs()).toBe(5);

    // (And another table is shown with its own view)
    await page.getByText("Head").click();
    await expect(page.locator("gt-table[data-old]")).toHaveCount(0);
    await expect(table).toHaveAttribute("data-gti-state", "ready");
    await expect.poll(state).toEqual(["", "", [], [0, 1, 2, 3], []]);
    await expect.poll(shown).toEqual([[0, 1, 2, 3], [], "", []]);
    expect(errors).toEqual([]);
  } finally {
    server.kill();
  }
});

// (Of a data frame, and of a LazyFrame)
for (const [what, app, needs] of [
  ["", "streamlit_kernel_app.py", []],
  [" of a LazyFrame", "streamlit_lazy_app.py", ["polars"]],
] as const) {
  test(`Streamlit: a table${what} whose rows are the app's, a page at a time`, async ({ page }) => {
    test.skip(!has("streamlit", ...needs), `${["Streamlit", ...needs].join(" and ")} aren't all installed`);
    const { base, server } = await streamlit(app);
    try {
      const errors = watch(page);
      await page.goto(base);
      const table = page.locator("gt-table");
      await expect(table).toHaveAttribute("data-gti-state", "ready");
      const state = async () => JSON.parse((await page.locator(".st-key-state").textContent()) || "null");
      const shown = () => table.evaluate((el: any) => [el.rows, el.pageCount, el.loading]);
      const rows = (start: number, step = 1) => Array.from({ length: 10 }, (_, i) => start + i * step);
      await expect.poll(shown).toEqual([rows(0), 500, false]);
      await expect.poll(state).toEqual([5000, [0, 1, 2], ""]);

      // (Each page, sort and search, from the app, which finds the rows)
      await table.evaluate((el: any) => {
        el.page = 3;
      });
      await expect.poll(shown).toEqual([rows(20), 500, false]);
      await table.locator("thead button.gt-i-sort").first().click();
      await table.locator("thead button.gt-i-sort").first().click();
      await expect.poll(shown).toEqual([rows(4999, -1), 500, false]);
      await expect(table.locator("tbody tr:not([hidden]) td").first()).toHaveText("4999");
      await expect.poll(state).toEqual([5000, [4999, 4998, 4997], ""]);
      await table.getByRole("button", { name: "Search the table" }).click();
      await table.locator("input.gt-i-search").fill("4998");
      await expect.poll(shown).toEqual([[4998], 1, false]);
      await expect.poll(state).toEqual([1, [4998], "4998"]);

      // (And a view the app sets, which the asks for its pages don't undo)
      await page.getByRole("button", { name: "Update" }).click();
      await expect.poll(shown).toEqual([rows(1, 2), 250, false]);
      await expect.poll(state).toEqual([2500, [1, 3, 5], ""]);
      await table.evaluate((el: any) => {
        el.page = 2;
      });
      await expect.poll(shown).toEqual([rows(21, 2), 250, false]);
      await expect.poll(state).toEqual([2500, [1, 3, 5], ""]);
      expect(errors).toEqual([]);
    } finally {
      server.kill();
    }
  });
}

// A Panel app, once it answers (on a port of its own), at its URL
async function panel(app: string): Promise<{ url: string; server: ChildProcess }> {
  const port = await freePort();
  const url = `http://127.0.0.1:${port}/${app.replace(/\.py$/, "")}`;
  const server = await serve(
    url,
    ...["-m", "panel", "serve", app, "--port", String(port), "--address", "127.0.0.1"],
    `--allow-websocket-origin=127.0.0.1:${port}`,
  );
  return { url, server };
}

// (What the app shows of the pane's parameters: Panel's components are each in a shadow root,
// which the locators see into)
const panelState = async (page: Page): Promise<unknown> =>
  JSON.parse((await page.locator("pre").filter({ hasText: /^\[/ }).textContent()) || "null");

test("Panel: a table's parameters, which the app watches and sets", async ({ page }) => {
  test.skip(!has("panel"), "Panel isn't installed");
  const { url, server } = await panel("panel_state_app.py");
  try {
    const errors = watch(page);
    await page.goto(url);
    const table = page.locator("gt-table");
    await expect(table).toHaveAttribute("data-gti-state", "ready");
    const state = () => panelState(page);
    const shown = () => table.evaluate((el: any) => [el.rows, el.selection, el.search, el.sort]);
    await expect.poll(state).toEqual(["", "", [], [0, 1, 2, 3, 4, 5, 6, 7], []]);

    // What the reader does, the app has (with the runtime's CSS, in the component's shadow root)
    await expect(table.locator("button.gt-i-sort").first()).toHaveCSS("cursor", "pointer");
    await table.getByRole("button", { name: "Search the table" }).click();
    await table.locator("input.gt-i-search").fill("an");
    await expect.poll(state).toEqual(["", "an", [], [1, 3], []]);
    await table.locator("tbody input[type=checkbox]").nth(3).check();
    await expect.poll(state).toEqual(["", "an", [], [1, 3], [3]]);
    await table.locator("input.gt-i-search").fill("");
    await expect.poll(state).toEqual(["", "", [], [0, 1, 2, 3, 4, 5, 6, 7], [3]]);

    // What the app sets, the table shows
    await page.getByRole("button", { name: "Update" }).click();
    await expect.poll(shown).toEqual([[1, 0], [0], "", [{ column: "num", descending: true }]]);
    await expect.poll(state).toEqual(['fctr in ("one", "two")', "", ["-num"], [1, 0], [0]]);
    expect(errors).toEqual([]);
  } finally {
    server.kill();
  }
});

// (Of a data frame, and of a LazyFrame)
for (const [what, app, needs] of [
  ["", "panel_kernel_app.py", []],
  [" of a LazyFrame", "panel_lazy_app.py", ["polars"]],
] as const) {
  test(`Panel: a table${what} whose rows are the app's, a page at a time`, async ({ page }) => {
    test.skip(!has("panel", ...needs), `${["Panel", ...needs].join(" and ")} aren't all installed`);
    const { url, server } = await panel(app);
    try {
      const errors = watch(page);
      await page.goto(url);
      const table = page.locator("gt-table");
      await expect(table).toHaveAttribute("data-gti-state", "ready");
      const state = () => panelState(page);
      const shown = () => table.evaluate((el: any) => [el.rows, el.pageCount, el.loading]);
      const rows = (start: number, step = 1) => Array.from({ length: 10 }, (_, i) => start + i * step);
      await expect.poll(shown).toEqual([rows(0), 500, false]);
      await expect.poll(state).toEqual([5000, [0, 1, 2], ""]);

      // (Each page, sort and search, from the app, which finds the rows)
      await table.evaluate((el: any) => {
        el.page = 3;
      });
      await expect.poll(shown).toEqual([rows(20), 500, false]);
      await table.locator("thead button.gt-i-sort").first().click();
      await table.locator("thead button.gt-i-sort").first().click();
      await expect.poll(shown).toEqual([rows(4999, -1), 500, false]);
      await expect(table.locator("tbody tr:not([hidden]) td").first()).toHaveText("4999");
      await expect.poll(state).toEqual([5000, [4999, 4998, 4997], ""]);
      await table.getByRole("button", { name: "Search the table" }).click();
      await table.locator("input.gt-i-search").fill("4998");
      await expect.poll(shown).toEqual([[4998], 1, false]);
      await expect.poll(state).toEqual([1, [4998], "4998"]);

      // (And a view the app sets, which the asks for its pages don't undo)
      await page.getByRole("button", { name: "Update" }).click();
      await expect.poll(shown).toEqual([rows(1, 2), 250, false]);
      await expect.poll(state).toEqual([2500, [1, 3, 5], ""]);
      await table.evaluate((el: any) => {
        el.page = 2;
      });
      await expect.poll(shown).toEqual([rows(21, 2), 250, false]);
      await expect.poll(state).toEqual([2500, [1, 3, 5], ""]);
      expect(errors).toEqual([]);
    } finally {
      server.kill();
    }
  });
}

test("Panel: a table in a notebook in JupyterLab, which the kernel reads and changes", async ({ page }) => {
  test.skip(!has("jupyterlab", "ipykernel", "panel"), "JupyterLab, ipykernel and Panel aren't installed");
  const errors = watch(page, /^No active debugger session$/);
  await lab(page, "panel.ipynb", async () => {
    await runAll(page);
    const table = page.locator(".jp-OutputArea gt-table");
    await expect(table).toHaveAttribute("data-gti-state", "ready");
    const shown = () => table.evaluate((el: any) => [el.rows, el.selection, el.search, el.sort]);
    const state = () => kernelValue(page, "[pane.query, pane.search, pane.sort, pane.rows, pane.selection]");
    await expect.poll(state).toEqual(["", "", [], [0, 1, 2, 3, 4, 5, 6, 7], []]);

    // What the reader does, the kernel has
    await table.getByRole("button", { name: "Search the table" }).click();
    await table.locator("input.gt-i-search").fill("an");
    await expect.poll(state).toEqual(["", "an", [], [1, 3], []]);
    await table.locator("tbody input[type=checkbox]").nth(3).check();
    await expect.poll(state).toEqual(["", "an", [], [1, 3], [3]]);

    // What the kernel changes, the table shows
    await kernelRun(page, 'pane.param.update(search="", query=\'fctr in ("one", "two")\', sort=["-num"], selection=[0])');
    await expect.poll(shown).toEqual([[1, 0], [0], "", [{ column: "num", descending: true }]]);
    await expect.poll(state).toEqual(['fctr in ("one", "two")', "", ["-num"], [1, 0], [0]]);
  });
  expect(errors).toEqual([]);
});

test("Panel: a table in a notebook in JupyterLab, shown twice, whose rows are the kernel's", async ({ page }) => {
  test.skip(!has("jupyterlab", "ipykernel", "panel"), "JupyterLab, ipykernel and Panel aren't installed");
  const errors = watch(page, /^No active debugger session$/);
  await lab(page, "panel_kernel.ipynb", async () => {
    await runAll(page);
    const tables = page.locator(".jp-OutputArea gt-table");
    await expect(tables).toHaveCount(2);
    const [one, two] = [tables.first(), tables.last()];
    await expect(one).toHaveAttribute("data-gti-state", "ready");
    await expect(two).toHaveAttribute("data-gti-state", "ready");
    const shown = (table: typeof one) => () => table.evaluate((el: any) => [el.rows, el.pageCount, el.loading]);
    const rows = (start: number, step = 1) => Array.from({ length: 10 }, (_, i) => start + i * step);
    await expect.poll(shown(one)).toEqual([rows(0), 500, false]);

    // (Each page, sort and search, from the kernel; and the other view follows the view's)
    await one.evaluate((el: any) => {
      el.page = 3;
    });
    await expect.poll(shown(one)).toEqual([rows(20), 500, false]);
    await one.locator("thead button.gt-i-sort").first().click();
    await one.locator("thead button.gt-i-sort").first().click();
    await expect.poll(shown(one)).toEqual([rows(4999, -1), 500, false]);
    await expect.poll(shown(two)).toEqual([rows(4999, -1), 500, false]);
    await one.getByRole("button", { name: "Search the table" }).click();
    await one.locator("input.gt-i-search").fill("4998");
    await expect.poll(shown(one)).toEqual([[4998], 1, false]);
    await expect.poll(shown(two)).toEqual([[4998], 1, false]);
    await expect.poll(() => kernelValue(page, "[pane.rows, pane.search]")).toEqual([[4998], "4998"]);

    // (And a view the kernel sets, on both)
    await kernelRun(page, 'pane.param.update(search="", query=\'kind in ("odd")\', sort=["n"])');
    await expect.poll(shown(one)).toEqual([rows(1, 2), 250, false]);
    await expect.poll(shown(two)).toEqual([rows(1, 2), 250, false]);
    expect(await kernelValue(page, "pane.rows[:3]")).toEqual([1, 3, 5]);
  });
  expect(errors).toEqual([]);
});

// A Solara app, once it answers (on a port of its own)
async function solara(app: string): Promise<{ url: string; server: ChildProcess }> {
  const port = await freePort();
  const url = `http://127.0.0.1:${port}/`;
  const server = await serve(
    url,
    ...["-m", "solara", "run", app, "--port", String(port), "--host", "127.0.0.1"],
    ...["--no-open", "--production"],
  );
  return { url, server };
}

// (What the app shows of the table's values; and what anywidget says went wrong, as a widget
// it can't make is only logged)
const solaraState = async (page: Page): Promise<unknown> =>
  JSON.parse((await page.locator(".state").textContent()) || "null");

function watchWidgets(page: Page, errors: string[]): void {
  page.on("console", (msg) => {
    if (msg.text().startsWith("[anywidget]")) {
      errors.push(msg.text());
    }
  });
}

test("Solara: a table's values, which the app reads and sets", async ({ page }) => {
  test.skip(!has("solara"), "Solara isn't installed");
  const { url, server } = await solara("solara_state_app.py");
  try {
    const errors = watch(page);
    watchWidgets(page, errors);
    await page.goto(url);
    const table = page.locator("gt-table");
    await expect(table).toHaveAttribute("data-gti-state", "ready");
    const state = () => solaraState(page);
    const shown = () => table.evaluate((el: any) => [el.rows, el.selection, el.search, el.sort]);
    await expect.poll(state).toEqual(["", "", [], [0, 1, 2, 3, 4, 5, 6, 7], []]);

    // What the reader does, the app has
    await expect(table.locator("button.gt-i-sort").first()).toHaveCSS("cursor", "pointer");
    await table.getByRole("button", { name: "Search the table" }).click();
    await table.locator("input.gt-i-search").fill("an");
    await expect.poll(state).toEqual(["", "an", [], [1, 3], []]);
    await table.locator("tbody input[type=checkbox]").nth(3).check();
    await expect.poll(state).toEqual(["", "an", [], [1, 3], [3]]);
    await table.locator("input.gt-i-search").fill("");
    await expect.poll(state).toEqual(["", "", [], [0, 1, 2, 3, 4, 5, 6, 7], [3]]);

    // What the app sets, the table shows (the table, made again on each render, is the same one)
    await table.evaluate((el) => el.setAttribute("data-old", ""));
    await page.getByRole("button", { name: "Update" }).click();
    await expect.poll(shown).toEqual([[1, 0], [0], "", [{ column: "num", descending: true }]]);
    await expect.poll(state).toEqual(['fctr in ("one", "two")', "", ["-num"], [1, 0], [0]]);
    await expect(page.locator("gt-table[data-old]")).toHaveCount(1);

    // (And another table is shown with the app's values)
    await page.getByText("Head").click();
    await expect(page.locator("gt-table[data-old]")).toHaveCount(0);
    await expect(table).toHaveAttribute("data-gti-state", "ready");
    await expect.poll(shown).toEqual([[1, 0], [0], "", [{ column: "num", descending: true }]]);
    await expect.poll(state).toEqual(['fctr in ("one", "two")', "", ["-num"], [1, 0], [0]]);
    expect(errors).toEqual([]);
  } finally {
    server.kill();
  }
});

// (Of a data frame, and of a LazyFrame)
for (const [what, app, needs] of [
  ["", "solara_kernel_app.py", []],
  [" of a LazyFrame", "solara_lazy_app.py", ["polars"]],
] as const) {
  test(`Solara: a table${what} whose rows are the app's, a page at a time`, async ({ page }) => {
    test.skip(!has("solara", ...needs), `${["Solara", ...needs].join(" and ")} aren't all installed`);
    const { url, server } = await solara(app);
    try {
      const errors = watch(page);
      watchWidgets(page, errors);
      await page.goto(url);
      const table = page.locator("gt-table");
      await expect(table).toHaveAttribute("data-gti-state", "ready");
      const state = () => solaraState(page);
      const shown = () => table.evaluate((el: any) => [el.rows, el.pageCount, el.loading]);
      const rows = (start: number, step = 1) => Array.from({ length: 10 }, (_, i) => start + i * step);
      await expect.poll(shown).toEqual([rows(0), 500, false]);
      await expect.poll(state).toEqual([5000, [0, 1, 2], ""]);

      // (Each page, sort and search, from the app, which finds the rows)
      await table.evaluate((el: any) => {
        el.page = 3;
      });
      await expect.poll(shown).toEqual([rows(20), 500, false]);
      await table.locator("thead button.gt-i-sort").first().click();
      await table.locator("thead button.gt-i-sort").first().click();
      await expect.poll(shown).toEqual([rows(4999, -1), 500, false]);
      await expect(table.locator("tbody tr:not([hidden]) td").first()).toHaveText("4999");
      await expect.poll(state).toEqual([5000, [4999, 4998, 4997], ""]);
      await table.getByRole("button", { name: "Search the table" }).click();
      await table.locator("input.gt-i-search").fill("4998");
      await expect.poll(shown).toEqual([[4998], 1, false]);
      await expect.poll(state).toEqual([1, [4998], "4998"]);

      // (And a view the app sets, which the asks for its pages don't undo)
      await page.getByRole("button", { name: "Update" }).click();
      await expect.poll(shown).toEqual([rows(1, 2), 250, false]);
      await expect.poll(state).toEqual([2500, [1, 3, 5], ""]);
      await table.evaluate((el: any) => {
        el.page = 2;
      });
      await expect.poll(shown).toEqual([rows(21, 2), 250, false]);
      await expect.poll(state).toEqual([2500, [1, 3, 5], ""]);
      expect(errors).toEqual([]);
    } finally {
      server.kill();
    }
  });
}

test("Solara: a table in a notebook in JupyterLab, which the kernel reads and changes", async ({ page }) => {
  test.skip(!has("jupyterlab", "ipykernel", "solara"), "JupyterLab, ipykernel and Solara aren't installed");
  const errors = watch(page, /^No active debugger session$/);
  watchWidgets(page, errors);
  await lab(page, "solara.ipynb", async () => {
    await runAll(page);
    const table = page.locator(".jp-OutputArea gt-table");
    await expect(table).toHaveAttribute("data-gti-state", "ready");
    const shown = () => table.evaluate((el: any) => [el.rows, el.selection, el.search, el.sort]);
    const state = () => kernelValue(page, "[query.value, sort.value, rows.value, selection.value]");
    await expect.poll(state).toEqual(["", [], [0, 1, 2, 3, 4, 5, 6, 7], []]);

    // What the reader does, the kernel has
    await table.locator("tbody input[type=checkbox]").nth(3).check();
    await expect.poll(state).toEqual(["", [], [0, 1, 2, 3, 4, 5, 6, 7], [3]]);
    await table.locator("thead button.gt-i-sort").first().click();
    await expect.poll(state).toEqual(["", ["num"], [0, 1, 2, 3, 4, 6, 7, 5], [3]]);

    // What the kernel changes, the table shows
    await kernelRun(page, 'query.set(\'fctr in ("one", "two")\'); sort.set(["-num"]); selection.set([0])');
    await expect.poll(shown).toEqual([[1, 0], [0], "", [{ column: "num", descending: true }]]);
    await expect.poll(state).toEqual(['fctr in ("one", "two")', ["-num"], [1, 0], [0]]);
  });
  expect(errors).toEqual([]);
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

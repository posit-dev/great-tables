// Run tables through the built runtime, for Great Tables' differential tests of its queries
// (tests/test_gti_query.py), which check that Python keeps the rows that `<gt-table>` shows.
//
//   node scripts/engine.mjs < cases.jsonl
//
// Each line in is a JSON object `{"html": ...}`: a `<gt-table>`, with its spec but not the
// runtime. Each line out is `{"rows": [...], "state": ..., "warnings": [...]}`: the data rows
// shown once the table is ready, in order, the element's state, and what it warned about. With
// `"code": true`, it has `"code"` too: the view's code for each library (`toCode()`), or the
// error writing it.
//
// A line `{"parse": text}` reads a query's text (`GTI.parseQuery()`), giving `{"query": ...}` or
// `{"syntaxError": message}`, and a line `{"format": query}` writes one (`GTI.formatQuery()`),
// giving `{"text": ...}`: for checking that Great Tables reads and writes queries as the runtime does.

import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { createInterface } from "node:readline";
import { fileURLToPath } from "node:url";
import { Window } from "happy-dom";

const pkgDir = join(dirname(fileURLToPath(import.meta.url)), "..");
const runtime = readFileSync(join(pkgDir, "..", "..", "great_tables", "js", "gti.js"), "utf8");

const window = new Window({
  settings: { enableJavaScriptEvaluation: true, suppressInsecureJavaScriptEnvironmentWarning: true },
});
const document = window.document;
const warnings = [];
window.console.warn = (...args) => warnings.push(args.map(String).join(" "));
// (The runtime is strict code, so its `var GTI` stays in the eval: it's the eval's value instead)
const GTI = window.eval(`${runtime}\nGTI;`);

const tick = () => new Promise((resolve) => window.setTimeout(resolve, 0));

async function run(html, code) {
  warnings.length = 0;
  document.body.innerHTML = html;
  await tick();
  const el = document.querySelector("gt-table");
  const rows = [];
  for (const tr of el?.querySelectorAll("tbody.gt_table_body > tr") ?? []) {
    const row = el.bodyRow(tr);
    if (!tr.hidden && typeof row === "number") {
      rows.push(row);
    }
  }
  const result = { rows, state: el?.state ?? null, warnings: [...warnings] };
  if (code) {
    result.code = {};
    for (const backend of ["polars", "pandas", "narwhals"]) {
      try {
        result.code[backend] = el.toCode(backend);
      } catch (err) {
        result.code[backend] = { error: String(err?.message ?? err) };
      }
    }
  }
  return result;
}

function parse(text) {
  try {
    return { query: GTI.parseQuery(text) };
  } catch (err) {
    // (The runtime's `SyntaxError`, of the window's realm)
    if (err?.name === "SyntaxError") {
      return { syntaxError: err.message };
    }
    throw err;
  }
}

const lines = createInterface({ input: process.stdin, crlfDelay: Infinity });
for await (const line of lines) {
  if (line.trim() === "") {
    continue;
  }
  let result;
  try {
    const input = JSON.parse(line);
    if ("parse" in input) {
      result = parse(input.parse);
    } else if ("format" in input) {
      result = { text: GTI.formatQuery(input.format) };
    } else {
      result = await run(input.html, input.code === true);
    }
  } catch (err) {
    result = { error: String(err?.stack ?? err) };
  }
  process.stdout.write(`${JSON.stringify(result)}\n`);
}
await window.happyDOM.close();

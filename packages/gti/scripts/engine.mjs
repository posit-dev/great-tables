// Run tables through the built runtime, for Great Tables' differential tests of its queries
// (tests/test_gti_query.py), which check that Python keeps the rows that `<gt-table>` shows.
//
//   node scripts/engine.mjs < cases.jsonl
//
// Each line in is a JSON object `{"html": ...}`: a `<gt-table>`, with its spec but not the
// runtime. Each line out is `{"rows": [...], "state": ..., "warnings": [...]}`: the data rows
// shown once the table is ready, in order, the element's state, and what it warned about.

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
window.eval(runtime);

const tick = () => new Promise((resolve) => window.setTimeout(resolve, 0));

async function run(html) {
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
  return { rows, state: el?.state ?? null, warnings: [...warnings] };
}

const lines = createInterface({ input: process.stdin, crlfDelay: Infinity });
for await (const line of lines) {
  if (line.trim() === "") {
    continue;
  }
  let result;
  try {
    result = await run(JSON.parse(line).html);
  } catch (err) {
    result = { error: String(err?.stack ?? err) };
  }
  process.stdout.write(`${JSON.stringify(result)}\n`);
}
await window.happyDOM.close();

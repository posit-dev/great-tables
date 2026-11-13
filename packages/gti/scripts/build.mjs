// Build the GTI runtime into great_tables/js/gti.{js,css}, the template of a stacked table's own
// CSS into great_tables/js/gti-stack.css, and the glue of a table shown as an anywidget into
// great_tables/js/gti-widget.js, of tables in a Shiny app into great_tables/js/gti-shiny.js, and of
// a table shown as a Streamlit component into great_tables/js/gti-streamlit.js.
//
//   node scripts/build.mjs           build and write the bundle
//   node scripts/build.mjs --check   build in memory and fail if the committed bundle is stale or
//                                    over the size budget (run in CI)
//
// The built files are committed so that Python contributors and users never need Node.

import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";
import { gzipSync } from "node:zlib";
import * as esbuild from "esbuild";
import { mangledNames } from "./mangle.mjs";

// Budget for the core runtime (JS and CSS together), minified and gzipped.
const BUDGET_BYTES = 70 * 1024;

const pkgDir = join(dirname(fileURLToPath(import.meta.url)), "..");
const outDir = join(pkgDir, "..", "..", "great_tables", "js");
const pkg = JSON.parse(readFileSync(join(pkgDir, "package.json"), "utf8"));

const banner = `/*! GTI ${pkg.version} | MIT License | generated from packages/gti, do not edit */`;

const shared = {
  bundle: true,
  minify: true,
  write: false,
  logLevel: "warning",
  absWorkingDir: pkgDir,
};

async function buildOne(options) {
  const result = await esbuild.build({ ...shared, ...options });
  const text = result.outputFiles[0].text;
  return text.endsWith("\n") ? text : text + "\n";
}

const js = {
  ...shared,
  entryPoints: ["src/index.ts"],
  outfile: "gti.js",
  format: "iife",
  globalName: "GTI",
  target: "es2020",
  define: { __GTI_VERSION__: JSON.stringify(pkg.version) },
  banner: { js: banner },
};
// (Private members' names, shortened: see scripts/mangle.mjs)
const mangled = await mangledNames(pkgDir, js);

const outputs = {
  "gti.js": await buildOne({ ...js, mangleProps: new RegExp(`^(?:${mangled.join("|")})$`) }),
  "gti.css": await buildOne({
    entryPoints: ["src/gti.css"],
    outfile: "gti.css",
    banner: { css: banner },
  }),
  // (Not the runtime's: producers include it with each table that can be stacked)
  "gti-stack.css": await buildOne({
    entryPoints: ["src/stack.css"],
    outfile: "gti-stack.css",
    banner: { css: banner },
  }),
  // (Nor this: the module a widget runs after the runtime; see src/widget.ts)
  "gti-widget.js": await buildOne({
    entryPoints: ["src/widget.ts"],
    outfile: "gti-widget.js",
    format: "esm",
    target: "es2020",
    banner: { js: banner },
  }),
  // (Nor this: the script a Shiny app has once, after the runtime; see src/shiny.ts)
  "gti-shiny.js": await buildOne({
    entryPoints: ["src/shiny.ts"],
    outfile: "gti-shiny.js",
    format: "iife",
    target: "es2020",
    banner: { js: banner },
  }),
  // (Nor this: the module a Streamlit component runs after the runtime; see src/streamlit.ts)
  "gti-streamlit.js": await buildOne({
    entryPoints: ["src/streamlit.ts"],
    outfile: "gti-streamlit.js",
    format: "esm",
    target: "es2020",
    banner: { js: banner },
  }),
};

const check = process.argv.includes("--check");
const problems = [];
let total = 0;

for (const [name, text] of Object.entries(outputs)) {
  const path = join(outDir, name);
  const gzipped = gzipSync(text, { level: 9 }).length;
  const runtime = name === "gti.js" || name === "gti.css";
  if (runtime) {
    total += gzipped;
  }
  console.log(
    `${relative(process.cwd(), path)}: ${text.length} B, ${gzipped} B gzipped${runtime ? "" : " (not in the budget)"}`,
  );

  if (check) {
    let committed = null;
    try {
      committed = readFileSync(path, "utf8");
    } catch {
      // Reported below.
    }
    if (committed !== text) {
      problems.push(`${name} is missing or stale; run \`npm run build\` in packages/gti and commit it`);
    }
  } else {
    writeFileSync(path, text);
  }
}

console.log(`total: ${total} B gzipped (budget ${BUDGET_BYTES} B)`);
if (total > BUDGET_BYTES) {
  problems.push(`runtime is ${total} B gzipped, over the ${BUDGET_BYTES} B budget`);
}

if (problems.length > 0) {
  for (const problem of problems) {
    console.error(`error: ${problem}`);
  }
  process.exit(1);
}

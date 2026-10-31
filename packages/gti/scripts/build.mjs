// Build the GTI runtime into great_tables/js/gti.{js,css}.
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

// Budget for the core runtime (JS and CSS together), minified and gzipped.
const BUDGET_BYTES = 30 * 1024;

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

const outputs = {
  "gti.js": await buildOne({
    entryPoints: ["src/index.ts"],
    outfile: "gti.js",
    format: "iife",
    globalName: "GTI",
    target: "es2020",
    define: { __GTI_VERSION__: JSON.stringify(pkg.version) },
    banner: { js: banner },
  }),
  "gti.css": await buildOne({
    entryPoints: ["src/gti.css"],
    outfile: "gti.css",
    banner: { css: banner },
  }),
};

const check = process.argv.includes("--check");
const problems = [];
let total = 0;

for (const [name, text] of Object.entries(outputs)) {
  const path = join(outDir, name);
  const gzipped = gzipSync(text, { level: 9 }).length;
  total += gzipped;
  console.log(`${relative(process.cwd(), path)}: ${text.length} B, ${gzipped} B gzipped`);

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

// The names of the runtime's private members that the build can shorten (esbuild's `mangleProps`),
// for size: TypeScript's `private` is gone by then, so minifying keeps them as they are.
//
// esbuild renames a property everywhere it's a property, on any object, so a name is shortened
// only if it can't be anything else: it's declared `private` (in a class in src/), and nowhere in
// the source is it declared otherwise (a public member, an interface's, an object's key), and in
// the bundle, without comments, every use of it is `this.<name>` or the declaration of a method.
// That leaves out the names that are also the spec's keys, the element's API, the DOM's, strings
// or local variables, which is more than it need, but never less. The names the browser tests read
// from the element (`(node as any).matchCount`) are left as they are too.

import { readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import * as esbuild from "esbuild";

// Names the browser calls by name, never shortened
const RESERVED = new Set([
  "constructor",
  "connectedCallback",
  "disconnectedCallback",
  "adoptedCallback",
  "attributeChangedCallback",
  "observedAttributes",
  "handleEvent",
  "toJSON",
  "toString",
  "valueOf",
  "then",
]);

const NAME = "[A-Za-z_$][\\w$]*";
const MODIFIERS = "(?:(?:public|protected|private|static|readonly|override|declare|abstract|async|get|set)\\s+)*";
const escape = (name) => name.replace(/\$/g, "\\$");
// (Before a method's name, on its line, as esbuild writes them)
const METHOD = /^[ \t]+(?:(?:static|async|get|set)\s+)*\*?\s*$/;
const THIS = /(?<![\w$.])this\.$/;

/**
 * The private members' names that are safe to shorten, sorted.
 *
 * @param {string[]} sources the TypeScript source files' text
 * @param {string} bundle the bundle, built without minifying (so without comments)
 * @param {Iterable<string>} [kept] names to leave as they are, besides those always kept
 * @returns {string[]}
 */
export function mangleable(sources, bundle, kept = []) {
  const reserved = new Set([...RESERVED, ...kept]);
  const ts = sources.join("\n");
  const declared = new RegExp(`^[ \\t]+private\\s+${MODIFIERS}\\*?\\s*(${NAME})`, "gm");
  const names = new Set(Array.from(ts.matchAll(declared), (match) => match[1]));
  return [...names]
    .filter((name) => !reserved.has(name))
    .filter((name) => {
      const word = escape(name);
      // (A line that starts with it, in a declaration's place, that isn't the private one)
      const other = new RegExp(`^[ \\t]*(?!private\\b)${MODIFIERS}\\*?\\s*${word}\\s*[?!]?\\s*[(=;:<,}]`, "m");
      if (other.test(ts)) {
        return false;
      }
      const uses = new RegExp(`(?<![\\w$])${word}(?![\\w$])`, "g");
      for (const use of bundle.matchAll(uses)) {
        const before = bundle.slice(bundle.lastIndexOf("\n", use.index) + 1, use.index);
        if (!THIS.test(before) && !(METHOD.test(before) && bundle[use.index + name.length] === "(")) {
          return false;
        }
      }
      return true;
    })
    .sort();
}

/**
 * The names to shorten in the runtime that `options` build (in `pkgDir`).
 *
 * @param {string} pkgDir
 * @param {import("esbuild").BuildOptions} options
 * @returns {Promise<string[]>}
 */
export async function mangledNames(pkgDir, options) {
  const read = (dir) =>
    readdirSync(join(pkgDir, dir))
      .filter((file) => file.endsWith(".ts"))
      .map((file) => readFileSync(join(pkgDir, dir, file), "utf8"));
  const tests = read("e2e").join("\n");
  const kept = Array.from(tests.matchAll(new RegExp(`\\bas any\\)\\.(${NAME})`, "g")), (match) => match[1]);
  const result = await esbuild.build({
    ...options,
    minify: false,
    legalComments: "none",
    banner: {},
    write: false,
  });
  return mangleable(read("src"), result.outputFiles[0].text, kept);
}

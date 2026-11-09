// @vitest-environment node
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { describe, expect, it } from "vitest";

const SRC = join(dirname(fileURLToPath(import.meta.url)), "..", "src");

// A stylesheet's rules, without its comments
const rules = (name: string) => readFileSync(join(SRC, name), "utf8").replace(/\/\*[\s\S]*?\*\//g, "");

describe("the stylesheets", () => {
  // (Any rule with `:has()` makes Chromium slow to move a body's rows, matching or not: putting
  // 10,000 back took 1.9 s with one, 14 ms without)
  it.each(["gti.css", "stack.css"])("%s has no :has()", (name) => {
    expect(rules(name)).not.toMatch(/:has\(/);
  });
});

// @vitest-environment node
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { describe, expect, it } from "vitest";
import { mangleable, mangledNames } from "../scripts/mangle.mjs";

const source = `
class Table {
  private rows: number[] = [];
  private count = 0;
  private async draw(): Promise<void> {}
  private get shown(): number {
    return this.count;
  }
}
`;

const bundle = `
  class Table {
    constructor() {
      this.rows = [];
      this.count = 0;
    }
    async draw() {
    }
    get shown() {
      return this.count;
    }
  }
`;

describe("mangleable()", () => {
  it("takes private members used only on `this`", () => {
    expect(mangleable([source], bundle)).toEqual(["count", "draw", "rows", "shown"]);
  });

  it("leaves a name declared otherwise in the source", () => {
    const other = "interface Spec {\n  rows: number;\n}\nconst x = {\n  count: 1,\n};\nclass B {\n  draw() {}\n}";
    expect(mangleable([source, other], bundle)).toEqual(["shown"]);
  });

  it("leaves a name used other than on `this` in the bundle", () => {
    expect(mangleable([source], `${bundle}\nnode.rows.push(1);`)).toEqual(["count", "draw", "shown"]);
    expect(mangleable([source], `${bundle}\nconst { count } = spec;`)).toEqual(["draw", "rows", "shown"]);
    expect(mangleable([source], `${bundle}\nif ("draw" in el) {}`)).toEqual(["count", "rows", "shown"]);
    expect(mangleable([source], `${bundle}\nconst shown = 1;`)).toEqual(["count", "draw", "rows"]);
    expect(mangleable([source], `${bundle}\nthis?.rows;`)).toEqual(["count", "draw", "shown"]);
  });

  it("leaves the names it's told to keep, and the browser's", () => {
    const element = "class El {\n  private connectedCallback(): void {}\n  private rows = 1;\n}";
    const built = "  connectedCallback() {\n  }\n  this.rows = 1;";
    expect(mangleable([element], built)).toEqual(["rows"]);
    expect(mangleable([element], built, ["rows"])).toEqual([]);
  });
});

describe("mangledNames()", () => {
  it("leaves the runtime's API, and the names the browser tests read", async () => {
    const pkgDir = join(dirname(fileURLToPath(import.meta.url)), "..");
    const names = await mangledNames(pkgDir, {
      entryPoints: ["src/index.ts"],
      bundle: true,
      format: "iife",
      globalName: "GTI",
      target: "es2020",
      define: { __GTI_VERSION__: '"0.0.0"' },
      absWorkingDir: pkgDir,
      logLevel: "warning",
    });
    expect(names).toContain("makeGroupToken");
    expect(names.length).toBeGreaterThan(100);
    for (const name of ["filter", "toCode", "connectedCallback", "matchCount", "state", "spec"]) {
      expect(names).not.toContain(name);
    }
  });
});

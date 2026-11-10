import { readFileSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import { places, ramp, textColor } from "../src/color";
import type { ColorSpec } from "../src/spec";

// The colors `data_color()` makes (written by `test/make_colors.py`)
const made = JSON.parse(readFileSync(join(__dirname, "colors.json"), "utf8")) as {
  cases: { name: string; spec: ColorSpec; keep: number[]; expected: Record<string, [string, string | null]> }[];
  ramps: { palette: string[]; colors: string[]; apca: string[]; wcag: string[]; alpha: string[] }[];
};

describe("colors as data_color() makes them", () => {
  it.each(made.ramps)("mixes a palette in CIELAB, with the text that contrasts more: $palette", (expected) => {
    const color = ramp(expected.palette);
    const colors = Array.from({ length: 41 }, (_, i) => color(i / 40));
    expect(colors).toEqual(expected.colors);
    expect(colors.map((fill) => textColor(fill, "apca"))).toEqual(expected.apca);
    expect(colors.map((fill) => textColor(fill, "wcag"))).toEqual(expected.wcag);
    // (Over white, with an alpha)
    expect(colors.map((fill) => textColor(`${fill}66`, "apca"))).toEqual(expected.alpha);
  });

  it.each(made.cases)("colors the rows kept as data_color() colors them alone: $name", ({ spec, keep, expected }) => {
    const color = ramp(spec.palette);
    const at = places(spec, (row) => keep.includes(row));
    const found: Record<string, [string, string | null]> = {};
    spec.rows.forEach((row, k) => {
      const t = at[k];
      if (t != null) {
        const fill = color(t) + spec.alpha;
        found[row] = [fill, spec.text === null ? null : textColor(fill, spec.text)];
      }
    });
    expect(found).toEqual(expected);
  });

  it("leaves out the rows not kept", () => {
    const spec = made.cases[0]?.spec as ColorSpec;
    expect(places(spec, () => false).every((t) => t === null)).toBe(true);
  });
});

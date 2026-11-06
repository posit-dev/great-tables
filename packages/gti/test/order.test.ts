import { describe, expect, it } from "vitest";
import { columnRuns, orderRuns } from "../src/order";
import { type Spec } from "../src/spec";

// A spec with these columns (`id`, then whether it's reorderable, and its pin), and spanners
function spec(columns: [string | null, boolean, ("start" | "end")?][], spanners: Spec["spanners"] = []): Spec {
  return {
    columns: columns.map(([id, reorderable, pin], i) => ({
      id,
      role: i === 0 && id === "stub" ? "stub" : "data",
      reorderable,
      ...(pin === undefined ? {} : { pin }),
    })),
    spanners,
  } as unknown as Spec;
}

describe("columnRuns", () => {
  it("has the stretches of reorderable data columns next to one another, of two or more", () => {
    expect(
      columnRuns(
        spec([
          ["stub", true],
          ["a", true],
          ["b", true],
          ["c", false],
          ["d", true],
          ["e", true],
          ["f", true],
          ["g", false],
          ["h", true],
        ]),
      ),
    ).toEqual([
      [1, 2],
      [4, 5, 6],
    ]);
    expect(columnRuns(spec([["a", false], ["b", false]]))).toEqual([]);
  });

  it("splits a stretch where the spanners over it, or its pin, change", () => {
    const spanners = [
      { id: "s", level: 1, columns: ["a", "b"], header: null },
      { id: "t", level: 2, columns: ["a", "b", "c", "d"], header: null },
    ] as unknown as Spec["spanners"];
    expect(
      columnRuns(
        spec(
          [
            ["a", true],
            ["b", true],
            ["c", true],
            ["d", true],
            ["e", true, "end"],
            ["f", true, "end"],
            ["g", true],
          ],
          spanners,
        ),
      ),
    ).toEqual([
      [0, 1],
      [2, 3],
      [4, 5],
    ]);
  });
});

describe("orderRuns", () => {
  const RUNS = [
    ["a", "b", "c"],
    ["d", "e"],
  ];

  it("puts each run's columns in the order given, then those left out in the author's", () => {
    expect(orderRuns(["c", "a", "b", "e", "d"], RUNS)).toEqual(["c", "a", "b", "e", "d"]);
    expect(orderRuns(["c"], RUNS)).toEqual(["c", "a", "b", "d", "e"]);
    expect(orderRuns(["e", "b"], RUNS)).toEqual(["b", "a", "c", "e", "d"]);
    expect(orderRuns([], RUNS)).toEqual(["a", "b", "c", "d", "e"]);
  });

  it("goes by a column's first place, and leaves out those of no run", () => {
    expect(orderRuns(["b", "x", "a", "b"], RUNS)).toEqual(["b", "a", "c", "d", "e"]);
    expect(orderRuns(["a"], [])).toEqual([]);
  });
});

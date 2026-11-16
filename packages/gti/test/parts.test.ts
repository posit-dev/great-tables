import { describe, expect, it } from "vitest";
import { type Box, type Part, placeParts, union } from "../src/parts";

const box = (left: number, top: number, right: number, bottom: number): Box => ({ left, top, right, bottom });
const size = { width: 40, height: 10 };
const bounds = box(0, 0, 400, 300);

describe("union()", () => {
  it("is the box around the boxes, or null for none", () => {
    expect(union([])).toBeNull();
    expect(union([box(10, 20, 30, 40), box(0, 30, 20, 50)])).toEqual(box(0, 20, 30, 50));
  });
});

describe("placeParts()", () => {
  it("puts a name at its first place, centred on its part, with a line across the gap", () => {
    const [placed] = placeParts([{ name: "a", boxes: [box(100, 100, 200, 120)], places: ["above"] }], [size], bounds);
    expect(placed?.label).toEqual(box(130, 86, 170, 96));
    expect(placed?.line).toEqual(box(149.5, 96, 150.5, 100));
  });

  it("stacks a name above another, rather than over it", () => {
    const parts: Part[] = [
      { name: "a", boxes: [box(100, 100, 200, 120)], places: ["above"] },
      { name: "b", boxes: [box(110, 100, 190, 120)], places: ["above"] },
    ];
    const [a, b] = placeParts(parts, [size, size], bounds);
    expect(a?.label.top).toBe(86);
    expect(b?.label).toEqual(box(130, 72, 170, 82));
    expect(b?.line).toEqual(box(149.5, 82, 150.5, 100));
  });

  it("goes to a later place to keep clear of the other parts", () => {
    const parts: Part[] = [
      { name: "a", boxes: [box(100, 100, 200, 120)], places: ["left", "right"] },
      { name: "b", boxes: [box(50, 100, 95, 120)], places: ["below"] },
    ];
    const [a] = placeParts(parts, [size, size], bounds);
    expect(a?.label).toEqual(box(204, 105, 244, 115));
    expect(a?.line).toEqual(box(200, 109.5, 204, 110.5));
  });

  it("keeps a name within bounds, or else at its first place", () => {
    const [edge, out] = placeParts(
      [
        { name: "edge", boxes: [box(0, 100, 20, 120)], places: ["above"] },
        { name: "out", boxes: [box(100, 0, 200, 20)], places: ["above"] },
      ],
      [size, size],
      bounds,
    );
    // (Moved along, to start at the bounds)
    expect(edge?.label.left).toBe(0);
    // (Above the bounds, with no other place to go)
    expect(out?.label.bottom).toBe(-4);
  });

  it("puts a name over its part from the start, when that's its place", () => {
    const [placed] = placeParts([{ name: "a", boxes: [box(100, 100, 200, 200)], places: ["over"] }], [size], bounds);
    expect(placed?.label).toEqual(box(104, 104, 144, 114));
    expect(placed?.line).toBeNull();
  });

  it("would rather overlap another part than another name", () => {
    const parts: Part[] = [
      { name: "a", boxes: [box(100, 40, 200, 120)], places: ["below"] },
      { name: "b", boxes: [box(100, 124, 200, 300)], places: ["above"] },
    ];
    // (Every place for each overlaps the other's box: each takes the first clear of the names)
    const [a, b] = placeParts(parts, [size, size], bounds);
    expect(a?.label).toEqual(box(130, 124, 170, 134));
    expect(b?.label).toEqual(box(130, 110, 170, 120));
  });
});

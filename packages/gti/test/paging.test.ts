import { describe, expect, it } from "vitest";
import { pageCount, pageItems, pageSizeChoices } from "../src/index";

describe("pageCount()", () => {
  it.each([
    [0, 10, 1],
    [1, 10, 1],
    [10, 10, 1],
    [11, 10, 2],
    [310, 25, 13],
    [5, null, 1],
  ])("%d rows, %s to a page, is %d pages", (rows, size, expected) => {
    expect(pageCount(rows, size)).toBe(expected);
  });
});

describe("pageSizeChoices()", () => {
  it("adds the page size to the choices, in order and without repeats", () => {
    expect(pageSizeChoices(10, [10, 25, 50])).toEqual([10, 25, 50]);
    expect(pageSizeChoices(5, [10, 25])).toEqual([5, 10, 25]);
    expect(pageSizeChoices(30, [50, 10, 10, 25])).toEqual([10, 25, 30, 50]);
  });
});

describe("pageItems()", () => {
  it("lists every page when there are 7 or fewer", () => {
    expect(pageItems(1, 1)).toEqual([1]);
    expect(pageItems(3, 7)).toEqual([1, 2, 3, 4, 5, 6, 7]);
  });

  it.each([
    [1, [1, 2, 3, 4, 5, null, 20]],
    [4, [1, 2, 3, 4, 5, null, 20]],
    [5, [1, null, 4, 5, 6, null, 20]],
    [10, [1, null, 9, 10, 11, null, 20]],
    [16, [1, null, 15, 16, 17, null, 20]],
    [17, [1, null, 16, 17, 18, 19, 20]],
    [20, [1, null, 16, 17, 18, 19, 20]],
  ])("gives page %d of 20 with its neighbours, the ends, and gaps", (page, expected) => {
    expect(pageItems(page, 20)).toEqual(expected);
  });

  it("always has 7 items, with the current page, the first and the last", () => {
    for (const count of [8, 9, 12, 50]) {
      for (let page = 1; page <= count; page++) {
        const items = pageItems(page, count);
        expect(items).toHaveLength(7);
        expect(items).toContain(page);
        expect(items[0]).toBe(1);
        expect(items[6]).toBe(count);
        // Pages in order, and a gap only where pages are left out
        items.forEach((item, i) => {
          const before = items[i - 1];
          const after = items[i + 1];
          if (item === null) {
            expect((after as number) - (before as number)).toBeGreaterThan(1);
          } else if (typeof before === "number") {
            expect(item).toBe(before + 1);
          }
        });
      }
    }
  });
});

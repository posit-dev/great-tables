import { describe, expect, it } from "vitest";
import { BINS, Profile, TOP, timeOf } from "../src/profile";
import type { ProfileSpec } from "../src/spec";

const histogram = (values: ProfileSpec["values"]): ProfileSpec => ({ column: "c", plot: "histogram", values });
const TOP_SPEC: ProfileSpec = { column: "c", plot: "top", values: null };

// The bars' ranges
const ranges = (profile: Profile) => profile.bars.map((bar) => [bar.low, bar.high]);

describe("timeOf()", () => {
  it("reads dates, and dates and times, without an offset as UTC", () => {
    expect(timeOf("2015-06-15")).toBe(Date.UTC(2015, 5, 15));
    expect(timeOf("2015-06-15T09:30:00.123456789")).toBe(Date.UTC(2015, 5, 15, 9, 30, 0, 123));
    expect(timeOf("0050-01-01")).toBe(new Date("0050-01-01T00:00:00Z").getTime());
  });

  it("reads them with an offset at their time, and other text as NaN", () => {
    expect(timeOf("2015-06-15T09:30:00+02:00")).toBe(Date.UTC(2015, 5, 15, 7, 30));
    expect(timeOf("June")).toBeNaN();
  });
});

describe("Profile", () => {
  it("bins numbers into equal ranges, from the lowest to the highest", () => {
    // (Ranks of 0, 2.5, 10 and 100)
    const profile = new Profile(histogram([0, 2.5, 10, 100]), [0, 1, 2, 3, 3, null]);
    expect(profile.bars).toHaveLength(BINS);
    expect(ranges(profile)[0]).toEqual([0, 5]);
    expect(ranges(profile)[BINS - 1]).toEqual([95, 100]);
    expect(profile.times).toBe(false);
    const counts = profile.count(null);
    expect(counts.bars[0]).toBe(2);
    expect(counts.bars[2]).toBe(1);
    expect(counts.bars[BINS - 1]).toBe(2);
    expect(counts).toMatchObject({ rows: 6, missing: 1, low: 0, high: 3, distinct: 4 });
  });

  it("gives a bin to each whole number, if they're few, with its rank", () => {
    const profile = new Profile(histogram([3, 4, 7]), [2, 0, 1]);
    expect(ranges(profile)).toEqual([
      [3, 3],
      [4, 4],
      [5, 5],
      [6, 6],
      [7, 7],
    ]);
    expect(profile.bars.map((bar) => bar.rank)).toEqual([0, 1, -1, -1, 2]);
    expect(profile.count(null).bars).toEqual([1, 1, 0, 0, 1]);
  });

  it("gives whole numbers far apart equal ranges", () => {
    const profile = new Profile(histogram([0, 40]), [0, 1]);
    expect(profile.bars).toHaveLength(BINS);
    expect(ranges(profile)[0]).toEqual([0, 2]);
  });

  it("has one bin for one value", () => {
    const profile = new Profile(histogram([2.5]), [0, 0, null]);
    expect(profile.bars).toEqual([{ rank: 0, low: 2.5, high: 2.5 }]);
    expect(profile.count(null)).toMatchObject({ bars: [2], missing: 1 });
  });

  it("has no bins without values, every row missing", () => {
    const profile = new Profile(histogram([null]), [0, null]);
    expect(profile.bars).toEqual([]);
    expect(profile.count(null)).toMatchObject({ bars: [], rows: 2, missing: 2, low: -1, distinct: 0 });
  });

  it("bins dates by the day, if they're few, or else equal ranges of time", () => {
    const days = new Profile(histogram(["2015-06-15", "2015-06-17"]), [0, 1]);
    expect(days.times).toBe(true);
    expect(ranges(days)).toHaveLength(3);
    expect(days.bars[0]).toEqual({ rank: 0, low: Date.UTC(2015, 5, 15), high: Date.UTC(2015, 5, 15) });
    const times = new Profile(histogram(["2015-06-15T00:00", "2015-06-15T10:00"]), [0, 1]);
    expect(times.bars).toHaveLength(BINS);
    expect(times.bars[0]?.high).toBe(Date.UTC(2015, 5, 15, 0, 30));
  });

  it("counts a value NaN stood for (null) as missing", () => {
    const profile = new Profile(histogram([1, 2, null]), [0, 1, 2]);
    expect(profile.count(null)).toMatchObject({ rows: 3, missing: 1, high: 1, distinct: 2 });
  });

  it("counts only the rows kept, in the same bins", () => {
    const profile = new Profile(histogram([3, 4, 7]), [2, 0, 1, null]);
    const counts = profile.count(Uint8Array.from([0, 1, 0, 1]));
    expect(counts).toEqual({ bars: [1, 0, 0, 0, 0], rows: 2, missing: 1, low: 0, high: 0, distinct: 1 });
    expect(profile.count(new Uint8Array(4))).toMatchObject({ rows: 0, low: -1, high: -1 });
  });

  it("shows the values most rows have, first of those with as many, and a bar of the others", () => {
    // (Rank 3 in 3 rows, 1 in 2, the rest in 1)
    const ranks = [3, 1, 3, 0, 2, 3, 1, 4, 5, 6];
    const profile = new Profile(TOP_SPEC, ranks);
    expect(profile.bars.map((bar) => bar.rank)).toEqual([3, 1, 0, 2, 4, -1]);
    expect(profile.bars).toHaveLength(TOP + 1);
    expect(profile.others).toBe(2);
    expect(profile.rowOf[3]).toBe(0);
    expect(profile.count(null)).toMatchObject({ bars: [3, 2, 1, 1, 1, 2], distinct: 7 });
  });

  it("shows every value, if there's only one more than it shows", () => {
    const profile = new Profile(TOP_SPEC, [0, 1, 2, 3, 4, 5, null]);
    expect(profile.bars.map((bar) => bar.rank)).toEqual([0, 1, 2, 3, 4, 5]);
    expect(profile.others).toBe(0);
    expect(profile.count(null)).toMatchObject({ missing: 1, rows: 7 });
  });
});

/**
 * Column profiles: under a column's label, a plot of the values in the rows the search and filters
 * keep (a histogram of its numbers or dates, or bars for its most common values), and how many of
 * them are missing.
 *
 * A profile's bars are set by the whole column (a histogram's bins span its range, and "top" has
 * the values most rows have), so that they stay put as rows are filtered; only their counts change.
 */

import { dateKey } from "./filter";
import type { ProfileSpec } from "./spec";

/** The most bins a histogram has, and the most values "top" shows (before a bar for the others). */
export const BINS = 20;
export const TOP = 5;

const DAY = 864e5;

/**
 * A bar: of a histogram's bin, from `low` up to `high` (numbers, or times in ms), or of one of
 * "top"'s values (`low` and `high` NaN), or its other values (`rank` -1). A bar of one value (all
 * of "top"'s but the others', and a histogram's whole number or day, if a row has it) has its rank.
 */
export interface Bar {
  rank: number;
  low: number;
  high: number;
}

/** A profile's counts, of the rows kept. */
export interface Counts {
  /** Each bar's rows. */
  bars: number[];
  /** The rows kept, and those of them with a missing value (or one a histogram can't place). */
  rows: number;
  missing: number;
  /** The lowest and highest ranks of the rows kept (-1 without any), and how many there are. */
  low: number;
  high: number;
  distinct: number;
}

/**
 * The time (ms since 1970) ISO 8601 text gives: a date, or a date and time, without an offset as
 * UTC; NaN for text that isn't one.
 */
export function timeOf(text: string): number {
  const key = dateKey(text);
  if (key === null) {
    return Date.parse(text);
  }
  const [year, month, day, hour, minute, second, nanos] = key.split(/[-T:.]/).map(Number) as number[];
  const date = new Date(0);
  // (Not `Date.UTC()`, which takes years before 100 to be 1900 and after)
  date.setUTCFullYear(year as number, (month as number) - 1, day);
  date.setUTCHours(hour as number, minute, second, Math.floor((nanos as number) / 1e6));
  return date.getTime();
}

export class Profile {
  /** The bars, in order. */
  readonly bars: Bar[] = [];
  /** Whether a histogram's values are times (in ms), rather than numbers. */
  readonly times: boolean;
  /** How many values "top"'s last bar has, if it's of the others; else 0. */
  readonly others: number = 0;
  /** A data row with each rank (-1 for none). */
  readonly rowOf: Int32Array;
  // Each rank's bar (-1 for none, for a value a histogram can't place)
  private readonly barOf: Int32Array;

  constructor(
    readonly spec: ProfileSpec,
    private readonly ranks: readonly (number | null)[],
  ) {
    const values = spec.values;
    const distinct = values?.length ?? ranks.reduce<number>((most, rank) => Math.max(most, (rank ?? -1) + 1), 0);
    this.barOf = new Int32Array(distinct).fill(-1);
    this.rowOf = new Int32Array(distinct).fill(-1);
    const counts = new Array<number>(distinct).fill(0);
    ranks.forEach((rank, row) => {
      if (rank !== null) {
        counts[rank] = (counts[rank] as number) + 1;
        if (this.rowOf[rank] === -1) {
          this.rowOf[rank] = row;
        }
      }
    });
    this.times = values?.some((value) => typeof value === "string") ?? false;

    if (values === null) {
      // The values most rows have (the first of those with as many), then the others
      const order = counts.map((_, rank) => rank).sort((a, b) => (counts[b] as number) - (counts[a] as number) || a - b);
      const shown = order.length > TOP + 1 ? TOP : order.length;
      order.forEach((rank, i) => {
        this.barOf[rank] = Math.min(i, shown);
        if (i <= shown) {
          this.bars.push({ rank: i < shown ? rank : -1, low: NaN, high: NaN });
        }
      });
      this.others = order.length - shown;
      return;
    }

    const xs = values.map((value) => (typeof value === "number" ? value : typeof value === "string" ? timeOf(value) : NaN));
    let low = Infinity;
    let high = -Infinity;
    for (const x of xs) {
      if (Number.isFinite(x)) {
        low = Math.min(low, x);
        high = Math.max(high, x);
      }
    }
    if (low > high) {
      return;
    }
    // (A bin per whole number, or day, if they're few; else as many as fit, of equal width)
    const unit = this.times ? DAY : 1;
    const whole = high - low < BINS * unit && xs.every((x) => !Number.isFinite(x) || Number.isInteger(x / unit));
    const n = whole ? Math.round((high - low) / unit) + 1 : low === high ? 1 : BINS;
    const width = whole ? unit : (high - low) / n;
    for (let i = 0; i < n; i++) {
      this.bars.push({ rank: -1, low: low + i * width, high: whole ? low + i * width : i === n - 1 ? high : low + (i + 1) * width });
    }
    xs.forEach((x, rank) => {
      if (Number.isFinite(x)) {
        const i = width === 0 ? 0 : Math.min(n - 1, Math.floor((x - low) / width));
        const bar = this.bars[i] as Bar;
        this.barOf[rank] = i;
        if (bar.low === bar.high) {
          bar.rank = rank;
        }
      }
    });
  }

  /** The counts of the rows `kept` has (all of them, for `null`). */
  count(kept: Uint8Array | null): Counts {
    const counts: Counts = { bars: this.bars.map(() => 0), rows: 0, missing: 0, low: -1, high: -1, distinct: 0 };
    const seen = new Uint8Array(this.barOf.length);
    this.ranks.forEach((rank, row) => {
      if (kept !== null && kept[row] !== 1) {
        return;
      }
      counts.rows++;
      const bar = rank === null ? -1 : (this.barOf[rank] ?? -1);
      if (rank === null || bar < 0) {
        counts.missing++;
        return;
      }
      counts.bars[bar] = (counts.bars[bar] as number) + 1;
      if (seen[rank] === 0) {
        seen[rank] = 1;
        counts.distinct++;
      }
      if (counts.low === -1 || rank < counts.low) {
        counts.low = rank;
      }
      counts.high = Math.max(counts.high, rank);
    });
    return counts;
  }
}

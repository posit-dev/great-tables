/**
 * Column profiles: under a column's label, a plot of the values in the rows the search and filters
 * keep (a histogram of its numbers or dates, or a strip of its most common values), and how many of
 * them are missing.
 *
 * A profile's bars are set by the whole column (a histogram's bins span its range, and "top" has
 * the values most rows have), so that they stay put as rows are filtered; only their counts change.
 * A column with missing values has a bar of them too, last.
 */

import { dateKey } from "./filter";
import type { ProfileSpec } from "./spec";

/** The most bins a histogram has, and the most values "top" shows (before bars for the others). */
export const BINS = 20;
export const TOP = 5;

const DAY = 864e5;

/**
 * What a bar is of: a histogram's bin, or one of "top"'s values (`"value"`); "top"'s other values
 * in more than one row each (`"others"`), or in one row each (`"unique"`); or the missing values.
 */
export type BarKind = "value" | "others" | "unique" | "missing";

/**
 * A bar: of a histogram's bin, from `low` up to `high` (numbers, or times in ms), or else `low` and
 * `high` NaN. A bar of one value (each of "top"'s values, and a histogram's whole number or day,
 * if a row has it) has its rank; the others' rank is -1.
 */
export interface Bar {
  kind: BarKind;
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

// (A date and time, then its offset, as Python writes a time zone's: "+02:00", "-05:00", or with
// seconds)
const ZONED = /^(.*T.*?)(?:Z|[+-]\d{2}:\d{2}(?::\d{2}(?:\.\d{1,6})?)?)$/;

/**
 * The time (ms since 1970) ISO 8601 text gives, as UTC: a date, or a date and time, with an offset
 * at the time its own clock shows (as its cells show it, so that a column in a time zone is binned,
 * and its bins written, in it); NaN for text that isn't one.
 */
export function timeOf(text: string): number {
  const key = dateKey(ZONED.exec(text)?.[1] ?? text);
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
  /** How many values "top"'s bars of the others, and of the values in one row each, have (or 0). */
  readonly others: number = 0;
  readonly uniques: number = 0;
  /** Whether "top" has too many values to show, each in one row (and so shows none of them). */
  readonly unique: boolean = false;
  /** A data row with each rank (-1 for none). */
  readonly rowOf: Int32Array;
  // Each rank's bar (-1 for none, for a value a histogram can't place), and the missing values' bar
  // (-1 for none)
  private readonly barOf: Int32Array;
  private readonly missingBar: number = -1;

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
      // The values most rows have (the first of those with as many), then the others: all of them,
      // if there's only one more than it shows; else those in more than one row, then the rest
      const order = counts.map((_, rank) => rank).sort((a, b) => (counts[b] as number) - (counts[a] as number) || a - b);
      const many = order.length > TOP + 1;
      const repeated = many ? order.filter((rank) => (counts[rank] as number) > 1) : order;
      const shown = repeated.length > TOP + 1 ? TOP : repeated.length;
      const singles = order.slice(repeated.length);
      this.others = repeated.length - shown;
      this.uniques = singles.length > 1 ? singles.length : 0;
      this.unique = many && repeated.length === 0;
      const add = (kind: BarKind, group: number[]) => {
        group.forEach((rank) => (this.barOf[rank] = this.bars.length));
        this.bars.push({ kind, rank: kind === "value" ? (group[0] as number) : -1, low: NaN, high: NaN });
      };
      repeated.slice(0, shown).forEach((rank) => add("value", [rank]));
      if (this.others > 0) {
        add("others", repeated.slice(shown));
      }
      // (A value in one row, alone, has a bar of its own)
      if (singles.length > 0) {
        add(singles.length === 1 ? "value" : "unique", singles);
      }
      this.missingBar = this.addMissing(ranks);
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
      this.missingBar = this.addMissing(ranks);
      return;
    }
    // (A bin per whole number, or day, if they're few; else as many as fit, of equal width)
    const unit = this.times ? DAY : 1;
    const whole = high - low < BINS * unit && xs.every((x) => !Number.isFinite(x) || Number.isInteger(x / unit));
    const n = whole ? Math.round((high - low) / unit) + 1 : low === high ? 1 : BINS;
    const width = whole ? unit : (high - low) / n;
    for (let i = 0; i < n; i++) {
      this.bars.push({ kind: "value", rank: -1, low: low + i * width, high: whole ? low + i * width : i === n - 1 ? high : low + (i + 1) * width });
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
    this.missingBar = this.addMissing(ranks);
  }

  // A bar of the missing values (and those a histogram can't place), if a row has one: its index
  private addMissing(ranks: readonly (number | null)[]): number {
    if (!ranks.some((rank) => rank === null || (this.barOf[rank] as number) < 0)) {
      return -1;
    }
    this.bars.push({ kind: "missing", rank: -1, low: NaN, high: NaN });
    return this.bars.length - 1;
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
        counts.bars[this.missingBar] = (counts.bars[this.missingBar] as number) + 1;
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

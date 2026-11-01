/**
 * Sorting: ordering data rows by the sort ranks in the spec.
 *
 * Ranks come from the data frame's own sort (see `_get_column_ranks()` in Python), so ordering
 * rows by them gives what sorting the frame would. Missing values (a `null` rank) go last in
 * either direction, and ties keep their order.
 */

import type { Spec } from "./spec";

export interface SortKey {
  column: string;
  descending: boolean;
}

/** A sort key as accepted from callers: `descending` defaults to `false`. */
export interface SortKeyInit {
  column: string;
  descending?: boolean;
}

/**
 * Check and normalize sort keys against a spec's ranks.
 *
 * @throws {RangeError} for a column that isn't sortable, or one given twice.
 */
export function normalizeSort(keys: readonly SortKeyInit[], ranks: Spec["ranks"]): SortKey[] {
  const seen = new Set<string>();
  return keys.map((key) => {
    if (!Object.prototype.hasOwnProperty.call(ranks, key.column)) {
      throw new RangeError(`"${key.column}" isn't a sortable column`);
    }
    if (seen.has(key.column)) {
      throw new RangeError(`"${key.column}" is in the sort more than once`);
    }
    seen.add(key.column);
    return { column: key.column, descending: key.descending === true };
  });
}

/** The data rows `rows` (in their current order), sorted by `keys`. */
export function sortRows(
  rows: readonly number[],
  keys: readonly SortKey[],
  ranks: Spec["ranks"],
): number[] {
  const sorted = rows.slice();
  if (keys.length === 0) {
    return sorted;
  }
  const compared = keys.map((key) => ({
    ranks: ranks[key.column] as readonly (number | null)[],
    sign: key.descending ? -1 : 1,
  }));

  // `Array.prototype.sort()` is stable, so ties keep their order
  return sorted.sort((a, b) => {
    for (const { ranks, sign } of compared) {
      const ra = ranks[a] ?? null;
      const rb = ranks[b] ?? null;
      if (ra === rb) {
        continue;
      }
      if (ra === null) {
        return 1;
      }
      if (rb === null) {
        return -1;
      }
      return sign * (ra - rb);
    }
    return 0;
  });
}

/**
 * The sort after a click on a column's header.
 *
 * A click on the only sort column cycles it through ascending, descending and unsorted; on any
 * other column, it sorts by that column alone, ascending. With `extend` (Shift-click), the column
 * is cycled in place in the current sort, or added to its end, so that the other keys are kept.
 */
export function toggleSort(current: readonly SortKey[], column: string, extend: boolean): SortKey[] {
  const existing = current.find((key) => key.column === column);
  const next: SortKey | null =
    existing === undefined
      ? { column, descending: false }
      : existing.descending
        ? null
        : { column, descending: true };

  if (!extend) {
    if (current.length !== 1 || existing === undefined) {
      return [{ column, descending: false }];
    }
    return next === null ? [] : [next];
  }
  if (existing === undefined) {
    return [...current, next as SortKey];
  }
  return current.flatMap((key) => (key.column !== column ? [key] : next === null ? [] : [next]));
}

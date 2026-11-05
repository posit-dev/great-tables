/**
 * The order of the columns readers can move. They move in runs: a run is a stretch of reorderable
 * data columns next to one another (in the author's order), under the same spanners and pinned to
 * the same side, and a column moves only within its run. So it stays under its spanners, by its
 * side, and on the same side of each column readers can't move.
 */

import type { Spec } from "./spec";

/** The runs of the spec's columns (by index), in column order: those of two columns or more. */
export function columnRuns(spec: Spec): number[][] {
  const runs: number[][] = [];
  let run: number[] = [];
  let last: string | null = null;
  // (A column's run is known by its pin and its spanners)
  const spanners = (id: string) => spec.spanners.filter((spanner) => spanner.columns.includes(id)).map((spanner) => spanner.id);
  spec.columns.forEach((column, i) => {
    const id = column.id;
    const key =
      column.role === "data" && column.reorderable === true && id !== null
        ? JSON.stringify([column.pin ?? null, spanners(id).sort()])
        : null;
    if (key === null || key !== last) {
      if (run.length > 1) {
        runs.push(run);
      }
      run = [];
    }
    if (key !== null) {
      run.push(i);
    }
    last = key;
  });
  if (run.length > 1) {
    runs.push(run);
  }
  return runs;
}

/**
 * The columns of `runs` (each a run's columns, in the author's order) in the order `ids` has them:
 * each run's in the order they're in `ids`, then those it leaves out, in the author's order.
 */
export function orderRuns(ids: readonly string[], runs: readonly (readonly string[])[]): string[] {
  const rank = new Map<string, number>();
  ids.forEach((id, i) => {
    if (!rank.has(id)) {
      rank.set(id, i);
    }
  });
  return runs.flatMap((run) => {
    const at = (id: string) => rank.get(id) ?? ids.length + run.indexOf(id);
    return [...run].sort((a, b) => at(a) - at(b));
  });
}

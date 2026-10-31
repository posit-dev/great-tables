import { define, GtTable, SORT_EVENT, TAG_NAME, VERSION } from "./gt-table";
import { normalizeSort, sortRows, toggleSort } from "./sort";
import { parseSpec, SPEC_VERSION, SpecError } from "./spec";

define();

export type { SortEventDetail, State } from "./gt-table";
export type { SortKey, SortKeyInit } from "./sort";
export type * from "./spec";
export {
  define,
  GtTable,
  normalizeSort,
  parseSpec,
  SORT_EVENT,
  SPEC_VERSION,
  SpecError,
  sortRows,
  TAG_NAME,
  toggleSort,
  VERSION,
};

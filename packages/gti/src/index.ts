import {
  define,
  GtTable,
  SEARCH_EVENT,
  SEARCH_HIGHLIGHT,
  SORT_EVENT,
  TAG_NAME,
  VERSION,
} from "./gt-table";
import { fold, searchTerms } from "./search";
import { normalizeSort, sortRows, toggleSort } from "./sort";
import { parseSpec, SPEC_VERSION, SpecError } from "./spec";

define();

export type { SearchEventDetail, SortEventDetail, State } from "./gt-table";
export type { SortKey, SortKeyInit } from "./sort";
export type * from "./spec";
export {
  define,
  fold,
  GtTable,
  normalizeSort,
  parseSpec,
  SEARCH_EVENT,
  SEARCH_HIGHLIGHT,
  SORT_EVENT,
  SPEC_VERSION,
  SpecError,
  searchTerms,
  sortRows,
  TAG_NAME,
  toggleSort,
  VERSION,
};

import {
  define,
  GtTable,
  PAGE_EVENT,
  RESIZE_EVENT,
  SEARCH_EVENT,
  SEARCH_HIGHLIGHT,
  SELECT_EVENT,
  SORT_EVENT,
  TAG_NAME,
  VERSION,
} from "./gt-table";
import { pageCount, pageItems, pageSizeChoices } from "./paging";
import { fold, searchTerms } from "./search";
import { normalizeSort, sortRows, toggleSort } from "./sort";
import { parseSpec, SPEC_VERSION, SpecError } from "./spec";

define();

export type {
  PageEventDetail,
  ResizeEventDetail,
  SearchEventDetail,
  SelectEventDetail,
  SortEventDetail,
  State,
} from "./gt-table";
export type { SortKey, SortKeyInit } from "./sort";
export type * from "./spec";
export {
  define,
  fold,
  GtTable,
  normalizeSort,
  PAGE_EVENT,
  pageCount,
  pageItems,
  pageSizeChoices,
  parseSpec,
  RESIZE_EVENT,
  SEARCH_EVENT,
  SEARCH_HIGHLIGHT,
  SELECT_EVENT,
  SORT_EVENT,
  SPEC_VERSION,
  SpecError,
  searchTerms,
  sortRows,
  TAG_NAME,
  toggleSort,
  VERSION,
};

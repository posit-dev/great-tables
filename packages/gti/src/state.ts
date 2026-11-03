/**
 * The reader's view of a table, kept (with the spec's `view_state`) in the page's URL and the
 * browser's storage, so that it's there when the page is opened again.
 *
 * A view is kept as the parts of it that differ from the author's (the spec's `view`, without a
 * search, on the first page of the table's page size), each a parameter of a query string:
 *
 *   ?towny.filter=population_2021+%3E%3D+10000&towny.sort=-population_2021&towny.page=2
 *
 * `filter` is the filters' query as text (see `query.ts`), empty for none; `sort`, a column (with
 * `-` before it, for descending), once per sort key, or once empty for none; `search`, the search;
 * `page` and `size`, numbers; `hidden`, a hidden column, once per column, or once empty for none
 * (as `sort` is); and `order`, a column readers can move, once per column, in the order shown. In
 * the URL, each is named after the table's key (`towny.`), so that
 * tables keep views of their own, and the page's other parameters are left as they are; in
 * storage, they're without the key.
 */

import type { FilterQuery } from "./filter";
import { orderRuns } from "./order";
import { formatQuery, parseQuery } from "./query";
import { normalizeSort, type SortKey } from "./sort";
import type { Spec } from "./spec";

export interface View {
  filter: FilterQuery | null;
  sort: SortKey[];
  search: string;
  /** The page shown, from 1. */
  page: number;
  /** The number of data rows on a page, or `null` for one page of every row. */
  pageSize: number | null;
  /** The columns hidden, in column order. */
  hidden: string[];
  /** The columns readers can move, in the order shown. */
  order: string[];
}

export type ViewPart = "filter" | "sort" | "search" | "page" | "size" | "hidden" | "order";

const PARTS: readonly string[] = ["filter", "sort", "search", "page", "size", "hidden", "order"];

/** A view as parameters: each part, and its text (`sort` once per sort key, `hidden` and `order` per column). */
export type ViewParams = [ViewPart, string][];

/** What a table can have of a view kept for it. */
export interface ViewLimits {
  /** Per column the reader can sort by, its ranks; `null` if the reader can't sort the table. */
  ranks: Spec["ranks"] | null;
  search: boolean;
  /** The page sizes the reader can choose from; none, without pages. */
  sizes: number[];
  /** The columns the reader can hide, in column order. */
  hideable: string[];
  /** The runs of columns the reader can move (see `order.ts`), each in the author's order. */
  runs: string[][];
}

const sortText = (key: SortKey) => (key.descending ? "-" : "") + key.column;

const encode = (text: string) => encodeURIComponent(text).replace(/%20/g, "+");

// Texts as parameters of a part, once each, or once empty for none
const repeated = (part: ViewPart, texts: string[]): ViewParams =>
  (texts.length === 0 ? [""] : texts).map((text): [ViewPart, string] => [part, text]);

/** The parts of `view` that differ from `base` (the author's view), as parameters. */
export function viewParams(view: View, base: View): ViewParams {
  const params: ViewParams = [];
  const filter = formatQuery(view.filter);
  if (filter !== formatQuery(base.filter)) {
    params.push(["filter", filter]);
  }
  const sort = view.sort.map(sortText);
  if (JSON.stringify(sort) !== JSON.stringify(base.sort.map(sortText))) {
    params.push(...repeated("sort", sort));
  }
  if (view.search !== base.search) {
    params.push(["search", view.search]);
  }
  if (view.page !== base.page) {
    params.push(["page", String(view.page)]);
  }
  // (Readers can't have every row on one page of a table with pages)
  if (view.pageSize !== base.pageSize && view.pageSize !== null) {
    params.push(["size", String(view.pageSize)]);
  }
  if (JSON.stringify(view.hidden) !== JSON.stringify(base.hidden)) {
    params.push(...repeated("hidden", view.hidden));
  }
  if (JSON.stringify(view.order) !== JSON.stringify(base.order)) {
    params.push(...repeated("order", view.order));
  }
  return params;
}

/** Parameters as a query string has them (without its `?`), each named after `key` (`key.part`), if given. */
export function paramsText(params: ViewParams, key = ""): string {
  const prefix = key === "" ? "" : `${key}.`;
  return params.map(([part, text]) => `${encode(prefix + part)}=${encode(text)}`).join("&");
}

// A query string's parameters, each with its text as it is in the string
function entries(query: string): { raw: string; name: string; value: string }[] {
  return query
    .replace(/^\?/, "")
    .split("&")
    .filter((raw) => raw !== "")
    .map((raw) => {
      const [entry] = new URLSearchParams(raw);
      const [name = "", value = ""] = entry ?? [];
      return { raw, name, value };
    });
}

// The part of the view a parameter is (named after `key`, if given), if any
function partOf(name: string, key: string): ViewPart | null {
  const prefix = key === "" ? "" : `${key}.`;
  const part = name.startsWith(prefix) ? name.slice(prefix.length) : "";
  return PARTS.includes(part) ? (part as ViewPart) : null;
}

/** The parameters of a view in a query string (named after `key`, if given); `null` without any. */
export function readParams(query: string, key = ""): ViewParams | null {
  const params: ViewParams = [];
  for (const { name, value } of entries(query)) {
    const part = partOf(name, key);
    if (part !== null) {
      params.push([part, value]);
    }
  }
  return params.length === 0 ? null : params;
}

/**
 * A query string (with its `?`, or empty) with the parameters named after `key` replaced by
 * `params`. The others are kept as they are.
 */
export function writeParams(query: string, key: string, params: ViewParams): string {
  const kept = entries(query)
    .filter(({ name }) => partOf(name, key) === null)
    .map(({ raw }) => raw);
  const text = [...kept, ...(params.length === 0 ? [] : [paramsText(params, key)])].join("&");
  return text === "" ? "" : `?${text}`;
}

/**
 * The view that parameters keep: `base` (the author's view), with the parts they have. A part the
 * table can't have (as `limits` says), or that isn't one, is left out, with `warn()` saying why;
 * the filter's query is read, but not checked against the table's filters.
 */
export function readView(params: ViewParams, base: View, limits: ViewLimits, warn: (message: string) => void): View {
  const view: View = { ...base, sort: base.sort.map((key) => ({ ...key })), hidden: [...base.hidden], order: [...base.order] };
  const leftOut = (part: ViewPart, why: string) => warn(`the saved view's ${part} is left out (${why})`);
  const sort: string[] = [];
  let sorted = false;
  let hidden: Set<string> | null = null;
  let order: string[] | null = null;
  for (const [part, text] of params) {
    if (part === "filter") {
      try {
        view.filter = parseQuery(text);
      } catch (err) {
        if (!(err instanceof SyntaxError)) {
          throw err;
        }
        leftOut(part, err.message);
      }
    } else if (part === "sort") {
      sorted = true;
      if (text !== "") {
        sort.push(text);
      }
    } else if (part === "hidden") {
      // (Empty for none)
      hidden ??= new Set();
      if (limits.hideable.includes(text)) {
        hidden.add(text);
      } else if (text !== "") {
        warn(`the saved view's hidden column ${JSON.stringify(text)} is left out (it isn't one the reader can hide)`);
      }
    } else if (part === "order") {
      order ??= [];
      if (limits.runs.some((run) => run.includes(text))) {
        order.push(text);
      } else if (text !== "") {
        warn(`the saved view's column ${JSON.stringify(text)} is left out of its order (it isn't one the reader can move)`);
      }
    } else if (part === "search") {
      if (limits.search) {
        view.search = text;
      } else {
        leftOut(part, "the table can't be searched");
      }
    } else {
      const n = /^[1-9]\d{0,8}$/.test(text) ? Number(text) : 0;
      if (limits.sizes.length === 0) {
        leftOut(part, "the table has no pages");
      } else if (part === "page") {
        if (n === 0) {
          leftOut(part, `${JSON.stringify(text)} isn't a page number`);
        } else {
          view.page = n;
        }
      } else if (!limits.sizes.includes(n)) {
        leftOut(part, `${JSON.stringify(text)} isn't a page size the table has`);
      } else {
        view.pageSize = n;
      }
    }
  }
  if (hidden !== null) {
    const kept = hidden;
    view.hidden = limits.hideable.filter((id) => kept.has(id));
  }
  if (order !== null) {
    view.order = orderRuns(order, limits.runs);
  }
  if (sorted) {
    const ranks = limits.ranks;
    if (ranks === null) {
      leftOut("sort", "the table can't be sorted");
    } else {
      // (`-x` is column `x`, descending, if the table has one; otherwise, column `-x`)
      const keys = sort.map((text) => {
        const descending = text.startsWith("-") && Object.prototype.hasOwnProperty.call(ranks, text.slice(1));
        return { column: descending ? text.slice(1) : text, descending };
      });
      try {
        view.sort = normalizeSort(keys, ranks);
      } catch (err) {
        if (!(err instanceof RangeError)) {
          throw err;
        }
        leftOut("sort", err.message);
      }
    }
  }
  return view;
}

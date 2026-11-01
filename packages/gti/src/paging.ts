/**
 * Pagination: splitting the rows a reader can see into pages.
 *
 * Pages hold data rows only; group headings and summary rows go with them (see `GtTable`).
 */

/** The number of pages for `rows` rows, `size` to a page; at least 1, so there's always a page. */
export function pageCount(rows: number, size: number | null): number {
  return size === null ? 1 : Math.max(1, Math.ceil(rows / size));
}

/** The page sizes to offer: the author's, and the current size, in order and without repeats. */
export function pageSizeChoices(size: number, sizes: readonly number[]): number[] {
  return Array.from(new Set([...sizes, size])).sort((a, b) => a - b);
}

// With more pages than this, some page numbers give way to gaps
const SLOTS = 7;

/**
 * The page numbers to show for page `page` of `count`, with `null` for a gap ("…"). The first and
 * last pages and the pages either side of the current one are always there, and there are always
 * the same number of items (once there are more than 7 pages), so the controls keep their width
 * while the reader pages through.
 */
export function pageItems(page: number, count: number): (number | null)[] {
  const range = (from: number, to: number) => Array.from({ length: to - from + 1 }, (_, i) => from + i);
  if (count <= SLOTS) {
    return range(1, count);
  }
  // 1 … 4 5 6 … 20, or one gap when the current page is near either end
  const near = SLOTS - 2;
  if (page < near) {
    return [...range(1, near), null, count];
  }
  if (page > count - near + 1) {
    return [1, null, ...range(count - near + 1, count)];
  }
  return [1, null, page - 1, page, page + 1, null, count];
}

/**
 * Borders for a table whose header and footer rows stick as its body scrolls.
 *
 * GT's tables collapse their borders (`border-collapse: collapse`), and collapsed borders are the
 * table's, not the cells': they stay where they are as sticky cells move. So a table that scrolls
 * has its borders separated, and the borders GT collapsed are drawn again on its cells. Each edge
 * between cells gets the border the browser would have collapsed it to (CSS 2.2, 17.6.2.1), drawn
 * by one of the cells on it, so that it moves with whichever of them sticks.
 */

export type Side = "top" | "right" | "bottom" | "left";

export interface Border {
  width: number;
  style: string;
  color: string;
}

/** Where a border that could be drawn on an edge comes from: a cell, a row, a row group, the table. */
export const CELL = 3;
export const ROW = 2;
export const ROW_GROUP = 1;
export const TABLE = 0;

export interface Candidate extends Border {
  origin: number;
}

const SIDES: readonly Side[] = ["top", "right", "bottom", "left"];

// Of two borders as wide, the one in the style listed first wins
const STYLES = ["double", "solid", "dashed", "dotted", "ridge", "outset", "groove", "inset"];

const styleRank = (style: string) => {
  const i = STYLES.indexOf(style);
  return i < 0 ? STYLES.length : i;
};

function beats(a: Border & { origin?: number }, b: Border & { origin?: number }): boolean {
  if (a.width !== b.width) {
    return a.width > b.width;
  }
  const ranks = styleRank(a.style) - styleRank(b.style);
  if (ranks !== 0) {
    return ranks < 0;
  }
  return (a.origin ?? 0) > (b.origin ?? 0);
}

/**
 * The border an edge collapses to, from the borders on it (listed from the top or left, which
 * wins a tie): none if any is `hidden`, else the widest, in the strongest style, from the most
 * specific origin.
 */
export function collapse(candidates: readonly (Candidate | undefined)[]): Border | null {
  let best: Candidate | null = null;
  for (const candidate of candidates) {
    if (candidate === undefined) {
      continue;
    }
    if (candidate.style === "hidden") {
      return null;
    }
    if (candidate.style === "none" || !(candidate.width > 0)) {
      continue;
    }
    if (best === null || beats(candidate, best)) {
      best = candidate;
    }
  }
  return best === null ? null : { width: best.width, style: best.style, color: best.color };
}

const PROPERTIES = SIDES.flatMap((side) =>
  ["width", "style", "color"].map((part) => `border-${side}-${part}`),
);

type Borders = Record<Side, Border>;

interface Placed {
  cell: HTMLTableCellElement;
  r0: number;
  r1: number;
  c0: number;
  c1: number;
}

/**
 * Draws a table's collapsed borders on its cells, for the rows shown. Each cell's own borders are
 * read (from its computed style) the first time it's drawn, and kept, since drawing changes them.
 */
export class TableBorders {
  private readonly table: HTMLTableElement;
  private readonly own = new WeakMap<Element, Borders>();
  // A cell's inline border declarations, before it was drawn
  private readonly authored = new WeakMap<HTMLTableCellElement, [string, string][]>();
  private readonly drawn = new WeakMap<HTMLTableCellElement, Record<Side, Border | null>>();
  private readonly ownsBelow: (tr: HTMLTableRowElement) => boolean;

  /**
   * `ownsBelow` says which rows draw the edge below them (sticky rows that hold the edge between
   * them and the rows that scroll under them); otherwise the row below an edge draws it.
   */
  constructor(table: HTMLTableElement, ownsBelow: (tr: HTMLTableRowElement) => boolean) {
    this.table = table;
    this.ownsBelow = ownsBelow;
    this.read(table);
    const style = table.style;
    style.borderCollapse = "separate";
    style.borderSpacing = "0";
    style.borderStyle = "none";
  }

  /** The border a cell draws on a side (once drawn). */
  drawnBorder(cell: HTMLTableCellElement, side: Side): Border | null {
    return this.drawn.get(cell)?.[side] ?? null;
  }

  /** A row's classes changed (and with them, maybe, its cells' borders): read them again. */
  forget(tr: HTMLTableRowElement): void {
    for (const cell of Array.from(tr.cells)) {
      const authored = this.authored.get(cell);
      if (authored === undefined) {
        continue;
      }
      for (const [property, value] of authored) {
        if (value === "") {
          cell.style.removeProperty(property);
        } else {
          cell.style.setProperty(property, value);
        }
      }
      this.authored.delete(cell);
      this.drawn.delete(cell);
      this.own.delete(cell);
    }
  }

  /** Draw the borders of the rows shown. */
  redraw(): void {
    const rows = Array.from(this.table.rows).filter((tr) => !tr.hidden);
    const n = rows.length;
    if (n === 0) {
      return;
    }

    // Lay the cells out on a grid of the rows shown (a cell spans rows only in its row group)
    const sectionEnd: number[] = new Array<number>(n);
    for (let r = n - 1; r >= 0; r--) {
      const next = rows[r + 1];
      sectionEnd[r] = next !== undefined && next.parentElement === rows[r]?.parentElement ? (sectionEnd[r + 1] as number) : r;
    }
    const grid: (Placed | undefined)[][] = rows.map(() => []);
    const placed: Placed[] = [];
    rows.forEach((tr, r) => {
      const line = grid[r] as (Placed | undefined)[];
      let c = 0;
      for (const cell of Array.from(tr.cells)) {
        while (line[c] !== undefined) {
          c++;
        }
        const r1 = cell.rowSpan === 0 ? (sectionEnd[r] as number) : Math.min(r + Math.max(1, cell.rowSpan) - 1, sectionEnd[r] as number);
        const c1 = c + Math.max(1, cell.colSpan) - 1;
        const p: Placed = { cell, r0: r, r1, c0: c, c1 };
        placed.push(p);
        for (let rr = r; rr <= r1; rr++) {
          const target = grid[rr] as (Placed | undefined)[];
          for (let cc = c; cc <= c1; cc++) {
            target[cc] = p;
          }
        }
        c = c1 + 1;
      }
    });
    const ncols = Math.max(...grid.map((line) => line.length));

    const sides = new Map<HTMLTableCellElement, Record<Side, Border | null>>();
    for (const p of placed) {
      this.read(p.cell);
      sides.set(p.cell, { top: null, right: null, bottom: null, left: null });
    }
    const give = (p: Placed, side: Side, border: Border | null) => {
      const drawn = sides.get(p.cell) as Record<Side, Border | null>;
      const had = drawn[side];
      if (border !== null && (had === null || beats(border, had))) {
        drawn[side] = border;
      }
    };
    const of = (el: Element | null, side: Side, origin: number): Candidate | undefined => {
      const border = el === null ? undefined : this.read(el)[side];
      return border === undefined ? undefined : { ...border, origin };
    };
    const group = (tr: HTMLTableRowElement) => {
      const parent = tr.parentElement;
      return parent === this.table ? null : parent;
    };
    const table = this.table;

    // Edges between rows: the edge above row `r` (the table's top for 0, its bottom for `n`)
    for (let r = 0; r <= n; r++) {
      const above = rows[r - 1];
      const below = rows[r];
      const sectionChange = above === undefined || below === undefined || group(above) !== group(below);
      for (let c = 0; c < ncols; c++) {
        const a = above === undefined ? undefined : grid[r - 1]?.[c];
        const b = below === undefined ? undefined : grid[r]?.[c];
        if (a !== undefined && a === b) {
          continue;
        }
        const border = collapse([
          a === undefined ? undefined : of(a.cell, "bottom", CELL),
          b === undefined ? undefined : of(b.cell, "top", CELL),
          above === undefined ? undefined : of(above, "bottom", ROW),
          below === undefined ? undefined : of(below, "top", ROW),
          sectionChange && above !== undefined ? of(group(above), "bottom", ROW_GROUP) : undefined,
          sectionChange && below !== undefined ? of(group(below), "top", ROW_GROUP) : undefined,
          above === undefined ? of(table, "top", TABLE) : undefined,
          below === undefined ? of(table, "bottom", TABLE) : undefined,
        ]);
        if (a !== undefined && (b === undefined || this.ownsBelow(above as HTMLTableRowElement))) {
          give(a, "bottom", border);
        } else if (b !== undefined) {
          give(b, "top", border);
        }
      }
    }

    // Edges between columns, in each row: the edge before column `c` (the row's end for `ncols`).
    // A cell spanning rows takes the strongest of the borders along its side.
    rows.forEach((tr, r) => {
      const line = grid[r] as (Placed | undefined)[];
      for (let c = 0; c <= ncols; c++) {
        const a = line[c - 1];
        const b = line[c];
        if ((a !== undefined && a === b) || (a === undefined && b === undefined)) {
          continue;
        }
        const first = c === 0;
        const last = b === undefined;
        const border = collapse([
          a === undefined ? undefined : of(a.cell, "right", CELL),
          b === undefined ? undefined : of(b.cell, "left", CELL),
          first ? of(tr, "left", ROW) : last ? of(tr, "right", ROW) : undefined,
          first ? of(group(tr), "left", ROW_GROUP) : last ? of(group(tr), "right", ROW_GROUP) : undefined,
          first ? of(table, "left", TABLE) : last ? of(table, "right", TABLE) : undefined,
        ]);
        if (b !== undefined) {
          give(b, "left", border);
        } else if (a !== undefined) {
          give(a, "right", border);
        }
      }
    });

    for (const [cell, drawn] of sides) {
      this.draw(cell, drawn);
    }
  }

  private draw(cell: HTMLTableCellElement, drawn: Record<Side, Border | null>): void {
    const before = this.drawn.get(cell);
    for (const side of SIDES) {
      const border = drawn[side];
      const had = before?.[side];
      if (before !== undefined && same(border, had ?? null)) {
        continue;
      }
      cell.style.setProperty(
        `border-${side}`,
        border === null ? "none" : `${border.width}px ${border.style} ${border.color}`,
      );
    }
    this.drawn.set(cell, drawn);
  }

  // An element's own borders, as computed before they were drawn
  private read(el: Element): Borders {
    let borders = this.own.get(el);
    if (borders !== undefined) {
      return borders;
    }
    const view = el.ownerDocument.defaultView;
    const style = view === null ? null : view.getComputedStyle(el);
    const side = (name: Side): Border => ({
      width: parseFloat(style?.getPropertyValue(`border-${name}-width`) ?? "") || 0,
      style: style?.getPropertyValue(`border-${name}-style`) || "none",
      color: style?.getPropertyValue(`border-${name}-color`) || "currentcolor",
    });
    borders = { top: side("top"), right: side("right"), bottom: side("bottom"), left: side("left") };
    this.own.set(el, borders);
    if (el instanceof HTMLTableCellElement && !this.authored.has(el)) {
      this.authored.set(
        el,
        PROPERTIES.map((property) => [property, el.style.getPropertyValue(property)]),
      );
    }
    return borders;
  }
}

const same = (a: Border | null, b: Border | null) =>
  a === b || (a !== null && b !== null && a.width === b.width && a.style === b.style && a.color === b.color);

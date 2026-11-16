/**
 * The names of a table's parts, drawn over it (see `GtTable.showParts()`): each part's outline,
 * and its name beside it, where there's room for it, clear of the other names and parts.
 */

export interface Box {
  left: number;
  top: number;
  right: number;
  bottom: number;
}

/** Where a part's name goes: beside it, or over it (inside it, from its start). */
export type Place = "above" | "below" | "left" | "right" | "over";

export interface Part {
  name: string;
  /** Its outlines (the name is beside the first) */
  boxes: Box[];
  /** Where its name goes, in order of preference */
  places: Place[];
}

export interface Placed extends Part {
  /** The name's box */
  label: Box;
  /** The line from the name to the part, if it isn't next to it */
  line: Box | null;
}

const GAP = 4;
// (Names above or below a part are stacked as far as this many deep, to keep clear of each other)
const DEPTH = 4;

const overlaps = (a: Box, b: Box) => a.left < b.right && b.left < a.right && a.top < b.bottom && b.top < a.bottom;

/** The box around `boxes` (or `null` for none) */
export function union(boxes: Box[]): Box | null {
  if (boxes.length === 0) {
    return null;
  }
  return {
    left: Math.min(...boxes.map((box) => box.left)),
    top: Math.min(...boxes.map((box) => box.top)),
    right: Math.max(...boxes.map((box) => box.right)),
    bottom: Math.max(...boxes.map((box) => box.bottom)),
  };
}

/**
 * Place the parts' names, of the sizes given, within `bounds`: each at the first of its places
 * with room for it that is clear of the names placed before it, of the other parts and of `avoid`
 * (or, with none, at its first place)
 */
export function placeParts(
  parts: Part[],
  sizes: { width: number; height: number }[],
  bounds: Box,
  avoid: Box[] = [],
): Placed[] {
  const taken: Box[] = [];
  return parts.map((part, i) => {
    const { width, height } = sizes[i] as { width: number; height: number };
    const box = part.boxes[0] as Box;
    const x = (box.left + box.right) / 2;
    const y = (box.top + box.bottom) / 2;
    const across = (left: number) => Math.max(bounds.left, Math.min(left, bounds.right - width));
    const down = (top: number) => Math.max(bounds.top, Math.min(top, bounds.bottom - height));
    const at = (left: number, top: number): Box => ({ left, top, right: left + width, bottom: top + height });
    const candidates: [Place, Box][] = part.places.flatMap((place): [Place, Box][] => {
      const step = (k: number) => k * (height + GAP);
      if (place === "left" || place === "right") {
        return [[place, at(place === "left" ? box.left - GAP - width : box.right + GAP, down(y - height / 2))]];
      }
      return Array.from({ length: DEPTH }, (_, k): [Place, Box] => [
        place,
        place === "above"
          ? at(across(x - width / 2), box.top - GAP - height - step(k))
          : place === "below"
            ? at(across(x - width / 2), box.bottom + GAP + step(k))
            : at(across(box.left + GAP), box.top + GAP + step(k)),
      ]);
    });
    const clear = ([, label]: [Place, Box]) =>
      label.left >= bounds.left &&
      label.right <= bounds.right &&
      label.top >= bounds.top &&
      label.bottom <= bounds.bottom &&
      !taken.some((other) => overlaps(label, other));
    const fits = (candidate: [Place, Box]) =>
      clear(candidate) &&
      !parts.some((other, j) => j !== i && other.boxes.some((b) => overlaps(candidate[1], b))) &&
      !avoid.some((b) => overlaps(candidate[1], b));
    // (Clear of the other parts and `avoid`, or else of the other names at least)
    const [place, label] = candidates.find(fits) ?? candidates.find(clear) ?? (candidates[0] as [Place, Box]);
    taken.push(label);
    // A line from the name to the part, across the gap between them
    const mid = (from: number, to: number, at: number) => Math.max(from + 4, Math.min(at, to - 4));
    let line: Box | null = null;
    if (place === "above" && label.bottom < box.top) {
      const lx = mid(label.left, label.right, x);
      line = { left: lx - 0.5, right: lx + 0.5, top: label.bottom, bottom: box.top };
    } else if (place === "below" && label.top > box.bottom) {
      const lx = mid(label.left, label.right, x);
      line = { left: lx - 0.5, right: lx + 0.5, top: box.bottom, bottom: label.top };
    } else if (place === "left" || place === "right") {
      const ly = mid(label.top, label.bottom, y);
      const [left, right] = place === "left" ? [label.right, box.left] : [box.right, label.left];
      line = { left, right, top: ly - 0.5, bottom: ly + 0.5 };
    }
    return { ...part, label, line };
  });
}

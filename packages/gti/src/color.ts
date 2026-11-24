// Colors as `data_color()` makes them (see `great_tables/_data_color/`), for the columns whose colors
// are made again from the rows kept (`i_cols_controls(data_color="recompute")`): the palette's
// colors mixed in CIELAB (as R's farver does), at the place of each value in the range of those of
// the rows kept, and black or white text, whichever contrasts with the color more.

import type { ColorSpec } from "./spec";

type Triple = [number, number, number];

const rgbOf = (hex: string): Triple => [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16)) as Triple;

// (Python's `round()`, which rounds halves to even)
const round = (x: number): number => (Math.abs(x % 1) === 0.5 ? 2 * Math.round(x / 2) : Math.round(x));

function labOf(rgb: Triple): Triple {
  const [r, g, b] = rgb.map((channel) => {
    const c = channel / 255;
    return (c > 0.04045 ? ((c + 0.055) / 1.055) ** 2.4 : c / 12.92) * 100;
  }) as Triple;
  const f = (t: number): number => (t > 0.008856 ? t ** (1 / 3) : 7.787 * t + 16 / 116);
  const fx = f((r * 0.4124564 + g * 0.3575761 + b * 0.1804375) / 95.047);
  const fy = f((r * 0.2126729 + g * 0.7151522 + b * 0.072175) / 100);
  const fz = f((r * 0.0193339 + g * 0.119192 + b * 0.9503041) / 108.883);
  return [116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)];
}

function hexOf([lightness, a, b]: Triple): string {
  const fy = (lightness + 16) / 116;
  const inv = (t: number): number => (t ** 3 > 0.008856 ? t ** 3 : (t - 16 / 116) / 7.787);
  const x = (inv(a / 500 + fy) * 95.047) / 100;
  const y = (inv(fy) * 100) / 100;
  const z = (inv(fy - b / 200) * 108.883) / 100;
  return `#${[
    x * 3.2404542 + y * -1.5371385 + z * -0.4985314,
    x * -0.969266 + y * 1.8760108 + z * 0.041556,
    x * 0.0556434 + y * -0.2040259 + z * 1.0572252,
  ]
    .map((c) => {
      c = c > 0.0031308 ? 1.055 * c ** (1 / 2.4) - 0.055 : 12.92 * c;
      return Math.min(255, Math.max(0, round(c * 255)))
        .toString(16)
        .padStart(2, "0");
    })
    .join("")}`;
}

/** The palette's color at `t` (from 0 to 1), its colors spread evenly over the range. */
export function ramp(palette: string[]): (t: number) => string {
  const labs = palette.map((color) => labOf(rgbOf(color)));
  const step = 1 / (labs.length - 1);
  return (t) => {
    // (The last color whose place is at or before `t`, short of the last)
    let i = 0;
    while (i < labs.length - 2 && (i + 1) * step <= t) {
      i++;
    }
    const from = labs[i] as Triple;
    const to = labs[i + 1] as Triple;
    const start = i * step;
    return hexOf(from.map((v, k) => (((to[k] as number) - v) / ((i + 1) * step - start)) * (t - start) + v) as Triple);
  };
}

const apcaLum = (rgb: Triple): number => {
  const lum = rgb.reduce((sum, x, k) => sum + (x / 255) ** 2.4 * ([0.2126729, 0.7151522, 0.072175][k] as number), 0);
  return lum <= 0.022 ? lum + (0.022 - lum) ** 1.414 : lum;
};

function apca(txt: Triple, bg: Triple): number {
  const t = apcaLum(txt);
  const b = apcaLum(bg);
  if (Math.abs(b - t) < 0.0005) {
    return 0;
  }
  let ratio: number;
  if (b > t) {
    ratio = (b ** 0.56 - t ** 0.57) * 1.14;
    ratio = ratio < 0.1 ? 0 : ratio - 0.027;
  } else {
    ratio = (b ** 0.65 - t ** 0.62) * 1.14;
    ratio = ratio > -0.1 ? 0 : ratio + 0.027;
  }
  return ratio * 100;
}

const wcagLum = (rgb: Triple): number =>
  rgb.reduce((sum, x, k) => {
    const c = x / 255;
    return sum + (c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4) * ([0.2126, 0.7152, 0.0722][k] as number);
  }, 0);

function wcag(one: Triple, two: Triple): number {
  const [a, b] = [wcagLum(one), wcagLum(two)];
  return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
}

/** Black or white, whichever text contrasts with the fill (`#RRGGBB`, or `#RRGGBBAA` over white) more. */
export function textColor(fill: string, algo: "apca" | "wcag"): string {
  let bg = rgbOf(fill);
  if (fill.length === 9) {
    const alpha = parseInt(fill.slice(7), 16) / 255;
    bg = bg.map((c) => Math.max(0, Math.min(255, Math.trunc(c * alpha + 255 * (1 - alpha))))) as Triple;
  }
  const contrast = algo === "apca" ? apca : wcag;
  const black: Triple = [0, 0, 0];
  const white: Triple = [255, 255, 255];
  return Math.abs(contrast(black, bg)) >= Math.abs(contrast(white, bg)) ? "#000000" : "#FFFFFF";
}

/**
 * Each place (from 0 to 1) in the palette of the rows of `spec` that `kept` keeps (in the order
 * of `spec.rows`; `null` for those it doesn't), as `data_color()` would have them from those rows.
 */
export function places(spec: ColorSpec, kept: (row: number) => boolean): (number | null)[] {
  const keep = spec.rows.map(kept);
  const { levels, midpoint } = spec;
  if (levels != null) {
    // (The levels of the rows kept, in the order they first come in them)
    const index = new Map<number, number>();
    for (const [k, value] of spec.values.entries()) {
      if (keep[k] === true && !index.has(value as number)) {
        index.set(value as number, index.size);
      }
    }
    return spec.values.map((value, k) =>
      keep[k] === true ? (index.size === 1 ? 0 : (index.get(value as number) as number) / (index.size - 1)) : null,
    );
  }
  const numbers = spec.values.map(Number);
  const finite = numbers.filter((x, k) => keep[k] === true && Number.isFinite(x));
  let scale: (x: number) => number;
  if (midpoint != null) {
    // (A range made even around the midpoint, without an end at it)
    const extent = finite.reduce((most, x) => Math.max(most, Math.abs(x - midpoint)), 0);
    const stops = [midpoint - extent, midpoint, midpoint + extent];
    const at = [0, 0.5, 1].filter((_, i) => i === 1 || stops[i] !== midpoint);
    const ends = stops.filter((stop, i) => i === 1 || stop !== midpoint);
    scale = (x) => {
      let i = 0;
      while (i < ends.length && (ends[i] as number) <= x) {
        i++;
      }
      const below = ends[i - 1] as number;
      return below === x
        ? (at[i - 1] as number)
        : (at[i - 1] as number) + ((x - below) / ((ends[i] as number) - below)) * ((at[i] as number) - (at[i - 1] as number));
    };
  } else {
    // (Without a spread, which a long column would overflow)
    const low = finite.length === 0 ? 0 : finite.reduce((a, b) => Math.min(a, b));
    const range = (finite.length === 0 ? 0 : finite.reduce((a, b) => Math.max(a, b))) - low;
    scale = (x) => (range === 0 ? 0 : (x - low) / range);
  }
  // (Infinite values take the ends of the palette)
  return numbers.map((x, k) => (keep[k] !== true ? null : Number.isFinite(x) ? scale(x) : x > 0 ? 1 : 0));
}

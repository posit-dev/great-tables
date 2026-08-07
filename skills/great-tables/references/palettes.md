# Palettes — the single source of truth for every color hex

Load this whenever you pick a Big-Color fill, a heading-band hue, or any
Small-Color surface (Step 3, 4, or 5). Every hex the skill uses lives here.

There are **three palettes, deliberately linked**: the Small-Color light tints are
just **washed-out versions of the Big-Color solids**, so a table's quiet polish
always echoes its loud color. Use one coherent theme per table.

---

## 1. Dark Academia — SOLID Big-Color palette (Warm set)

Used for **every Big-Color treatment that is not a gradient / heatmap / diverging
fill**: dark heading bands, full-column fills, full-row highlights, status fills,
colored-text anchors. **White text on all solid members.**

| Member | Solid hex | Washed light tint | Use when… |
|---|---|---|---|
| **Navy** | `#22384F` | `#EAF0F6` | **Default** with no other cue |
| Forest | `#2F4A38` | `#EAF1EC` | Nature, growth, environment, money/finance |
| Oxblood | `#5C2E2E` | `#F5EBEB` | Risk, alerts, deficits, intensity (non-diverging) |
| Espresso | `#4A3A2C` | `#F1EADD` | Historical, literary, food/wine, vintage |
| Ochre (accent) | `#9A7B33` | `#F5EFDC` | Premium / awards / highlight |
| Tan (accent/mid) | `#8A7452` | `#EFE7D6` | Secondary warm accent (cream tint) |

### DA hue-selection rule (applies to any solid DA use, including the dark band)

Resolve to **exactly one** hue — this is a deterministic lookup, **not** a
harmonization. **Default Navy.** Otherwise walk this priority order and **pick the
FIRST that applies**, then stop (do not blend hues):

1. any heatmap/gradient palette hue already present in the table — match its family,
2. the data source's subject — per the "Use when…" column of the table above,
3. any other color already used in the table.

If none applies, the hue **is Navy**. One coherent theme per table — the same table
cues resolve to the same hue on every run. *(For the dark heading-band case
specifically — which only occurs when there is **no** Big Color — priority (1) never
applies, so it resolves to subject/theme, i.e. usually Navy.)*

---

## 2. Small Color — light structural surfaces (washed-DA + neutrals)

All quiet surfaces (heading band, stripes, stub tint, dividers, empty cells) draw
from **neutral greys OR a super-light washed-out tint of the table's Big-Color
hue** (the right-hand column of §1) — never a saturated color.

| Neutral role | Default hex | Weight |
|---|---|---|
| Light label band | `#F0F0F0` | — |
| Row stripe | `#F6F6F6` | — |
| Cell hairline (between rows) | `#E8E8E8` | 1px |
| Column-label bottom rule | `#CCCCCC` | 2px |
| Group / summary structural rule | `#BDBDBD` | — |
| Column-group vertical divider | `#D0D0D0` | light but easily noticeable |
| NA / empty cell | `#808080` | `na_color=` fill; `sub_missing("—")` text |

**Default is grey.** When the table has Big Color, harmonize the light surfaces to
the washed tint matching the dominant Big-Color hue (e.g. `Blues` fills → pale-blue
`#EAF0F6` band/stub). This is also what the grey-budget rule reaches for.

### The grey-budget rule

Count the light-grey elements in play (label band, stripes, stub, empty/NA cells,
hairlines). When grey becomes **monotonous** — several large grey areas stacking —
re-color the **highest-priority** element to the **washed-DA tint of the Big-Color
hue** (§1). Shift only as many elements as needed to break the monotony (usually
just one).

**Priority order:** `stub → labels → row design (striping / empty cells)`

Example: grey band + grey stripes + grey stub with `Blues` fills → recolor the
**stub** (highest priority) to pale blue `#EAF0F6`.

---

## 3. Sequential / Diverging — for the ≤2 colored MEASURES only

Used when a measure is a magnitude / trend / signed story. These are matplotlib /
brewer palette **names** passed to `data_color(palette=…)`, not fixed hexes.

### Sequential — fixed hue per semantic (F-deterministic-branch)

This is a **lookup, not a menu.** Read the measure's semantic, take that row's
palette. There is **no choice** and no coin-flip — the same semantic resolves to the
same hue on every run.

| Measure semantic | Palette |
|---|---|
| money · price · revenue · cost · volume · count · population · size — any **neutral magnitude** with no inherent good/bad direction | **`Blues`** — always |
| growth · gain · improvement · "more is better" | **`Greens`** |
| loss · risk · warning · worse · error rate — "more is worse" | **`Reds`** (`Oranges` = documented alternate only, when `Reds` clashes with another hue already in the table) |

A **single** neutral magnitude (money/price/volume/count/population) is **always
`Blues`** — never Greens. `Greens`/`Reds` are reserved for measures that carry an
explicit direction. This removes the Blues-vs-Greens coin-flip. (For the case of **two**
neutral magnitudes in one table, which would both want `Blues`, see the neutral
tie-breaker under "Rules for the colored measures" below.)

### Diverging (signed values)

`RdYlGn` **default**. Orientation is computable, not assumed: positive = good ⇒
`RdYlGn` (green = positive); **positive = bad** (cost/variance-over-budget, error,
defect, latency, delay, downtime, churn — "more is worse") ⇒ `RdYlGn` with
`reverse=True` (green = negative). `RdBu` / `PuOr` colorblind-safe alternatives. The
symmetric domain `[-M, M]` is identical in both orientations — see
`big_color/diverging_fill.md` for the full test.

### Rules for the colored measures

- **Consistency within a measure:** every column of a measure shares the **same
  palette and the same `domain`** — one `data_color` domain spanning all facet
  columns, not per-column domains.
- **Diverging domain:** **symmetric around 0**, covering the full data range, with
  `truncate=False` so out-of-range values keep the most extreme color rather than
  disappearing. (e.g. data −30 → +40 ⇒ `domain=[-40, 40]`.)
- **Two sequential measures:** give them **two distinct semantic hue families —
  never the same** (e.g. `Greens` + `Blues`, not `Blues` + `Blues`). When each measure
  carries its own direction, the semantic lookup already yields distinct hues.
- **Two NEUTRAL measures (the tie-breaker):** two same-semantic neutral magnitudes
  (e.g. price + volume, horsepower + price) both resolve to `Blues` by the lookup, which
  would violate "distinct hues". Resolve deterministically: the **primary** neutral
  measure keeps **`Blues`**; the **secondary** takes the next entry from the pinned
  ordered fallback ladder **`Blues → Greens → Oranges`** (i.e. the second neutral →
  `Greens`; a — never-reached under the ≤2 ceiling — third → `Oranges`). `Reds` is
  excluded from this ladder (reserved for a directional "worse" measure). The ladder is
  applied for **distinctness only**; the fallback hue carries no good/bad meaning here.
  - **Which measure is "primary" (total, computable order):** (1) the measure the
    prompt names/emphasises first, in prompt order; else (2) leftmost-first by DataFrame
    column order. This is the SAME priority order used to pick the ≤2 colored measures
    (`big_color/column_gradient_fill.md`), so both runs assign the same two palettes to
    the same two columns.
- **Non-gradient Big Color uses the Dark Academia solids** (§1), hue per the
  DA hue-selection rule — never these sequential/diverging palettes.

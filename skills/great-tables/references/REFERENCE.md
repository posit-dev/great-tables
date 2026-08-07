# REFERENCE.md — the router: open the right file before each decision

SKILL.md sent you here **before you write any Python**. This is a checklist you
*execute*, not an index you skim. Run it top to bottom against **your** data; for
every row that matches, open the file it names and **copy the exact value out of that
file into your code**. Do not retype a palette, hex, or domain from memory — SKILL.md
holds none of them on purpose. Filenames live here and nowhere else, so you never have
to point past this file.

Paths below are relative to the skill's `references/` directory (this file's own
directory). The worked examples are the one exception: they live at the skill root in
`assets/` — a **sibling** of `references/`, not inside it — so every example path is
written with a leading `../` (i.e. `../assets/examples/…`, which resolves from
`references/`). There is no `references/assets/`.

---

## 0. Unsure of any method signature/args/defaults — at any step

Open **`api.md`** and copy the exact signature. Mechanical API detail only; every
design decision stays in SKILL.md and the files below.

## 1. EVERY table — unconditional (Steps 1, 2, 4 & 5)

- **`data.md`** — the data-cleaning sub-step (Step 1, **before you organize columns**):
  get to ONE correctly-typed DataFrame. Strip currency/percent strings to floats, coerce
  `object`-dtype numerics, fix a non-zero header row, cast SQL `Decimal`s, standardize
  missing values. `great_tables` formats numbers, it does not parse strings — skip this
  and `fmt_*` / `data_color` break silently.
- **`small_color.md` → "Deterministic triggers" section — BEFORE you write the
  `GT(...)` constructor (Step 2).** The stub trigger (PP-13 → `rowname_col=`), the
  grouping trigger (PP-1 → `groupname_col=`), and the ambiguous-measure rule
  (F-canonical-metric, PP-18) all decide **constructor arguments**, so resolve them when
  you organize columns (Step 2), **not** at Step 5. Read that one section now; the rest
  of `small_color.md` (the polish checklist) is read later, at Step 5 (next bullet).
- **`palettes.md`** — the single source of truth for every hex: Dark Academia solids,
  their washed light tints, the neutral greys, and the sequential/diverging palette
  *names*. Open it before you write any color at all.
- **`small_color.md`** — the fixed Small-Color polish checklist (cell borders, column
  dividers, the row-striping gate, stub tint, `fmt_*` per semantic type, the
  grey-budget rule, row-group emphasis) plus **all neutral hexes** and the **frame
  border color/width + the `gtsave` margin/zoom values**. Open it before Step 5 and
  before you set the frame; run every gated item.

## 2. A numeric magnitude / trend / signed measure is present (Step 3)

**Before you write `data_color(...)`**, find your data shape below, open the **one**
file it names, and copy that file's palette + domain rule. Also read `palettes.md` §3
for the palette *name* and the diverging-symmetric-domain rule.

| Your data shape | Open |
|---|---|
| **Signed** measure (neg/pos, opposite meaning) | `big_color/diverging_fill.md` |
| **Ordered magnitude**, ≥5 rows | `big_color/column_gradient_fill.md` |
| **Matrix / heatmap** (facets sharing one scale) | `big_color/column_gradient_fill.md` |
| **Top-N** "winner" rows | `big_color/full_row_highlight.md` |
| **Binary / categorical status** | `big_color/status_cell_fill.md` |
| A few **outlier cells** | `big_color/bold_colored_number.md` |
| **One text column that IS the column** | `big_color/full_column_fill.md` |

Ceiling: **≤ 2 colored measures**. One measure ⇒ it's the hero and gets colored. A
pure categorical/text table with no magnitude/trend/signed/winner story gets **no**
fill — its anchor is the dark heading band (Step 4). (Hero text that is not a colored
measure gets **bold text**, never a second fill — a one-line rule, no file needed.)

## 3. Choosing the heading band (Step 4)

Open **`big_color/column_label_emphasis.md`** for the band decision itself (the
dark-vs-light branch keyed off Big Color), then **`palettes.md`** for the exact **band
hex** — a washed tint of the Big-Color hue if the table has ANY Big Color, else a
**dark DA solid with white text** — and the **DA hue-selection rule**. Keep the
column-label bottom rule regardless of band (hex in `small_color.md`).

## 4. Your data matches an archetype (Steps 2 & 5)

Open the matching worked example for a full runnable table to pattern-match against
(`../assets/examples/EXAMPLES.md` indexes them all).

| Archetype — use when… | Open |
|---|---|
| Money, prices, signed deltas, percentages | `../assets/examples/financial/` |
| Dates, trends, monthly/yearly aggregation | `../assets/examples/time_series/` |
| Color-encoded data cells | `../assets/examples/heatmap/` |
| Top-N lists, ordered results | `../assets/examples/ranking/` |
| Aggregations, totals, subtotals | `../assets/examples/summary_stats/` |
| Measurements with units, sig figs | `../assets/examples/scientific/` |

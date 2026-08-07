# Big Color — Column Gradient Fill

Apply `data_color` to an ordered numeric column so that each cell's background encodes its magnitude on a sequential palette. The column becomes a mini-heatmap.

## Trigger (computable — not optional)

**IF an ordered numeric magnitude is present over ≥5 rows ⇒ it QUALIFIES as a colored
measure** (the hero, if it is the only one that qualifies). This is a deterministic
branch, **not** a judgment call — do not ask "should this be colored?" The ≥5-row
magnitude answers it: yes, it qualifies. (Below 5 rows a gradient reads as random
pastel — it does not qualify; use a targeted highlight instead, see the last rule.)

"Qualifies" is not the same as "is colored": the router caps a table at **≤ 2 colored
measures**. When **1 or 2** measures qualify, colour **all** of them (each is
mandatory — do not leave a qualifying measure uncoloured). When **3 or more** qualify,
you MUST colour exactly 2 — the ceiling wins — and the priority rule below picks
**which** 2. This resolves the apparent conflict: qualifying is mandatory *eligibility*,
the ceiling is a *hard cap*, and the priority rule is the deterministic selector.

## Selecting the ≤2 when 3+ qualify (deterministic priority)

Rank every qualifying measure by this order and take the **top 2**. The order is total
and computable, so two runs on the same prompt+data pick the SAME 2 columns:

1. **Prompt-named / emphasised measures first**, in the order they appear in the
   prompt. A measure the user explicitly names, asks to "show/highlight/compare", or
   puts in the title outranks any unnamed one.
2. **Then leftmost-first by DataFrame column order.** Among measures with equal prompt
   priority (e.g. none named, or several named at once), the one whose column appears
   earlier (smallest column index) wins.

Take the first 2 from this ranking; colour those, leave the rest uncoloured (a
qualifying-but-unselected measure gets neither a fill nor a competing highlight — its
magnitude is carried by the number alone). A measure that spans several facet columns
(a matrix/heatmap block) counts as **one** measure occupying **one** of the 2 slots.

## When to use

- The column is an **ordered numeric measure** (revenue, volume, score, count, rate).
- The table has **≥5 rows** so the gradient has enough steps to read.
- Relative magnitude — not just the raw number — is part of the story.
- The values have a natural direction (higher = better, higher = worse, or purely neutral quantity).

If the column has both negatives and positives with opposite meaning, use `diverging_fill.md` instead.

## Recipe

```python
import numpy as np
from great_tables import GT

# DATA-DRIVEN domain, shared across ALL facet columns of this ONE measure.
# Never a per-column domain, never a round guess — compute it from the frame.
# Backend-neutral: .to_numpy() + np.nanmin/nanmax return a scalar on BOTH pandas and
# polars. (df[cols].min().min() returns a 1-row frame on polars and breaks float(...).)
cols = ["measure"]                              # every column that IS this measure
lo = float(np.nanmin(df[cols].to_numpy()))     # min across all facet columns
hi = float(np.nanmax(df[cols].to_numpy()))     # max across all facet columns

gt = (
    GT(df, rowname_col="entity")
    .fmt_number(columns=cols, decimals=1)
    .data_color(
        columns=cols,
        palette="Blues",         # hue by semantic — palettes.md §3 lookup (neutral magnitude → Blues, always)
        domain=[lo, hi],         # explicit, ONE shared domain over all facet columns — never omit
        truncate=False,          # outliers keep the extreme color, never disappear
        na_color="#808080",      # NA/empty neutral (palettes.md §2)
    )
)
```

## Rules

- **Domain = `[min, max]` across ALL facet columns of the measure — one shared domain.**
  Compute `lo`/`hi` from the frame with the **backend-neutral** reduction
  `float(np.nanmin(df[cols].to_numpy()))` / `float(np.nanmax(df[cols].to_numpy()))`
  (matches the diverging recipe; works on pandas AND polars — the pandas-only
  `df[cols].min().min()` returns a 1-row frame on polars and breaks `float(...)`); the
  bound must be **DATA-DRIVEN**, never a round guess. If the measure spans several facet
  columns, they share this **single** domain (not a per-column domain), so equal values
  read as equal color across the block. A too-narrow domain flattens the extremes; a
  too-wide domain washes out the middle.
- **Palette by semantic — pin it from `palettes.md` §3, not by aesthetic.** It is a
  lookup, not a choice: neutral magnitude (money/price/volume/count/population) → `Blues`
  (always); good-direction ("more is better") → `Greens`; warning/worse → `Reds`
  (`Oranges` only as the documented alternate). This kills the Blues-vs-Greens coin-flip.
- **Do not gradient-fill the stub or identifier columns** — the gradient must apply to the measure only.
- **Leave `truncate=False`** (default). If an outlier appears later it should still get the extreme color, not disappear.
- **Do not** also bold or color the text of the same cells — the fill already carries the signal. Layering both crowds the cell.
- **≥5 rows** or skip: a 3-row gradient reads as random pastel; use a targeted highlight instead.

## Counts as

One Big Color treatment. If you also add a totals row that participates in the gradient, that's still one treatment.

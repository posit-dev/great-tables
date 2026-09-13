# Big Color — Full Column Fill

Apply a solid background color to every body cell in one (or a small number of) column(s) so that the column reads as *the* column in the table.

## When to use

- One column carries the primary message and its values are **categorical, ordinal, or otherwise not well-suited to a gradient** (labels, tiers, tags).
- You want the reader's eye to lock onto that column before scanning left/right.
- The fill is a *label*, not a *scale* — the same shade on every cell, not a gradient.

If the column is an ordered numeric measure, use `column_gradient_fill.md` instead so the fill carries magnitude.

## Recipe

```python
from great_tables import GT, style, loc

gt = (
    GT(df)
    .tab_style(
        style=[style.fill(color="#22384F"),          # Dark Academia solid (Navy default)
               style.text(color="#ffffff", weight="bold")],   # white text on the solid
        locations=loc.body(columns="focus_col"),
    )
)
```

## Rules

- **One fill color for the whole column.** Do not vary it row-by-row — that's a different technique (`column_gradient_fill` or `status_cell_fill`).
- **A solid Dark Academia hex with white text** (this is a non-gradient Big Color). Navy `#22384F` is the default; harmonize to the table's DA hue per the DA hue-selection rule in `references/palettes.md` §1 (Forest `#2F4A38`, Oxblood `#5C2E2E`, Espresso `#4A3A2C`, Ochre `#9A7B33`, Tan `#8A7452`). Never a pale/washed tint here — that quiet tint belongs to the stub, not to a Big-Color column.
- **Also fill the column-label header** for that column with the same DA solid if you want the emphasis to extend into the header — pair with the `column_label_emphasis` technique on just that column.
- **Do not** fill the stub column this way. Stub is structural — use the stub tint in `references/small_color.md` instead.

## Counts as

One Big Color treatment (even if you also bold the text — bold + fill on the same target answers one question).

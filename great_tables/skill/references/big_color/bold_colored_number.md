# Big Color — Bold + Colored Number

Apply bold weight and a strong text color to a small number of individual cells so the outliers or threshold breaches pop off an otherwise-quiet table.

## When to use

- A small fraction of cells (roughly ≤20% of the rows in the target column) genuinely stand out — extremes, threshold breaches, records.
- You want the table body to stay mostly neutral so that these few cells read as "the answer."
- The rest of the column is not being gradient- or diverging-filled (this technique is the *alternative* to filling the whole column, not an addition to it).

If you want to emphasize every row in the column, use `column_gradient_fill.md` or `diverging_fill.md` instead — this technique loses meaning when overused.

## Recipe

```python
from great_tables import GT, style, loc

threshold_hi = 0.10
threshold_lo = -0.10

hi_rows = df.index[df["return"] >=  threshold_hi].tolist()
lo_rows = df.index[df["return"] <=  threshold_lo].tolist()

gt = (
    GT(df, rowname_col="period")
    .fmt_percent(columns="return", decimals=1, force_sign=True)
    .tab_style(
        style=style.text(weight="bold", color="#2F4A38"),      # Forest solid = positive outliers
        locations=loc.body(columns="return", rows=hi_rows),
    )
    .tab_style(
        style=style.text(weight="bold", color="#5C2E2E"),      # Oxblood solid = negative outliers
        locations=loc.body(columns="return", rows=lo_rows),
    )
)
```

## Rules

- **Collect row indices into a list first**, then make one `tab_style` call per style. Never loop `tab_style` once per row.
- **Cap the number of highlighted cells.** If more than ~1/3 of the column is bold-colored, nothing stands out — switch to a gradient/diverging fill instead.
- **Colored text uses the Dark Academia solids** (per `references/palettes.md` §1): Forest `#2F4A38` = positive/good, Oxblood `#5C2E2E` = negative/bad, Ochre `#9A7B33` for a single "warning" tier. No more than 2–3 text colors in one table.
- **Use `rows=<list of int positions>`** — positional row indices in the displayed table, not DataFrame index values (they only match when the DataFrame index is `0..n-1`).
- Bold-only (no color) is also a valid variant when the highlight is about *importance*, not *direction* — e.g. the row that answers the user's specific question.

## Counts as

One Big Color treatment even though it touches multiple cells: the treatment answers a single question ("which values are extreme?").

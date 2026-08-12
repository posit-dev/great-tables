# Big Color — Full Row Highlight

Apply a background fill (optionally with bold text) to one or a small number of *entire rows* so that a small set of "winner" rows dominates the visual hierarchy.

## When to use

- A ranking or leaderboard where the top 1–3 rows are the message (top-N).
- A single "current" or "featured" row (this quarter, this user, selected item) needs to be found instantly.
- The number of highlighted rows is **small relative to the total** — roughly ≤30% of body rows. Any more and the highlight becomes the norm.

If you're trying to encode magnitude across all rows, use `column_gradient_fill.md`. If the emphasis is per-cell (only certain values in a column), use `bold_colored_number.md`.

## Recipe

```python
from great_tables import GT, style, loc

top_rows = df.nsmallest(3, "rank").index.tolist()   # rank=1 is best

gt = (
    GT(df, rowname_col="rank")
    .tab_style(
        style=[style.fill(color="#9A7B33"),          # Dark Academia solid (Ochre = premium/awards)
               style.text(color="#ffffff", weight="bold")],   # white text on the solid
        locations=loc.body(rows=top_rows),
    )
)
```

## Rules

- **Fill spans all columns** in the body — omit `columns=` in `loc.body()` so the whole row gets the fill.
- **A solid Dark Academia hex with white text** (this is a non-gradient Big Color). Ochre `#9A7B33` reads as "featured / winner / premium"; use Oxblood `#5C2E2E` when the highlighted row means "bad" (a violation, a losing entry); Navy `#22384F` is the neutral default. Pick the hue per the DA hue-selection rule in `references/palettes.md` §1. Never a pale/washed tint here — that quiet tint is a Small-Color surface, not a Big-Color highlight.
- **Do not** stack a full-row highlight on top of a column gradient or diverging fill — the two treatments compete and cancel out. Pick one.
- **≤30% of rows.** More than that and you're not highlighting, you're recoloring the table.

## Counts as

One Big Color treatment.

# Big Color — Diverging Fill

Apply `data_color` with a diverging palette to a signed numeric column so that negatives and positives get opposite hues around a neutral midpoint.

## When to use

- The column contains **signed values** (returns, P&L, YoY change, budget variance, deltas).
- Positive and negative carry **opposite meaning** (up = good and down = bad, or vice versa).
- Zero (or another explicit midpoint) is the natural neutral.

If the column is one-directional (only positive, only "more = more"), use `column_gradient_fill.md` instead. A diverging palette on **unsigned** data is WRONG (see the "Do NOT" block below).

## Palette (pinned)

- **`RdYlGn` — the default for any signed measure.** This is the deterministic choice;
  do not substitute a custom hex list. But its **orientation** depends on which sign is
  the *unfavorable* one — resolve that with the computable test below, do not assume.
- `RdBu` / `PuOr` — colorblind-safe alternatives; use one of these when accessibility is a hard requirement.

### Orientation — which sign is red (computable, not a judgment call)

`RdYlGn` reads red→yellow→green from low→high. The question is only whether **positive**
is the good (green) or the bad (red) end. Apply this deterministic test:

- **Positive-is-bad?** The measure QUALIFIES as positive-is-bad when its name/semantic
  is one where **more = worse**: cost/expense/spend **variance vs budget** or
  **over-budget** amount, **error** count/rate, **defect** count/rate, **latency /
  response time / delay**, **downtime**, **waste/scrap**, **churn**, **complaints**,
  **overrun**. (Rule of thumb: rising values are the thing you want to *reduce*.)
- **Resolution:**
  - positive-is-bad measure ⇒ **`palette="RdYlGn", reverse=True`** (green = negative =
    favorable, red = positive = unfavorable).
  - every other signed measure (the **default** — returns, P&L, gain/loss, YoY growth,
    net delta, where positive = good) ⇒ **`palette="RdYlGn"`** (no `reverse`; green =
    positive, red = negative).

The symmetric data-driven domain `[-M, M]`, `M = max(|min|, |max|)`, is **identical**
in both branches — only the palette direction flips, so `0` still sits at the neutral
midpoint. If unsure which side is unfavorable, state the chosen orientation in a source
note so the choice is reproducible.

## Recipe

```python
import numpy as np
from great_tables import GT

# SYMMETRIC, DATA-DRIVEN domain across ALL facet columns of this ONE measure.
cols = ["return"]                                        # every column that IS this measure
lo = float(np.nanmin(df[cols].to_numpy()))
hi = float(np.nanmax(df[cols].to_numpy()))
M  = max(abs(lo), abs(hi))                               # M = max(|min|, |max|)

gt = (
    GT(df, rowname_col="period")
    .fmt_percent(columns=cols, decimals=1, force_sign=True)
    .data_color(
        columns=cols,
        palette="RdYlGn",                            # signed default; RdBu / PuOr = colorblind-safe alts
        reverse=False,                               # positive=good default; set reverse=True for positive-is-bad (see Orientation)
        domain=[-M, M],                              # SYMMETRIC so 0 sits at the palette midpoint (identical in both orientations)
        truncate=False,                              # extreme outliers keep the strongest hue
    )
)
```

## Rules

- **Symmetric, data-driven domain — always `[-M, M]` where `M = max(|min|, |max|)`**
  computed over **all facet columns** of the measure. Compute it from the frame; never
  hand-pick a round bound. The domain is symmetric so `0` lands exactly on the palette
  midpoint and a +5% gain and a −5% loss render at equal saturation.
- **`force_sign=True`** in the formatter so the `+`/`−` is part of the cell text — the reader shouldn't have to infer sign from color alone.
- **Do not also color the text** red/green on top of the fill. Redundant encoding on top of the fill adds no signal and crowds the cell. Pick fill *or* colored-bold-text, not both. (If you want colored bold text for outliers only, use `bold_colored_number.md` and skip the fill.)
- **Leave `truncate=False`** (default) so extreme outliers still get the strongest hue.

## Do NOT (these are WRONG — the two failure modes)

- **Asymmetric domain** (e.g. `domain=[-30, 15]`) — WRONG. `0` must sit at the palette
  midpoint; an off-center domain shifts the neutral point, so equal-magnitude gains and
  losses render at different saturations and the red/green split lies about the data.
- **A diverging palette on UNSIGNED data** (e.g. `RdYlGn` on a price or volume) — WRONG.
  Diverging implies a good-vs-bad axis around a midpoint that does **not** exist for a
  pure magnitude; use a **sequential** gradient (`column_gradient_fill.md`) instead.

## Counts as

One Big Color treatment.

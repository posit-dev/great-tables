# Big Color — Column Label Emphasis (the heading band)

The column-label band is decided by the **Step-4 rule**, and it keys **only off Big
Color** (fills, colored text, a highlighted column/row from Step 3). The quiet
washed/grey surfaces of Step 5 do **not** count.

```
Does the table have ANY Big Color?
  ├─ NO  → DARK saturated band  (Dark Academia solid, white text) — THIS FILE.
  │        The band is the table's anchor; hue per the DA hue-selection rule → usually Navy.
  └─ YES → LIGHT band  (washed-DA tint of the Big-Color hue, or grey).
           Let the data color dominate; the band stays quiet. See the light branch below.
```

So a **dark saturated header band anchors the table ONLY when there is no Big Color**
— the pure categorical/text table (gtcars-style) with no magnitude/trend/signed/winner
story. **When Big Color exists, the band goes light** and is a Small-Color surface, not
a Big-Color one.

## When to use the DARK band (no-Big-Color branch)

- The body is intentionally quiet — no `data_color` fill, no status pills, no
  highlighted rows, no colored text. The header must be the top anchor.
- The table has **spanners** or many columns and the reader needs the header to
  structure everything below.
- You want an editorial look where the header is a clear band across the top.

## Recipe — DARK band (no Big Color)

```python
from great_tables import GT

gt = (
    GT(df)
    .tab_options(
        column_labels_background_color="#22384F",        # Dark Academia solid (Navy default)
        column_labels_font_weight="bold",
        column_labels_text_transform="uppercase",        # optional editorial touch
        column_labels_border_bottom_color="#CCCCCC",      # keep the 2px bottom rule (Step-4 constant)
        column_labels_border_bottom_width="2px",
    )
)
```

White label text on the solid comes from great-tables' automatic contrast; set it
explicitly with `column_labels.style` if a theme overrode it. Pick the hue per the DA
hue-selection rule in `references/palettes.md` §1 — default **Navy** `#22384F`, else
harmonize to the subject/theme (Forest `#2F4A38`, Oxblood `#5C2E2E`, Espresso
`#4A3A2C`, Ochre `#9A7B33`, Tan `#8A7452`).

For a single-column emphasis (anchor just the one "answer" column's header):

```python
from great_tables import style, loc

gt = gt.tab_style(
    style=[style.fill(color="#22384F"), style.text(color="#ffffff", weight="bold")],
    locations=loc.column_labels(columns="focus_col"),
)
```

## The LIGHT band (Big Color present)

When the table has any Big Color, **do not use a dark band.** The header becomes a
quiet washed-DA tint (matched to the dominant Big-Color hue) or grey — a Small-Color
surface. Set it with `tab_options(column_labels_background_color=…)` using a washed
tint from `references/palettes.md` §1 (e.g. pale-blue `#EAF0F6` for a `Blues` table) or
grey `#F0F0F0`, keeping bold labels dark. The bottom rule stays `#CCCCCC`, 2px either
way. This light case is governed by the grey-budget rule in `references/small_color.md`.

## Rules

- **Dark band ⇒ no Big Color.** If any Big Color exists, the band is light — never
  stack a dark saturated band on top of a colored body; they fight for the anchor role.
- **Dark fill + white text** (never dark-on-dark). Light fill ⇒ dark bold text.
- **The header emphasis must match or exceed spanner emphasis.** If you loud-fill the
  column labels, the spanners need at least the same visual weight (bolder, matching
  fill, or a slightly darker shade of the same DA hue).
- **One strong header treatment per table.** Don't also loud-color the row-group
  labels, source note, and stub — the header alone owns the "structural loud" slot.
- **Stub column labels are part of the header.** If you fill the header, either include
  the stubhead in the same fill or explicitly leave it blank; a mismatched stubhead
  cell reads as a bug.

## Counts as

One Big Color treatment (the dark-band case). If you *also* fill spanner cells to match,
that's still one treatment (they're the same structural band). The light-band case is
**not** a Big Color treatment — it's Small-Color chrome.

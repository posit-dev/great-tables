# Big Color — Column Label Emphasis (the heading band)

The column-label band is a **fixed branding constant** (`references/palettes.md`
§0), not a Big-Color decision. Every table gets the **same** dark navy branding
band, bold column labels, and white label text — regardless of whether any measure
in the body is colored, and regardless of what hue a colored measure uses.

Blues/navy is the standard hue for branding surfaces specifically — it does not
follow the same data-driven, per-measure hue selection used for a heatmapped
measure's own fill (`references/palettes.md` §3). A `Greens` heatmap, a `RdYlGn`
diverging fill, or no fill at all in the body: the header band is `#08306B` either
way.

## Recipe — every table, unconditionally

```python
from great_tables import GT

gt = (
    GT(df)
    .tab_options(
        column_labels_background_color="#08306B",        # fixed branding navy — every table
        column_labels_font_weight="bold",
        column_labels_border_bottom_color="#CCCCCC",      # keep the 2px bottom rule (Step-4 constant)
        column_labels_border_bottom_width="2px",
    )
)
```

White text on a `tab_options(column_labels_background_color=...)` fill comes from
great-tables' automatic contrast. `tab_style` does **not** auto-contrast, so if you
also use it (e.g. the single-column recipe below), set `style.text(color="white")`
explicitly:

```python
from great_tables import style, loc

gt = gt.tab_style(
    style=[style.fill(color="#08306B"), style.text(color="#ffffff", weight="bold")],
    locations=loc.column_labels(columns="focus_col"),   # single-column emphasis on top of the band
)
```

## Rules

- **Unconditional.** Every table gets the same dark navy band, bold labels, and
  white text — never a light/washed alternative, never keyed off whether Big Color
  exists in the body.
- **Dark fill + white text, always** (never dark-on-dark).
- **The header emphasis must match or exceed spanner emphasis.** If spanners exist,
  they need at least the same visual weight (bolder, matching fill, or a slightly
  darker shade).
- **One strong header treatment per table.** Don't also loud-color the row-group
  labels, source note, and stub — the header alone owns the "structural loud" slot.
- **Stub column labels are part of the header.** If you fill the header, either
  include the stubhead in the same fill or explicitly leave it blank; a mismatched
  stubhead cell reads as a bug.
- **Column-label bottom rule stays `#CCCCCC`, 2px** — present under the band on
  every table.

## Counts as

The branding band is **not** a Big-Color treatment for Step 3's measure-fill
purposes — it's a fixed structural constant every table gets, so it never competes
with, or counts toward, which measures earn a heatmap fill.

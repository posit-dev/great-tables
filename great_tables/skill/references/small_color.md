# Small Color — the fixed Step-5 checklist

Step 5 is **overall formatting**, and it is **not a menu**. Every table runs this
checklist top to bottom. Each item is **gated** by a rule (the condition that fires
it) and, when it fires, uses the **one** `great_tables` mechanism given here. Every
light surface is drawn from the **branding tier + neutral-grey** palette below — never
an improvised saturated color.

This file is self-contained: all hexes are inlined so you never need a second hop.
(They mirror `references/palettes.md` §0 for the branding tier and §2 for neutrals.)

## The palette this checklist draws from

**Branding tier — fixed, every table, never varies by hue** (`palettes.md` §0):

| Role | Hex |
|---|---|
| Header band | `#08306B` |
| Stub tint | `#EAF0F6` |
| Row stripe | `#F6F6F6` |

Neutral greys (for the remaining quiet surfaces — dividers, hairlines, empty cells,
group rules):

| Role | Hex | Weight |
|---|---|---|
| Cell hairline (between rows) | `#E8E8E8` | 1px |
| Column-label bottom rule | `#CCCCCC` | 2px |
| Group / summary structural rule | `#BDBDBD` | — |
| Column-group vertical divider | `#D0D0D0` | 1px, light but noticeable |
| NA / empty cell | `#808080` | `na_color=` fill; `sub_missing("—")` text |

---

## Deterministic triggers — resolve these at Step 2, BEFORE the constructor

These three triggers set **`GT(...)` constructor arguments** (`rowname_col=`,
`groupname_col=`) and the canonical-metric definition, so resolve them when you
**organize columns (Step 2)** — before you write the constructor — not at Step 5 with
the rest of this checklist. (REFERENCE.md §1 routes you here at Step 2 for exactly this
reason.) Each is a decision the model **executes** on a computable condition, not a
judgment call. Read the condition first; if it fires, the action is mandatory.

### Stub default — a computable trigger (PP-13)

**IF a column holds row identifiers (name / date / ID) ⇒ it IS the stub**
(`rowname_col=…`) — **default ON, not optional.** Do not leave an obvious identifier
as a plain value column. A `tab_stubhead(label=…)` **requires** that the stub already
exist — **no orphan label** (setting a stubhead when there is no `rowname_col` is
wrong, PP-25).

Never rely on `df.set_index("col")` for the stub — `great_tables` never reads the
pandas index; the stub is a real column set via `rowname_col=`. `set_index()`
defaults to `drop=True`, which removes that column from the frame entirely, so
`GT(...)` renders without it — the identifier's values vanish, rather than merely
being demoted to a plain column. Pass `GT(df, rowname_col="col")` on the frame while
`col` is still a real column (i.e. before any `set_index()` call) — passing
`rowname_col="col"` once `col` is only the pandas index raises a `KeyError`, since
it's no longer a column at all.

### Grouping — a computable trigger (PP-1)

**IF the user's prompt names a grouping dimension** ("grouped by X", "by country",
"per region"), **OR the data has a low-cardinality categorical that is the organizing
story ⇒ use `groupname_col=…`.** When the prompt says group, grouping is
**MANDATORY** (Rule 0) — never render that dimension as a plain column. (Stub + groups
may coexist.)

### Ambiguous measures — pick ONE canonical definition (F-canonical-metric, PP-18)

**IF a requested measure has more than one reasonable definition** (e.g. "highest
single-day gain" = `close − open`? intraday `high − low`? day-over-day
`close.diff()`?) **⇒ pick ONE canonical definition, compute it, and STATE the chosen
definition** in the subtitle or a source note (on a table with ≥5 body rows, this
definition is the analytical caption half of (f) below's two-call footer — put it
there, not the subtitle) so the number is reproducible. Do **not**
silently pick one — an unstated choice makes the same prompt yield different numbers
across runs.

### Hero-measure redundancy check when 2+ measures are named (Step 3, before `data_color`)

**IF the prompt names 2+ numeric measures with no explicit ranking** ("Horsepower and
Price," "density changes... with percentage changes," "temperature, wind speed, and
ozone") **⇒ color EACH one that represents a genuinely distinct dimension of what the
request is about.** There is **no cap forcing you down to one** colored measure —
qualifying (see the trigger in `big_color/column_gradient_fill.md`) plus being a
distinct dimension of the story is enough to earn a fill:

- `towny_growth_trends.py` — density (a level) and inter-Census percent change (a
  rate of change) are different concepts, so **both** measures are colored.
- `airquality_monthly_summary.py` — ozone and temperature are different physical
  measurements, so **both** are colored (wind speed stays plain, but because it
  carries no narrative role in this request, not because of a numeric cap).
- `sp500_monthly_performance.py` — percent change, average volume, best-day gain, and
  worst-day loss are four distinct dimensions of "monthly performance," so all four
  carry some form of color treatment.

**Only skip a fill when two candidate measures are near-redundant restatements of the
same underlying idea** — two different proxies for essentially the same question,
where coloring both would just be two heatmaps competing for the same visual
attention without adding information. In that narrow case, color the one the
request's phrasing emphasizes as the actual ask, and leave the other plain:

- `gtcars_hp_price.py` — horsepower and price are both rough proxies for "how
  impressive is this car": redundant, not distinct, dimensions. Price is the natural
  financial hero for this kind of request, so **only `msrp` is colored**; `hp` stays
  fully plain (no fill, no bold).

A secondary measure that's merely mentioned, and isn't a distinct dimension of the
request or the thing its phrasing emphasizes, is exactly the plain-text case this
file's own rule describes ("a named measure that doesn't earn the fill renders fully
plain") — that rule only does its job if you actually identify redundancy instead of
reflexively capping the colored count at one.

---

## (a) Cell borders — ALWAYS

**Gate:** every table.

Light hairline between all body rows. Structurally meaningful rows (summary/total
rows, row-group boundaries) get a **slightly stronger but still restrained** rule so
structure reads without shouting. This is a **separate setting from (b)**.

```python
from great_tables import GT, style, loc

gt = (
    GT(df)
    .tab_options(
        table_body_hlines_style="solid",
        table_body_hlines_color="#E8E8E8",     # hairline between every row
        table_body_hlines_width="1px",
    )
    # structural row (e.g. a totals row) — stronger, still restrained
    .tab_style(
        style=style.borders(sides="top", color="#BDBDBD", weight="1.5px"),
        locations=loc.body(rows=[totals_row_index]),
    )
)
```

Keep the **column-label bottom rule** at `#CCCCCC`, 2px (this is the Step-4 constant,
present under any heading band):

```python
gt = gt.tab_options(column_labels_border_bottom_color="#CCCCCC",
                    column_labels_border_bottom_width="2px")
```

**Column-label text is white — pin it explicitly via `tab_style`.** The heading band
(Step 4) requires white column-label text over the dark navy fill. As
`big_color/column_label_emphasis.md` explains, `great_tables` actually
**auto-contrasts** column-label text to white by default whenever the band is dark
enough — a bare `tab_options(column_labels_background_color=...)` band with no
`tab_style` call at all already renders white label text. This project's convention is
to pin it explicitly anyway, matching every worked example in this project's corpus
(e.g. `assets/examples/ranking/ranking.py`) rather than relying on the auto-contrast
default:

```python
from great_tables import GT, style, loc

gt = gt.tab_style(style=style.text(color="white"), locations=loc.column_labels())
```

`tab_options()` has **no** `column_labels_font_color` or `column_labels_text_color`
parameter — confirmed via `inspect.signature(GT.tab_options)` (great_tables 0.22.0):
none of its 141 parameters matches either name — so this explicit pin has to go
through `tab_style`, not a same-call `tab_options()` kwarg.

If you're also touching heading-band `tab_options(...)` kwargs (background color,
padding, alignment), see the `heading_*` hallucinated-kwarg guardrail under item (c)
below — it lists the invented names to avoid and the real ones to use.

---

## (b) Column-group vertical dividers

**Gate:** logical column groups / multiple spanners exist. No column groups → **none**.

A light, easily-noticeable vertical divider **at each group boundary only** — not
between every column, not a full grid. Put a right border on the **last column of each
group**, in **both** the body and the column labels so the seam runs full height.

```python
from great_tables import GT, style, loc

gt = (
    GT(df)
    .tab_spanner(label="Density", columns=["y1996", "y2001", "y2006"])
    .tab_spanner(label="Change",  columns=["c9601", "c0106"])
    .tab_style(                                       # seam in the body
        style=style.borders(sides="right", color="#D0D0D0", weight="1px"),
        locations=loc.body(columns="y2006"),          # last col of the first group
    )
    .tab_style(                                       # matching seam in the header
        style=style.borders(sides="right", color="#D0D0D0", weight="1px"),
        locations=loc.column_labels(columns="y2006"),
    )
)
```

---

## (c) Row striping

**Gate:** apply by default, always. Skip **only** when the table's visible body —
every non-stub, non-group column — is **already 100% covered by color** (e.g. one
fully-heatmapped measure column next to a stub, with nothing else): a striped row and
a fully-filled cell fight for the same visual space, so stripes add nothing there.
Row count is **not** a factor — a 5-row table stripes exactly like a 500-row table.

```python
gt = (
    GT(df)
    .opt_row_striping()                               # default very-pale stripe
    # optional explicit control:
    .tab_options(row_striping_background_color="#F6F6F6")
)
```

**Hallucinated-kwarg guardrail.** `opt_row_striping()` takes **only** `row_striping: bool
= True` — confirmed via `inspect.signature(GT.opt_row_striping)`. It has no color/style
parameter of its own. Do not invent `opt_row_striping(background_color=...)`,
`opt_row_striping(color=...)`, `opt_row_striping(style=...)`, or
`opt_row_striping(row_striping_background_color=...)` — stripe color is set exactly as
shown above, via a **separate** `tab_options(row_striping_background_color=...)` call.

The same discipline applies to `heading_*` kwargs on `tab_options()`. Confirmed via
`inspect.signature(GT.tab_options)` (great_tables 0.22.0), the real ones are
`heading_title_font_size`, `heading_subtitle_font_size`, `heading_title_font_weight`,
`heading_subtitle_font_weight`, `heading_background_color`, `heading_align`,
`heading_padding`, `heading_padding_horizontal`, and `heading_border_bottom_*` /
`heading_border_lr_*`. There is **no** `heading_font_size`, `heading_text_transform`,
`heading_font_weight`, `heading_text_font_weight`, `heading_text_color`, or
`heading_has_subtitle_padding` — none of these exist on `tab_options()`.

---

## (d) Stub tint

**Gate:** a stub (`rowname_col`) exists.

A light pale-blue tint on the stub so the row labels separate from the value columns.
**`#EAF0F6`, unconditionally** — the branding tier's fixed stub value (`palettes.md`
§0), the same on every table regardless of the table's own Big-Color hue. This is a
fixed default, not a harmonization step.

```python
from great_tables import GT, style, loc

gt = (
    GT(df, rowname_col="entity")
    .tab_style(
        style=style.fill(color="#EAF0F6"),            # fixed branding stub tint — unconditional
        locations=loc.stub(),
    )
)
```

---

## (e) Formatting per column (`fmt_*`)

**Gate:** every value column. Match the semantic type; these precision defaults are
overridable by an explicit user instruction.

| Type | Formatter | Default precision |
|---|---|---|
| Percent | `fmt_percent(columns=…, decimals=1)` | 1 decimal |
| Currency (whole-dollar / large) | `fmt_currency(columns=…, decimals=0)` | 0 decimals |
| Currency (small money) | `fmt_currency(columns=…, decimals=2)` | 2 decimals |
| Number | `fmt_number(columns=…, decimals=1)` | meaningful precision (default 1) |

Always: `use_seps=True` for thousands separators, and `sub_missing(columns=…,
missing_text="—")` for empty cells. Put units in the column **label** only when the
formatter doesn't already convey them.

**Force sign on zero-crossing percent columns — independent of color.** Any column
with percent semantics whose actual data spans both positive and negative values gets
`fmt_percent(columns=…, decimals=1, force_sign=True)`, regardless of whether that
column is colored. A signed percent-change column rendered as plain or bold text,
never touched by `data_color`, still needs `force_sign=True` — a reader shouldn't have
to infer the sign from the number alone.

---

## (f) Titles & annotations (Step 6) — two footer calls, not one

**Gate:** every table (title/subtitle are handled by SKILL.md's Step 6; this item is
about the footer).

1. **An analytical caption** — one `tab_source_note(...)` call stating the table's
   actual finding or a definition you had to pick (the "Ambiguous measures" trigger
   above), e.g. *"Fastest-growing means highest percent change across the full
   1996–2021 span, not the average of the intervening Census periods."* Required
   whenever the table has **≥5 body rows**.
2. **A separate source/provenance note** — a second `tab_source_note(...)` call
   naming where the data came from, e.g. *"Source: Statistics Canada Census
   subdivisions, 1996–2021."*

**Two calls, not one.** A single combined line (*"Source: towny.csv. Density =
population ÷ land area."*) is provenance only — it never satisfies the
analytical-caption half, even when it mentions a definition in passing.
`tab_source_note(...)` stacks every call as its own footer line, so calling it twice
costs nothing structurally:

```python
gt = (
    gt.tab_source_note(source_note="Fastest-growing means highest percent change across the full span, not a per-period average.")
      .tab_source_note(source_note="Source: Statistics Canada Census subdivisions, 1996-2021.")
)
```

**A named-but-uncolored measure stays plain at the measure level — no consolation
bold.** When Step 3 leaves a named measure without the fill (a categorical/text
table's hero, or a secondary measure that turned out to be a near-redundant
restatement of another colored measure — see the redundancy check above), render it
as an ordinary, unstyled value column — no whole-column `style.text(weight="bold")`,
no whole-column text-color treatment, no fill. Plain text is the correct, final
treatment for that measure, not a placeholder for a missing color. This is a
whole-measure rule, not a ban on the separate, narrower `bold_colored_number.md`
technique of bolding a small number of individual outlier CELLS within an
otherwise-plain column when the request specifically calls for highlighting extremes
— that's a distinct technique for a few cells, not a consolation treatment for a
whole measure that lost a fill.

---

## The grey-budget rule — retired

This rule used to promote the stub tint or the heading band to a washed tint of the
table's own Big-Color hue when several grey surfaces stacked up and looked
monotonous. It no longer applies: the heading band, stub tint, and row stripe are now
the fixed branding constants above (and in `palettes.md` §0) — they never vary by
table, so there is nothing left to harmonize or re-balance.

---

## Sub-note — no cap on colored measures

There is no numeric cap on colored measures — color what the request is actually
about, with the correct palette for each. A measure that isn't part of what the
request is actually about renders fully plain at the measure level: no whole-column
fill, no whole-column bold, no whole-column text-color treatment — its magnitude is
carried by the number alone. (This whole-measure rule doesn't touch the separate,
narrower `bold_colored_number.md` technique of bolding a handful of individual
outlier cells within an otherwise-plain column — that's a few-cells technique, not a
whole-measure consolation.) This applies regardless of how many other measures
already carry a color fill.

Cross-linked from `big_color/column_gradient_fill.md`'s priority ladder, which picks
which measures earn the full fill (that ranking is deterministic; how many of the
ranked measures actually earn a fill is a judgment call weighing the request's core
ask against table noise) — but whichever measures don't make the cut follow this same
plain-text rule, never a whole-measure bold/text-color consolation.

## Sub-note — row-group emphasis

**Gate:** the table uses `groupname_col=`. An unstyled group label sits in the flow of
body rows and the reader loses the section boundary.

Give each `groupname_col` header row **bold weight** plus a `#BDBDBD` top/bottom
structural rule — **no background fill**. Bold plus the rule together read as a
section heading; a fill would compete with the header band's branding role
(`column_label_emphasis.md`) and add a color surface where two structural rules
already do the job.

```python
gt = (
    GT(df, groupname_col="Region")
    .tab_options(
        row_group_font_weight="bold",            # required
        row_group_border_top_color="#BDBDBD",    # structural rule (item a)
        row_group_border_bottom_color="#BDBDBD",
        row_group_padding="6px",                 # a touch more air than a body row
    )
)
```

Never fill a group header with a background color, saturated or neutral — bold
weight plus the `#BDBDBD` rule is the complete, non-negotiable treatment. Editorial
weight belongs on the **column labels** (the branding band), not on group headers.

## Sub-note — do NOT use `opt_stylize` as a whole-table styler (PP-17)

**Do NOT use `opt_stylize(...)` to theme the whole table** — it bypasses Steps 4–5.
Build the heading **band (Step 4)** and the **Small-Color polish (Step 5)** explicitly
from this checklist, so the band hue, stripes, and dividers are the pinned hexes and
not a built-in theme. Escaping to `opt_stylize(style=N)` is exactly the off-flowchart
drift that made "same-prompt" runs render as different products.

`opt_stylize(...)` is a full **theme preset** — it sets backgrounds, line colors, and
styles across the whole table. There is **no** exception: do **not** call it for the
whole table, for the container, for "just the rounded corners", or for anything else.
Any use reintroduces exactly the unpinned styling this checklist exists to remove.

**Rounded corners.** `great_tables` has **no** pinned `tab_options(...)` corner-radius
option, so there is **no deterministic rounded-corner mechanism** — the **square**
four-side Frame border below (color `#CCCCCC`, 1px, all sides) **is** the deterministic
Frame, and SKILL.md explicitly declares a square light border acceptable. If (and only
if) rounded corners are explicitly requested, the **only** border-radius-only escape
that touches nothing else is a single `opt_css("table { border-radius: 6px; }")` rule —
CSS scoped to `border-radius` alone, never `opt_stylize`. Default to the square Frame.

## Frame & render parameters (the Global-constant values)

SKILL.md and `REFERENCE.md` route the **Frame** and **font-size fit** global constants
here for their exact values.

**Frame — the boxed enclosing border (every table).** A light border on **all four
sides** plus an outer margin; never flat/edge-to-edge. The border color is the neutral
`#CCCCCC`, 1px, `solid`. Great Tables defaults the *left/right* border style to
`"none"`, so you MUST set the style explicitly or the sides render invisible (you'd get
top/bottom rules, not a box):

```python
gt = gt.tab_options(
    table_border_top_style="solid",    table_border_top_color="#CCCCCC",    table_border_top_width="1px",
    table_border_bottom_style="solid", table_border_bottom_color="#CCCCCC", table_border_bottom_width="1px",
    table_border_left_style="solid",   table_border_left_color="#CCCCCC",   table_border_left_width="1px",
    table_border_right_style="solid",  table_border_right_color="#CCCCCC",  table_border_right_width="1px",
)
```

**Outer margin.** `gt.gtsave("table.png", expand=15)` — raise from the 5px default to
**~15–20** so the box has breathing room. (Scripted variant: `finalize(gt)` applies
this.)

**Render / fit order.** Keep the default **`zoom=2.0`**. When a table renders too big,
in order: (1) raise `gtsave(vwidth=…, vheight=…)` to give it room; (2) raise
`gtsave(zoom=…)` to keep it crisp; (3) only then reduce font size, minimally. Never
*lower* `zoom` below 2.0 to force a fit — that just blurs the render.

**Compact layout — `cols_width` + pinned padding (a consistency addition, not
currently mechanically checked).** Every table sizes each column with
`cols_width(cases={...})` to its own content plus a small buffer — never left to
auto-width. Exact widths are content-dependent (pick per column based on your actual
header/value text). These six padding values are consistent across nearly every
table in this project's corpus (one ground truth in this project's corpus,
`towny_growth_trends.py`, uses `6px` instead of `8px` for the two horizontal-padding
values) — treat `8px`/`8px` as the default and
`6px`/`6px` as an acceptable, occasionally-used alternative, not a hard universal
constant. Pin whichever pair you choose via `tab_options(...)`:

```python
gt = gt.cols_width(cases={"category_col": "180px", "metric_a": "120px", "metric_b": "110px"})  # illustrative -- size to YOUR content
gt = gt.tab_options(
    heading_padding="6px",
    column_labels_padding="6px",
    column_labels_padding_horizontal="8px",
    data_row_padding="5px",
    data_row_padding_horizontal="8px",
    source_notes_padding="6px",
)
```

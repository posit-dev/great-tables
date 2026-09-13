"""Heatmap / data-cell-styling archetype — distilled reference example.

Data: data/towny.csv  (414 Ontario municipalities; population and
      growth across five Census windows from 1996 to 2021)
Story: 25 years of growth in Ontario's 15 largest cities — population
       density and each five-year percent change both color-encoded, as
       two distinct dimensions of "growth." Raw 2021 population stays a
       plain column: it drives the top-15 selection and is shown for
       context, but it is NOT the colored measure (see note below).
"""
import numpy as np
import pandas as pd
from great_tables import GT, html, loc, style

df = pd.read_csv("data/towny.csv")

change_cols = [
    "pop_change_1996_2001_pct",
    "pop_change_2001_2006_pct",
    "pop_change_2006_2011_pct",
    "pop_change_2011_2016_pct",
    "pop_change_2016_2021_pct",
]
# Restrict to top 15 by 2021 population — heatmap patterns live in the
# reader's ability to scan a small grid; 414 rows is unreadable.
top = (
    df.nlargest(15, "population_2021")
      .loc[:, ["name", "population_2021", "density_2021"] + change_cols]
      .reset_index(drop=True)
)

# Symmetric ±|max| domain so 0% always maps to the white midpoint regardless
# of the data range. This is the correctness invariant for diverging color:
# without it, a column of all-positive values would map 0% to red.
chg_lo = float(np.nanmin(top[change_cols].to_numpy()))
chg_hi = float(np.nanmax(top[change_cols].to_numpy()))
abs_max = max(abs(chg_lo), abs(chg_hi))

# Density (a level, normalized by land area) and the five window changes (a
# rate of change) are two genuinely distinct dimensions of "growth" — both
# earn a fill, the same density+percent-change pairing used in this skill's
# towny_growth_trends ground truth. Raw population COUNT is intentionally
# NOT the colored level here: for these 15 rows it spans 166K-2.8M with
# Toronto and Ottawa alone occupying the top of that range, so a linear
# domain over the raw count would land 12 of 15 rows in the bottom 20% of
# the color ramp — the same "nearly every cell nearly the same faint shade"
# failure `scientific` cites as its reason to skip Big Color altogether.
# Density is normalized by land area, so it isn't dominated by the same one
# or two outliers (only 3 of 15 land in the bottom 20% of its domain) and
# produces a heatmap that actually differentiates rows.
dens_lo = float(top["density_2021"].min())
dens_hi = float(top["density_2021"].max())

fastest_city = top.loc[top["pop_change_2016_2021_pct"].idxmax(), "name"]
fastest_pct = top["pop_change_2016_2021_pct"].max()

gt = (
    GT(top, rowname_col="name")
    .tab_header(
        title="Population growth in Ontario's 15 largest cities",
        subtitle="2021 population and density, plus the five-year percent change across each Census window, 1996–2021",
    )
    .cols_label(
        population_2021="2021 pop.",
        density_2021=html("2021 density<br>(persons/km²)"),
        pop_change_1996_2001_pct="1996–2001",
        pop_change_2001_2006_pct="2001–2006",
        pop_change_2006_2011_pct="2006–2011",
        pop_change_2011_2016_pct="2011–2016",
        pop_change_2016_2021_pct="2016–2021",
    )
    .tab_spanner(label="Inter-Census growth", columns=change_cols)
    .fmt_integer(columns=["population_2021"])
    .fmt_number(columns=["density_2021"], decimals=1)
    # force_sign on the percent labels — the +/− gives a redundant directional
    # signal so the table remains usable for color-blind readers.
    .fmt_percent(columns=change_cols, decimals=1, force_sign=True)
    # Density: neutral magnitude → sequential Blues (fixed lookup). Colored
    # in place of raw population count — see the domain-skew note above.
    .data_color(
        columns=["density_2021"],
        palette="Blues",
        domain=[dens_lo, dens_hi],
        na_color="#808080",
        truncate=False,
        autocolor_text=True,
    )
    # Inter-Census growth: signed → diverging RdYlGn, one symmetric domain
    # shared across all five window columns. Positive = good (more residents).
    .data_color(
        columns=change_cols,
        palette="RdYlGn",
        domain=[-abs_max, abs_max],
        na_color="#808080",
        truncate=False,
        autocolor_text=True,
    )
    .cols_align(align="left", columns=["name"])
    .cols_align(align="right", columns=["population_2021", "density_2021"] + change_cols)
    # Column-group divider at the seam between the plain population column
    # and the colored block (density + the growth spanner).
    .tab_style(style=style.borders(sides="right", color="#D0D0D0", weight="1px"), locations=loc.body(columns="population_2021"))
    .tab_style(style=style.borders(sides="right", color="#D0D0D0", weight="1px"), locations=loc.column_labels(columns="population_2021"))
    # Heading band — fixed branding navy, bold labels, white text, every table.
    .tab_options(
        column_labels_background_color="#08306B",
        column_labels_font_weight="bold",
        column_labels_border_bottom_color="#CCCCCC",
        column_labels_border_bottom_width="2px",
    )
    .tab_style(style=style.text(color="white"), locations=loc.column_labels())
    # Stub tint — fixed branding hex, unconditional whenever a stub exists.
    .tab_style(style=style.fill(color="#EAF0F6"), locations=loc.stub())
    # Row striping — default on every table. Density and the five growth
    # columns are fully color-filled, but population_2021 is a genuine plain
    # column now (it lost its fill in favor of density, see the domain-skew
    # note above), so a stripe has a real plain cell to show through on.
    .opt_row_striping()
    .tab_options(
        row_striping_background_color="#F6F6F6",
        table_body_hlines_style="solid",
        table_body_hlines_color="#E8E8E8",
        table_body_hlines_width="1px",
        table_border_top_style="solid", table_border_top_color="#CCCCCC", table_border_top_width="1px",
        table_border_bottom_style="solid", table_border_bottom_color="#CCCCCC", table_border_bottom_width="1px",
        table_border_left_style="solid", table_border_left_color="#CCCCCC", table_border_left_width="1px",
        table_border_right_style="solid", table_border_right_color="#CCCCCC", table_border_right_width="1px",
    )
    .cols_width(cases={
        "name": "170px", "population_2021": "100px", "density_2021": "110px",
        **{c: "100px" for c in change_cols},
    })
    .tab_options(
        heading_padding="6px",
        column_labels_padding="6px",
        column_labels_padding_horizontal="8px",
        data_row_padding="5px",
        data_row_padding_horizontal="8px",
        source_notes_padding="6px",
    )
    .tab_source_note(
        source_note=html(
            f"{fastest_city} grew fastest in the most recent window (2016–2021, {fastest_pct:+.1%}) "
            "among these 15 cities."
        )
    )
    .tab_source_note(
        source_note=html(
            "Source: Statistics Canada Census of Population, 1996–2021, "
            "via the <code>towny</code> dataset (Posit / great_tables sample data)."
        )
    )
)

gt.gtsave("heatmap.png", zoom=2.0, expand=15)

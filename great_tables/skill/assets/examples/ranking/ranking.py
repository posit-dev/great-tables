"""Ranking archetype — distilled reference example.

Data: data/gtcars.csv  (47 high-performance cars)
Story: Top 10 production cars by horsepower, with the leader visually
       called out.
"""
import pandas as pd
from great_tables import GT, loc, style

df = pd.read_csv("data/gtcars.csv")

# Compose a single human label per row. Two separate mfr/model columns force
# the reader to combine them mentally on every row.
df["car"] = df["mfr"] + " " + df["model"]

# Sort by hp descending and take the top 10. The sort IS the message; an
# unsorted dump erases the archetype.
top = df.sort_values("hp", ascending=False).head(10).reset_index(drop=True)
top["rank"] = top.index + 1  # 1-based; leaderboards start at #1, not #0.
top = top[["rank", "car", "year", "ctry_origin", "hp", "trq", "drivetrain", "msrp"]]

leader = top.loc[0, "car"]
leader_hp = int(top.loc[0, "hp"])
runner_up_hp = int(top.loc[1, "hp"])

gt = (
    # rowname_col="rank" (not "car"): the fixed branding stub tint is a
    # table-wide surface with no per-row exception (see gt_check.py's
    # check_stub_tint) — the stub must stay uniformly tinted for every row,
    # including the leader's. Putting "car" in the stub would put the one
    # cell that most needs the leader highlight outside loc.body()'s reach.
    # references/big_color/full_row_highlight.md's own recipe uses
    # rowname_col="rank" for exactly this reason: the stub holds a plain
    # rank number that needs no highlight, and every column that carries
    # the story (including the car name) is a body column the highlight
    # can reach in one `loc.body()` call.
    GT(top, rowname_col="rank")
    .tab_stubhead(label="#")
    .tab_header(
        title="Top 10 by Horsepower",
        subtitle="Production cars in the gtcars dataset, ranked by peak HP",
    )
    .cols_label(
        car="Car", year="Year", ctry_origin="Country",
        hp="HP", trq="Torque (lb-ft)", drivetrain="Drive", msrp="MSRP",
    )
    .fmt_currency(columns=["msrp"], currency="USD", decimals=0)
    .fmt_integer(columns=["hp", "trq"])
    # use_seps=False on year — `2,017` is wrong for a year.
    .fmt_integer(columns=["year"], use_seps=False)
    # Full-row highlight on the #1 leader (a Top-N "winner" story) — a solid
    # Dark Academia hex with white text, spanning every body column. Every
    # other measure otherwise renders fully plain: no consolation bold.
    .tab_style(
        style=[style.fill(color="#9A7B33"), style.text(color="#ffffff", weight="bold")],
        locations=loc.body(rows=[0]),
    )
    .cols_align(align="left", columns=["car", "ctry_origin", "drivetrain"])
    .cols_align(align="right", columns=["year", "hp", "trq", "msrp"])
    # Heading band — fixed branding navy, bold labels, white text, every table.
    .tab_options(
        column_labels_background_color="#08306B",
        column_labels_font_weight="bold",
        column_labels_border_bottom_color="#CCCCCC",
        column_labels_border_bottom_width="2px",
    )
    .tab_style(style=style.text(color="white"), locations=loc.column_labels())
    # Stub tint — fixed branding hex, unconditional whenever a stub exists,
    # uniform across every row (no per-row exception, unlike the highlight
    # above, which lives entirely in the body now).
    .tab_style(style=style.fill(color="#EAF0F6"), locations=loc.stub())
    # Row striping — default on every table (only one row is highlighted).
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
        "car": "210px", "year": "70px", "ctry_origin": "110px",
        "hp": "80px", "trq": "110px", "drivetrain": "70px", "msrp": "110px",
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
        source_note=f"{leader} leads the field with {leader_hp} hp, {leader_hp - runner_up_hp} more than the #2 car."
    )
    .tab_source_note(source_note="Source: gtcars dataset (Posit / great_tables sample data).")
)

gt.gtsave("ranking.png", zoom=2.0, expand=15)

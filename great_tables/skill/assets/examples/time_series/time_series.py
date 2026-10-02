"""Time-series archetype — distilled reference example.

Data: data/airquality.csv  (NYC daily air quality, May-Sep 1973)
Story: Monthly summary across the summer, with ozone and temperature
       color-encoded as two distinct physical measurements, plus a
       signed month-over-month ozone delta.
"""
import pandas as pd
from great_tables import GT, html, loc, style

df = pd.read_csv("data/airquality.csv")

# Map numeric Month codes to human labels so the reader does not have to
# translate "Month=7" → "July" mentally on every row.
month_name = {5: "May", 6: "June", 7: "July", 8: "August", 9: "September"}

monthly = df.groupby("Month").agg(
    ozone_mean=("Ozone", "mean"),
    temp_mean=("Temp", "mean"),
    wind_mean=("Wind", "mean"),
    solar_mean=("Solar_R", "mean"),
).reset_index()

monthly["ozone_delta"] = monthly["ozone_mean"].diff()
monthly["month_label"] = monthly["Month"].map(month_name)
monthly = monthly[[
    "month_label", "ozone_mean", "ozone_delta",
    "temp_mean", "wind_mean", "solar_mean",
]]

# Ozone and temperature are different physical measurements — two genuinely
# distinct dimensions of "summer conditions" — so both earn a fill. Wind and
# solar radiation stay plain: they carry no narrative role in this request,
# not because of a numeric cap. Ozone is "more is worse" (a health-risk
# pollutant) → Reds; temperature is a neutral magnitude → Blues.
ozone_lo = float(monthly["ozone_mean"].min())
ozone_hi = float(monthly["ozone_mean"].max())
temp_lo = float(monthly["temp_mean"].min())
temp_hi = float(monthly["temp_mean"].max())

# ozone_delta is a near-redundant restatement of ozone_mean (its own
# month-over-month difference) — it stays plain text, but still needs
# force_sign since the underlying data crosses zero.
peak_month = monthly.loc[monthly["ozone_mean"].idxmax(), "month_label"]
peak_ozone = monthly["ozone_mean"].max()
trough_month = monthly.loc[monthly["ozone_mean"].idxmin(), "month_label"]

gt = (
    GT(monthly, rowname_col="month_label")
    .tab_header(
        title="NYC Air Quality — Summer 1973",
        subtitle="Monthly means and month-over-month ozone change",
    )
    # Spanners group the two ozone columns and the three condition columns so
    # the reader parses the units block at a time.
    .tab_spanner(label="Ozone (ppb)", columns=["ozone_mean", "ozone_delta"])
    .tab_spanner(label="Conditions", columns=["temp_mean", "wind_mean", "solar_mean"])
    .cols_label(
        ozone_mean="Mean",
        ozone_delta=html("&Delta; vs prev"),
        temp_mean=html("Temp (&deg;F)"),
        wind_mean="Wind (mph)",
        solar_mean=html("Solar (W/m&sup2;)"),
    )
    # One decimal: half a ppb is below instrument resolution; more would be
    # spurious precision.
    .fmt_number(columns=["ozone_mean", "temp_mean", "wind_mean", "solar_mean"], decimals=1)
    .fmt_number(columns=["ozone_delta"], decimals=1, force_sign=True)
    .sub_missing(columns=["ozone_delta"], missing_text="—")
    .data_color(
        columns=["ozone_mean"],
        palette="Reds",
        domain=[ozone_lo, ozone_hi],
        na_color="#808080",
        truncate=False,
        autocolor_text=True,
    )
    .data_color(
        columns=["temp_mean"],
        palette="Blues",
        domain=[temp_lo, temp_hi],
        na_color="#808080",
        truncate=False,
        autocolor_text=True,
    )
    .cols_align(align="right", columns=["ozone_mean", "ozone_delta", "temp_mean", "wind_mean", "solar_mean"])
    # Column-group divider at the Ozone/Conditions spanner seam.
    .tab_style(style=style.borders(sides="right", color="#D0D0D0", weight="1px"), locations=loc.body(columns="ozone_delta"))
    .tab_style(style=style.borders(sides="right", color="#D0D0D0", weight="1px"), locations=loc.column_labels(columns="ozone_delta"))
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
    # Row striping — default on every table (delta/wind/solar stay plain).
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
        "month_label": "100px", "ozone_mean": "80px", "ozone_delta": "90px",
        "temp_mean": "90px", "wind_mean": "90px", "solar_mean": "100px",
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
            f"Ozone peaked in {peak_month} ({peak_ozone:.1f} ppb) and was lowest in {trough_month}."
        )
    )
    .tab_source_note(
        source_note="Source: New York State Department of Conservation, daily measurements May–September 1973."
    )
)

gt.gtsave("time_series.png", zoom=2.0, expand=15)

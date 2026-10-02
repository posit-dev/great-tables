"""Financial archetype — distilled reference example.

Data: data/sp500.csv  (S&P 500 daily prices, 1950-2015)
Story: At-a-glance monthly summary of the S&P 500 in 2015 - closing
       level, intraday range, month-over-month return, year-to-date
       return.
"""
import numpy as np
import pandas as pd
from great_tables import GT, loc, style

df = pd.read_csv("data/sp500.csv", parse_dates=["date"]).sort_values("date")

# Restrict to the most recent full year. Twelve rows is the cap most readers
# can scan without scrolling or grouping.
year = df[df["date"].dt.year == 2015].copy()
year["month"] = year["date"].dt.to_period("M")

# Month-end close: last observation in the month, not a mean (mean smears
# the month and would not reconcile with the published close).
monthly = year.groupby("month").agg(
    close=("close", "last"),
    high=("high", "max"),
    low=("low", "min"),
)

# Use the prior-year close as the baseline so January's MoM is meaningful
# (and YTD has an anchor).
prior_year_close = df.loc[df["date"] == "2014-12-31", "close"].iloc[0]
monthly["mom_return"] = monthly["close"].pct_change()
monthly.loc[monthly.index[0], "mom_return"] = (
    monthly["close"].iloc[0] / prior_year_close - 1
)
monthly["ytd_return"] = monthly["close"] / prior_year_close - 1
monthly = monthly.reset_index()
monthly["month_label"] = monthly["month"].dt.strftime("%b %Y")
monthly = monthly[["month_label", "close", "high", "low", "mom_return", "ytd_return"]].reset_index(drop=True)

# MoM and YTD are both signed, positive-is-good measures, but they are two
# genuinely distinct dimensions of "performance" (a single-month rate vs. a
# cumulative-since-January rate) — each earns its OWN diverging fill with its
# OWN symmetric, data-driven domain. Close/high/low stay plain: in a real
# performance recap the reader scans color for the SIGNAL (up or down), not
# for the absolute price level, so heatmapping the price block would just add
# noise without adding information.
mom_m = float(np.nanmax(np.abs(monthly["mom_return"].to_numpy())))
ytd_m = float(np.nanmax(np.abs(monthly["ytd_return"].to_numpy())))

best_month = monthly.loc[monthly["mom_return"].idxmax(), "month_label"]
best_month_pct = monthly["mom_return"].max()
year_return = monthly["ytd_return"].iloc[-1]

gt = (
    GT(monthly, rowname_col="month_label")
    .tab_header(
        title="S&P 500 — 2015 Year in Review",
        subtitle="Month-end close, intraday range, and returns",
    )
    # Spanners group the columns under one label so the reader parses "Return"
    # once instead of twice.
    .tab_spanner(label="Price ($)", columns=["close", "high", "low"])
    .tab_spanner(label="Return", columns=["mom_return", "ytd_return"])
    .cols_label(
        close="Close", high="High", low="Low",
        mom_return="MoM", ytd_return="YTD",
    )
    # fmt_currency on prices — renders the $, thousands separator, and decimals
    # as one locale-aware unit. fmt_number + a manual prefix breaks under RTL.
    .fmt_currency(columns=["close", "high", "low"], currency="USD", decimals=2)
    # force_sign=True so the leading + is the at-a-glance up/down signal —
    # independent of whether the column is also colored.
    .fmt_percent(columns=["mom_return", "ytd_return"], decimals=2, force_sign=True)
    .data_color(
        columns=["mom_return"],
        palette="RdYlGn",
        domain=[-mom_m, mom_m],
        na_color="#808080",
        truncate=False,
        autocolor_text=True,
    )
    .data_color(
        columns=["ytd_return"],
        palette="RdYlGn",
        domain=[-ytd_m, ytd_m],
        na_color="#808080",
        truncate=False,
        autocolor_text=True,
    )
    .cols_align(align="right", columns=["close", "high", "low", "mom_return", "ytd_return"])
    # Column-group vertical divider at the Price/Return spanner seam.
    .tab_style(style=style.borders(sides="right", color="#D0D0D0", weight="1px"), locations=loc.body(columns="low"))
    .tab_style(style=style.borders(sides="right", color="#D0D0D0", weight="1px"), locations=loc.column_labels(columns="low"))
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
    # Row striping — default on every table. Price stays plain so the body is
    # nowhere near 100% color-filled.
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
        "month_label": "90px", "close": "90px", "high": "90px", "low": "90px",
        "mom_return": "80px", "ytd_return": "80px",
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
        source_note=(
            f"{best_month} was the strongest month ({best_month_pct:+.1%} MoM); the index "
            f"finished 2015 at {year_return:+.1%} YTD. January's MoM and YTD both use the "
            "2014 year-end close as the baseline, so every month has a defined return."
        )
    )
    .tab_source_note(source_note="Source: S&P 500 daily closing prices, 2015.")
)

gt.gtsave("financial.png", zoom=2.0, expand=15)

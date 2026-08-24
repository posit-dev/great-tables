"""Summary-statistics archetype — distilled reference example.

Data: data/pizzaplace.csv  (49,574 individual pizza orders)
Story: Per-category, per-size sales totals with subtotals per category
       and a grand total at the bottom.
"""
import pandas as pd
from great_tables import GT, loc, style

df = pd.read_csv("data/pizzaplace.csv")

agg = (
    df.groupby(["type", "size"])
      .agg(orders=("id", "count"),
           revenue=("price", "sum"),
           avg_price=("price", "mean"))
      .reset_index()
)

# Ordered Categorical on size so rows land S → M → L → XL → XXL rather than
# alphabetic. Without ordered=True pandas would default to L, M, S, XL, XXL.
size_order = ["S", "M", "L", "XL", "XXL"]
agg["size"] = pd.Categorical(agg["size"], categories=size_order, ordered=True)
agg["type"] = agg["type"].map({"classic": "Classic", "veggie": "Veggie",
                                "chicken": "Chicken", "supreme": "Supreme"})
agg = agg.sort_values(["type", "size"]).reset_index(drop=True)

top_category = agg.groupby("type")["revenue"].sum().idxmax()
rev_lo = float(agg["revenue"].min())
rev_hi = float(agg["revenue"].max())

gt = (
    # rowname_col + groupname_col is the gt-native way to express a two-level
    # row layout: group banners on `type`, indented size labels under each.
    GT(agg, rowname_col="size", groupname_col="type")
    .tab_header(
        title="Pizza Sales by Category and Size",
        subtitle="Full-year totals across the four menu categories",
    )
    .cols_label(orders="Orders", revenue="Revenue", avg_price="Avg. price")
    .fmt_currency(columns=["revenue", "avg_price"], currency="USD", decimals=2)
    .fmt_integer(columns=["orders"])
    # Revenue is the headline business metric this table exists to compare —
    # a sequential Blues gradient (neutral magnitude). Orders and avg. price
    # stay plain: orders is a count that tracks revenue closely at this
    # aggregation level, and avg. price is a derived ratio of the other two,
    # not a distinct third dimension.
    .data_color(
        columns=["revenue"],
        palette="Blues",
        domain=[rev_lo, rev_hi],
        na_color="#808080",
        truncate=False,
        autocolor_text=True,
    )
    # Per-category subtotal — the story this archetype exists to demonstrate.
    # summary_rows()/grand_summary_rows() raise NotImplementedError if you pass
    # columns= to scope a fmt= call to specific columns in one call, so a
    # single shared formatter can't treat "orders" and "revenue" differently.
    # The workaround: have the aggregation function itself return an
    # already-formatted string per column (matching the body's currency
    # style for revenue, plain comma-grouped integers for orders) and omit
    # fmt= entirely — great_tables renders a pre-formatted string as literal
    # text without re-formatting it.
    .summary_rows(
        groups=list(agg["type"].unique()),
        fns={"Subtotal": lambda d: pd.Series({
            "orders": f"{int(d['orders'].sum()):,}",
            "revenue": f"${float(d['revenue'].sum()):,.2f}",
        })},
        missing_text="",
    )
    # Grand summary row at the bottom — the headline number a manager carries
    # away. Callable form returning pd.Series is the pandas escape; pl.col
    # expressions only work on polars-backed tables. avg_price is omitted
    # because a mean-of-means is not meaningful. Same pre-formatted-string
    # workaround as the subtotal rows above, so the grand total keeps its $.
    .grand_summary_rows(
        fns={"All categories": lambda d: pd.Series({
            "orders": f"{int(d['orders'].sum()):,}",
            "revenue": f"${float(d['revenue'].sum()):,.2f}",
        })},
        missing_text="",
    )
    # Group header emphasis: bold weight + structural rules, never a fill —
    # a fill would compete with the header band's own branding role.
    .tab_options(
        row_group_font_weight="bold",
        row_group_border_top_color="#BDBDBD",
        row_group_border_bottom_color="#BDBDBD",
        row_group_padding="6px",
    )
    .cols_align(align="right", columns=["orders", "revenue", "avg_price"])
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
    # Row striping — default on every table (orders/avg. price stay plain).
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
    .cols_width(cases={"size": "120px", "orders": "90px", "revenue": "110px", "avg_price": "100px"})
    .tab_options(
        heading_padding="6px",
        column_labels_padding="6px",
        column_labels_padding_horizontal="8px",
        data_row_padding="5px",
        data_row_padding_horizontal="8px",
        source_notes_padding="6px",
    )
    .tab_source_note(source_note=f"{top_category} is the top-grossing category for the year.")
    .tab_source_note(source_note="Source: pizzaplace dataset (Posit / great_tables sample data).")
)

gt.gtsave("summary_stats.png", zoom=2.0, expand=15)

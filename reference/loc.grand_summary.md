# loc.grand_summary

Target the data cells in grand summary rows.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_locations.py#L803-L863)

``` python
loc.grand_summary(
    columns=None,
    rows=None,
    mask=None,
)
```

With [loc.grand_summary()](../reference/loc.grand_summary.md#great_tables.loc.grand_summary) we can target the cells containing the grand summary data. This is useful for applying custom styling with the [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style) method. That method has a `locations=` argument and this class should be used there to perform the targeting.

## Parameters

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
The rows to target. Can either be a single row name or a series of row names provided in a list. Note that if rows are targeted by index, top and bottom grand summary rows are indexed as one combined list starting with the top rows.

## Returns

`LocGrandSummary`  
A LocGrandSummary object, which is used for a `locations=` argument if specifying the table's grand summary rows.

## Examples

Let's use a subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We will style all of the grand summary cells by using `locations=loc.grand_summary()` within [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style).

``` python
from great_tables import GT, style, loc, vals
from great_tables.data import gtcars

(
    GT(
        gtcars[["mfr", "model", "hp", "trq", "mpg_c"]].head(6),
        rowname_col="model",
    )
    .fmt_integer(columns=["hp", "trq", "mpg_c"])
    .grand_summary_rows(
        fns={
            "Min": lambda df: df.min(numeric_only=True),
            "Max": lambda x: x.max(numeric_only=True),
        },
        side="top",
        fmt=vals.fmt_integer,
    )
    .tab_style(
        style=[style.text(color="crimson", weight="bold"), style.fill(color="lightgray")],
        locations=loc.grand_summary(),
    )
)
```

|              | mfr     | hp  | trq | mpg_c |
|--------------|---------|-----|-----|-------|
| Min          | ---     | 553 | 398 | 11    |
| Max          | ---     | 661 | 561 | 16    |
| GT           | Ford    | 647 | 550 | 11    |
| 458 Speciale | Ferrari | 597 | 398 | 13    |
| 458 Spider   | Ferrari | 562 | 398 | 13    |
| 458 Italia   | Ferrari | 562 | 398 | 13    |
| 488 GTB      | Ferrari | 661 | 561 | 15    |
| California   | Ferrari | 553 | 557 | 16    |

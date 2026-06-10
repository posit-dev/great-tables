## GT.grand_summary_rows()


Add grand summary rows to the table.


Usage

``` python
GT.grand_summary_rows(
    *, fns, fmt=None, columns=None, side="bottom", missing_text="---"
)
```


Add grand summary rows by using the table data and any suitable aggregation functions. With grand summary rows, all of the available data in the gt table is incorporated (regardless of whether some of the data are part of row groups). Multiple grand summary rows can be added via expressions given to fns. You can selectively format the values in the resulting grand summary cells by use of formatting expressions from the `vals.fmt_*` class of functions.

Note that currently all arguments are keyword-only, since the final positions may change.


## Parameters


`fns: dict[str, PlExpr] | dict[str, Callable[[TblData], Any]]`  
A dictionary mapping row labels to aggregation expressions. Can be either Polars expressions or callable functions that take the entire DataFrame and return aggregated results. Each key becomes the label for a grand summary row.

`fmt: FormatFn | None = None`  
A formatting function from the `vals.fmt_*` family (e.g., [vals.fmt_number](vals.fmt_number.md#great_tables.vals.fmt_number), [vals.fmt_currency](vals.fmt_currency.md#great_tables.vals.fmt_currency)) to apply to the summary row values. If `None`, no formatting is applied.

`columns: SelectExpr = None`  
Currently, this function does not support selection by columns. If you would like to choose which columns to summarize, you can select columns within the functions given to `fns=`. See examples below for more explicit cases.

`side: Literal[``"bottom", `<span class="st">`"top"``]`</span>` = ``"bottom"`  
Should the grand summary rows be placed at the `"bottom"` (the default) or the `"top"` of the table?

`missing_text: str = ``"--"`  
The text to be used in summary cells with no data outputs.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use a subset of the [sp500](data.sp500.md#great_tables.data.sp500) dataset to create a table with grand summary rows. We'll calculate min, max, and mean values for the numeric columns. Notice the different approaches to selecting columns to apply the aggregations to: we can use polars selectors or select the columns directly.


``` python
import polars as pl
import polars.selectors as cs
from great_tables import GT, vals, style, loc
from great_tables.data import sp500

sp500_mini = (
    pl.from_pandas(sp500)
    .slice(0, 7)
    .drop(["volume", "adj_close"])
)

(
    GT(sp500_mini, rowname_col="date")
    .grand_summary_rows(
        fns={
            "Minimum": pl.min("open", "high", "low", "close"),
            "Maximum": pl.col("open", "high", "low", "close").max(),
            "Average": cs.numeric().mean(),
        },
        fmt=vals.fmt_currency,
    )
    .tab_style(
        style=[
            style.text(color="crimson"),
            style.fill(color="lightgray"),
        ],
        locations=loc.grand_summary(),
    )
)
```


|            | open       | high       | low        | close      |
|------------|------------|------------|------------|------------|
| 2015-12-31 | 2060.5901  | 2062.54    | 2043.62    | 2043.9399  |
| 2015-12-30 | 2077.3401  | 2077.3401  | 2061.97    | 2063.3601  |
| 2015-12-29 | 2060.54    | 2081.5601  | 2060.54    | 2078.3601  |
| 2015-12-28 | 2057.77    | 2057.77    | 2044.2     | 2056.5     |
| 2015-12-24 | 2063.52    | 2067.3601  | 2058.73    | 2060.99    |
| 2015-12-23 | 2042.2     | 2064.73    | 2042.2     | 2064.29    |
| 2015-12-22 | 2023.15    | 2042.74    | 2020.49    | 2038.97    |
| Minimum    | \$2,023.15 | \$2,042.74 | \$2,020.49 | \$2,038.97 |
| Maximum    | \$2,077.34 | \$2,081.56 | \$2,061.97 | \$2,078.36 |
| Average    | \$2,055.02 | \$2,064.86 | \$2,047.39 | \$2,058.06 |


We can also use custom callable functions to create more complex summary calculations. Notice here that grand summary rows can be placed at the top of the table and formatted with currency notation, by passing a formatter from the `vals.fmt_*` class of functions.


``` python
from great_tables import GT, style, loc, vals
from great_tables.data import gtcars

def pd_median(df):
    return df.median(numeric_only=True)


(
    GT(
        gtcars[["mfr", "model", "hp", "trq", "mpg_c"]].head(6),
        rowname_col="model",
    )
    .fmt_integer(columns=["hp", "trq", "mpg_c"])
    .grand_summary_rows(
        fns={
            "Min": lambda df: df.min(numeric_only=True),
            "Max": lambda df: df.max(numeric_only=True),
            "Median": pd_median,
        },
        side="top",
        fmt=vals.fmt_integer,
    )
    .tab_style(
        style=[style.text(color="crimson", weight="bold"), style.fill(color="lightgray")],
        locations=loc.grand_summary_stub(),
    )
)
```


|              | mfr     | hp  | trq | mpg_c |
|--------------|---------|-----|-----|-------|
| Min          | ---     | 553 | 398 | 11    |
| Max          | ---     | 661 | 561 | 16    |
| Median       | ---     | 580 | 474 | 13    |
| GT           | Ford    | 647 | 550 | 11    |
| 458 Speciale | Ferrari | 597 | 398 | 13    |
| 458 Spider   | Ferrari | 562 | 398 | 13    |
| 458 Italia   | Ferrari | 562 | 398 | 13    |
| 488 GTB      | Ferrari | 661 | 561 | 15    |
| California   | Ferrari | 553 | 557 | 16    |

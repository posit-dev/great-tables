# GT.summary_rows()

Add group-wise summary rows to the table.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_modify_rows.py#L209-L463)

``` python
GT.summary_rows(
    *,
    fns,
    fmt=None,
    columns=None,
    groups=None,
    side="bottom",
    missing_text="---",
)
```

Add summary rows by using the table data and any suitable aggregation functions. With [summary_rows()](../reference/GT.summary_rows.md#great_tables.GT.summary_rows), the data within each row group is aggregated separately and summary rows are placed adjacent to each group. Multiple summary rows can be added via expressions given to `fns=`. You can selectively format the values in the resulting summary cells by use of formatting expressions from the `vals.fmt_*` class of functions.

Note that currently all arguments are keyword-only, since the final positions may change.

## Parameters

`fns: dict[str, PlExpr] | dict[str, Callable[[TblData], Any]]`  
A dictionary mapping row labels to aggregation expressions. Can be either Polars expressions or callable functions that take a DataFrame subset and return aggregated results. Each key becomes the label for a summary row within each group.

`fmt: FormatFn | None = None`  
A formatting function from the `vals.fmt_*` family (e.g., [vals.fmt_number](../reference/vals.fmt_number.md#great_tables.vals.fmt_number), [vals.fmt_currency](../reference/vals.fmt_currency.md#great_tables.vals.fmt_currency)) to apply to the summary row values. If `None`, no formatting is applied.

`columns: SelectExpr = None`  
Currently, this function does not support selection by columns. If you would like to choose which columns to summarize, you can select columns within the functions given to `fns=`. See examples below for more explicit cases.

`groups: list[str] | None = None`  
The groups to target for summary row insertion. Can be a list of group IDs as strings. By default (`None`), summary rows are generated for all groups.

`side: Literal["bottom", "top"] = "bottom"`  
Should the summary rows be placed at the `"bottom"` (the default) or the `"top"` of each group?

`missing_text: str = "--"`  
The text to be used in summary cells with no data outputs.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Let's use a subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset to create a table with group summary rows. We'll group by manufacturer and show min and max values for horsepower and torque columns.

``` python
import polars as pl
from great_tables import GT, vals
from great_tables.data import gtcars

gtcars_mini = (
    pl.from_pandas(gtcars)
    .select(["mfr", "model", "hp", "trq"])
    .head(12)
)

(
    GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
    .summary_rows(
        fns={
            "Min": pl.col("hp", "trq").min(),
            "Max": pl.col("hp", "trq").max(),
        },
        fmt=vals.fmt_integer,
    )
)
```

|               | hp    | trq   |
|---------------|-------|-------|
| Ford          |       |       |
| GT            | 647.0 | 550.0 |
| Min           | 647   | 550   |
| Max           | 647   | 550   |
| Ferrari       |       |       |
| 458 Speciale  | 597.0 | 398.0 |
| 458 Spider    | 562.0 | 398.0 |
| 458 Italia    | 562.0 | 398.0 |
| 488 GTB       | 661.0 | 561.0 |
| California    | 553.0 | 557.0 |
| GTC4Lusso     | 680.0 | 514.0 |
| FF            | 652.0 | 504.0 |
| F12Berlinetta | 731.0 | 509.0 |
| LaFerrari     | 949.0 | 664.0 |
| Min           | 553   | 398   |
| Max           | 949   | 664   |
| Acura         |       |       |
| NSX           | 573.0 | 476.0 |
| Min           | 573   | 476   |
| Max           | 573   | 476   |
| Nissan        |       |       |
| GT-R          | 545.0 | 436.0 |
| Min           | 545   | 436   |
| Max           | 545   | 436   |

We can also target specific groups by using the `groups=` parameter. Here we only show summary rows for the `"Ferrari"` group:

``` python
(
    GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
    .summary_rows(
        fns={
            "Average": pl.col("hp", "trq").mean(),
        },
        groups=["Ferrari"],
        fmt=vals.fmt_number,
    )
)
```

|               | hp     | trq    |
|---------------|--------|--------|
| Ford          |        |        |
| GT            | 647.0  | 550.0  |
| Ferrari       |        |        |
| 458 Speciale  | 597.0  | 398.0  |
| 458 Spider    | 562.0  | 398.0  |
| 458 Italia    | 562.0  | 398.0  |
| 488 GTB       | 661.0  | 561.0  |
| California    | 553.0  | 557.0  |
| GTC4Lusso     | 680.0  | 514.0  |
| FF            | 652.0  | 504.0  |
| F12Berlinetta | 731.0  | 509.0  |
| LaFerrari     | 949.0  | 664.0  |
| Average       | 660.78 | 500.33 |
| Acura         |        |        |
| NSX           | 573.0  | 476.0  |
| Nissan        |        |        |
| GT-R          | 545.0  | 436.0  |

Callable functions work with pandas DataFrames. Each function receives the subset of data for that group:

``` python
from great_tables import GT, vals
from great_tables.data import gtcars

(
    GT(
        gtcars[["mfr", "model", "hp", "trq"]].head(12),
        rowname_col="model",
        groupname_col="mfr",
    )
    .summary_rows(
        fns={
            "Min": lambda df: df.min(numeric_only=True),
            "Max": lambda df: df.max(numeric_only=True),
        },
        fmt=vals.fmt_integer,
    )
)
```

|               | hp    | trq   |
|---------------|-------|-------|
| Ford          |       |       |
| GT            | 647.0 | 550.0 |
| Min           | 647   | 550   |
| Max           | 647   | 550   |
| Ferrari       |       |       |
| 458 Speciale  | 597.0 | 398.0 |
| 458 Spider    | 562.0 | 398.0 |
| 458 Italia    | 562.0 | 398.0 |
| 488 GTB       | 661.0 | 561.0 |
| California    | 553.0 | 557.0 |
| GTC4Lusso     | 680.0 | 514.0 |
| FF            | 652.0 | 504.0 |
| F12Berlinetta | 731.0 | 509.0 |
| LaFerrari     | 949.0 | 664.0 |
| Min           | 553   | 398   |
| Max           | 949   | 664   |
| Acura         |       |       |
| NSX           | 573.0 | 476.0 |
| Min           | 573   | 476   |
| Max           | 573   | 476   |
| Nissan        |       |       |
| GT-R          | 545.0 | 436.0 |
| Min           | 545   | 436   |
| Max           | 545   | 436   |

Summary rows can be placed at the top of each group using `side="top"`:

``` python
import polars as pl
from great_tables import GT, vals
from great_tables.data import gtcars

gtcars_mini = (
    pl.from_pandas(gtcars)
    .select(["mfr", "model", "hp", "trq"])
    .head(12)
)

(
    GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
    .summary_rows(
        fns={"Mean": pl.col("hp", "trq").mean()},
        side="top",
        fmt=vals.fmt_number,
    )
)
```

|               | hp     | trq    |
|---------------|--------|--------|
| Ford          |        |        |
| Mean          | 647.00 | 550.00 |
| GT            | 647.0  | 550.0  |
| Ferrari       |        |        |
| Mean          | 660.78 | 500.33 |
| 458 Speciale  | 597.0  | 398.0  |
| 458 Spider    | 562.0  | 398.0  |
| 458 Italia    | 562.0  | 398.0  |
| 488 GTB       | 661.0  | 561.0  |
| California    | 553.0  | 557.0  |
| GTC4Lusso     | 680.0  | 514.0  |
| FF            | 652.0  | 504.0  |
| F12Berlinetta | 731.0  | 509.0  |
| LaFerrari     | 949.0  | 664.0  |
| Acura         |        |        |
| Mean          | 573.00 | 476.00 |
| NSX           | 573.0  | 476.0  |
| Nissan        |        |        |
| Mean          | 545.00 | 436.00 |
| GT-R          | 545.0  | 436.0  |

Combining group summaries with grand summary rows and styling provides a comprehensive summary view of the data. Use `loc.summary()` to style all group summary cells:

``` python
import polars as pl
from great_tables import GT, vals, style, loc
from great_tables.data import gtcars

gtcars_mini = (
    pl.from_pandas(gtcars)
    .select(["mfr", "model", "hp", "trq"])
    .head(12)
)

(
    GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
    .summary_rows(
        fns={
            "Min": pl.col("hp", "trq").min(),
            "Max": pl.col("hp", "trq").max(),
        },
        fmt=vals.fmt_integer,
    )
    .grand_summary_rows(
        fns={"Overall Mean": pl.col("hp", "trq").mean()},
        fmt=vals.fmt_number,
    )
    .tab_style(
        style=[style.fill(color="lightyellow")],
        locations=loc.summary(),
    )
    .tab_style(
        style=[style.fill(color="lightblue")],
        locations=loc.grand_summary(),
    )
)
```

|               | hp     | trq    |
|---------------|--------|--------|
| Ford          |        |        |
| GT            | 647.0  | 550.0  |
| Min           | 647    | 550    |
| Max           | 647    | 550    |
| Ferrari       |        |        |
| 458 Speciale  | 597.0  | 398.0  |
| 458 Spider    | 562.0  | 398.0  |
| 458 Italia    | 562.0  | 398.0  |
| 488 GTB       | 661.0  | 561.0  |
| California    | 553.0  | 557.0  |
| GTC4Lusso     | 680.0  | 514.0  |
| FF            | 652.0  | 504.0  |
| F12Berlinetta | 731.0  | 509.0  |
| LaFerrari     | 949.0  | 664.0  |
| Min           | 553    | 398    |
| Max           | 949    | 664    |
| Acura         |        |        |
| NSX           | 573.0  | 476.0  |
| Min           | 573    | 476    |
| Max           | 573    | 476    |
| Nissan        |        |        |
| GT-R          | 545.0  | 436.0  |
| Min           | 545    | 436    |
| Max           | 545    | 436    |
| Overall Mean  | 642.67 | 497.08 |

When groups are displayed as a column in the stub (using `row_group_as_column=True`), the summary row labels span the stub columns:

``` python
import polars as pl
from great_tables import GT, vals
from great_tables.data import gtcars

gtcars_mini = (
    pl.from_pandas(gtcars)
    .select(["mfr", "model", "hp", "trq"])
    .head(12)
)

(
    GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
    .tab_options(row_group_as_column=True)
    .summary_rows(
        fns={
            "Min": pl.col("hp", "trq").min(),
            "Max": pl.col("hp", "trq").max(),
        },
        fmt=vals.fmt_integer,
    )
)
```

|         |               | hp    | trq   |
|---------|---------------|-------|-------|
| Ford    | GT            | 647.0 | 550.0 |
|         | Min           | 647   | 550   |
|         | Max           | 647   | 550   |
| Ferrari | 458 Speciale  | 597.0 | 398.0 |
|         | 458 Spider    | 562.0 | 398.0 |
|         | 458 Italia    | 562.0 | 398.0 |
|         | 488 GTB       | 661.0 | 561.0 |
|         | California    | 553.0 | 557.0 |
|         | GTC4Lusso     | 680.0 | 514.0 |
|         | FF            | 652.0 | 504.0 |
|         | F12Berlinetta | 731.0 | 509.0 |
|         | LaFerrari     | 949.0 | 664.0 |
|         | Min           | 553   | 398   |
|         | Max           | 949   | 664   |
| Acura   | NSX           | 573.0 | 476.0 |
|         | Min           | 573   | 476   |
|         | Max           | 573   | 476   |
| Nissan  | GT-R          | 545.0 | 436.0 |
|         | Min           | 545   | 436   |
|         | Max           | 545   | 436   |

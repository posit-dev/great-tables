# GT.tab_spanner()

Insert a spanner above a selection of column headings.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_spanners.py#L27-L272)

``` python
GT.tab_spanner(
    label,
    columns=None,
    spanners=None,
    level=None,
    id=None,
    gather=True,
    replace=False,
)
```

This part of the table contains, at a minimum, column labels and, optionally, an unlimited number of levels for spanners. A spanner will occupy space over any number of contiguous column labels and it will have an associated label and ID value. This method allows for mapping to be defined by column names, existing spanner ID values, or a mixture of both.

The spanners are placed in the order of calling [tab_spanner()](../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner) so if a later call uses the same columns in its definition (or even a subset) as the first invocation, the second spanner will be overlaid atop the first. Options exist for forcibly inserting a spanner underneath others (with `level` as space permits) and with `replace`, which allows for full or partial spanner replacement.

## Parameters

`label: str | BaseText`  
The text to use for the spanner label. We can optionally use the [`md()`](../reference/md.md#great_tables.md) and [`html()`](../reference/html.md#great_tables.md) helper functions to style the text as Markdown or to retain HTML elements in the text. Alternatively, units notation can be used (see [`define_units()`](../reference/define_units.md#great_tables.define_units) for details).

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`spanners: str | list[str] | None = None`  
The spanners that should be spanned over, should they already be defined. One or more spanner ID values (in quotes) can be supplied here. This argument works in tandem with the `columns` argument.

`level: int | None = None`  
An explicit level to which the spanner should be placed. If not provided, **Great Tables** will choose the level based on the inputs provided within `columns` and `spanners`, placing the spanner label where it will fit. The first spanner level (right above the column labels) is `0`.

`id: str | None = None`  
The ID for the spanner. When accessing a spanner through the `spanners` argument of [tab_spanner()](../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner) the `id` value is used as the reference (and not the `label`). If an `id` is not explicitly provided here, it will be taken from the `label` value. It is advisable to set an explicit `id` value if you plan to access this cell in a later call and the label text is complicated (e.g., contains markup, is lengthy, or both). Finally, when providing an `id` value you must ensure that it is unique across all ID values set for spanner labels (the method will throw an error if `id` isn't unique).

`gather: bool = True`  
An option to move the specified `columns` such that they are unified under the spanner. Ordering of the moved-into-place columns will be preserved in all cases. By default, this is set to `True`.

`replace: bool = False`  
Should new spanners be allowed to partially or fully replace existing spanners? (This is a possibility if setting spanners at an already populated `level`.) By default, this is set to `False` and an error will occur if some replacement is attempted.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Let's create a table using a small portion of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset. Over several columns (`hp`, `hp_rpm`, `trq`, `trq_rpm`, `mpg_c`, `mpg_h`) we'll use [tab_spanner()](../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner) to add a spanner with the label `"performance"`. This effectively groups together several columns related to car performance under a unifying label.

``` python
from great_tables import GT, md
from great_tables.data import gtcars

colnames = ["model", "hp", "hp_rpm", "trq", "trq_rpm", "mpg_c", "mpg_h"]
gtcars_mini = gtcars[colnames].head(10)

(
    GT(gtcars_mini)
    .tab_spanner(
        label="performance",
        columns=["hp", "hp_rpm", "trq", "trq_rpm", "mpg_c", "mpg_h"]
    )
)
```

| model         | performance |        |       |         |       |       |
|---------------|-------------|--------|-------|---------|-------|-------|
|               | hp          | hp_rpm | trq   | trq_rpm | mpg_c | mpg_h |
| GT            | 647.0       | 6250.0 | 550.0 | 5900.0  | 11.0  | 18.0  |
| 458 Speciale  | 597.0       | 9000.0 | 398.0 | 6000.0  | 13.0  | 17.0  |
| 458 Spider    | 562.0       | 9000.0 | 398.0 | 6000.0  | 13.0  | 17.0  |
| 458 Italia    | 562.0       | 9000.0 | 398.0 | 6000.0  | 13.0  | 17.0  |
| 488 GTB       | 661.0       | 8000.0 | 561.0 | 3000.0  | 15.0  | 22.0  |
| California    | 553.0       | 7500.0 | 557.0 | 4750.0  | 16.0  | 23.0  |
| GTC4Lusso     | 680.0       | 8250.0 | 514.0 | 5750.0  | 12.0  | 17.0  |
| FF            | 652.0       | 8000.0 | 504.0 | 6000.0  | 11.0  | 16.0  |
| F12Berlinetta | 731.0       | 8250.0 | 509.0 | 6000.0  | 11.0  | 16.0  |
| LaFerrari     | 949.0       | 9000.0 | 664.0 | 6750.0  | 12.0  | 16.0  |

One cool feature of [tab_spanner()](../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner) is its support for multiple levels, allowing you to group columns in various ways. For example, you can create three bottom spanners and a top spanner:

``` python
(
    GT(gtcars_mini)
    .tab_spanner(
        label="hp",
        columns=["hp", "hp_rpm"],
    )
    .tab_spanner(
        label="trq",
        columns=["trq", "trq_rpm"],
    )
    .tab_spanner(
        label="mpg",
        columns=["mpg_c", "mpg_h"],
    )
    .tab_spanner(
        label="performance",
        columns=["hp", "hp_rpm", "trq", "trq_rpm", "mpg_c", "mpg_h"],
    )
)
```

|               | performance |        |       |         |       |       |
|---------------|-------------|--------|-------|---------|-------|-------|
| model         | hp          |        | trq   |         | mpg   |       |
|               | hp          | hp_rpm | trq   | trq_rpm | mpg_c | mpg_h |
| GT            | 647.0       | 6250.0 | 550.0 | 5900.0  | 11.0  | 18.0  |
| 458 Speciale  | 597.0       | 9000.0 | 398.0 | 6000.0  | 13.0  | 17.0  |
| 458 Spider    | 562.0       | 9000.0 | 398.0 | 6000.0  | 13.0  | 17.0  |
| 458 Italia    | 562.0       | 9000.0 | 398.0 | 6000.0  | 13.0  | 17.0  |
| 488 GTB       | 661.0       | 8000.0 | 561.0 | 3000.0  | 15.0  | 22.0  |
| California    | 553.0       | 7500.0 | 557.0 | 4750.0  | 16.0  | 23.0  |
| GTC4Lusso     | 680.0       | 8250.0 | 514.0 | 5750.0  | 12.0  | 17.0  |
| FF            | 652.0       | 8000.0 | 504.0 | 6000.0  | 11.0  | 16.0  |
| F12Berlinetta | 731.0       | 8250.0 | 509.0 | 6000.0  | 11.0  | 16.0  |
| LaFerrari     | 949.0       | 9000.0 | 664.0 | 6750.0  | 12.0  | 16.0  |

Did you notice that the spanners stacked automatically? What if you want granular control to specify a spanner in a specific hierarchy? **Great Tables** has you covered. By using the `level=` parameter, you can easily adjust the hierarchy of spanners. For example, by specifying `level=0` for the last call of [tab_spanner()](../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner), you can place that spanner at the bottom level (level `0`) instead of the top level (level `2`).

``` python
(
    GT(gtcars_mini)
    .tab_spanner(
        label="hp",
        columns=["hp", "hp_rpm"],
    )
    .tab_spanner(
        label="performance",
        columns=["hp", "hp_rpm", "trq", "trq_rpm"],
    )
    .tab_spanner(
        label="trq",
        columns=["trq", "trq_rpm"],
        level=0,
    )
)
```

|               | performance |        |       |         |       |       |
|---------------|-------------|--------|-------|---------|-------|-------|
| model         | hp          |        | trq   |         | mpg_c | mpg_h |
|               | hp          | hp_rpm | trq   | trq_rpm |       |       |
| GT            | 647.0       | 6250.0 | 550.0 | 5900.0  | 11.0  | 18.0  |
| 458 Speciale  | 597.0       | 9000.0 | 398.0 | 6000.0  | 13.0  | 17.0  |
| 458 Spider    | 562.0       | 9000.0 | 398.0 | 6000.0  | 13.0  | 17.0  |
| 458 Italia    | 562.0       | 9000.0 | 398.0 | 6000.0  | 13.0  | 17.0  |
| 488 GTB       | 661.0       | 8000.0 | 561.0 | 3000.0  | 15.0  | 22.0  |
| California    | 553.0       | 7500.0 | 557.0 | 4750.0  | 16.0  | 23.0  |
| GTC4Lusso     | 680.0       | 8250.0 | 514.0 | 5750.0  | 12.0  | 17.0  |
| FF            | 652.0       | 8000.0 | 504.0 | 6000.0  | 11.0  | 16.0  |
| F12Berlinetta | 731.0       | 8250.0 | 509.0 | 6000.0  | 11.0  | 16.0  |
| LaFerrari     | 949.0       | 9000.0 | 664.0 | 6750.0  | 12.0  | 16.0  |

We can also use Markdown formatting for the spanner label. In this example, we'll use `gt.md("*Performance*")` to make the label italicized.

``` python
(
    GT(gtcars_mini)
    .tab_spanner(
        label=md("*Performance*"),
        columns=["hp", "hp_rpm", "trq", "trq_rpm", "mpg_c", "mpg_h"]
    )
)
```

| model         | *Performance* |        |       |         |       |       |
|---------------|---------------|--------|-------|---------|-------|-------|
|               | hp            | hp_rpm | trq   | trq_rpm | mpg_c | mpg_h |
| GT            | 647.0         | 6250.0 | 550.0 | 5900.0  | 11.0  | 18.0  |
| 458 Speciale  | 597.0         | 9000.0 | 398.0 | 6000.0  | 13.0  | 17.0  |
| 458 Spider    | 562.0         | 9000.0 | 398.0 | 6000.0  | 13.0  | 17.0  |
| 458 Italia    | 562.0         | 9000.0 | 398.0 | 6000.0  | 13.0  | 17.0  |
| 488 GTB       | 661.0         | 8000.0 | 561.0 | 3000.0  | 15.0  | 22.0  |
| California    | 553.0         | 7500.0 | 557.0 | 4750.0  | 16.0  | 23.0  |
| GTC4Lusso     | 680.0         | 8250.0 | 514.0 | 5750.0  | 12.0  | 17.0  |
| FF            | 652.0         | 8000.0 | 504.0 | 6000.0  | 11.0  | 16.0  |
| F12Berlinetta | 731.0         | 8250.0 | 509.0 | 6000.0  | 11.0  | 16.0  |
| LaFerrari     | 949.0         | 9000.0 | 664.0 | 6750.0  | 12.0  | 16.0  |

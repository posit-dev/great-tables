# GTI.i_scale()

Set where the rows of the table, shown as a widget or in a Shiny app, are searched,

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L1975-L2032)

``` python
GTI.i_scale(engine="auto")
```

filtered and sorted.

A table shown in the browser has all of its rows there, which does all of this: quick for a table of a few thousand rows, but slow to load (and to sort) with many more. Shown as a widget (with [`i_as_widget()`](../reference/GTI.i_as_widget.md#great_tables.GTI.i_as_widget)), or in a Shiny app (with [`render_gt()`](../reference/shiny.render_gt.md#great_tables.shiny.render_gt)), a table can keep its rows in Python instead (in the notebook's kernel, or on the app's server), which searches, filters and sorts them (with [Narwhals](https://narwhals-dev.github.io/narwhals/), on the data's own library), and sends the browser the page it shows, one at a time: so the table loads as quickly with a million rows as with a few.

In the kernel, a table always has pages (as [`i_pagination()`](../reference/GTI.i_pagination.md#great_tables.GTI.i_pagination) sets them up), and its readers can't group its rows by a column, see its columns' profiles, see rows' details, or export the rows themselves (they can copy the code that filters and sorts the data as the view does, if the table has the `"code"` format); nor do its [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) colors change with the rows kept, or does it filter linked tables (see [`i_link()`](../reference/GTI.i_link.md#great_tables.GTI.i_link)). A table with row groups, summary rows, or a stub of more than one column is shown in the browser, as anywhere else, and so is a table that isn't shown as a widget or in a Shiny app.

A table of a lazy frame (a Polars LazyFrame, a DuckDB relation or an Ibis table) keeps its rows in the frame, and has only the page shown collected (see [`GTI()`](../reference/GTI.md#great_tables.GTI)).

## Parameters

`engine: Engine = "auto"`  
Where the rows are searched, filtered and sorted: in Python, if the table is shown as a widget or in a Shiny app and has more rows than the browser is quick with (more than 3,000, or more than 10 MB of HTML), and in the browser otherwise (`"auto"`, the default); in the browser (`"browser"`); or in Python, if the table is shown as a widget or in a Shiny app (`"kernel"`).

## Returns

`GTI`  
The GTI object is returned.

## Examples

This table of a million rows is shown a page at a time, from Python.

``` python
import numpy as np
import polars as pl
from great_tables import GTI

rng = np.random.default_rng(1)
df = pl.DataFrame({"x": rng.normal(size=1_000_000), "n": rng.integers(0, 100, 1_000_000)})

GTI(df).fmt_number(columns="x").i_cols_filter().i_scale(engine="kernel").i_as_widget()
```

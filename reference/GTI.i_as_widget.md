# GTI.i_as_widget()

Show the table as a widget, whose view and selection can be read and set from Python.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L2103-L2197)

``` python
GTI.i_as_widget()
```

The widget (an [anywidget](https://anywidget.dev)) shows the table as it's shown anywhere else, in a notebook in Jupyter, VS Code or Colab, or in marimo (where `mo_gti()` shows it as a UI element, so that the cells that read it run again with each change), and keeps Python up to date with what the reader does with it: the rows its search and filters keep, in the order shown, and those selected. Python can change the table's filters, sort, search and selection, too, and the table shows the change. The table works in the browser, as without a widget: Python is told what it does.

The widget has these, to read and set:

- [query](../reference/streamlit.GTIState.md#great_tables.streamlit.GTIState.query): the filters, as a query in text (as the query box has it, e.g. `'category in ("Tools") and margin > 0.2'`), or `""` without any; set it to a query (in text, or as [`i_view()`](../reference/GTI.i_view.md#great_tables.GTI.i_view)'s `filter=` takes it), or to `""`.
- [search](../reference/streamlit.GTIState.md#great_tables.streamlit.GTIState.search): the search, or `""`.
- [sort](../reference/streamlit.GTIState.md#great_tables.streamlit.GTIState.sort): the columns the rows are sorted by, most significant first, with a `-` before each one sorted in descending order (e.g., `["-net", "store"]`).
- `selection`: the data rows selected (numbered by position in the data, from 0), in data order, as far as [`i_selection()`](../reference/GTI.i_selection.md#great_tables.GTI.i_selection) lets readers select them.

And these, to read:

- `rows`: the data rows the search and filters keep (and linked tables' selections; see [`i_link()`](../reference/GTI.i_link.md#great_tables.GTI.i_link)), in the order shown, on every page.
- `view()`: the table's data with those rows, as a DataFrame of the data's library (with all its columns); `view(selected=True)` has the rows selected.

And `on_change(callback)` has `callback` called, with the widget, after each change the reader makes (`on_change(callback, remove=True)` stops it).

The rows are the browser's: a change made from Python is applied by the browser once the code making it has run, so in a notebook, `rows` and `view()` have it in the next cell (in the same cell, they raise an error). Before the widget is shown, they're those of the table's view (see [`i_view()`](../reference/GTI.i_view.md#great_tables.GTI.i_view)), as Python finds them.

A table with more rows than the browser is quick with keeps them in Python instead (see [`i_scale()`](../reference/GTI.i_scale.md#great_tables.GTI.i_scale)), which sends the browser a page at a time: then the rows are Python's, and `rows` and `view()` have a change at once.

The widget needs the `anywidget` package (`pip install anywidget`, or `pip install great_tables[widget]`).

## Returns

`GTIWidget`  
The widget, which shows the table when it's a cell's output (or with `display()`).

## Examples

Here the reader can filter the cars by their make and select some; Python gets them.

``` python
from great_tables import GTI
from great_tables.data import gtcars

cars = gtcars[["mfr", "model", "year", "hp", "msrp"]]

widget = (
    GTI(cars, rowname_col="model")
    .i_cols_filter(columns="mfr", type="facet")
    .i_selection("multiple")
    .i_as_widget()
)
widget
```

In a later cell, after filtering and selecting:

``` python
widget.query           # 'mfr in ("Ferrari", "Lamborghini")'
widget.view()          # those makes' cars, as a Pandas DataFrame
widget.view(selected=True)
```

And from Python, the table shows the cars with the most power first:

``` python
widget.sort = "-hp"
```

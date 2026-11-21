# panel.GTIPane

An interactive table in a Panel app or notebook, whose view and selection are parameters.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/panel.py#L128-L450)

``` python
panel.GTIPane(
    table,
    **params,
)
```

The table (a [GTI](../reference/GTI.md#great_tables.GTI) table, or a [GT](../reference/GT.md#great_tables.GT) table with [opt_interactive()](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive)) is shown as a Panel component, and its state is in its parameters: [query](../reference/streamlit.GTIState.md#great_tables.streamlit.GTIState.query), [search](../reference/streamlit.GTIState.md#great_tables.streamlit.GTIState.search) and [sort](../reference/streamlit.GTIState.md#great_tables.streamlit.GTIState.sort) (its view), `rows` (the rows the view keeps) and `selection` (the rows selected). Each change the reader makes to them sets them, so that they can be watched (with `pn.bind()`, `param.depends()` or `.param.watch()`) like any other Panel parameter; and setting [query](../reference/streamlit.GTIState.md#great_tables.streamlit.GTIState.query), [search](../reference/streamlit.GTIState.md#great_tables.streamlit.GTIState.search), [sort](../reference/streamlit.GTIState.md#great_tables.streamlit.GTIState.sort) or `selection` changes the table, as if the reader had.

A [GTI](../reference/GTI.md#great_tables.GTI) table with more rows than the browser is quick with keeps them in Python instead (see [`i_scale()`](../reference/GTI.i_scale.md#great_tables.GTI.i_scale)), and sends the browser a page at a time. Then `rows` is found in Python (without linked tables' selections).

## Parameters

`table: GT`  
The table to show: a [GTI](../reference/GTI.md#great_tables.GTI) table, or a [GT](../reference/GT.md#great_tables.GT) table with [opt_interactive()](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive).

`**params: Any`  
Panel's parameters of a component (e.g., `margin=`, `visible=`), and the pane's own `query=`, `search=`, `sort=` and `selection=`, which are set after the table's own view and selection (as if they were set once the pane's made), and checked as they are then.

## Examples

``` python
import panel as pn
from great_tables import GTI, exibble
from great_tables.panel import GTIPane

pn.extension()

table = GTIPane(
    GTI(exibble).i_cols_filter(columns="fctr", type="facet").i_selection("multiple")
)


def selected(selection):
    return exibble.iloc[selection]


pn.Column(table, pn.bind(selected, table.param.selection)).servable()
```

## Methods

| Name | Description |
|----|----|
| [data()](#great_tables.panel.GTIPane.data) | The table's data, with the rows its view keeps, in the order shown (see `rows`), or with |

### data()

The table's data, with the rows its view keeps, in the order shown (see `rows`), or with

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/panel.py#L414-L430)

``` python
data(selected=False)
```

`selected=True`, the rows selected (in data order): a DataFrame of the data's library, with all of its columns.

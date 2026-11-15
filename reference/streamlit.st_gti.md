# streamlit.st_gti()

Show an interactive table in a Streamlit app, and get its state.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/streamlit.py#L163-L268)

``` python
streamlit.st_gti(
    table,
    *,
    key,
    on_change="rerun",
)
```

The table (a [GTI](../reference/GTI.md#great_tables.GTI) table, or a [GT](../reference/GT.md#great_tables.GT) table with [opt_interactive()](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive)) is shown as a component, and its state is given back: its view, the rows the view keeps, and those selected (see [`GTIState`](../reference/streamlit.GTIState.md#great_tables.streamlit.GTIState)). Each change the reader makes to them (a search, a filter, a sort, a selection, …) runs the app again, and the table's state is then what the reader made it. [`update_gti()`](../reference/streamlit.update_gti.md#great_tables.streamlit.update_gti) changes it from the app.

A [GTI](../reference/GTI.md#great_tables.GTI) table with more rows than the browser is quick with keeps them in Python instead (see [`i_scale()`](../reference/GTI.i_scale.md#great_tables.GTI.i_scale)), and sends the browser a page at a time: the browser asks for each one (and for a filter's counts) by running the app again, which answers. Then the rows its view keeps are found in Python (without linked tables' selections). Such a table is best made once, with `st.cache_resource`: a table the app makes again on each run is rendered again each time (which, with many rows in a DataFrame, takes a while).

## Parameters

`table: GT`  
The table to show: a [GTI](../reference/GTI.md#great_tables.GTI) table, or a [GT](../reference/GT.md#great_tables.GT) table with [opt_interactive()](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive).

`key: str`  
The table's key, unique in the app: the table keeps its view and selection by it (when it's made again on each run, but rendered the same), and `update_gti()` changes it.

`on_change: Literal["rerun", "ignore"] | Callable[[], Any] = "rerun"`  
What a change the reader makes does: run the app again (`"rerun"`, the default); not, so that the table's state is only what the app made it (`"ignore"`); or call a function (with no arguments), and run the app again. A table whose rows are in Python runs the app again for each page all the same.

## Returns

`GTIState`  
The table's state: its view, the rows the view keeps, and those selected. Until it's shown, as it's first shown (its rows as Python finds them); once it's shown, as the browser last gave it.

## Examples

``` python
import streamlit as st
from great_tables import GTI, exibble
from great_tables.streamlit import st_gti

table = GTI(exibble).i_cols_filter(columns="fctr", type="facet").i_selection("multiple")
state = st_gti(table, key="table")

st.write(f"{len(state.rows or [])} rows, filtered by {state.query!r}")
st.dataframe(exibble.iloc[state.selection])
```

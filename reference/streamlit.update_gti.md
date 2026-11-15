# streamlit.update_gti()

Change an interactive table's view or selection, from a Streamlit app.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/streamlit.py#L419-L498)

``` python
streamlit.update_gti(
    key,
    *,
    query=None,
    search=None,
    sort=None,
    selection=None,
)
```

The table (shown with [`st_gti()`](../reference/streamlit.st_gti.md#great_tables.streamlit.st_gti), with the same `key`) is filtered, searched, sorted, and has its rows selected, as if the reader had done it (so that a change to its filters, search or sort shows its first page). What isn't given (or is `None`) is left as it is. It's changed by the table's next [st_gti()](../reference/streamlit.st_gti.md#great_tables.streamlit.st_gti): so call `update_gti()` before it, as in a widget's callback (`on_click=` or `on_change=`), which is run before the app; one called after it is the next run's.

## Parameters

`key: str`  
The table's key.

`query: str | dict[str, Any] | None = None`  
The table's filters: a query in text (as the query box has it), or as [`i_view()`](../reference/GTI.i_view.md#great_tables.GTI.i_view)'s `filter=` takes it; `""` for none.

`search: str | None = None`  
The table's search; `""` for none.

`sort: str | list[str] | None = None`  
The columns to sort the table by, most significant first, each with a `-` before it to sort it in descending order (e.g., `["-net", "store"]`), or one column; `[]` to leave it unsorted.

`selection: list[int] | None = None`  
The data rows to select (numbered by position in the data, from 0), and only those; `[]` for none. The table must let readers select rows (with [`i_selection()`](../reference/GTI.i_selection.md#great_tables.GTI.i_selection)).

## Examples

``` python
import streamlit as st
from great_tables import GTI, exibble
from great_tables.streamlit import st_gti, update_gti

st.button(
    "Largest first",
    on_click=update_gti,
    args=("table",),
    kwargs={"query": 'fctr in ("one", "two")', "sort": "-num"},
)
state = st_gti(GTI(exibble).i_cols_filter(columns="fctr", type="facet"), key="table")
st.write(f"{len(state.rows or [])} rows, filtered by {state.query!r}")
```

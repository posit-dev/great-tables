# solara.GTITable()

An interactive table in a Solara app, whose view and selection are the app's to read and set.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/solara.py#L62-L214)

``` python
solara.GTITable(
    table,
    query=None,
    search=None,
    sort=None,
    selection=None,
    on_query=None,
    on_search=None,
    on_sort=None,
    on_selection=None,
    on_rows=None,
)
```

The table (a [GTI](../reference/GTI.md#great_tables.GTI) table, or a [GT](../reference/GT.md#great_tables.GT) table with [opt_interactive()](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive)) is shown as a widget (see [`i_as_widget()`](../reference/GTI.i_as_widget.md#great_tables.GTI.i_as_widget)), and its state is in the component's values, as with Solara's own components: [query](../reference/streamlit.GTIState.md#great_tables.streamlit.GTIState.query), [search](../reference/streamlit.GTIState.md#great_tables.streamlit.GTIState.search) and [sort](../reference/streamlit.GTIState.md#great_tables.streamlit.GTIState.sort) (its view), and `selection` (the rows selected). Each can be a value with a callback (`on_query=`, …) or a reactive variable (`solara.reactive()`, `solara.use_reactive()`), which each change the reader makes sets; and when the app changes it, the table changes, as if the reader had. One left as `None` (as are all of them by default) starts as the table has it, and is then set. The rows the view keeps are given to `on_rows=`.

A [GTI](../reference/GTI.md#great_tables.GTI) table with more rows than the browser is quick with keeps them in Python instead (see [`i_scale()`](../reference/GTI.i_scale.md#great_tables.GTI.i_scale)), and sends the browser a page at a time. Then the rows the view keeps are found in Python (without linked tables' selections). Such a table is best made once (at the module's top level, or with `solara.use_memo()`): a table made again on each render is rendered again each time (which, with many rows, takes a while), though the reader's view is kept if it's rendered the same.

## Parameters

`table: GT`  
The table to show: a [GTI](../reference/GTI.md#great_tables.GTI) table, or a [GT](../reference/GT.md#great_tables.GT) table with [opt_interactive()](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive).

`query: _Value[str] = None`  
The table's filters, as a query in text (as the query box has it), or as [`i_view()`](../reference/GTI.i_view.md#great_tables.GTI.i_view)'s `filter=` takes it; `""` for none. It's set to a query in text.

`search: _Value[str] = None`  
The table's search; `""` for none.

`sort: _Value[list[str]] = None`  
The columns the table is sorted by, most significant first, each with a `-` before it if it's sorted in descending order (e.g., `["-net", "store"]`); `[]` if it isn't sorted.

`selection: _Value[list[int]] = None`  
The data rows selected (numbered by position in the data, from 0), in data order; `[]` for none. Setting it needs a table that lets readers select rows (see [`i_selection()`](../reference/GTI.i_selection.md#great_tables.GTI.i_selection)).

`on_query: Callable[[str], None] | None = None`  
Called with the new value, after each change to it (by the reader, or by the app).

`on_search: Callable[[str], None] | None = None`  
Called with the new value, after each change to it (by the reader, or by the app).

`on_sort: Callable[[str], None] | None = None`  
Called with the new value, after each change to it (by the reader, or by the app).

`on_selection: Callable[[str], None] | None = None`  
Called with the new value, after each change to it (by the reader, or by the app).

`on_rows: Callable[[list[int]], None] | None = None`  
Called with the data rows the table's search and filters keep (and linked tables' selections), in the order shown, on every page (numbered by position in the data, from 0), whenever they change: first when they're known (before the table is shown, if Python can find them; a [GT](../reference/GT.md#great_tables.GT) table's, and one with a search, once the browser has).

## Returns

`solara.Element`  
The table.

## Examples

``` python
import solara
from great_tables import GTI, exibble
from great_tables.solara import GTITable

table = GTI(exibble).i_cols_filter(columns="fctr", type="facet").i_selection("multiple")
query = solara.reactive("")
selection = solara.reactive([])


@solara.component
def Page():
    solara.Button("One and two", on_click=lambda: query.set('fctr in ("one", "two")'))
    GTITable(table, query=query, selection=selection)
    solara.DataFrame(exibble.iloc[selection.value])
```

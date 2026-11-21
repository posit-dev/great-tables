# streamlit.GTIState

An interactive table's state in a Streamlit app, as [`st_gti()`](../reference/streamlit.st_gti.md#great_tables.streamlit.st_gti)

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/streamlit.py#L122-L160)

``` python
streamlit.GTIState(
    view,
    rows,
    selection,
)
```

gives it.

## Attributes

`view: dict[str, Any]`  
The table's view: a dict with its filters as a query in text (`"query"`), its `"search"`, its `"sort"` (columns, with a `-` before those in descending order), its `"page"` and `"page_size"`, its `"hidden"` columns and the column its rows are grouped by (`"group_by"`).

`rows: list[int] | None`  
The data rows its search and filters keep (and linked tables' selections), in the order shown, on every page, numbered by position in the data (from 0); or `None` until the browser has found them (when the app is run again).

`selection: list[int]`  
The data rows selected, in data order.

## Attributes

| Name | Description |
|----|----|
| [query](#great_tables.streamlit.GTIState.query) | The table's filters, as a query in text (`""` without any). |
| [search](#great_tables.streamlit.GTIState.search) | The table's search (`""` without one). |
| [sort](#great_tables.streamlit.GTIState.sort) | The table's sort: its columns, each with a `-` before it if it's in descending order. |

### query

The table's filters, as a query in text (`""` without any).

`query: str`

### search

The table's search (`""` without one).

`search: str`

### sort

The table's sort: its columns, each with a `-` before it if it's in descending order.

`sort: list[str]`

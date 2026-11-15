# shiny.update_gti()

Change an interactive table's view or selection, from a Shiny app's server.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/shiny.py#L204-L297)

``` python
shiny.update_gti(
    id,
    *,
    query=None,
    search=None,
    sort=None,
    selection=None,
    session=None,
)
```

The table (rendered with [`render_gt()`](../reference/shiny.render_gt.md#great_tables.shiny.render_gt)) is filtered, searched, sorted, and has its rows selected, as if the reader had done it (so that a change to its filters, search or sort shows its first page). What isn't given (or is `None`) is left as it is. The table's inputs then give the new state (see [render_gt()](../reference/shiny.render_gt.md#great_tables.shiny.render_gt)).

## Parameters

`id: str`  
The table's output id.

`query: str | dict[str, Any] | None = None`  
The table's filters: a query in text (as the query box has it), or as [`i_view()`](../reference/GTI.i_view.md#great_tables.GTI.i_view)'s `filter=` takes it; `""` for none.

`search: str | None = None`  
The table's search; `""` for none.

`sort: str | list[str] | None = None`  
The columns to sort the table by, most significant first, each with a `-` before it to sort it in descending order (e.g., `["-net", "store"]`), or one column; `[]` to leave it unsorted.

`selection: list[int] | None = None`  
The data rows to select (numbered by position in the data, from 0), and only those; `[]` for none. The table must let readers select rows (with [`i_selection()`](../reference/GTI.i_selection.md#great_tables.GTI.i_selection)).

`session: Session | None = None`  
The Shiny session (by default, the current one).

## Examples

``` python
from shiny import App, reactive, render, ui
from great_tables import GTI, exibble
from great_tables.shiny import output_gt, render_gt, update_gti

app_ui = ui.page_fluid(
    ui.input_action_button("big", "Largest first"),
    output_gt("table"),
    ui.output_text("shown"),
)


def server(input, output, session):
    @render_gt
    def table():
        return GTI(exibble).i_cols_filter(columns="fctr", type="facet")

    @render.text
    def shown():
        return f"{len(input.table_rows())} rows, filtered by {input.table_view()['query']!r}"

    @reactive.effect
    @reactive.event(input.big)
    def _():
        update_gti("table", query='fctr in ("one", "two")', sort="-num")


app = App(app_ui, server)
```

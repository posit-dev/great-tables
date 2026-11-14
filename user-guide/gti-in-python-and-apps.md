# GTI in Python and Apps

An interactive table works in the browser on its own, but Python can also read what readers do with it, and change it: in a notebook, with a `GTI` table (see [GTI Tables](gti-tables.md)) as a widget, and in Shiny, Streamlit, Panel and Solara apps, which take a `GTI` table or a [GT](../reference/GT.md#great_tables.GT) table with `opt_interactive()`, get its view and selection, and can set them from the app.

## Using the table from Python

In a notebook, `i_as_widget()` shows the table as a widget (with [anywidget](https://anywidget.dev), installed with `pip install great_tables[widget]`), whose view and selection Python can read and set: what the reader searched for, filtered and sorted by, the rows that leaves, and the rows they selected. The table still works in the browser; the widget tells Python what it shows.

``` python
import polars as pl
from great_tables import GTI
from great_tables.data import gtcars

cars = pl.from_pandas(gtcars).select(["mfr", "model", "year", "hp", "mpg_c", "msrp"])

widget = (
    GTI(cars)
    .i_cols_filter(columns="mfr", type="facet")
    .i_selection("multiple")
    .i_as_widget()
)
widget
```

Then, in another cell (as the browser gives Python the table's state once the cell is done):

``` python
widget.query            # the filters, as a query in text: 'mfr in ("Ferrari")'
widget.search           # the search
widget.sort             # the sort, e.g., ["-hp"]
widget.rows             # the data rows kept, in the order shown (numbered from 0)
widget.view()           # those rows, as a DataFrame of the data's library
widget.view(selected=True)  # the rows selected

widget.query = 'mfr in ("Ferrari", "Lamborghini")'
widget.sort = "-hp"
widget.selection = [0, 3]
```

Setting `query`, `search`, `sort` or `selection` changes the table as shown, and `widget.on_change(callback)` calls `callback(widget)` after each change the reader makes. A change made from Python is applied by the browser after the cell runs, so ask for the rows it leaves in another cell.

## Using the table in a Shiny app

In a [Shiny](https://shiny.posit.co/py/) app, an interactive table (a `GTI` table, or a [GT](../reference/GT.md#great_tables.GT) table with `opt_interactive()`) rendered with `render_gt()`, from `great_tables.shiny`, gives the server its state as inputs, named after the output: `input.<id>_view()` (a dict with the `"query"`, `"search"`, `"sort"`, `"page"`, `"page_size"`, `"hidden"` columns and `"group_by"` column), `input.<id>_rows()` (the data rows kept, in the order shown) and `input.<id>_selection()` (the rows selected). `update_gti()` sets its query, search, sort and selection from the server.

``` python
from shiny import App, reactive, render, ui
from great_tables import GTI
from great_tables.data import gtcars
from great_tables.shiny import output_gt, render_gt, update_gti

app_ui = ui.page_fluid(
    ui.input_action_button("fastest", "Fastest first"),
    output_gt("cars"),
    ui.output_text("chosen"),
)


def server(input, output, session):
    @render_gt
    def cars():
        return (
            GTI(gtcars[["mfr", "model", "year", "hp", "msrp"]])
            .i_cols_filter(columns="mfr", type="facet")
            .i_selection("multiple")
        )

    @render.text
    def chosen():
        rows = input.cars_selection()
        return f"{len(rows)} of {len(input.cars_rows())} cars selected"

    @reactive.effect
    @reactive.event(input.fastest)
    def _():
        update_gti("cars", sort="-hp", selection=[])


app = App(app_ui, server)
```

The table works in the browser as it does anywhere else, so the server isn't asked for each page, sort or search; a table rendered again starts with the view it's given.

## Using the table in a Streamlit app

In a [Streamlit](https://streamlit.io) app, `st_gti()`, from `great_tables.streamlit` (installed with `pip install great_tables[streamlit]`), shows an interactive table (a `GTI` table, or a [GT](../reference/GT.md#great_tables.GT) table with `opt_interactive()`) and gives its state: its `query`, `search` and `sort`, the data `rows` kept (in the order shown) and the rows in its `selection`. Each change the reader makes runs the app again, with the table's new state. `update_gti()`, called in a widget's callback, sets its query, search, sort and selection from the app.

``` python
import streamlit as st
from great_tables import GTI
from great_tables.data import gtcars
from great_tables.streamlit import st_gti, update_gti

st.button("Fastest first", on_click=update_gti, args=("cars",), kwargs={"sort": "-hp"})
table = (
    GTI(gtcars[["mfr", "model", "year", "hp", "msrp"]])
    .i_cols_filter(columns="mfr", type="facet")
    .i_selection("multiple")
)
state = st_gti(table, key="cars")
st.write(f"{len(state.selection)} of {len(state.rows or [])} cars selected")
```

The table keeps its view and selection by its `key` as the app runs again, as long as it's rendered the same. A table whose rows are kept in Python (with `i_scale()`) asks the app for each page, which runs it again; make it once, with `st.cache_resource`, so that it isn't rendered again each time.

## Using the table in a Panel app

In a [Panel](https://panel.holoviz.org) app or notebook, `GTIPane`, from `great_tables.panel` (installed with `pip install great_tables[panel]`), shows an interactive table (a `GTI` table, or a [GT](../reference/GT.md#great_tables.GT) table with `opt_interactive()`) as a Panel component, whose state is in its parameters: `query`, `search` and `sort` (a list, e.g., `["-hp"]`), the data `rows` kept (in the order shown) and the rows in its `selection`. Each change the reader makes sets them, so that they can be used with `pn.bind()` or watched like any other parameter; and setting `query`, `search`, `sort` or `selection` changes the table.

``` python
import panel as pn
from great_tables import GTI
from great_tables.data import gtcars
from great_tables.panel import GTIPane

pn.extension()

cars = gtcars[["mfr", "model", "year", "hp", "msrp"]]
table = GTIPane(
    GTI(cars).i_cols_filter(columns="mfr", type="facet").i_selection("multiple")
)


def chosen(rows, selection):
    return f"{len(selection)} of {len(rows or [])} cars selected"


fastest = pn.widgets.Button(name="Fastest first")
fastest.on_click(lambda _: table.param.update(sort=["-hp"], selection=[]))
pn.Column(fastest, table, pn.bind(chosen, table.param.rows, table.param.selection)).servable()
```

`table.data()` gives the rows kept as a DataFrame of the data's library (and `table.data(selected=True)` the rows selected). The table works in the browser, which finds its `rows`, so they can be `None` until it has (as before the table's shown with a search). A table whose rows are kept in Python (with `i_scale()`) asks the app for each page instead, and its `rows` are found in Python.

## Using the table in a Solara app

In a [Solara](https://solara.dev) app or notebook, the `GTITable` component, from `great_tables.solara` (installed with `pip install great_tables[solara]`), shows an interactive table (a `GTI` table, or a [GT](../reference/GT.md#great_tables.GT) table with `opt_interactive()`), whose `query`, `search`, `sort` (a list, e.g., `["-hp"]`) and `selection` are the app's values, as with Solara's own components. Each can be a reactive variable, which each change the reader makes sets and which changes the table when the app sets it, or a value with a callback (`on_query=`, `on_sort=`, …). One that isn't given starts as the table has it. The data rows kept (in the order shown) are given to `on_rows=`.

``` python
import solara
from great_tables import GTI
from great_tables.data import gtcars
from great_tables.solara import GTITable

cars = gtcars[["mfr", "model", "year", "hp", "msrp"]]
table = GTI(cars).i_cols_filter(columns="mfr", type="facet").i_selection("multiple")

sort = solara.reactive([])
selection = solara.reactive([])
rows = solara.reactive([])


@solara.component
def Page():
    solara.Button("Fastest first", on_click=lambda: (sort.set(["-hp"]), selection.set([])))
    GTITable(table, sort=sort, selection=selection, on_rows=rows.set)
    solara.Text(f"{len(selection.value)} of {len(rows.value)} cars selected")
```

The component keeps the table's view as the app renders again, as long as it's given the same table or one rendered the same. A table whose rows are kept in Python (with `i_scale()`) asks the app for each page, and its rows are found in Python; make it once (at the module's top level, as here, or with `solara.use_memo()`), so that it isn't rendered again each time.

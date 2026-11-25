import solara

from great_tables import GT, GTI, data
from great_tables.solara import GTITable

cars = data.gtcars[["mfr", "model", "year", "hp", "msrp"]]
table = (
    GTI(cars)
    .fmt_integer("hp")
    .fmt_currency("msrp", decimals=0)
    .i_cols_filter(columns="mfr", type="facet")
    .i_selection("multiple")
    .i_responsive("scroll")
)

sort = solara.reactive([])
selection = solara.reactive([])
rows = solara.reactive([])


def fastest():
    sort.set(["-hp"])
    selection.set([])


@solara.component
def Page():
    solara.Button("Fastest first", on_click=fastest)
    GTITable(table, sort=sort, selection=selection, on_rows=rows.set)
    solara.Text(f"{len(selection.value)} of {len(rows.value)} cars selected")

    chosen = GT(cars.iloc[selection.value]).fmt_integer("hp").fmt_currency("msrp", decimals=0)
    solara.HTML(unsafe_innerHTML=chosen.as_raw_html())

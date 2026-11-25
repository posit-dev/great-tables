import panel as pn

from great_tables import GT, GTI, data
from great_tables.panel import GTIPane

pn.extension()

cars = data.gtcars[["mfr", "model", "year", "hp", "msrp"]]
table = GTIPane(
    GTI(cars)
    .fmt_integer("hp")
    .fmt_currency("msrp", decimals=0)
    .i_cols_filter(columns="mfr", type="facet")
    .i_selection("multiple")
    .i_responsive("scroll")
)


def chosen(rows, selection):
    picked = GT(cars.iloc[selection]).fmt_integer("hp").fmt_currency("msrp", decimals=0)
    return pn.Column(f"{len(selection)} of {len(rows or [])} cars selected", pn.pane.HTML(picked))


fastest = pn.widgets.Button(name="Fastest first")
fastest.on_click(lambda _: table.param.update(sort=["-hp"], selection=[]))
pn.Column(fastest, table, pn.bind(chosen, table.param.rows, table.param.selection)).servable()

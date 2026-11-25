# /// script
# dependencies = ["great-tables[marimo]", "pandas"]
# ///
import marimo

app = marimo.App()


@app.cell
def _():
    import marimo as mo

    from great_tables import GT, GTI, data
    from great_tables.marimo import mo_gti

    cars = data.gtcars[["mfr", "model", "year", "hp", "msrp"]]
    table = mo_gti(
        GTI(cars)
        .fmt_integer("hp")
        .fmt_currency("msrp", decimals=0)
        .i_cols_filter(columns="mfr", type="facet")
        .i_selection("multiple")
        .i_responsive("scroll")
    )
    table
    return GT, mo, table


@app.cell
def _(mo, table):
    def fastest(_):
        table.sort = "-hp"
        table.selection = []

    fastest_button = mo.ui.button(label="Fastest first", on_click=fastest)
    fastest_button
    return


@app.cell
def _(GT, mo, table):
    chosen = table.view(selected=True)
    mo.vstack(
        [
            mo.md(f"{len(chosen)} of {len(table.value['rows'] or [])} cars selected"),
            GT(chosen).fmt_integer("hp").fmt_currency("msrp", decimals=0),
        ]
    )
    return


if __name__ == "__main__":
    app.run()

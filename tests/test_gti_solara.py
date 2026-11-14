"""Interactive tables in a Solara app: `GTITable`.

The component is rendered with `solara.render()`, and the browser's changes are set on its widget
as packages/gti/src/widget.ts writes them. The two together are tested in Solara apps and a
notebook (packages/gti/e2e/hosts.spec.ts).
"""

from __future__ import annotations

from typing import Any

import pandas as pd
import pytest

solara = pytest.importorskip("solara")

from great_tables import GT, GTI  # noqa: E402
from great_tables._gti._widget import GTIWidget  # noqa: E402
from great_tables.solara import GTITable  # noqa: E402

DATA = pd.DataFrame(
    {
        "char": ["apricot", "banana", "coconut", "durian", "fig"],
        "num": [3.0, 1.0, None, 5.0, 2.0],
        "fctr": ["one", "two", "one", "three", "two"],
    }
)

VIEW = {
    "filter": None,
    "sort": [],
    "search": "",
    "page": 1,
    "page_size": None,
    "hidden": [],
    "group_by": None,
}

ONE_TWO = 'fctr in ("one", "two")'


def make_gti(data: pd.DataFrame = DATA) -> GTI:
    return GTI(data).i_cols_filter(columns="fctr", type="facet").i_selection("multiple")


def render(element: Any) -> tuple[Any, Any]:
    _, rc = solara.render(element, handle_error=False)
    return rc, lambda: rc.find(GTIWidget).widget


def show(widget: GTIWidget, **view: Any) -> None:
    # (As the browser writes the reader's changes)
    rows = view.pop("rows")
    selection = view.pop("selection", widget.selection)
    widget.set_state({"_view": {**VIEW, **view}, "_rows": rows, "_selection": selection})


def test_table_starts_as_the_author_made_it():
    query, sort, rows = solara.reactive(None), solara.reactive(None), []
    table = make_gti().i_view(filter='fctr in ("one")', sort="-num")
    rc, widget = render(GTITable(table, query=query, sort=sort, on_rows=rows.append))
    assert widget()._html.startswith("<gt-table")
    # (The values left as `None` are set to the table's own, and its rows are given)
    assert query.value == 'fctr in ("one")' and sort.value == ["-num"]
    assert rows == [[0, 2]]
    rc.close()


def test_app_sets_the_table():
    query, search, sort = solara.reactive(""), solara.reactive(""), solara.reactive([])
    selection, rows = solara.reactive([]), []
    rc, widget = render(
        GTITable(
            make_gti(),
            query=query,
            search=search,
            sort=sort,
            selection=selection,
            on_rows=rows.append,
        )
    )
    assert rows == [[0, 1, 2, 3, 4]]
    query.set(ONE_TWO)
    sort.set(["-num"])
    selection.set([0, 4])
    assert widget().query == ONE_TWO and widget().sort == ["-num"]
    assert widget().selection == [0, 4]
    assert rows[-1] == [0, 4, 1, 2]
    # (A search is the browser's to apply, so the rows come once it has)
    search.set("an")
    assert widget().search == "an" and rows[-1] == [0, 4, 1, 2]
    show(widget(), search="an", sort=[{"column": "num", "descending": True}], rows=[1])
    assert rows[-1] == [1]
    rc.close()


def test_app_query_is_set_as_text():
    query = solara.reactive(None)
    rc, widget = render(GTITable(make_gti(), query=query))
    query.set({"and": [{"col": "fctr", "op": "in", "value": ["one"]}]})
    assert widget().query == 'fctr in ("one")'
    assert query.value == 'fctr in ("one")'
    rc.close()


def test_reader_sets_the_values():
    query, sort, selection = solara.reactive(""), solara.reactive([]), solara.reactive([])
    changes: list[Any] = []
    rc, widget = render(
        GTITable(
            make_gti(),
            query=query,
            sort=sort,
            selection=selection,
            on_query=changes.append,
            on_rows=changes.append,
        )
    )
    changes.clear()
    one = {"and": [{"col": "fctr", "op": "in", "value": ["one"]}]}
    show(widget(), filter=one, sort=[{"column": "num", "descending": True}], rows=[0, 2])
    assert query.value == 'fctr in ("one")' and sort.value == ["-num"]
    assert changes == ['fctr in ("one")', [0, 2]]
    show(
        widget(),
        filter=one,
        sort=[{"column": "num", "descending": True}],
        rows=[0, 2],
        selection=[2],
    )
    assert selection.value == [2]
    # (Rows the same as before aren't given again)
    assert changes == ['fctr in ("one")', [0, 2]]
    rc.close()


def test_values_with_callbacks():
    changes: list[Any] = []

    @solara.component
    def Page(query: str):
        GTITable(make_gti(), query=query, on_query=changes.append)

    query = solara.reactive(ONE_TWO)

    @solara.component
    def App():
        Page(query.value)

    rc, widget = render(App())
    assert widget().query == ONE_TWO and changes == []
    # (The reader's change is the callback's, and the value the app gives, the table's)
    show(widget(), rows=[0, 1, 2, 3, 4])
    assert changes == [""]
    assert widget().query == ""
    query.set('fctr in ("three")')
    assert widget().query == 'fctr in ("three")'
    rc.close()


def test_app_values_are_checked():
    with pytest.raises(ValueError, match="no filter"):
        render(GTITable(make_gti(), query="num > 2"))
    sort = solara.reactive([])
    _, widget = render(GTITable(make_gti(), sort=sort))
    with pytest.raises(ValueError, match="nope"):
        sort.set(["nope"])
    assert widget().sort == []


def test_same_table_keeps_its_widget():
    head, renders = solara.reactive(False), solara.reactive(0)
    sort = solara.reactive(["-num"])
    selection = solara.reactive([0])
    tables: list[GTI] = []

    @solara.component
    def Page():
        # (Made again on each render)
        renders.value
        table = make_gti(DATA.head(4) if head.value else DATA)
        tables.append(table)
        GTITable(table, sort=sort, selection=selection)

    rc, widget = render(Page())
    first = widget()
    assert first._gti._options.table_id.value.startswith("gti-")
    assert tables[0]._options.table_id.value is None
    sort.set(["num"])
    assert widget() is first and first.sort == ["num"]
    # (A table rendered the same keeps the widget, which then has it)
    renders.set(1)
    assert len(tables) == 2 and widget() is first and first.sort == ["num"]
    assert first._gti._tbl_data is tables[1]._tbl_data
    # (Another table is another widget, with the app's values from the start)
    head.set(True)
    second = widget()
    assert second is not first and first.comm is None
    assert second.sort == ["num"] and second.selection == [0]
    assert second._gti._options.table_id.value == first._gti._options.table_id.value
    rc.close()


def test_another_table_takes_the_values_it_can():
    head = solara.reactive(False)
    sort = solara.reactive(["-num"])
    selection = solara.reactive([4])

    @solara.component
    def Page():
        data = DATA[["char", "fctr"]].head(3) if head.value else DATA
        GTITable(make_gti(data), sort=sort, selection=selection)

    rc, widget = render(Page())
    head.set(True)
    # (Without `num`, or a fifth row)
    assert widget().sort == [] and widget().selection == []
    assert sort.value == [] and selection.value == []
    rc.close()


def test_table_with_an_id_keeps_it():
    rc, widget = render(GTITable(make_gti().with_id("cars")))
    assert widget()._gti._options.table_id.value == "cars"
    assert 'id="cars"' in widget()._html
    rc.close()


def test_opt_interactive_table():
    query, rows = solara.reactive(None), []
    table = GT(DATA).opt_interactive(use_filters=True)
    rc, widget = render(GTITable(table, query=query, on_rows=rows.append))
    assert query.value == ""
    # (Its rows are the browser's to find)
    assert rows == []
    show(widget(), rows=[0, 1, 2, 3, 4])
    assert rows == [[0, 1, 2, 3, 4]]
    rc.close()


@pytest.mark.parametrize("table", [GT(DATA), DATA])
def test_needs_an_interactive_table(table: Any):
    with pytest.raises(TypeError, match="interactive tables|`GTI` or a `GT` table"):
        render(GTITable(table))


def test_kernel_mode_rows_are_pythons():
    big = pd.DataFrame({"n": range(50), "kind": ["odd" if i % 2 else "even" for i in range(50)]})
    table = GTI(big).i_cols_filter(columns="kind", type="facet").i_scale(engine="kernel")
    query, rows = solara.reactive(""), []
    rc, widget = render(GTITable(table, query=query, on_rows=rows.append))
    assert widget()._kernel is True
    assert rows == [list(range(50))]
    query.set('kind in ("odd")')
    assert rows[-1] == list(range(1, 50, 2))
    rc.close()

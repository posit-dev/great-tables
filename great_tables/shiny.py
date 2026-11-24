from __future__ import annotations

__all__ = (
    "output_gt",
    "render_gt",
    "update_gti",
)

import warnings
from typing import TYPE_CHECKING, Any, overload
from weakref import WeakKeyDictionary

from . import __version__
from .gt import GT

try:
    # (htmltools is a dependency of shiny, not of great_tables)
    from htmltools import HTML, HTMLDependency, Tag, TagList, div
    from shiny._namespaces import resolve_id
    from shiny.input_handler import input_handlers
    from shiny.render.transformer import (
        TransformerMetadata,
        ValueFn,
        output_transformer,
        resolve_value_fn,
    )
    from shiny.session import require_active_session
except ImportError:
    raise ImportError(
        "The great_tables.shiny module requires the shiny package to be installed."
        " Please install it with this command:"
        "\n\n    pip install shiny"
    )

from ._gti._kernel import KernelEngine, render_table
from ._gti._lazy import table_rows
from ._gti._render import JS_DIR, inline_runtime, render_gti_element
from ._gti._state import check_query_value, check_search, check_selection, check_sort, view_of
from ._render import infer_render_env_defaults

if TYPE_CHECKING:
    from shiny.session import Session
    from shiny.session._utils import RenderedDeps

    from ._gti._spec import Spec

# (As src/shiny.ts has them, in packages/gti)
MESSAGE = "great_tables.update_gti"
VIEW_TYPE = "great_tables.gti_view"
ROWS_TYPE = "great_tables.gti_rows"
# (The request handler of a table whose rows are the server's is the output's, with this after
# its id)
ASK_SUFFIX = "_gti"

# Each session's interactive tables' specs, by output (its id, namespaced), as last rendered, for
# `update_gti()` to check what it sets against
_SPECS: WeakKeyDictionary[Any, dict[str, Spec]] = WeakKeyDictionary()

# Each session's tables whose rows are kept on the server (`i_scale()`), by output, as last
# rendered
_ENGINES: WeakKeyDictionary[Any, dict[str, KernelEngine]] = WeakKeyDictionary()


@input_handlers.add(VIEW_TYPE, force=True)
def _view_input(value: Any, name: Any, session: Any) -> dict[str, Any]:
    return view_of(value)


@input_handlers.add(ROWS_TYPE, force=True)
def _rows_input(value: Any, name: Any, session: Any) -> list[int]:
    # (A table whose rows are the server's gives its view as its rows, which the server finds;
    # the input's name is the output's id, namespaced, then "_rows")
    engine = _ENGINES.get(session.root_scope(), {}).get(str(name).removesuffix("_rows"))
    if engine is None or not isinstance(value, dict):
        return []
    # (A view the table doesn't have, as an old table's might be once it's rendered again, keeps
    # none, rather than ending the session)
    try:
        return engine.find({**_lists(value), "links": []})
    except (TypeError, ValueError):
        return []


def _lists(value: Any) -> Any:
    # (Shiny reads the browser's arrays as tuples, where the engine takes lists, as JSON has them)
    if isinstance(value, dict):
        return {key: _lists(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_lists(item) for item in value]
    return value


def _gti_dependency() -> HTMLDependency:
    # (The glue, run once per page, after the runtime: see packages/gti/src/shiny.ts)
    return HTMLDependency(
        "great-tables-gti-shiny",
        __version__,
        source={"subdir": str(JS_DIR)},
        script={"src": "gti-shiny.js"},
        all_files=False,
    )


def output_gt(id: str, placeholder: bool | None = None) -> Tag:
    """Output UI for a great_tables table.

    Parameters
    ----------
    id
        An output id.
    placeholder
        Deprecated and has no effect. This argument was never implemented and will be removed in a
        future release.
    """
    if placeholder is not None:
        warnings.warn(
            "The `placeholder` argument of `output_gt()` is deprecated, has no effect, and will be "
            "removed in a future release. Please remove it from your call to `output_gt()`.",
            FutureWarning,
            stacklevel=2,
        )

    return div({"class": "shiny-html-output"}, id=resolve_id(id))


@output_transformer(default_ui=output_gt)
async def GtTransformer(_meta: TransformerMetadata, _fn: ValueFn[GT | None]) -> RenderedDeps | None:
    value = await resolve_value_fn(_fn)
    if value is None:
        _keep_rows(_meta.session, _meta.name, None)
        return None
    elif isinstance(value, GT):
        from .gti import GTI

        session = _meta.session
        if isinstance(value, GTI) or value._options.ihtml_active.value:
            all_important = infer_render_env_defaults()["all_important"]
            engine = None
            if isinstance(value, GTI):
                # (Whose rows, kept on the server, there are this many of)
                attrs = f' data-gti-server="{table_rows(value)}"'
                html, spec, engine = render_table(value, all_important=all_important, attrs=attrs)
            else:
                html, spec = render_gti_element(value, all_important=all_important)
            _SPECS.setdefault(session.root_scope(), {})[session.ns(_meta.name)] = spec
            _keep_rows(session, _meta.name, engine)
            return session._process_ui(TagList(_gti_dependency(), HTML(inline_runtime(html))))
        _keep_rows(session, _meta.name, None)
        return session._process_ui(HTML(value._repr_html_()))

    raise TypeError(f"Expected a great_tables.GT object, got {type(value)}")


def _keep_rows(session: Session, name: str, engine: KernelEngine | None) -> None:
    # Keep the rows of an output's table on the server, with what answers the browser's asks for
    # them (see packages/gti/src/shiny.ts's `ShinySource`), or, without them, neither
    full_id = session.ns(name)
    if engine is None:
        if _ENGINES.get(session.root_scope(), {}).pop(full_id, None) is not None:
            session.set_message_handler(name + ASK_SUFFIX, None)
        return
    _ENGINES.setdefault(session.root_scope(), {})[full_id] = engine
    # (An error is the browser's to log, as it does a source's)
    session.set_message_handler(name + ASK_SUFFIX, lambda ask: engine.answer(_lists(ask)))


@overload
def render_gt() -> GtTransformer.OutputRendererDecorator: ...


@overload
def render_gt(_fn: GtTransformer.ValueFn) -> GtTransformer.OutputRenderer: ...


def render_gt(
    _fn: GtTransformer.ValueFn | None = None,
) -> GtTransformer.OutputRenderer | GtTransformer.OutputRendererDecorator:
    """Render a great_tables table.

    An interactive table (a `GTI` table, or a `GT` table with `opt_interactive()`) gives the app
    its state as inputs, for an output with id `id`:

    - `input.<id>_view()`: the table's view, a dict with its filters as a query in text
      (`"query"`), its `"search"`, its `"sort"` (columns, with a `-` before those in descending
      order), its `"page"` and `"page_size"`, its `"hidden"` columns and the column its rows are
      grouped by (`"group_by"`);
    - `input.<id>_rows()`: the data rows its search and filters keep (and linked tables'
      selections), in the order shown, on every page, numbered by position in the data (from 0);
    - `input.<id>_selection()`: the data rows selected, in data order.

    They're set once the table is shown, then after each change to them, whether the reader
    makes it or the server does, with [`update_gti()`](`great_tables.shiny.update_gti`). A table
    rendered again starts again with the view it's given.

    A `GTI` table with more rows than the browser is quick with keeps them on the server instead
    (see [`i_scale()`](`great_tables.GTI.i_scale`)), which sends the browser a page at a time:
    then `input.<id>_rows()` is found on the server, from the table's view (without linked
    tables' selections).
    """

    return GtTransformer(_fn)


def update_gti(
    id: str,
    *,
    query: str | dict[str, Any] | None = None,
    search: str | None = None,
    sort: str | list[str] | None = None,
    selection: list[int] | None = None,
    session: Session | None = None,
) -> None:
    """
    Change an interactive table's view or selection, from a Shiny app's server.

    The table (rendered with [`render_gt()`](`great_tables.shiny.render_gt`)) is filtered,
    searched, sorted, and has its rows selected, as if the reader had done it (so that a change to
    its filters, search or sort shows its first page). What isn't given (or is `None`) is left as
    it is. The table's inputs then give the new state (see `render_gt()`).

    Parameters
    ----------
    id
        The table's output id.
    query
        The table's filters: a query in text (as the query box has it), or as
        [`i_view()`](`great_tables.GTI.i_view`)'s `filter=` takes it; `""` for none.
    search
        The table's search; `""` for none.
    sort
        The columns to sort the table by, most significant first, each with a `-` before it to
        sort it in descending order (e.g., `["-net", "store"]`), or one column; `[]` to leave it
        unsorted.
    selection
        The data rows to select (numbered by position in the data, from 0), and only those; `[]`
        for none. The table must let readers select rows (with
        [`i_selection()`](`great_tables.GTI.i_selection`)).
    session
        The Shiny session (by default, the current one).

    Examples
    --------
    ```python
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
    """
    session = require_active_session(session)
    full_id = session.ns(id)
    # (Checked against the table as last rendered, if it has been)
    spec = _SPECS.get(session.root_scope(), {}).get(full_id)

    view: dict[str, Any] = {}
    if query is not None:
        view["filter"] = check_query_value(spec, query, "`query=`")
    if search is not None:
        view["search"] = check_search(search, "`search=`")
    if sort is not None:
        view["sort"] = check_sort(spec, sort, "`sort=`")
    message: dict[str, object] = {"id": full_id}
    if view:
        message["view"] = view
    if selection is not None:
        message["selection"] = check_selection(spec, selection, "`selection=`")
    if len(message) == 1:
        return

    # (Once the outputs rendered in this flush are sent, so that a table rendered again takes it)
    async def send() -> None:
        await session.send_custom_message(MESSAGE, message)

    session.on_flushed(send, once=True)

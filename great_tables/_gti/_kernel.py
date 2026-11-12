"""Kernel mode (`i_scale(engine="kernel")`): a table whose rows stay in Python (a widget's, in
the notebook's kernel, or a Shiny app's, on its server).

The browser has a page of the rows at a time, and the table is remote (its spec has `remote`, see
packages/gti/src/source.ts): it asks Python for each page of its view (and for a facet's counts),
which `KernelEngine` finds with Narwhals, on the data's own library, as the runtime would find
them (sorted by the spec's ranks, and searched and filtered by the cells' text, as the runtime
reads it), and gives as the page's rows' HTML, made as the table's body is (by rendering the body
with a stub of the page's rows, `_PageStub`). The spec it starts with has the first page of the
view, and leaves out what the browser would need every row for.

A table with row groups, summary rows, or a stub of more than one column (whose cells are merged
across rows) isn't kept in Python (see `kernel_reasons()`): its body's rows aren't one per data
row, in the data's order.

`render_table()` renders a table for a host that can keep its rows in Python, which keeps them if
`i_scale()` says to (and they can be).
"""

from __future__ import annotations

import json
import re
import warnings
from collections import Counter
from typing import TYPE_CHECKING, Any

from .._gt_data import Stub
from .._locations import LocBody, LocStub
from .._tbl_data import (
    _get_cell,
    _get_column_values,
    cast_frame_to_string,
    get_column_names,
    n_rows,
    reorder,
    replace_null_frame,
)
from .._utils_render_html import create_body_component_h
from ._pattern import pattern_search
from ._query import (
    JS_WHITESPACE,
    _body_trs,
    _data_cells,
    _free_name,
    _js_number,
    _leaves,
    _text_of,
    filter_exprs,
    fold,
    label_text,
    match_text,
)
from ._render import (
    MAX_BYTES,
    MAX_ROWS,
    GTIEngineWarning,
    _build,
    _warn_size,
    gti_element,
    render_gti_element,
)
from ._settings import settings_of
from ._spec import Spec, build_spec
from ._state import check_query_value

if TYPE_CHECKING:
    from .._gt_data import GroupRowInfo, GTData
    from ..gti import GTI

__all__ = ["KernelEngine", "kernel_reasons", "render_table"]

# A row of the body's HTML starts at a line of its own (as `create_body_component_h()` makes it),
# as each of its cells does
_ROW_START = re.compile(r"(?m)^  <tr(?=[ >])")
_CELL_START = re.compile(r'(?m)^    <(?:td|th)\b[^>]*? class="')

# What the search's terms are split at (JavaScript's `\s`)
_TERM_SPLIT = re.compile(f"[{re.escape(JS_WHITESPACE)}]+")

# The queries whose rows are kept, for the pages that follow
_CACHED = 4


class _PageStub(Stub):
    """A table's stub, but for its body's rows: those of a page (in its order), each without a
    group (`kernel_reasons()` keeps tables with row groups in the browser)."""

    def __init__(self, stub: Stub, rows: list[int]):
        self.rows = self._d = stub.rows
        self.group_rows = stub.group_rows
        self._page = rows

    def group_indices_map(self) -> list[tuple[int, GroupRowInfo | None]]:
        return [(row, None) for row in self._page]


def kernel_reasons(data: GTData) -> list[str]:
    """Why a built table's rows can't be kept in Python (none, if they can)."""
    from .._gt_data import ColInfoTypeEnum

    reasons = []
    # (A table of a LazyFrame is built without rows, so has no groups, but its column of them)
    if data._stub.group_ids or any(
        info.type == ColInfoTypeEnum.row_group for info in data._boxhead
    ):
        reasons.append("row groups")
    if data._summary_rows or data._summary_rows_grand:
        reasons.append("summary rows")
    if len(data._boxhead._get_stub_columns()) > 1:
        reasons.append("a stub of more than one column")
    return reasons


def _dropped(gti: GTI, spec: Spec) -> list[str]:
    """What a table does that it can't with its rows in Python."""
    settings = settings_of(gti)
    dropped = []
    if not settings.pagination:
        dropped.append("every row on one page (it has pages)")
    if spec["profiles"]:
        dropped.append("columns' profiles")
    if settings.row_details is not None:
        dropped.append("rows' details")
    if any(column["groupable"] for column in spec["columns"]):
        dropped.append("rows grouped by a column")
    if spec["colors"]:
        dropped.append("colors made again from the rows kept")
    exported = [f for f in spec["export"]["formats"] if f != "code"]
    if exported:
        dropped.append(f"its rows exported (as {_listed(list(map(repr, exported)))})")
    if spec["link"] is not None:
        dropped.append("a link to other tables")
    return dropped


def _warn_dropped(gti: GTI, spec: Spec) -> None:
    # (Called by an engine's `__init__()`)
    dropped = _dropped(gti, spec)
    if dropped:
        warnings.warn(
            "With its rows kept in Python (`i_scale()`), this table can't have "
            f"{_listed(dropped)}, so it's shown without.",
            GTIEngineWarning,
            # (For the caller of `i_as_widget()`)
            stacklevel=6,
        )


class KernelEngine:
    """A table's rows, in Python: the pages of its views, as the runtime would show them."""

    def __init__(self, gti: GTI) -> None:
        import narwhals as nw

        self._gti = gti
        self._built = built = _build(gti)
        # (Every row's, as the browser would have it, for Python's own use: checking views, and
        # finding rows)
        self.spec = spec = build_spec(built, details=[])
        _warn_dropped(gti, spec)
        self._nrows = spec["nrows"]
        # (Each column's missing values, for tinting them, as the runtime does)
        self._missing = [set(column["missing"] or []) for column in spec["columns"]]
        frame = nw.maybe_reset_index(nw.from_native(gti._tbl_data, eager_only=True))
        self._namespace = nw.get_native_namespace(frame)
        self._taken = set(frame.columns)
        self._frame = frame
        self._row = self._add("__gti_row", list(range(self._nrows)), nw.Int64)
        self._ranks: dict[str, tuple[str, str]] = {}
        self._texts: dict[str, list[str]] = {}
        self._folded: dict[str, str] = {}
        self._matched: dict[tuple[str, str], str] = {}
        self._cells: Any = None
        self._found: dict[str, list[int]] = {}

    # -----
    # Columns of the frame, added as they're needed

    def _add(self, base: str, values: list[Any], dtype: Any) -> str:
        import narwhals as nw

        name = _free_name(base, self._taken)
        self._taken.add(name)
        series = nw.new_series(name, values, dtype, backend=self._namespace)
        self._frame = self._frame.with_columns(series)
        return name

    def _rank_columns(self, column: str) -> tuple[str, str]:
        # A column's ranks, for sorting: whether each row's is missing (as missing values go last,
        # in either direction), and the rank
        import narwhals as nw

        if column not in self._ranks:
            ranks = self.spec["ranks"][column]
            self._ranks[column] = (
                self._add(f"__gti_missing_{column}", [int(r is None) for r in ranks], nw.Int64),
                self._add(
                    f"__gti_rank_{column}", [-1 if r is None else r for r in ranks], nw.Int64
                ),
            )
        return self._ranks[column]

    def _text(self, column: str) -> list[str]:
        """Each data row's text in a column, as the runtime matches it (not folded)."""
        if column not in self._texts:
            query_texts = {c["id"]: c["texts"] for c in self.spec["query_columns"]}
            if column in query_texts:
                self._texts[column] = list(query_texts[column] or [""] * self._nrows)
            else:
                self._texts[column] = self._cell_texts(column)
        return self._texts[column]

    def _cell_texts(self, column: str) -> list[str]:
        # (A cell's footnote marks aren't matched, but those placed on the left come with a space,
        # so the cells of rows with marks are read as they're rendered)
        cells = self._body_cells()
        values = _get_column_values(cells, column)
        texts = [
            match_text(value if isinstance(value, str) else str(_get_cell(cells, i, column)))
            for i, value in enumerate(values)
        ]
        marked = sorted(
            {
                int(footnote.rownum)
                for footnote in self._built._footnotes
                if isinstance(footnote.locname, (LocBody, LocStub)) and footnote.rownum is not None
            }
        )
        if marked:
            index = next(i for i, c in enumerate(self.spec["columns"]) if c["id"] == column)
            trs = _body_trs(f"<table>{self._body_html(marked)}</table>")
            for row, tr in zip(marked, trs):
                cells = _data_cells(tr)
                if index < len(cells):
                    texts[row] = _text_of(cells[index])[0]
        return texts

    def _body_cells(self) -> Any:
        # The cells' HTML, as `create_body_component_h()` has them (without footnote marks)
        if self._cells is None:
            built = self._built
            self._cells = replace_null_frame(
                built._body.body, cast_frame_to_string(built._tbl_data)
            )
        return self._cells

    def _folded_column(self, column: str) -> str:
        import narwhals as nw

        if column not in self._folded:
            folded = [fold(text) for text in self._text(column)]
            self._folded[column] = self._add(f"__gti_text_{column}", folded, nw.String)
        return self._folded[column]

    def _matched_column(self, column: str, pattern: str) -> str:
        # (With Python's `re`, as the runtime matches them, rather than the data's library)
        import narwhals as nw

        if (column, pattern) not in self._matched:
            search = pattern_search(pattern)
            found = [search(text) for text in self._text(column)]
            self._matched[column, pattern] = self._add(f"__gti_matches_{column}", found, nw.Boolean)
        return self._matched[column, pattern]

    # -----
    # Finding rows

    def _query(self, query: Any) -> tuple[Any, str, list[str], list[dict[str, Any]]]:
        """A query from the browser, checked: its filter, search, hidden columns, and sort."""
        if not isinstance(query, dict):
            raise TypeError(f"A query must be an object, not {query!r}.")
        spec = self.spec
        filter = check_query_value(spec, query.get("filter"), "The query's `filter`")
        search = query.get("search", "")
        hidden = query.get("hidden", [])
        sort = query.get("sort", [])
        if not isinstance(search, str):
            raise TypeError(f"The query's `search` must be text, not {search!r}.")
        if not (isinstance(hidden, list) and all(isinstance(c, str) for c in hidden)):
            raise TypeError(f"The query's `hidden` must be column names, not {hidden!r}.")
        if not (
            isinstance(sort, list)
            and all(
                isinstance(key, dict)
                and key.get("column") in spec["ranks"]
                and isinstance(key.get("descending", False), bool)
                for key in sort
            )
        ):
            raise ValueError(f"The query's `sort` must be keys of sortable columns, not {sort!r}.")
        return filter, search, hidden, sort

    def find(self, query: Any, sort: bool = True) -> list[int]:
        """The data rows a query (as the browser asks, a `RowQuery` or a `PageQuery`) keeps, in
        order (if `sort`, else in data order)."""
        import narwhals as nw

        filter, search, hidden, keys = self._query(query)
        key = json.dumps([filter, search, hidden, keys if sort else None], sort_keys=True)
        if key in self._found:
            return self._found[key]

        spec = self.spec
        texts: dict[str, str] = {}
        matched: dict[tuple[str, str], str] = {}
        for clause in _leaves(filter["and"] if filter is not None else []):
            col, op = clause["col"], clause["op"]
            if op == "contains":
                texts[col] = self._folded_column(col)
            elif op == "matches":
                matched[col, clause["value"]] = self._matched_column(col, clause["value"])
        predicates = filter_exprs(filter, spec, self._frame.schema, texts, matched)

        # (Every term is in a cell of a column searched, as `rowMatches()` has it)
        terms = [term for term in _TERM_SPLIT.split(fold(search)) if term != ""]
        if terms:
            searched = [
                self._folded_column(column["id"])
                for column in spec["columns"]
                if column["id"] is not None and column["searchable"] and column["id"] not in hidden
            ]
            for term in terms:
                found = [nw.col(name).str.contains(term, literal=True) for name in searched]
                predicates.append(
                    nw.any_horizontal(*found, ignore_nulls=True) if found else nw.lit(False)
                )

        # (The ranks' columns are added first, as the frame filtered is the one sorted)
        by: list[str] = []
        descending: list[bool] = []
        for k in keys if sort else []:
            missing, rank = self._rank_columns(k["column"])
            by += [missing, rank]
            descending += [False, k.get("descending", False)]
        frame = self._frame.filter(*predicates) if predicates else self._frame
        if by:
            frame = frame.sort([*by, self._row], descending=[*descending, False])
        rows = [int(row) for row in frame[self._row].to_list()]

        if len(self._found) >= _CACHED:
            del self._found[next(iter(self._found))]
        self._found[key] = rows
        return rows

    def rows(self, query: Any) -> list[int]:
        """The data rows a `RowQuery` keeps, in data order."""
        return self.find(query, sort=False)

    def facet(self, query: Any, column: Any) -> list[list[int]]:
        """The rows a `RowQuery` keeps with each value of a filter's column (its rank, or -1 for a
        missing value), as pairs."""
        if not any(f["column"] == column for f in self.spec["filters"]):
            raise ValueError(f"The table has no filter on column {column!r}.")
        ranks = self.spec["ranks"].get(column, [])
        counts = Counter(
            -1 if row >= len(ranks) or ranks[row] is None else ranks[row]
            for row in self.find(query, sort=False)
        )
        return [[key, count] for key, count in counts.items()]

    def page(self, query: Any) -> dict[str, Any]:
        """A page of the rows a `PageQuery` keeps (a `PageAnswer`): the last, if it starts past
        them."""
        start, size = query.get("start", 0), query.get("size")
        if isinstance(start, bool) or not isinstance(start, int) or start < 0:
            raise ValueError(f"The query's `start` must be a whole number, not {start!r}.")
        if size is not None and (isinstance(size, bool) or not isinstance(size, int) or size < 1):
            raise ValueError(f"The query's `size` must be a positive whole number, not {size!r}.")
        rows = self.find(query)
        count = len(rows)
        if size is None:
            start, shown = 0, rows
        else:
            if start >= count:
                start = max(0, (count - 1) // size * size)
            shown = rows[start : start + size]
        return {"count": count, "start": start, "rows": shown, "html": self.page_html(shown)}

    def answer(self, ask: Any) -> Any:
        """The answer to what the browser asks (an "ask": its `kind`, `query`, and a facet's
        `column`), as `page()`, `facet()` or `rows()` gives it."""
        if not isinstance(ask, dict):
            raise TypeError(f"An ask must be an object, not {ask!r}.")
        kind, query = ask.get("kind"), ask.get("query")
        if kind == "page":
            return self.page(query)
        if kind == "facet":
            return self.facet(query, ask.get("column"))
        if kind == "rows":
            return self.rows(query)
        raise ValueError(f"There's no answer to a {kind!r} ask.")

    def data(self, rows: list[int]) -> Any:
        """The data of the rows, in their order (a frame of the data's library)."""
        data = self._gti._tbl_data
        return reorder(data, rows, get_column_names(data))

    # -----
    # The rows' HTML

    def page_data(self, rows: list[int]) -> GTData:
        """The built table, with a body of `rows`."""
        return self._built._replace(_stub=_PageStub(self._built._stub, rows))

    def _body_html(self, rows: list[int]) -> str:
        return create_body_component_h(self.page_data(rows))

    def page_html(self, rows: list[int]) -> str:
        """The `<tr>`s of the rows, as the table's body has them, with their missing values tinted
        (as the runtime tints them, with `i_inspect()`)."""
        if not rows:
            return ""
        body = self._body_html(rows)
        starts = [found.start() for found in _ROW_START.finditer(body)]
        end = body.rindex("</tbody>")
        trs = [body[a:b].rstrip("\n") for a, b in zip(starts, [*starts[1:], end])]
        if len(trs) != len(rows):
            raise ValueError(f"The page's body has {len(trs)} rows, not {len(rows)}.")
        missing = self._missing_on(rows)
        if any(missing):
            trs = [self._tint(tr, row, missing) for tr, row in zip(trs, rows)]
        return "\n".join(trs)

    def _missing_on(self, rows: list[int]) -> list[set[int]]:
        # Each column's rows with a missing value (of those of a page, at least)
        return self._missing

    def _tint(self, tr: str, row: int, missing: list[set[int]]) -> str:
        columns = [i for i, rows in enumerate(missing) if row in rows]
        if not columns:
            return tr
        cells = list(_CELL_START.finditer(tr))
        # (If the row's cells can't be told apart, they're left as they are)
        if len(cells) != len(missing):
            return tr
        parts, last = [], 0
        for i in columns:
            at = cells[i].end()
            parts += [tr[last:at], "gt-i-missing "]
            last = at
        return "".join([*parts, tr[last:]])

    # -----
    # The table, as the browser starts with it

    def render(self, all_important: bool = False, attrs: str = "") -> tuple[str, Spec]:
        """The table's `<gt-table>` element, with the first page of its view (and `attrs`), and
        its spec."""
        spec = self.spec
        view = spec["view"]
        first = self.page(
            {
                "filter": view["filter"],
                "search": "",
                "hidden": view["hidden"],
                "links": [],
                "sort": view["sort"],
                "start": 0,
                "size": spec["pagination"]["page_size"],
            }
        )
        data = self.page_data(first["rows"])
        remote = self._remote_spec(first)
        table_html = data._render_as_html(all_important=all_important)
        return gti_element(data, table_html, remote, {}, attrs=attrs), remote

    def _remote_spec(self, first: dict[str, Any]) -> Spec:
        # The spec, without what the browser would need every row for: each column's ranks (the
        # sort is Python's), a column only for querying's texts, the rows with missing values
        # (but those on the page, which the runtime tints, and a filter's first, so that a facet
        # has a missing value to choose), and what's dropped (see `_dropped()`). A facet's (or a
        # bool filter's) values have their labels, which the browser can't read from its rows.
        spec = self.spec
        page = first["rows"]
        on_page = set(page)
        filters = []
        for f in spec["filters"]:
            remote_filter: Any = {**f, "missing": f["missing"][:1]}
            if f["type"] in ("facet", "bool") and f["values"] is not None:
                remote_filter["labels"] = self._labels(f["column"], len(f["values"]))
            filters.append(remote_filter)
        export = spec["export"]
        return Spec(
            **{
                **spec,
                "columns": [
                    {
                        **column,
                        "groupable": False,
                        "missing": None
                        if column["missing"] is None
                        else [row for row in column["missing"] if row in on_page],
                    }
                    for column in spec["columns"]
                ],
                "query_columns": [{**c, "texts": None} for c in spec["query_columns"]],
                "body": list(page),
                "ranks": {column: [] for column in spec["ranks"]},
                "pagination": {**spec["pagination"], "enabled": True},
                "filters": filters,
                "profiles": [],
                "view": {**spec["view"], "group_by": None},
                "export": {**export, "formats": [f for f in export["formats"] if f == "code"]},
                "details": [],
                "link": None,
                "colors": [],
                "remote": {"count": first["count"], "rows": list(page)},
            }
        )

    def _labels(self, column: str, count: int) -> list[str]:
        # Each value's label: the text of the first cell with it, as the runtime labels a facet's
        # values (or a column only for querying's text)
        ranks = self.spec["ranks"].get(column, [])
        first: dict[int, int] = {}
        for row, rank in enumerate(ranks):
            if rank is not None and rank not in first:
                first[rank] = row
        values = next(f["values"] for f in self.spec["filters"] if f["column"] == column) or []
        query_texts = {c["id"]: c["texts"] for c in self.spec["query_columns"]}
        texts = query_texts.get(column) or []
        labels = []
        for k in range(count):
            row = first.get(k)
            label = ""
            if row is not None and column not in query_texts:
                label = label_text(str(_get_cell(self._body_cells(), row, column)))
            elif row is not None and row < len(texts):
                label = texts[row]
            labels.append(label or _js_string(values[k] if k < len(values) else None))
        return labels


def render_table(
    gti: GTI, all_important: bool = False, attrs: str = ""
) -> tuple[str, Spec, KernelEngine | None]:
    """The table's element, its spec, and if its rows are kept in Python (as `i_scale()` says,
    and as they can be), what keeps them (and then the element has `attrs`)."""
    from ._lazy import LazyEngine, few_rows, lazy_of, lazy_reasons, template

    engine = settings_of(gti).engine
    lazy = lazy_of(gti) is not None
    # (Rendered without the warning that its rows aren't in Python)
    browser = gti._set_interactive(engine="browser")
    if engine == "browser":
        html, spec = render_gti_element(browser, all_important=all_important)
        return html, spec, None
    # (A table of a LazyFrame with few rows has them collected, then)
    if engine == "auto" and (few_rows(gti) if lazy else n_rows(gti._tbl_data) <= MAX_ROWS):
        html, spec = render_gti_element(browser, all_important=all_important, warn=False)
        if len(html.encode("utf-8")) <= MAX_BYTES:
            _warn_size(gti, spec, html)
            return html, spec, None
    if lazy:
        reasons = kernel_reasons(_build(template(gti)))
        reasons += [reason for reason in lazy_reasons(gti) if reason not in reasons]
    else:
        reasons = kernel_reasons(_build(gti))
    if reasons:
        if engine == "kernel":
            warnings.warn(
                f"The rows of a table with {_listed(reasons)} can't be kept in Python "
                '(`i_scale(engine="kernel")`) yet, so they\'re in the browser.',
                GTIEngineWarning,
                # (For the caller of `i_as_widget()`)
                stacklevel=4,
            )
        html, spec = render_gti_element(browser, all_important=all_important)
        return html, spec, None
    kernel = LazyEngine(gti) if lazy else KernelEngine(gti)
    html, _ = kernel.render(all_important=all_important, attrs=attrs)
    return html, kernel.spec, kernel


def _listed(items: list[str]) -> str:
    if len(items) <= 2:
        return " or ".join(items)
    return f"{', '.join(items[:-1])}, or {items[-1]}"


def _js_string(value: Any) -> str:
    # (A JSON value as JavaScript's `String()` has it)
    if value is None or isinstance(value, bool):
        return json.dumps(value)
    if isinstance(value, (int, float)):
        return _js_number(float(value))
    return str(value)

"""Tables of lazy frames (`GTI(lf)`: a Polars LazyFrame, a DuckDB relation or an Ibis table), whose
rows are collected as they're shown.

A `GTI` table of a lazy frame (called a LazyFrame here, whatever its backend) is made over a frame
with its columns but none of its rows (its template), and keeps the LazyFrame, with the calls of `GT`'s methods that made the table (`Lazy`:
see `gti.py`, which records them). The table of some of the rows (a page of them, or all) is made
again from them, by the same calls (`materialize()`): so only the rows shown are formatted, and
rendered. A method that needs every row (to color cells by their values, or a footnote on some of
them) can't be used on such a table, and its rows can't be chosen by their positions (which are a
page's, once it's made again).

A LazyFrame's rows are numbered as it has them, for Polars; a DuckDB relation's or an Ibis table's
have no order that's kept from one query to the next, so they're numbered as they sort by
`order_by=`'s columns, then by every other column that sorts (`Lazy.order`).

In kernel mode (a widget's, or a Shiny app's: see `_kernel.py`), `LazyEngine` finds the rows of
each view with queries on the LazyFrame (through Narwhals, but its columns' text: see
`_with_texts()`): the search and "contains" and "matches" clauses
match the rows' values, as text (not the cells' text, as the runtime matches them); and sorts them
by their values, as the runtime would by their ranks. Anywhere else (or for a table that can't
keep its rows in Python: see `kernel_reasons()`), the LazyFrame is collected, and the table is
shown as one of its rows (`collected()`).
"""

from __future__ import annotations

import inspect
from collections import Counter
from dataclasses import dataclass, field, replace
from typing import TYPE_CHECKING, Any

from .._gt_data import Boxhead, Stub
from .._locations import LocBody, LocStub
from .._tbl_data import (
    _get_cell,
    _get_column_missing,
    cast_frame_to_string,
    replace_null_frame,
)
from .._tbl_data_align import ALIGNMENT_MAP, NUMBER_LIKE_PATTERN
from ._kernel import _TERM_SPLIT, KernelEngine, _js_string, _warn_dropped
from ._pattern import pattern_code
from ._query import _free_name, _leaves, _value_key, filter_exprs, fold, label_text
from ._render import MAX_ROWS, _build
from ._spec import _json_value, build_spec

if TYPE_CHECKING:
    from .._gt_data import GroupRowInfo, GTData
    from ..gt import GT
    from ..gti import GTI

__all__ = ["Lazy", "LazyEngine", "collected", "eager", "lazy_of", "lazy_table"]


@dataclass(frozen=True)
class Lazy:
    """A table's LazyFrame, how `GTI()` was called with it (`init`), and the calls of the methods
    that made the table since (each one's name, and its arguments)."""

    frame: Any
    init: dict[str, Any]
    # (The table's columns as `GTI()` makes them, aligned by all of the rows)
    boxhead: Boxhead
    # (The columns its rows are numbered by, or `None` for its own order: see the module's notes)
    order: tuple[str, ...] | None
    calls: tuple[tuple[str, tuple[Any, ...], dict[str, Any]], ...] = ()
    # (What's found of the frame, kept for the table: its rows, collected, and their count)
    cache: dict[str, Any] = field(default_factory=dict, compare=False, repr=False)

    def called(self, name: str, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Lazy:
        calls = (*self.calls, (name, args, kwargs))
        # (The frame's rows are the same, but not the table of them)
        cache = {"count": self.cache["count"]} if "count" in self.cache else {}
        return Lazy(self.frame, self.init, self.boxhead, self.order, calls, cache)

    def numbered(self, row: str) -> Any:
        """The frame (a Narwhals LazyFrame), with its rows' numbers (as column `row`)."""
        frame = _narwhals().from_native(self.frame)
        return frame.with_row_index(row, order_by=None if self.order is None else list(self.order))

    def ordered(self) -> Any:
        """The frame (a Narwhals LazyFrame), its rows in their order (as they're numbered)."""
        frame = _narwhals().from_native(self.frame)
        if self.order is None:
            return frame
        row = _free_name("__gti_row", set(frame.collect_schema().names()))
        return self.numbered(row).sort(row).drop(row)


def _narwhals() -> Any:
    try:
        import narwhals
    except ImportError:
        raise ImportError(
            "A `GTI` table of a lazy frame needs the narwhals package: "
            "install it with `pip install narwhals`."
        ) from None
    return narwhals


def _sortable(dtype: Any) -> bool:
    nw = _narwhals()
    return not dtype.is_nested() and not isinstance(dtype, (nw.Object, nw.Unknown))


def lazy_table(
    frame: Any, init: dict[str, Any], order_by: str | list[str] | None = None
) -> tuple[Any, Lazy]:
    """A frame of a LazyFrame's columns, without rows (a DataFrame), for `GTI()` to make a table
    of, and the LazyFrame, with what `GTI()` was given (`init`), and the order of its rows (by the
    columns of `order_by=`, then the rest: see the module's notes)."""
    nw = _narwhals()
    lf = nw.from_native(frame)
    schema = lf.collect_schema()
    keys = [order_by] if isinstance(order_by, str) else list(order_by or [])
    unknown = [key for key in keys if key not in schema]
    if unknown:
        raise ValueError(f"`order_by=` names columns the data doesn't have: {unknown}.")
    order = None
    if keys or not lf.implementation.is_polars():
        order = (*keys, *(n for n, dtype in schema.items() if n not in keys and _sortable(dtype)))
        if not order:
            raise ValueError(
                "The rows of a lazy frame are numbered by their columns' values, which this "
                "one's columns can't be sorted by: give an `order_by=` column."
            )
    empty = lf.head(0).collect().to_native()
    boxhead = Boxhead(
        empty,
        auto_align=init["auto_align"],
        rowname_col=init["rowname_col"],
        groupname_col=init["groupname_col"],
    )
    # (A column of text that looks like numbers, in every row, is aligned as numbers are)
    texts = [name for name, dtype in schema.items() if dtype == nw.String]
    if init["auto_align"] and texts:
        found = (
            lf.select(
                (
                    (nw.col(name).null_count() < nw.len())
                    & nw.col(name).str.contains(NUMBER_LIKE_PATTERN.pattern).fill_null(True).all()
                ).alias(name)
                for name in texts
            )
            .collect()
            .rows(named=True)[0]
        )
        aligned = ALIGNMENT_MAP["numeric"]
        boxhead = Boxhead(
            [
                replace(info, column_align=aligned) if found.get(info.var) else info
                for info in boxhead
            ]
        )
    return empty, Lazy(frame, init, boxhead, order)


# The methods whose results are of the rows they're given (summary rows), which a table of a
# LazyFrame has only once it's made again from all of them (as it is in the browser), so that
# aren't run on the table without rows (`template()`)
UNRUN = {"summary_rows", "grand_summary_rows"}


def lazy_reasons(gti: GTI) -> list[str]:
    """Why a table of a LazyFrame can't keep its rows in Python, from the calls that made it (as
    `kernel_reasons()` has them)."""
    lazy = lazy_of(gti)
    assert lazy is not None
    return ["summary rows"] if any(name in UNRUN for name, _, _ in lazy.calls) else []


def lazy_of(gt: GT) -> Lazy | None:
    """The LazyFrame (and the rest) of a table of one, or `None`."""
    return gt.__dict__.get("_lazy")


def check_call(name: str, method: Any, args: tuple[Any, ...], kwargs: dict[str, Any]) -> None:
    """Raise if a method can't be used on a table of a LazyFrame (as it needs every row)."""
    if name == "data_color":
        raise ValueError(
            "`data_color()` colors cells by every row's values, so it can't be used on a table "
            "of a lazy frame (yet). Collect the frame first."
        )
    if name == "tab_footnote":
        bound = inspect.signature(method).bind(None, *args, **kwargs)
        locations = bound.arguments.get("locations")
        listed = locations if isinstance(locations, list) else [locations]
        if any(isinstance(location, (LocBody, LocStub)) for location in listed):
            raise ValueError(
                "A footnote on the body or the stub of a table of a lazy frame would be on the "
                "rows shown, not every row, so it can't be placed there (yet). Collect the frame "
                "first, or place it elsewhere (e.g., on a column label)."
            )


def template(gti: GTI) -> GTI:
    """A table of a LazyFrame, as one of no rows (its columns')."""
    return gti._replace(_lazy=None)


def materialize(gti: GTI, frame: Any) -> GTI:
    """A table of a LazyFrame, made again from some of its rows (a DataFrame, of its columns)."""
    from ..gti import GTI

    lazy = lazy_of(gti)
    assert lazy is not None
    table = GTI(frame, **lazy.init)
    table = table._replace(_boxhead=lazy.boxhead)
    for name, args, kwargs in lazy.calls:
        table = getattr(table, name)(*args, **kwargs)
    return table._replace(_interactive=gti._interactive)


def few_rows(gti: GTI) -> bool:
    """Whether a table of a LazyFrame has `MAX_ROWS` or fewer (which are then kept, collected)."""
    lazy = lazy_of(gti)
    assert lazy is not None
    if "few" not in lazy.cache:
        head = lazy.ordered().head(MAX_ROWS + 1).collect().to_native()
        lazy.cache["few"] = few = len(head) <= MAX_ROWS
        if few:
            lazy.cache["count"] = len(head)
            lazy.cache["collected"] = materialize(gti, head)
    return lazy.cache["few"]


def count(gti: GTI) -> int:
    """How many rows a table of a LazyFrame has."""
    nw = _narwhals()
    lazy = lazy_of(gti)
    assert lazy is not None
    if "count" not in lazy.cache:
        frame = nw.from_native(lazy.frame)
        lazy.cache["count"] = int(frame.select(nw.len()).collect().item())
    return lazy.cache["count"]


def collected(gti: GTI) -> GTI:
    """A table of a LazyFrame, made again from all of its rows (collected once)."""
    lazy = lazy_of(gti)
    assert lazy is not None
    if "collected" not in lazy.cache:
        lazy.cache["collected"] = materialize(gti, lazy.ordered().collect().to_native())
    return lazy.cache["collected"]._replace(_interactive=gti._interactive)


def eager(gt: GT) -> GT:
    """A table with its rows: a table of a LazyFrame, collected (see `collected()`)."""
    return collected(gt) if lazy_of(gt) is not None else gt  # type: ignore[arg-type]


def table_rows(gt: GT) -> int:
    """How many data rows a table has."""
    from .._tbl_data import n_rows

    return count(gt) if lazy_of(gt) is not None else n_rows(gt._tbl_data)  # type: ignore[arg-type]


class _PageRows(Stub):
    """A page's stub (that of a table made again from the page's rows), whose rows are numbered
    by their places in the data (in their cells' ids), as they are in the table of every row."""

    def __init__(self, stub: Stub, rows: list[int]):
        self.rows = self._d = stub.rows
        self.group_rows = stub.group_rows
        self._numbers = rows

    def group_indices_map(self) -> list[tuple[int, GroupRowInfo | None]]:
        return [(i, None) for i in range(len(self.rows))]

    def row_number(self, index: int) -> int:
        return self._numbers[index] + 1


def _texts(dtype: Any) -> bool:
    # Whether a column's values have text (not nested values, objects, bytes, or of no type)
    nw = _narwhals()
    return not dtype.is_nested() and not isinstance(dtype, (nw.Object, nw.Binary, nw.Unknown))


def _polars_text(column: str, dtype: Any) -> Any:
    # A column's values (of Narwhals' `dtype`), as text, as Polars has them
    import polars as pl

    if not _texts(dtype):
        return pl.lit(None, dtype=pl.String)
    if isinstance(dtype, _narwhals().Duration):
        return pl.col(column).dt.to_string()
    return pl.col(column).cast(pl.String)


def _polars_folded(text: Any) -> Any:
    # Text folded, as `fold()` folds it: decomposed, without combining marks, lowercased (a
    # character at a time, so a capital sigma is a sigma, which Polars makes final at a word's end)
    text = text.str.normalize("NFD").str.replace_all(r"\p{M}", "")
    return text.str.replace_all("Σ", "σ", literal=True).str.to_lowercase()


def _quoted(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


def _ibis_folds(table: Any) -> bool:
    # Whether an Ibis table's backend has DuckDB's `strip_accents()`
    from ibis.common.exceptions import IbisError

    try:
        return table._find_backend(use_default=True).name == "duckdb"
    except IbisError:
        return False


def refolder(frame: Any) -> Any:
    """How text folded by `fold()` is folded as a LazyFrame's backend folds its columns' text (see
    `_with_texts()`): DuckDB's `strip_accents()` composes what it leaves, as NFC does."""
    import unicodedata

    if frame.implementation.is_polars():
        return lambda text: text
    if frame.implementation.is_ibis() and not _ibis_folds(frame.to_native()):
        return lambda text: text
    return lambda text: unicodedata.normalize("NFC", text)


def _with_texts(frame: Any, schema: Any, texts: dict[str, tuple[str, bool]]) -> Any:
    """A LazyFrame (Narwhals') with columns of other columns' values as text, folded or not
    (`texts`: each new column's data column, and whether it's folded): made with each backend's
    own expressions, as Narwhals has none for folding text, nor for a Polars duration's text.

    (An Ibis table of a backend other than DuckDB has its text lowercased, but keeps its accents.)
    """
    nw = _narwhals()
    native = frame.to_native()
    impl = frame.implementation
    if impl.is_polars():
        exprs = {}
        for name, (column, folded) in texts.items():
            text = _polars_text(column, schema[column])
            exprs[name] = _polars_folded(text) if folded else text
        return nw.from_native(native.with_columns(**exprs))
    if impl.is_duckdb():
        import duckdb

        exprs = []
        for name, (column, folded) in texts.items():
            if _texts(schema[column]):
                text = f"CAST({_quoted(column)} AS VARCHAR)"
                text = f"lower(strip_accents({text}))" if folded else text
            else:
                text = "CAST(NULL AS VARCHAR)"
            exprs.append(duckdb.SQLExpression(text).alias(name))
        return nw.from_native(native.select(duckdb.StarExpression(), *exprs))
    if impl.is_ibis():
        import ibis

        strip = _ibis_folds(native)
        exprs = {}
        for name, (column, folded) in texts.items():
            if not _texts(schema[column]):
                exprs[name] = ibis.null("string")
                continue
            text = native[column].cast("string")
            if folded:
                text = (_strip_accents(text) if strip else text).lower()
            exprs[name] = text
        return nw.from_native(native.mutate(**exprs))
    raise TypeError(f"A table can't be of a lazy frame of {impl}.")


def _strip_accents(text: Any) -> Any:
    import ibis

    @ibis.udf.scalar.builtin
    def strip_accents(text: str) -> str: ...

    return strip_accents(text)


class _Rows:
    """What a table's filters need of the rows of its LazyFrame (see `FilterRows`)."""

    def __init__(self, frame: Any, row: str, nrows: int, schema: Any):
        self._frame = frame
        self._row = row
        self._schema = schema
        self.nrows = nrows

    def distinct(self, column: str) -> int:
        nw = _narwhals()
        col = nw.col(column)
        found = self._frame.filter(~col.is_null()).select(col.n_unique()).collect()
        return int(found.item())

    def values(self, column: str, type: str) -> list[Any]:
        nw = _narwhals()
        col = nw.col(column)
        dtype = self._schema[column]
        if type in ("facet", "bool"):
            # (Sorted as the backend sorts them, as the ranks of a DataFrame's column are)
            found = self._frame.select(col).filter(~col.is_null()).unique().sort(column)
            return [_json_value(value) for value in found.collect().get_column(column).to_list()]
        # (A range's numbers, but NaN and infinities, which it doesn't have; a date filter's
        # first and last, and if there are any, a time other than midnight and one with seconds)
        values = nw.when(col.is_finite()).then(col) if dtype.is_float() else col
        exprs = [values.min().alias("min"), values.max().alias("max")]
        if isinstance(dtype, nw.Datetime):
            seconds = (col.dt.second() != 0) | (col.dt.microsecond() != 0)
            timed = (col.dt.hour() != 0) | (col.dt.minute() != 0) | seconds
            exprs += [
                nw.when(timed).then(col).min().alias("time"),
                nw.when(seconds).then(col).min().alias("seconds"),
            ]
        found = self._frame.select(exprs).collect().rows()[0]
        return [_json_value(value) for value in sorted({v for v in found if v is not None})]

    def missing(self, column: str) -> list[int]:
        nw = _narwhals()
        col = nw.col(column)
        missing = col.is_null() | col.is_nan() if self._schema[column].is_float() else col.is_null()
        found = self._frame.filter(missing).select(nw.col(self._row).min()).collect().item()
        return [] if found is None else [int(found)]


class LazyEngine(KernelEngine):
    """A table of a LazyFrame's rows, in Python: its views found with queries of its backend (by
    Narwhals), and the tables of their pages made again from their rows (see `materialize()`)."""

    def __init__(self, gti: GTI) -> None:
        nw = _narwhals()
        lazy = lazy_of(gti)
        assert lazy is not None
        self._gti = gti
        # (The table without rows, for its columns)
        self._built = _build(template(gti))
        self._schema = schema = nw.from_native(lazy.frame).collect_schema()
        self._row = _free_name("__gti_row", set(schema.names()))
        self._frame = lazy.numbered(self._row)
        self._numbered = lazy.order is not None
        self._refold = refolder(self._frame)
        rows = _Rows(self._frame, self._row, count(gti), schema)
        self.spec = spec = build_spec(self._built, details=[], rows=rows)
        _warn_dropped(gti, spec)
        self._nrows = spec["nrows"]
        self._found: dict[str, list[int]] = {}
        # (The last page made, and its rows)
        self._made: tuple[list[int], GTData, list[set[int]]] | None = None

    # -----
    # Finding rows

    def _filtered(self, filter: Any, search: str, hidden: list[str]) -> Any:
        # The rows a query's filter and search keep (a Narwhals LazyFrame), in data order
        nw = _narwhals()
        spec, schema = self.spec, self._schema
        taken = {*schema.names(), self._row}
        added: dict[str, tuple[str, bool]] = {}
        folded: dict[str, str] = {}
        texts: dict[str, str] = {}
        matched: dict[tuple[str, str], str] = {}

        def text(col: str, fold: bool) -> str:
            # (The name of a column of a column's text, folded or not)
            names = folded if fold else texts
            if col not in names:
                names[col] = name = _free_name(f"__gti_{'folded' if fold else 'text'}_{col}", taken)
                taken.add(name)
                added[name] = (col, fold)
            return names[col]

        patterns: dict[str, Any] = {}
        for clause in _leaves([filter] if filter is not None else []):
            col, op = clause["col"], clause["op"]
            if op == "contains":
                text(col, True)
            elif op == "matches" and (col, clause["value"]) not in matched:
                matched[col, clause["value"]] = name = _free_name(f"__gti_matches_{col}", taken)
                taken.add(name)
                patterns[name] = (text(col, False), pattern_code(clause["value"]))

        # (Every term is in the value of a column searched, as text)
        terms = [self._refold(t) for t in _TERM_SPLIT.split(fold(search)) if t != ""]
        searched = []
        if terms:
            searched = [
                text(column["id"], True)
                for column in spec["columns"]
                if column["id"] is not None and column["searchable"] and column["id"] not in hidden
            ]

        frame = _with_texts(self._frame, schema, added) if added else self._frame
        if patterns:
            frame = frame.with_columns(
                **{
                    name: nw.col(col).str.contains(pattern)
                    for name, (col, pattern) in patterns.items()
                }
            )
        predicates = filter_exprs(filter, spec, schema, folded, matched, refold=self._refold)
        if predicates:
            frame = frame.filter(*predicates)
        for term in terms:
            found = [
                nw.col(name).str.contains(term, literal=True).fill_null(False) for name in searched
            ]
            frame = frame.filter(
                nw.any_horizontal(*found, ignore_nulls=False) if found else nw.lit(False)
            )
        dropped = [*added, *patterns]
        return frame.drop(dropped) if dropped else frame

    def find(self, query: Any, sort: bool = True) -> list[int]:
        import json

        filter, search, hidden, keys = self._query(query)
        key = json.dumps([filter, search, hidden, keys if sort else None], sort_keys=True)
        if key in self._found:
            return self._found[key]

        frame = self._filtered(filter, search, hidden)
        if sort and keys:
            # (By the columns' values, as the backend sorts them, missing values last, in either
            # direction, and ties in data order: as the ranks of a DataFrame's column sort)
            frame = frame.sort(
                [*(k["column"] for k in keys), self._row],
                descending=[*(k.get("descending", False) for k in keys), False],
                nulls_last=True,
            )
        elif self._numbered:
            # (Rows numbered by their columns are found in any order)
            frame = frame.sort(self._row)
        found = frame.select(self._row).collect().get_column(self._row).to_list()
        rows = [int(row) for row in found]

        if len(self._found) >= 4:
            del self._found[next(iter(self._found))]
        self._found[key] = rows
        return rows

    def facet(self, query: Any, column: Any) -> list[list[int]]:
        nw = _narwhals()
        found = next((f for f in self.spec["filters"] if f["column"] == column), None)
        if found is None:
            raise ValueError(f"The table has no filter on column {column!r}.")
        filter, search, hidden, _ = self._query(query)
        indices = {_value_key(value): i for i, value in enumerate(found["values"] or [])}
        grouped = (
            self._filtered(filter, search, hidden)
            .group_by(column)
            .agg(nw.len().alias(self._row))
            .collect()
        )
        counts: Counter[int] = Counter()
        for value, n in grouped.rows():
            key = -1 if value is None else indices.get(_value_key(_json_value(value)), -1)
            counts[key] += n
        return [[key, n] for key, n in counts.items()]

    def data(self, rows: list[int]) -> Any:
        """The data of the rows, in their order (a DataFrame, of the backend's)."""
        return self._collect(rows)

    def _collect(self, rows: list[int]) -> Any:
        # The rows' data, in their order (a DataFrame, of the backend's)
        nw = _narwhals()
        frame = self._frame.filter(nw.col(self._row).is_in(rows)).collect()
        places = {row: i for i, row in enumerate(rows)}
        numbers = frame.get_column(self._row).to_list()
        order = sorted(range(len(frame)), key=lambda i: places[numbers[i]])
        frame = frame[order] if order != list(range(len(frame))) else frame
        return frame.drop(self._row).to_native()

    # -----
    # The rows' HTML

    def _make(self, rows: list[int]) -> tuple[GTData, list[set[int]]]:
        # The built table of the rows (made again from them), and each column's rows with a
        # missing value (for tinting them)
        if self._made is not None and self._made[0] == rows:
            return self._made[1], self._made[2]
        frame = self._collect(rows)
        built = _build(materialize(self._gti, frame))
        built = built._replace(_stub=_PageRows(built._stub, rows))
        missing = [
            set()
            if column["id"] is None or column["missing"] is None
            else {rows[i] for i in _get_column_missing(frame, column["id"])}
            for column in self.spec["columns"]
        ]
        self._made = (list(rows), built, missing)
        return built, missing

    def page_data(self, rows: list[int]) -> GTData:
        return self._make(rows)[0]

    def _missing_on(self, rows: list[int]) -> list[set[int]]:
        return self._make(rows)[1]

    # -----
    # The table, as the browser starts with it

    def _remote_spec(self, first: dict[str, Any]) -> Any:
        spec = super()._remote_spec(first)
        missing = self._missing_on(first["rows"])
        spec["columns"] = [
            {**column, "missing": None if column["missing"] is None else sorted(rows)}
            for column, rows in zip(spec["columns"], missing)
        ]
        return spec

    def _labels(self, column: str, count: int) -> list[str]:
        # Each value's label: the text of the first cell with it (in the table made again from
        # those rows)
        nw = _narwhals()
        values = next(f["values"] for f in self.spec["filters"] if f["column"] == column) or []
        indices = {_value_key(value): i for i, value in enumerate(values)}
        firsts = self._frame.group_by(column).agg(nw.col(self._row).min()).collect()
        first: dict[int, int] = {}
        for value, row in firsts.rows():
            if value is not None:
                k = indices.get(_value_key(_json_value(value)))
                if k is not None:
                    first[k] = min(int(row), first.get(k, int(row)))
        rows = sorted(set(first.values()))
        cells = None
        if rows:
            built = self._make(rows)[0]
            cells = replace_null_frame(built._body.body, cast_frame_to_string(built._tbl_data))
        places = {row: i for i, row in enumerate(rows)}
        labels = []
        for k in range(count):
            row = first.get(k)
            label = ""
            if row is not None and cells is not None:
                label = label_text(str(_get_cell(cells, places[row], column)))
            labels.append(label or _js_string(values[k] if k < len(values) else None))
        return labels

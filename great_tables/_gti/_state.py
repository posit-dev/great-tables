"""A shown table's view and selection, as Python reads and sets them: from a notebook (with
`GTI.i_as_widget()`, in `_widget.py`) or a Shiny app (with `update_gti()`, in `great_tables.shiny`).

The browser gives the view as the `<gt-table>` element has it (`filter`, `sort` as keys, ...), and
Python reads it with the filter as a query in text and the sort as columns (with a `-` before
those in descending order). What's set is checked here against the table's spec, as `i_view()`
checks it, so that the browser applies it without an error.
"""

from __future__ import annotations

import operator
from typing import TYPE_CHECKING, Any

from ._query import check_query, check_view, format_query, parse_sort

if TYPE_CHECKING:
    from ._spec import Spec

__all__ = [
    "author_view",
    "check_query_value",
    "check_search",
    "check_selection",
    "check_sort",
    "sort_names",
    "view_of",
]


def author_view(spec: Spec) -> dict[str, Any]:
    """The view the table is first shown with (the author's), as the browser gives it."""
    pagination = spec["pagination"]
    return {
        "filter": spec["view"]["filter"],
        "sort": spec["view"]["sort"],
        "search": "",
        "page": 1,
        "page_size": pagination["page_size"] if pagination["enabled"] else None,
        "hidden": spec["view"]["hidden"],
        "group_by": spec["view"]["group_by"],
    }


def sort_names(keys: list[dict[str, Any]]) -> list[str]:
    """The sort's columns, with a `-` before those in descending order."""
    return [f"-{key['column']}" if key["descending"] else key["column"] for key in keys]


def view_of(view: dict[str, Any]) -> dict[str, Any]:
    """The view the browser gives, as Python reads it: the filter as a query in text (`query`)
    and the sort as columns (see `sort_names()`)."""
    return {
        "query": format_query(view.get("filter")),
        "search": view.get("search", ""),
        "sort": sort_names(view.get("sort") or []),
        "page": view.get("page", 1),
        "page_size": view.get("page_size"),
        "hidden": list(view.get("hidden") or []),
        "group_by": view.get("group_by"),
    }


def check_query_value(spec: Spec | None, value: Any, name: str) -> dict[str, Any] | None:
    """A query (in text, as `i_view()`'s `filter=` takes it, or `None` or blank text for none)
    checked against the table (if its spec is known): its columns' filters and kinds."""
    if isinstance(value, str) and value.strip() == "":
        value = None
    try:
        query = check_query(value)
    except ValueError as err:
        raise ValueError(str(err).replace("`filter=`", name)) from None
    if spec is None:
        return query
    kinds = {
        **{column["id"]: column["kind"] for column in spec["columns"]},
        **{column["id"]: column["kind"] for column in spec["query_columns"]},
    }
    check_view(query, (), spec["filters"], spec["ranks"], kinds=kinds)
    return query


def check_search(value: Any, name: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{name} must be a string, not {value!r}.")
    return value


def check_sort(spec: Spec | None, value: Any, name: str) -> list[dict[str, Any]]:
    """A sort (columns, a column, or `None`), as the browser's keys, checked against the table
    (if its spec is known)."""
    keys = parse_sort(value)
    for column, _ in keys:
        if spec is not None and column not in spec["ranks"]:
            raise ValueError(
                f"{name} can't sort the table by column {column!r}: it isn't one the table can "
                "be sorted by."
            )
    return [{"column": column, "descending": desc} for column, desc in keys]


def check_selection(spec: Spec | None, rows: Any, name: str) -> list[int]:
    """The data rows to select (in data order), as far as the table (if its spec is known) lets
    readers select them."""
    mode = spec["controls"]["selection"] if spec is not None else "multiple"
    nrows = spec["nrows"] if spec is not None else None
    if isinstance(rows, (str, bytes)):
        raise TypeError(f"{name} must be a list of data rows, not {rows!r}.")
    try:
        items = list(rows)
    except TypeError:
        raise TypeError(f"{name} must be a list of data rows, not {rows!r}.") from None
    checked: set[int] = set()
    for row in items:
        try:
            index = -1 if isinstance(row, bool) else operator.index(row)
        except TypeError:
            index = -1
        if index < 0:
            raise ValueError(f"{name} must hold data rows (whole numbers, from 0), not {row!r}.")
        if nrows is not None and index >= nrows:
            raise ValueError(f"{name} has row {index}, but the table has {nrows} rows.")
        checked.add(index)
    limit = {None: 0, "single": 1}.get(mode)
    if limit is not None and len(checked) > limit:
        raise ValueError(
            "The table's rows can't be selected: let readers select them with `i_selection()`."
            if mode is None
            else "Only one of the table's rows can be selected (it has `i_selection('single')`)."
        )
    return sorted(checked)

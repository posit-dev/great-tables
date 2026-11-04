"""How an interactive table behaves: its controls, pages, scrolling and look.

A `GTI` table keeps its settings, set by its `i_` methods; a `GT` table made interactive with
`opt_interactive()` has them in its options (`ihtml_*`), from which `Settings.from_options()` reads
them. The spec (see `_spec.py`) is made from either.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from .._gt_data import GTData, Options

SelectionMode = Literal["single", "multiple"]

SELECTION_MODES: tuple[SelectionMode, ...] = ("single", "multiple")

PaginationType = Literal["numbers", "simple", "full", "jump"]

PAGINATION_TYPES: tuple[PaginationType, ...] = ("numbers", "simple", "full", "jump")

PAGE_SIZES = (10, 25, 50, 100)

# A column's filter: as its kind suggests ("auto"), or the text it shows, a choice of its values,
# a range of its numbers, a range of its dates, or one of its booleans
FilterType = Literal["auto", "text", "facet", "range", "date", "bool"]

FILTER_TYPES: tuple[FilterType, ...] = ("auto", "text", "facet", "range", "date", "bool")

# How readers can export the rows: by copying them, or downloading them as CSV; or copy the code
# that filters and sorts the data as the view does
ExportFormat = Literal["csv", "clipboard", "code"]

EXPORT_FORMATS: tuple[ExportFormat, ...] = ("csv", "clipboard", "code")

# The side of the table a column is pinned to: the stub's (the first columns), or the other one
PinSide = Literal["left", "right"]

PIN_SIDES: tuple[PinSide, ...] = ("left", "right")


@dataclass(frozen=True)
class Settings:
    """An interactive table's settings, with `GTI`'s defaults."""

    sorting: bool = True
    search: bool = True
    resizing: bool = True
    selection: SelectionMode | None = None
    pagination: bool = True
    page_size: int = 10
    # (The sizes the reader can choose from; none, if `page_size_select` is off)
    page_sizes: tuple[int, ...] = PAGE_SIZES
    page_size_select: bool = True
    page_info: bool = True
    pagination_type: PaginationType = "jump"
    # (A CSS length; `None` to grow with the content)
    height: str | None = None
    highlight: bool = True
    compact: bool = False
    wrap: bool = True
    # (GTI's control bar below the table; `opt_interactive()` tables keep a search box above the
    # table and page controls below it, as `pagination_type` says)
    bar: bool = True
    # (The columns readers can't sort by, search, or resize, where the table lets them, as
    # `i_cols_controls()` set them, in the order they were set)
    unsortable: tuple[str, ...] = ()
    unsearchable: tuple[str, ...] = ()
    unresizable: tuple[str, ...] = ()
    # (The columns readers can hide, and those they can move, in the order they were set; none, by
    # default)
    hideable: tuple[str, ...] = ()
    reorderable: tuple[str, ...] = ()
    # (The columns left out of the table but shipped for querying, in the order they were set)
    query_only: tuple[str, ...] = ()
    # (The columns pinned to a side, as `i_cols_pin()` set them, in the order they were set)
    pins: tuple[tuple[str, PinSide], ...] = ()
    # (The columns readers can filter by, and how, in the order they were set)
    filters: tuple[tuple[str, FilterType], ...] = ()
    # (How the table is first shown: a query, checked as `i_view()` takes it, and sort keys,
    # each a column and whether it's descending; and the columns hidden)
    view_filter: dict[str, list[dict[str, Any]]] | None = None
    view_sort: tuple[tuple[str, bool], ...] = ()
    view_hidden: tuple[str, ...] = ()
    # (How readers can export the rows, from the bar; none, by default. The name of a download,
    # without its extension)
    export_formats: tuple[ExportFormat, ...] = ()
    export_filename: str = "table"
    # (Where the reader's view is kept, so that it's there when the page is opened again: in the
    # page's URL, and in the browser's storage; neither, by default. And whether the reader's
    # changes to it can be undone)
    view_state_url: bool = False
    view_state_storage: bool = False
    view_state_undo: bool = False

    @classmethod
    def from_options(cls, options: Options) -> Settings:
        """The settings `opt_interactive()` (or `tab_options()`) set in a table's options."""
        # (`tab_options()` takes "auto", a CSS length, or a number, made into px)
        height = options.ihtml_height.value
        # (`tab_options()` takes only these)
        selection = options.ihtml_selection_mode.value
        # (`opt_interactive()` doesn't check the type; the reactable renderer falls back the same way)
        pagination_type = options.ihtml_pagination_type.value
        return cls(
            sorting=bool(options.ihtml_use_sorting.value),
            search=bool(options.ihtml_use_search.value),
            resizing=bool(options.ihtml_use_resizers.value),
            selection=selection if selection in SELECTION_MODES else None,
            pagination=bool(options.ihtml_use_pagination.value),
            page_size=int(options.ihtml_page_size_default.value),
            page_sizes=tuple(
                int(size) for size in options.ihtml_page_size_values.value or PAGE_SIZES
            ),
            page_size_select=bool(options.ihtml_use_page_size_select.value),
            page_info=bool(options.ihtml_use_pagination_info.value),
            pagination_type=pagination_type if pagination_type in PAGINATION_TYPES else "numbers",
            height=None if height in (None, "auto") else str(height),
            highlight=bool(options.ihtml_use_highlight.value),
            compact=bool(options.ihtml_use_compact_mode.value),
            wrap=bool(options.ihtml_use_text_wrapping.value),
            bar=False,
        )


def settings_of(data: GTData) -> Settings:
    """A table's settings: a `GTI`'s own, or those in a `GT`'s options."""
    settings = getattr(data, "_interactive", None)
    return settings if isinstance(settings, Settings) else Settings.from_options(data._options)

"""How an interactive table behaves: its controls, pages, scrolling and look.

A `GTI` table keeps its settings, set by its `i_` methods; a `GT` table made interactive with
`opt_interactive()` has them in its options (`ihtml_*`), from which `Settings.from_options()` reads
them. The spec (see `_spec.py`) is made from either.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from .._gt_data import GTData, Options

SelectionMode = Literal["single", "multiple"]

SELECTION_MODES: tuple[SelectionMode, ...] = ("single", "multiple")

PaginationType = Literal["numbers", "simple", "full", "jump"]

PAGINATION_TYPES: tuple[PaginationType, ...] = ("numbers", "simple", "full", "jump")

PAGE_SIZES = (10, 25, 50, 100)


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
        )


def settings_of(data: GTData) -> Settings:
    """A table's settings: a `GTI`'s own, or those in a `GT`'s options."""
    settings = getattr(data, "_interactive", None)
    return settings if isinstance(settings, Settings) else Settings.from_options(data._options)

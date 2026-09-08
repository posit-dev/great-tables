# Set version ----
from importlib_metadata import version as _v

__version__ = _v("great_tables")

del _v

# Main gt imports ----
from typing import TYPE_CHECKING

from . import loc, style, vals

if TYPE_CHECKING:
    from .data import exibble as exibble
    from .data import load_dataset as load_dataset
from ._helpers import (
    LETTERS,
    define_units,
    google_font,
    html,
    letters,
    md,
    nanoplot_options,
    pct,
    px,
    random_id,
    stub,
    system_fonts,
)
from ._styles import FromColumn as from_column
from .gt import GT

__all__ = (
    "GT",
    "LETTERS",
    "define_units",
    "exibble",
    "from_column",
    "google_font",
    "html",
    "letters",
    "load_dataset",
    "loc",
    "md",
    "nanoplot_options",
    "pct",
    "px",
    "random_id",
    "stub",
    "style",
    "system_fonts",
    "vals",
)


def __getattr__(k: str):
    # exibble dataset available on top-level module, but is a pandas DataFrame.
    # Since pandas is an optional dependency, we import exibble dynamically.
    if k == "exibble":
        from great_tables.data import exibble

        return exibble

    if k == "load_dataset":
        from great_tables.data import load_dataset

        return load_dataset

    # allow the data submodule to be accessed directly, as if it were a top-level import
    if k == "data":
        import great_tables.data

        return great_tables.data

    raise AttributeError(f"cannot get attribute {k} from great_tables ({__file__})")

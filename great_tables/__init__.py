# Set version ----
from importlib_metadata import version as _v

__version__ = _v("great_tables")

del _v

# Main gt imports ----

from . import loc, style, vals
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
    system_fonts,
)
from ._styles import FromColumn as from_column
from .gt import GT

__all__ = (
    "GT",
    "exibble",
    "letters",
    "LETTERS",
    "px",
    "pct",
    "md",
    "html",
    "google_font",
    "system_fonts",
    "define_units",
    "nanoplot_options",
    "random_id",
    "from_column",
    "vals",
    "loc",
    "style",
)


def __getattr__(k: str):
    # exibble dataset available on top-level module, but is a pandas DataFrame.
    # Since pandas is an optional dependency, we import exibble dynamically.
    if k == "exibble":
        from great_tables.data import exibble

        return exibble

    # allow the data submodule to be accessed directly, as if it were a top-level import
    if k == "data":
        import great_tables.data

        return great_tables.data

    raise AttributeError(f"cannot get attribute {k} from great_tables ({__file__})")

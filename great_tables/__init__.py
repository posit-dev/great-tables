# Set version ----
from importlib_metadata import version as _v

__version__ = _v("great_tables")

del _v

# Main gt imports ----

from .gt import GT
from . import vals, loc, style
from ._styles import FromColumn as from_column
from ._helpers import (
    letters,
    LETTERS,
    px,
    pct,
    md,
    html,
    google_font,
    random_id,
    system_fonts,
    define_units,
    nanoplot_options,
)


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

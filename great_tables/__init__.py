# Set version ----
from importlib_metadata import version as _v

__version__ = _v("great_tables")

del _v

# Main gt imports ----

from .gt import GT
from . import vals
from . import loc
from . import style
from ._styles import FromColumn as from_column
from ._helpers import letters, LETTERS, px, pct, md, html, random_id, system_fonts, nanoplot_options


__all__ = (
    "GT",
    "exibble",
    "letters",
    "LETTERS",
    "px",
    "pct",
    "md",
    "html",
    "system_fonts",
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

    raise AttributeError(f"cannot get attribute {k} from great_tables ({__file__})")

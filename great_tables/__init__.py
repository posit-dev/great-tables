# Set version ----
from importlib_metadata import version as _v

__version__ = _v("great_tables")

del _v

# Main gt imports ----

from .gt import GT
from . import data
from . import vals
from . import loc
from . import style
from ._styles import FromColumn as from_column
from ._helpers import letters, LETTERS, px, pct, md, html, random_id, system_fonts
from .data import exibble


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
    "random_id",
    "from_column",
    "vals",
    "loc",
    "style",
)


def __getattr__(k: str):
    # datasets are no longer exposed in this module.
    # this function ensures that we raise a friendly error when people try to import them.

    dataset_names = [entry for entry in dir(data) if not entry.startswith("_")]
    if k in dataset_names:
        raise ImportError(
            "Cannot import dataset from top-level of package. Please import from data submodule:"
            f"\n\nfrom great_tables.data import {k}"
        )
    else:
        raise AttributeError(f"cannot get attribute {k} from great_tables ({__file__})")

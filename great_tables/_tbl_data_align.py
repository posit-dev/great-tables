"""Column classification for auto-alignment."""

from __future__ import annotations

import re
from datetime import date
from functools import singledispatch
from numbers import Real
from typing import TYPE_CHECKING, Literal

from ._tbl_data import (
    PdDataFrame,
    _get_column_dtype,
    is_na,
    to_list,
)

if TYPE_CHECKING:
    from ._tbl_data import DataFrameLike

AlignmentClass = Literal["numeric", "string", "other"]

ALIGNMENT_MAP: dict[AlignmentClass, Literal["right", "left", "center"]] = {
    "numeric": "right",
    "string": "left",
    "other": "center",
}

# Used with re.match, so it anchors at the start: "timestamp[us]" is numeric, "list(int64)" isn't
NUMERIC_DTYPE_PATTERN = re.compile(r"int|uint|float|date|double|timestamp")

# "object" is pandas 2 text, "str" pandas 3 text, and "[pyarrow]" names come from pandas ArrowDtype
STRING_DTYPES = {
    "object",
    "str",
    "utf8",
    "string",
    "large_string",
    "string_view",
    "string[pyarrow]",
    "large_string[pyarrow]",
    "string_view[pyarrow]",
}

# Dates, times and formatted numbers. The ` -/` range admits every character from space to `/`
NUMBER_LIKE_PATTERN = re.compile(r"^[0-9 -/:\\.]*$")


def is_number_like_column(data: DataFrameLike, column: str) -> bool:
    """True when the column holds at least one string and every string looks like a number."""
    strings = [val for val in to_list(data[column]) if isinstance(val, str)]
    return bool(strings) and all(NUMBER_LIKE_PATTERN.match(val) for val in strings)


@singledispatch
def classify_dtype_for_alignment(data: DataFrameLike, column: str) -> AlignmentClass:
    """Classify a column by its dtype: "numeric" (right), "string" (left) or "other" (center)."""
    dtype = str(_get_column_dtype(data, column)).lower()

    if NUMERIC_DTYPE_PATTERN.match(dtype):
        return "numeric"
    elif dtype in STRING_DTYPES:
        return "string"
    else:
        return "other"


@classify_dtype_for_alignment.register(PdDataFrame)
def _classify_pandas(data: PdDataFrame, column: str) -> AlignmentClass:
    dtype = str(data[column].dtype).lower()

    if NUMERIC_DTYPE_PATTERN.match(dtype):
        return "numeric"
    elif dtype == "object":
        values = [v for v in to_list(data[column]) if not is_na(data, v)]
        # An object column without strings is classified by what it holds, as the typed columns
        # of the other backends are: dates and numbers are numeric, anything else (booleans with
        # a missing value, times, decimals, lists, only missing values) is "other"
        if not any(isinstance(v, str) for v in values):
            if values and all(isinstance(v, date) for v in values):
                return "numeric"
            if values and all(isinstance(v, Real) and not isinstance(v, bool) for v in values):
                return "numeric"
            return "other"
        return "string"
    elif dtype in STRING_DTYPES:
        return "string"
    else:
        return "other"

"""Type classification for auto-alignment.

This module provides backend-specific dtype classification for determining
column text alignment. The approach uses singledispatch to handle pandas,
polars, and pyarrow backends with their native type APIs.
"""

from __future__ import annotations

import re
from functools import singledispatch
from typing import TYPE_CHECKING, Literal

from ._tbl_data import (
    PdDataFrame,
    PlDataFrame,
    PyArrowTable,
    _get_column_dtype,
    to_list,
)

if TYPE_CHECKING:
    from ._tbl_data import DataFrameLike

AlignmentClass = Literal["numeric", "string", "other"]

ALIGNMENT_MAP: dict[AlignmentClass, str] = {
    "numeric": "right",
    "string": "left",
    "other": "center",
}

# Pattern matching numeric types in dtype strings (matches at start of string)
# NOTE: Uses re.match (start anchored) to match original _str_detect behavior
# This means "list(int64)" won't match, but "int64" will
NUMERIC_DTYPE_PATTERN = re.compile(r"int|uint|float|date|double")

# String dtypes that should be left-aligned
# Includes "str" for pandas 3.x compatibility (pandas 2.x uses "object")
STRING_DTYPES = {"object", "utf8", "string", "str"}

# Pattern for "number-like" strings (dates, times, formatted numbers)
# NOTE: Preserves original behavior including the character class quirk
# The original pattern [0-9 -/:\\.] has " -/" which is technically a range from space to /
# We keep this for now to match existing behavior exactly
NUMBER_LIKE_PATTERN = re.compile(r"^[0-9 -/:\\.]*$")


def is_number_like_column(data: DataFrameLike, column: str) -> bool:
    """Check if an object/string column contains only number-like strings.

    Used to right-align object columns that contain formatted dates/numbers.

    Note: This preserves the original regex behavior exactly. See Phase 3 for bug fixes.
    """
    col_vals = to_list(data[column])

    # Match original behavior: only check string values, skip non-strings
    # If all string values match pattern (or there are no strings), return True
    number_like_matches = (
        NUMBER_LIKE_PATTERN.match(val) for val in col_vals if isinstance(val, str)
    )
    return all(number_like_matches)


@singledispatch
def classify_dtype_for_alignment(data: DataFrameLike, column: str) -> AlignmentClass:
    """Classify a column's dtype for alignment purposes.

    Returns:
        "numeric" -> right-aligned (numbers, dates, times)
        "string" -> left-aligned (text)
        "other" -> center-aligned (boolean, etc.)
    """
    # Fallback: use string-based pattern matching (matches original behavior)
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

    # Match original behavior: pattern-based detection
    if NUMERIC_DTYPE_PATTERN.match(dtype):
        return "numeric"
    elif dtype in STRING_DTYPES:
        return "string"
    else:
        return "other"


@classify_dtype_for_alignment.register(PlDataFrame)
def _classify_polars(data: PlDataFrame, column: str) -> AlignmentClass:
    dtype = str(data[column].dtype).lower()

    # Match original behavior: pattern-based detection
    if NUMERIC_DTYPE_PATTERN.match(dtype):
        return "numeric"
    elif dtype in STRING_DTYPES:
        return "string"
    else:
        return "other"


@classify_dtype_for_alignment.register(PyArrowTable)
def _classify_pyarrow(data: PyArrowTable, column: str) -> AlignmentClass:
    dtype = str(data.column(column).type).lower()

    # Match original behavior: pattern-based detection
    if NUMERIC_DTYPE_PATTERN.match(dtype):
        return "numeric"
    elif dtype in STRING_DTYPES:
        return "string"
    else:
        return "other"

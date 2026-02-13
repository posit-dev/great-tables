from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from ._tbl_data import Agnostic, _get_cell, _set_cell, is_na

if TYPE_CHECKING:
    from ._gt_data import Body, GTData
    from ._tbl_data import TblData


@dataclass(frozen=True)
class ColMergeInfo:
    """Information about a column merge operation.

    This class stores the configuration for a column merge and provides methods
    to validate the pattern and perform the actual value merging.

    Attributes
    ----------
    vars
        List of column names to merge. The first column is the target column.
    rows
        List of row indices to apply the merge to.
    type
        Type of merge operation (currently only 'merge' is used).
    pattern
        The pattern string for merging, using {0}, {1}, etc. for column references.
        Supports conditional sections with <<...>> for handling missing values.

    Notes
    -----
    The pattern uses 0-based indexing (e.g., {0} for the first column), consistent
    with standard Python indexing conventions.

    Examples
    --------
    >>> info = ColMergeInfo(
    ...     vars=["first", "last"],
    ...     rows=[0, 1, 2],
    ...     type="merge",
    ...     pattern="{0} {1}"
    ... )
    >>> info.merge("John", "Doe")
    'John Doe'
    """

    vars: list[str]
    rows: list[int]
    type: str
    pattern: str

    @property
    def pattern_columns(self) -> list[str]:
        """Extract unique column references from the pattern string.

        Returns
        -------
        list[str]
            Unique column reference numbers as strings (e.g., ["0", "1"]),
            in the order they first appear in the pattern.
        """
        matches = re.findall(r"\{(\d+)\}", self.pattern)

        seen: set[str] = set()
        result: list[str] = []

        for match in matches:
            if match not in seen:
                result.append(match)
                seen.add(match)

        return result

    def validate_pattern(self) -> None:
        """Validate that pattern references are valid for the provided columns.

        Raises
        ------
        ValueError
            If the pattern references a column index greater than or equal to
            the number of columns.
        """
        for col_ref in self.pattern_columns:
            col_idx = int(col_ref)

            if col_idx >= len(self.vars):
                raise ValueError(
                    f"Pattern references column {{{col_ref}}} but only {len(self.vars)} "
                    f"columns were provided (valid indices are 0 to {len(self.vars) - 1})."
                )

    @staticmethod
    def replace_na(*values: Any, tbl_data: TblData | None = None) -> tuple[Any, ...]:
        """Replace NA values with None for uniform missing value handling.

        This method normalizes various NA representations (NaN, pd.NA, None, etc.)
        to Python's None, making it easy to check for missing values with `is None`.

        Parameters
        ----------
        *values
            Values to check for NA.
        tbl_data
            Optional table data for backend-specific NA detection.
            If not provided, uses generic NA detection.

        Returns
        -------
        tuple
            Values with NA values replaced by None.

        Examples
        --------
        >>> import math
        >>> ColMergeInfo.replace_na("hello", math.nan, "world")
        ('hello', None, 'world')

        >>> ColMergeInfo.replace_na("a", None, "b")
        ('a', None, 'b')
        """
        check_data = tbl_data if tbl_data is not None else Agnostic()
        return tuple(None if is_na(check_data, v) else v for v in values)

    def merge(self, *values: Any) -> str:
        """Merge values according to pattern.

        This method provides a simple interface for merging values. Values that
        are None are treated as missing and will cause conditional sections
        (<<...>>) referencing them to be omitted.

        Parameters
        ----------
        *values
            Values to merge (positional, corresponding to {0}, {1}, etc.).
            Pass None for missing values. Use `replace_na()` first if you need
            to convert NA values from table data.

        Returns
        -------
        str
            The merged string result.

        Examples
        --------
        >>> info = ColMergeInfo(vars=["a", "b"], rows=[0], type="merge", pattern="{0} {1}")
        >>> info.merge("John", "Doe")
        'John Doe'

        >>> info = ColMergeInfo(vars=["a", "b"], rows=[0], type="merge", pattern="{0}<< ({1})>>")
        >>> info.merge("John", None)
        'John'
        """
        col_values = {str(i): str(v) if v is not None else "" for i, v in enumerate(values)}
        col_is_missing = {str(i): v is None for i, v in enumerate(values)}

        return _process_col_merge_pattern(self.pattern, col_values, col_is_missing)


ColMerges = list[ColMergeInfo]


# -- Pattern processing utilities -------------------------------------------------------

# Token used to represent missing values during pattern processing
_MISSING_VAL_TOKEN = "::NA::"


def _process_col_merge_pattern(
    pattern: str,
    col_values: dict[str, str],
    col_is_missing: dict[str, bool],
) -> str:
    """Process a column merge pattern by substituting values and handling missing data."""

    # Replace values with tokens if they are truly missing
    processed_values = {}
    for key, value in col_values.items():
        if col_is_missing.get(key, False):
            processed_values[key] = _MISSING_VAL_TOKEN
        else:
            processed_values[key] = value

    # Substitute `{n}` placeholders with values
    result = pattern
    for key, value in processed_values.items():
        result = result.replace(f"{{{key}}}", value)

    # Process conditional sections (`<<...>>`)
    if "<<" in result and ">>" in result:
        result = _resolve_conditional_sections(result)

    # Clean up any remaining missing value tokens
    result = result.replace(_MISSING_VAL_TOKEN, "NA")

    return result


def _resolve_conditional_sections(text: str) -> str:
    """Resolve conditional sections marked with <<...>> in text."""
    max_iterations = 100
    iteration = 0

    while "<<" in text and ">>" in text and iteration < max_iterations:
        iteration += 1

        # Find the last occurrence of `<<` (innermost section start)
        last_open = text.rfind("<<")
        if last_open == -1:
            break

        # Find the first `>>` after that `<<`
        first_close = text.find(">>", last_open)
        if first_close == -1:
            break

        # Extract the content between << and >>
        section_content = text[last_open + 2 : first_close]

        # Check if the section contains a missing value token
        if _MISSING_VAL_TOKEN in section_content:
            replacement = ""
        else:
            replacement = section_content

        text = text[:last_open] + replacement + text[first_close + 2 :]

    return text


def merge_pattern(pattern: str, *values: Any) -> str:
    """Merge values into a pattern string.

    This is a convenience function for quick experimentation with merge patterns
    outside of a GT table context.

    Parameters
    ----------
    pattern
        Pattern with {0}, {1}, etc. for positional values.
        Use <<...>> for conditional sections that are omitted
        if any referenced value inside is missing (None, NaN, etc.).
    *values
        Values to substitute (0-indexed in pattern).

    Returns
    -------
    str
        The merged string result.

    Examples
    --------
    >>> merge_pattern("{0} {1}", "John", "Doe")
    'John Doe'

    >>> merge_pattern("{0}<< ({1})>>", "John", None)
    'John'

    >>> merge_pattern("{0}—{1}", 10, 20)
    '10—20'

    >>> merge_pattern("{0}<< to {1}<< to {2}>>>>", 10, 20, None)
    '10 to 20'
    """
    normalized = ColMergeInfo.replace_na(*values)
    info = ColMergeInfo(pattern=pattern, vars=[], rows=[], type="merge")
    return info.merge(*normalized)


def perform_col_merge(data: GTData) -> GTData:
    """Perform all column merge operations on the table data.

    This function processes all column merge operations registered on the GT object,
    modifying the body data to contain the merged values.

    Parameters
    ----------
    data
        The GTData object containing the table data and merge operations.

    Returns
    -------
    GTData
        The modified GTData object with merged columns.
    """
    if not data._col_merge:
        return data

    new_body = data._body.copy()

    for col_merge in data._col_merge:
        new_body = _apply_single_col_merge(
            col_merge=col_merge,
            body=new_body,
            tbl_data=data._tbl_data,
        )

    return data._replace(_body=new_body)


def _apply_single_col_merge(
    col_merge: ColMergeInfo,
    body: Body,
    tbl_data: TblData,
) -> Body:
    """Apply a single column merge operation to the body.

    Parameters
    ----------
    col_merge
        The column merge specification.
    body
        The body data to modify.
    tbl_data
        The original table data (for checking missing values).

    Returns
    -------
    Body
        The modified body data.
    """
    if col_merge.type != "merge":
        raise NotImplementedError(
            f"Column merge type {col_merge.type!r} is not supported. "
            f"Only 'merge' is currently implemented."
        )

    col_merge.validate_pattern()

    target_column = col_merge.vars[0]

    for row_idx in col_merge.rows:
        # For each column, get the display value and determine if it's truly missing.
        # A value is only considered missing if BOTH the body AND original are NA.
        # This means sub_missing() replacements (e.g., "--") are not treated as missing,
        # matching R's gt behavior.
        values: list[Any] = []

        for col_name in col_merge.vars:
            formatted_value = _get_cell(body.body, row_idx, col_name)
            original_value = _get_cell(tbl_data, row_idx, col_name)

            original_na = ColMergeInfo.replace_na(original_value, tbl_data=tbl_data)
            formatted_na = ColMergeInfo.replace_na(formatted_value, tbl_data=body.body)

            if formatted_na[0] is None and original_na[0] is None:
                # Truly missing
                values.append(None)
            elif formatted_na[0] is None:
                # Body is NA but original has a value (unformatted)
                values.append(str(original_value))
            else:
                # Body has a value (possibly from sub_missing or formatting)
                values.append(str(formatted_value))

        merged_value = col_merge.merge(*values)

        result = _set_cell(body.body, row_idx, target_column, merged_value)

        # For Pandas and Polars, _set_cell() modifies in place and returns None but
        # for PyArrow, _set_cell() returns a new table
        if result is not None:
            body.body = result

    return body

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from ._tbl_data import Agnostic, _get_cell, _set_cell, is_na
from ._utils import _extract_pattern_columns, _process_col_merge_pattern

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
    type: str  # type of merge operation (only 'merge' used currently)
    pattern: str | None = None

    @property
    def pattern_columns(self) -> list[str]:
        """Extract column references from the pattern string.

        Returns
        -------
        list[str]
            List of column reference numbers as strings (e.g., ["0", "1"]).
        """
        if self.pattern is None:
            return []

        return _extract_pattern_columns(self.pattern)

    def validate_pattern(self) -> None:
        """Validate that pattern references are valid for the provided columns.

        Raises
        ------
        ValueError
            If the pattern is None (required for merge operations).
        ValueError
            If the pattern references a column index greater than or equal to
            the number of columns.
        """
        if self.pattern is None:
            raise ValueError("Pattern must be provided for column merge operations.")

        pattern_cols = self.pattern_columns

        for col_ref in pattern_cols:
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

        Raises
        ------
        ValueError
            If the pattern is None.

        Examples
        --------
        >>> info = ColMergeInfo(vars=["a", "b"], rows=[0], type="merge", pattern="{0} {1}")
        >>> info.merge("John", "Doe")
        'John Doe'

        >>> info = ColMergeInfo(vars=["a", "b"], rows=[0], type="merge", pattern="{0}<< ({1})>>")
        >>> info.merge("John", None)
        'John'
        """
        if self.pattern is None:
            raise ValueError("Pattern must be provided for column merge operations.")

        col_values = {str(i): str(v) if v is not None else "" for i, v in enumerate(values)}
        col_is_missing = {str(i): v is None for i, v in enumerate(values)}

        return _process_col_merge_pattern(self.pattern, col_values, col_is_missing)

    def merge_values(
        self,
        col_values: dict[str, str],
        col_is_missing: dict[str, bool],
    ) -> str:
        """Merge column values according to the pattern (dict-based interface).

        This method is used internally when values and missing status are already
        computed. For a simpler interface, use the `merge()` method instead.

        Parameters
        ----------
        col_values
            Dictionary mapping column indices (as strings, 0-based) to their display values.
        col_is_missing
            Dictionary mapping column indices (as strings, 0-based) to whether the
            original value was missing.

        Returns
        -------
        str
            The merged string result.

        Raises
        ------
        ValueError
            If the pattern is None.

        Examples
        --------
        >>> info = ColMergeInfo(vars=["a", "b"], rows=[0], type="merge", pattern="{0}-{1}")
        >>> info.merge_values({"0": "10", "1": "20"}, {"0": False, "1": False})
        '10-20'
        """
        if self.pattern is None:
            raise ValueError("Pattern must be provided for column merge operations.")

        return _process_col_merge_pattern(
            pattern=self.pattern,
            col_values=col_values,
            col_is_missing=col_is_missing,
        )


ColMerges = list[ColMergeInfo]


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
    # Use replace_na to normalize NA values to None (no tbl_data needed)
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
    # If no column merging defined, return unchanged
    if not data._col_merge:
        return data

    # Create a copy of the body for modification
    new_body = data._body.copy()

    # Process each column merge operation in order
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
        # TODO: incorporate other specialized merging operations (e.g., "merge_range") but
        # only handle the basic 'merge' type for now
        return body

    # Validate the pattern
    col_merge.validate_pattern()

    # Get the target column (column that receives the merged values)
    target_column = col_merge.vars[0]

    # Process each row (according to the `rows=` parameter in `cols_merge()`)
    for row_idx in col_merge.rows:
        # Collect values for all columns in this row
        merge_values = []

        for col_name in col_merge.vars:
            # Get the formatted value from the body
            formatted_value = _get_cell(body.body, row_idx, col_name)

            # Get the original value from the data table
            original_value = _get_cell(tbl_data, row_idx, col_name)

            body_is_na = is_na(body.body, formatted_value)
            original_is_na = is_na(tbl_data, original_value)

            # Determine the display value and whether it's missing for merge purposes
            # A value is only considered missing if BOTH the body AND original are NA.
            # This means sub_missing() replacements (e.g., "--") are not treated as missing.
            if body_is_na and original_is_na:
                # Truly missing: both body and original are NA
                merge_values.append(None)
            elif body_is_na and not original_is_na:
                # Cell is unformatted but has a value in the original data
                merge_values.append(str(original_value))
            else:
                # Cell is formatted (possibly by sub_missing): use formatted value
                merge_values.append(str(formatted_value))

        # Use merge() as it checks `val is None` for missing detection
        merged_value = col_merge.merge(*merge_values)

        # Set the merged value in the target column
        result = _set_cell(body.body, row_idx, target_column, merged_value)

        # For Pandas and Polars, _set_cell() modifies in place and returns None but
        # for PyArrow, _set_cell() returns a new table
        if result is not None:
            body.body = result

    return body

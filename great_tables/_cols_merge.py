from __future__ import annotations

from typing import TYPE_CHECKING

from ._tbl_data import _get_cell, _set_cell, is_na

if TYPE_CHECKING:
    from ._gt_data import Body, ColMergeInfo, GTData
    from ._tbl_data import TblData


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
        # Collect values and missing status for all columns
        col_values, col_is_missing = _collect_row_values(
            columns=col_merge.vars,
            row_idx=row_idx,
            body=body,
            tbl_data=tbl_data,
        )

        # Process the pattern with the collected values
        merged_value = col_merge.merge_values(col_values, col_is_missing)

        # Set the merged value in the target column
        result = _set_cell(body.body, row_idx, target_column, merged_value)

        # For Pandas and Polars, _set_cell() modifies in place and returns None but
        # for PyArrow, _set_cell() returns a new table
        if result is not None:
            body.body = result

    return body


def _collect_row_values(
    columns: list[str],
    row_idx: int,
    body: Body,
    tbl_data: TblData,
) -> tuple[dict[str, str], dict[str, bool]]:
    """Collect values and missing status for all columns in a row.

    Parameters
    ----------
    columns
        List of column names to collect values from.
    row_idx
        The row index to collect values from.
    body
        The body data containing formatted values.
    tbl_data
        The original table data for checking missing values.

    Returns
    -------
    tuple[dict[str, str], dict[str, bool]]
        A tuple of (col_values, col_is_missing) dictionaries.
        Keys are 1-based string indices (e.g., "1", "2", "3").
    """
    col_values: dict[str, str] = {}
    col_is_missing: dict[str, bool] = {}

    for i, col_name in enumerate(columns):
        # Get the formatted value from the body
        formatted_value = _get_cell(body.body, row_idx, col_name)

        # Get the original value from the data table
        original_value = _get_cell(tbl_data, row_idx, col_name)

        # If the body cell is missing (unformatted) and the original has a value,
        # use the original value; otherwise use the formatted value
        if is_na(body.body, formatted_value) and not is_na(tbl_data, original_value):
            # Cell is unformatted but has a value in the original data
            display_value = str(original_value)
        else:
            # If the cell is formatted OR the original is missing then use the
            # formatted value (which has the proper NA representation like "<NA>")
            display_value = str(formatted_value)

        # Store with 1-based index (as used in the pattern)
        col_key = str(i + 1)
        col_values[col_key] = display_value
        col_is_missing[col_key] = is_na(tbl_data, original_value)

    return col_values, col_is_missing

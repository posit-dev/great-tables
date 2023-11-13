from __future__ import annotations

import itertools

from typing import TYPE_CHECKING, Union, List, Dict, Optional

from ._gt_data import Spanners, SpannerInfo
from ._locations import resolve_cols_c

if TYPE_CHECKING:
    from ._gt_data import GTData, Boxhead


SpannerMatrix = List[Dict[str, Union[str, None]]]


def tab_spanner(
    data: GTData,
    label: str,
    columns: Union[list[str], str, None] = None,
    spanners: Union[list[str], str, None] = None,
    level: Optional[int] = None,
    id: Optional[str] = None,
    gather: bool = True,
    replace: bool = False,
):
    """Insert a spanner in the column labels part of a gt table.

    This part of the table contains, at a minimum, column labels and, optionally, an
    unlimited number of levels for spanners. A spanner will occupy space over any number
    of contiguous column labels and it will have an associated label and ID value. This
    function allows for mapping to be defined by column names, existing spanner ID values,
    or a mixture of both.

    The spanners are placed in the order of calling tab_spanner() so if a later call uses
    the same columns in its definition (or even a subset) as the first invocation, the
    second spanner will be overlaid atop the first. Options exist for forcibly inserting a
    spanner underneath other (with level as space permits) and with replace, which allows
    for full or partial spanner replacement.

    Parameters
    ----------
    label:
        Spanner label text.
    columns:
        Columns to target.
    spanners:
        Spanners to target.
    level:
        Spanner level for insertion.
    id:
        Spanner ID.
    gather:
        Gather columns together.
    replace:
        Replace existing spanners.
    """

    crnt_spanner_ids = [span.spanner_id for span in data._spanners]

    if id is None:
        id = label

    if isinstance(columns, str):
        columns = [columns]

    if isinstance(spanners, str):
        spanners = [spanners]

    # validations ----
    if level is not None and level < 0:
        raise ValueError(f"Level may not be negative. Received {level}.")
    if id in crnt_spanner_ids:
        raise ValueError(f"Spanner id {id} already exists.")

    # select columns ----

    if columns is None:
        # TODO: null_means is unimplemented
        raise NotImplementedError()

    selected_column_names = resolve_cols_c(columns, data, null_means="nothing")

    # select spanner ids ----
    # TODO: this supports tidyselect
    # TODO: could we use something like resolve_vector_l
    if spanners is not None:
        assert set(spanners).issubset(set(crnt_spanner_ids))
        spanner_ids = spanners
    else:
        spanner_ids = crnt_spanner_ids

    if not len(selected_column_names) and not len(spanner_ids):
        return data

    # get column names associated with selected spanners ----
    _vars = [span.vars for span in data._spanners if span.spanner_id in spanner_ids]
    spanner_column_names = list({k: True for k in itertools.chain(*_vars)})

    column_names = list({k: True for k in [*selected_column_names, *spanner_column_names]})

    # combine columns names and those from spanners ----

    # get spanner level ----
    if level is None:
        level = data._spanners.next_level(column_names)

    # get spanner units and labels ----
    # TODO: grep units from {{.*}}, may need to switch delimiters
    spanner_units = None
    spanner_pattern = None

    new_span = SpannerInfo(
        spanner_id=id,
        spanner_level=level,
        vars=column_names,
        spanner_units=spanner_units,
        spanner_pattern=spanner_pattern,
        spanner_label=label,
    )

    spanners = data._spanners.append_entry(new_span)

    new_data = data._replace(_spanners=spanners)

    if gather and not len(spanner_ids) and level == 0:
        return cols_move(new_data, columns=column_names, after=column_names[0])

    return new_data


def cols_move(data: GTData, columns: list[str], after: str) -> GTData:
    sel_cols = resolve_cols_c(columns, data)

    sel_after = resolve_cols_c([after], data)

    vars = [col.var for col in data._boxhead]

    if not len(sel_after):
        raise ValueError(f"Column {after} not found in table.")
    elif len(sel_after) > 1:
        raise ValueError(
            f"Only 1 value should be supplied to `after`, recieved argument: {sel_after}"
        )

    if not len(columns):
        raise Exception("No columns selected.")
    elif not all([col in vars for col in columns]):
        raise ValueError("All `columns` must exist and be visible in the input `data` table.")

    moving_columns = [col for col in sel_cols if col not in sel_after]
    other_columns = [col for col in vars if col not in moving_columns]

    indx = other_columns.index(after)
    final_vars = [*other_columns[: indx + 1], *moving_columns, *other_columns[indx + 1 :]]

    new_boxhead = data._boxhead.reorder(final_vars)
    return data._replace(_boxhead=new_boxhead)


def spanners_print_matrix(
    spanners: Spanners,
    boxhead: Boxhead,
    include_hidden: bool = False,
    ids: bool = False,
    omit_columns_row: bool = False,
) -> tuple[SpannerMatrix, list[str]]:
    if not include_hidden:
        # TODO: no "type" field on boxhead, is this use of visible right?
        vars = [row.var for row in boxhead if row.visible]
    else:
        vars = [row.var for row in boxhead]

    if not spanners:
        return empty_spanner_matrix(vars=vars, omit_columns_row=omit_columns_row)

    # Modify `spanners_tbl` such that:
    # (1) only visible vars are included in the `vars` column
    # (2) entries with no vars (after step 1) are removed, and
    # (3) `spanner_level` values have all gaps removed, being compressed
    #     down to start at 1 (e.g., 7, 5, 3, 1 -> 4, 3, 2, 1)
    _vars = [set(span.vars) & set(vars) for span in spanners]
    _lvls = sorted({span.spanner_level for span in spanners})

    non_empty_spans = [span for crnt_vars, span in zip(_vars, spanners) if len(crnt_vars)]
    new_levels = [_lvls.index(span.spanner_level) for span in non_empty_spans]

    crnt_spans = Spanners(non_empty_spans).relevel(new_levels)

    if not crnt_spans:
        return empty_spanner_matrix(vars=vars, omit_columns_row=omit_columns_row)

    spanner_height = len(_lvls)
    # TODO: span.built can be None. When does it get set?
    spanner_reprs = [span.spanner_id if ids else span.built for span in crnt_spans]

    # Create a matrix with dimension spanner_height x vars (e.g. presented columns)
    label_matrix: SpannerMatrix = [
        {var_name: None for var_name in vars} for _ in range(spanner_height)
    ]
    print(spanner_reprs)

    for span_ii, span in enumerate(crnt_spans):
        for var in span.vars:
            print(var)
            label_matrix[span.spanner_level][var] = spanner_reprs[span_ii]

    # reverse order , so if you were to print it out, level 0 would appear on the bottom
    label_matrix.reverse()

    # add column names to matrix
    if not omit_columns_row:
        label_matrix.append({var: var for var in vars})

    return label_matrix, vars


def empty_spanner_matrix(
    vars: list[str], omit_columns_row: bool
) -> tuple[SpannerMatrix, list[str]]:
    if omit_columns_row:
        return [], vars

    return [{var: var for var in vars}], vars


def seq_groups(seq: list[str]):
    # TODO: 0-length sequence
    if len(seq) == 0:
        raise StopIteration
    elif len(seq) == 1:
        yield seq[0], 1
    else:
        crnt_ttl = 1
        for crnt_el, next_el in zip(seq[:-1], seq[1:]):
            if crnt_el == next_el:
                crnt_ttl += 1
            else:
                yield crnt_el, crnt_ttl
                crnt_ttl = 1

        # final step has same elements, so we need to yield one last time
        if crnt_el == next_el:
            yield crnt_el, crnt_ttl

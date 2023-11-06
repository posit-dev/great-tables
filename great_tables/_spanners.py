from __future__ import annotations

from typing import TYPE_CHECKING, NewType, Union, List, Dict

from ._gt_data import Spanners

if TYPE_CHECKING:
    from ._gt_data import Boxhead


SpannerMatrix = List[Dict[str, Union[str, None]]]


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

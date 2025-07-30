from __future__ import annotations

import math
from datetime import date, datetime
from typing import TYPE_CHECKING, Any, Callable, Iterator, Sequence

import pandas as pd
from narwhals.typing import IntoSeries, SeriesT

if TYPE_CHECKING:
    from typing_extensions import TypeAlias


SeriesConstructor: TypeAlias = Callable[[Sequence[Any]], IntoSeries]


def zip_strict(left: SeriesT, right: SeriesT) -> Iterator[Any]:
    if len(left) != len(right):
        msg = f"{len(left)=} != {len(right)=}\nLeft: {left}\nRight: {right}"  # pragma: no cover
        raise AssertionError(msg)  # pragma: no cover
    return zip(left, right)


def assert_series_equal(left: SeriesT, right: SeriesT, *, check_name: bool = False) -> None:
    if check_name:
        left_name, right_name = left.name, right.name
        assert (
            left_name == right_name
        ), f"Expected names to be equal, found '{left_name}' and '{right_name}'"

    for i, (lhs, rhs) in enumerate(zip_strict(left, right)):
        if isinstance(lhs, float) and not math.isnan(lhs):
            are_equivalent_values = rhs is not None and math.isclose(
                lhs, rhs, rel_tol=0, abs_tol=1e-6
            )
        elif isinstance(lhs, float) and math.isnan(lhs):
            are_equivalent_values = rhs is None or math.isnan(rhs)
        elif isinstance(rhs, float) and math.isnan(rhs):
            are_equivalent_values = lhs is None or math.isnan(lhs)
        elif lhs is None:
            are_equivalent_values = rhs is None
        elif isinstance(lhs, list) and isinstance(rhs, list):
            are_equivalent_values = all(
                left_side == right_side for left_side, right_side in zip(lhs, rhs)
            )
        elif pd.isna(lhs):
            are_equivalent_values = pd.isna(rhs)
        elif type(lhs) is date and type(rhs) is datetime:
            are_equivalent_values = datetime(lhs.year, lhs.month, lhs.day) == rhs
        else:
            are_equivalent_values = lhs == rhs

        assert (
            are_equivalent_values
        ), f"Mismatch at index {i}: {lhs} != {rhs}\nExpected: {right}\nGot: {left}"

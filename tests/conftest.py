from __future__ import annotations

from importlib.util import find_spec

from typing import Any, Sequence

import pytest

from narwhals.typing import IntoSeries
from narwhals.utils import parse_version

from tests.utils import SeriesConstructor


def pandas_series_constructor(obj: Sequence[Any]) -> IntoSeries:
    import pandas as pd

    return pd.Series(obj)  # type: ignore[no-any-return]


def pandas_nullable_series_constructor(obj: Sequence[Any]) -> IntoSeries:
    import pandas as pd

    return pd.Series(obj).convert_dtypes(dtype_backend="numpy_nullable")  # type: ignore[no-any-return]


def pandas_pyarrow_series_constructor(obj: Sequence[Any]) -> IntoSeries:
    import pandas as pd

    return pd.Series(obj).convert_dtypes(dtype_backend="pyarrow")  # type: ignore[no-any-return]


def polars_series_constructor(obj: Sequence[Any]) -> IntoSeries:
    import polars as pl

    return pl.Series(obj)


def pyarrow_array_constructor(obj: Sequence[Any]) -> IntoSeries:
    import pyarrow as pa

    return pa.chunked_array([obj])  # type: ignore[no-any-return]


series_constructors: list[SeriesConstructor] = []

is_pyarrow_installed = find_spec("pyarrow") is not None

if find_spec("pandas"):
    import pandas as pd

    series_constructors.append(pandas_series_constructor)

    pandas_ge_v2 = parse_version(pd.__version__) >= parse_version("2.0.0")

    if pandas_ge_v2:
        series_constructors.append(pandas_nullable_series_constructor)

    if pandas_ge_v2 and is_pyarrow_installed:
        # pandas 2.0+ supports pyarrow dtype backend
        # https://pandas.pydata.org/docs/whatsnew/v2.0.0.html#new-dtype-backends
        series_constructors.append(pandas_pyarrow_series_constructor)

if find_spec("polars"):
    series_constructors.append(polars_series_constructor)

if is_pyarrow_installed:
    series_constructors.append(pyarrow_array_constructor)


@pytest.fixture(params=series_constructors)
def series_constructor(request: pytest.FixtureRequest):
    return request.param  # type: ignore[no-any-return]

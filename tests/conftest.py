from __future__ import annotations

from importlib.util import find_spec
from typing import Any

import pytest

from great_tables._tbl_data import DataFrameLike, SeriesLike, _re_version
from tests.utils import DataFrameConstructor, DataLike, SeriesConstructor


def pandas_constructor(obj: DataLike) -> DataFrameLike:
    import pandas as pd

    return pd.DataFrame(obj)  # type: ignore[no-any-return]


def pandas_nullable_constructor(obj: DataLike) -> DataFrameLike:
    import pandas as pd

    return pd.DataFrame(obj).convert_dtypes(dtype_backend="numpy_nullable")  # type: ignore[no-any-return]


def pandas_pyarrow_constructor(obj: DataLike) -> DataFrameLike:
    import pandas as pd

    return pd.DataFrame(obj).convert_dtypes(dtype_backend="pyarrow")  # type: ignore[no-any-return]


def polars_constructor(obj: DataLike) -> DataFrameLike:
    import polars as pl

    return pl.DataFrame(obj)


def pyarrow_table_constructor(obj: DataLike) -> DataFrameLike:
    import pyarrow as pa

    return pa.table(obj)  # type: ignore[no-any-return]


def pandas_series_constructor(obj: list[Any]) -> SeriesLike:
    import pandas as pd

    return pd.Series(obj)


def pandas_nullable_series_constructor(obj: list[Any]) -> SeriesLike:
    import pandas as pd

    return pd.Series(obj).convert_dtypes(dtype_backend="numpy_nullable")


def pandas_pyarrow_series_constructor(obj: list[Any]) -> SeriesLike:
    import pandas as pd

    return pd.Series(obj).convert_dtypes(dtype_backend="pyarrow")


def polars_series_constructor(obj: list[Any]) -> SeriesLike:
    import polars as pl

    return pl.Series(obj)


def pyarrow_array_constructor(obj: list[Any]) -> SeriesLike:
    import pyarrow as pa

    return pa.array(obj)


def pyarrow_chunked_array_constructor(obj: list[Any]) -> SeriesLike:
    import pyarrow as pa

    return pa.chunked_array([obj])


# the frame constructor that builds the same backend and dtypes as each series constructor
frame_constructor_by_series: dict[SeriesConstructor, DataFrameConstructor] = {
    pandas_series_constructor: pandas_constructor,
    pandas_nullable_series_constructor: pandas_nullable_constructor,
    pandas_pyarrow_series_constructor: pandas_pyarrow_constructor,
    polars_series_constructor: polars_constructor,
    pyarrow_array_constructor: pyarrow_table_constructor,
    pyarrow_chunked_array_constructor: pyarrow_table_constructor,
}

frame_constructors: list[DataFrameConstructor] = []
series_constructors: list[SeriesConstructor] = []

is_pandas_installed = find_spec("pandas") is not None
is_polars_installed = find_spec("polars") is not None
is_pyarrow_installed = find_spec("pyarrow") is not None

if is_pandas_installed:
    import pandas as pd

    frame_constructors.append(pandas_constructor)
    series_constructors.append(pandas_series_constructor)

    pandas_ge_v2 = _re_version(pd.__version__) >= (2, 0, 0)

    if pandas_ge_v2:
        frame_constructors.append(pandas_nullable_constructor)
        series_constructors.append(pandas_nullable_series_constructor)

    if pandas_ge_v2 and is_pyarrow_installed:
        # pandas 2.0+ supports pyarrow dtype backend
        # https://pandas.pydata.org/docs/whatsnew/v2.0.0.html#new-dtype-backends
        frame_constructors.append(pandas_pyarrow_constructor)
        series_constructors.append(pandas_pyarrow_series_constructor)

if is_polars_installed:
    frame_constructors.append(polars_constructor)
    series_constructors.append(polars_series_constructor)

if is_pyarrow_installed:
    frame_constructors.append(pyarrow_table_constructor)
    series_constructors.append(pyarrow_array_constructor)
    series_constructors.append(pyarrow_chunked_array_constructor)


@pytest.fixture(params=frame_constructors)
def frame_constructor(request: pytest.FixtureRequest) -> DataFrameConstructor:
    return request.param  # type: ignore[no-any-return]


@pytest.fixture(params=[c for c in frame_constructors if c.__name__.startswith("pandas_")])
def pandas_frame_constructor(request: pytest.FixtureRequest) -> DataFrameConstructor:
    return request.param  # type: ignore[no-any-return]


@pytest.fixture(params=series_constructors)
def series_constructor(request: pytest.FixtureRequest) -> SeriesConstructor:
    return request.param  # type: ignore[no-any-return]


@pytest.fixture
def paired_frame_constructor(series_constructor: SeriesConstructor) -> DataFrameConstructor:
    return frame_constructor_by_series[series_constructor]

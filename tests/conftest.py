from __future__ import annotations

from importlib.util import find_spec

import pytest

from great_tables._tbl_data import DataFrameLike, _re_version
from tests.utils import DataFrameConstructor, DataLike


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


frame_constructors: list[DataFrameConstructor] = []

is_pandas_installed = find_spec("pandas") is not None
is_polars_installed = find_spec("polars") is not None
is_pyarrow_installed = find_spec("pyarrow") is not None

if is_pandas_installed:
    import pandas as pd

    frame_constructors.append(pandas_constructor)

    pandas_ge_v2 = _re_version(pd.__version__) >= (2, 0, 0)

    if pandas_ge_v2:
        frame_constructors.append(pandas_nullable_constructor)

    if pandas_ge_v2 and is_pyarrow_installed:
        # pandas 2.0+ supports pyarrow dtype backend
        # https://pandas.pydata.org/docs/whatsnew/v2.0.0.html#new-dtype-backends
        frame_constructors.append(pandas_pyarrow_constructor)

if is_polars_installed:
    frame_constructors.append(polars_constructor)

if is_pyarrow_installed:
    frame_constructors.append(pyarrow_table_constructor)


@pytest.fixture(params=frame_constructors)
def frame_constructor(request: pytest.FixtureRequest) -> DataFrameConstructor:
    return request.param  # type: ignore[no-any-return]

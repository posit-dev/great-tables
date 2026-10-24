from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, Literal

from great_tables._tbl_data import DataFrameLike, SeriesLike
from great_tables._utils_render_html import (
    create_body_component_h,
    create_columns_component_h,
    create_source_notes_component_h,
)

if TYPE_CHECKING:
    from typing_extensions import TypeAlias


DataLike: TypeAlias = dict[str, list[Any]]
DataFrameConstructor: TypeAlias = Callable[[DataLike], DataFrameLike]
SeriesConstructor: TypeAlias = Callable[[list[Any]], SeriesLike]
Backend: TypeAlias = Literal["pandas", "polars", "pyarrow"]


def native_backend(obj: Any) -> Backend:
    library = type(obj).__module__.split(".")[0]
    if library in ("pandas", "polars", "pyarrow"):
        return library
    raise NotImplementedError(f"Unsupported data type: {type(obj)}")


def assert_rendered_source_notes(snapshot, gt):
    built = gt._build_data("html")
    source_notes = create_source_notes_component_h(built)

    assert snapshot == source_notes


def assert_rendered_columns(snapshot, gt):
    built = gt._build_data("html")
    columns = create_columns_component_h(built)

    assert snapshot == str(columns)


def assert_rendered_body(snapshot, gt):
    built = gt._build_data("html")
    body = create_body_component_h(built)

    assert snapshot == body


def assert_frame_equal(src: DataFrameLike, target: DataFrameLike):
    # Imports are deferred so this module can be loaded in the no-pandas test environment
    type_name = f"{type(src).__module__}.{type(src).__name__}"

    if type_name.startswith("pandas."):
        import pandas as pd

        pd.testing.assert_frame_equal(src, target)
    elif type_name.startswith("polars."):
        import polars.testing

        polars.testing.assert_frame_equal(src, target)
    elif type_name.startswith("pyarrow."):
        assert src.equals(target)
    else:
        raise NotImplementedError(f"Unsupported data type: {type(src)}")

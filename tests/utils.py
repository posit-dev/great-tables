from __future__ import annotations

import difflib
from typing import TYPE_CHECKING, Any, Callable, Literal, TypedDict

from great_tables._tbl_data import DataFrameLike, PdDataFrame, PlDataFrame, SeriesLike
from great_tables._utils_render_html import (
    create_body_component_h,
    create_columns_component_h,
    create_source_notes_component_h,
)

if TYPE_CHECKING:
    from syrupy.assertion import SnapshotAssertion
    from typing_extensions import TypeAlias


DataLike: TypeAlias = dict[str, list[Any]]
DataFrameConstructor: TypeAlias = Callable[[DataLike], DataFrameLike]
SeriesConstructor: TypeAlias = Callable[[list[Any]], SeriesLike]
Backend: TypeAlias = Literal["pandas", "polars", "pyarrow"]
Render: TypeAlias = Callable[[DataFrameConstructor], str]


class Divergent(TypedDict, total=False):
    """Why each constructor's output differs from the others today, keyed by constructor name."""

    pandas_constructor: str
    pandas_nullable_constructor: str
    pandas_pyarrow_constructor: str
    polars_constructor: str
    pyarrow_table_constructor: str


def native_backend(obj: Any) -> Backend:
    library = type(obj).__module__.split(".")[0]
    if library in ("pandas", "polars", "pyarrow"):
        return library
    raise NotImplementedError(f"Unsupported data type: {type(obj)}")


def cast_to_categorical(df: DataFrameLike, column: str, *, ordered: bool) -> DataFrameLike:
    # Python values can't build categorical columns. Ordered categories follow first appearance.
    # Imports are deferred so this module can be loaded in the no-pandas test environment.
    if isinstance(df, PdDataFrame):
        import pandas as pd

        categories = df[column].dropna().unique()
        categorical = pd.Categorical(df[column], categories=categories, ordered=ordered)
        return df.assign(**{column: categorical})

    if isinstance(df, PlDataFrame):
        import polars as pl

        categories = df[column].drop_nulls().unique(maintain_order=True)
        return df.with_columns(
            pl.col(column).cast(pl.Enum(categories) if ordered else pl.Categorical)
        )

    import pyarrow as pa

    encoded = df[column].dictionary_encode()
    if ordered:
        encoded = encoded.cast(
            pa.dictionary(encoded.type.index_type, encoded.type.value_type, ordered=True)
        )
    return df.set_column(df.column_names.index(column), column, encoded)


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


def assert_parity(
    snapshot: SnapshotAssertion,
    constructors: list[DataFrameConstructor],
    render: Render,
    divergent: Divergent | None = None,
) -> None:
    """Render one scenario with every constructor and assert the outputs agree.

    A constructor listed in `divergent` must still differ, and its own snapshot pins how, so a
    fix or a regression on either side fails the test.
    """
    divergent = divergent or {}
    unknown = divergent.keys() - Divergent.__annotations__.keys()
    assert not unknown, f"unknown constructors in divergent: {sorted(unknown)}"

    outputs: dict[str, str] = {}
    for constructor in constructors:
        try:
            outputs[constructor.__name__] = render(constructor)
        except Exception as e:
            # NOTE: a crash is an output too, so it can be listed as divergent
            outputs[constructor.__name__] = f"<raised {type(e).__name__}: {e}>"

    agreeing = {name: output for name, output in outputs.items() if name not in divergent}
    assert agreeing, "every constructor is listed as divergent"
    reference_name, reference = next(iter(agreeing.items()))
    # every backend raising the same error is agreement on a crash, not parity
    assert not reference.startswith("<raised "), f"{reference_name}: {reference}"
    mismatched = [name for name, output in agreeing.items() if output != reference]
    if mismatched:
        diff = difflib.unified_diff(
            reference.splitlines(),
            agreeing[mismatched[0]].splitlines(),
            reference_name,
            mismatched[0],
            lineterm="",
        )
        raise AssertionError(f"{mismatched} differ from {reference_name}\n" + "\n".join(diff))
    assert snapshot(name="all") == reference

    for name, reason in divergent.items():
        # pandas < 2 has no nullable or pyarrow-backed constructor
        if name in outputs:
            assert (
                outputs[name] != reference
            ), f"{name} now matches: drop it from divergent ({reason})"
            assert snapshot(name=name) == outputs[name]


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

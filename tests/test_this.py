from __future__ import annotations

import importlib
import sys

import pytest

import great_tables.this as zen
from great_tables._tbl_data import frame_from_dict
from tests.utils import DataFrameConstructor, native_backend


def test_import_prints_the_zen(capsys: pytest.CaptureFixture[str]):
    importlib.reload(zen)

    lines = capsys.readouterr().out.splitlines()

    assert lines[:2] == ["The Zen of Great Tables, by the Great Tables crew", ""]
    assert len(lines) == 2 + 19


def test_zen_table_renders(frame_constructor: DataFrameConstructor):
    html = zen._zen_table(frame_constructor(zen._COLUMNS)).as_raw_html()

    assert html.count("border-radius:999px") == 19
    assert html.count("<svg") == 19
    assert "Left for Rich Iannone to write." in html
    assert ">XX<" in html


@pytest.mark.parametrize(
    "blocked, expected",
    [((), "polars"), (("polars",), "pandas"), (("polars", "pandas"), "pyarrow")],
)
def test_frame_from_dict_prefers_polars_then_pandas_then_pyarrow(
    monkeypatch: pytest.MonkeyPatch, blocked: tuple[str, ...], expected: str
):
    pytest.importorskip(expected)
    for name in blocked:
        monkeypatch.setitem(sys.modules, name, None)

    assert native_backend(frame_from_dict({"x": [1, 2]})) == expected


def test_frame_from_dict_needs_a_dataframe_library(monkeypatch: pytest.MonkeyPatch):
    for name in ("polars", "pandas", "pyarrow"):
        monkeypatch.setitem(sys.modules, name, None)

    with pytest.raises(ImportError, match="polars, pandas, or pyarrow"):
        frame_from_dict({"x": [1]})

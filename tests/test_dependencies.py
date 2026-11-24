# Tests to be run with pandas uninstalled.

import pytest

# mark file as nopandas
pytestmark = pytest.mark.no_pandas


def test_no_pandas_import_fails():
    with pytest.raises(ModuleNotFoundError):
        import pandas


def test_no_pandas_import_exibble_works_with_polars():
    from great_tables import exibble
    import polars as pl

    assert isinstance(exibble, pl.DataFrame)


def test_no_pandas_import():
    from great_tables import GT


def test_no_pandas_vals_funcs_polars():
    from great_tables import vals
    import polars as pl

    assert vals.fmt_percent(pl.Series([0.11, 0.22]), decimals=0) == ["11%", "22%"]


def test_no_pandas_as_gridwell_polars():
    import json
    from pathlib import Path

    from great_tables import GT, exibble

    ir = json.loads(
        GT(exibble, rowname_col="row", groupname_col="group").fmt_number("num").as_gridwell()
    )
    assert ir["ir_version"] == "1.0"
    assert [g["group_id"] for g in ir["table"]["tbody"]] == ["grp_a", "grp_b"]
    # Valid IR, when jsonschema is there to check it
    jsonschema = pytest.importorskip("jsonschema")
    schema = Path(__file__).parent / "gridwell_kit" / "ir-1.0.schema.json"
    jsonschema.validate(ir, json.loads(schema.read_text(encoding="utf-8")))

import pandas as pd
from great_tables import GT
from great_tables.gt import _get_column_labels
from great_tables._helpers import UnitStr


def test_cols_label():
    df = pd.DataFrame({"x": [1.234, 2.345], "y": [3.456, 4.567]})
    gt = GT(df).cols_label(x="ex", y="why")

    x = _get_column_labels(gt=gt, context="html")
    y = ["ex", "why"]
    assert x == y


def test_cols_label_mix_cases_kwargs():
    df = pd.DataFrame({"x": [1.234, 2.345], "y": [3.456, 4.567], "z": [5.678, 6.789]})
    gt = GT(df).cols_label({"x": "ex"}, **{"y": "why"}, z="Zee")

    x = _get_column_labels(gt=gt, context="html")
    y = ["ex", "why", "Zee"]
    assert x == y


def test_cols_label_units_text():
    df = pd.DataFrame({"x": [1.234, 2.345], "y": [3.456, 4.567], "z": [5.678, 6.789]})
    gt = GT(df).cols_label(x="Area ({{m^2}})", y="Density ({{kg / m^3}})", z="Zee")

    x = _get_column_labels(gt=gt, context="text")
    assert isinstance(x[0], UnitStr)
    assert isinstance(x[1], UnitStr)
    assert x[2] == "Zee"

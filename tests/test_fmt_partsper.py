import pandas as pd
import pytest
from great_tables import GT, vals
from great_tables.gt import _get_column_of_values


@pytest.fixture
def df_proportions():
    return pd.DataFrame({"x": [0.001, 0.0001, 0.00001, 0.5, -0.005, 0]})


class TestFmtPartsperBasic:
    """Test basic fmt_partsper functionality with different to_units values."""

    def test_per_mille(self, df_proportions):
        gt = GT(df_proportions).fmt_partsper(columns="x", to_units="per-mille")
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == [
            "1.00\u2030",
            "0.10\u2030",
            "0.01\u2030",
            "500.00\u2030",
            "\u22125.00\u2030",
            "0.00\u2030",
        ]

    def test_per_myriad(self, df_proportions):
        gt = GT(df_proportions).fmt_partsper(columns="x", to_units="per-myriad")
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == [
            "10.00\u2031",
            "1.00\u2031",
            "0.10\u2031",
            "5,000.00\u2031",
            "\u221250.00\u2031",
            "0.00\u2031",
        ]

    def test_ppm(self):
        df = pd.DataFrame({"x": [0.000001, 0.0001, 0.01]})
        gt = GT(df).fmt_partsper(columns="x", to_units="ppm")
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == ["1.00 ppm", "100.00 ppm", "10,000.00 ppm"]

    def test_ppb(self):
        df = pd.DataFrame({"x": [0.000000001, 0.0000001]})
        gt = GT(df).fmt_partsper(columns="x", to_units="ppb")
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == ["1.00 ppb", "100.00 ppb"]

    def test_ppt(self):
        df = pd.DataFrame({"x": [0.000000000001, 0.0000000001]})
        gt = GT(df).fmt_partsper(columns="x", to_units="ppt")
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == ["1.00 ppt", "100.00 ppt"]

    def test_ppq(self):
        df = pd.DataFrame({"x": [0.000000000000001, 0.0000000000001]})
        gt = GT(df).fmt_partsper(columns="x", to_units="ppq")
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == ["1.00 ppq", "100.00 ppq"]

    def test_pcm(self):
        df = pd.DataFrame({"x": [0.00001, 0.001]})
        gt = GT(df).fmt_partsper(columns="x", to_units="pcm")
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == ["1.00 pcm", "100.00 pcm"]


class TestFmtPartsperOptions:
    """Test fmt_partsper with various formatting options."""

    def test_scale_values_false(self):
        df = pd.DataFrame({"x": [50.0, 100.0]})
        gt = GT(df).fmt_partsper(columns="x", to_units="ppm", scale_values=False)
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == ["50.00 ppm", "100.00 ppm"]

    def test_custom_symbol(self):
        df = pd.DataFrame({"x": [0.0000015]})
        gt = GT(df).fmt_partsper(columns="x", to_units="ppb", symbol="ppbV")
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == ["1,500.00 ppbV"]

    def test_decimals(self):
        df = pd.DataFrame({"x": [0.001]})
        gt = GT(df).fmt_partsper(columns="x", to_units="per-mille", decimals=0)
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == ["1\u2030"]

    def test_decimals_4(self):
        df = pd.DataFrame({"x": [0.001234]})
        gt = GT(df).fmt_partsper(columns="x", to_units="per-mille", decimals=4)
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == ["1.2340\u2030"]

    def test_drop_trailing_zeros(self):
        df = pd.DataFrame({"x": [0.001]})
        gt = GT(df).fmt_partsper(
            columns="x", to_units="per-mille", decimals=4, drop_trailing_zeros=True
        )
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == ["1\u2030"]

    def test_force_sign(self):
        df = pd.DataFrame({"x": [0.001, -0.001, 0]})
        gt = GT(df).fmt_partsper(columns="x", to_units="per-mille", force_sign=True)
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == ["+1.00\u2030", "\u22121.00\u2030", "0.00\u2030"]

    def test_incl_space_true_for_symbol(self):
        df = pd.DataFrame({"x": [0.001]})
        gt = GT(df).fmt_partsper(columns="x", to_units="per-mille", incl_space=True)
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == ["1.00 \u2030"]

    def test_incl_space_false_for_text(self):
        df = pd.DataFrame({"x": [0.000001]})
        gt = GT(df).fmt_partsper(columns="x", to_units="ppm", incl_space=False)
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == ["1.00ppm"]

    def test_pattern(self):
        df = pd.DataFrame({"x": [0.001]})
        gt = GT(df).fmt_partsper(columns="x", to_units="per-mille", pattern="[{x}]")
        x = _get_column_of_values(gt, column_name="x", context="html")
        assert x == ["[1.00\u2030]"]

    def test_use_seps_false(self):
        df = pd.DataFrame({"x": [0.5]})
        gt = GT(df).fmt_partsper(columns="x", to_units="per-mille", use_seps=False)
        x = _get_column_of_values(gt, column_name="x", context="html")
        # 0.5 * 1000 = 500, no separators needed here but test with large value
        df2 = pd.DataFrame({"x": [5.0]})
        gt2 = GT(df2).fmt_partsper(columns="x", to_units="per-mille", use_seps=False)
        x2 = _get_column_of_values(gt2, column_name="x", context="html")
        assert x2 == ["5000.00\u2030"]

    def test_sep_mark(self):
        df = pd.DataFrame({"x": [5.0]})
        gt = GT(df).fmt_partsper(columns="x", to_units="per-mille", sep_mark=".")
        x = _get_column_of_values(gt, column_name="x", context="html")
        # 5 * 1000 = 5000 -> "5.000" with sep_mark="." but dec_mark is still "."
        # We need to also change dec_mark to avoid confusion
        gt2 = GT(df).fmt_partsper(columns="x", to_units="per-mille", sep_mark=".", dec_mark=",")
        x2 = _get_column_of_values(gt2, column_name="x", context="html")
        assert x2 == ["5.000,00\u2030"]


class TestFmtPartsperValidation:
    """Test validation of fmt_partsper parameters."""

    def test_invalid_to_units(self):
        df = pd.DataFrame({"x": [0.001]})
        with pytest.raises(ValueError, match="Invalid `to_units` value"):
            GT(df).fmt_partsper(columns="x", to_units="invalid")

    def test_incl_space_auto_symbol_units(self):
        """Verify 'auto' gives no space for per-mille/per-myriad, space for text units."""
        df = pd.DataFrame({"x": [0.001]})

        # per-mille: no space
        gt1 = GT(df).fmt_partsper(columns="x", to_units="per-mille")
        x1 = _get_column_of_values(gt1, column_name="x", context="html")
        assert "\u2030" in x1[0] and " \u2030" not in x1[0]

        # ppm: space
        gt2 = GT(df).fmt_partsper(columns="x", to_units="ppm")
        x2 = _get_column_of_values(gt2, column_name="x", context="html")
        assert " ppm" in x2[0]


class TestFmtPartsperLatex:
    """Test LaTeX rendering of fmt_partsper."""

    def test_per_mille_latex(self):
        df = pd.DataFrame({"x": [0.001]})
        gt = GT(df).fmt_partsper(columns="x", to_units="per-mille")
        x = _get_column_of_values(gt, column_name="x", context="latex")
        assert x == ["1.00\\textperthousand{}"]

    def test_per_myriad_latex(self):
        df = pd.DataFrame({"x": [0.001]})
        gt = GT(df).fmt_partsper(columns="x", to_units="per-myriad")
        x = _get_column_of_values(gt, column_name="x", context="latex")
        assert x == ["10.00\\textpertenthousand{}"]

    def test_ppm_latex(self):
        df = pd.DataFrame({"x": [0.000001]})
        gt = GT(df).fmt_partsper(columns="x", to_units="ppm")
        x = _get_column_of_values(gt, column_name="x", context="latex")
        assert x == ["1.00 ppm"]


class TestValFmtPartsper:
    """Test the vals.fmt_partsper function."""

    def test_basic_per_mille(self):
        result = vals.fmt_partsper([0.001, 0.01, 0.1], to_units="per-mille")
        assert result == ["1.00\u2030", "10.00\u2030", "100.00\u2030"]

    def test_basic_ppm(self):
        result = vals.fmt_partsper([0.000001, 0.0001], to_units="ppm")
        assert result == ["1.00 ppm", "100.00 ppm"]

    def test_single_value(self):
        result = vals.fmt_partsper(0.001, to_units="per-mille")
        assert result == ["1.00\u2030"]

    def test_negative_values(self):
        result = vals.fmt_partsper([-0.001, -0.01], to_units="per-mille")
        assert result == ["\u22121.00\u2030", "\u221210.00\u2030"]

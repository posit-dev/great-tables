import pytest
import polars as pl
from great_tables import GT, vals


@pytest.fixture
def gt_tbl():
    df = pl.DataFrame({"x": [1.5e9, 2.7e6, 4200.0, 0.3, 0.00012, 2.4e-8]})
    return GT(df)


class TestFmtNumberSi:
    def test_basic_engineering_prefixes(self):
        result = vals.fmt_number_si([1.5e9, 2.7e6, 4200, 0.3, 0.00012, 2.4e-8])
        assert result == ["1.50 G", "2.70 M", "4.20 k", "300.00 m", "120.00 µ", "24.00 n"]

    def test_with_unit(self):
        result = vals.fmt_number_si([1.5e9, 2.7e6, 4200], unit="W")
        assert result == ["1.50 GW", "2.70 MW", "4.20 kW"]

    def test_zero_value(self):
        result = vals.fmt_number_si([0])
        assert result == ["0.00"]

    def test_zero_value_with_unit(self):
        result = vals.fmt_number_si([0], unit="m")
        assert result == ["0.00 m"]

    def test_negative_values(self):
        result = vals.fmt_number_si([-3500, -0.005])
        assert result == ["\u22123.50 k", "\u22125.00 m"]

    def test_no_prefix_needed(self):
        # Values between 1 and 999 in engineering mode need no prefix
        result = vals.fmt_number_si([5.0, 100.0, 999.0])
        assert result == ["5.00", "100.00", "999.00"]

    def test_decimals(self):
        result = vals.fmt_number_si([4200], decimals=0)
        assert result == ["4 k"]

    def test_decimals_four(self):
        result = vals.fmt_number_si([4200], decimals=4)
        assert result == ["4.2000 k"]

    def test_drop_trailing_zeros(self):
        result = vals.fmt_number_si([4200], decimals=4, drop_trailing_zeros=True)
        assert result == ["4.2 k"]

    def test_force_sign(self):
        result = vals.fmt_number_si([4200], force_sign=True)
        assert result == ["+4.20 k"]

    def test_incl_space_false(self):
        result = vals.fmt_number_si([4200], unit="Hz", incl_space=False)
        assert result == ["4.20kHz"]

    def test_scale_by(self):
        # Scale meters to millimeters (multiply by 1000)
        # 0.5 * 1000 = 500, which is in [1, 1000) so gets no prefix
        result = vals.fmt_number_si([0.5], unit="m", scale_by=1000)
        assert result == ["500.00 m"]

    def test_scale_by_with_prefix(self):
        # 1.2 * 1000 = 1200, which gets k prefix
        result = vals.fmt_number_si([1.2], unit="m", scale_by=1000)
        assert result == ["1.20 km"]

    def test_decimal_mode(self):
        result = vals.fmt_number_si([150], prefix_mode="decimal")
        assert result == ["1.50 h"]

    def test_decimal_mode_centi(self):
        result = vals.fmt_number_si([0.05], prefix_mode="decimal")
        assert result == ["5.00 c"]

    def test_pattern(self):
        result = vals.fmt_number_si([4200], pattern="[{x}]")
        assert result == ["[4.20 k]"]

    def test_dec_mark(self):
        result = vals.fmt_number_si([4200], dec_mark=",")
        assert result == ["4,20 k"]

    def test_n_sigfig(self):
        result = vals.fmt_number_si([0.0051, 0.000075, 0.0002], n_sigfig=2)
        assert result == ["5.1 m", "75 µ", "200 µ"]

    def test_n_sigfig_large(self):
        result = vals.fmt_number_si([1500, 2400000], n_sigfig=3)
        assert result == ["1.50 k", "2.40 M"]

    def test_gt_method(self, gt_tbl):
        # Verify the method exists and returns a GT object
        result = gt_tbl.fmt_number_si(columns="x", unit="W")
        assert isinstance(result, GT)

    def test_large_values(self):
        result = vals.fmt_number_si([1e15, 1e18, 1e24])
        assert result == ["1.00 P", "1.00 E", "1.00 Y"]

    def test_small_values(self):
        result = vals.fmt_number_si([1e-12, 1e-15, 1e-24])
        assert result == ["1.00 p", "1.00 f", "1.00 y"]

    def test_na_handling(self):
        result = vals.fmt_number_si([float("nan")])
        assert result == ["NaN"]

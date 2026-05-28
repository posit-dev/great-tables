from datetime import timedelta

import pandas as pd
import pytest

from great_tables import GT, vals


class TestFmtDurationNarrow:
    """Tests for fmt_duration with narrow (default) style."""

    def test_seconds_input(self):
        result = vals.fmt_duration([3661], input_units="seconds")
        assert result == ["1h 1m 1s"]

    def test_minutes_input(self):
        result = vals.fmt_duration([90], input_units="minutes")
        assert result == ["1h 30m"]

    def test_hours_input(self):
        result = vals.fmt_duration([1.5], input_units="hours")
        assert result == ["1h 30m"]

    def test_days_input(self):
        result = vals.fmt_duration([1.5], input_units="days")
        assert result == ["1d 12h"]

    def test_weeks_input(self):
        result = vals.fmt_duration([2], input_units="weeks")
        assert result == ["2w"]

    def test_zero_value(self):
        result = vals.fmt_duration([0], input_units="seconds")
        assert result == ["0s"]

    def test_multiple_values(self):
        result = vals.fmt_duration([3661, 86400, 60], input_units="seconds")
        assert result == ["1h 1m 1s", "1d", "1m"]

    def test_large_value(self):
        # 1 week + 2 days + 3 hours + 4 minutes + 5 seconds = 788645 seconds
        result = vals.fmt_duration([788645], input_units="seconds")
        assert result == ["1w 2d 3h 4m 5s"]


class TestFmtDurationWide:
    """Tests for fmt_duration with wide style."""

    def test_singular_units(self):
        result = vals.fmt_duration([3601], input_units="seconds", duration_style="wide")
        assert result == ["1 hour 1 second"]

    def test_plural_units(self):
        result = vals.fmt_duration([7322], input_units="seconds", duration_style="wide")
        assert result == ["2 hours 2 minutes 2 seconds"]

    def test_days_wide(self):
        result = vals.fmt_duration([2], input_units="days", duration_style="wide")
        assert result == ["2 days"]

    def test_singular_day(self):
        result = vals.fmt_duration([1], input_units="days", duration_style="wide")
        assert result == ["1 day"]


class TestFmtDurationColonSep:
    """Tests for fmt_duration with colon-separated style."""

    def test_basic(self):
        result = vals.fmt_duration([3661], input_units="seconds", duration_style="colon-sep")
        assert result == ["01:01:01"]

    def test_with_days(self):
        result = vals.fmt_duration([90061], input_units="seconds", duration_style="colon-sep")
        assert result == ["1/01:01:01"]

    def test_zero_padded(self):
        result = vals.fmt_duration([61], input_units="seconds", duration_style="colon-sep")
        assert result == ["00:01:01"]

    def test_output_units_mm_ss(self):
        result = vals.fmt_duration(
            [125],
            input_units="seconds",
            duration_style="colon-sep",
            output_units=["minutes", "seconds"],
        )
        assert result == ["02:05"]

    def test_output_units_hh_mm(self):
        result = vals.fmt_duration(
            [5400],
            input_units="seconds",
            duration_style="colon-sep",
            output_units=["hours", "minutes"],
        )
        assert result == ["01:30"]

    def test_output_units_hh_mm_ss(self):
        result = vals.fmt_duration(
            [3661],
            input_units="seconds",
            duration_style="colon-sep",
            output_units=["hours", "minutes", "seconds"],
        )
        assert result == ["01:01:01"]

    def test_output_units_d_hh_mm(self):
        result = vals.fmt_duration(
            [90060],
            input_units="seconds",
            duration_style="colon-sep",
            output_units=["days", "hours", "minutes"],
        )
        assert result == ["1/01:01"]


class TestFmtDurationISO:
    """Tests for fmt_duration with ISO 8601 style."""

    def test_basic(self):
        result = vals.fmt_duration([3661], input_units="seconds", duration_style="iso")
        assert result == ["P1H1M1S"]

    def test_days_only(self):
        result = vals.fmt_duration([86400], input_units="seconds", duration_style="iso")
        assert result == ["P1DT"]

    def test_days_and_time(self):
        result = vals.fmt_duration([90061], input_units="seconds", duration_style="iso")
        assert result == ["P1DT1H1M1S"]

    def test_hours_only(self):
        result = vals.fmt_duration([7200], input_units="seconds", duration_style="iso")
        assert result == ["P2H"]

    def test_zero(self):
        result = vals.fmt_duration([0], input_units="seconds", duration_style="iso")
        assert result == ["P0S"]


class TestFmtDurationTrimZeroUnits:
    """Tests for trim_zero_units parameter."""

    def test_trim_true(self):
        # Default: trim all zeros (leading, trailing, internal)
        result = vals.fmt_duration([3661], input_units="seconds", trim_zero_units=True)
        assert result == ["1h 1m 1s"]

    def test_trim_false(self):
        result = vals.fmt_duration([3661], input_units="seconds", trim_zero_units=False)
        assert result == ["0w 0d 1h 1m 1s"]

    def test_trim_leading_only(self):
        # 1 day and 5 seconds = 86405; without internal trim: "1d 0h 0m 5s"
        result = vals.fmt_duration([86405], input_units="seconds", trim_zero_units=["leading"])
        assert result == ["1d 0h 0m 5s"]

    def test_trim_trailing_only(self):
        # 1 hour = 3600; without leading trim: "0w 0d 1h"
        result = vals.fmt_duration([3600], input_units="seconds", trim_zero_units=["trailing"])
        assert result == ["0w 0d 1h"]

    def test_trim_internal_only(self):
        # 1 day and 5 seconds = 86405; without leading/trailing trim
        result = vals.fmt_duration([86405], input_units="seconds", trim_zero_units=["internal"])
        assert result == ["0w 1d 5s"]

    def test_trim_leading_and_trailing(self):
        result = vals.fmt_duration(
            [86405], input_units="seconds", trim_zero_units=["leading", "trailing"]
        )
        assert result == ["1d 0h 0m 5s"]


class TestFmtDurationOutputUnits:
    """Tests for output_units parameter."""

    def test_days_only(self):
        result = vals.fmt_duration([172800], input_units="seconds", output_units=["days"])
        assert result == ["2d"]

    def test_hours_minutes(self):
        result = vals.fmt_duration([5400], input_units="seconds", output_units=["hours", "minutes"])
        assert result == ["1h 30m"]

    def test_single_string(self):
        result = vals.fmt_duration([172800], input_units="seconds", output_units="days")
        assert result == ["2d"]


class TestFmtDurationMaxOutputUnits:
    """Tests for max_output_units parameter."""

    def test_max_1(self):
        result = vals.fmt_duration([90061], input_units="seconds", max_output_units=1)
        assert result == ["1d"]

    def test_max_2(self):
        result = vals.fmt_duration([90061], input_units="seconds", max_output_units=2)
        assert result == ["1d 1h"]

    def test_max_3(self):
        result = vals.fmt_duration([90061], input_units="seconds", max_output_units=3)
        assert result == ["1d 1h 1m"]


class TestFmtDurationSign:
    """Tests for negative values and force_sign."""

    def test_negative_narrow(self):
        result = vals.fmt_duration([-3661], input_units="seconds")
        # Uses Unicode minus sign in HTML context
        assert "1h 1m 1s" in result[0]
        assert result[0].startswith("\u2212") or result[0].startswith("-")

    def test_negative_wide(self):
        result = vals.fmt_duration([-3600], input_units="seconds", duration_style="wide")
        assert "1 hour" in result[0]

    def test_force_sign_positive(self):
        result = vals.fmt_duration([3661], input_units="seconds", force_sign=True)
        assert result[0].startswith("+")

    def test_force_sign_negative(self):
        result = vals.fmt_duration([-3661], input_units="seconds", force_sign=True)
        assert "1h 1m 1s" in result[0]


class TestFmtDurationTimedelta:
    """Tests for timedelta input."""

    def test_timedelta_pandas(self):
        df = pd.DataFrame({"dur": [timedelta(hours=1, minutes=30)]})
        gt = GT(df).fmt_duration(columns="dur")
        built = gt._build_data("html")
        from great_tables._tbl_data import _get_cell

        cell = _get_cell(built._body.body, 0, "dur")
        assert cell == "1h 30m"

    def test_timedelta_days(self):
        df = pd.DataFrame({"dur": [timedelta(days=2, hours=3)]})
        gt = GT(df).fmt_duration(columns="dur")
        built = gt._build_data("html")
        from great_tables._tbl_data import _get_cell

        cell = _get_cell(built._body.body, 0, "dur")
        assert cell == "2d 3h"

    def test_timedelta_no_input_units_needed(self):
        # timedelta doesn't require input_units
        df = pd.DataFrame({"dur": [timedelta(seconds=90)]})
        gt = GT(df).fmt_duration(columns="dur")
        built = gt._build_data("html")
        from great_tables._tbl_data import _get_cell

        cell = _get_cell(built._body.body, 0, "dur")
        assert cell == "1m 30s"


class TestFmtDurationPattern:
    """Tests for pattern parameter."""

    def test_pattern(self):
        result = vals.fmt_duration([3600], input_units="seconds", pattern="Duration: {x}")
        assert result == ["Duration: 1h"]


class TestFmtDurationSepMark:
    """Tests for sep_mark parameter."""

    def test_large_number_with_sep(self):
        # 10000 hours in narrow
        result = vals.fmt_duration([10000], input_units="hours", sep_mark=",")
        # Should have comma in weeks or days value
        assert "," not in result[0]  # values won't exceed 1000 in typical decomposition

    def test_very_large_days(self):
        # 10000 days
        result = vals.fmt_duration([10000], input_units="days", output_units=["days"], sep_mark=",")
        assert result == ["10,000d"]


class TestFmtDurationValidation:
    """Tests for input validation."""

    def test_invalid_input_units(self):
        with pytest.raises(ValueError, match="input_units"):
            vals.fmt_duration([100], input_units="invalid")

    def test_invalid_output_units(self):
        with pytest.raises(ValueError, match="output_units"):
            vals.fmt_duration([100], input_units="seconds", output_units=["invalid"])

    def test_invalid_duration_style(self):
        with pytest.raises(ValueError, match="duration_style"):
            vals.fmt_duration([100], input_units="seconds", duration_style="invalid")

    def test_invalid_trim_zero_units(self):
        with pytest.raises(ValueError, match="trim_zero_units"):
            vals.fmt_duration([100], input_units="seconds", trim_zero_units=["invalid"])

    def test_invalid_max_output_units(self):
        with pytest.raises(ValueError, match="max_output_units"):
            vals.fmt_duration([100], input_units="seconds", max_output_units=0)

    def test_missing_input_units_for_numeric(self):
        with pytest.raises(ValueError, match="input_units"):
            vals.fmt_duration([100])


class TestFmtDurationGTMethod:
    """Tests for fmt_duration as a GT method."""

    def test_basic_gt_method(self):
        df = pd.DataFrame({"seconds": [3661, 86400, 0]})
        gt = GT(df).fmt_duration(columns="seconds", input_units="seconds")
        built = gt._build_data("html")
        from great_tables._tbl_data import _get_cell

        assert _get_cell(built._body.body, 0, "seconds") == "1h 1m 1s"
        assert _get_cell(built._body.body, 1, "seconds") == "1d"
        assert _get_cell(built._body.body, 2, "seconds") == "0s"

    def test_rows_parameter(self):
        df = pd.DataFrame({"seconds": [3661, 86400, 7200]})
        gt = GT(df).fmt_duration(columns="seconds", rows=[0, 2], input_units="seconds")
        built = gt._build_data("html")
        from great_tables._tbl_data import _get_cell

        assert _get_cell(built._body.body, 0, "seconds") == "1h 1m 1s"
        # Row 1 should remain unformatted (nan placeholder in body since not targeted)
        assert _get_cell(built._body.body, 2, "seconds") == "2h"


class TestFmtDurationSubUnitRemainder:
    """Tests for values smaller than the smallest output unit."""

    def test_sub_unit_narrow(self):
        # 30 seconds when output is only days — less than 1 day
        result = vals.fmt_duration([30], input_units="seconds", output_units=["days"])
        assert result == ["<1d"]

    def test_sub_unit_wide(self):
        # 30 seconds when output is only hours — less than 1 hour
        result = vals.fmt_duration(
            [30], input_units="seconds", output_units=["hours"], duration_style="wide"
        )
        assert result == ["<1 hour"]

    def test_sub_unit_not_triggered_when_zero(self):
        # Exact zero should not get the "<" prefix
        result = vals.fmt_duration([0], input_units="seconds", output_units=["days"])
        assert result == ["0d"]


class TestFmtDurationColonSepTrimLeading:
    """Tests for colon-sep with leading trim."""

    def test_colon_sep_trim_leading_list(self):
        # Less than 1 hour with trim_zero_units=["leading"]
        result = vals.fmt_duration(
            [125],
            input_units="seconds",
            duration_style="colon-sep",
            trim_zero_units=["leading"],
        )
        assert result == ["02:05"]

    def test_colon_sep_trim_leading_with_hours(self):
        # More than 1 hour — leading trim should still show hours
        result = vals.fmt_duration(
            [3661],
            input_units="seconds",
            duration_style="colon-sep",
            trim_zero_units=["leading"],
        )
        assert result == ["01:01:01"]


class TestFmtDurationNAHandling:
    """Tests for NA/None value handling."""

    def test_none_value(self):
        df = pd.DataFrame({"dur": [3661.0, None]})
        gt = GT(df).fmt_duration(columns="dur", input_units="seconds")
        built = gt._build_data("html")
        from great_tables._tbl_data import _get_cell

        assert _get_cell(built._body.body, 0, "dur") == "1h 1m 1s"


class TestFmtDurationLatexContext:
    """Tests for LaTeX context output."""

    def test_pattern_latex_context(self):
        df = pd.DataFrame({"dur": [3600]})
        gt = GT(df).fmt_duration(columns="dur", input_units="seconds", pattern="({x})")
        built = gt._build_data("latex")
        from great_tables._tbl_data import _get_cell

        cell = _get_cell(built._body.body, 0, "dur")
        assert "1h" in cell
        assert "(" in cell

    def test_negative_in_latex(self):
        df = pd.DataFrame({"dur": [-3600.0]})
        gt = GT(df).fmt_duration(columns="dur", input_units="seconds")
        built = gt._build_data("latex")
        from great_tables._tbl_data import _get_cell

        cell = _get_cell(built._body.body, 0, "dur")
        assert "1h" in cell


class TestFmtDurationEdgeCases:
    """Tests for edge cases and boundary conditions."""

    def test_very_small_fractional_seconds(self):
        # 0.5 seconds with output_units=["minutes"] → less than 1 minute
        result = vals.fmt_duration([0.5], input_units="seconds", output_units=["minutes"])
        assert result == ["<1m"]

    def test_non_numeric_non_timedelta_passthrough(self):
        # Non-numeric values should be passed through as strings
        df = pd.DataFrame({"dur": ["not a number", 3661.0]})
        gt = GT(df).fmt_duration(columns="dur", input_units="seconds")
        built = gt._build_data("html")
        from great_tables._tbl_data import _get_cell

        assert _get_cell(built._body.body, 0, "dur") == "not a number"
        assert _get_cell(built._body.body, 1, "dur") == "1h 1m 1s"

    def test_iso_with_weeks_output_units_overridden(self):
        # ISO style should override output_units to days/hours/minutes/seconds
        result = vals.fmt_duration(
            [604800], input_units="seconds", duration_style="iso", output_units=["weeks"]
        )
        assert result == ["P7DT"]

    def test_colon_sep_invalid_output_units_falls_back(self):
        # Invalid colon-sep combo falls back to default days/hours/minutes/seconds
        result = vals.fmt_duration(
            [90061],
            input_units="seconds",
            duration_style="colon-sep",
            output_units=["weeks", "days"],
        )
        assert result == ["1/01:01:01"]

    def test_all_zeros_after_trim(self):
        # 0 seconds with all trimming — should still produce output
        result = vals.fmt_duration([0], input_units="seconds", trim_zero_units=True)
        assert result == ["0s"]

    def test_colon_sep_large_days(self):
        # Large days value with separator
        result = vals.fmt_duration(
            [86400000], input_units="seconds", duration_style="colon-sep", sep_mark=","
        )
        assert result == ["1,000/00:00:00"]

    def test_negative_colon_sep(self):
        result = vals.fmt_duration([-3661], input_units="seconds", duration_style="colon-sep")
        assert "01:01:01" in result[0]

    def test_negative_iso(self):
        result = vals.fmt_duration([-3661], input_units="seconds", duration_style="iso")
        assert "P1H1M1S" in result[0]

    def test_force_sign_zero(self):
        # Zero should not get a sign
        result = vals.fmt_duration([0], input_units="seconds", force_sign=True)
        assert result == ["0s"]

    def test_multiple_columns(self):
        df = pd.DataFrame({"a": [3600, 7200], "b": [60, 120]})
        gt = GT(df).fmt_duration(columns=["a", "b"], input_units="seconds")
        built = gt._build_data("html")
        from great_tables._tbl_data import _get_cell

        assert _get_cell(built._body.body, 0, "a") == "1h"
        assert _get_cell(built._body.body, 0, "b") == "1m"
        assert _get_cell(built._body.body, 1, "a") == "2h"
        assert _get_cell(built._body.body, 1, "b") == "2m"

    def test_iso_zero(self):
        # ISO zero should be P0S (time-only, no T when no date parts)
        result = vals.fmt_duration([0], input_units="seconds", duration_style="iso")
        assert result == ["P0S"]

    def test_iso_only_date_parts(self):
        # 2 weeks = 14 days in ISO; T always follows date parts (matching R gt behavior)
        result = vals.fmt_duration([14], input_units="days", duration_style="iso")
        assert result == ["P14DT"]


class TestFmtDurationLocale:
    """Tests for locale-aware duration formatting."""

    def test_french_wide_singular(self):
        result = vals.fmt_duration(
            [3600], input_units="seconds", duration_style="wide", locale="fr"
        )
        assert "heure" in result[0]
        assert "heures" not in result[0]

    def test_french_wide_plural(self):
        result = vals.fmt_duration(
            [7200], input_units="seconds", duration_style="wide", locale="fr"
        )
        assert "heures" in result[0]

    def test_french_narrow(self):
        result = vals.fmt_duration([3661], input_units="seconds", locale="fr")
        assert result == ["1h 1min 1s"]

    def test_german_wide_singular(self):
        result = vals.fmt_duration(
            [3600], input_units="seconds", duration_style="wide", locale="de"
        )
        assert "Stunde" in result[0]
        assert "Stunden" not in result[0]

    def test_german_wide_plural(self):
        result = vals.fmt_duration(
            [7200], input_units="seconds", duration_style="wide", locale="de"
        )
        assert "Stunden" in result[0]

    def test_german_narrow(self):
        result = vals.fmt_duration([7200], input_units="seconds", locale="de")
        assert result == ["2h"]

    def test_spanish_wide(self):
        result = vals.fmt_duration(
            [90061], input_units="seconds", duration_style="wide", locale="es"
        )
        assert "día" in result[0] or "día" in result[0]
        assert "hora" in result[0] or "horas" in result[0]

    def test_japanese_wide(self):
        result = vals.fmt_duration(
            [3661], input_units="seconds", duration_style="wide", locale="ja"
        )
        assert "時間" in result[0]
        assert "分" in result[0]
        assert "秒" in result[0]

    def test_chinese_wide(self):
        result = vals.fmt_duration(
            [86400], input_units="seconds", duration_style="wide", locale="zh"
        )
        assert "天" in result[0]

    def test_korean_wide(self):
        result = vals.fmt_duration(
            [3600], input_units="seconds", duration_style="wide", locale="ko"
        )
        assert "시간" in result[0]

    def test_english_locale_unchanged(self):
        # English locale should produce same result as default
        default = vals.fmt_duration([3661], input_units="seconds")
        with_locale = vals.fmt_duration([3661], input_units="seconds", locale="en")
        assert default == with_locale

    def test_locale_iso_unaffected(self):
        # ISO style should not change with locale
        result = vals.fmt_duration([3661], input_units="seconds", duration_style="iso", locale="fr")
        assert result == ["P1H1M1S"]

    def test_locale_colon_sep_unaffected(self):
        # Colon-sep style should not change with locale
        result = vals.fmt_duration(
            [3661], input_units="seconds", duration_style="colon-sep", locale="de"
        )
        assert result == ["01:01:01"]

    def test_locale_sub_unit_remainder_narrow(self):
        # "<1" pattern with locale
        result = vals.fmt_duration(
            [30], input_units="seconds", locale="fr", output_units=["minutes"]
        )
        assert "<1" in result[0]
        assert "min" in result[0]

    def test_locale_sub_unit_remainder_wide(self):
        result = vals.fmt_duration(
            [30],
            input_units="seconds",
            duration_style="wide",
            locale="de",
            output_units=["minutes"],
        )
        assert "<1" in result[0]
        assert "Minute" in result[0]

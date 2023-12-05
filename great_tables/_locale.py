from __future__ import annotations
from typing import Optional
import pandas as pd
import pkg_resources


class Locale:
    locale: Optional[str]

    def __init__(self, locale: str | None = ""):
        if locale is None or locale == "":
            locale = "en"
        self._locale = locale


def _get_locales_data() -> pd.DataFrame:
    _x_locales_fname = pkg_resources.resource_filename("great_tables.data", "x_locales.csv")
    _x_locales_dtype = {
        "locale": "object",
        "lang_name": "object",
        "lang_desc": "object",
        "script_name": "object",
        "script_desc": "object",
        "territory_name": "object",
        "territory_desc": "object",
        "variant_name": "object",
        "variant_desc": "object",
        "chr_index": "object",
        "decimal": "object",
        "group": "object",
        "percent_sign": "object",
        "plus_sign": "object",
        "minus_sign": "object",
        "approx_sign": "object",
        "exp_sign": "object",
        "sup_exp": "object",
        "per_mille": "object",
        "infinity": "object",
        "nan": "object",
        "approx_pattern": "object",
        "at_least_pattern": "object",
        "at_most_pattern": "object",
        "range_pattern": "object",
        "decimal_format": "object",
        "sci_format": "object",
        "percent_format": "object",
        "currency_format": "object",
        "accounting_format": "object",
        "default_numbering_system": "object",
        "minimum_grouping_digits": "Int64",
        "currency_code": "object",
        "no_table_data_text": "object",
        "sort_label_text": "object",
        "filter_label_text": "object",
        "search_placeholder_text": "object",
        "page_next_text": "object",
        "page_previous_text": "object",
        "page_numbers_text": "object",
        "page_info_text": "object",
        "page_size_options_text": "object",
        "page_next_label_text": "object",
        "page_previous_label_text": "object",
        "page_number_label_text": "object",
        "page_jump_label_text": "object",
        "page_size_options_label_text": "object",
    }
    __x_locales: pd.DataFrame = pd.read_csv(_x_locales_fname, dtype=_x_locales_dtype)
    return __x_locales


def _get_default_locales_data() -> pd.DataFrame:
    _x_default_locales_fname = pkg_resources.resource_filename(
        "great_tables.data", "x_default_locales.csv"
    )
    _x_default_locales_dtype = {
        "default_locale": "object",
        "base_locale": "object",
    }
    __x_default_locales: pd.DataFrame = pd.read_csv(
        _x_default_locales_fname, dtype=_x_default_locales_dtype
    )
    return __x_default_locales


def _get_currencies_data() -> pd.DataFrame:
    _x_currencies_fname = pkg_resources.resource_filename("great_tables.data", "x_currencies.csv")
    _x_currencies_dtype = {
        "curr_code": "object",
        "curr_number": "object",
        "exponent": "object",
        "curr_name": "object",
        "symbol": "object",
    }
    __x_currencies: pd.DataFrame = pd.read_csv(_x_currencies_fname, dtype=_x_currencies_dtype)
    return __x_currencies

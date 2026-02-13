from __future__ import annotations

from csv import DictReader
from typing import Any, TypedDict, cast

from importlib_resources import files

DATA_MOD = files("great_tables") / "data"


def read_csv(fname: str) -> list[dict[str, Any]]:
    with open(fname, encoding="utf8") as f:
        return list(DictReader(f))


class Locale:
    locale: str | None

    def __init__(self, locale: str | None = ""):
        if locale is None or locale == "":
            locale = "en"
        self._locale = locale


class LocalesDict(TypedDict):
    locale: object
    lang_name: object
    lang_desc: object
    script_name: object
    script_desc: object
    territory_name: object
    territory_desc: object
    variant_name: object
    variant_desc: object
    chr_index: object
    decimal: object
    group: object
    percent_sign: object
    plus_sign: object
    minus_sign: object
    approx_sign: object
    exp_sign: object
    sup_exp: object
    per_mille: object
    infinity: object
    nan: object
    approx_pattern: object
    at_least_pattern: object
    at_most_pattern: object
    range_pattern: object
    decimal_format: object
    sci_format: object
    percent_format: object
    currency_format: object
    accounting_format: object
    default_numbering_system: object
    minimum_grouping_digits: int
    currency_code: object
    no_table_data_text: object
    sort_label_text: object
    filter_label_text: object
    search_placeholder_text: object
    page_next_text: object
    page_previous_text: object
    page_numbers_text: object
    page_info_text: object
    page_size_options_text: object
    page_next_label_text: object
    page_previous_label_text: object
    page_number_label_text: object
    page_jump_label_text: object
    page_size_options_label_text: object


class DefaultLocalesDict(TypedDict):
    default_locale: object
    base_locale: object


class CurrenciesDataDict(TypedDict):
    curr_code: object
    curr_number: object
    exponent: object
    curr_name: object
    symbol: object


class FlagsDataDict(TypedDict):
    country_code_2: str
    country_code_3: str
    country_name: str
    country_flag: str


# Note that all the functions below cast the result hint of read_csv
# to a more specific dict type, which contains item info.


def _get_locales_data() -> list[LocalesDict]:
    fname = DATA_MOD / "x_locales.csv"

    return cast("list[LocalesDict]", read_csv(fname))


def _get_default_locales_data() -> list[DefaultLocalesDict]:
    fname = DATA_MOD / "x_default_locales.csv"
    return cast("list[DefaultLocalesDict]", read_csv(fname))


def _get_currencies_data() -> list[CurrenciesDataDict]:
    fname = DATA_MOD / "x_currencies.csv"

    return cast("list[CurrenciesDataDict]", read_csv(fname))


def _get_flags_data() -> list[FlagsDataDict]:
    fname = DATA_MOD / "x_flags.csv"

    return cast("list[FlagsDataDict]", read_csv(fname))

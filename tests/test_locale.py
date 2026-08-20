from great_tables._locale import (
    Locale,
    _get_currencies_data,
    _get_default_locales_data,
    _get_durations_data,
    _get_flags_data,
    _get_locales_data,
)


def test_locale_default():
    loc = Locale()

    assert loc._locale == "en"


def test_locale_none_becomes_en():
    loc = Locale(None)

    assert loc._locale == "en"


def test_locale_empty_string_becomes_en():
    loc = Locale("")

    assert loc._locale == "en"


def test_locale_custom():
    loc = Locale("fr")

    assert loc._locale == "fr"


def test_get_locales_data():
    result = _get_locales_data()

    assert isinstance(result, list)
    assert len(result) > 0
    assert "locale" in result[0]


def test_get_default_locales_data():
    result = _get_default_locales_data()

    assert isinstance(result, list)
    assert len(result) > 0
    assert "default_locale" in result[0]


def test_get_currencies_data():
    result = _get_currencies_data()

    assert isinstance(result, list)
    assert len(result) > 0
    assert "curr_code" in result[0]


def test_get_flags_data():
    result = _get_flags_data()

    assert isinstance(result, list)
    assert len(result) > 0
    assert "country_code_2" in result[0]


def test_get_durations_data():
    result = _get_durations_data()

    assert isinstance(result, list)
    assert len(result) > 0
    assert "locale" in result[0]

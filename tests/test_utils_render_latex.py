from great_tables._utils_render_latex import (
    get_px_conversion,
    get_units_from_length_string,
    convert_to_px,
    convert_to_pt,
)


def test_get_units_from_length_string():

    assert get_units_from_length_string("12.5pt") == "pt"
    assert get_units_from_length_string("") == "px"


def test_get_px_conversion_val():

    assert get_px_conversion(length="2343.23pt") == 4 / 3
    assert get_px_conversion(length="43.2px") == 1.0


def test_convert_to_px():

    assert convert_to_px("12.5pt") == 17.0
    assert convert_to_px("12.5px") == 12.5


def test_convert_to_pt():

    assert convert_to_pt("16px") == 12.0

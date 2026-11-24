import pytest

from great_tables._databackend import MissingClass, _load_class


def test_load_class_missing_attribute_raises_when_strict():
    with pytest.raises(AttributeError):
        _load_class("great_tables", "NotAClass", strict=True)


def test_load_class_missing_attribute_is_missing_class_when_not_strict():
    assert _load_class("great_tables", "NotAClass", strict=False) is MissingClass

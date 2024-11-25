import pytest

from great_tables._utils_selenium import (
    _get_web_driver,
    no_op_callable,
    _ChromeWebDriver,
    _SafariWebDriver,
    _FirefoxWebDriver,
    _EdgeWebDriver,
)


def test_no_op_callable():
    """
    The test should cover the scenario of obtaining a remote driver in `_get_web_driver`.
    """
    fake_input = object()
    f = no_op_callable(fake_input)
    assert f(1, x="x") is fake_input


@pytest.mark.parametrize(
    "web_driver,Driver",
    [
        ("chrome", _ChromeWebDriver),
        ("safari", _SafariWebDriver),
        ("firefox", _FirefoxWebDriver),
        ("edge", _EdgeWebDriver),
    ],
)
def test_get_web_driver(web_driver, Driver):
    assert _get_web_driver(web_driver) is Driver


def test_get_web_driver_raise():
    fake_web_driver = "fake_web_driver"
    with pytest.raises(ValueError) as exc_info:
        _get_web_driver(fake_web_driver)
        assert exc_info.value.args[0] == f"Unsupported web driver: {fake_web_driver}"

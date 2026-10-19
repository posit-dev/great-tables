import os
import sys

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


def _get_driver_arguments(Driver, debug_port):
    # Set up the options without starting a browser
    driver = object.__new__(Driver)
    driver.debug_port = debug_port
    driver.wd_options = driver.cls_wd_options()
    driver.add_arguments()
    return driver.wd_options.arguments


@pytest.mark.parametrize("Driver", [_ChromeWebDriver, _EdgeWebDriver])
@pytest.mark.parametrize(
    "platform,euid,no_sandbox",
    [
        ("linux", 0, True),
        ("linux", 1000, False),
        ("darwin", 0, False),
        ("win32", None, False),
    ],
)
@pytest.mark.parametrize("debug_port", [None, 9222])
def test_chromium_web_driver_arguments(monkeypatch, Driver, platform, euid, no_sandbox, debug_port):
    monkeypatch.setattr(sys, "platform", platform)
    if euid is None:
        # Windows has no `os.geteuid()`
        monkeypatch.delattr(os, "geteuid", raising=False)
    else:
        monkeypatch.setattr(os, "geteuid", lambda: euid, raising=False)

    expected = ["--headless=new"]
    if no_sandbox:
        expected.append("--no-sandbox")
    expected.append("--disable-dev-shm-usage")
    if debug_port is not None:
        expected.append(f"--remote-debugging-port={debug_port}")

    assert _get_driver_arguments(Driver, debug_port) == expected

from __future__ import annotations

import os
import sys
from types import TracebackType
from typing import Literal
from typing_extensions import TypeAlias
from selenium import webdriver

# Create a list of all selenium webdrivers
WebDrivers: TypeAlias = Literal[
    "chrome",
    "firefox",
    "safari",
    "edge",
]


class _BaseWebDriver:  # pragma: no cover
    def __init__(self, debug_port: int | None = None):
        self.debug_port = debug_port
        self.wd_options = self.cls_wd_options()
        self.add_arguments()
        self.driver = self.cls_driver(self.wd_options)

    def add_arguments(self): ...

    def __enter__(self) -> WebDrivers | webdriver.Remote:
        return self.driver

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        self.driver.quit()


def _running_as_root_on_linux() -> bool:
    return sys.platform.startswith("linux") and os.geteuid() == 0


class _ChromiumWebDriver(_BaseWebDriver):  # pragma: no cover
    def add_arguments(self):
        self.wd_options.add_argument("--headless=new")
        # Chromium refuses to start as root (e.g., in Google Colab or a Docker container) unless
        # its sandbox is turned off; elsewhere the sandbox stays on, since the page can load
        # remote content (web fonts, images)
        if _running_as_root_on_linux():
            self.wd_options.add_argument("--no-sandbox")
        # Containers often have a small /dev/shm, which can crash the browser
        self.wd_options.add_argument("--disable-dev-shm-usage")
        if self.debug_port is not None:
            self.wd_options.add_argument(f"--remote-debugging-port={self.debug_port}")


class _ChromeWebDriver(_ChromiumWebDriver):  # pragma: no cover
    cls_driver = webdriver.Chrome
    cls_wd_options = webdriver.ChromeOptions


class _SafariWebDriver(_BaseWebDriver):  # pragma: no cover
    cls_driver = webdriver.Safari
    cls_wd_options = webdriver.SafariOptions


class _FirefoxWebDriver(_BaseWebDriver):  # pragma: no cover
    cls_driver = webdriver.Firefox
    cls_wd_options = webdriver.FirefoxOptions

    def add_arguments(self):
        self.wd_options.add_argument("--headless")
        if self.debug_port is not None:
            self.wd_options.add_argument(f"--start-debugger-server {self.debug_port}")


class _EdgeWebDriver(_ChromiumWebDriver):  # pragma: no cover
    cls_driver = webdriver.Edge
    cls_wd_options = webdriver.EdgeOptions


def no_op_callable(web_driver: webdriver.Remote):  # pragma: no cover
    def wrapper(*args, **kwargs):
        return web_driver

    return wrapper


def _get_web_driver(web_driver: WebDrivers | webdriver.Remote):  # pragma: no cover
    if isinstance(web_driver, webdriver.Remote):
        return no_op_callable(web_driver)
    elif web_driver == "chrome":
        return _ChromeWebDriver
    elif web_driver == "safari":
        return _SafariWebDriver
    elif web_driver == "firefox":
        return _FirefoxWebDriver
    elif web_driver == "edge":
        return _EdgeWebDriver
    else:
        raise ValueError(f"Unsupported web driver: {web_driver}")

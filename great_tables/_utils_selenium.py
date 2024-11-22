from __future__ import annotations

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


class _BaseWebDriver:
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


class _ChromeWebDriver(_BaseWebDriver):
    cls_driver = webdriver.Chrome
    cls_wd_options = webdriver.ChromeOptions

    def add_arguments(self):
        self.wd_options.add_argument("--headless=new")
        if self.debug_port is not None:
            self.wd_options.add_argument(f"--remote-debugging-port={self.debug_port}")


class _SafariWebDriver(_BaseWebDriver):
    cls_driver = webdriver.Safari
    cls_wd_options = webdriver.SafariOptions


class _FirefoxWebDriver(_BaseWebDriver):
    cls_driver = webdriver.Firefox
    cls_wd_options = webdriver.FirefoxOptions

    def add_arguments(self):
        self.wd_options.add_argument("--headless")
        if self.debug_port is not None:
            self.wd_options.add_argument(f"--start-debugger-server {self.debug_port}")


class _EdgeWebDriver(_BaseWebDriver):
    cls_driver = webdriver.Edge
    cls_wd_options = webdriver.EdgeOptions

    def add_arguments(self):
        self.wd_options.add_argument("--headless")


def no_op_callable(web_driver: webdriver.Remote):
    def wrapper(*args, **kwargs):
        return web_driver

    return wrapper


def _get_web_driver(web_driver: WebDrivers | webdriver.Remote):
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

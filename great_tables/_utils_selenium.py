from types import TracebackType
from typing import Literal
from typing_extensions import TypeAlias, Self
from selenium import webdriver

# Create a list of all selenium webdrivers
WebDrivers: TypeAlias = Literal[
    "chrome",
    "firefox",
    "safari",
    "edge",
]


class _NoOpDriverCtx:
    """Context manager that no-ops entering a webdriver(options=...) instance."""

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def __call__(self, options) -> Self:
        # no-op what is otherwise instantiating webdriver with options,
        # since a webdriver instance was already passed on init
        return self

    def __enter__(self) -> webdriver.Remote:
        return self.driver

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        pass


class _BaseWebDriver:

    def __init__(self):
        self.add_arguments()

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
    def __init__(self, debug_port: int | None = None):
        self.debug_port = debug_port
        self.wd_options = webdriver.ChromeOptions()
        super().__init__()
        self.driver = webdriver.Chrome(self.wd_options)

    def add_arguments(self):
        self.wd_options.add_argument("--headless=new")
        if self.debug_port is not None:
            self.wd_options.add_argument(f"--remote-debugging-port={self.debug_port}")


class _SafariWebDriver(_BaseWebDriver):
    def __init__(self, debug_port: int | None = None):
        self.debug_port = debug_port
        self.wd_options = webdriver.SafariOptions()
        super().__init__()
        self.driver = webdriver.Safari(self.wd_options)


class _FirefoxWebDriver(_BaseWebDriver):
    def __init__(self, debug_port: int | None = None):
        self.debug_port = debug_port
        self.wd_options = webdriver.FirefoxOptions()
        super().__init__()
        self.driver = webdriver.Firefox(self.wd_options)

    def add_arguments(self):
        self.wd_options.add_argument("--headless")
        if self.debug_port is not None:
            self.wd_options.add_argument(f"--start-debugger-server {self.debug_port}")


class _EdgeWebDriver(_BaseWebDriver):
    def __init__(self, debug_port: int | None = None):
        self.debug_port = debug_port
        self.wd_options = webdriver.EdgeOptions()
        super().__init__()
        self.driver = webdriver.Edge(self.wd_options)

    def add_arguments(self):
        self.wd_options.add_argument("--headless")


class _NoOpWebDriver(_BaseWebDriver):
    def __init__(self, debug_port: int | None = None):
        self.debug_port = debug_port
        self.wd_options = None
        super().__init__()
        self.driver = _NoOpDriverCtx(self.wd_options)


def _get_web_driver(web_driver: WebDrivers | webdriver.Remote):
    if isinstance(web_driver, webdriver.Remote):
        return _NoOpWebDriver
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

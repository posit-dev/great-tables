from __future__ import annotations

import os
from typing import Literal

IDE_ENV_FLAGS = {
    "default": {"make_page": False, "all_important": False},
    "quarto": {"make_page": False, "all_important": False},
    "databricks": {"make_page": False, "all_important": False},
    "ipython_terminal": {"make_page": False, "all_important": False},
    "vscode": {"make_page": False, "all_important": True},
    "positron": {"make_page": True, "all_important": True},
}


def infer_render_env() -> (
    Literal["quarto", "databricks", "ipython_terminal", "vscode", "positron", "default"]
):
    # Check if we are rendering in the Quarto environment
    if "QUARTO_BIN_PATH" in os.environ:
        return "quarto"
    elif "DATABRICKS_RUNTIME_VERSION" in os.environ:
        return "databricks"
    elif "POSITRON_VERSION" in os.environ:
        return "positron"
    elif "VSCODE_PID" in os.environ:
        return "vscode"
    else:
        try:
            import IPython

            shell = IPython.get_ipython()
            if shell.__class__.__name__ == "TerminalInteractiveShell":
                return "ipython_terminal"
        except ImportError:
            pass

    return "default"


def infer_render_env_defaults():
    env = infer_render_env()
    return IDE_ENV_FLAGS[env]

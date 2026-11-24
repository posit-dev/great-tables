from __future__ import annotations

import json
import os
from contextlib import suppress


def is_quarto_render() -> bool:
    """
    Check if the current environment is a Quarto environment.

    This environment variable check is used to determine if there is currently a Quarto
    render occurring. This is useful for determining if certain rendering options should be
    enabled or disabled for this specific environment.
    """

    return "QUARTO_BIN_PATH" in os.environ


# The base format of the render in progress, as Quarto last sent it to this kernel ("" if that
# message had none). Quarto can keep a kernel running between renders of a document (`quarto
# preview`, or `quarto render` in a terminal), and that kernel's `QUARTO_EXECUTE_INFO` is still
# the first render's, whose file is gone by the next one (or is another format's).
_kernel_format: str | None = None


def _on_kernel_setup(comm, msg) -> None:
    global _kernel_format
    try:
        _kernel_format = msg["content"]["data"]["options"]["format"]["identifier"]["base-format"]
    except (KeyError, TypeError):
        _kernel_format = ""
    if not isinstance(_kernel_format, str):
        _kernel_format = ""
    # (As the kernel does for a comm with no handler)
    comm.close()


def _watch_kernel_setup() -> None:
    """
    Before it runs a document's cells, Quarto opens a `quarto_kernel_setup` comm with the kernel,
    whose message has the render's format: keep it, for each render after this one.
    """

    # (Not in an IPython kernel, there's nothing to watch)
    with suppress(ImportError, AttributeError):
        from IPython import get_ipython

        get_ipython().kernel.comm_manager.register_target("quarto_kernel_setup", _on_kernel_setup)


def quarto_format_is_html() -> bool:
    """
    Check if the Quarto render in progress targets an HTML-based format.

    Takes the format Quarto last sent to the kernel, if it has since `great_tables` was imported
    (from the second render on, in a kernel Quarto keeps running), or else reads it from the file
    named by `QUARTO_EXECUTE_INFO` (which only recent versions of Quarto set). Anything unknown (no
    variable, an unreadable file, or missing keys) doesn't count as HTML.
    """

    if _kernel_format is not None:
        base_format = _kernel_format
    else:
        try:
            with open(os.environ["QUARTO_EXECUTE_INFO"], encoding="utf-8") as f:
                info = json.load(f)
            base_format = info["format"]["identifier"]["base-format"]
        except (OSError, ValueError, KeyError, TypeError):
            return False

    return base_format in ("html", "revealjs", "dashboard")


if is_quarto_render():
    _watch_kernel_setup()

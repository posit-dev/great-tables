import json
import os


def is_quarto_render() -> bool:
    """
    Check if the current environment is a Quarto environment.

    This environment variable check is used to determine if there is currently a Quarto
    render occurring. This is useful for determining if certain rendering options should be
    enabled or disabled for this specific environment.
    """

    return "QUARTO_BIN_PATH" in os.environ


_quarto_pandoc_to: str | None = None


def _get_quarto_pandoc_to() -> str:
    """Read the Pandoc target format from Quarto's execution info JSON file.

    Quarto sets QUARTO_EXECUTE_INFO to a path pointing to a JSON file containing
    format.pandoc.to (e.g., "typst", "html", "latex"). The file is a temp file
    that may be cleaned up during rendering, so we cache the result on first read.
    """
    global _quarto_pandoc_to

    if _quarto_pandoc_to is not None:
        return _quarto_pandoc_to

    result = ""
    info_path = os.environ.get("QUARTO_EXECUTE_INFO", "")
    if info_path and os.path.isfile(info_path):
        try:
            with open(info_path) as f:
                info = json.load(f)
            result = info.get("format", {}).get("pandoc", {}).get("to", "")
        except (json.JSONDecodeError, OSError):
            pass

    _quarto_pandoc_to = result
    return result


# Eagerly read at import time since the temp file may be gone later
if "QUARTO_EXECUTE_INFO" in os.environ:
    _get_quarto_pandoc_to()


def is_quarto_typst_render() -> bool:
    """
    Check if the current Quarto render targets Typst output.

    Reads the QUARTO_EXECUTE_INFO JSON file to determine the Pandoc target format.

    Note: Quarto already translates CSS properties on HTML tables to Typst properties
    automatically. Native Typst output produces cleaner, more idiomatic results.
    """

    if not is_quarto_render():
        return False

    return _get_quarto_pandoc_to() == "typst"

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


def quarto_format_is_html() -> bool:
    """
    Check if the Quarto render in progress targets an HTML-based format.

    Reads the format from the file named by `QUARTO_EXECUTE_INFO` (which only recent versions of
    Quarto set). Anything unknown (no variable, an unreadable file, or missing keys) doesn't count
    as HTML.
    """

    try:
        with open(os.environ["QUARTO_EXECUTE_INFO"], encoding="utf-8") as f:
            info = json.load(f)
        base_format = info["format"]["identifier"]["base-format"]
    except (OSError, ValueError, KeyError, TypeError):
        return False

    return base_format in ("html", "revealjs", "dashboard")

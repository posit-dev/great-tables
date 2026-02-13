import os


def is_quarto_render() -> bool:
    """
    Check if the current environment is a Quarto environment.

    This environment variable check is used to determine if there is currently a Quarto
    render occurring. This is useful for determining if certain rendering options should be
    enabled or disabled for this specific environment.
    """

    return "QUARTO_BIN_PATH" in os.environ

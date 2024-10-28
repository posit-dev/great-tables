import os


def is_quarto_render() -> bool:

    # Check for the presence of the QUARTO_BIN_PATH environment variable
    # to determine if the current environment is a Quarto environment.
    return "QUARTO_BIN_PATH" in os.environ

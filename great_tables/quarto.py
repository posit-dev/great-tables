import os


def check_quarto() -> bool:

    # Check for the presence of the QUARTO_BIN_PATH environment variable
    # to determine if the current environment is a Quarto environment.
    return "QUARTO_BIN_PATH" in os.environ

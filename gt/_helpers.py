from typing import Union, List


def letters() -> List[str]:
    """Lowercase letters of the Roman alphabet

    Returns:
        List[str]: the 26 lowercase letters of the Roman alphabet
    """
    lett = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    return lett


def LETTERS() -> List[str]:
    """Uppercase letters of the Roman alphabet

    Returns:
        List[str]: the 26 uppercase letters of the Roman alphabet
    """
    lett = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    return lett


def px(x: Union[int, float]) -> str:
    return f"{x}px"


def pct(x: Union[int, float]) -> str:
    return f"{x}%"

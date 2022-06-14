from typing import Optional, List


def heading_has_title(title: Optional[str]) -> bool:
    if title is None:
        return False
    else:
        return True


def heading_has_subtitle(subtitle: Optional[str]) -> bool:
    if subtitle is None:
        return False
    else:
        return True


# TODO: generate informative user-facing error message if argument value is not matched
# TODO: require that `lst` contains unique elements
def _match_arg(x: str, lst: List[str]):
    return [el for el in lst if x in el]

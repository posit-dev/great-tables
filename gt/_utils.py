from typing import Optional


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

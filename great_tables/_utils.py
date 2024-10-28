from __future__ import annotations

from collections.abc import Set
import importlib
import itertools
import json
import re
from collections.abc import Generator
from types import ModuleType
from typing import Any, Iterable

from ._tbl_data import PdDataFrame


def _try_import(name: str, pip_install_line: str | None = None) -> ModuleType:
    try:
        return importlib.import_module(name)
    except ImportError:
        if pip_install_line is not None:
            raise ImportError(
                f"Module {name} not found. Run the following to install."
                f"\n\n`{pip_install_line}`"
            ) from None
        else:
            raise ImportError(f"Module {name} not found.")


def heading_has_title(title: str | None) -> bool:
    return title is not None


def heading_has_subtitle(subtitle: str | None) -> bool:
    return subtitle is not None


def _match_arg(x: str, lst: list[str]) -> str:
    # Ensure that `lst` has at least one element
    if len(lst) == 0:
        raise ValueError("The `lst` object must contain at least one element.")

    # Ensure that all elements in `lst` are strings
    if not all(isinstance(el, str) for el in lst):
        raise ValueError("All elements in the `lst` object must be strings.")

    # Ensure that `lst` does not have duplicates by comparing against
    # a set based on `lst` (using `set()` will remove duplicates)
    if len(lst) != len(set(lst)):
        raise ValueError("The `lst` object must contain unique elements.")

    matched = [el for el in lst if x in el]

    # Raise error if there is no match
    if len(matched) == 0:
        raise ValueError(f"The supplied value (`{x}`) is not an allowed option.")

    return matched.pop()


def _assert_str_scalar(x: Any) -> None:
    if not isinstance(x, str):
        raise AssertionError(f"The supplied value (`{x}`) is not a string.")


def _assert_str_list(x: Any) -> None:
    if not isinstance(x, list):
        raise AssertionError(f"The supplied value (`{x}`) is not a list.")
    if not all(map(lambda x: isinstance(x, str), x)):
        raise AssertionError("Not all elements of the supplied list are strings.")


def _assert_str_in_set(x: str, set: list[str]) -> None:
    if x not in set:
        raise AssertionError(f"The string `{x}` is not part of the defined `set`.")


def _assert_list_is_subset(x: list[Any], set_list: list[Any]) -> None:
    if not set(x).issubset(set(set_list)):
        raise AssertionError("The columns provided are not present in the table.")


def _str_scalar_to_list(x: str) -> list[str]:
    _assert_str_scalar(x)
    return [x]


class OrderedSet(Set):
    def __init__(self, d: Iterable = ()):
        self._d = self._create(d)

    def _create(self, d: Iterable):
        return {k: True for k in d}

    def as_set(self):
        return set(self._d)

    def as_list(self):
        return list(self._d)

    def as_dict(self):
        return dict(self._d)

    def __contains__(self, k):
        return k in self._d

    def __iter__(self):
        return iter(self._d)

    def __len__(self):
        return len(self._d)

    def __repr__(self):
        cls_name = type(self).__name__
        lst = self.as_list()
        return f"{cls_name}({lst!r})"


def _as_css_font_family_attr(fonts: list[str], value_only: bool = False) -> str:
    fonts_w_spaces = list(map(lambda x: f"'{x}'" if " " in x else x, fonts))

    fonts_str = ", ".join(fonts_w_spaces)

    if value_only:
        return fonts_str

    return f"font-family: {fonts_str};"


def _object_as_dict(v: Any) -> Any:
    try:
        return v.object_as_dict()
    except Exception:
        pass
    if isinstance(v, PdDataFrame):
        return v.to_dict()
    if isinstance(v, (tuple, list)):
        return list(_object_as_dict(i) for i in v)
    if isinstance(v, dict):
        return dict((k, _object_as_dict(val)) for (k, val) in v.items())
    if type(v) == type(_object_as_dict):  # FIXME figure out how to get "function"
        return f"<function {v.__name__}>"
    try:
        d = vars(v)
    except TypeError:
        try:
            json.dumps(v)
        except TypeError:
            return "JSON_UNSERIALIZABLE"
        return v
    return dict((k, _object_as_dict(v)) for (k, v) in d.items())


def prettify_gt_object(v: Any) -> str:
    return json.dumps(_object_as_dict(v), indent=2)


def _collapse_list_elements(lst: list[Any], separator: str = "") -> str:
    """
    Concatenates all elements of a list into a single string, separated by a given separator.

    Args:
        lst (list): The list to be collapsed.
        separator (str, optional): The separator to be used. Defaults to "".

    Returns:
        str: The collapsed string.
    """
    return separator.join(lst)


def _insert_into_list(lst: list[Any], el: Any) -> list[Any]:
    """
    Inserts an element into the beginning of a list and returns the updated list.

    Args:
        lst (list[Any]): The list to insert the element into.
        el (Any): The element to insert.

    Returns:
        list[Any]: The updated list with the element inserted at the beginning.
    """
    lst.insert(0, el)
    return lst


def _str_replace(string: str, pattern: str, replace: str) -> str:
    return string.replace(pattern, replace)


def _str_detect(string: str, pattern: str) -> bool:
    return bool(re.match(pattern, string))


def pairwise(iterable: Iterable[Any]) -> Generator[tuple[Any, Any], None, None]:
    """
    https://docs.python.org/3/library/itertools.html#itertools.pairwise
    pairwise('ABCDEFG') → AB BC CD DE EF FG
    """
    # This function can be replaced by `itertools.pairwise` if we only plan to support
    # Python 3.10+ in the future.
    iterator = iter(iterable)
    a = next(iterator, None)
    for b in iterator:
        yield a, b
        a = b


def seq_groups(seq: Iterable[str]) -> Generator[tuple[str, int], None, None]:
    iterator = iter(seq)

    # TODO: 0-length sequence
    a = next(iterator)  # will raise StopIteration if `seq` is empty

    try:
        b = next(iterator)
    except StopIteration:
        yield a, 1
        return

    # We can confirm that we have two elements and both are not `None`,
    # so we can chain them back together as the original seq.
    seq = itertools.chain([a, b], iterator)

    crnt_ttl = 1
    for crnt_el, next_el in pairwise(seq):
        if is_equal(crnt_el, next_el):
            crnt_ttl += 1
        else:
            yield crnt_el, crnt_ttl
            crnt_ttl = 1

    # final step has same elements, so we need to yield one last time
    if is_equal(crnt_el, next_el):
        yield crnt_el, crnt_ttl
    else:
        yield next_el, 1


def is_equal(x: Any, y: Any) -> bool:
    return x is not None and x == y

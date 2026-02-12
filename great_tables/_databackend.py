from __future__ import annotations

import sys
import importlib

from abc import ABCMeta
from typing import List, Tuple


class MissingClass:
    """Represent a class that can't be found."""


def _load_class(mod_name: str, cls_name: str, strict: bool):
    try:
        mod = importlib.import_module(mod_name)
        return getattr(mod, cls_name)
    except AttributeError as e:
        if strict:
            raise e
        return MissingClass
    return None


class _AbstractBackendMeta(ABCMeta):
    def register_backend(cls, mod_name: str, cls_name: str):
        cls._backends.append((mod_name, cls_name))
        cls._abc_caches_clear()


class AbstractBackend(metaclass=_AbstractBackendMeta):
    _backends: List[Tuple[str, str]]
    _strict: bool = True

    @classmethod
    def __init_subclass__(cls):
        if not hasattr(cls, "_backends"):
            cls._backends = []

    @classmethod
    def __subclasshook__(cls, subclass):
        for mod_name, cls_name in cls._backends:
            if mod_name not in sys.modules:
                # module isn't loaded, so it can't be the subclass
                # we don't want to import the module to explicitly run the check
                # so skip here.
                continue
            else:
                parent_candidate = _load_class(mod_name, cls_name, cls._strict)
                if issubclass(subclass, parent_candidate):
                    return True

        return NotImplemented

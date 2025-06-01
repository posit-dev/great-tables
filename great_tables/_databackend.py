from __future__ import annotations

import importlib
from abc import ABCMeta
from types import ModuleType


def _load_class(mod_name: str, cls_name: str) -> type:
    # follow the path of mods if it is one
    listified_mod_path: list[str] = cls_name.split(".")

    sub_module_path: list[str] = [mod_name] + listified_mod_path[:-1]

    cur_mod: ModuleType = importlib.import_module(sub_module_path[0])
    _cls_name: str = listified_mod_path[-1]

    if len(sub_module_path) == 1:  # no submodules, just the module itself
        return getattr(cur_mod, _cls_name)

    # now, we must increment the module paths to import the final class
    remaining_mods: list[str] = sub_module_path[1:]
    for mod in remaining_mods:
        cur_mod: ModuleType = getattr(cur_mod, mod)

    return getattr(cur_mod, _cls_name)


class _AbstractBackendMeta(ABCMeta):
    def register_backend(cls, mod_name: str, cls_name: str):
        cls._backends.append((mod_name, cls_name))
        cls._abc_caches_clear()


class AbstractBackend(metaclass=_AbstractBackendMeta):
    @classmethod
    def __init_subclass__(cls):
        if not hasattr(cls, "_backends"):
            cls._backends = []

    @classmethod
    def __subclasshook__(cls, subclass):
        for mod_name, cls_name in cls._backends:
            try:
                parent_candidate = _load_class(mod_name, cls_name)
                if issubclass(subclass, parent_candidate):
                    return True
            except (ModuleNotFoundError, ImportError):
                continue

        return NotImplemented

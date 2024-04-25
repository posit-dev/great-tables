from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from ._gt_data import GTData as GTData

    GTSelf = TypeVar("GTSelf", bound=GTData)

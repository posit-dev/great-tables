from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, ClassVar, Literal, TypedDict, TypeVar, cast

from ._gt_data import GTData, RowGroups

if TYPE_CHECKING:
    from ._types import GTSelf


def row_group_order(self: GTSelf, groups: RowGroups):
    new_stub = self._stub.order_groups(groups)

    return self._replace(_stub=new_stub)

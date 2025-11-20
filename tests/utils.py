from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable

from great_tables._tbl_data import DataFrameLike

if TYPE_CHECKING:
    from typing_extensions import TypeAlias


DataLike: TypeAlias = dict[str, list[Any]]
DataFrameConstructor: TypeAlias = Callable[[DataLike], DataFrameLike]

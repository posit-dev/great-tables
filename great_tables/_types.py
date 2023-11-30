from typing import TypeVar, TYPE_CHECKING


if TYPE_CHECKING:
    from ._gt_data import GTData as GTData

    GTSelf = TypeVar("GTSelf", bound=GTData)

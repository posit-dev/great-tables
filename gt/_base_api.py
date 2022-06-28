from typing import cast

from ._tbl_data import TblData, TblDataAPI


class BaseAPI:
    # It's important that we never keep state in this class, as
    # we will be multiply inheriting from it. I think. --jcheng

    def _get_tbl_data(self) -> TblData:
        result = cast(TblDataAPI, self)._tbl_data
        if result is None:
            raise AssertionError(
                "BaseAPI._data was called before TblDataAPI was initialized"
            )
        return result

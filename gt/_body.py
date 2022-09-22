from typing import List, Optional, Union
import pandas as pd


class Body:
    body: pd.DataFrame
    data: Optional[int]

    def __init__(self, body: pd.DataFrame, data: Optional[int] = None):
        self.body = body
        self.data = data

    def _render_formats(self) -> "Body":
        self = Body(self.body, self.data)
        return self


class BodyAPI:
    _body: Body

    def __init__(self):
        pass

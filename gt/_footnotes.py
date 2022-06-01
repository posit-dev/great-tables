import pandas as pd


class Footnotes:
    def __init__(self):

        # The `footnotes` DataFrame is used to handle footnote text, the precise
        # location where footnote marks should be placed, the placement of the
        # footnote mark around the text, and more
        # 0: `locname` (empty, str)
        # 1: `grpname` (empty, str)
        # 2: `colname` (empty, str)
        # 3: `locnum` (empty, number)
        # 4: `colnum` (empty, int)
        # 5: `footnotes` (empty list, str)
        # 6: `placement` (empty, str)

        self._footnotes: pd.DataFrame = pd.DataFrame(
            columns=[
                "locname",
                "grpname",
                "colname",
                "locnum",
                "colnum",
                "footnotes",
                "placement",
            ]
        )


class FootnotesAPI:
    _footnotes: Footnotes

    def __init__(self):
        self._footnotes = Footnotes()

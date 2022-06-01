import pandas as pd


class Footnotes:
    def __init__(self):

        # The `footnotes` DataFrame is used to store information
        # on table footnotes. The major components include precise
        # location data for where the footnote marks should be
        # placed, the footnote text, and the placement of the
        # footnote mark around the text.
        # 0: `locname` (empty, str)
        # 1: `grpname` (empty, str)
        # 2: `colname` (empty, str)
        # 3: `locnum` (empty, number)
        # 4: `rownum` (empty, int)
        # 5: `colnum` (empty, int)
        # 6: `footnotes` (empty list, str)
        # 7: `placement` (empty, str)

        self._footnotes: pd.DataFrame = pd.DataFrame(
            columns=[
                "locname",
                "grpname",
                "colname",
                "locnum",
                "rownum",
                "colnum",
                "footnotes",
                "placement",
            ]
        )


class FootnotesAPI:
    _footnotes: Footnotes

    def __init__(self):
        self._footnotes = Footnotes()

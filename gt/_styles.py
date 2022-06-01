import pandas as pd


class Styles:
    def __init__(self):

        # The `styles` DataFrame is used to store information
        # on cell styling. The major components include precise
        # location data for where the styling should occur and
        # the styling directives.
        # 0: `locname` (empty, str)
        # 1: `grpname` (empty, str)
        # 2: `colname` (empty, str)
        # 3: `locnum` (empty, number)
        # 4: `rownum` (empty, int)
        # 5: `colnum` (empty, int)
        # 6: `styles` (empty list, str)

        self._styles: pd.DataFrame = pd.DataFrame(
            columns=[
                "locname",
                "grpname",
                "colname",
                "locnum",
                "rownum",
                "colnum",
                "styles",
            ]
        )


class StylesAPI:
    _styles: Styles

    def __init__(self):
        self._styles = Styles()

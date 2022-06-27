import pandas as pd


class Cell:
    value: str

    def __init__(self):
        self.value = ""

    def set_cell_value(self, val: str):
        self.value = val

    def get_cell_value(self):
        self.value


class Table:
    cells: dict[tuple[int, int], Cell]
    columns: dict[str, int]
    n_row: int
    n_col: int

    def __init__(self, df: pd.DataFrame):
        self.cells = {}
        columns = list(df.columns)
        self.columns = dict((v, i) for (i, v) in enumerate(columns))
        self.n_col = len(columns)
        self.n_row = len(df)
        for col in range(self.n_col):
            for row in range(self.n_row):
                self.cells[(row, col)] = Cell()

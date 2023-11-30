import great_tables as gt
import pandas as pd


def test_cols_label_relabel_columns():
    # Create a table with default column labels
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    table = gt.GT(df)

    # Relabel the columns
    modified_table = table.cols_label(A="Column 1", B="Column 2")

    # Check that the column labels have been updated
    assert modified_table._boxhead._get_column_labels() == ["Column 1", "Column 2"]


def test_cols_label_relabel_columns_with_markdown():
    # Create a table with default column labels
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    table = gt.GT(df)

    # Relabel a column with a Markdown formatted label
    modified_table = table.cols_label(A=gt.md("*Column 1*"))

    # Check that the column label has been updated with Markdown formatting
    modified_column_labels = modified_table._boxhead._get_column_labels()

    assert modified_column_labels[0].text == "*Column 1*"
    assert modified_column_labels[1] == "B"


def test_cols_label_return_type():
    # Create a table with default column labels
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    table = gt.GT(df)

    # Call cols_label() with changes
    modified_table = table.cols_label(A="Column 1", B="Column 2")

    # Check that the return type is GT
    assert isinstance(modified_table, gt.GT)

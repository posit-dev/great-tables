import pandas as pd
import pytest
from great_tables import GT, md, exibble
from great_tables._scss import compile_scss


@pytest.fixture
def gt_tbl():
    gt_tbl = (
        GT(
            exibble[["num", "char", "currency", "row", "group"]],
            rowname_col="row",
            groupname_col="group",
            id="test_table",
        )
        .tab_header(
            title=md("Data listing from **exibble**"),
            subtitle=md("`exibble` is a **Great Tables** dataset."),
        )
        .fmt_number(columns="num")
        .fmt_currency(columns="currency")
        .tab_source_note(source_note="This is only a subset of the dataset.")
    )

    return gt_tbl


def test_html_string_generated(gt_tbl: GT, snapshot):
    assert snapshot == gt_tbl.as_raw_html()


def test_save_image_file(gt_tbl: GT, tmp_path):
    gt_tbl.save(filename="test_image.png", path=tmp_path)

    # Wait for the file to be created before checking; wait up to 5 seconds
    for _ in range(5):
        if (tmp_path / "test_image.png").exists():
            break
        else:
            time.sleep(1)

    assert (tmp_path / "test_image.png").exists()

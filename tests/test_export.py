import sys
import time
from pathlib import Path

import pytest
from great_tables import GT, exibble, md


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


def test_html_string_generated(gt_tbl: GT, snapshot: str):
    assert snapshot == gt_tbl.as_raw_html()


@pytest.mark.skipif(sys.platform == "win32", reason="chrome might not be installed.")
@pytest.mark.extra
def test_save_image_file(gt_tbl: GT, tmp_path):

    f_path = tmp_path / "test_image.png"
    gt_tbl.save(file=str(f_path))

    time.sleep(0.1)
    assert f_path.exists()


def test_save_non_png(gt_tbl: GT, tmp_path):
    f_path = tmp_path / "test_image.pdf"
    gt_tbl.save(file=str(f_path))

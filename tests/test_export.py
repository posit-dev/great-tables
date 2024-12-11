import pytest
import requests
import sys
import tempfile
import time

from great_tables import GT, exibble, md
from great_tables.data import gtcars
from great_tables._export import _infer_render_target, _create_temp_file_server
from pathlib import Path

from IPython.terminal.interactiveshell import TerminalInteractiveShell, InteractiveShell
from ipykernel.zmqshell import ZMQInteractiveShell


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


@pytest.fixture
def gt_tbl_small():
    gt_tbl_small = GT(
        exibble[["num", "char"]].head(2),
        id="test_table_small",
    ).fmt_number(columns="num")

    return gt_tbl_small


def test_html_string_generated(gt_tbl: GT, snapshot: str):
    assert snapshot == gt_tbl.as_raw_html()


def test_html_string_generated_inline_css(gt_tbl_small: GT, snapshot: str):
    assert snapshot == gt_tbl_small.as_raw_html(inline_css=True)


def test_html_string_generated_inline_css_make_page(gt_tbl_small: GT, snapshot: str):
    assert snapshot == gt_tbl_small.as_raw_html(inline_css=True, make_page=True)


def test_html_string_generated_all_important(gt_tbl_small: GT):
    assert "!important;" in gt_tbl_small.as_raw_html(inline_css=False, all_important=True)
    assert "!important;" in gt_tbl_small.as_raw_html(inline_css=True, all_important=True)


@pytest.mark.skipif(sys.platform == "win32", reason="chrome might not be installed.")
@pytest.mark.extra
def test_save_image_file(gt_tbl: GT, tmp_path):
    f_path = tmp_path / "test_image.png"
    gt_tbl.save(file=str(f_path))

    time.sleep(0.05)
    assert f_path.exists()


def test_save_non_png(gt_tbl: GT, tmp_path):
    f_path = tmp_path / "test_image.pdf"
    gt_tbl.save(file=str(f_path))


def test_save_custom_webdriver(gt_tbl: GT, tmp_path):
    from selenium import webdriver

    f_path = tmp_path / "test_image.png"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    with webdriver.Chrome(options) as wd:
        gt_tbl.save(file=str(f_path), web_driver=wd)

    time.sleep(0.05)
    assert f_path.exists()


@pytest.mark.parametrize(
    "src, dst",
    [
        (InteractiveShell, "notebook"),
        (TerminalInteractiveShell, "browser"),
        (ZMQInteractiveShell, "notebook"),
        (None, "browser"),
    ],
)
def test_infer_render_target(src, dst):
    shell = src() if src is not None else src
    assert _infer_render_target(shell) == dst


def test_create_temp_file_server():
    from threading import Thread

    with tempfile.TemporaryDirectory() as tmp_dir:
        p_file = Path(tmp_dir, "index.html")
        p_file.write_text("abc")
        server = _create_temp_file_server(p_file)
        thread = Thread(target=server.handle_request)
        thread.start()

        time.sleep(0.3)
        r = requests.get(f"http://127.0.0.1:{server.server_port}/{p_file.name}")
        r.raise_for_status()
        r.content.decode() == "abc"

        thread.join()


def test_snap_as_latex(snapshot):
    gt_tbl = (
        GT(
            gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5),
        )
        .tab_header(title="The _title_", subtitle="The subtitle")
        .tab_spanner(label="Make _and_ Model", columns=["mfr", "model"])
        .tab_spanner(label="Performance", columns=["hp", "trq"])
        .fmt_currency(columns="msrp")
        .tab_source_note("Note 1")
        .tab_source_note("Note 2")
        .tab_options(table_width="600px", table_font_size="12px")
    )

    latex_str_as_latex = gt_tbl.as_latex(use_longtable=True)

    assert snapshot == latex_str_as_latex

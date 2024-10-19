import pytest
import requests
import sys
import tempfile
import time

from great_tables import GT, exibble, md
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


def test_html_string_generated(gt_tbl: GT, snapshot: str):
    assert snapshot == gt_tbl.as_raw_html()


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


@pytest.mark.extra
def test_save_pdf(gt_tbl: GT, tmp_path):
    import pypdf

    # test `expand` parameter
    f_path_e0 = tmp_path / "test_image_expand0.pdf"
    gt_tbl.save_pdf(f_path_e0, expand=0)
    assert f_path_e0.exists

    f_path_e5 = tmp_path / "test_image_expand5.pdf"
    gt_tbl.save_pdf(f_path_e5, expand=5)
    assert f_path_e5.exists

    with pypdf.PdfReader(f_path_e0) as p0, pypdf.PdfReader(f_path_e5) as p5:
        mb0 = p0.pages[0].mediabox
        mb5 = p5.pages[0].mediabox
        assert mb0.left == pytest.approx(mb5.left + 5.0)
        assert mb0.bottom == pytest.approx(mb5.bottom + 5.0)
        assert mb0.width == pytest.approx(mb5.width - 10.0)
        assert mb0.height == pytest.approx(mb5.height - 10.0)

    # test `page_size` parameter
    for i, sz in enumerate([("100cm", "10cm"), "100cm 10cm"]):
        f_path_sz = tmp_path / f"test_image_sz{i}.pdf"
        gt_tbl.save_pdf(f_path_sz, page_size=sz, expand=0)
        assert f_path_sz.exists
        with pypdf.PdfReader(f_path_sz) as p:
            assert len(p.pages) == 2
            for pg in p.pages:
                assert pg.mediabox.height <= 10 / 2.54 * 72  # ≤ 10cm

    # test `scale` parameter
    for sc in 1.5, 0.5:
        f_path_sc = tmp_path / f"test_image_x{int(sc*10):02}.pdf"
        gt_tbl.save_pdf(f_path_sc, expand=0, scale=sc)
        assert f_path_sc.exists

        with pypdf.PdfReader(f_path_sc) as rdr:
            mb = rdr.pages[0].mediabox
            assert mb0.width == pytest.approx(mb.width / sc)
            assert mb0.height == pytest.approx(mb.height / sc)


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

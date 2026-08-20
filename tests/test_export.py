import tempfile
import time
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import requests
from ipykernel.zmqshell import ZMQInteractiveShell
from IPython.terminal.interactiveshell import InteractiveShell, TerminalInteractiveShell

from great_tables import GT, exibble, md
from great_tables._export import _create_temp_file_server, _infer_render_target
from great_tables.data import gtcars


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


def test_write_raw_html_raises(gt_tbl):
    with pytest.raises(TypeError):
        gt_tbl.write_raw_html()  # `filename=` must be specified


def test_write_raw_html(gt_tbl):
    with tempfile.TemporaryDirectory() as tmp_dir:
        # pass the filename as a pathlib.Path() object
        p_file = Path(tmp_dir, "table1.html")
        gt_tbl.write_raw_html(p_file)
        assert p_file.exists()

        # Pass the filename as a string
        s_file = str(Path(tmp_dir, "table2.html"))
        gt_tbl.write_raw_html(s_file)
        assert Path(s_file).exists()


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


def test_as_raw_html_inline_css_without_explicit_id():
    # Test the path where table_id is None (uses random_id())
    gt = GT(exibble[["num", "char"]].head(2))  # no explicit id=
    html = gt.as_raw_html(inline_css=True)
    assert "<table" in html


def test_show_unknown_target_raises(gt_tbl: GT):
    with pytest.raises(Exception, match="Unknown target display"):
        gt_tbl.show(target="unknown")  # type: ignore[arg-type]


def test_show_notebook_target(gt_tbl: GT):
    import sys

    mock_display_html = MagicMock()
    mock_display_module = MagicMock()
    mock_display_module.display_html = mock_display_html
    mock_ipython_core = MagicMock()
    mock_ipython_core.display = mock_display_module
    mock_ipython = MagicMock()
    mock_ipython.core = mock_ipython_core

    with patch.dict(
        sys.modules,
        {
            "IPython": mock_ipython,
            "IPython.core": mock_ipython_core,
            "IPython.core.display": mock_display_module,
        },
    ):
        gt_tbl.show(target="notebook")

    mock_display_html.assert_called_once()


def test_save_unsupported_selector(gt_tbl: GT):
    with pytest.raises(NotImplementedError, match="selector='table'"):
        with pytest.warns(FutureWarning):
            gt_tbl.save("output.png", selector="div")  # type: ignore[arg-type]


def test_pickle():
    import pickle

    import polars as pl
    from polars.testing import assert_frame_equal

    from great_tables.gt import _get_column_labels

    df = pl.DataFrame({"col": [1, 2, 3]})
    gt_tbl = GT(df).cols_label({"col": "new_col"})

    pickled = pickle.dumps(gt_tbl)
    gt_tbl2 = pickle.loads(pickled)

    # ensure the DataFrame remains unchanged after pickling
    assert_frame_equal(gt_tbl2._tbl_data, df)

    # verify that column label is preserved
    assert _get_column_labels(gt=gt_tbl2, context="html")[0] == "new_col"


def test_infer_render_target_no_args():
    result = _infer_render_target()
    assert result in ("browser", "notebook")


def test_infer_render_target_import_error():
    with patch.dict("sys.modules", {"IPython": None}):
        result = _infer_render_target()
    assert result == "browser"


def test_show_browser_target(gt_tbl: GT):
    with (
        patch("webbrowser.open"),
        patch("great_tables._export._create_temp_file_server") as mock_server,
    ):
        mock_srv = MagicMock()
        mock_srv.server_port = 9999
        mock_server.return_value = mock_srv
        gt_tbl.show(target="browser")
        mock_srv.handle_request.assert_called_once()


def test_infer_render_target_auto(gt_tbl: GT):
    with (
        patch("great_tables._export._infer_render_target", return_value="notebook") as mock_infer,
        patch("IPython.core.display.display_html") as mock_display,
    ):
        gt_tbl.show(target="auto")
        mock_infer.assert_called_once()


def test_gtsave_invalid_extension_raises(gt_tbl: GT):
    import sys

    mock_nokap = MagicMock()
    with patch.dict(sys.modules, {"nokap": mock_nokap}):
        with pytest.raises(ValueError, match="Unsupported file extension"):
            gt_tbl.gtsave("my_table.tiff")


def test_write_raw_html_creates_file(gt_tbl: GT, tmp_path):
    from great_tables._export import write_raw_html

    out = tmp_path / "table.html"
    write_raw_html(gt_tbl, str(out))
    assert out.exists()
    assert "<table" in out.read_text()

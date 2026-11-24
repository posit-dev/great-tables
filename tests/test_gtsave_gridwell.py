"""`GT.gtsave()` to the formats gridwell writes (https://github.com/rich-iannone/gridwell).

Skipped when gridwell isn't installed.
"""

import sys
import zipfile
from pathlib import Path
from unittest.mock import patch

import pytest

from great_tables import GT, exibble

gridwell = pytest.importorskip("gridwell")

# The file extension, gridwell's name for the format, and whether it is binary
FORMATS = [
    (".svg", "svg", False),
    (".rtf", "rtf", False),
    (".typ", "typst", False),
    (".docx", "docx", True),
    (".xlsx", "xlsx", True),
    (".pptx", "pptx", True),
]


@pytest.fixture
def gt_tbl():
    return (
        GT(exibble[["num", "char", "currency"]].head(3))
        .tab_header(title="Test Table", subtitle="A subtitle")
        .fmt_number(columns="num")
        .fmt_currency(columns="currency")
    )


def rendered(gt: GT, format: str, binary: bool) -> bytes:
    """What gridwell makes of the table's IR in a format."""
    table = gridwell.Table(gt.as_gridwell())
    return table.render_binary(format) if binary else table.render(format).encode()


@pytest.mark.parametrize("extension, format, binary", FORMATS)
def test_gtsave_writes_what_gridwell_renders(
    gt_tbl: GT, tmp_path: Path, extension: str, format: str, binary: bool
):
    out = tmp_path / f"table{extension}"
    result = gt_tbl.gtsave(out)

    assert result is gt_tbl
    assert out.read_bytes() == rendered(gt_tbl, format, binary)


@pytest.mark.parametrize("extension, format, binary", FORMATS)
def test_gtsave_takes_the_extension_in_any_case(
    gt_tbl: GT, tmp_path: Path, extension: str, format: str, binary: bool
):
    out = tmp_path / f"table{extension.upper()}"
    gt_tbl.gtsave(out)

    assert out.read_bytes() == rendered(gt_tbl, format, binary)


def test_gtsave_takes_a_str_path(gt_tbl: GT, tmp_path: Path):
    gt_tbl.gtsave(str(tmp_path / "table.svg"))

    assert (tmp_path / "table.svg").read_bytes() == rendered(gt_tbl, "svg", False)


def test_gtsave_needs_no_browser_for_gridwell_formats(gt_tbl: GT, tmp_path: Path):
    # Without nokap (the headless browser), the image formats fail but these still save
    with patch.dict(sys.modules, {"nokap": None}):
        for extension, _, _ in FORMATS:
            gt_tbl.gtsave(tmp_path / f"table{extension}")
        with pytest.raises(ImportError):
            gt_tbl.gtsave(tmp_path / "table.png")

    assert sorted(path.suffix for path in tmp_path.iterdir()) == sorted(f[0] for f in FORMATS)


def test_gtsave_ignores_image_options_for_gridwell_formats(gt_tbl: GT, tmp_path: Path):
    gt_tbl.gtsave(tmp_path / "plain.svg")
    gt_tbl.gtsave(tmp_path / "options.svg", zoom=4.0, expand=20, vwidth=1200)

    assert (tmp_path / "plain.svg").read_bytes() == (tmp_path / "options.svg").read_bytes()


def test_svg_is_an_svg_of_the_table(gt_tbl: GT, tmp_path: Path):
    out = tmp_path / "table.svg"
    gt_tbl.gtsave(out)
    svg = out.read_text(encoding="utf-8")

    assert "<svg" in svg and svg.rstrip().endswith("</svg>")
    assert "Test Table" in svg and "A subtitle" in svg


@pytest.mark.parametrize(
    "extension, part",
    [(".docx", "word/document.xml"), (".xlsx", "xl/sharedStrings.xml"), (".pptx", None)],
)
def test_office_files_are_documents_with_the_table(
    gt_tbl: GT, tmp_path: Path, extension: str, part: str | None
):
    out = tmp_path / f"table{extension}"
    gt_tbl.gtsave(out)

    with zipfile.ZipFile(out) as zf:
        assert zf.testzip() is None
        names = zf.namelist()
        parts = [part] if part else [n for n in names if n.startswith("ppt/slides/slide")]
        text = "".join(zf.read(name).decode("utf-8") for name in parts)
    assert "Test Table" in text

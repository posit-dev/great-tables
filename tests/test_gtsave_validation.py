import sys
from pathlib import Path
from unittest.mock import patch

import pytest

from great_tables import GT, exibble


@pytest.fixture
def gt_tbl():
    return (
        GT(exibble[["num", "char", "currency"]].head(3))
        .tab_header(title="Test Table", subtitle="A subtitle")
        .fmt_number(columns="num")
        .fmt_currency(columns="currency")
    )


class TestGtsaveInvalidExtension:
    def test_unsupported_extension_bmp(self, gt_tbl: GT, tmp_path: Path):
        with pytest.raises(ValueError, match="Unsupported file extension: '.bmp'"):
            gt_tbl.gtsave(tmp_path / "table.bmp")

    def test_unsupported_extension_html(self, gt_tbl: GT, tmp_path: Path):
        with pytest.raises(ValueError, match="Unsupported file extension: '.html'"):
            gt_tbl.gtsave(tmp_path / "table.html")

    def test_unsupported_extension_txt(self, gt_tbl: GT, tmp_path: Path):
        with pytest.raises(ValueError, match="Unsupported file extension: '.txt'"):
            gt_tbl.gtsave(tmp_path / "table.txt")

    def test_unsupported_extension_lists_every_format(self, gt_tbl: GT, tmp_path: Path):
        with pytest.raises(ValueError) as info:
            gt_tbl.gtsave(tmp_path / "table.tiff")
        listed = str(info.value).split("Supported formats: ")[1].split(", ")
        assert listed == sorted(
            [".docx", ".jpeg", ".jpg", ".pdf", ".png", ".pptx", ".rtf", ".svg", ".typ"]
            + [".webp", ".xlsx"]
        )

    def test_case_insensitive_valid_extension(self, gt_tbl: GT, tmp_path: Path):
        # Uppercase .PNG should NOT raise ValueError (it's a valid format)
        # It may fail later at the nokap rendering stage without Chrome,
        # but the extension validation itself should pass
        try:
            gt_tbl.gtsave(tmp_path / "table.PNG")
        except ValueError:
            pytest.fail("Uppercase .PNG should be accepted as a valid extension")
        except Exception:
            pass  # Other errors (e.g., Chrome not found) are fine here


@pytest.mark.parametrize("extension", [".svg", ".docx", ".xlsx", ".pptx", ".rtf", ".typ"])
def test_gridwell_formats_without_gridwell_say_what_to_install(
    gt_tbl: GT, tmp_path: Path, extension: str
):
    out = tmp_path / f"table{extension}"
    with (
        patch.dict(sys.modules, {"gridwell": None}),
        pytest.raises(ImportError, match=r'pip install "great_tables\[gridwell\]"'),
    ):
        gt_tbl.gtsave(out)
    assert not out.exists()

from pathlib import Path

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

    def test_unsupported_extension_svg(self, gt_tbl: GT, tmp_path: Path):
        with pytest.raises(ValueError, match="Unsupported file extension: '.svg'"):
            gt_tbl.gtsave(tmp_path / "output.svg")

    def test_unsupported_extension_txt(self, gt_tbl: GT, tmp_path: Path):
        with pytest.raises(ValueError, match="Unsupported file extension: '.txt'"):
            gt_tbl.gtsave(tmp_path / "table.txt")

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

from pathlib import Path

import pytest

from great_tables import GT, exibble


pytestmark = pytest.mark.integration


@pytest.fixture
def gt_tbl():
    return (
        GT(exibble[["num", "char", "currency"]].head(3))
        .tab_header(title="Test Table", subtitle="A subtitle")
        .fmt_number(columns="num")
        .fmt_currency(columns="currency")
    )


class TestGtsavePNG:
    def test_basic_png(self, gt_tbl: GT, tmp_path: Path):
        out = tmp_path / "table.png"
        result = gt_tbl.gtsave(out)

        assert out.exists()
        assert out.stat().st_size > 0
        # Should return self for method chaining
        assert result is gt_tbl

    def test_png_no_extension(self, gt_tbl: GT, tmp_path: Path):
        out = tmp_path / "table"
        gt_tbl.gtsave(out)

        # Should default to .png
        assert (tmp_path / "table.png").exists()

    def test_png_with_zoom(self, gt_tbl: GT, tmp_path: Path):
        out_1x = tmp_path / "table_1x.png"
        out_3x = tmp_path / "table_3x.png"

        gt_tbl.gtsave(out_1x, zoom=1)
        gt_tbl.gtsave(out_3x, zoom=3)

        # Higher zoom should produce a larger file
        assert out_3x.stat().st_size > out_1x.stat().st_size

    def test_png_with_expand(self, gt_tbl: GT, tmp_path: Path):
        out_tight = tmp_path / "tight.png"
        out_padded = tmp_path / "padded.png"

        gt_tbl.gtsave(out_tight, expand=0)
        gt_tbl.gtsave(out_padded, expand=30)

        # More padding should produce a larger file
        assert out_padded.stat().st_size > out_tight.stat().st_size

    def test_png_with_expand_tuple(self, gt_tbl: GT, tmp_path: Path):
        out = tmp_path / "table.png"
        gt_tbl.gtsave(out, expand=(10, 20, 10, 20))

        assert out.exists()
        assert out.stat().st_size > 0


class TestGtsaveJPEG:
    def test_jpeg(self, gt_tbl: GT, tmp_path: Path):
        out = tmp_path / "table.jpg"
        gt_tbl.gtsave(out)

        assert out.exists()
        assert out.stat().st_size > 0

    def test_jpeg_extension(self, gt_tbl: GT, tmp_path: Path):
        out = tmp_path / "table.jpeg"
        gt_tbl.gtsave(out)

        assert out.exists()
        assert out.stat().st_size > 0


class TestGtsaveWebP:
    def test_webp(self, gt_tbl: GT, tmp_path: Path):
        out = tmp_path / "table.webp"
        gt_tbl.gtsave(out)

        assert out.exists()
        assert out.stat().st_size > 0


class TestGtsavePDF:
    def test_basic_pdf(self, gt_tbl: GT, tmp_path: Path):
        out = tmp_path / "table.pdf"
        gt_tbl.gtsave(out)

        assert out.exists()
        assert out.stat().st_size > 0
        # Verify it's actually a PDF
        with open(out, "rb") as f:
            assert f.read(4) == b"%PDF"

    def test_pdf_returns_self(self, gt_tbl: GT, tmp_path: Path):
        out = tmp_path / "table.pdf"
        result = gt_tbl.gtsave(out)
        assert result is gt_tbl


class TestGtsaveMethodChaining:
    def test_chaining(self, tmp_path: Path):
        out = tmp_path / "table.png"
        html = (
            GT(exibble[["num", "char"]].head(2)).fmt_number(columns="num").gtsave(out).as_raw_html()
        )
        assert "<table" in html
        assert out.exists()


class TestGtsaveStringPath:
    def test_string_path(self, gt_tbl: GT, tmp_path: Path):
        out = str(tmp_path / "table.png")
        gt_tbl.gtsave(out)

        assert Path(out).exists()

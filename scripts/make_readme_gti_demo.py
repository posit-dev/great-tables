"""Make the animation of an interactive table, being used, in the README.

    python scripts/make_readme_gti_demo.py               # write assets/readme_gti_demo.webp
    python scripts/make_readme_gti_demo.py --frames DIR  # also keep each frame as a PNG in DIR

A `GTI` table is rendered to a page, and `readme_gti_demo.mjs` (next to this script) uses it as a
reader would, in headless Chromium through Playwright: it sorts a column, filters another, searches
the table, downloads the rows that are left as CSV (shown in a card, since a download isn't seen in
a screenshot), and opens the filters as text, with a cursor drawn where it clicks. It screenshots each
step, and the frames are put together into one animated image with Pillow (a lossless WebP, as for
the README's table showcase). Playwright comes from `packages/gti`, so run `npm ci` there first
(and `npx playwright install chromium`, if it isn't installed).
"""

from __future__ import annotations

import argparse
import json
import subprocess
import tempfile
from pathlib import Path

import polars as pl
from PIL import Image

from great_tables import GTI, data

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "readme_gti_demo.webp"
DRIVER = Path(__file__).resolve().parent / "readme_gti_demo.mjs"

# The page, in CSS pixels; the frames are twice this size.
FRAME_W, FRAME_H = 880, 600


def gtcars_gti() -> GTI:
    cars = data.pl.gtcars.select(
        "mfr", "model", "year", "bdy_style", "ctry_origin", "hp", "mpg_h", "msrp"
    ).with_columns(pl.col("bdy_style").str.to_titlecase())

    return (
        GTI(cars, id="cars")
        .tab_header(title="Grand Touring Cars", subtitle="47 cars from the gtcars dataset")
        .cols_label(
            mfr="Make",
            model="Model",
            year="Year",
            bdy_style="Body",
            ctry_origin="Origin",
            hp="HP",
            mpg_h="MPG",
            msrp="Price",
        )
        .cols_width(
            cases={
                "mfr": "130px",
                "model": "115px",
                "year": "60px",
                "bdy_style": "105px",
                "ctry_origin": "130px",
                "hp": "80px",
                "mpg_h": "75px",
                "msrp": "145px",
            }
        )
        .fmt_integer(columns=["year", "hp", "mpg_h"], use_seps=False)
        .fmt_currency(columns="msrp", decimals=0)
        .data_color(columns="hp", palette=["#FFF5EB", "#FDAE6B"])
        .i_cols_filter()
        .i_cols_profile(columns=["hp", "msrp"])
        .i_export("csv", filename="gtcars")
        .i_pagination(page_size=8)
        .i_display(compact=True)
    )


PAGE = """<!doctype html>
<html><head><meta charset="utf-8"><style>
  html, body {{ margin: 0; background: #ffffff; }}
  body {{
    width: {w}px; height: {h}px; box-sizing: border-box; padding: 14px 20px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial,
      sans-serif;
  }}
  #caption {{ height: 26px; font-size: 17px; font-weight: 600; color: #333; }}
  #caption code {{
    margin-left: 8px; font: 12.5px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    background: #F2F4F7; color: #3A4A64; border-radius: 4px; padding: 2px 6px;
    font-weight: normal;
  }}
  #download {{
    position: fixed; left: 40px; top: 282px; z-index: 900; padding: 10px 14px;
    background: #ffffff; border: 1px solid #D0D5DD; border-radius: 8px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.14);
  }}
  #download .name {{ font-size: 13px; font-weight: 600; color: #333; margin-bottom: 6px; }}
  #download pre {{
    margin: 0; font: 12px/1.5 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    color: #3A4A64;
  }}
  #cursor {{
    position: fixed; left: 0; top: 0; z-index: 1000; pointer-events: none;
    filter: drop-shadow(0 1px 1.5px rgba(0, 0, 0, 0.35));
  }}
</style></head><body>
<div id="caption"></div>
{table}
<svg id="cursor" width="20" height="24" viewBox="0 0 20 24">
  <path d="M2 2 L2 19 L6.5 15 L9.5 22 L12.5 20.7 L9.6 14 L15.5 14 Z"
    fill="#111" stroke="#fff" stroke-width="1.5" stroke-linejoin="round"/>
</svg>
</body></html>
"""


def page_html(table: GTI) -> str:
    return PAGE.format(w=FRAME_W, h=FRAME_H, table=table.as_raw_html())


def record(page: Path, out_dir: Path) -> list[tuple[Path, int]]:
    """Run the driver, returning each frame and how long it's shown (in milliseconds)."""
    subprocess.run(
        ["node", str(DRIVER), str(page), str(out_dir), str(FRAME_W), str(FRAME_H)], check=True
    )
    frames = json.loads((out_dir / "frames.json").read_text())
    return [(out_dir / f["file"], f["ms"]) for f in frames]


def assemble(frames: list[tuple[Path, int]], out: Path) -> None:
    images = [Image.open(p).convert("RGB") for p, _ in frames]
    images[0].save(
        out,
        save_all=True,
        append_images=images[1:],
        duration=[ms for _, ms in frames],
        loop=0,
        lossless=True,
        quality=100,
        method=6,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--frames", type=Path, help="a directory to keep the frames in, as PNGs")
    args = parser.parse_args()

    with tempfile.TemporaryDirectory() as tmp:
        frames_dir = args.frames or Path(tmp)
        frames_dir.mkdir(parents=True, exist_ok=True)
        page = Path(tmp) / "gti_demo.html"
        page.write_text(page_html(gtcars_gti()))
        frames = record(page, frames_dir)
        assemble(frames, OUT)

    total = sum(ms for _, ms in frames) / 1000
    print(
        f"Wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size / 1024:.0f} kB, "
        f"{len(frames)} frames, {total:.1f} s)"
    )


if __name__ == "__main__":
    main()

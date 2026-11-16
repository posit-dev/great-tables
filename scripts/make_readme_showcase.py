"""Make the animated table showcase at the top of the README.

    python scripts/make_readme_showcase.py               # write assets/readme_showcase.webp
    python scripts/make_readme_showcase.py --frames DIR  # also keep each frame as a PNG in DIR

Each table is built from the Polars versions of the package's datasets, set in a fixed-size
frame with a caption naming the features it shows, and rendered with headless Chrome (through
`nokap`, the same renderer that `GT.gtsave()` uses). The frames are then put together into one
animated image with Pillow: a lossless WebP, which keeps the text sharp and is a third the size
of an APNG of the same frames. Chrome or Chromium must be installed.
"""

from __future__ import annotations

import argparse
import html as html_lib
import tempfile
from dataclasses import dataclass
from pathlib import Path

import nokap
import polars as pl
from PIL import Image

from great_tables import GT, GTI, data, html, loc, md, nanoplot_options, style, vals

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "readme_showcase.webp"
METRO_IMAGES = ROOT / "great_tables" / "data" / "metro_images"

# The frame, in CSS pixels; it's rendered at `ZOOM` times this size.
FRAME_W, FRAME_H = 880, 540
ZOOM = 2

# How long each table is shown, in milliseconds.
HOLD_MS = 3500


@dataclass
class Slide:
    title: str
    methods: list[str]
    table: GT


# --- the tables -------------------------------------------------------------------------------


def gtcars_table() -> GT:
    cars = (
        data.pl.gtcars.filter(pl.col("ctry_origin").is_in(["Germany", "Italy", "United Kingdom"]))
        .sort("hp", descending=True)
        .group_by("ctry_origin", maintain_order=True)
        .head(3)
        .select("ctry_origin", "mfr", "model", "hp", "trq", "mpg_c", "mpg_h", "msrp")
    )

    return (
        GT(cars, rowname_col="model", groupname_col="ctry_origin")
        .tab_header(
            title=md("**The Fastest Cars** in `gtcars`"),
            subtitle="The three most powerful cars from each of Germany, Italy, and the UK",
        )
        .tab_stubhead(label="Car")
        .cols_merge(columns=["model", "mfr"], pattern="{1} {0}")
        .tab_spanner(label="Performance", columns=["hp", "trq"])
        .tab_spanner(label="Fuel Economy", columns=["mpg_c", "mpg_h"])
        .cols_label(
            mfr="Make",
            hp="Power ({{hp}})",
            trq="Torque ({{lb ft}})",
            mpg_c="City",
            mpg_h="Highway",
            msrp="Price",
        )
        .fmt_integer(columns=["hp", "trq", "mpg_c", "mpg_h"])
        .fmt_currency(columns="msrp", decimals=0)
        .tab_footnote(
            footnote="Miles per gallon (US).",
            locations=loc.spanner_labels(ids=["Fuel Economy"]),
        )
        .tab_source_note(source_note="Source: the gtcars dataset in Great Tables.")
        .tab_style(style=style.text(weight="bold"), locations=loc.row_groups())
        .opt_vertical_padding(scale=0.6)
    )


def sp500_table() -> GT:
    months = (
        data.pl.sp500.with_columns(pl.col("date").str.to_date())
        .filter(pl.col("date").dt.year() == 2015)
        .sort("date")
        .group_by(pl.col("date").dt.truncate("1mo").alias("month"), maintain_order=True)
        .agg(
            pl.col("open").first(),
            pl.col("close").last(),
            pl.col("close").alias("trend"),
            (pl.col("volume") / 1e9).alias("volume"),
        )
        .with_columns(change=(pl.col("close") / pl.col("open") - 1))
        .head(8)
    )

    return (
        GT(months, rowname_col="month")
        .tab_header(
            title="S&P 500 in 2015",
            subtitle="Daily closing values and trading volume, month by month",
        )
        .fmt_date(columns="month", date_style="month")
        .fmt_currency(columns=["open", "close"])
        .fmt_percent(columns="change", decimals=1, force_sign=True)
        .fmt_nanoplot(
            columns="trend",
            plot_type="line",
            options=nanoplot_options(
                data_line_stroke_color="#2C5282",
                data_area_fill_color="#BEE3F8",
                show_data_points=False,
            ),
        )
        .fmt_nanoplot(
            columns="volume",
            plot_type="bar",
            options=nanoplot_options(data_bar_fill_color="#5F7FBF"),
        )
        .data_color(
            columns="change", palette=["#D7301F", "#FFFFFF", "#1A9850"], domain=[-0.07, 0.07]
        )
        .cols_label(
            open="Open",
            close="Close",
            change="Change",
            trend="Daily Close",
            volume="Volume ({{billions}})",
        )
        .cols_align(align="center", columns=["trend", "volume"])
    )


def countrypops_table() -> GT:
    pops = data.pl.countrypops.filter(pl.col("year") >= 1972)
    largest = (
        pops.filter(pl.col("year") == pops["year"].max())
        .sort("population", descending=True)
        .head(8)["country_code_3"]
    )
    countries = (
        pops.filter(pl.col("country_code_3").is_in(largest.implode()))
        .sort("year")
        .group_by("country_code_2", "country_name", maintain_order=True)
        .agg(
            pl.col("population").first().alias("pop_start"),
            pl.col("population").last().alias("pop_end"),
            pl.col("population").alias("trend"),
        )
        .with_columns(growth=pl.col("pop_end") / pl.col("pop_start") - 1)
        .sort("pop_end", descending=True)
    )
    start, end = pops["year"].min(), pops["year"].max()

    return (
        GT(countries)
        .tab_header(
            title="The World's Most Populous Countries",
            subtitle=f"Population in {start} and {end}, with the trend between",
        )
        .fmt_flag(columns="country_code_2")
        .fmt_number(columns=["pop_start", "pop_end"], compact=True, decimals=1)
        .fmt_percent(columns="growth", decimals=0)
        .fmt_nanoplot(
            columns="trend",
            plot_type="line",
            options=nanoplot_options(
                data_area_fill_color="#E9C46A",
                data_line_stroke_color="#264653",
                show_data_points=False,
            ),
        )
        .data_color(columns="growth", palette="YlGn")
        .cols_label(
            country_code_2="",
            country_name="Country",
            pop_start=str(start),
            pop_end=str(end),
            trend="Trend",
            growth="Growth",
        )
        .cols_move_to_start(columns="country_code_2")
        .tab_source_note(source_note="Source: the World Bank, via the countrypops dataset.")
        .opt_stylize(style=1, color="green", add_row_striping=False)
        .opt_vertical_padding(scale=0.7)
    )


def sza_table() -> GT:
    sza = (
        data.pl.sza.filter((pl.col("latitude") == "20") & (pl.col("tst") <= "1200"))
        .drop("latitude")
        .filter(pl.col("sza").is_not_null())
        .pivot(on="tst", index="month", values="sza", sort_columns=True)
    )
    times = [c for c in sza.columns if c != "month"]

    return (
        GT(sza, rowname_col="month")
        .tab_header(
            title="Solar Zenith Angles at 20°N",
            subtitle="By month and by true solar time, from sunrise to noon",
        )
        .sub_missing(missing_text="")
        .fmt_number(columns=times, decimals=0)
        .data_color(
            columns=times,
            palette=["#B2182B", "#FDDBC7", "#FFFFFF"],
            domain=[0, 90],
            na_color="#FFFFFF",
        )
        .cols_label(cases={t: f"{t[:2]}:{t[2:]}" for t in times})
        .text_transform(locations=loc.stub(), fn=str.title)
        .cols_label_rotate(columns=times)
        .tab_options(table_font_size="13px")
        .opt_vertical_padding(scale=0.5)
        .opt_horizontal_padding(scale=0.6)
    )


def pizzaplace_table() -> GT:
    names = {
        "thai_ckn": "Thai Chicken",
        "bbq_ckn": "Barbecue Chicken",
        "classic_dlx": "Classic Deluxe",
        "hawaiian": "Hawaiian",
        "spicy_ital": "Spicy Italian",
        "ital_supr": "Italian Supreme",
        "four_cheese": "Four Cheese",
        "mexicana": "Mexicana",
    }
    quarters = ["Q1", "Q2", "Q3", "Q4"]
    pizzas = (
        data.pl.pizzaplace.filter(pl.col("name").is_in(list(names)))
        .with_columns(quarter=pl.format("Q{}", pl.col("date").str.to_date().dt.quarter()))
        .pivot(on="quarter", index=["type", "name"], values="id", aggregate_function="len")
        .with_columns(total=pl.sum_horizontal(quarters))
        .sort("type", "total", descending=[False, True])
        .with_columns(pl.col("type").str.to_titlecase(), pl.col("name").replace_strict(names))
    )

    return (
        GT(pizzas, rowname_col="name", groupname_col="type")
        .tab_header(
            title=md("**Best-Selling Pizzas** of 2015"),
            subtitle="The top two pizzas of each type, with subtotals and a grand total",
        )
        .summary_rows(fns={"Subtotal": pl.col(*quarters, "total").sum()}, fmt=vals.fmt_integer)
        .grand_summary_rows(fns={"Total": pl.col(*quarters, "total").sum()}, fmt=vals.fmt_integer)
        .fmt_integer(columns=[*quarters, "total"])
        .tab_spanner(label="Pizzas Sold", columns=quarters)
        .cols_label(total="Year")
        .tab_style(style=style.text(weight="bold"), locations=loc.body(columns="total"))
        .opt_stylize(style=6, color="red", add_row_striping=False)
        .opt_vertical_padding(scale=0.5)
    )


def reactions_table() -> GT:
    gases = (
        data.pl.reactions.filter(
            pl.col("cmpd_name").is_in(
                [
                    "ethene",
                    "propene",
                    "1-butene",
                    "(E)-2-butene",
                    "isoprene",
                    "furan",
                    "(E)-2-butenal",
                ]
            )
        )
        .select("cmpd_name", "cmpd_formula", "OH_k298", "O3_k298", "NO3_k298", "Cl_k298")
        .sort("OH_k298")
    )
    rates = ["OH_k298", "O3_k298", "NO3_k298", "Cl_k298"]

    return (
        GT(gases, rowname_col="cmpd_name")
        .tab_header(
            title="Gas-Phase Reaction Rates of Unsaturated Compounds",
            subtitle=html(
                "Rate constants at 298 K, in cm<sup>3</sup> molecules<sup>&minus;1</sup> s<sup>&minus;1</sup>"
            ),
        )
        .fmt_chem(columns="cmpd_formula")
        .fmt_scientific(columns=rates, decimals=2)
        .sub_missing(missing_text="—")
        .tab_spanner(label="Reaction with", columns=rates)
        .cols_label(
            cmpd_formula="Formula",
            OH_k298="OH",
            O3_k298=html("O<sub>3</sub>"),
            NO3_k298=html("NO<sub>3</sub>"),
            Cl_k298="Cl",
        )
        .tab_source_note(source_note="Source: the reactions dataset.")
        .opt_stylize(style=3, color="cyan")
    )


def metro_table() -> GT:
    stations = (
        data.pl.metro.sort("passengers", descending=True, nulls_last=True)
        .head(7)
        .select("name", "lines", "connect_rer", "location", "passengers")
    )

    return (
        GT(stations, rowname_col="name")
        .tab_header(
            title="The Busiest Stations of the Paris Métro",
            subtitle="With the lines and RER connections at each station",
        )
        .fmt_image(columns="lines", path=METRO_IMAGES, file_pattern="metro_{}.svg", height="20px")
        .cols_align(align="center", columns="lines")
        .fmt_integer(columns="passengers")
        .sub_missing(missing_text="")
        .cols_label(
            lines="Lines",
            connect_rer="RER",
            location="Location",
            passengers="Passengers (2021)",
        )
        .tab_style(
            style=style.text(color="#666", size="small"), locations=loc.body(columns="location")
        )
        .opt_stylize(style=2, color="blue", add_row_striping=False)
        .opt_vertical_padding(scale=0.6)
    )


def towny_gti() -> GTI:
    towns = data.pl.towny.select(
        "name", "status", "population_2021", "density_2021", "pop_change_2016_2021_pct"
    )

    return (
        GTI(towns, rowname_col="name")
        .tab_header(
            title="Ontario's Municipalities",
            subtitle="Sort, search, filter, and page through all 414 of them",
        )
        .fmt_integer(columns="population_2021")
        .fmt_number(columns="density_2021", decimals=1)
        .fmt_percent(columns="pop_change_2016_2021_pct", decimals=1, force_sign=True)
        .data_color(
            columns="pop_change_2016_2021_pct",
            palette=["#D7301F", "#FFFFFF", "#1A9850"],
            domain=[-0.2, 0.2],
        )
        .cols_label(
            status="Status",
            population_2021="Population",
            density_2021="Density",
            pop_change_2016_2021_pct="Change",
        )
        .cols_width(
            cases={
                "name": "170px",
                "status": "110px",
                "population_2021": "130px",
                "density_2021": "130px",
                "pop_change_2016_2021_pct": "200px",
            }
        )
        .i_cols_filter()
        .i_cols_profile(columns=["population_2021", "density_2021", "pop_change_2016_2021_pct"])
        .i_view(filter='status in ("single-tier")', sort="-population_2021")
        .i_pagination(page_size=8)
        .i_display(compact=True)
    )


SLIDES = [
    Slide(
        "Flags, nanoplots, and themes",
        ["fmt_flag()", "fmt_nanoplot()", "opt_stylize()"],
        countrypops_table(),
    ),
    Slide("Nanoplots", ["fmt_nanoplot()", "data_color()"], sp500_table()),
    Slide("Structure", ["tab_header()", "tab_spanner()", "tab_footnote()"], gtcars_table()),
    Slide("Heatmaps", ["data_color()", "cols_label_rotate()"], sza_table()),
    Slide("Images in cells", ["fmt_image()"], metro_table()),
    Slide("Science", ["fmt_chem()", "fmt_scientific()"], reactions_table()),
    Slide("Summary rows", ["summary_rows()", "grand_summary_rows()"], pizzaplace_table()),
    Slide(
        "Interactive tables",
        ["GTI()", "i_cols_filter()", "i_cols_profile()", "i_view()"],
        towny_gti(),
    ),
]


# --- rendering ----------------------------------------------------------------------------------

PAGE = """<!doctype html>
<html><head><meta charset="utf-8"><style>
  html, body {{ margin: 0; background: #ffffff; }}
  #frame {{
    width: {w}px; height: {h}px; box-sizing: border-box; padding: 14px 20px 18px;
    display: flex; flex-direction: column; background: #ffffff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial,
      sans-serif;
  }}
  #caption {{ display: flex; align-items: baseline; gap: 10px; color: #333; }}
  #caption .title {{ font-size: 17px; font-weight: 600; }}
  #caption code {{
    font: 12.5px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    background: #F2F4F7; color: #3A4A64; border-radius: 4px; padding: 2px 6px;
  }}
  #stage {{ flex: 1; display: flex; align-items: center; justify-content: center;
    overflow: hidden; min-height: 0; }}
</style></head><body>
<div id="frame">
  <div id="caption"><span class="title">{title}</span>{methods}</div>
  <div id="stage"><div id="fit">{table}</div></div>
</div>
<script>
  // Shrink the table to fit the stage, if it has to. (An interactive table is made to fit instead:
  // it sizes its columns from their measured widths, which a zoom throws off.)
  const stage = document.getElementById("stage");
  const fit = document.getElementById("fit");
  if (!fit.querySelector("gt-table")) {{
    fit.style.zoom = Math.min(
      1, stage.clientWidth / fit.scrollWidth, stage.clientHeight / fit.scrollHeight
    );
  }}
</script>
</body></html>
"""


def page_html(slide: Slide) -> str:
    methods = "".join(f"<code>{html_lib.escape(m)}</code>" for m in slide.methods)
    return PAGE.format(
        w=FRAME_W,
        h=FRAME_H,
        title=html_lib.escape(slide.title),
        methods=methods,
        table=slide.table.as_raw_html(),
    )


def render_frames(slides: list[Slide], out_dir: Path) -> list[Path]:
    paths = []
    for i, slide in enumerate(slides, start=1):
        path = out_dir / f"frame_{i:02d}.png"
        nokap.from_html(
            html=page_html(slide),
            file=path,
            selector="#frame",
            expand=0,
            zoom=ZOOM,
            delay=1.5,
            vwidth=FRAME_W + 40,
            vheight=FRAME_H + 40,
        )
        paths.append(path)
    return paths


def assemble(frames: list[Path], out: Path) -> None:
    images = [Image.open(p).convert("RGB") for p in frames]
    size = images[0].size
    images = [im if im.size == size else im.resize(size) for im in images]
    images[0].save(
        out,
        save_all=True,
        append_images=images[1:],
        duration=HOLD_MS,
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
        frames = render_frames(SLIDES, frames_dir)
        assemble(frames, OUT)

    print(f"Wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size / 1024:.0f} kB)")


if __name__ == "__main__":
    main()

"""Write the table fragments the theme tests (theme.spec.ts) render (into e2e/.fixtures/theme/).

Each table is written as `<table>.<variant>.html`. The variants are the table as `as_raw_html()`
gives it (`auto`), with its mode fixed (`light`, `dark`), and as literal CSS, without variables
(`light-literal`, `dark-literal`), which the variable CSS must render the same as. Run by
e2e/global-setup.ts; needs great_tables importable (e.g. `pip install -e .` at the repo root).
"""

from __future__ import annotations

from pathlib import Path

from great_tables import GT, Theme, exibble, loc, style

OUT = Path(__file__).parent / ".fixtures" / "theme"


def base(name: str) -> GT:
    return (
        GT(exibble, rowname_col="row", groupname_col="group", id=f"t-{name}")
        .tab_header(title="exibble", subtitle="A small table")
        .tab_spanner(label="Numbers", columns=["num", "currency"])
        .fmt_number(columns="num", decimals=2)
        .fmt_currency(columns="currency")
        .tab_source_note("Source: great_tables.exibble")
        .opt_row_striping()
    )


def cells() -> GT:
    """A table with colors written on its cells, which are literal and were chosen for a light table."""
    by_row = [
        style.fill(color="lightcyan"),
        style.fill(color="navy"),
        style.text(color="navy"),
        style.text(color="black"),
        style.text(color="#CC0000"),
    ]
    gt = base("cells")
    for i, cell_style in enumerate(by_row):
        gt = gt.tab_style(style=cell_style, locations=loc.body(columns="char", rows=[i]))
    # (A black border, as `style.borders()` draws by default: blended in dark)
    gt = gt.tab_style(
        style=style.borders(sides="bottom", weight="2px"),
        locations=loc.body(columns="char", rows=[5]),
    )
    # (A light palette: the default one has mid-gray fills, where its own text choice is under 4.5:1)
    gt = gt.data_color(
        columns="currency", palette=["lightyellow", "lightgreen"], na_color="lightgray"
    )
    # (Fills with no contrast text: the inherited text in light, the dark text on them in dark)
    return gt.data_color(
        columns="num", palette=["white", "lightyellow"], na_color="white", autocolor_text=False
    )


def tables() -> dict[str, GT]:
    return {
        "plain": base("plain"),
        "stylized": base("stylized").opt_stylize(style=6, color="blue"),
        "themed": base("themed").opt_theme(
            Theme(
                border="#CC3333",
                data_row_padding="2px",
                dark=Theme(background="#101418", table_body_hlines_color="#3A4A5A"),
            )
        ),
        "padded": base("padded").tab_options(data_row_padding="6px"),
        # (A dark background with no foreground: the text is chosen for contrast with it)
        "navy": base("navy").opt_theme(Theme(background="#0B1E33")),
        "cells": cells(),
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, gt in tables().items():
        variants = {"auto": gt.as_raw_html()}
        for mode in ("light", "dark"):
            themed = gt.opt_theme(mode=mode)
            variants[mode] = themed.as_raw_html()
            variants[f"{mode}-literal"] = themed._build_data("html")._render_as_html(
                variables=False
            )
        for variant, html in variants.items():
            (OUT / f"{name}.{variant}.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()

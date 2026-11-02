"""The Zen of Great Tables.

Like `import this` prints the Zen of Python, `import great_tables.this` prints the Zen of Great
Tables, or shows it as a great table in a notebook.
"""

from __future__ import annotations

import codecs
import contextlib
import difflib
import io
import re

from . import loc, style
from ._export import _infer_render_target
from ._helpers import md, nanoplot_options
from ._tbl_data import DataFrameLike, frame_from_dict
from .gt import GT

# `import this` prints the Zen of Python on first import, so capture it.
with contextlib.redirect_stdout(io.StringIO()):
    import this as _this

_PEP20 = codecs.decode(_this.s, "rot13").splitlines()[2:]

# Each aphorism, paired with the method that embodies it.
_APHORISMS = [
    ("Beautiful is better than printed at the console.", "opt_stylize()"),
    ("A data table is input. A display table is output.", "gtsave()"),
    ("Simple is better than complex.", "cols_hide()"),
    ("Complex is better than copying it into Excel.", "tab_style()"),
    ("Flat is better than nested, unless it's under a spanner.", "tab_spanner()"),
    ("Sparse is better than dense, but a nanoplot can be both.", "fmt_nanoplot()"),
    ("Readability counts, in every locale from `af` to `zu`.", "fmt_number()"),
    ("Special cases aren't special enough to break the six components.", "tab_stub()"),
    ("Although `opt_css()` beats purity, provided you have those CSS skillz.", "opt_css()"),
    ("Missing values should never pass silently.", "data_color()"),
    ("Unless explicitly `sub_missing()`.", "sub_missing()"),
    ("In the face of ambiguity, label your columns.", "cols_label()"),
    ("There should be one (and preferably only one) obvious way to make a table.", "GT()"),
    ("Although that way may not be obvious at first unless you're Rich.", "md()"),
    ("Now is better than never.", "fmt_datetime()"),
    ("Although the 1949 Census Manual is often better than *right* now.", "fmt_roman()"),
    ("If the table is hard to explain, add a footnote.", "tab_footnote()"),
    ("If the table is easy to explain, it may be a great table.", "tab_header()"),
    (
        "Bringing your own DataFrame is one honking great idea: let's do more of those!",
        "GT(your_df)",
    ),
]

text = "The Zen of Great Tables, by the Great Tables crew\n\n" + "\n".join(
    aphorism for aphorism, _ in _APHORISMS
)


def _faithfulness(new: str, old: str) -> float:
    plain = new.replace("`", "").replace("*", "")
    return difflib.SequenceMatcher(None, plain.lower(), old.lower()).ratio()


_FAITHFULNESS = [_faithfulness(a, o) for (a, _), o in zip(_APHORISMS, _PEP20, strict=True)]

# PEP 20 has 20 aphorisms, "only 19 of which have been written down": row XX stays empty.
_COLUMNS = {
    "n": list(range(1, 21)),
    "aphorism": [a for a, _ in _APHORISMS] + [None],
    "original": _PEP20 + [None],
    "method": [m for _, m in _APHORISMS] + [None],
    # One column draws the bar, the other prints the value
    "faithful": _FAITHFULNESS + [None],
    "faithful_pct": _FAITHFULNESS + [None],
}

_FAMILY_COLORS = {
    "tab": "#22384F",
    "fmt": "#2F4A38",
    "cols": "#9A7B33",
    "opt": "#5C2E2E",
    "sub": "#8A7452",
    "core": "#4A3A2C",
}


def _chip(method: object) -> str:
    # Missing values arrive as None, NaN or pd.NA depending on the DataFrame library
    if not isinstance(method, str):
        return ""

    family = re.match(r"(tab|fmt|cols|opt|sub)_", method)
    color = _FAMILY_COLORS[family.group(1) if family else "core"]
    return (
        f'<span style="background:{color};color:white;border-radius:999px;padding:3px 10px;'
        f'font-family:ui-monospace,Menlo,Consolas,monospace;font-size:0.85em">{method}</span>'
    )


def _zen_table(data: DataFrameLike) -> GT:
    return (
        GT(data, rowname_col="n")
        .tab_header(
            title="The Zen of Great Tables",
            subtitle=md("by the Great Tables crew, after Tim Peters's `import this`"),
        )
        .tab_spanner(label="Faithful to PEP 20", columns=["faithful", "faithful_pct"])
        .cols_label(aphorism="Aphorism", method="Embodied by", faithful="", faithful_pct="")
        # formatting ----
        .fmt_roman(columns="n")
        .fmt_markdown(columns="aphorism")
        .fmt(_chip, columns="method")
        .fmt_nanoplot(
            columns="faithful",
            plot_type="bar",
            options=nanoplot_options(
                data_bar_fill_color="#08306B", data_bar_stroke_color="#08306B"
            ),
        )
        .fmt_percent(columns="faithful_pct", decimals=0)
        .sub_missing(columns="aphorism", missing_text="Left for Rich Iannone to write.")
        .sub_missing(columns=["original", "method", "faithful", "faithful_pct"], missing_text="")
        .cols_merge(
            columns=["aphorism", "original"],
            pattern="{0}<br><span style='color:#808080;font-size:0.8em;font-style:italic'>{1}</span>",
        )
        # style ----
        .tab_style(
            style=style.text(color="white", weight="bold"),
            locations=[loc.column_labels(), loc.spanner_labels(ids=["Faithful to PEP 20"])],
        )
        .tab_style(style=style.text(weight="bold"), locations=loc.stub())
        .tab_style(
            style=style.text(style="italic", color="#808080"),
            locations=loc.body(columns="aphorism", rows=[19]),  # XX
        )
        .cols_align(align="center", columns="method")
        .cols_width(
            cases={
                "n": "60px",
                "aphorism": "560px",
                "method": "150px",
                "faithful": "150px",
                "faithful_pct": "60px",
            }
        )
        .opt_row_striping()
        .tab_options(
            column_labels_background_color="#08306B",
            stub_background_color="#EAF0F6",
            row_striping_background_color="#F6F6F6",
            table_body_hlines_color="#E8E8E8",
            table_border_top_color="#CCCCCC",
            table_border_bottom_color="#CCCCCC",
            table_border_left_style="solid",
            table_border_left_color="#CCCCCC",
            table_border_right_style="solid",
            table_border_right_color="#CCCCCC",
        )
        # footer ----
        .tab_footnote("See?", locations=loc.body(columns="method", rows=[16]))  # XVII
        .tab_source_note(
            "Faithfulness is difflib's similarity ratio between each aphorism and its PEP 20"
            " original."
        )
        .tab_source_note(
            md("Originals: PEP 20, *The Zen of Python*. Remix: the Great Tables docs and blog.")
        )
    )


def table() -> GT:
    """The Zen of Great Tables, as a great table.

    The table is made with the first DataFrame library installed: polars, pandas, then pyarrow.
    """

    return _zen_table(frame_from_dict(_COLUMNS))


def _show() -> None:
    if _infer_render_target() == "notebook":
        try:
            table().show("notebook")
            return
        except ImportError:  # no DataFrame library to make the table with
            pass

    print(text)


_show()

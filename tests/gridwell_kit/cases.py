# The conformance cases, as Great Tables tables: each builds a GT. Imported by
# harness/gt-reference-py/make.py (which writes the reference files) and by the
# Python tests (which check that the checked-in IR still matches what gt_to_ir()
# produces).
#
# The cases mirror cases.R (the same names and tables, in gt), so the two "vs
# gridwell" pages can be read side by side and the expected grids compared.
#
# Adding a case: add it here and to cases.R, run both make scripts (make.R and
# make.py in harness/gt-reference*), then conformance/make.py, and check in the
# new files.

import pandas as pd
from great_tables import GT, loc, md, style, vals
from great_tables.data import exibble

# ─── Cases ───
#
# `description` is shown in the gallery; `build` returns the GT table. Fixed ids
# keep the HTML deterministic (Great Tables otherwise generates a random id for
# its scoped CSS).


def demographics_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "group": ["Age (years)"] * 3 + ["Sex, n (%)"] * 2 + ["Race, n (%)"] * 3,
            "label": [
                "n",
                "Mean (SD)",
                "Median (Min, Max)",
                "Female",
                "Male",
                "White",
                "Black or African American",
                "Other",
            ],
            "placebo": [
                "86",
                "75.2 (8.59)",
                "76.0 (52, 89)",
                "53 (61.6)",
                "33 (38.4)",
                "78 (90.7)",
                "8 (9.3)",
                "0",
            ],
            "low": [
                "84",
                "75.7 (8.29)",
                "77.5 (51, 88)",
                "50 (59.5)",
                "34 (40.5)",
                "78 (92.9)",
                "6 (7.1)",
                "0",
            ],
            "high": [
                "84",
                "74.4 (7.89)",
                "76.0 (56, 88)",
                "40 (47.6)",
                "44 (52.4)",
                "74 (88.1)",
                "9 (10.7)",
                "1 (1.2)",
            ],
        }
    )


def mtcars_head() -> pd.DataFrame:
    # head(mtcars) in R, with its row names as a column.
    return pd.DataFrame(
        {
            "model": [
                "Mazda RX4",
                "Mazda RX4 Wag",
                "Datsun 710",
                "Hornet 4 Drive",
                "Hornet Sportabout",
                "Valiant",
            ],
            "mpg": [21.0, 21.0, 22.8, 21.4, 18.7, 18.1],
            "cyl": [6, 6, 4, 6, 8, 6],
            "disp": [160.0, 160.0, 108.0, 258.0, 360.0, 225.0],
            "hp": [110, 110, 93, 110, 175, 105],
            "qsec": [16.46, 17.02, 18.61, 19.44, 17.02, 20.22],
            "am": [1, 1, 1, 0, 0, 0],
            "gear": [4, 4, 4, 3, 3, 3],
        }
    )


def stores_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "region": ["Europe", "Europe", "Europe", "Asia", "Asia"],
            "country": ["France", "France", "Germany", "Japan", "Japan"],
            "city": ["Paris", "Lyon", "Berlin", "Tokyo", "Osaka"],
            "stores": [12, 4, 9, 20, 7],
            "staff": [140, 38, 95, 260, 81],
        }
    )


def _demographics() -> GT:
    return (
        GT(demographics_data(), rowname_col="label", groupname_col="group", id="demographics")
        .tab_header(
            title="Table 14.1.1 Summary of Demographic Characteristics",
            subtitle="Safety Population",
        )
        .tab_spanner(label="Xanomeline", columns=["low", "high"])
        .cols_label(placebo="Placebo", low="Low Dose", high="High Dose")
        .tab_footnote(
            footnote="Percentages are based on the number of subjects in each arm.",
            locations=loc.row_groups(rows=["Sex, n (%)"]),
        )
        .tab_source_note("Source: ADSL (CDISC pilot study)")
    )


def _exibble_basic() -> GT:
    return GT(exibble, id="exibble_basic")


def _groups_and_stub() -> GT:
    return (
        GT(
            exibble[["row", "group", "char", "num", "currency"]],
            rowname_col="row",
            groupname_col="group",
            id="groups_and_stub",
        )
        .fmt_number(columns="num", decimals=2)
        .fmt_currency(columns="currency", currency="USD")
    )


def _nested_spanners() -> GT:
    return (
        GT(mtcars_head(), rowname_col="model", id="nested_spanners")
        .tab_spanner(label="Engine", columns=["cyl", "disp", "hp"], id="engine")
        .tab_spanner(label="Drivetrain", columns=["am", "gear"], id="drivetrain")
        .tab_spanner(label="Specifications", spanners=["engine", "drivetrain"])
        .fmt_number(columns=["mpg", "qsec"], decimals=1)
    )


def _adjacent_spanners() -> GT:
    data = pd.DataFrame({"a1": [1, 2], "a2": [3, 4], "b1": [5, 6], "b2": [7, 8]})
    return (
        GT(data, id="adjacent_spanners")
        .tab_spanner(label="Group A", columns=["a1", "a2"])
        .tab_spanner(label="Group B", columns=["b1", "b2"])
    )


def _summary_rows() -> GT:
    total = {"Total": lambda df: df[["num", "currency"]].sum()}
    return (
        GT(
            exibble[["row", "group", "num", "currency"]],
            rowname_col="row",
            groupname_col="group",
            id="summary_rows",
        )
        .fmt_number(columns="num", decimals=1)
        .summary_rows(fns=total, fmt=lambda x: vals.fmt_number(x, decimals=1))
        .grand_summary_rows(
            fns={"Grand total": total["Total"]},
            fmt=lambda x: vals.fmt_number(x, decimals=1),
        )
    )


def _tab_style() -> GT:
    data = exibble[["char", "num", "currency"]].head(5)
    over_one = [i for i, v in enumerate(data["num"]) if v > 1]
    return (
        GT(data, id="tab_style")
        .tab_style(
            style=[style.fill(color="#E8F0FE"), style.text(weight="bold")],
            locations=loc.body(columns="num", rows=over_one),
        )
        .tab_style(
            style=style.text(color="#B42318", style="italic"),
            locations=loc.body(columns="char"),
        )
        .tab_style(style=style.fill(color="#F2F4F7"), locations=loc.column_labels())
    )


def _striped_theme() -> GT:
    return (
        GT(exibble[["char", "fctr", "num", "date"]].head(6), id="striped_theme")
        .tab_header(title="A stylized table")
        .opt_stylize(style=6, color="blue")
        .opt_row_striping()
    )


def _notes_and_marks() -> GT:
    return (
        GT(exibble[["char", "num", "date"]].head(4), id="notes_and_marks")
        .tab_header(title=md("**Notes** and marks"), subtitle="Subtitle text")
        .tab_footnote("A column label note.", locations=loc.column_labels(columns="num"))
        .tab_footnote("A body cell note.", locations=loc.body(columns="char", rows=[1]))
        .tab_footnote("A title note.", locations=loc.title())
        .tab_source_note("Source note one.")
        .tab_source_note(md("Source note *two*."))
    )


def _hierarchical_stub() -> GT:
    return (
        GT(
            stores_data(),
            rowname_col=["country", "city"],
            groupname_col="region",
            id="hierarchical_stub",
        )
        .tab_stubhead("Location")
        .tab_spanner(label="Network", columns=["stores", "staff"])
        .cols_label(stores="Stores", staff="Staff")
    )


def _row_group_column() -> GT:
    return (
        GT(
            stores_data()[["region", "city", "stores", "staff"]],
            rowname_col="city",
            groupname_col="region",
            id="row_group_column",
        )
        .tab_options(row_group_as_column=True)
        .tab_stubhead("City")
        .tab_style(style=style.text(weight="bold"), locations=loc.row_groups())
        .cols_label(stores="Stores", staff="Staff")
    )


cases = {
    "demographics": {
        "description": (
            "Clinical demographics (t14_1_1): row groups, stub, a spanner, "
            "a footnote and a source note"
        ),
        "build": _demographics,
    },
    "exibble_basic": {
        "description": "GT(exibble) with no options: the default look for every column type",
        "build": _exibble_basic,
    },
    "groups_and_stub": {
        "description": "Row groups and a stub (exibble with rowname_col and groupname_col)",
        "build": _groups_and_stub,
    },
    "nested_spanners": {
        "description": "Two levels of spanners over formatted numbers",
        "build": _nested_spanners,
    },
    "adjacent_spanners": {
        "description": (
            "Two spanners side by side: their rules have a gap between them "
            "and run to the table's edges"
        ),
        "build": _adjacent_spanners,
    },
    "summary_rows": {
        "description": "Group summary rows and a grand summary",
        "build": _summary_rows,
    },
    "tab_style": {
        "description": "tab_style(): fills, bold, colored text, and a styled column label",
        "build": _tab_style,
    },
    "striped_theme": {
        "description": "opt_stylize() theme with row striping",
        "build": _striped_theme,
    },
    "notes_and_marks": {
        "description": "Title, subtitle, footnotes on several locations, and source notes",
        "build": _notes_and_marks,
    },
    "hierarchical_stub": {
        "description": (
            "A stub of two columns (rowname_col=[...]), its repeats merged, in row groups"
        ),
        "build": _hierarchical_stub,
    },
    "row_group_column": {
        "description": (
            "Row groups as a stub column (row_group_as_column=True), their labels bold"
        ),
        "build": _row_group_column,
    },
}

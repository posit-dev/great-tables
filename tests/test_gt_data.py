import pandas as pd
from great_tables import GT, style, loc, google_font
from great_tables._gt_data import Boxhead, ColInfo, RowInfo, Stub


def test_stub_construct_df():
    stub = Stub.from_data(pd.DataFrame({"x": [8, 9]}))

    assert len(stub) == 2
    assert stub[0] == RowInfo(0)
    assert stub[1] == RowInfo(1)


def test_stub_construct_manual():
    stub = Stub.from_data(pd.DataFrame({"x": [8, 9]}))

    stub2 = Stub(stub.rows, stub.group_rows)
    assert stub2[0] == RowInfo(0)


def test_stub_construct_df_rowname():
    # TODO: remove groupname_col from here
    stub = Stub.from_data(
        pd.DataFrame({"x": [8, 9], "y": [1, 2]}), rowname_col="x", groupname_col=None
    )


def test_stub_order_groups():
    stub = Stub.from_data(pd.DataFrame({"g": ["b", "a", "b", "c"]}), groupname_col="g")
    assert stub.group_ids == ["b", "a", "c"]

    stub2 = stub.order_groups(["c", "a", "b"])
    assert stub2.group_ids == ["c", "a", "b"]

    indice_labels = [(ii, info.defaulted_label()) for ii, info in stub2.group_indices_map()]
    assert indice_labels == [(3, "c"), (1, "a"), (0, "b"), (2, "b")]


def test_boxhead_reorder():
    boxh = Boxhead([ColInfo("a"), ColInfo("b"), ColInfo("c")])
    new_boxh = boxh.reorder(["b", "a", "c"])

    assert new_boxh == Boxhead([ColInfo("b"), ColInfo("a"), ColInfo("c")])


def test_opt_table_font_no_duplicates():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    gt_table = GT(df)

    # Apply the same Google Font multiple times with `opt_table_font()`
    gt_table = gt_table.opt_table_font(font=google_font(name="Roboto"))
    gt_table = gt_table.opt_table_font(font=google_font(name="Roboto"))
    gt_table = gt_table.opt_table_font(font=google_font(name="Open Sans"))
    gt_table = gt_table.opt_table_font(font=google_font(name="Roboto"))

    # Get the Google Font imports
    google_font_imports = gt_table._get_google_font_imports()

    # Count import statements
    roboto_imports = [css for css in google_font_imports if "Roboto" in css and "@import" in css]
    open_sans_imports = [
        css for css in google_font_imports if "Open+Sans" in css and "@import" in css
    ]

    # We should have exactly one import for each unique font
    assert len(roboto_imports) == 1
    assert len(open_sans_imports) == 1


def test_tab_style_no_duplicates():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    gt_table = GT(df)

    # Apply the same Google Font multiple times via tab_style
    gt_table = gt_table.tab_style(
        style=style.text(font=google_font(name="IBM Plex Mono")),
        locations=loc.body(columns="x"),
    )
    gt_table = gt_table.tab_style(
        style=style.text(font=google_font(name="IBM Plex Mono")),  # Same font again
        locations=loc.body(columns="y"),
    )
    gt_table = gt_table.tab_style(
        style=style.text(font=google_font(name="Source Code Pro")),  # Different font
        locations=loc.body(columns="x"),
    )
    gt_table = gt_table.tab_style(
        style=style.text(font=google_font(name="IBM Plex Mono")),  # Same font again
        locations=loc.body(columns="y"),
    )

    # Get the Google Font imports
    google_font_imports = gt_table._get_google_font_imports()

    # Count import statements
    ibm_plex_imports = [
        css for css in google_font_imports if "IBM+Plex+Mono" in css and "@import" in css
    ]
    source_code_imports = [
        css for css in google_font_imports if "Source+Code+Pro" in css and "@import" in css
    ]

    # We should have exactly one import for each unique font
    assert (
        len(ibm_plex_imports) == 1
    ), f"Expected 1 IBM Plex Mono import, got {len(ibm_plex_imports)}"
    assert (
        len(source_code_imports) == 1
    ), f"Expected 1 Source Code Pro import, got {len(source_code_imports)}"


def test_mixed_usage_no_duplicates():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    gt_table = GT(df)

    # Mix opt_table_font and tab_style with same fonts
    gt_table = gt_table.opt_table_font(font=google_font(name="Nunito"))
    gt_table = gt_table.tab_style(
        style=style.text(font=google_font(name="Nunito")),
        locations=loc.body(columns="x"),
    )
    gt_table = gt_table.opt_table_font(font=google_font(name="Nunito"))
    gt_table = gt_table.tab_style(
        style=style.text(font=google_font(name="Lato")),
        locations=loc.body(columns="y"),
    )

    # Get the Google Font imports
    google_font_imports = gt_table._get_google_font_imports()

    # Count import statements
    nunito_imports = [css for css in google_font_imports if "Nunito" in css and "@import" in css]
    lato_imports = [css for css in google_font_imports if "Lato" in css and "@import" in css]

    # Should have exactly one import for each unique font
    assert len(nunito_imports) == 1, f"Expected 1 Nunito import, got {len(nunito_imports)}"
    assert len(lato_imports) == 1, f"Expected 1 Lato import, got {len(lato_imports)}"


def test_rendered_html_no_duplicates():
    df = pd.DataFrame({"num": [1, 2], "char": ["a", "b"]})

    gt_table = (
        GT(df)
        .opt_table_font(font=google_font(name="Playfair Display"))
        .tab_style(
            style=style.text(font=google_font(name="Playfair Display")),
            locations=loc.body(columns="num"),
        )
        .tab_style(
            style=style.text(font=google_font(name="Fira Code")),
            locations=loc.body(columns="char"),
        )
    )

    # Get the raw HTML output
    html = gt_table.as_raw_html()

    # Count import statements in the HTML
    playfair_count = html.count(
        "@import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');"
    )
    fira_code_count = html.count(
        "@import url('https://fonts.googleapis.com/css2?family=Fira+Code&display=swap');"
    )

    # Expect one import for each unique font in the HTML output
    assert playfair_count == 1
    assert fira_code_count == 1


def test_google_font_imports_methods():
    df = pd.DataFrame({"x": [1, 2, 3]})
    gt_table = GT(df)

    import1 = "@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');"
    import2 = "@import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');"

    # Test of the initial state (no imports)
    assert gt_table._get_google_font_imports() == []

    gt_tbl = gt_table._add_google_font_import(import1)
    assert len(gt_tbl._get_google_font_imports()) == 1
    assert import1 in gt_tbl._get_google_font_imports()

    # Test with a duplicate font import (doesn't add to the count)
    gt_tbl = gt_tbl._add_google_font_import(import1)
    assert len(gt_tbl._get_google_font_imports()) == 1

    # Add a second unique import
    gt_tbl = gt_tbl._add_google_font_import(import2)
    assert len(gt_tbl._get_google_font_imports()) == 2

    # Check that both imports are present
    assert import1 in gt_tbl._get_google_font_imports()
    assert import2 in gt_tbl._get_google_font_imports()

    # Test that imports are sorted consistently
    imports = gt_tbl._get_google_font_imports()
    assert imports == sorted(imports)

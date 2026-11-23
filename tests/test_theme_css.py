import re
import sys

import pandas as pd
import pytest

from great_tables import GT, Theme, loc, style
from great_tables._scss import compile_scss, css_var, theme_declarations, var_blocks


@pytest.fixture
def gt() -> GT:
    return GT(pd.DataFrame({"x": [1, 2]}), id="abc")


VAR = re.compile(r"var\((--[\w-]+)(?:,\s*([^()]*))?\)")
CALC = re.compile(r"calc\((\d+)px ([+-]) (\d+)px\)")


def resolve_vars(text: str, env: dict[str, str]) -> str:
    """Replace var() references innermost first, then fold `calc(Apx +/- Bpx)`. A variable set to
    `initial` is unset, so its fallback is used."""
    while VAR.search(text):
        text = VAR.sub(lambda m: env[m[1]] if env.get(m[1], "initial") != "initial" else m[2], text)
    return CALC.sub(lambda m: f"{int(m[1]) + (int(m[3]) if m[2] == '+' else -int(m[3]))}px", text)


def resolved_css(data: GT, dark: bool = False) -> str:
    light, dark_decls = theme_declarations(data)
    css = compile_scss(data, id="abc", compress=False, variables=True)
    css = css.replace(var_blocks("#abc", light, dark_decls), "")
    return resolve_vars(css, {**light, **dark_decls} if dark else light)


CONFIGS = {
    "default": lambda gt: gt,
    "explicit": lambda gt: gt.tab_options(
        table_background_color="#FFFFFF", data_row_padding="3px", heading_padding="6px"
    ),
    "stylize": lambda gt: gt.opt_stylize(style=6, color="blue"),
    "tokens": lambda gt: gt.opt_theme(
        Theme(
            background="#FDF6E3", foreground="#073642", border="#CCCCCC", font="Inter", font_size=14
        )
    ),
    "dark_theme": lambda gt: gt.opt_theme(
        Theme(
            table_body_hlines_color="#ABCDEF",
            dark=Theme(
                background="#101418", stripe="#181C20", column_labels_background_color="#202830"
            ),
        )
    ),
    "overrides": lambda gt: gt.tab_options(data_row_padding="3px").opt_theme(
        Theme(
            foreground="#073642",
            stripe="#EEEEEE",
            accent="#FF0000",
            table_body_hlines_color="#ABCDEF",
            table_font_color="#111111",
            dark=Theme(
                foreground="#FAFAFA", table_body_hlines_color="#222222", data_row_padding="9px"
            ),
        )
    ),
    "keywords": lambda gt: gt.tab_options(
        heading_background_color="transparent", column_labels_background_color="currentcolor"
    ),
    "navy": lambda gt: gt.opt_theme(Theme(background="#0B1E33")),
    "pale_dark": lambda gt: gt.opt_theme(Theme(dark=Theme(background="#FAFAFA"))),
    "pale_dark_foreground": lambda gt: gt.opt_theme(
        Theme(foreground="#073642", dark=Theme(background="#FAFAFA"))
    ),
}


PINNED = ("explicit", "stylize", "keywords")


def test_css_var():
    assert css_var("data_row_padding") == "--gt-data-row-padding"


@pytest.mark.parametrize("config", CONFIGS)
def test_variables_resolve_to_literal_css_light(gt: GT, config: str):
    data = CONFIGS[config](gt).opt_theme(mode="light")
    assert resolved_css(data) == compile_scss(data, id="abc", compress=False, variables=False)


def test_rules_are_the_same_for_every_table(gt: GT):
    def rules(data: GT) -> str:
        css = compile_scss(data, id="abc", compress=False, variables=True)
        return css.replace(var_blocks("#abc", *theme_declarations(data)), "")

    assert rules(gt) == rules(gt.tab_options(data_row_padding="3px", table_body_hlines_color="red"))


def test_only_python_set_values_are_declared_publicly(gt: GT):
    light, _ = theme_declarations(gt)
    assert not any(name.startswith("--gt-") for name in light)

    themed = gt.tab_options(data_row_padding="3px").opt_theme(
        Theme(border="#CCCCCC", accent="#FF0000")
    )
    light, _ = theme_declarations(themed)
    public = {name: value for name, value in light.items() if name.startswith("--gt-")}
    assert public == {
        "--gt-data-row-padding": "3px",
        "--gt-color-border": "#CCCCCC",
        "--gt-color-accent": "#FF0000",
    }
    assert light["--_gt-border"] == "var(--gt-color-border, #D3D3D3)"


def test_non_px_length_in_derived_padding(gt: GT):
    css = compile_scss(gt.tab_options(heading_padding="1em"), id="abc", variables=True)
    assert "calc(var(--gt-heading-padding, 4px) - 1px)" in css
    assert "--gt-heading-padding: 1em" in css


def test_important_applies_to_rules_only(gt: GT):
    css = compile_scss(
        gt.tab_options(data_row_padding="3px"), id="abc", all_important=True, variables=True
    )
    assert "--gt-data-row-padding: 3px;" in css
    assert "padding-top: var(--gt-data-row-padding, 8px) !important;" in css


@pytest.mark.parametrize("variables", [False, True])
def test_theme_additional_css_is_applied(gt: GT, variables: bool):
    themed = gt.opt_theme(Theme(table_additional_css=[".zzz{color:red}"]))
    assert ".zzz{color:red}" in compile_scss(themed, id="abc", variables=variables)


@pytest.mark.parametrize("config", CONFIGS)
def test_dark_block_resolves_to_literal_dark_css(gt: GT, config: str):
    data = CONFIGS[config](gt)
    forced = data.opt_theme(mode="dark")
    if config in PINNED:
        assert theme_declarations(data)[1] is None
    else:
        assert resolved_css(data, dark=True) == compile_scss(
            forced, id="abc", compress=False, variables=False
        )
    assert resolved_css(forced) == compile_scss(forced, id="abc", compress=False, variables=False)


@pytest.mark.parametrize(
    "pin",
    [
        lambda gt: gt.opt_stylize(style=6, color="blue"),
        lambda gt: gt.tab_options(heading_background_color="#FF0000"),
    ],
)
def test_table_with_own_backgrounds_stays_light_in_auto_mode(gt: GT, pin):
    data = pin(gt)
    css = compile_scss(data, id="abc", variables=True)
    assert "prefers-color-scheme" not in css and "vscode-dark" not in css
    assert theme_declarations(data)[1] is None
    assert '<html lang="en">' in data.as_raw_html(make_page=True)


def test_backgrounds_from_a_theme_do_not_pin_auto_mode(gt: GT):
    data = gt.opt_theme(Theme(heading_background_color="#FF0000"))
    assert "prefers-color-scheme" in compile_scss(data, id="abc", variables=True)
    assert '<html lang="en" style="color-scheme: light dark">' in data.as_raw_html(make_page=True)


def test_forced_dark_still_applies_to_a_table_with_own_backgrounds(gt: GT):
    data = gt.opt_stylize().opt_theme(mode="dark")
    assert "var(--gt-color-background, #1E1E1E)" in compile_scss(data, id="abc", variables=True)


def test_auto_mode_selectors(gt: GT):
    css = compile_scss(gt, id="abc", compress=False, variables=True)
    assert 'body[data-jp-theme-light="false"] #abc' in css
    assert "body.vscode-dark #abc" in css
    assert 'body.dark-theme[data-theme="dark"] #abc' in css
    assert "@media (prefers-color-scheme: dark)" in css
    assert '#abc:not(body[data-jp-theme-light="true"] *, body.vscode-light *' in css
    assert 'body.light-theme[data-theme="light"] *' in css


@pytest.mark.parametrize("mode, background", [("light", "#FFFFFF"), ("dark", "#1E1E1E")])
def test_fixed_modes_emit_no_switching(gt: GT, mode: str, background: str):
    css = compile_scss(gt.opt_theme(mode=mode), id="abc", compress=False, variables=True)
    assert "prefers-color-scheme" not in css
    assert "vscode-dark" not in css
    assert f"var(--gt-color-background, {background})" in css


def test_light_token_is_overridden_in_dark(gt: GT):
    _, dark = theme_declarations(gt.opt_theme(Theme(background="#FDF6E3", border="#CCCCCC")))
    assert dark["--gt-color-background"] == "#1E1E1E"
    assert dark["--gt-color-border"] == "#4A4A4A"
    assert "--gt-color-stripe" not in dark


def test_explicit_option_is_not_overridden_in_dark(gt: GT):
    themed = gt.tab_options(table_body_hlines_color="#000000").opt_theme(
        Theme(dark=Theme(table_body_hlines_color="#222222"))
    )
    _, dark = theme_declarations(themed)
    assert "--gt-table-body-hlines-color" not in dark


def test_table_without_id_uses_class_scope(gt: GT):
    css = compile_scss(gt, id=None, compress=False, variables=True)
    assert "body.vscode-dark .gt_table" in css
    assert ".gt_table:not(body" in css


def test_html_output_uses_variables_and_follows_preference(gt: GT):
    html = gt.as_raw_html()
    assert "var(--_gt-background)" in html
    assert "prefers-color-scheme" in html


def test_inline_css_is_literal(gt: GT):
    pytest.importorskip("css_inline")
    html = gt.as_raw_html(inline_css=True)
    assert "var(" not in html and "prefers-color-scheme" not in html
    dark = gt.opt_theme(mode="dark").as_raw_html(inline_css=True)
    assert "#1e1e1e" in dark.lower() and "var(" not in dark


@pytest.mark.parametrize("interactive", [False, True])
@pytest.mark.parametrize(
    "mode, root",
    [
        ("auto", '<html lang="en" style="color-scheme: light dark">'),
        ("dark", '<html lang="en" style="color-scheme: dark">'),
        ("light", '<html lang="en">'),
    ],
)
def test_page_declares_color_scheme_on_its_root(gt: GT, mode: str, root: str, interactive: bool):
    if interactive:
        gt = gt.opt_interactive()
    html = gt.opt_theme(mode=mode).as_raw_html(make_page=True)
    assert root in html
    assert '<meta name="color-scheme"' not in html


@pytest.mark.parametrize(
    "base_format, uses_variables",
    [("html", True), ("revealjs", True), ("typst", False), ("docx", False)],
)
def test_quarto_non_html_render_is_literal(
    gt: GT, monkeypatch, tmp_path, base_format, uses_variables
):
    import json

    info = tmp_path / "info.json"
    info.write_text(json.dumps({"format": {"identifier": {"base-format": base_format}}}))
    monkeypatch.setenv("QUARTO_BIN_PATH", "/usr/bin/quarto")
    monkeypatch.setenv("QUARTO_EXECUTE_INFO", str(info))
    html = gt.as_raw_html()
    assert ("var(--_gt-background)" in html) is uses_variables
    assert ("prefers-color-scheme" in html) is uses_variables
    assert ("color-scheme:" in gt.as_raw_html(make_page=True).split("<head>")[0]) is uses_variables


def test_quarto_without_execute_info_is_literal(gt: GT, monkeypatch):
    monkeypatch.setenv("QUARTO_BIN_PATH", "/usr/bin/quarto")
    monkeypatch.delenv("QUARTO_EXECUTE_INFO", raising=False)
    html = gt.as_raw_html()
    assert "var(--_gt-background)" not in html and "prefers-color-scheme" not in html


@pytest.mark.parametrize("content", [None, "not json", '{"format": {}}', "[1]"])
def test_quarto_unreadable_execute_info_is_not_html(monkeypatch, tmp_path, content):
    from great_tables.quarto import quarto_format_is_html

    info = tmp_path / "info.json"
    if content is not None:
        info.write_text(content)
    monkeypatch.setenv("QUARTO_EXECUTE_INFO", str(info))
    assert quarto_format_is_html() is False


def test_quarto_format_without_execute_info_is_not_html(monkeypatch):
    from great_tables.quarto import quarto_format_is_html

    monkeypatch.delenv("QUARTO_EXECUTE_INFO", raising=False)
    assert quarto_format_is_html() is False


class FakeComm:
    closed = False

    def close(self):
        self.closed = True


def kernel_setup_msg(base_format: str) -> dict:
    options = {"format": {"identifier": {"base-format": base_format}}}
    return {"content": {"target_name": "quarto_kernel_setup", "data": {"options": options}}}


@pytest.mark.parametrize(
    "base_format, uses_variables",
    [("html", True), ("dashboard", True), ("typst", False), ("docx", False)],
)
@pytest.mark.parametrize("info_format", [None, "html", "typst"])
def test_quarto_kernel_setup_format_wins_over_execute_info(
    gt: GT, monkeypatch, tmp_path, base_format, uses_variables, info_format
):
    # A kernel Quarto keeps running between renders: QUARTO_EXECUTE_INFO is the first render's,
    # whose file is gone (None) or is another format's
    import json

    from great_tables import quarto

    info = tmp_path / "info.json"
    if info_format is not None:
        info.write_text(json.dumps({"format": {"identifier": {"base-format": info_format}}}))
    monkeypatch.setenv("QUARTO_BIN_PATH", "/usr/bin/quarto")
    monkeypatch.setenv("QUARTO_EXECUTE_INFO", str(info))
    monkeypatch.setattr(quarto, "_kernel_format", None)
    comm = FakeComm()
    quarto._on_kernel_setup(comm, kernel_setup_msg(base_format))
    assert comm.closed
    assert quarto.quarto_format_is_html() is uses_variables
    assert ("var(--_gt-background)" in gt.as_raw_html()) is uses_variables


@pytest.mark.parametrize(
    "msg",
    [{}, {"content": {"data": {}}}, {"content": {"data": {"options": None}}}, kernel_setup_msg(1)],
)
def test_quarto_kernel_setup_without_format_is_not_html(monkeypatch, tmp_path, msg):
    import json

    from great_tables import quarto

    info = tmp_path / "info.json"
    info.write_text(json.dumps({"format": {"identifier": {"base-format": "html"}}}))
    monkeypatch.setenv("QUARTO_EXECUTE_INFO", str(info))
    monkeypatch.setattr(quarto, "_kernel_format", None)
    quarto._on_kernel_setup(FakeComm(), msg)
    assert quarto.quarto_format_is_html() is False


def test_quarto_kernel_setup_is_watched_in_an_ipython_kernel(monkeypatch):
    IPython = pytest.importorskip("IPython")
    from great_tables import quarto

    targets = {}

    class Shell:
        class kernel:
            class comm_manager:
                @staticmethod
                def register_target(name, callback):
                    targets[name] = callback

    monkeypatch.setattr(IPython, "get_ipython", lambda: Shell())
    quarto._watch_kernel_setup()
    assert targets == {"quarto_kernel_setup": quarto._on_kernel_setup}

    # (And nothing happens outside a kernel: outside IPython, in a terminal's, or without IPython)
    for shell in [None, object()]:
        monkeypatch.setattr(IPython, "get_ipython", lambda shell=shell: shell)
        quarto._watch_kernel_setup()
    monkeypatch.setitem(sys.modules, "IPython", None)
    quarto._watch_kernel_setup()
    assert list(targets) == ["quarto_kernel_setup"]


@pytest.mark.parametrize("base_format, meta", [("html", True), ("typst", False)])
def test_interactive_page_declares_color_scheme_by_quarto_format(
    gt: GT, monkeypatch, tmp_path, base_format, meta
):
    import json

    info = tmp_path / "info.json"
    info.write_text(json.dumps({"format": {"identifier": {"base-format": base_format}}}))
    monkeypatch.setenv("QUARTO_BIN_PATH", "/usr/bin/quarto")
    monkeypatch.setenv("QUARTO_EXECUTE_INFO", str(info))
    html = gt.opt_interactive().as_raw_html(make_page=True)
    assert ('<html lang="en" style="color-scheme: light dark">' in html) is meta
    assert '<meta name="color-scheme"' not in html


def test_gti_page_declares_color_scheme(gt: GT):
    from great_tables import GTI

    html = GTI(pd.DataFrame({"x": [1, 2]})).opt_theme(mode="dark").as_raw_html(make_page=True)
    assert '<html lang="en" style="color-scheme: dark">' in html


def filled(gt: GT, *styles) -> str:
    return gt.tab_style(style=list(styles), locations=loc.body(columns="x", rows=[0])).as_raw_html()


@pytest.mark.parametrize(
    "color, text",
    [
        ("lightcyan", "var(--_gt-text-dark)"),
        ("navy", "var(--_gt-text-light)"),
        ("#FFFFFF", "var(--_gt-text-dark)"),
    ],
)
def test_filled_cell_gets_contrast_text(gt: GT, color: str, text: str):
    assert f"color: {text}; background-color: {color};" in filled(gt, style.fill(color=color))


def test_opaque_hex_fill_with_alpha_gets_contrast_text(gt: GT):
    assert "color: var(--_gt-text-light); background-color: #000080FF;" in filled(
        gt, style.fill(color="#000080FF")
    )


def test_filled_cell_keeps_its_own_text_color(gt: GT):
    html = filled(gt, style.fill(color="lightcyan"), style.text(color="red"))
    assert "--_gt-text" not in html.split("</style>")[1]


def test_fill_with_text_style_but_no_color_gets_contrast_text(gt: GT):
    html = filled(gt, style.fill(color="lightcyan"), style.text(weight="bold"))
    assert "color: var(--_gt-text-dark);" in html


@pytest.mark.parametrize(
    "color",
    [
        "rgba(0, 0, 0, 0.5)",
        "var(--x)",
        "transparent",
        "currentcolor",
        "currentColor",
        "inherit",
        "initial",
        "unset",
        "TRANSPARENT",
        "Inherit",
        "#FFFFFF00",
        "#FFFF0080",
        "#ff08",
    ],
)
def test_unparseable_fill_is_left_alone(gt: GT, color: str):
    assert "--_gt-text" not in filled(gt, style.fill(color=color)).split("</style>")[1]


def test_data_color_cells_are_unchanged(gt: GT):
    assert "--_gt-text" not in gt.data_color(columns="x").as_raw_html().split("</style>")[1]


def test_data_color_without_autocolor_text_is_unchanged(gt: GT):
    html = gt.data_color(
        columns="x", palette=["navy", "lightcyan"], autocolor_text=False
    ).as_raw_html()
    assert "--_gt-text" not in html.split("</style>")[1]
    assert "light-dark(" not in html.split("</style>")[1]


def test_style_fill_over_data_color_without_autocolor_text_gets_contrast_text(gt: GT):
    styled = gt.data_color(columns="x", palette=["navy", "navy"], autocolor_text=False)
    html = styled.tab_style(
        style=style.fill(color="navy"), locations=loc.body(columns="x", rows=[0])
    ).as_raw_html()
    assert (
        "color: var(--_gt-text-light); background-color: #000080; background-color: navy;" in html
    )


def test_inline_css_fill_text_is_literal(gt: GT):
    pytest.importorskip("css_inline")
    themed = gt.tab_options(table_font_color_light="#FAFAFA")
    html = themed.tab_style(style=style.fill(color="navy"), locations=loc.body()).as_raw_html(
        inline_css=True
    )
    assert "var(" not in html
    assert "#fafafa" in html.lower()


def test_inline_css_fill_text_in_forced_dark(gt: GT):
    pytest.importorskip("css_inline")
    styled = (
        gt.opt_theme(mode="dark")
        .tab_style(style=style.fill(color="lightcyan"), locations=loc.body(rows=[0]))
        .tab_style(style=style.fill(color="navy"), locations=loc.body(rows=[1]))
    )
    cells = re.findall(r"<td[^>]*>", styled.as_raw_html(inline_css=True))
    assert "color: #333333" in cells[0] and "background-color: lightcyan" in cells[0]
    assert "color: #E0E0E0" in cells[1] and "background-color: navy" in cells[1]


def test_text_color_on_unfilled_cell_adapts_in_dark(gt: GT):
    html = filled(gt, style.text(color="navy"))
    assert (
        "color: navy; color: light-dark(navy, color-mix(in srgb, navy 35%, currentcolor));" in html
    )


def last_color(html: str) -> str:
    cell = re.search(r'<td[^>]*style="([^"]*)"', html.split("</style>")[1])[1]
    return re.findall(r"(?:^|(?<=;))\s*color: ([^;]*);", cell)[-1]


def test_authored_css_color_beats_contrast_text(gt: GT):
    html = filled(gt, style.fill(color="navy"), style.css("color: yellow;"))
    assert "var(--_gt-text-light)" in html
    assert last_color(html) == "yellow"


def test_authored_css_color_beats_dark_blend(gt: GT):
    html = filled(gt, style.text(color="navy"), style.css("color: red;"))
    assert "light-dark(navy" in html
    assert last_color(html) == "red"


def test_text_blend_follows_its_color(gt: GT):
    html = filled(gt, style.text(color="navy", weight="bold"))
    assert (
        "color: navy; color: light-dark(navy, color-mix(in srgb, navy 35%, currentcolor));"
        "font-weight: bold;" in html
    )


def test_authored_light_dark_is_kept_in_literal_output(gt: GT):
    pytest.importorskip("css_inline")
    styled = gt.tab_style(
        style=[style.text(color="navy"), style.css("color: light-dark(black, white);")],
        locations=loc.body(columns="x", rows=[0]),
    )
    html = styled.as_raw_html(inline_css=True)
    assert "light-dark(black, white)" in html
    assert "light-dark(navy" not in html


def test_text_color_on_filled_cell_is_left_alone(gt: GT):
    assert "light-dark(" not in filled(gt, style.fill(color="lightcyan"), style.text(color="navy"))


@pytest.mark.parametrize("mode", ["light", "dark"])
def test_literal_output_keeps_authored_text_color(gt: GT, mode: str):
    pytest.importorskip("css_inline")
    styled = gt.opt_theme(mode=mode).tab_style(style=style.text(color="navy"), locations=loc.body())
    html = styled.as_raw_html(inline_css=True)
    assert "light-dark(" not in html and "color: navy" in html


@pytest.mark.parametrize("mode", ["light", "dark"])
def test_color_scheme_is_declared(gt: GT, mode: str):
    light, dark = theme_declarations(gt)
    assert light["color-scheme"] == "light" and dark["color-scheme"] == "dark"
    fixed, _ = theme_declarations(gt.opt_theme(mode=mode))
    assert fixed["color-scheme"] == mode


def test_fill_signature_has_only_color():
    import inspect

    assert list(inspect.signature(style.fill).parameters) == ["color"]

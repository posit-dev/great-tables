import re
import sys

import pandas as pd
import pytest

from great_tables import GT, Theme, loc, style
from great_tables._scss import (
    compile_scss,
    css_var,
    substitute_vars,
    theme_declarations,
    var_blocks,
)


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


DECLARATION = re.compile(r"^ *(--[\w-]+): (.*);$", flags=re.MULTILINE)

# (What only the CSS of a table that switches has)
SWITCHING = "@supports (color: light-dark(#000, #fff))"


def pick_scheme(text: str, dark: bool) -> str:
    """Replace each `light-dark(L, D)` with L, or with D if `dark`."""
    while (start := text.find("light-dark(")) != -1:
        depth, end, comma = 1, start + len("light-dark("), None
        while depth:
            depth += {"(": 1, ")": -1}.get(text[end], 0)
            if text[end] == "," and depth == 1 and comma is None:
                comma = end
            end += 1
        chosen = text[comma + 1 : end - 1] if dark else text[start + len("light-dark(") : comma]
        text = text[:start] + chosen.strip() + text[end:]
    return text


# (A border color set for both modes, blended in dark mode: the literal CSS has it as given)
BLEND = re.compile(r"color-mix\(in srgb, ([^()]+?) 35%, currentcolor\)")


def resolved_css(data: GT, dark: bool = False) -> str:
    """The table's rules with the custom properties that its CSS declares (in the order it does)
    filled in, for the light or dark scheme."""
    blocks = var_blocks("#abc", *theme_declarations(data))
    css = compile_scss(data, id="abc", compress=False, variables=True).replace(blocks, "")
    env = {name: pick_scheme(value, dark) for name, value in DECLARATION.findall(blocks)}
    return resolve_vars(css, env)


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
                foreground="#FAFAFA",
                table_body_hlines_color="#222222",
                table_body_vlines_color="#333333",
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


def test_substitute_vars():
    values = {"--gt-a": "#111111", "--gt-b": "initial"}
    assert substitute_vars("var(--gt-a, #000000)", values) == "#111111"
    assert substitute_vars("var(--gt-b, #222222) var(--gt-c)", values) == "#222222 var(--gt-c)"
    nested = "var(--gt-c, var(--gt-b, var(--gt-a, #000000)))"
    assert substitute_vars(nested, values) == "var(--gt-c, #111111)"


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
def test_dark_scheme_resolves_to_literal_dark_css(gt: GT, config: str):
    data = CONFIGS[config](gt)
    forced = data.opt_theme(mode="dark")
    if config in PINNED:
        assert theme_declarations(data)[1] is None
    else:
        assert BLEND.sub(r"\1", resolved_css(data, dark=True)) == compile_scss(
            forced, id="abc", compress=False, variables=False
        )
    assert BLEND.sub(r"\1", resolved_css(forced)) == compile_scss(
        forced, id="abc", compress=False, variables=False
    )


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
    assert SWITCHING not in css and "@scope" not in css
    assert theme_declarations(data)[1] is None
    assert '<html lang="en">' in data.as_raw_html(make_page=True)


def test_background_from_a_theme_pins_auto_mode_without_a_dark_value(gt: GT):
    data = gt.opt_theme(Theme(heading_background_color="#FF0000"))
    assert SWITCHING not in compile_scss(data, id="abc", variables=True)
    assert theme_declarations(data)[1] is None
    assert '<html lang="en">' in data.as_raw_html(make_page=True)


def test_background_from_a_theme_with_a_dark_value_follows_the_page(gt: GT):
    data = gt.opt_theme(
        Theme(
            heading_background_color="#FF0000",
            dark=Theme(heading_background_color="#400000"),
        )
    )
    assert SWITCHING in compile_scss(data, id="abc", variables=True)
    assert '<html lang="en" style="color-scheme: light dark">' in data.as_raw_html(make_page=True)
    assert "light-dark(#FF0000, #400000)" in compile_scss(data, id="abc", variables=True)


def test_forced_dark_still_applies_to_a_table_with_own_backgrounds(gt: GT):
    data = gt.opt_stylize().opt_theme(mode="dark")
    assert "var(--gt-color-background, #1E1E1E)" in compile_scss(data, id="abc", variables=True)


def test_auto_mode_takes_its_scheme_from_the_page(gt: GT):
    css = compile_scss(gt, id="abc", compress=False, variables=True)
    first = css[css.index("#abc {") : css.index("}", css.index("#abc {"))]
    assert "color-scheme" not in first and "prefers-color-scheme" not in css
    assert "--_gt-stripe: light-dark(var(--gt-color-stripe, #F4F4F4), " in css
    assert (
        '@scope (body[data-jp-theme-light="false"], body.vscode-dark, '
        "body.vscode-high-contrast:not(.vscode-high-contrast-light), body.quarto-dark, "
        '[data-bs-theme="dark"], body.dark-theme[data-theme="dark"]) {\n'
        "  #abc {\n    color-scheme: dark;\n  }\n}"
    ) in css
    assert (
        '@scope (body[data-jp-theme-light="true"], body.vscode-light, '
        "body.vscode-high-contrast-light, body.quarto-light, "
        '[data-bs-theme="light"], body.light-theme[data-theme="light"]) {\n'
        "  #abc {\n    color-scheme: light;\n  }\n}"
    ) in css
    # (For browsers without `@scope`)
    assert '@layer {\n  body[data-jp-theme-light="false"] #abc,\n' in css


@pytest.mark.parametrize("mode, background", [("light", "#FFFFFF"), ("dark", "#1E1E1E")])
def test_fixed_modes_emit_no_switching(gt: GT, mode: str, background: str):
    css = compile_scss(gt.opt_theme(mode=mode), id="abc", compress=False, variables=True)
    assert SWITCHING not in css and "@scope" not in css
    assert f"#abc {{\n  color-scheme: {mode};" in css
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
    # (Blended, as a border color set for both modes is)
    assert dark["--gt-table-body-hlines-color"] == "color-mix(in srgb, #000000 35%, currentcolor)"


@pytest.mark.parametrize(
    "config",
    [
        lambda gt: gt.tab_options(table_body_hlines_color="black", table_border_top_color="red"),
        lambda gt: gt.opt_theme(
            Theme(table_body_hlines_color="black", table_border_top_color="red")
        ),
    ],
)
def test_border_colors_set_for_both_modes_are_blended_in_dark(gt: GT, config):
    data = config(gt)
    css = compile_scss(data, id="abc", compress=False, variables=True)
    assert (
        "    --gt-table-body-hlines-color: light-dark(black, "
        "color-mix(in srgb, black 35%, currentcolor));"
    ) in css
    assert (
        "    --gt-table-border-top-color: light-dark(red, color-mix(in srgb, red 35%, currentcolor));"
    ) in css
    forced = compile_scss(data.opt_theme(mode="dark"), id="abc", compress=False, variables=True)
    assert "  --gt-table-body-hlines-color: color-mix(in srgb, black 35%, currentcolor);" in forced
    # (In light mode, and in literal CSS, the color is as given)
    assert resolved_css(data).count("color-mix(") == 0
    literal = compile_scss(data.opt_theme(mode="dark"), id="abc", compress=False, variables=False)
    assert "color-mix(" not in literal


def test_border_color_with_a_dark_value_is_not_blended(gt: GT):
    data = gt.opt_theme(
        Theme(table_body_hlines_color="black", dark=Theme(table_body_hlines_color="#555555"))
    )
    _, dark = theme_declarations(data)
    assert dark["--gt-table-body-hlines-color"] == "#555555"
    assert "color-mix(" not in compile_scss(data, id="abc", variables=True)


def test_table_without_id_uses_class_scope(gt: GT):
    css = compile_scss(gt, id=None, compress=False, variables=True)
    assert '@scope (body[data-jp-theme-light="false"]' in css
    assert "  .gt_table {\n    color-scheme: dark;" in css
    assert ".gt_table {\n    --_gt-background: light-dark(" in css


def test_html_output_uses_variables_and_follows_preference(gt: GT):
    html = gt.as_raw_html()
    assert "var(--_gt-background)" in html
    assert SWITCHING in html


def test_inline_css_is_literal(gt: GT):
    pytest.importorskip("css_inline")
    html = gt.as_raw_html(inline_css=True)
    assert "var(" not in html and "light-dark(" not in html
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
    assert (SWITCHING in html) is uses_variables
    assert ("color-scheme:" in gt.as_raw_html(make_page=True).split("<head>")[0]) is uses_variables


def test_quarto_without_execute_info_is_literal(gt: GT, monkeypatch):
    monkeypatch.setenv("QUARTO_BIN_PATH", "/usr/bin/quarto")
    monkeypatch.delenv("QUARTO_EXECUTE_INFO", raising=False)
    html = gt.as_raw_html()
    assert "var(--_gt-background)" not in html and SWITCHING not in html


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


def test_data_color_without_autocolor_text_gets_contrast_text_in_dark_only(gt: GT):
    styled = gt.data_color(columns="x", palette=["navy", "lightcyan"], autocolor_text=False)
    body = styled.as_raw_html().split("</style>")[1]
    assert (
        "color: light-dark(currentcolor, var(--_gt-text-light)); background-color: #000080;" in body
    )
    assert (
        "color: light-dark(currentcolor, var(--_gt-text-dark)); background-color: #e0ffff;" in body
    )


def test_cell_border_color_is_blended_in_dark_only(gt: GT):
    styled = gt.tab_style(style=style.borders(sides=["top", "left"]), locations=loc.body(rows=[0]))
    blend = "light-dark(#000000, color-mix(in srgb, #000000 35%, currentcolor))"
    assert (
        f"border-top: 1px solid #000000;border-left: 1px solid #000000; "
        f"border-top-color: {blend}; border-left-color: {blend};"
    ) in styled.as_raw_html()


@pytest.mark.parametrize("mode", ["light", "dark"])
def test_inline_css_cell_border_color_is_as_written(gt: GT, mode: str):
    pytest.importorskip("css_inline")
    styled = gt.tab_style(style=style.borders(sides="top", color="red"), locations=loc.body())
    html = styled.opt_theme(mode=mode).as_raw_html(inline_css=True)
    assert "border-top: 1px solid red" in html
    assert "light-dark(" not in html and "color-mix(" not in html


@pytest.mark.parametrize(("mode", "text"), [("light", None), ("dark", "#333333")])
def test_inline_css_data_color_without_autocolor_text(gt: GT, mode: str, text: str | None):
    pytest.importorskip("css_inline")
    styled = gt.data_color(columns="x", palette=["lightcyan", "lightcyan"], autocolor_text=False)
    html = styled.opt_theme(mode=mode).as_raw_html(inline_css=True)
    assert "light-dark(" not in html and "currentcolor" not in html
    cells = re.findall(r'<td class="gt_row[^"]*" style="([^"]*)"', html)
    assert all(("color: #333333;" in cell) == (text is not None) for cell in cells)


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
    html = filled(gt, style.fill(color="lightcyan"), style.text(color="navy"))
    assert "light-dark(" not in html.split("</style>")[1]


@pytest.mark.parametrize("mode", ["light", "dark"])
def test_literal_output_keeps_authored_text_color(gt: GT, mode: str):
    pytest.importorskip("css_inline")
    styled = gt.opt_theme(mode=mode).tab_style(style=style.text(color="navy"), locations=loc.body())
    html = styled.as_raw_html(inline_css=True)
    assert "light-dark(" not in html and "color: navy" in html


@pytest.mark.parametrize("mode", ["light", "dark"])
def test_color_scheme_is_declared(gt: GT, mode: str):
    light, dark = theme_declarations(gt)
    assert "color-scheme" not in light and "color-scheme" not in dark
    fixed, _ = theme_declarations(gt.opt_theme(mode=mode))
    assert fixed["color-scheme"] == mode


def test_fill_signature_has_only_color():
    import inspect

    assert list(inspect.signature(style.fill).parameters) == ["color"]

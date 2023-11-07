from __future__ import annotations
from typing import Optional, Union, List, Any, cast
from great_tables import _utils

default_fonts_list = [
    "-apple-system",
    "BlinkMacSystemFont",
    "Segoe UI",
    "Roboto",
    "Oxygen",
    "Ubuntu",
    "Cantarell",
    "Helvetica Neue",
    "Fira Sans",
    "Droid Sans",
    "Arial",
    "sans-serif",
]


class OptionsInfo:
    parameter: str
    scss: Optional[bool]
    category: Optional[str]
    type: Optional[str]
    value: Optional[Union[Any, List[str]]]

    def __init__(
        self,
        parameter: str,
        scss: Optional[bool] = None,
        category: Optional[str] = None,
        type: Optional[str] = None,
        value: Optional[Union[Any, List[str]]] = None,
    ):
        self.parameter = parameter
        self.scss = scss
        self.category = category
        self.type = type
        self.value = value


# fmt: off
class Options:
    def __init__(self):
        self._options: dict[str, OptionsInfo] = dict(
           (v.parameter, v) for v in [
            #           parameter                            scss    category            type        value
            OptionsInfo("container_width",                   False,  "container",        "px",       "auto"),
            OptionsInfo("container_height",                  False,  "container",        "px",       "auto"),
            OptionsInfo("container_overflow_x",              False,  "container",        "overflow", "auto"),
            OptionsInfo("container_overflow_y",              False,  "container",        "overflow", "auto"),
            OptionsInfo("table_id",                          False,  "table",            "value",    None),
            OptionsInfo("table_caption",                     False,  "table",            "value",    None),
            OptionsInfo("table_width",                        True,  "table",            "px",       "auto"),
            OptionsInfo("table_layout",                       True,  "table",            "value",    "fixed"),
            OptionsInfo("table_margin_left",                  True,  "table",            "px",       "auto"),
            OptionsInfo("table_margin_right",                 True,  "table",            "px",       "auto"),
            OptionsInfo("table_background_color",             True,  "table",            "value",    "#FFFFFF"),
            OptionsInfo("table_additional_css",              False,  "table",            "values",   None),
            OptionsInfo("table_font_names",                  False,  "table",            "values",   default_fonts_list),
            OptionsInfo("table_font_size",                    True,  "table",            "px",       "16px"),
            OptionsInfo("table_font_weight",                  True,  "table",            "value",    "normal"),
            OptionsInfo("table_font_style",                   True,  "table",            "value",    "normal"),
            OptionsInfo("table_font_color",                   True,  "table",            "value",    "#333333"),
            OptionsInfo("table_font_color_light",             True,  "table",            "value",    "#FFFFFF"),
            OptionsInfo("table_border_top_include",          False,  "table",            "boolean",  True),
            OptionsInfo("table_border_top_style",             True,  "table",            "value",    "solid"),
            OptionsInfo("table_border_top_width",             True,  "table",            "px",       "2px"),
            OptionsInfo("table_border_top_color",             True,  "table",            "value",    "#A8A8A8"),
            OptionsInfo("table_border_right_style",           True,  "table",            "value",    "none"),
            OptionsInfo("table_border_right_width",           True,  "table",            "px",       "2px"),
            OptionsInfo("table_border_right_color",           True,  "table",            "value",    "#D3D3D3"),
            OptionsInfo("table_border_bottom_include",       False,  "table",            "boolean",  True),
            OptionsInfo("table_border_bottom_style",          True,  "table",            "value",    "solid"),
            OptionsInfo("table_border_bottom_width",          True,  "table",            "px",       "2px"),
            OptionsInfo("table_border_bottom_color",          True,  "table",            "value",    "#A8A8A8"),
            OptionsInfo("table_border_left_style",            True,  "table",            "value",    "none"),
            OptionsInfo("table_border_left_width",            True,  "table",            "px",       "2px"),
            OptionsInfo("table_border_left_color",            True,  "table",            "value",    "#D3D3D3"),
            OptionsInfo("heading_background_color",           True,  "heading",          "value",    None),
            OptionsInfo("heading_align",                      True,  "heading",          "value",    "center"),
            OptionsInfo("heading_title_font_size",            True,  "heading",          "px",       "125%"),
            OptionsInfo("heading_title_font_weight",          True,  "heading",          "value",    "initial"),
            OptionsInfo("heading_subtitle_font_size",         True,  "heading",          "px",       "85%"),
            OptionsInfo("heading_subtitle_font_weight",       True,  "heading",          "value",    "initial"),
            OptionsInfo("heading_padding",                    True,  "heading",          "px",       "4px"),
            OptionsInfo("heading_padding_horizontal",         True,  "heading",          "px",       "5px"),
            OptionsInfo("heading_border_bottom_style",        True,  "heading",          "value",    "solid"),
            OptionsInfo("heading_border_bottom_width",        True,  "heading",          "px",       "2px"),
            OptionsInfo("heading_border_bottom_color",        True,  "heading",          "value",    "#D3D3D3"),
            OptionsInfo("heading_border_lr_style",            True,  "heading",          "value",    "none"),
            OptionsInfo("heading_border_lr_width",            True,  "heading",          "px",       "1px"),
            OptionsInfo("heading_border_lr_color",            True,  "heading",          "value",    "#D3D3D3"),
            OptionsInfo("column_labels_background_color",     True,  "column_labels",    "value",    None),
            OptionsInfo("column_labels_font_size",            True,  "column_labels",    "px",       "100%"),
            OptionsInfo("column_labels_font_weight",          True,  "column_labels",    "value",    "normal"),
            OptionsInfo("column_labels_text_transform",       True,  "column_labels",    "value",    "inherit"),
            OptionsInfo("column_labels_padding",              True,  "column_labels",    "px",       "5px"),
            OptionsInfo("column_labels_padding_horizontal",   True,  "column_labels",    "px",       "5px"),
            OptionsInfo("column_labels_vlines_style",         True,  "table_body",       "value",    "none"),
            OptionsInfo("column_labels_vlines_width",         True,  "table_body",       "px",       "1px"),
            OptionsInfo("column_labels_vlines_color",         True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("column_labels_border_top_style",     True,  "column_labels",    "value",    "solid"),
            OptionsInfo("column_labels_border_top_width",     True,  "column_labels",    "px",       "2px"),
            OptionsInfo("column_labels_border_top_color",     True,  "column_labels",    "value",    "#D3D3D3"),
            OptionsInfo("column_labels_border_bottom_style",  True,  "column_labels",    "value",    "solid"),
            OptionsInfo("column_labels_border_bottom_width",  True,  "column_labels",    "px",       "2px"),
            OptionsInfo("column_labels_border_bottom_color",  True,  "column_labels",    "value",    "#D3D3D3"),
            OptionsInfo("column_labels_border_lr_style",      True,  "column_labels",    "value",    "none"),
            OptionsInfo("column_labels_border_lr_width",      True,  "column_labels",    "px",       "1px"),
            OptionsInfo("column_labels_border_lr_color",      True,  "column_labels",    "value",    "#D3D3D3"),
            OptionsInfo("column_labels_hidden",              False,  "column_labels",    "boolean",  False),
            OptionsInfo("row_group_background_color",         True,  "row_group",        "value",    None),
            OptionsInfo("row_group_font_size",                True,  "row_group",        "px",       "100%"),
            OptionsInfo("row_group_font_weight",              True,  "row_group",        "value",    "initial"),
            OptionsInfo("row_group_text_transform",           True,  "row_group",        "value",    "inherit"),
            OptionsInfo("row_group_padding",                  True,  "row_group",        "px",       "8px"),
            OptionsInfo("row_group_padding_horizontal",       True,  "row_group",        "px",       "5px"),
            OptionsInfo("row_group_border_top_style",         True,  "row_group",        "value",    "solid"),
            OptionsInfo("row_group_border_top_width",         True,  "row_group",        "px",       "2px"),
            OptionsInfo("row_group_border_top_color",         True,  "row_group",        "value",    "#D3D3D3"),
            OptionsInfo("row_group_border_right_style",       True,  "row_group",        "value",    "none"),
            OptionsInfo("row_group_border_right_width",       True,  "row_group",        "px",       "1px"),
            OptionsInfo("row_group_border_right_color",       True,  "row_group",        "value",    "#D3D3D3"),
            OptionsInfo("row_group_border_bottom_style",      True,  "row_group",        "value",    "solid"),
            OptionsInfo("row_group_border_bottom_width",      True,  "row_group",        "px",       "2px"),
            OptionsInfo("row_group_border_bottom_color",      True,  "row_group",        "value",    "#D3D3D3"),
            OptionsInfo("row_group_border_left_style",        True,  "row_group",        "value",    "none"),
            OptionsInfo("row_group_border_left_width",        True,  "row_group",        "px",       "1px"),
            OptionsInfo("row_group_border_left_color",        True,  "row_group",        "value",    "#D3D3D3"),
            OptionsInfo("row_group_default_label",           False,  "row_group",        "value",    None),
            OptionsInfo("row_group_as_column",               False,  "row_group",        "boolean",  False),
            OptionsInfo("table_body_hlines_style",            True,  "table_body",       "value",    "solid"),
            OptionsInfo("table_body_hlines_width",            True,  "table_body",       "px",       "1px"),
            OptionsInfo("table_body_hlines_color",            True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("table_body_vlines_style",            True,  "table_body",       "value",    "none"),
            OptionsInfo("table_body_vlines_width",            True,  "table_body",       "px",       "1px"),
            OptionsInfo("table_body_vlines_color",            True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("table_body_border_top_style",        True,  "table_body",       "value",    "solid"),
            OptionsInfo("table_body_border_top_width",        True,  "table_body",       "px",       "2px"),
            OptionsInfo("table_body_border_top_color",        True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("table_body_border_bottom_style",     True,  "table_body",       "value",    "solid"),
            OptionsInfo("table_body_border_bottom_width",     True,  "table_body",       "px",       "2px"),
            OptionsInfo("table_body_border_bottom_color",     True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("data_row_padding",                   True,  "data_row",         "px",       "8px"),
            OptionsInfo("data_row_padding_horizontal",        True,  "data_row",         "px",       "5px"),
            OptionsInfo("stub_background_color",              True,  "stub",             "value",    None),
            OptionsInfo("stub_font_size",                     True,  "stub",             "px",       "100%"),
            OptionsInfo("stub_font_weight",                   True,  "stub",             "value",    "initial"),
            OptionsInfo("stub_text_transform",                True,  "stub",             "value",    "inherit"),
            OptionsInfo("stub_border_style",                  True,  "stub",             "value",    "solid"),
            OptionsInfo("stub_border_width",                  True,  "stub",             "px",       "2px"),
            OptionsInfo("stub_border_color",                  True,  "stub",             "value",    "#D3D3D3"),
            OptionsInfo("stub_row_group_background_color",    True,  "stub",             "value",    None),
            OptionsInfo("stub_row_group_font_size",           True,  "stub",             "px",       "100%"),
            OptionsInfo("stub_row_group_font_weight",         True,  "stub",             "value",    "initial"),
            OptionsInfo("stub_row_group_text_transform",      True,  "stub",             "value",    "inherit"),
            OptionsInfo("stub_row_group_border_style",        True,  "stub",             "value",    "solid"),
            OptionsInfo("stub_row_group_border_width",        True,  "stub",             "px",       "2px"),
            OptionsInfo("stub_row_group_border_color",        True,  "stub",             "value",    "#D3D3D3"),
            OptionsInfo("summary_row_padding",                True,  "summary_row",      "px",       "8px"),
            OptionsInfo("summary_row_padding_horizontal",     True,  "summary_row",      "px",       "5px"),
            OptionsInfo("summary_row_background_color",       True,  "summary_row",      "value",    None),
            OptionsInfo("summary_row_text_transform",         True,  "summary_row",      "value",    "inherit"),
            OptionsInfo("summary_row_border_style",           True,  "summary_row",      "value",    "solid"),
            OptionsInfo("summary_row_border_width",           True,  "summary_row",      "px",       "2px"),
            OptionsInfo("summary_row_border_color",           True,  "summary_row",      "value",    "#D3D3D3"),
            OptionsInfo("grand_summary_row_padding",          True,  "grand_summary_row", "px",      "8px"),
            OptionsInfo("grand_summary_row_padding_horizontal",True, "grand_summary_row", "px",      "5px"),
            OptionsInfo("grand_summary_row_background_color", True,  "grand_summary_row", "value",   None),
            OptionsInfo("grand_summary_row_text_transform",   True,  "grand_summary_row", "value",   "inherit"),
            OptionsInfo("grand_summary_row_border_style",     True,  "grand_summary_row", "value",   "double"),
            OptionsInfo("grand_summary_row_border_width",     True,  "grand_summary_row", "px",      "6px"),
            OptionsInfo("grand_summary_row_border_color",     True,  "grand_summary_row", "value",   "#D3D3D3"),
            OptionsInfo("footnotes_font_size",                True,  "footnotes",        "px",       "90%"),
            OptionsInfo("footnotes_padding",                  True,  "footnotes",        "px",       "4px"),
            OptionsInfo("footnotes_padding_horizontal",       True,  "footnotes",        "px",       "5px"),
            OptionsInfo("footnotes_background_color",         True,  "footnotes",        "value",    None),
            OptionsInfo("footnotes_margin",                   True,  "footnotes",        "px",       "0px"),
            OptionsInfo("footnotes_border_bottom_style",      True,  "footnotes",        "value",    "none"),
            OptionsInfo("footnotes_border_bottom_width",      True,  "footnotes",        "px",       "2px"),
            OptionsInfo("footnotes_border_bottom_color",      True,  "footnotes",        "value",    "#D3D3D3"),
            OptionsInfo("footnotes_border_lr_style",          True,  "footnotes",        "value",    "none"),
            OptionsInfo("footnotes_border_lr_width",          True,  "footnotes",        "px",       "2px"),
            OptionsInfo("footnotes_border_lr_color",          True,  "footnotes",        "value",    "#D3D3D3"),
            OptionsInfo("footnotes_marks" ,                  False,  "footnotes",        "values",   "numbers"),
            OptionsInfo("footnotes_multiline",               False,  "footnotes",        "boolean",  True),
            OptionsInfo("footnotes_sep",                     False,  "footnotes",        "value",    " "),
            OptionsInfo("source_notes_padding",               True,  "source_notes",     "px",       "4px"),
            OptionsInfo("source_notes_padding_horizontal",    True,  "source_notes",     "px",       "5px"),
            OptionsInfo("source_notes_background_color",      True,  "source_notes",     "value",    None),
            OptionsInfo("source_notes_font_size",             True,  "source_notes",     "px",       "90%"),
            OptionsInfo("source_notes_border_bottom_style",   True,  "source_notes",     "value",    "none"),
            OptionsInfo("source_notes_border_bottom_width",   True,  "source_notes",     "px",       "2px"),
            OptionsInfo("source_notes_border_bottom_color",   True,  "source_notes",     "value",    "#D3D3D3"),
            OptionsInfo("source_notes_border_lr_style",       True,  "source_notes",     "value",    "none"),
            OptionsInfo("source_notes_border_lr_width",       True,  "source_notes",     "px",       "2px"),
            OptionsInfo("source_notes_border_lr_color",       True,  "source_notes",     "value",    "#D3D3D3"),
            OptionsInfo("source_notes_multiline",            False,  "source_notes",     "boolean",  True),
            OptionsInfo("source_notes_sep",                  False,  "source_notes",     "value",    " "),
            OptionsInfo("row_striping_background_color",      True,  "row",              "value",    "rgba(128,128,128,0.05)"),
            OptionsInfo("row_striping_include_stub",         False,  "row",              "boolean",  False),
            OptionsInfo("row_striping_include_table_body",   False,  "row",              "boolean",  False),
            OptionsInfo("page_orientation",                  False,  "page",             "value",    "portrait"),
            OptionsInfo("page_numbering",                    False,  "page",             "boolean",  False),
            OptionsInfo("page_header_use_tbl_headings",      False,  "page",             "boolean",  False),
            OptionsInfo("page_footer_use_tbl_notes",         False,  "page",             "boolean",  False),
            OptionsInfo("page_width",                        False,  "page",             "value",    "8.5in"),
            OptionsInfo("page_height",                       False,  "page",             "value",    "11.0in"),
            OptionsInfo("page_margin_left",                  False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_margin_right",                 False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_margin_top",                   False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_margin_bottom",                False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_header_height",                False,  "page",             "value",    "0.5in"),
            OptionsInfo("page_footer_height",                False,  "page",             "value",    "0.5in"),
        ])
# fmt: on

    def _get_all_options_keys(self) -> List[Union[str, None]]:
        return [x.parameter for x in self._options.values()]

    #def __setattr__(self, __name: str, __value: Any) -> None:
    #    self._options[__name].value = __value

    def __getattr__(self, __name: str) -> OptionsInfo:
        return self._options[__name]
        # use this like
        #
        # options = Options()
        # options.foo.value = "bar"
        # print(options.foo.type)

    #def _get_option_type(self, option: str) -> Union[Any, List[str]]:
    #    return self._options[option].type

    def _get_option_value(self, option: str) -> Union[Any, List[str]]:
        return self._options[option].value

    def _set_option_value(self, option: str, value: Any):
       self._options[option].value = value
       return self


class OptionsAPI:
    def tab_options(
            self,
            container_width: Optional[str] = None,
            container_height: Optional[str] = None,
            container_overflow_x: Optional[str] = None,
            container_overflow_y: Optional[str] = None,
            table_width: Optional[str] = None,
            table_layout: Optional[str] = None,
            table_align: Optional[str] = None,
            table_margin_left: Optional[str] = None,
            table_margin_right: Optional[str] = None,
            table_background_color: Optional[str] = None,
            table_additional_css: Optional[str] = None,
            table_font_names: Optional[str] = None,
            table_font_size: Optional[str] = None,
            table_font_weight: Optional[str] = None,
            table_font_style: Optional[str] = None,
            table_font_color: Optional[str] = None,
            table_font_color_light: Optional[str] = None,
            table_border_top_style: Optional[str] = None,
            table_border_top_width: Optional[str] = None,
            table_border_top_color: Optional[str] = None,
            table_border_right_style: Optional[str] = None,
            table_border_right_width: Optional[str] = None,
            table_border_right_color: Optional[str] = None,
            table_border_bottom_style: Optional[str] = None,
            table_border_bottom_width: Optional[str] = None,
            table_border_bottom_color: Optional[str] = None,
            table_border_left_style: Optional[str] = None,
            table_border_left_width: Optional[str] = None,
            table_border_left_color: Optional[str] = None,
            heading_background_color: Optional[str] = None,
            heading_align: Optional[str] = None,
            heading_title_font_size: Optional[str] = None,
            heading_title_font_weight: Optional[str] = None,
            heading_subtitle_font_size: Optional[str] = None,
            heading_subtitle_font_weight: Optional[str] = None,
            heading_padding: Optional[str] = None,
            heading_padding_horizontal: Optional[str] = None,
            heading_border_bottom_style: Optional[str] = None,
            heading_border_bottom_width: Optional[str] = None,
            heading_border_bottom_color: Optional[str] = None,
            heading_border_lr_style: Optional[str] = None,
            heading_border_lr_width: Optional[str] = None,
            heading_border_lr_color: Optional[str] = None,
            column_labels_background_color: Optional[str] = None,
            column_labels_font_size: Optional[str] = None,
            column_labels_font_weight: Optional[str] = None,
            column_labels_text_transform: Optional[str] = None,
            column_labels_padding: Optional[str] = None,
            column_labels_padding_horizontal: Optional[str] = None,
            column_labels_vlines_style: Optional[str] = None,
            column_labels_vlines_width: Optional[str] = None,
            column_labels_vlines_color: Optional[str] = None,
            column_labels_border_top_style: Optional[str] = None,
            column_labels_border_top_width: Optional[str] = None,
            column_labels_border_top_color: Optional[str] = None,
            column_labels_border_bottom_style: Optional[str] = None,
            column_labels_border_bottom_width: Optional[str] = None,
            column_labels_border_bottom_color: Optional[str] = None,
            column_labels_border_lr_style: Optional[str] = None,
            column_labels_border_lr_width: Optional[str] = None,
            column_labels_border_lr_color: Optional[str] = None,
            column_labels_hidden: Optional[bool] = None,
            row_group_background_color: Optional[str] = None,
            row_group_font_size: Optional[str] = None,
            row_group_font_weight: Optional[str] = None,
            row_group_text_transform: Optional[str] = None,
            row_group_padding: Optional[str] = None,
            row_group_padding_horizontal: Optional[str] = None,
            row_group_border_top_style: Optional[str] = None,
            row_group_border_top_width: Optional[str] = None,
            row_group_border_top_color: Optional[str] = None,
            row_group_border_bottom_style: Optional[str] = None,
            row_group_border_bottom_width: Optional[str] = None,
            row_group_border_bottom_color: Optional[str] = None,
            row_group_border_left_style: Optional[str] = None,
            row_group_border_left_width: Optional[str] = None,
            row_group_border_left_color: Optional[str] = None,
            row_group_border_right_style: Optional[str] = None,
            row_group_border_right_width: Optional[str] = None,
            row_group_border_right_color: Optional[str] = None,
            row_group_default_label: Optional[str] = None,
            row_group_as_column: Optional[bool] = None,
            table_body_hlines_style: Optional[str] = None,
            table_body_hlines_width: Optional[str] = None,
            table_body_hlines_color: Optional[str] = None,
            table_body_vlines_style: Optional[str] = None,
            table_body_vlines_width: Optional[str] = None,
            table_body_vlines_color: Optional[str] = None,
            table_body_border_top_style: Optional[str] = None,
            table_body_border_top_width: Optional[str] = None,
            table_body_border_top_color: Optional[str] = None,
            table_body_border_bottom_style: Optional[str] = None,
            table_body_border_bottom_width: Optional[str] = None,
            table_body_border_bottom_color: Optional[str] = None,
            stub_background_color: Optional[str] = None,
            stub_font_size: Optional[str] = None,
            stub_font_weight: Optional[str] = None,
            stub_text_transform: Optional[str] = None,
            stub_border_style: Optional[str] = None,
            stub_border_width: Optional[str] = None,
            stub_border_color: Optional[str] = None,
            stub_row_group_font_size: Optional[str] = None,
            stub_row_group_font_weight: Optional[str] = None,
            stub_row_group_text_transform: Optional[str] = None,
            stub_row_group_border_style: Optional[str] = None,
            stub_row_group_border_width: Optional[str] = None,
            stub_row_group_border_color: Optional[str] = None,
            data_row_padding: Optional[str] = None,
            data_row_padding_horizontal: Optional[str] = None,
            summary_row_background_color: Optional[str] = None,
            summary_row_text_transform: Optional[str] = None,
            summary_row_padding: Optional[str] = None,
            summary_row_padding_horizontal: Optional[str] = None,
            summary_row_border_style: Optional[str] = None,
            summary_row_border_width: Optional[str] = None,
            summary_row_border_color: Optional[str] = None,
            grand_summary_row_background_color: Optional[str] = None,
            grand_summary_row_text_transform: Optional[str] = None,
            grand_summary_row_padding: Optional[str] = None,
            grand_summary_row_padding_horizontal: Optional[str] = None,
            grand_summary_row_border_style: Optional[str] = None,
            grand_summary_row_border_width: Optional[str] = None,
            grand_summary_row_border_color: Optional[str] = None,
            footnotes_background_color: Optional[str] = None,
            footnotes_font_size: Optional[str] = None,
            footnotes_padding: Optional[str] = None,
            footnotes_padding_horizontal: Optional[str] = None,
            footnotes_border_bottom_style: Optional[str] = None,
            footnotes_border_bottom_width: Optional[str] = None,
            footnotes_border_bottom_color: Optional[str] = None,
            footnotes_border_lr_style: Optional[str] = None,
            footnotes_border_lr_width: Optional[str] = None,
            footnotes_border_lr_color: Optional[str] = None,
            footnotes_marks: Optional[Union[str, List[str]]] = None,
            footnotes_multiline: Optional[bool] = None,
            footnotes_sep: Optional[str] = None,
            source_notes_background_color: Optional[str] = None,
            source_notes_font_size: Optional[str] = None,
            source_notes_padding: Optional[str] = None,
            source_notes_padding_horizontal: Optional[str] = None,
            source_notes_border_bottom_style: Optional[str] = None,
            source_notes_border_bottom_width: Optional[str] = None,
            source_notes_border_bottom_color: Optional[str] = None,
            source_notes_border_lr_style: Optional[str] = None,
            source_notes_border_lr_width: Optional[str] = None,
            source_notes_border_lr_color: Optional[str] = None,
            source_notes_multiline: Optional[bool] = None,
            source_notes_sep: Optional[str] = None,
            row_striping_background_color: Optional[str] = None,
            row_striping_include_stub: Optional[bool] = None,
            row_striping_include_table_body: Optional[bool] = None,
            page_orientation: Optional[str] = None,
            page_numbering: Optional[bool] = None,
            page_header_use_tbl_headings: Optional[bool] = None,
            page_footer_use_tbl_notes: Optional[bool] = None,
            page_width: Optional[str] = None,
            page_height: Optional[str] = None,
            page_margin_left: Optional[str] = None,
            page_margin_right: Optional[str] = None,
            page_margin_top: Optional[str] = None,
            page_margin_bottom: Optional[str] = None,
            page_header_height: Optional[str] = None,
            page_footer_height: Optional[str] = None,
    ):
        """
        Modify the table output options

        Modify the options available in a table. These options are named by the
        components, the subcomponents, and the element that can adjusted.

        Parameters
        ----------
        container_width,container_height
            The width and height of the table's container. Can be specified as
            a single-length character with units of pixels or as a percentage.
            If provided as a scalar numeric value, it is assumed that the
            value is given in units of pixels. The `px()` and `pct()` helper
            functions can also be used to pass in numeric values and obtain values
            as pixel or percent units.

        container_overflow_x,container_overflow_y
            Options to enable scrolling in the horizontal and vertical directions
            when the table content overflows the container dimensions. Using `True`
            (the default for both) means that horizontal or vertical scrolling is
            enabled to view the entire table in those directions. With `False`, the
            table may be clipped if the table width or height exceeds the
            `container_width` or `container_height`.

         table_width
            The width of the table. Can be specified as a single-length character
            with units of pixels or as a percentage. If provided as a scalar
            numeric value, it is assumed that the value is given in units of pixels.
            The `px()` and `pct()` helper functions can also be used to pass in
            numeric values and obtain values as pixel or percent units.

         table_layout
            The value for the `table-layout` CSS style in the HTML output context.
            By default, this is `"fixed"` but another valid option is `"auto"`.

         table_align
            The horizontal alignment of the table in its container. By default, this
            is `"center"`. Other options are `"left"` and `"right"`. This will
            automatically set `table_margin_left` and `table_margin_right` to the
            appropriate values.

         table_margin_left,table_margin_right
            The size of the margins on the left and right of the table within the
            container. Can be specified as a single-length character with units of
            pixels or as a percentage. If provided as a scalar numeric value, it is
            assumed that the value is given in units of pixels. The `px()` and
            `pct()` helper functions can also be used to pass in numeric values and
            obtain values as pixel or percent units. Using `table_margin_left` or
            `table_margin_right` will overwrite any values set by `table_align`.

         table_background_color,heading_background_color,column_labels_background_color,row_group_background_color,stub_background_color,summary_row_background_color,grand_summary_row_background_color,footnotes_background_color,source_notes_background_color
           Background colors for the parent element `table` and the following child
           elements: `heading`, `column_labels`, `row_group`, `stub`, `summary_row`,
           `grand_summary_row`, `footnotes`, and `source_notes`. A color name or a
           hexadecimal color code should be provided.

         table_additional_css
            This option can be used to supply an additional block of CSS rules to be
            applied after the automatically generated table CSS.

         table_font_names
            The names of the fonts used for the table. This should be provided as a
            list of font names. If the first font isn't available, then the next font
            is tried (and so on).

         table_font_style
            The font style for the table. Can be one of either `"normal"`, `"italic"`,
            or `"oblique"`.

         table_font_color,table_font_color_light
            The text color used throughout the table. There are two variants:
            `table_font_color` is for text overlaid on lighter background colors, and
            `table_font_color_light` is automatically used when text needs to be
            overlaid on darker background colors. A color name or a hexadecimal color
            code should be provided.

         table_font_size,heading_title_font_size,heading_subtitle_font_size,column_labels_font_size,row_group_font_size,stub_font_size,footnotes_font_size,source_notes_font_size
            The font sizes for the parent text element `table` and the following child
            elements: `heading_title`, `heading_subtitle`, `column_labels`,
            `row_group`, `footnotes`, and `source_notes`. Can be specified as a
            string with units of pixels (e.g., `"12px"`) or as a percentage (e.g.,
            `"80%"`). If provided as a scalar numeric value, it is assumed that the
            value is given in units of pixels. The `px()` and `pct()` helper
            functions can also be used to pass in numeric values and obtain values
            as pixel or percentage units.

         heading_align
            Controls the horizontal alignment of the heading title and subtitle. We can
            either use `"center"`, `"left"`, or `"right"`.

         table_font_weight,heading_title_font_weight,heading_subtitle_font_weight,column_labels_font_weight,row_group_font_weight,stub_font_weight
            The font weights of the table, `heading_title`, `heading_subtitle`,
            `column_labels`, `row_group`, and `stub` text elements. Can be a text-based
            keyword such as `"normal"`, `"bold"`, `"lighter"`, `"bolder"`, or, a
            numeric value between `1` and `1000`, inclusive. Note that only variable
            fonts may support the numeric mapping of weight.

         column_labels_text_transform,row_group_text_transform,stub_text_transform,summary_row_text_transform,grand_summary_row_text_transform
            Options to apply text transformations to the `column_labels`, `row_group`,
            `stub`, `summary_row`, and `grand_summary_row` text elements. Either of the
            `"uppercase"`, `"lowercase"`, or `"capitalize"` keywords can be used.

         heading_padding,column_labels_padding,data_row_padding,row_group_padding,summary_row_padding,grand_summary_row_padding,footnotes_padding,source_notes_padding
            The amount of vertical padding to incorporate in the `heading` (title and
            subtitle), the `column_labels` (this includes the column spanners), the row
            group labels (`row_group_padding`), in the body/stub rows
            (`data_row_padding`), in summary rows (`summary_row_padding` or
            `grand_summary_row_padding`), or in the footnotes and source notes
            (`footnotes_padding` and `source_notes_padding`).

         heading_padding_horizontal,column_labels_padding_horizontal,data_row_padding_horizontal,row_group_padding_horizontal,summary_row_padding_horizontal,grand_summary_row_padding_horizontal,footnotes_padding_horizontal,source_notes_padding_horizontal
            The amount of horizontal padding to incorporate in the `heading` (title and
            subtitle), the `column_labels` (this includes the column spanners), the row
            group labels (`row_group_padding_horizontal`), in the body/stub rows
            (`data_row_padding`), in summary rows (`summary_row_padding_horizontal` or
            `grand_summary_row_padding_horizontal`), or in the footnotes and source
            notes (`footnotes_padding_horizontal` and `source_notes_padding_horizontal`).

         table_border_top_style,table_border_top_width,table_border_top_color,table_border_right_style,table_border_right_width,table_border_right_color,table_border_bottom_style,table_border_bottom_width,table_border_bottom_color,table_border_left_style,table_border_left_width,table_border_left_color
            The style, width, and color properties of the table's absolute top and
            absolute bottom borders.

         heading_border_bottom_style,heading_border_bottom_width,heading_border_bottom_color
            The style, width, and color properties of the header's bottom border. This
            border shares space with that of the `column_labels` location. If the
            `width` of this border is larger, then it will be the visible border.

         heading_border_lr_style,heading_border_lr_width,heading_border_lr_color
            The style, width, and color properties for the left and right borders of
            the `heading` location.

         column_labels_vlines_style,column_labels_vlines_width,column_labels_vlines_color
            The style, width, and color properties for all vertical lines ('vlines')
            of the the `column_labels`.

         column_labels_border_top_style,column_labels_border_top_width,column_labels_border_top_color
            The style, width, and color properties for the top border of the
            `column_labels` location. This border shares space with that of the
            `heading` location. If the `width` of this border is larger, then it will
            be the visible border.

         column_labels_border_bottom_style,column_labels_border_bottom_width,column_labels_border_bottom_color
            The style, width, and color properties for the bottom border of the
            `column_labels` location.

         column_labels_border_lr_style,column_labels_border_lr_width,column_labels_border_lr_color
            The style, width, and color properties for the left and right borders of
            the `column_labels` location.

         column_labels_hidden
            An option to hide the column labels. If providing `TRUE` then the entire
            `column_labels` location won't be seen and the table header (if present)
            will collapse downward.

         row_group_border_top_style,row_group_border_top_width,row_group_border_top_color,row_group_border_bottom_style,row_group_border_bottom_width,row_group_border_bottom_color,row_group_border_left_style,row_group_border_left_width,row_group_border_left_color,row_group_border_right_style,row_group_border_right_width,row_group_border_right_color
            The style, width, and color properties for all top, bottom, left, and right
            borders of the `row_group` location.

         table_body_hlines_style,table_body_hlines_width,table_body_hlines_color,table_body_vlines_style,table_body_vlines_width,table_body_vlines_color
            The style, width, and color properties for all horizontal lines ('hlines')
            and vertical lines ('vlines') in the `table_body`.

         table_body_border_top_style,table_body_border_top_width,table_body_border_top_color,table_body_border_bottom_style,table_body_border_bottom_width,table_body_border_bottom_color
            The style, width, and color properties for all top and bottom borders of
            the `table_body` location.

         stub_border_style,stub_border_width,stub_border_color
            The style, width, and color properties for the vertical border of the table
            stub.

         stub_row_group_font_size,stub_row_group_font_weight,stub_row_group_text_transform,stub_row_group_border_style,stub_row_group_border_width,stub_row_group_border_color
            Options for the row group column in the stub (made possible when using
            `row_group_as_column = TRUE`). The defaults for these options mirror that
            of the `stub.*` variants (except for `stub_row_group_border_width`, which
            is `"1px"` instead of `"2px"`).

         row_group_default_label
            An option to set a default row group label for any rows not formally placed
            in a row group named by `group` in any call of `tab_row_group()`. If this
            is set as `None` and there are rows that haven't been placed into
            a row group (where one or more row groups already exist), those rows will
            be automatically placed into a row group without a label.

         row_group_as_column
            How should row groups be structured? By default, they are separate rows
            that lie above the each of the groups. Setting this to `True` will
            structure row group labels are columns to the far left of the table.

         summary_row_border_style,summary_row_border_width,summary_row_border_color
            The style, width, and color properties for all horizontal borders of the
            `summary_row` location.

         grand_summary_row_border_style,grand_summary_row_border_width,grand_summary_row_border_color
            The style, width, and color properties for the top borders of the
            `grand_summary_row` location.

         footnotes_border_bottom_style,footnotes_border_bottom_width,footnotes_border_bottom_color
            The style, width, and color properties for the bottom border of the
            `footnotes` location.

         footnotes_border_lr_style,footnotes_border_lr_width,footnotes_border_lr_color
            The style, width, and color properties for the left and right borders of
            the `footnotes` location.

         footnotes_marks
            The set of sequential marks used to reference and identify each of the
            footnotes (same input as the [opt_footnote_marks()] function. We can
            supply a list that represents the series of footnote marks. This
            list is recycled when its usage goes beyond the length of the set. At
            each cycle, the marks are simply combined (e.g., `*` -> `**` ->
            `***`). The option exists for providing keywords for certain types of
            footnote marks. The keyword `"numbers"` (the default, indicating that we
            want to use numeric marks). We can use lowercase `"letters"` or uppercase
            `"LETTERS"`. There is the option for using a traditional symbol set where
            `"standard"` provides four symbols, and, `"extended"` adds two more
            symbols, making six.

         footnotes_multiline,source_notes_multiline
            An option to either put footnotes and source notes in separate lines
            (the default, or `True`) or render them as a continuous line of text
            with `footnotes_sep` providing the separator (by default `" "`) between
            notes.

         footnotes_sep,source_notes_sep
            The separating characters between adjacent footnotes and source notes
            in their respective footer sections when rendered as a continuous
            line of text (when `footnotes_multiline is False`). The default value
            is a single space character (`" "`).

         source_notes_border_bottom_style,source_notes_border_bottom_width,source_notes_border_bottom_color
            The style, width, and color properties for the bottom border of the
            `source_notes` location.

         source_notes_border_lr_style,source_notes_border_lr_width,source_notes_border_lr_color
            The style, width, and color properties for the left and right borders of
            the `source_notes` location.

         row_striping_background_color
            The background color for striped table body rows. A color name or a
            hexadecimal color code should be provided.

         row_striping_include_stub
            An option for whether to include the stub when striping rows.

         row_striping_include_table_body
            An option for whether to include the table body when striping rows.

         page_orientation
            For RTF output, this provides an two options for page orientation:
            `"portrait"` (the default) and `"landscape"`.

         page_numbering
            Within RTF output, should page numbering be displayed? By default,
            this is set to `False` but if `True` then page numbering text will be
            added to the document header.

         page_header_use_tbl_headings
            If `True` then RTF output tables will migrate all table headings
            (including the table title and all column labels) to the page header.
            This page header content will repeat across pages. By default, this is
            `False`.

         page_footer_use_tbl_notes
            If `True` then RTF output tables will migrate all table footer content
            (this includes footnotes and source notes) to the page footer. This page
            footer content will repeat across pages. By default, this is `False`.

         page_width,page_height
            The page width and height in the standard portrait orientation. This is
            for RTF table output and the default values (in inches) are `8.5in` and
            `11.0in`.

         page_margin_left,page_margin_right,page_margin_top,page_margin_bottom
            For RTF table output, these options correspond to the left, right, top, and
            bottom page margins. The default values for each of these is `1.0in`.

         page_header_height,page_footer_height
            The heights of the page header and footer for RTF table outputs. Default
            values for both are `0.5in`.

        Returns
        -------

        GT
            Result of the table operation.
        """
        saved_args = locals()

        del saved_args["self"]

        modified_args = {k: v for k, v in saved_args.items() if v is not None}

        for i in range(len(modified_args)):
            self._options._set_option_value(
                option=list(modified_args.keys())[i],
                value=list(modified_args.values())[i]
            )

        return self


    def opt_footnote_marks(self, marks: Union[str, List[str]] = "numbers"):
        """
        Option to modify the set of footnote marks.

        Alter the footnote marks for any footnotes that may be present in the table.
        Either a list of marks can be provided (including Unicode characters), or,
        a specific keyword could be used to signify a preset sequence. This function
        serves as a shortcut for using `tab_options(footnotes_marks = <marks>)`

        We can supply a list of strings will represent the series of marks.
        The series of footnote marks is recycled when its usage goes beyond the
        length of the set. At each cycle, the marks are simply doubled, tripled, and
        so on (e.g., `*` -> `**` -> `***`). The option exists for providing keywords
        for certain types of footnote marks. The keywords are:

        - `"numbers"`: numeric marks, they begin from 1 and these marks are not
        subject to recycling behavior
        - `"letters"`: lowercase alphabetic marks. Same as using the `gt.letters()`
        function which produces a list of 26 lowercase letters from the Roman
        alphabet
        - `"LETTERS"`: uppercase alphabetic marks. Same as using the `gt.LETTERS()`
        function which produces a list of 26 uppercase letters from the Roman
        alphabet
        - `"standard"`: symbolic marks, four symbols in total
        - `"extended"`: symbolic marks, extends the standard set by adding two
        more symbols, making six

        Parameters
        ----------

        marks
            Either a list of strings that will represent the series of marks or a
            keyword string that represents a preset sequence of marks. The valid
            keywords are: `"numbers"` (for numeric marks), `"letters"` and `"LETTERS"`
            (for lowercase and uppercase alphabetic marks), `"standard"` (for a
            traditional set of four symbol marks), and `"extended"` (which adds two
            more symbols to the standard set).

        Returns
        -------

        GT
            Result of the table operation.
        """
        # Validate the marks keyword passed in as a string
        if marks is str:
            marks = _utils._match_arg(
                x=cast(str, marks),
                lst=["numbers", "letters", "LETTERS", "standard", "extended"],
            )

        self.tab_options(footnotes_marks=marks)
        return self


    def opt_row_striping(self, row_striping: bool = True):
        """
        Option to add or remove row striping.

        By default, a gt*table does not have row striping enabled. However, this
        method allows us to easily enable or disable striped rows in the table
        body. It's a convenient shortcut for
        `gt.tab_options(row_striping_include_table_body = <True|False>)`.

        Parameters
        ----------

        row_striping (bool):
            A boolean that indicates whether row striping should be added or
            removed. Defaults to True.

        Returns
        -------

        GT
            Result of the table operation.
        """
        self.tab_options(row_striping_include_table_body=row_striping)
        return self


    def opt_align_table_header(self, align: str = "center"):
        """
        Option to align the table header.

        By default, a table header added to a gt table has center alignment
        for both the title and the subtitle elements. This function allows us to
        easily set the horizontal alignment of the title and subtitle to the left
        or right by using the `"align"` argument. This function serves as a
        convenient shortcut for `gt.tab_options(heading.align = <align>)`.

        Parameters
        ----------

        align (str):
            The alignment of the title and subtitle elements in the table
            header. Options are `"center"` (the default), `"left"`, or
            `"right"`.

        Returns
        -------

        GT
            Result of the table operation.
        """

        align = _utils._match_arg(x=align, lst=["left", "center", "right"])

        self.tab_options(heading_align=align)
        return self

    # TODO: create the `opt_vertical_padding()` function

    # TODO: create the `opt_horizontal_padding()` function

    def opt_all_caps(
        self,
        all_caps: bool = True,
        locations: Union[str, List[str]] = ["column_labels", "stub", "row_group"],
    ):
        """
        Option to use all caps in select table locations.

        Sometimes an all-capitalized look is suitable for a table. By using
        `opt_all_caps()`, we can transform characters in the column labels,
        the stub, and in all row groups in this way (and there's control over which
        of these locations are transformed). This function serves as a convenient
        shortcut for `tab_options(<location>.text_transform="uppercase",
        <location>.font.size=gt.pct(80), <location>.font.weight="bolder")` (for
        all `locations` selected).

        Parameters
        ----------

        all_caps (bool):
            Indicates whether the text transformation to all caps should be
            performed (`True`, the default) or reset to default values (`False`)
            for the `locations` targeted.

        locations (list(str)):
            Which locations should undergo this text transformation? By default it
            includes all of the `"column_labels"`, the `"stub"`, and the
            `"row_group"` locations. However, we could just choose one or two
            of those.

        Returns
        -------

        GT
            Result of the table operation.
        """

        # If providing a scalar string value, normalize it to be in a list
        if type(locations).__name__ != "list":
            locations = _utils._str_scalar_to_list(cast(str, locations))

        # Ensure that the `locations` value is a list of strings
        _utils._assert_str_list(locations)

        # TODO: Ensure that all values within `locations` are valid

        # Set new options for `locations` selected, or, reset to default options
        # if `all_caps` is False
        if all_caps is True:
            if "column_labels" in locations:
                self.tab_options(column_labels_font_size="80%")
                self.tab_options(column_labels_font_weight="bolder")
                self.tab_options(column_labels_text_transform="uppercase")

            if "stub" in locations:
                self.tab_options(stub_font_size="80%")
                self.tab_options(stub_font_weight="bolder")
                self.tab_options(stub_text_transform="uppercase")

            if "row_group" in locations:
                self.tab_options(row_group_font_size="80%")
                self.tab_options(row_group_font_weight="bolder")
                self.tab_options(row_group_text_transform="uppercase")

        else:
            self.tab_options(column_labels_font_size="100%")
            self.tab_options(column_labels_font_weight="normal")
            self.tab_options(column_labels_text_transform="inherit")
            self.tab_options(stub_font_size="100%")
            self.tab_options(stub_font_weight="initial")
            self.tab_options(stub_text_transform="inherit")
            self.tab_options(row_group_font_size="100%")
            self.tab_options(row_group_font_weight="initial")
            self.tab_options(row_group_text_transform="inherit")

        return self

    # TODO: create the `opt_table_lines()` function

    # TODO: create the `opt_table_outline()` function

    # TODO: create the `opt_table_font()` function

    # TODO: create the `opt_css()` function

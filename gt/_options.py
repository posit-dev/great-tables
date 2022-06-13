from typing import Optional, Union, List, Any

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
    parameter: Optional[str]
    scss: Optional[bool]
    category: Optional[str]
    type: Optional[str]
    value: Optional[Union[Any, List[str]]]

    def __init__(
        self,
        parameter: Optional[str] = None,
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
        self._options: list[OptionsInfo] = [
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
            OptionsInfo("table_border_top_include",          False,  "table",            "logical",  True),
            OptionsInfo("table_border_top_style",             True,  "table",            "value",    "solid"),
            OptionsInfo("table_border_top_width",             True,  "table",            "px",       "2px"),
            OptionsInfo("table_border_top_color",             True,  "table",            "value",    "#A8A8A8"),
            OptionsInfo("table_border_right_style",           True,  "table",            "value",    "none"),
            OptionsInfo("table_border_right_width",           True,  "table",            "px",       "2px"),
            OptionsInfo("table_border_right_color",           True,  "table",            "value",    "#D3D3D3"),
            OptionsInfo("table_border_bottom_include",       False,  "table",            "logical",  True),
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
            OptionsInfo("column_labels_hidden",              False,  "column_labels",    "logical",  False),
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
            OptionsInfo("row_group_as_column",               False,  "row_group",        "logical",  False),
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
            OptionsInfo("footnotes_multiline",               False,  "footnotes",        "logical",  True),
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
            OptionsInfo("source_notes_multiline",            False,  "source_notes",     "logical",  True),
            OptionsInfo("source_notes_sep",                  False,  "source_notes",     "value",    " "),
            OptionsInfo("row_striping_background_color",      True,  "row",              "value",    "rgba(128,128,128,0.05)"),
            OptionsInfo("row_striping_include_stub",         False,  "row",              "logical",  False),
            OptionsInfo("row_striping_include_table_body",   False,  "row",              "logical",  False),
            OptionsInfo("page_orientation",                  False,  "page",             "value",    "portrait"),
            OptionsInfo("page_numbering",                    False,  "page",             "logical",  False),
            OptionsInfo("page_header_use_tbl_headings",      False,  "page",             "logical",  False),
            OptionsInfo("page_footer_use_tbl_notes",         False,  "page",             "logical",  False),
            OptionsInfo("page_width",                        False,  "page",             "value",    "8.5in"),
            OptionsInfo("page_height",                       False,  "page",             "value",    "11.0in"),
            OptionsInfo("page_margin_left",                  False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_margin_right",                 False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_margin_top",                   False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_margin_bottom",                False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_header_height",                False,  "page",             "value",    "0.5in"),
            OptionsInfo("page_footer_height",                False,  "page",             "value",    "0.5in"),
        ]
# fmt: on

    def _get_all_options_keys(self) -> List[Union[str, None]]:
        return [x.parameter for x in self._options]

    def _get_option_index(self, option: str) -> int:
        # TODO: ensure error if we pop from empty list
        return [x for x in range(len(self._options)) if self._options[x].parameter == option].pop() 

    def _get_option_type(self, option: str) -> Union[Any, List[str]]:
        # TODO: ensure error if we pop from empty list
        return [x.type for x in self._options if x.parameter == option].pop()

    def _get_option_value(self, option: str) -> Union[Any, List[str]]:
        # TODO: ensure error if we pop from empty list
        return [x.value for x in self._options if x.parameter == option].pop()
    
    def _set_option_value(self, option: str, value: Any):
        idx: int = self._get_option_index(option=option)
        self._options[idx].value = value
        return self


class OptionsAPI:
    _options: Options

    def __init__(self):
        self._options = Options()

    def tab_options(self,
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
        column_labels_hidden: Optional[str] = None,
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
        row_group_as_column: Optional[str] = None,
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
        footnotes_marks: Optional[str] = None,
        footnotes_multiline: Optional[str] = None,
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
        source_notes_multiline: Optional[str] = None,
        source_notes_sep: Optional[str] = None,
        row_striping_background_color: Optional[str] = None,
        row_striping_include_stub: Optional[str] = None,
        row_striping_include_table_body: Optional[str] = None,
        page_orientation: Optional[str] = None,
        page_numbering: Optional[str] = None,
        page_header_use_tbl_headings: Optional[str] = None,
        page_footer_use_tbl_notes: Optional[str] = None,
        page_width: Optional[str] = None,
        page_height: Optional[str] = None,
        page_margin_left: Optional[str] = None,
        page_margin_right: Optional[str] = None,
        page_margin_top: Optional[str] = None,
        page_margin_bottom: Optional[str] = None,
        page_header_height: Optional[str] = None,
        page_footer_height: Optional[str] = None,
    ):
        saved_args = locals()

        del saved_args["self"]

        modified_args = {k: v for k, v in saved_args.items() if v is not None}
        
        for i in range(len(modified_args)):
            self._options._set_option_value(
                option=list(modified_args.keys())[i],
                value=list(modified_args.values())[i]
            )

        return self

    # TODO: create the `opt_footnote_marks()` function

    # TODO: create the `opt_row_striping()` function

    # TODO: create the `opt_align_table_header()` function

    # TODO: create the `opt_vertical_padding()` function

    # TODO: create the `opt_horizontal_padding()` function

    # TODO: create the `opt_all_caps()` function

    # TODO: create the `opt_table_lines()` function

    # TODO: create the `opt_table_outline()` function

    # TODO: create the `opt_table_font()` function
    
    # TODO: create the `opt_css()` function

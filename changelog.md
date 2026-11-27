# Changelog

This changelog is generated automatically from [GitHub Releases](https://github.com/posit-dev/great-tables/releases).

## v1.2.0

*2026-11-20* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v1.2.0)

Great Tables `v1.2.0` is the biggest release yet, and it's centered on interactive tables. The new `GTI` class makes any table something readers can explore. Its `i_*()` methods add column filters, a query language, exports, column profiles, row details, row grouping, linked tables, and layouts that fit narrow screens. GTI tables work in notebooks, Quarto, and Shiny, Streamlit, Panel, Solara, marimo, and Flask/Django/FastHTML apps, and they can keep their rows in Python, a Polars LazyFrame, DuckDB, or Ibis. `opt_interactive()` now uses the same engine, so its tables keep everything a `GT` table has. Outside of interactivity, `gtsave()` can now write SVG, Word, Excel, PowerPoint, RTF, and Typst files, `fmt_nanoplot()` draws box plots, `fmt_datetime()` takes CLDR patterns, and PyArrow support is no longer experimental. This release also brings more than 50 bug fixes, many of them in the PyArrow and Polars backends.

#### New Features

- **`GTI`, interactive tables** -- `GTI(data)` (or `GTI.from_gt()` for a finished `GT` table) makes a table that readers can sort, search, page through, resize, and select rows of. Everything a `GT` table has is kept: formatting, styles, stub, row groups, spanners, footnotes, and summary rows. The table is GT's own HTML, brought to life by the bundled `<gt-table>` component, so it's readable before its script runs and needs no server or internet connection. `GTI` is experimental. Each feature has its own `i_*()` method, including `i_sorting()`, `i_search()`, `i_pagination()`, `i_selection()`, `i_resizing()`, `i_display()` (highlighting, compact rows, no-wrap, monospace), and `i_scroll()` (a scrolling body with sticky column labels). A wide table keeps its stub pinned as it scrolls sideways, and short pages are padded to a full page's height. ([\#1059](https://github.com/posit-dev/great-tables/issues/1059), [\#1060](https://github.com/posit-dev/great-tables/issues/1060), [\#1061](https://github.com/posit-dev/great-tables/issues/1061), [\#1062](https://github.com/posit-dev/great-tables/issues/1062), [\#1063](https://github.com/posit-dev/great-tables/issues/1063), [\#1065](https://github.com/posit-dev/great-tables/issues/1065), [\#1066](https://github.com/posit-dev/great-tables/issues/1066), [\#1069](https://github.com/posit-dev/great-tables/issues/1069), [\#1070](https://github.com/posit-dev/great-tables/issues/1070), [\#1073](https://github.com/posit-dev/great-tables/issues/1073), [\#1074](https://github.com/posit-dev/great-tables/issues/1074), [\#1075](https://github.com/posit-dev/great-tables/issues/1075))
- **A control bar for GTI tables** -- Search, page controls (first, previous, next, and last, with a jump-to readout), an info panel, keyboard shortcuts, a reset button, and tooltips sit next to the table. Drag handles change the rows per page and the scroll height. Pressing `?` outlines and names each part of the table, and `i_display(parts=True)` keeps those names showing (for docs). ([\#1076](https://github.com/posit-dev/great-tables/issues/1076), [\#1077](https://github.com/posit-dev/great-tables/issues/1077), [\#1121](https://github.com/posit-dev/great-tables/issues/1121), [\#1122](https://github.com/posit-dev/great-tables/issues/1122), [\#1164](https://github.com/posit-dev/great-tables/issues/1164), [\#1165](https://github.com/posit-dev/great-tables/issues/1165))
- **Column filters** -- `i_cols_filter()` gives columns a filter suited to their type: text, a choice of values (facet), a range of numbers or dates, or true/false. ([\#1078](https://github.com/posit-dev/great-tables/issues/1078), [\#1093](https://github.com/posit-dev/great-tables/issues/1093), [\#1094](https://github.com/posit-dev/great-tables/issues/1094))
- **Views and a query language** -- `i_view(filter=, sort=, group_by=)` sets what a table opens with. Filters show as tokens in the bar, and readers can edit them as text in a query box. The query language has `and`, `or`, `not`, parentheses, `in`/`not in`, `contains`, regex `matches`, `is null`, strict and inclusive bounds, and `top`/`bottom` clauses. Column labels can be typed in place of column names. `i_view_state()` keeps the reader's view in the URL or browser storage, and the view has undo and redo. ([\#1080](https://github.com/posit-dev/great-tables/issues/1080), [\#1081](https://github.com/posit-dev/great-tables/issues/1081), [\#1082](https://github.com/posit-dev/great-tables/issues/1082), [\#1085](https://github.com/posit-dev/great-tables/issues/1085), [\#1087](https://github.com/posit-dev/great-tables/issues/1087), [\#1096](https://github.com/posit-dev/great-tables/issues/1096), [\#1098](https://github.com/posit-dev/great-tables/issues/1098), [\#1099](https://github.com/posit-dev/great-tables/issues/1099), [\#1100](https://github.com/posit-dev/great-tables/issues/1100), [\#1101](https://github.com/posit-dev/great-tables/issues/1101), [\#1104](https://github.com/posit-dev/great-tables/issues/1104), [\#1171](https://github.com/posit-dev/great-tables/issues/1171))
- **Exports** -- `i_export()` lets readers download the rows they're looking at as CSV, TSV, or JSON, copy them as a rich table, or copy Polars, Pandas, or Narwhals code that filters and sorts the data as their view does. ([\#1083](https://github.com/posit-dev/great-tables/issues/1083), [\#1084](https://github.com/posit-dev/great-tables/issues/1084), [\#1095](https://github.com/posit-dev/great-tables/issues/1095))
- **Column controls** -- `i_cols_controls()` sets sorting, search, and resizing column by column. It can also let readers hide, reorder, and group by columns, keep a column only for querying (`display=False`), and recolor a column's `data_color()` colors from the rows kept (`data_color="recompute"`). `i_cols_pin()` pins columns to either side. ([\#1088](https://github.com/posit-dev/great-tables/issues/1088), [\#1089](https://github.com/posit-dev/great-tables/issues/1089), [\#1090](https://github.com/posit-dev/great-tables/issues/1090), [\#1091](https://github.com/posit-dev/great-tables/issues/1091), [\#1092](https://github.com/posit-dev/great-tables/issues/1092), [\#1119](https://github.com/posit-dev/great-tables/issues/1119), [\#1132](https://github.com/posit-dev/great-tables/issues/1132))
- **Layouts for narrow containers** -- `i_responsive()` either stacks rows as cards or drops the least important columns (set with `i_cols_priority()`) into an expandable row until the table fits. The default, `"auto"`, picks a layout based on the table. On phones, each column has a long-press sheet, and the table has a "Filter & sort" sheet. ([\#1105](https://github.com/posit-dev/great-tables/issues/1105), [\#1112](https://github.com/posit-dev/great-tables/issues/1112), [\#1114](https://github.com/posit-dev/great-tables/issues/1114))
- **Row details, profiles, and the explorer preset** -- `i_row_details()` lets readers open a row to show more about it, from a function or a column (even a nested `GT` table). `i_cols_profile()` draws a histogram or top-values plot under each column label, with tooltips and a larger view. `GTI(preset="explorer")` (and `GTI.from_gt(preset="explorer")`) sets a table up for looking through data, with filters, profiles, row numbers, dtypes, and missing values tinted by `i_inspect()`. ([\#1125](https://github.com/posit-dev/great-tables/issues/1125), [\#1126](https://github.com/posit-dev/great-tables/issues/1126), [\#1128](https://github.com/posit-dev/great-tables/issues/1128), [\#1175](https://github.com/posit-dev/great-tables/issues/1175), [\#1187](https://github.com/posit-dev/great-tables/issues/1187))
- **Row grouping and linked tables** -- Readers can group a table's rows by a column, with a heading and count for each group. `i_link()` links the tables on a page, so rows selected in one table filter the others. ([\#1130](https://github.com/posit-dev/great-tables/issues/1130), [\#1131](https://github.com/posit-dev/great-tables/issues/1131))
- **GTI in notebooks and apps** -- `i_as_widget()` makes the table an anywidget, whose view and selection Python can read and set. In Shiny, `render_gt()` gives the app inputs for the view, rows, and selection, and `update_gti()` sets them from the server. There's also `st_gti()` for Streamlit, `GTIPane` for Panel, `GTITable` for Solara, and `mo_gti()` for marimo. `great_tables.web` has helpers for pages that Flask, Django, or FastHTML apps make themselves, and `GT` tables can go straight into Jinja templates (`__html__()`) and FastHTML components (`__ft__()`). ([\#1138](https://github.com/posit-dev/great-tables/issues/1138), [\#1139](https://github.com/posit-dev/great-tables/issues/1139), [\#1146](https://github.com/posit-dev/great-tables/issues/1146), [\#1147](https://github.com/posit-dev/great-tables/issues/1147), [\#1152](https://github.com/posit-dev/great-tables/issues/1152), [\#1153](https://github.com/posit-dev/great-tables/issues/1153), [\#1154](https://github.com/posit-dev/great-tables/issues/1154), [\#1182](https://github.com/posit-dev/great-tables/issues/1182))
- **Large data in GTI tables** -- With `i_scale()`, a large table keeps its rows in Python (in a widget) or on the Shiny server, and the browser asks for one page at a time. `GTI()` also takes a Polars LazyFrame, a DuckDB relation, or an Ibis table, and keeps its rows in that backend. A `GTISizeWarning` is raised when a table may be slow in the browser. ([\#1124](https://github.com/posit-dev/great-tables/issues/1124), [\#1141](https://github.com/posit-dev/great-tables/issues/1141), [\#1142](https://github.com/posit-dev/great-tables/issues/1142), [\#1143](https://github.com/posit-dev/great-tables/issues/1143), [\#1144](https://github.com/posit-dev/great-tables/issues/1144), [\#1145](https://github.com/posit-dev/great-tables/issues/1145))
- **New `gtsave()` formats** -- `gtsave()` can now write SVG, Word (`.docx`), Excel (`.xlsx`), PowerPoint (`.pptx`), RTF, and Typst (`.typ`) files through gridwell. Install it with `pip install "great_tables[gridwell]"`. The gridwell IR behind these formats is available as the experimental `GT.as_gridwell()`. ([\#1167](https://github.com/posit-dev/great-tables/issues/1167))
- **Box plots in `fmt_nanoplot()`** -- `plot_type="boxplot"` draws each row's values as a box and whiskers on a scale shared by all rows, with the statistics shown on hover. Reference lines and areas work with box plots. ([\#989](https://github.com/posit-dev/great-tables/issues/989))
- **CLDR patterns and flexible styles in `fmt_datetime()`** -- A `format_str=` without `%` is now a CLDR pattern (e.g., `"EEEE d MMMM y"`), formatted for the locale. There are also 24 flexible date styles and 20 flexible time styles (`"yMMMd"`, `"hm"`, …) that follow each locale's word order. These work in `vals.fmt_datetime()` too. ([\#992](https://github.com/posit-dev/great-tables/issues/992), [\#994](https://github.com/posit-dev/great-tables/issues/994))
- **Indian numbering system** -- `fmt_number()` and `fmt_integer()` (and their `vals` versions) take `system="ind"` to group digits as in `12,34,567`. ([\#1000](https://github.com/posit-dev/great-tables/issues/1000))

#### Enhancements

- PyArrow tables are no longer experimental and no longer warn. Every data-layer helper now behaves the same on Pandas, Polars, and PyArrow. ([\#1140](https://github.com/posit-dev/great-tables/issues/1140))
- Rendering is faster: formatted values are now written into the body one column at a time instead of one cell at a time. PyArrow render time used to grow with the square of the row count. ([\#996](https://github.com/posit-dev/great-tables/issues/996))
- GTI tables got many fixes and refinements before release, including scrolling, focus and keyboard handling, CSS zoom, pinned columns, search highlights, accessibility of labels and profiles, Panel notebook sync, and rendering speed. ([\#1097](https://github.com/posit-dev/great-tables/issues/1097), [\#1113](https://github.com/posit-dev/great-tables/issues/1113), [\#1123](https://github.com/posit-dev/great-tables/issues/1123), [\#1148](https://github.com/posit-dev/great-tables/issues/1148), [\#1149](https://github.com/posit-dev/great-tables/issues/1149), [\#1150](https://github.com/posit-dev/great-tables/issues/1150), [\#1162](https://github.com/posit-dev/great-tables/issues/1162), [\#1163](https://github.com/posit-dev/great-tables/issues/1163), [\#1166](https://github.com/posit-dev/great-tables/issues/1166), [\#1172](https://github.com/posit-dev/great-tables/issues/1172), [\#1173](https://github.com/posit-dev/great-tables/issues/1173), [\#1174](https://github.com/posit-dev/great-tables/issues/1174), [\#1177](https://github.com/posit-dev/great-tables/issues/1177), [\#1178](https://github.com/posit-dev/great-tables/issues/1178), [\#1179](https://github.com/posit-dev/great-tables/issues/1179), [\#1180](https://github.com/posit-dev/great-tables/issues/1180), [\#1181](https://github.com/posit-dev/great-tables/issues/1181), [\#1183](https://github.com/posit-dev/great-tables/issues/1183), [\#1184](https://github.com/posit-dev/great-tables/issues/1184), [\#1185](https://github.com/posit-dev/great-tables/issues/1185))

#### Behavior Changes

- `opt_interactive()` tables are now rendered by GTI instead of reactable. They keep their stub, row groups, spanners, footnotes, summary rows, styles, and fonts, and they need no network access. Every `opt_interactive()` option now works, including `use_highlight=`, `use_resizers=`, `selection_mode=`, `use_filters=`, and a `"full"` page style. ([\#1115](https://github.com/posit-dev/great-tables/issues/1115))
- `opt_interactive()` now raises for an unknown `pagination_type=`, and `selection_mode=None` now turns selection off after an earlier call turned it on. ([\#1187](https://github.com/posit-dev/great-tables/issues/1187))
- A column name that isn't in the table now raises a `ValueError` naming it, on every backend. Before, Pandas and PyArrow skipped it silently and Polars raised its own error. ([\#1186](https://github.com/posit-dev/great-tables/issues/1186))
- A list of booleans in `rows=` is now read as a mask (and its length is checked), rather than as the positions 0 and 1. ([\#1186](https://github.com/posit-dev/great-tables/issues/1186))
- `fmt_icon()` now draws icons from bundled Font Awesome 7.1.0 data, which redraws most of them. The 163 names that come in both solid and regular styles now render the regular style. Use a full name (`"fas fa-star"`) to choose a style. ([\#1055](https://github.com/posit-dev/great-tables/issues/1055))
- Footnotes now come before source notes in the table footer. ([\#1133](https://github.com/posit-dev/great-tables/issues/1133))
- Column labels have 1px more bottom padding by default (`column_labels_padding` + 1px). ([\#1134](https://github.com/posit-dev/great-tables/issues/1134))
- `sub_values(fn=)` is now called on missing values too, while `values=` and `pattern=` still never match them. ([\#985](https://github.com/posit-dev/great-tables/issues/985), [\#987](https://github.com/posit-dev/great-tables/issues/987))
- Number-like text now right-aligns on every string dtype (Polars, PyArrow, and Pandas nullable strings), not just Pandas `object`. Pandas `object` columns without strings are now aligned by what they hold. ([\#1086](https://github.com/posit-dev/great-tables/issues/1086), [\#1107](https://github.com/posit-dev/great-tables/issues/1107))
- `tab_style_body()` and `data_color(fn=)` now get `None` for a missing value on every backend. ([\#1064](https://github.com/posit-dev/great-tables/issues/1064))
- The Pandas datasets now keep text like Namibia's `"NA"` country code, as Polars does, instead of reading it as missing. ([\#1186](https://github.com/posit-dev/great-tables/issues/1186))

#### Bug Fixes

- Significant digits are now rounded once, from the stored value. This fixes an `OverflowError` for values below about 1e-306 and double rounding in `n_sigfig=` and `fmt_scientific()`. The same fix applies to `fmt_engineering()`, `fmt_number_si()`, compact numbers, and `fmt_bytes()`. ([\#980](https://github.com/posit-dev/great-tables/issues/980), [\#988](https://github.com/posit-dev/great-tables/issues/988), [\#990](https://github.com/posit-dev/great-tables/issues/990))
- Large integers now keep all their digits in `fmt_number()`, `fmt_integer()`, and `fmt_currency()`, including when scaled and with `n_sigfig=`. ([\#982](https://github.com/posit-dev/great-tables/issues/982), [\#984](https://github.com/posit-dev/great-tables/issues/984))
- Scientific and engineering notation now stays on one line in HTML. ([\#983](https://github.com/posit-dev/great-tables/issues/983))
- A float `scale_by=` now works on `Decimal` columns. ([\#987](https://github.com/posit-dev/great-tables/issues/987))
- `sub_values()` now handles `pd.NA` and skips missing values explicitly, and Pandas columns of arrays or lists now render. ([\#977](https://github.com/posit-dev/great-tables/issues/977), [\#985](https://github.com/posit-dev/great-tables/issues/985))
- `GT.save()` with Chrome now works in Colab and Docker containers (as root). ([\#978](https://github.com/posit-dev/great-tables/issues/978))
- `vals` functions now keep the values they're given, instead of letting Polars' type inference change them (e.g., very large integers, fixed UTC offsets, mixed types). ([\#993](https://github.com/posit-dev/great-tables/issues/993))
- `fmt_datetime(format_str=)` now works in tables with a locale. ([\#991](https://github.com/posit-dev/great-tables/issues/991))
- `fmt_duration()` with `duration_style="colon-sep"` now carries larger units into the first field shown and ignores `max_output_units=`, as documented. `trim_zero_units=` is now checked when the method is called. The `<` of `<1s` is now escaped in HTML. ([\#995](https://github.com/posit-dev/great-tables/issues/995), [\#997](https://github.com/posit-dev/great-tables/issues/997), [\#1186](https://github.com/posit-dev/great-tables/issues/1186))
- The CRC currency symbol's HTML entity is now closed, a zero-width non-joiner was removed from the BGN symbol, and the current ISO 4217 codes BYN, MRU, STN, and VES were added. ([\#1014](https://github.com/posit-dev/great-tables/issues/1014), [\#1015](https://github.com/posit-dev/great-tables/issues/1015), [\#1034](https://github.com/posit-dev/great-tables/issues/1034))
- `fmt_nanoplot()` now supports the `"first"` and `"last"` reference keywords, and draws PyArrow `float64` and `Decimal` columns, Pandas numeric columns holding `pd.NA`, and NumPy numbers. ([\#998](https://github.com/posit-dev/great-tables/issues/998), [\#1008](https://github.com/posit-dev/great-tables/issues/1008), [\#1009](https://github.com/posit-dev/great-tables/issues/1009), [\#1013](https://github.com/posit-dev/great-tables/issues/1013))
- With Polars data, `columns=` takes a function and `loc.body(rows=)` takes a callable. ([\#1010](https://github.com/posit-dev/great-tables/issues/1010), [\#1011](https://github.com/posit-dev/great-tables/issues/1011))
- PyArrow tables now render list and struct columns, accept callables that return a `ChunkedArray`, show a NaN in a formatted float column, keep rows with a null group key, and handle reordering with no rows. ([\#1012](https://github.com/posit-dev/great-tables/issues/1012), [\#1016](https://github.com/posit-dev/great-tables/issues/1016), [\#1018](https://github.com/posit-dev/great-tables/issues/1018), [\#1036](https://github.com/posit-dev/great-tables/issues/1036), [\#1037](https://github.com/posit-dev/great-tables/issues/1037))
- PyArrow `large_string` and `string_view` columns are now left-aligned. Datetime columns of PyArrow tables and PyArrow-backed Pandas are now right-aligned. `string_view` columns now work in rendering, grouping, and `data_color()`. ([\#1031](https://github.com/posit-dev/great-tables/issues/1031), [\#1039](https://github.com/posit-dev/great-tables/issues/1039), [\#1109](https://github.com/posit-dev/great-tables/issues/1109), [\#1186](https://github.com/posit-dev/great-tables/issues/1186))
- `data_color()` no longer fails on PyArrow tables when no rows are selected, and it follows the level order of ordered PyArrow dictionary columns. ([\#1006](https://github.com/posit-dev/great-tables/issues/1006), [\#1033](https://github.com/posit-dev/great-tables/issues/1033))
- Nested, Enum, interval, run-end-encoded, dictionary, and union dtypes are no longer treated as numeric. ([\#1043](https://github.com/posit-dev/great-tables/issues/1043), [\#1051](https://github.com/posit-dev/great-tables/issues/1051), [\#1108](https://github.com/posit-dev/great-tables/issues/1108))
- A missing `groupname_col` value now renders on Pandas as it does on Polars and PyArrow. ([\#1042](https://github.com/posit-dev/great-tables/issues/1042))
- `summary_rows()` now works for groups with empty, missing, or non-string keys. ([\#1072](https://github.com/posit-dev/great-tables/issues/1072))
- Missing values in a callable row mask now count as "not selected" on every backend, instead of raising. ([\#1106](https://github.com/posit-dev/great-tables/issues/1106))
- Generic missing-value checks no longer import Polars, so `fmt_nanoplot()` and `vals` functions work without it. ([\#1129](https://github.com/posit-dev/great-tables/issues/1129))
- `sub_missing()` text is no longer merged in as a value by `cols_merge_uncert()`, `cols_merge_n_pct()`, or `cols_merge_range()`. Equal `cols_merge_uncert()` bounds are now compared using the original values, and asymmetric bounds use a plain minus sign in LaTeX. ([\#1035](https://github.com/posit-dev/great-tables/issues/1035), [\#1038](https://github.com/posit-dev/great-tables/issues/1038), [\#1046](https://github.com/posit-dev/great-tables/issues/1046), [\#1056](https://github.com/posit-dev/great-tables/issues/1056))
- `tab_spanner_delim()` now gives spanners unique ids when a label repeats. ([\#1027](https://github.com/posit-dev/great-tables/issues/1027))
- Spanner footnotes are now ordered by column when a spanner's id differs from its label. Footnotes on a missing title, subtitle, or spanner are no longer shown. ([\#1103](https://github.com/posit-dev/great-tables/issues/1103), [\#1136](https://github.com/posit-dev/great-tables/issues/1136))
- Styles on source notes are now kept when `source_notes_multiline=False`. ([\#1133](https://github.com/posit-dev/great-tables/issues/1133))
- The default CSS's element rules are now scoped to the table, so they no longer change other tables on the page. The footnotes' text color rule is now valid CSS. ([\#1134](https://github.com/posit-dev/great-tables/issues/1134), [\#1135](https://github.com/posit-dev/great-tables/issues/1135))

#### Documentation

- The Interactive Tables pages of the User Guide were split into three and rewritten for GTI. They cover scrolling, wide tables, pinned columns, summary rows, notes, exports, selection, narrow layouts, and filter types, and they include a diagram of the parts of a GTI table. ([\#1151](https://github.com/posit-dev/great-tables/issues/1151), [\#1157](https://github.com/posit-dev/great-tables/issues/1157), [\#1168](https://github.com/posit-dev/great-tables/issues/1168), [\#1170](https://github.com/posit-dev/great-tables/issues/1170))
- `GTI` and its methods were added to the API reference. ([\#1156](https://github.com/posit-dev/great-tables/issues/1156))
- The rest of the User Guide was modernized. ([\#1158](https://github.com/posit-dev/great-tables/issues/1158))
- Docstring examples now use the `data.pl` datasets, and the docs show that a Polars `.style` table can become a GTI table. ([\#1159](https://github.com/posit-dev/great-tables/issues/1159), [\#1160](https://github.com/posit-dev/great-tables/issues/1160))
- The README now has an animated demo of a GTI table. ([\#1161](https://github.com/posit-dev/great-tables/issues/1161))
- A broken User Guide link on the home page was fixed. ([\#1117](https://github.com/posit-dev/great-tables/issues/1117))

#### Maintenance

- htmltools and faicons are no longer dependencies. ([\#1054](https://github.com/posit-dev/great-tables/issues/1054), [\#1055](https://github.com/posit-dev/great-tables/issues/1055))
- The data-layer tests now run on every frame and series constructor, and every rendering scenario is checked on every backend, with any differences pinned. This groundwork made the PyArrow promotion possible. ([\#1001](https://github.com/posit-dev/great-tables/issues/1001), [\#1004](https://github.com/posit-dev/great-tables/issues/1004), [\#1019](https://github.com/posit-dev/great-tables/issues/1019), [\#1029](https://github.com/posit-dev/great-tables/issues/1029), [\#1032](https://github.com/posit-dev/great-tables/issues/1032), [\#1050](https://github.com/posit-dev/great-tables/issues/1050), [\#1052](https://github.com/posit-dev/great-tables/issues/1052), [\#1057](https://github.com/posit-dev/great-tables/issues/1057), [\#1067](https://github.com/posit-dev/great-tables/issues/1067), [\#1071](https://github.com/posit-dev/great-tables/issues/1071))
- The GTI end-to-end tests run in Chromium, Firefox, and WebKit, and in Jupyter, Quarto, Shiny, marimo, and VS Code, with benchmarks for the runtime. ([\#1116](https://github.com/posit-dev/great-tables/issues/1116), [\#1118](https://github.com/posit-dev/great-tables/issues/1118))
- Earlier fixes to the reactable renderer that `opt_interactive()` used before this release, and the removal of its unused DataTables and jQuery files. ([\#986](https://github.com/posit-dev/great-tables/issues/986), [\#1041](https://github.com/posit-dev/great-tables/issues/1041), [\#1058](https://github.com/posit-dev/great-tables/issues/1058))
- Ruff was upgraded to 0.17.4 with its default lint rules, and CI now uses uv and builds the docs in parallel. A nested `pytest.approx()` that pytest 9.2 rejects was flattened. ([\#1044](https://github.com/posit-dev/great-tables/issues/1044), [\#1110](https://github.com/posit-dev/great-tables/issues/1110), [\#1111](https://github.com/posit-dev/great-tables/issues/1111), [\#1137](https://github.com/posit-dev/great-tables/issues/1137))

## v1.1.0

*2026-10-15* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v1.1.0)

Great Tables `v1.1.0` is quite a hefty release, and it's centered on richer color scaling, accessibility, and much more reliable LaTeX output. Tables can now have a stub made of several columns, and the new `cols_align_decimal()` method lines up numbers on their decimal mark. `data_color()` gains custom color functions, a `midpoint=` for diverging scales, row-wise coloring, and perceptually based text contrast (APCA). HTML tables now carry semantic markup for screen readers by default. This release also fixes more than 60 bugs, with most of the fixes in the number formatters (rounding, infinite and missing values) and in LaTeX rendering.

#### New Features

- **Multi-column stubs** -- `rowname_col=` now accepts a list of columns, so the stub can show several levels of row labels. Use the new `stub(n)` selector in any `columns=` argument to target one stub level (e.g., `cols_width(cases={stub(1): "70px", stub(2): "200px"})`). ([\#861](https://github.com/posit-dev/great-tables/issues/861), [\#933](https://github.com/posit-dev/great-tables/issues/933))
- **`cols_align_decimal()`** -- Aligns the numeric values in a column on their decimal mark, with optional `dec_mark=` and `locale=` settings. ([\#944](https://github.com/posit-dev/great-tables/issues/944))
- **Custom color functions in `data_color()`** -- The new `fn=` argument takes a function that maps a list of values to a list of colors, giving you full control over the color mapping. ([\#898](https://github.com/posit-dev/great-tables/issues/898))
- **Diverging scales with `midpoint=`** -- `data_color(midpoint=0)` centers the palette on a value. The domain is made symmetric around it unless you supply one. ([\#911](https://github.com/posit-dev/great-tables/issues/911))
- **Row-wise coloring** -- `data_color(direction="row")` computes colors across each row instead of down each column. ([\#950](https://github.com/posit-dev/great-tables/issues/950))
- **APCA text contrast** -- The new `contrast_algo=` argument in `data_color()` chooses between `"apca"` (the new default) and `"wcag"` for automatic text coloring. ([\#897](https://github.com/posit-dev/great-tables/issues/897))
- **Accessible HTML tables** -- Header cells now have unique ids, and body cells link to them through `headers`. Stub and row group header cells get `scope` attributes. Tables are named and described by their title and subtitle (`aria-labelledby`/`aria-describedby`). ([\#936](https://github.com/posit-dev/great-tables/issues/936), [\#957](https://github.com/posit-dev/great-tables/issues/957), [\#959](https://github.com/posit-dev/great-tables/issues/959))
- **`min_sep_threshold=` in number formatters** -- Sets the minimum number of digits before digit grouping applies, and follows each locale's own minimum grouping digits by default, as in gt. ([\#956](https://github.com/posit-dev/great-tables/issues/956))

#### Enhancements

- Images, nanoplots, flags, and icons now get accessible markup (alternative text and roles). ([\#968](https://github.com/posit-dev/great-tables/issues/968))
- Nanoplot CSS is now scoped to each plot, and the static view (`interactive_data_values=False`) is less cluttered. ([\#903](https://github.com/posit-dev/great-tables/issues/903))
- ISO durations from `fmt_duration()` are now machine-readable, and durations shown as zero no longer carry a sign. ([\#966](https://github.com/posit-dev/great-tables/issues/966))
- Units notation and `fmt_chem()` now render in LaTeX output. ([\#969](https://github.com/posit-dev/great-tables/issues/969), [\#973](https://github.com/posit-dev/great-tables/issues/973))
- The `rows=` argument of the `fmt_*()`, `sub_*()`, and `cols_merge*()` methods is now typed as `RowSelectExpr`, which improves editor and type-checker support. ([\#896](https://github.com/posit-dev/great-tables/issues/896))

#### Behavior Changes

- `data_color()` now picks text colors with APCA by default instead of the WCAG contrast ratio, so some cells may get different text colors. Use `contrast_algo="wcag"` to keep the old behavior. ([\#897](https://github.com/posit-dev/great-tables/issues/897))
- `data_color()` palettes are now interpolated in CIELAB, which gives smoother, more perceptually even gradients. Colors between palette stops will differ slightly from earlier versions. ([\#964](https://github.com/posit-dev/great-tables/issues/964))
- `data_color()` now uses the declared level order of ordered Pandas `Categorical` and Polars `Enum` columns as the inferred domain. ([\#902](https://github.com/posit-dev/great-tables/issues/902))
- Stub and row group columns are now excluded from column selections, as originally intended. When `columns=` is omitted, methods target body columns only, so `data_color()` no longer colors stub cells. `loc.body()` and `cols_move*()` raise a clear error when given a stub or group column. ([\#933](https://github.com/posit-dev/great-tables/issues/933))

#### Deprecations

- The `placeholder=` parameter of `output_gt()` is deprecated. ([\#909](https://github.com/posit-dev/great-tables/issues/909))
- The `islands` and `airquality` datasets are deprecated and now emit a `FutureWarning`. They will be removed in a future release. ([\#939](https://github.com/posit-dev/great-tables/issues/939))

#### Bug Fixes

- When rounding carries over, it now moves into the next exponent, suffix, unit, or prefix. This applies to `fmt_scientific()` and `n_sigfig=` ([\#906](https://github.com/posit-dev/great-tables/issues/906)), `fmt_engineering()` ([\#915](https://github.com/posit-dev/great-tables/issues/915)), compact numbers ([\#914](https://github.com/posit-dev/great-tables/issues/914)), `fmt_bytes()` ([\#916](https://github.com/posit-dev/great-tables/issues/916)), and `fmt_number_si()` ([\#918](https://github.com/posit-dev/great-tables/issues/918)).
- `drop_trailing_zeros=` no longer strips zeros from the integer part of a number. ([\#925](https://github.com/posit-dev/great-tables/issues/925))
- `fmt_scientific()` keeps trailing zeros with `n_sigfig=`, as documented. ([\#963](https://github.com/posit-dev/great-tables/issues/963))
- Negative values are now rounded away from zero, as in R gt. ([\#953](https://github.com/posit-dev/great-tables/issues/953))
- Values that round to zero are now shown without a sign. ([\#940](https://github.com/posit-dev/great-tables/issues/940))
- `fmt_currency()` now handles currency codes that have no minor unit. ([\#931](https://github.com/posit-dev/great-tables/issues/931))
- Number streams wrapped in brackets (e.g., `"[1, 2, 3]"`) now parse correctly. ([\#908](https://github.com/posit-dev/great-tables/issues/908))
- `fmt_partsper()`, `fmt_fraction()`, `fmt_number_si()`, and `fmt_duration()` now follow locales that don't group four-digit numbers. ([\#970](https://github.com/posit-dev/great-tables/issues/970))
- NaN and infinite values are now handled consistently across the formatters. This includes `fmt_scientific()`, `fmt_engineering()`, `fmt_bytes()`, `fmt_roman()`, `fmt_duration()`, `fmt_number_si()`, `n_sigfig=`, and `compact=True`. ([\#917](https://github.com/posit-dev/great-tables/issues/917), [\#920](https://github.com/posit-dev/great-tables/issues/920), [\#922](https://github.com/posit-dev/great-tables/issues/922), [\#926](https://github.com/posit-dev/great-tables/issues/926))
- Missing values in nullable Pandas columns no longer render as `0`. ([\#949](https://github.com/posit-dev/great-tables/issues/949))
- `fmt_fraction()`, `fmt_roman()`, and `fmt_index()` now format NumPy integer and `float32` values. ([\#958](https://github.com/posit-dev/great-tables/issues/958))
- `fmt_tf()` now accepts NumPy booleans from Pandas columns. ([\#921](https://github.com/posit-dev/great-tables/issues/921))
- Pandas columns of PyArrow-backed strings are now auto-aligned. ([\#900](https://github.com/posit-dev/great-tables/issues/900))
- `sub_large_vals(sign="-")` now shows the negative threshold. ([\#913](https://github.com/posit-dev/great-tables/issues/913))
- `sub_small_vals()` and `sub_large_vals()` now substitute NumPy scalars and treat booleans and `Decimal` values consistently. ([\#946](https://github.com/posit-dev/great-tables/issues/946), [\#967](https://github.com/posit-dev/great-tables/issues/967))
- `sub_zero()` now skips missing values in nullable Pandas columns and leaves boolean values alone. ([\#962](https://github.com/posit-dev/great-tables/issues/962), [\#971](https://github.com/posit-dev/great-tables/issues/971))
- A `sub_*()` call no longer turns off HTML/LaTeX escaping for the cells it skips. PyArrow tables are now escaped too. ([\#938](https://github.com/posit-dev/great-tables/issues/938))
- `fmt_time()` now accepts datetime values and the documented `YYYY-MM-DD HH:MM:SS` strings, and rejects date-only strings. ([\#919](https://github.com/posit-dev/great-tables/issues/919), [\#930](https://github.com/posit-dev/great-tables/issues/930))
- The `year_week` date style now uses the week-based year. ([\#924](https://github.com/posit-dev/great-tables/issues/924))
- In ISO durations, the `T` designator now comes before the time parts. ([\#947](https://github.com/posit-dev/great-tables/issues/947))
- In units notation, a slashed unit now has its exponent negated, and inverted first powers are dropped. ([\#942](https://github.com/posit-dev/great-tables/issues/942), [\#969](https://github.com/posit-dev/great-tables/issues/969))
- `data_color()` now applies `alpha=` to gradient palette colors. ([\#892](https://github.com/posit-dev/great-tables/issues/892))
- `data_color()` now handles Pandas `string` columns with `pd.NA`, scales `Decimal` values as numbers, and gives infinite values the colors at either end of the palette. ([\#902](https://github.com/posit-dev/great-tables/issues/902))
- Nanoplots now keep a stroke width of zero, use a separate area pattern for each fill color, and draw reference lines in single-value plots. ([\#893](https://github.com/posit-dev/great-tables/issues/893), [\#894](https://github.com/posit-dev/great-tables/issues/894), [\#901](https://github.com/posit-dev/great-tables/issues/901))
- Missing values in nanoplots are now handled correctly. ([\#905](https://github.com/posit-dev/great-tables/issues/905))
- Nanoplot number formatting at range boundaries and for compact currency values is now correct. ([\#928](https://github.com/posit-dev/great-tables/issues/928))
- `fmt_flag()` now handles invalid country codes. ([\#912](https://github.com/posit-dev/great-tables/issues/912))
- In LaTeX output, special characters are now escaped in the `fmt_index()` pattern, `<`/`>` characters, summary row labels, and the `<` of sub-unit durations. ([\#895](https://github.com/posit-dev/great-tables/issues/895), [\#941](https://github.com/posit-dev/great-tables/issues/941), [\#945](https://github.com/posit-dev/great-tables/issues/945), [\#954](https://github.com/posit-dev/great-tables/issues/954))
- LaTeX: the stubhead label now renders in the column headings, including when it's empty. ([\#907](https://github.com/posit-dev/great-tables/issues/907), [\#932](https://github.com/posit-dev/great-tables/issues/932))
- LaTeX: `sub_*()` replacement text now renders, and substitution thresholds are shown compactly. ([\#934](https://github.com/posit-dev/great-tables/issues/934), [\#941](https://github.com/posit-dev/great-tables/issues/941))
- LaTeX: `fmt_currency()` symbols are now written as LaTeX-safe characters. ([\#923](https://github.com/posit-dev/great-tables/issues/923))
- LaTeX: `fmt_bytes()` now uses the LaTeX minus sign. ([\#935](https://github.com/posit-dev/great-tables/issues/935))
- LaTeX: `exp_style="low-ten"` now uses a LaTeX subscript. ([\#943](https://github.com/posit-dev/great-tables/issues/943))
- LaTeX: `fmt_url()` and `fmt_email()` links are now written with `\href`. ([\#955](https://github.com/posit-dev/great-tables/issues/955))
- LaTeX: group summary rows with `side="top"` are now placed at the top of the group. ([\#948](https://github.com/posit-dev/great-tables/issues/948))
- LaTeX: row groups are now separated by a midrule when `row_group_as_column=True`. ([\#951](https://github.com/posit-dev/great-tables/issues/951))
- LaTeX: `tab_stub_indent()` now indents row labels, including for `rem`/`%` lengths and with correct point rounding. ([\#952](https://github.com/posit-dev/great-tables/issues/952), [\#961](https://github.com/posit-dev/great-tables/issues/961))
- LaTeX: decimal alignment, summary row values, and grouped summary rows now render correctly. ([\#965](https://github.com/posit-dev/great-tables/issues/965))
- LaTeX tables where a row starts with `[` no longer break. ([\#974](https://github.com/posit-dev/great-tables/issues/974))
- `great_tables.data` now defines `__all__`, so star imports no longer overwrite `pd`/`pl`. ([\#937](https://github.com/posit-dev/great-tables/issues/937))

#### Documentation

- Added an Accessibility page to the User Guide. ([\#960](https://github.com/posit-dev/great-tables/issues/960))
- Added a correlation matrix example to the gallery. ([\#857](https://github.com/posit-dev/great-tables/issues/857))
- The `as_latex()` Limitations list has been updated to match current LaTeX output. ([\#972](https://github.com/posit-dev/great-tables/issues/972))
- References to formatters that exist in both `GT` and `vals` are now fully qualified. ([\#975](https://github.com/posit-dev/great-tables/issues/975))
- Fixed the Premade Themes link in the `opt_stylize()` docs. ([\#976](https://github.com/posit-dev/great-tables/issues/976))

#### Maintenance

- The nanoplots code was refactored, with many new snapshot tests and a comparison script. Bar plots with `x` values now raise `NotImplementedError` instead of erroring. ([\#904](https://github.com/posit-dev/great-tables/issues/904))
- Internal cleanups: consolidated test helpers, shared rounding-carry and `pattern=` helpers, a shared dtype helper, and a refactor of column merge display values. ([\#899](https://github.com/posit-dev/great-tables/issues/899), [\#910](https://github.com/posit-dev/great-tables/issues/910), [\#927](https://github.com/posit-dev/great-tables/issues/927), [\#929](https://github.com/posit-dev/great-tables/issues/929), [\#970](https://github.com/posit-dev/great-tables/issues/970))

#### Contributors

Thank you to everyone who contributed to this release, especially [@LuisFigueroaG](https://github.com/LuisFigueroaG), [@raashish1601](https://github.com/raashish1601), [@manan28025](https://github.com/manan28025), [@Rodrigo-Palma](https://github.com/Rodrigo-Palma), [@taekop](https://github.com/taekop), [@blaahhrrgg](https://github.com/blaahhrrgg), and [@naseem173](https://github.com/naseem173).

## v1.0.0

*2026-09-25* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v1.0.0)

Great Tables `v1.0.0` is here. This milestone release introduces these powerful new formatting methods: `fmt_fraction()` for mixed fractions, `fmt_chem()` for chemical formulas, `fmt_index()` for alphabetical indices, and `fmt_url()`/`fmt_email()` for clickable links and buttons. The new `tab_style_body()` method lets you style cells based on their data values, and `opt_footnote_spec()` gives you fine-grained control over footnote presentation. Cell body values are now HTML-escaped by default, a breaking change that strengthens security against XSS. A new `load_dataset()` function provides a single entry point for all bundled example datasets.

#### Breaking Changes

- **Automatic HTML escaping** -- Unformatted body cell values are now automatically HTML-escaped before rendering. Cells that previously contained intentional raw HTML will now display the literal markup. Use the `html()` helper, `fmt_passthrough(escape=False)`, `fmt_markdown()`, or other formatting methods to opt out of escaping for specific cells. ([\#881](https://github.com/posit-dev/great-tables/issues/881))

#### New Features

- **`fmt_fraction()`** -- Format numeric values as mixed fractions (e.g., 2.5 becomes "2 1/2") with control over precision via `accuracy=` and a choice between `"inline"` and `"diagonal"` typesetting layouts. ([\#886](https://github.com/posit-dev/great-tables/issues/886))
- **`fmt_chem()`** -- Format text as properly typeset chemical formulas and reactions, automatically rendering subscripts, superscripts, isotope notation, and reaction arrows. ([\#887](https://github.com/posit-dev/great-tables/issues/887))
- **`fmt_index()`** -- Convert numeric values to alphabetical index characters (1 → "A", 2 → "B") with `"repeat"` and `"excel"` modes for values beyond the alphabet. ([\#888](https://github.com/posit-dev/great-tables/issues/888))
- **`fmt_url()` and `fmt_email()`** -- Transform URLs and email addresses into clickable links with options for custom labels, button styling, and configurable colors. ([\#891](https://github.com/posit-dev/great-tables/issues/891))
- **`tab_style_body()`** -- Apply styles to body cells based on their data values using exact matches, regex patterns, or predicate functions, with optional expansion to entire rows or columns. ([\#883](https://github.com/posit-dev/great-tables/issues/883))
- **Footnote specs and ordering** -- New `opt_footnote_spec()` controls how footnote marks are styled using a compact DSL, and `opt_footnote_order()` controls the arrangement of marked vs. unmarked footnotes in the footer. ([\#884](https://github.com/posit-dev/great-tables/issues/884))
- **`load_dataset()`** -- Load any of Great Tables' bundled datasets as a Pandas or Polars DataFrame through a single, consistent entry point. ([\#858](https://github.com/posit-dev/great-tables/issues/858))

#### Bug Fixes

- Interactive table sorting now uses original numeric values rather than formatted string representations, ensuring correct sort order for numeric columns. ([\#882](https://github.com/posit-dev/great-tables/issues/882))
- Booleans, missing values, and zero now render consistently across all backends. ([\#880](https://github.com/posit-dev/great-tables/issues/880))
- Nanoplots now drop positions whose x value is missing instead of breaking. ([\#889](https://github.com/posit-dev/great-tables/issues/889))
- Nanoplots warn when a curved data line is dropped due to insufficient x values. ([\#867](https://github.com/posit-dev/great-tables/issues/867))
- LaTeX output now correctly escapes backslash, tilde, and circumflex characters. ([\#872](https://github.com/posit-dev/great-tables/issues/872))
- LaTeX spanner rows now emit one cell per column. ([\#870](https://github.com/posit-dev/great-tables/issues/870))
- The ISO date style now correctly pads the year. ([\#869](https://github.com/posit-dev/great-tables/issues/869))
- Locale names are now accepted regardless of case. ([\#874](https://github.com/posit-dev/great-tables/issues/874))
- Options matching now uses prefix instead of substring, preventing false matches. ([\#873](https://github.com/posit-dev/great-tables/issues/873))
- HTTP scheme matching is now case-insensitive. ([\#876](https://github.com/posit-dev/great-tables/issues/876))
- Fractional parts are now preserved when scaling padding values. ([\#879](https://github.com/posit-dev/great-tables/issues/879))
- `tab_spanner()` is now a no-op when no columns or spanners are selected, instead of raising an error. ([\#865](https://github.com/posit-dev/great-tables/issues/865))
- The LSL currency symbol was corrected. ([\#890](https://github.com/posit-dev/great-tables/issues/890))

#### Enhancements

- `cols_*()` methods no longer raise an error when a list of column names are not all present in the data. ([\#860](https://github.com/posit-dev/great-tables/issues/860))

#### Documentation

- Added a glossary reference page. ([\#862](https://github.com/posit-dev/great-tables/issues/862))
- Added documentation for `loc.footnotes()`. ([\#885](https://github.com/posit-dev/great-tables/issues/885))

## v0.24.0

*2026-08-24* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.24.0)

Great Tables `v0.24.0` introduces interactive tables, letting users sort, search, filter, and paginate directly in the browser. A single call to `opt_interactive()` transforms any GT table into a client-side interactive widget while preserving all existing formatting and styling.

#### New Features

- **Interactive tables** -- The new `opt_interactive()` method enables column sorting, global search, per-column filters, pagination, row highlighting, etc. Works well with Jupyter, Quarto, and Shiny. ([\#856](https://github.com/posit-dev/great-tables/issues/856))

#### Bug Fixes

- Three incorrect parameter names in docstrings were corrected. ([\#853](https://github.com/posit-dev/great-tables/issues/853))

## v0.23.0

*2026-07-27* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.23.0)

Great Tables `v0.23.0` adds new table management and formatting capabilities. This release introduces `rm_*()` methods for selectively removing table components, a `tab_stub_indent()` method for controlling row label hierarchy, and the `fmt_number_si()` formatter for rendering values with SI (metric) prefixes like kilo, mega, and milli. A targeted bug fix for footnote resolution on spanners is also included.

#### New Features

- **`rm_*()` methods** -- New methods (`rm_header()`, `rm_stubhead()`, `rm_source_notes()`, `rm_footnotes()`, `rm_spanners()`) allow selective removal of table components, making it easier to reshape tables received from other functions or saved objects. ([\#847](https://github.com/posit-dev/great-tables/issues/847))

- **`tab_stub_indent()`** -- Control indentation of row labels in the stub to establish visual hierarchy. Supports explicit integer levels (0-5) or `"increase"`/`"decrease"` keyword directives for fine-grained control. ([\#849](https://github.com/posit-dev/great-tables/issues/849))

- **`fmt_number_si()`** -- Format numeric values with SI (International System of Units) prefixes, automatically selecting the appropriate prefix (e.g., k, M, G, m, µ, n) to keep values readable. Supports unit designation, engineering/decimal prefix modes, significant figures, and locale-aware formatting. Also available as `vals.fmt_number_si()`. ([\#851](https://github.com/posit-dev/great-tables/issues/851))

#### Bug Fixes

- Footnotes targeting a spanner with a different `id` compared to its `label` are now correctly resolved. ([\#844](https://github.com/posit-dev/great-tables/issues/844))

## v0.22.0

*2026-06-12* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.22.0)

Great Tables `v0.22.0` is a feature-rich release that greatly expands the formatting, text manipulation, and export capabilities of the library. Highlights include new methods for footnotes, duration formatting, parts-per notation, summary rows, and specialized column merges. A new suite of `text_*()` methods provides powerful cell-content transformations, while `gtsave()` replaces the deprecated `save()` with a modern headless-Chrome export pipeline. LaTeX output now supports stubs, row groups, and Markdown/HTML conversion. Pandas is no longer a required dependency--Polars-only usage is fully supported.

#### New Features

- **`tab_footnote()`** -- Add table footnotes with automatic, sequentially-ordered marks (symbols, numbers, or letters) attached to targeted cells. Supports placement control and styled text via `md()` and `html()`. ([\#763](https://github.com/posit-dev/great-tables/issues/763))
- **`fmt_duration()`** -- Format duration values in narrow (`5d 3h`), wide (`5 days, 3 hours`), colon-separated (`02:15:30`), or ISO 8601 styles. Auto-detects Polars `Duration` dtype and supports locale-aware plural forms. ([\#831](https://github.com/posit-dev/great-tables/issues/831))
- **`fmt_partsper()`** -- Format values as parts-per quantities (per-mille ‰, ppm, ppb, ppt, and more) with automatic scaling and context-aware symbol rendering for HTML and LaTeX. ([\#837](https://github.com/posit-dev/great-tables/issues/837))
- **`cols_reorder()`** -- Completely rearrange all table columns in a single call, replacing multiple `cols_move_*()` invocations for full reordering. ([\#625](https://github.com/posit-dev/great-tables/issues/625))
- **`cols_merge_*()` methods** -- Specialized column merge variants: `cols_merge_uncert()` for value ± uncertainty, `cols_merge_range()` for begin-end ranges, `cols_merge_n_pct()` for count (percent) pairs, and the generic `cols_merge()` with pattern templating. ([\#832](https://github.com/posit-dev/great-tables/issues/832))
- **`summary_rows()`** -- Add group-wise summary rows (e.g., totals, means) above or below each row group, with support for Polars expressions and custom aggregation functions. ([\#834](https://github.com/posit-dev/great-tables/issues/834))
- **`text_transform()` and `text_*()` methods** -- New text manipulation suite: `text_transform()` for custom functions, `text_replace()` for regex substitution, `text_case_match()` for switch-like replacements, and `text_case_when()` for predicate-based logic. ([\#835](https://github.com/posit-dev/great-tables/issues/835), [\#836](https://github.com/posit-dev/great-tables/issues/836))
- **Substitution family methods** -- Replace specific cell values with `sub_missing()`, `sub_zero()`, `sub_small_vals()`, `sub_large_vals()`, and `sub_values()` for clean, readable tables. ([\#833](https://github.com/posit-dev/great-tables/issues/833))
- **`gtsave()`** -- Save tables to PNG, JPEG, WebP, or PDF using headless Chrome with viewport, zoom, and padding controls. Replaces the deprecated `save()` method. ([\#841](https://github.com/posit-dev/great-tables/issues/841))

#### Enhancements

- LaTeX output now fully supports stubs and row groups, including spanning headers and row-group-as-column layout. ([\#784](https://github.com/posit-dev/great-tables/issues/784))
- Markdown and HTML content is now converted to LaTeX equivalents during LaTeX rendering. ([\#803](https://github.com/posit-dev/great-tables/issues/803))
- Nanoplot scaling now correctly respects row selections rather than scaling across all data. ([\#404](https://github.com/posit-dev/great-tables/issues/404))
- Pandas is no longer a required dependency--Great Tables works with Polars alone for lightweight installs. ([\#839](https://github.com/posit-dev/great-tables/issues/839))

#### Bug Fixes

- Polars container dtype entries (e.g., lists) are now correctly converted in `_get_cell`. ([\#794](https://github.com/posit-dev/great-tables/issues/794))
- PyArrow array slicing in `data_color` now works correctly. ([\#741](https://github.com/posit-dev/great-tables/issues/741))
- A charset meta tag is now prepended to HTML output in `save()` for proper encoding. ([\#823](https://github.com/posit-dev/great-tables/issues/823))
- Nanoplot number streams now gracefully handle `nan` values. ([\#838](https://github.com/posit-dev/great-tables/issues/838))
- Removed the internal `NpNan` backend in favor of expanded normalization logic. ([\#840](https://github.com/posit-dev/great-tables/issues/840))

#### Documentation

- Added a SEPTA timetable blog post demonstrating real-world table construction. ([\#636](https://github.com/posit-dev/great-tables/issues/636))
- Fixed a formatting issue in the `fmt_threshold()` docstring. ([\#821](https://github.com/posit-dev/great-tables/issues/821))
- Migrated the documentation site to Great Docs as the website generator. ([\#842](https://github.com/posit-dev/great-tables/issues/842))
- Updated the User Guide with coverage of new features. ([\#843](https://github.com/posit-dev/great-tables/issues/843))

#### New Contributors

- [@KristijanArmeni](https://github.com/KristijanArmeni) made their first contribution in https://github.com/posit-dev/great-tables/pull/794
- [@mrapacz](https://github.com/mrapacz) made their first contribution in https://github.com/posit-dev/great-tables/pull/823
- [@minimav](https://github.com/minimav) made their first contribution in https://github.com/posit-dev/great-tables/pull/404
- [@jiboncom](https://github.com/jiboncom) made their first contribution in https://github.com/posit-dev/great-tables/pull/803

## v0.21.0

*2026-03-03* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.21.0)

This release adds `cols_merge()` for combining cell contents across columns, `cols_label_with()` for function-based relabeling, `fmt_engineering()` for engineering notation, and `opt_css()` for injecting custom CSS rules.

#### Deprecations

- `opt_all_caps()` now uses `loc.column_labels`, `loc.stub`, and `loc.row_groups` for the `locations=` argument. String-based locations still work but trigger a deprecation warning. ([\#436](https://github.com/posit-dev/great-tables/issues/436), [@jrycw](https://github.com/jrycw))

#### New Features

- **`cols_merge()` method** -- Combine cell contents across two or more columns using format patterns. ([\#780](https://github.com/posit-dev/great-tables/issues/780))
- **`cols_label_with()` method** -- Relabel columns using a function (e.g., `str.upper`, `str.replace`). ([\#816](https://github.com/posit-dev/great-tables/issues/816))
- **`fmt_engineering()` method** -- Format values in engineering notation (exponents that are multiples of 3). ([\#786](https://github.com/posit-dev/great-tables/issues/786))
- **`opt_css()` method** -- Define arbitrary CSS rules for an HTML table. ([\#775](https://github.com/posit-dev/great-tables/issues/775))
- **Container padding in `tab_options()`** -- Set padding around the table container element. ([\#802](https://github.com/posit-dev/great-tables/issues/802), [@thriller08](https://github.com/thriller08))

#### Bug Fixes

- Refactored internal auto-align code for Pandas 3.0.0 compatibility. ([\#810](https://github.com/posit-dev/great-tables/issues/810))
- Added `int` to the `RowSelectExpr` type definition. ([\#800](https://github.com/posit-dev/great-tables/issues/800), [@tylerriccio33](https://github.com/tylerriccio33))
- Updated the Polars selector type annotation to use `Selector`. ([\#770](https://github.com/posit-dev/great-tables/issues/770), [@schmidma](https://github.com/schmidma))
- Annotated the `pipe()` method's first argument type as `GT`. ([\#757](https://github.com/posit-dev/great-tables/issues/757), [@FBruzzesi](https://github.com/FBruzzesi))
- `interactive_data_values=` is now handled correctly in nanoplots. ([\#792](https://github.com/posit-dev/great-tables/issues/792), [@lorenzo-w](https://github.com/lorenzo-w))
- Group labels are now properly modified when `render_formats()` is called. ([\#769](https://github.com/posit-dev/great-tables/issues/769), [@juleswg23](https://github.com/juleswg23))

#### Documentation

- Added docs for `val_fmt_engineering()`. ([\#808](https://github.com/posit-dev/great-tables/issues/808), [@jrycw](https://github.com/jrycw))
- Corrected the `fns=` parameter docs in `fmt()`. ([\#818](https://github.com/posit-dev/great-tables/issues/818))
- Improved docs for the `from_column()` function. ([\#766](https://github.com/posit-dev/great-tables/issues/766), [@jrycw](https://github.com/jrycw))
- Added a gt-extras example to the Examples page. ([\#759](https://github.com/posit-dev/great-tables/issues/759), [@juleswg23](https://github.com/juleswg23))
- Added an example demonstrating `define_units()`. ([\#446](https://github.com/posit-dev/great-tables/issues/446), [@jrycw](https://github.com/jrycw))

#### Internal

- Updated copyright end year to 2026. ([\#804](https://github.com/posit-dev/great-tables/issues/804))
- Fixed several typos. ([\#798](https://github.com/posit-dev/great-tables/issues/798), [@kianmeng](https://github.com/kianmeng))
- Added Plausible analytics to the project website. ([\#806](https://github.com/posit-dev/great-tables/issues/806))
- Added tests for `opt_all_caps()`. ([\#812](https://github.com/posit-dev/great-tables/issues/812))
- Fixed the checkout version tag in CI. ([\#768](https://github.com/posit-dev/great-tables/issues/768), [@juleswg23](https://github.com/juleswg23))

#### New Contributors

- [@kianmeng](https://github.com/kianmeng) made their first contribution in https://github.com/posit-dev/great-tables/pull/798
- [@thriller08](https://github.com/thriller08) made their first contribution in https://github.com/posit-dev/great-tables/pull/802
- [@schmidma](https://github.com/schmidma) made their first contribution in https://github.com/posit-dev/great-tables/pull/770
- [@lorenzo-w](https://github.com/lorenzo-w) made their first contribution in https://github.com/posit-dev/great-tables/pull/792

## v0.20.0

*2025-10-31* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.20.0)

This release adds the `grand_summary_rows()` method for table-wide aggregation rows and Polars expression support in `vals` functions.

#### New Features

- **`grand_summary_rows()` method** -- Add summary rows at the bottom of the entire table for grand totals and other aggregate statistics. ([\#765](https://github.com/posit-dev/great-tables/issues/765), [@juleswg23](https://github.com/juleswg23))
- **Polars expressions in `vals` functions** -- The `vals` module now accepts Polars expressions for more flexible value formatting. ([\#793](https://github.com/posit-dev/great-tables/issues/793))

## v0.19.0

*2025-10-07* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.19.0)

This release removes NumPy from the dependencies list, fixes `row_group_as_column` to work as intended, and improves color contrast in `data_color()` and row striping.

#### Enhancements

- NumPy has been removed as a dependency; all NumPy usage replaced with standard Python. ([\#749](https://github.com/posit-dev/great-tables/issues/749), [@tylerriccio33](https://github.com/tylerriccio33))
- `row_group_as_column=True` now correctly structures row groups as a column in the stub (previously a no-op). ([\#754](https://github.com/posit-dev/great-tables/issues/754), [@juleswg23](https://github.com/juleswg23))
- PyArrow `float64` columns are now right-aligned by default, matching Pandas and Polars behavior. ([\#734](https://github.com/posit-dev/great-tables/issues/734), [@FBruzzesi](https://github.com/FBruzzesi))

#### Bug Fixes

- Fixed an error when setting `groupname_col=` without `rowname_col=` in the `GT` constructor. ([\#756](https://github.com/posit-dev/great-tables/issues/756), [@juleswg23](https://github.com/juleswg23))
- `data_color()` now accounts for the alpha value of cell background colors when choosing foreground text color. ([\#747](https://github.com/posit-dev/great-tables/issues/747), [@juleswg23](https://github.com/juleswg23))
- Row striping now has better color contrast between text and the cell background. ([\#745](https://github.com/posit-dev/great-tables/issues/745), [@juleswg23](https://github.com/juleswg23))
- Column names are now accessed consistently via `get_column_names()` instead of `.columns`. ([\#736](https://github.com/posit-dev/great-tables/issues/736), [@FBruzzesi](https://github.com/FBruzzesi))
- Avoided double use of `clear` internally with Polars DataFrames. ([\#729](https://github.com/posit-dev/great-tables/issues/729), [@FBruzzesi](https://github.com/FBruzzesi))

#### Documentation

- Corrected various typos. ([\#730](https://github.com/posit-dev/great-tables/issues/730), [@FBruzzesi](https://github.com/FBruzzesi))
- Added a Posit badge to the project website header. ([\#777](https://github.com/posit-dev/great-tables/issues/777))

#### Internal

- Refactored code for better adherence to best practices and improved performance. ([\#731](https://github.com/posit-dev/great-tables/issues/731), [@FBruzzesi](https://github.com/FBruzzesi))

#### New Contributors

- [@FBruzzesi](https://github.com/FBruzzesi) made their first contribution in https://github.com/posit-dev/great-tables/pull/731

## v0.18.0

*2025-07-10* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.18.0)

This release introduces `tab_spanner_delim()` for automatic spanner creation from delimited column names, rotatable column labels, boolean formatting with `fmt_tf()`, and custom datetime format strings. Tables can now be pickled for serialization.

#### New Features

- **`tab_spanner_delim()` method** -- Automatically create column spanners by splitting column names on a delimiter. ([\#647](https://github.com/posit-dev/great-tables/issues/647))
- **`cols_label_rotate()` method** -- Rotate column label text 90 degrees for compact headers. ([\#696](https://github.com/posit-dev/great-tables/issues/696), [@juleswg23](https://github.com/juleswg23))
- **`fmt_tf()` method** -- Format boolean values with customizable true/false representations. ([\#665](https://github.com/posit-dev/great-tables/issues/665), [\#704](https://github.com/posit-dev/great-tables/issues/704))
- **Custom datetime format strings** -- `fmt_datetime()` now accepts a `format_str=` parameter for arbitrary datetime formatting. ([\#645](https://github.com/posit-dev/great-tables/issues/645))
- **Pickle support** -- GT tables can now be serialized with `pickle`. ([\#641](https://github.com/posit-dev/great-tables/issues/641), [@jrycw](https://github.com/jrycw))
- **Compact currency formatting** -- `fmt_currency()` gained a `compact=` parameter (e.g., `$13.4M`). ([\#664](https://github.com/posit-dev/great-tables/issues/664))
- **`truncate=` option in `data_color()`** -- Truncate values to the domain bounds instead of erroring on out-of-range data. ([\#673](https://github.com/posit-dev/great-tables/issues/673), [@mahdibaghbanzadeh](https://github.com/mahdibaghbanzadeh))

#### Enhancements

- Removed the Pandas dependency from `vals.fmt_integer()`. ([\#719](https://github.com/posit-dev/great-tables/issues/719))

#### Bug Fixes

- Fixed an off-by-one bug in `rescale_factor()` that affected `data_color()` output. ([\#718](https://github.com/posit-dev/great-tables/issues/718), [@juleswg23](https://github.com/juleswg23))
- Google Fonts import statements are no longer duplicated in HTML output. ([\#708](https://github.com/posit-dev/great-tables/issues/708))
- Fixed row striping applying to incorrect rows due to an indexing issue. ([\#701](https://github.com/posit-dev/great-tables/issues/701), [@juleswg23](https://github.com/juleswg23))
- Spanners can now be correctly styled with `tab_style()`. ([\#695](https://github.com/posit-dev/great-tables/issues/695), [@ChristopherRussell](https://github.com/ChristopherRussell))
- Removed unused `sep_mark=` parameter from `fmt_scientific()`. ([\#642](https://github.com/posit-dev/great-tables/issues/642))

#### Documentation

- Added note about using `.show("browser")` in VS Code. ([\#643](https://github.com/posit-dev/great-tables/issues/643))
- Suppressed a `cols_width()` warning that appeared in the docs. ([\#659](https://github.com/posit-dev/great-tables/issues/659), [@jrycw](https://github.com/jrycw))
- Updated docstrings for date/time formatting methods. ([\#658](https://github.com/posit-dev/great-tables/issues/658))
- Improved interlinking with quartodoc. ([\#697](https://github.com/posit-dev/great-tables/issues/697))
- Added underline to active link in top navigation bar. ([\#706](https://github.com/posit-dev/great-tables/issues/706))
- Improved documentation for `as_raw_html()`. ([\#707](https://github.com/posit-dev/great-tables/issues/707))
- Better introduction of the `show()` method via a callout. ([\#712](https://github.com/posit-dev/great-tables/issues/712))

#### Internal

- Added a no-Pandas dependency test for functions in the `vals` module. ([\#689](https://github.com/posit-dev/great-tables/issues/689))

#### New Contributors

- [@dpprdan](https://github.com/dpprdan) made their first contribution in https://github.com/posit-dev/great-tables/pull/670
- [@juleswg23](https://github.com/juleswg23) made their first contribution in https://github.com/posit-dev/great-tables/pull/696
- [@ChristopherRussell](https://github.com/ChristopherRussell) made their first contribution in https://github.com/posit-dev/great-tables/pull/695
- [@mahdibaghbanzadeh](https://github.com/mahdibaghbanzadeh) made their first contribution in https://github.com/posit-dev/great-tables/pull/673

## v0.17.0

*2025-03-11* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.17.0)

This release adds Quarto integration with a table-processing disable option, a new `cols_unhide()` method, and ensures unique HTML ID attributes for tables. The `css-inline` package is now an optional extra.

#### Breaking Changes

- HTML ID attributes are now unique per table, which may affect code that relied on the previous static ID. ([\#607](https://github.com/posit-dev/great-tables/issues/607), [@BenGale93](https://github.com/BenGale93))
- The `css-inline` package has been moved to an extras group (`pip install great_tables[extra]`). ([\#634](https://github.com/posit-dev/great-tables/issues/634))

#### New Features

- **Quarto table-processing option** -- Disable Quarto's default table processing and receive a warning on render when needed. ([\#611](https://github.com/posit-dev/great-tables/issues/611))
- **`cols_unhide()` method** -- Reveal previously hidden columns. ([\#629](https://github.com/posit-dev/great-tables/issues/629), [@jrycw](https://github.com/jrycw))
- **`inline_css=` argument** -- Inline CSS directly on table elements for constrained output contexts. ([\#633](https://github.com/posit-dev/great-tables/issues/633), [@tylerriccio33](https://github.com/tylerriccio33))

#### Bug Fixes

- Screenshots are no longer always saved as PNG regardless of the specified format. ([\#599](https://github.com/posit-dev/great-tables/issues/599))
- Resolved an encoding issue in `GT.save()`. ([\#609](https://github.com/posit-dev/great-tables/issues/609), [@jrycw](https://github.com/jrycw))
- Non-integer values are now correctly passed to nanoplot options. ([\#608](https://github.com/posit-dev/great-tables/issues/608), [@tylerriccio33](https://github.com/tylerriccio33))
- Fixed scientific notation zero padding when `exp_style=` is used (e.g., `"2.3E-03"` was incorrectly displayed as `"2.3E−30"`). ([\#622](https://github.com/posit-dev/great-tables/issues/622))
- Fixed nanoplot code to guard against string values (single string or list containing strings). ([\#623](https://github.com/posit-dev/great-tables/issues/623))

#### Documentation

- Updated docs for the `mask=` parameter in `loc.body()`. ([\#589](https://github.com/posit-dev/great-tables/issues/589), [@jrycw](https://github.com/jrycw))
- Updated the preview of the `year` column in the `gtcars` dataset. ([\#587](https://github.com/posit-dev/great-tables/issues/587), [@jrycw](https://github.com/jrycw))
- Added examples to the documentation. ([\#618](https://github.com/posit-dev/great-tables/issues/618), [@jrycw](https://github.com/jrycw))
- Added `style.css` entry to the API reference. ([\#624](https://github.com/posit-dev/great-tables/issues/624))
- Aligned the *Getting Started* guide with the README. ([\#627](https://github.com/posit-dev/great-tables/issues/627), [@zachvalenta](https://github.com/zachvalenta))

#### Internal

- Added a `deploy-pypi` environment with deployment protection rules for release workflow review. ([\#590](https://github.com/posit-dev/great-tables/issues/590))

#### New Contributors

- [@tylerriccio33](https://github.com/tylerriccio33) made their first contribution in https://github.com/posit-dev/great-tables/pull/608
- [@BenGale93](https://github.com/BenGale93) made their first contribution in https://github.com/posit-dev/great-tables/pull/607
- [@zachvalenta](https://github.com/zachvalenta) made their first contribution in https://github.com/posit-dev/great-tables/pull/627

## v0.16.1

*2025-01-24* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.16.1)

Great Tables `v0.16.1` is a patch release with a single data fix.

#### Bug Fixes

- Updated the `year` column dtype in the `gtcars` dataset. ([\#586](https://github.com/posit-dev/great-tables/issues/586))

## v0.16.0

*2025-01-24* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.16.0)

This release introduces the `mask=` argument for enhanced body cell targeting and a `write_raw_html()` helper for convenient HTML file output.

#### New Features

- **`mask=` argument in `loc.body()`** -- Target specific body cells using a boolean mask for more flexible styling and formatting. ([\#566](https://github.com/posit-dev/great-tables/issues/566), [@jrycw](https://github.com/jrycw))
- **`write_raw_html()` helper** -- Write table HTML output directly to a file without manual string handling. ([\#485](https://github.com/posit-dev/great-tables/issues/485), [@jrycw](https://github.com/jrycw))

#### Bug Fixes

- Fixed a deprecation warning in `as_raw_html()` for Python 3.13. ([\#563](https://github.com/posit-dev/great-tables/issues/563), [@stinodego](https://github.com/stinodego))
- Nanoplots now support the `pl.UInt` type. ([\#577](https://github.com/posit-dev/great-tables/issues/577), [@jrycw](https://github.com/jrycw))

#### Documentation

- Added pyOpenSci and DOI badges to the README to acknowledge successful peer review. ([\#576](https://github.com/posit-dev/great-tables/issues/576))
- Updated images and text for included datasets. ([\#562](https://github.com/posit-dev/great-tables/issues/562))
- Replaced JSON dataset with `.ndjson` file in coffee sales examples to fix a serialization error. ([\#580](https://github.com/posit-dev/great-tables/issues/580))

#### New Contributors

- [@stinodego](https://github.com/stinodego) made their first contribution in https://github.com/posit-dev/great-tables/pull/563

## v0.15.0

*2024-12-14* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.15.0)

This release brings several new formatting methods (`fmt_flag()` for country flags, `fmt_icon()` for FontAwesome icons), and accounting notation in numeric formatters. PyArrow tables are now experimentally supported as input, `as_raw_html()` can inline CSS, and the new `pipe()` method enables functional composition in table-building pipelines.

#### New Features

- **`fmt_flag()` method** -- Display country flag icons in table cells based on country codes. ([\#523](https://github.com/posit-dev/great-tables/issues/523))
- **`fmt_icon()` method** -- Render FontAwesome icons within table cells. ([\#515](https://github.com/posit-dev/great-tables/issues/515))
- **Accounting notation** -- `fmt_number()`, `fmt_percent()`, `fmt_integer()`, and `fmt_currency()` now support accounting notation for negative values. ([\#513](https://github.com/posit-dev/great-tables/issues/513))
- **PyArrow table support (experimental)** -- Use a `pyarrow.Table` as input data. ([\#487](https://github.com/posit-dev/great-tables/issues/487), [@amol](https://github.com/amol)-)
- **Inline CSS in `as_raw_html()`** -- New `inline_css=` argument writes CSS-inlined HTML strings for email and other constrained environments. ([\#557](https://github.com/posit-dev/great-tables/issues/557))
- **`pipe()` method** -- Chain custom functions in a table pipeline, similar to the Pandas and Polars `pipe()` APIs. ([\#363](https://github.com/posit-dev/great-tables/issues/363), [@jrycw](https://github.com/jrycw))
- **Enhanced `save()` method** -- Now supports intermediate saves by returning `self`, enabling chained workflows. ([\#499](https://github.com/posit-dev/great-tables/issues/499), [@jrycw](https://github.com/jrycw))
- **HTTP/HTTPS support in `fmt_image()`** -- The `columns=` parameter now supports URLs with `http`/`https` schemes. ([\#520](https://github.com/posit-dev/great-tables/issues/520), [@jrycw](https://github.com/jrycw))

#### Bug Fixes

- Hidden columns with column width definitions no longer mangle HTML table output. ([\#509](https://github.com/posit-dev/great-tables/issues/509))
- Improved detection of Polars installation. ([\#505](https://github.com/posit-dev/great-tables/issues/505), [@lukemanley](https://github.com/lukemanley))
- Fixed missing exception raise in `_val_is_numeric()` and `_val_is_str()`. ([\#510](https://github.com/posit-dev/great-tables/issues/510), [@jrycw](https://github.com/jrycw))

#### Documentation

- Added `CITATION.cff` and citation information to the README. ([\#551](https://github.com/posit-dev/great-tables/issues/551))
- Updated README with conda install instructions and usage environment details. ([\#552](https://github.com/posit-dev/great-tables/issues/552))
- Improved presentation of Contributing Guidelines. ([\#550](https://github.com/posit-dev/great-tables/issues/550))
- Added information about Pandas requirement when using internal datasets. ([\#549](https://github.com/posit-dev/great-tables/issues/549), [\#559](https://github.com/posit-dev/great-tables/issues/559))
- Included `vals.fmt_image()` in the API reference. ([\#486](https://github.com/posit-dev/great-tables/issues/486), [@jrycw](https://github.com/jrycw))
- Fixed spelling in the contributing guide. ([\#516](https://github.com/posit-dev/great-tables/issues/516), [@glemaitre](https://github.com/glemaitre))

#### Internal

- Switched to ruff for linting and formatting, and fixed `mypy` errors. ([\#511](https://github.com/posit-dev/great-tables/issues/511), [@jrycw](https://github.com/jrycw))
- Standardized imports by converting to relative imports. ([\#521](https://github.com/posit-dev/great-tables/issues/521), [@jrycw](https://github.com/jrycw))
- Added CI build for Python 3.13. ([\#514](https://github.com/posit-dev/great-tables/issues/514), [@glemaitre](https://github.com/glemaitre))
- Fixed CI README badge to report build status correctly. ([\#553](https://github.com/posit-dev/great-tables/issues/553))
- Excluded `if TYPE_CHECKING:` lines from coverage reports. ([\#556](https://github.com/posit-dev/great-tables/issues/556))

#### New Contributors

- [@lukemanley](https://github.com/lukemanley) made their first contribution in https://github.com/posit-dev/great-tables/pull/505
- [@glemaitre](https://github.com/glemaitre) made their first contribution in https://github.com/posit-dev/great-tables/pull/514
- [@amol](https://github.com/amol)- made their first contribution in https://github.com/posit-dev/great-tables/pull/487

## v0.14.0

*2024-11-11* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.14.0)

This release adds experimental LaTeX output support, enabling tables to be rendered as LaTeX code for use in scientific documents and publications.

#### New Features

- **`.as_latex()` method (experimental)** -- Render tables as LaTeX code for inclusion in LaTeX documents and PDF pipelines. See the [API reference](https://posit-dev.github.io/great-tables/reference/GT.as_latex.html) for current limitations. ([\#481](https://github.com/posit-dev/great-tables/issues/481))

#### Documentation

- Improved API reference layout on lower-width devices. ([\#427](https://github.com/posit-dev/great-tables/issues/427), [\#492](https://github.com/posit-dev/great-tables/issues/492))
- Added preview sections for built-in datasets. ([\#453](https://github.com/posit-dev/great-tables/issues/453), [@jrycw](https://github.com/jrycw))

## v0.13.0

*2024-10-04* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.13.0)

This release adds granular section restyling via convenience methods, image rendering in non-body components through `val_fmt_image()`, and the ability to pass a webdriver instance directly to `.save()`.

#### New Features

- **Granular section restyling** -- Convenience API for restyling individual table sections (header, body, footer, etc.) without touching global options. ([\#341](https://github.com/posit-dev/great-tables/issues/341), [@timkpaine](https://github.com/timkpaine))
- **`val_fmt_image()`** -- Render images in table components beyond the body (e.g., column labels, spanners). ([\#451](https://github.com/posit-dev/great-tables/issues/451), [@jrycw](https://github.com/jrycw))
- **Webdriver passthrough in `.save()`** -- Pass an existing webdriver instance to `.save()` for reuse across multiple exports. ([\#478](https://github.com/posit-dev/great-tables/issues/478))

#### Bug Fixes

- Global `locale` is now respected in all `fmt_*()` methods. ([\#473](https://github.com/posit-dev/great-tables/issues/473), [@jrycw](https://github.com/jrycw))
- Fixed headers causing their CSS classes to be printed in the output. ([\#477](https://github.com/posit-dev/great-tables/issues/477))

#### Documentation

- Added `google_font()` helper to the API reference. ([\#464](https://github.com/posit-dev/great-tables/issues/464), [\#471](https://github.com/posit-dev/great-tables/issues/471), [@jrycw](https://github.com/jrycw))
- Updated docs and code to support `GoogleFont` in `opt_table_font()`. ([\#470](https://github.com/posit-dev/great-tables/issues/470), [@jrycw](https://github.com/jrycw))
- Added docstrings for new location methods. ([\#474](https://github.com/posit-dev/great-tables/issues/474), [@jrycw](https://github.com/jrycw))
- Fixed deprecated warning for `pl.DataFrame.pivot()`. ([\#472](https://github.com/posit-dev/great-tables/issues/472))
- GT members are no longer documented inline on the reference page. ([\#475](https://github.com/posit-dev/great-tables/issues/475))

## v0.12.0

*2024-09-27* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.12.0)

This release adds Google Fonts integration and row striping support, with `opt_stylize()` now producing striped tables by default.

#### Breaking Changes

- `opt_stylize()` now produces row stripes by default. Set `add_row_striping=False` to remove them. ([\#461](https://github.com/posit-dev/great-tables/issues/461))
- `opt_stylize()` now adds borders to certain styles, matching the original design intent. ([\#463](https://github.com/posit-dev/great-tables/issues/463))

#### New Features

- **`google_font()` helper** -- Easily use Google Fonts in `opt_table_font()` and `style.text()`. ([\#423](https://github.com/posit-dev/great-tables/issues/423))
- **Row striping options** -- Configure row striping behavior through `opt_stylize()` and related options. ([\#461](https://github.com/posit-dev/great-tables/issues/461), [\#463](https://github.com/posit-dev/great-tables/issues/463))

#### Bug Fixes

- `.show()` now uses a full HTML page for correct UTF-8 display. ([\#458](https://github.com/posit-dev/great-tables/issues/458))

#### Documentation

- Updated the Super Bowl example to align with the latest version of Polars. ([\#460](https://github.com/posit-dev/great-tables/issues/460), [\#462](https://github.com/posit-dev/great-tables/issues/462), [@jrycw](https://github.com/jrycw))

## v0.11.1

*2024-09-20* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.11.1)

### Fixes

- Do not error when URL string supplied to `path=` argument in `fmt_image()` by [@jrycw](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/444
- Include an `encoding=` arg in `GT.save()` (with default `"utf-8"`) for more dependable saving in Windows by [@jrycw](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/454
- Unify the method signatures of `cols_label()` and `cols_width()` by having them both accept `cases=` and `**kwargs` by [@jrycw](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/452

### Chores

- Standardize on the `GTSelf` object in method signatures by [@jrycw](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/431
- Consistently use `isinstance()` checks throughout the codebase instead of checking with `hasattr()` by [@rich-iannone](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/434
- Improve test coverage for various `opt_*` methods by [@jrycw](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/437
- Consolidate ordered list code using the new `_create_ordered_list()` function by [@jrycw](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/407
- Internally use `OrderedSet().as_list()` instead of `list(OrderedSet())` for sake of clarity by [@jrycw](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/447
- Refactor import statements throughout the `_formats.py` file by [@jrycw](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/450

### Docs

- Update import statement in the `GT.data_color()` example by [@jrycw](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/432
- Indicate that `tab_spanner()` allows for use of units notation in its `label=` argument by [@rich-iannone](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/426
- Visually document options for theming table with `opt_stylize()` by [@rich-iannone](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/438
- Provide updates to PyCon- and SciPy-related blog posts by [@rich-iannone](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/445

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.11.0…v0.11.1](https://github.com/posit-dev/great-tables/compare/v0.11.0...v0.11.1)

## v0.11.0

*2024-08-30* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.11.0)

This release restructures the HTML output so that `<thead>` properly encloses both the title/subtitle and column labels, and fixes `.save()` compatibility with the latest version of Google Chrome.

#### Breaking Changes

- The `<thead>` element now encloses both title/subtitle and column label rows. This improves semantic correctness but may affect custom CSS targeting the old structure. ([\#421](https://github.com/posit-dev/great-tables/issues/421))

#### Bug Fixes

- `.save()` now works with the latest version of Google Chrome. ([\#425](https://github.com/posit-dev/great-tables/issues/425))

#### Documentation

- Mentioned Polars support in the *Get Started* section. ([\#408](https://github.com/posit-dev/great-tables/issues/408), [@jrycw](https://github.com/jrycw))
- Fixed typos and improved a code example in the "Design Philosophy" doc. ([\#401](https://github.com/posit-dev/great-tables/issues/401), [@alfredocarella](https://github.com/alfredocarella))
- Fixed a typo in a blog post. ([\#396](https://github.com/posit-dev/great-tables/issues/396))
- Updated documentation for datasets. ([\#397](https://github.com/posit-dev/great-tables/issues/397), [@jrycw](https://github.com/jrycw))
- Updated Polars examples for a deprecated argument. ([\#400](https://github.com/posit-dev/great-tables/issues/400), [@atseewal](https://github.com/atseewal))
- Removed mentions of `accounting` in `force_sign=` argument docs. ([\#422](https://github.com/posit-dev/great-tables/issues/422))

#### New Contributors

- [@alfredocarella](https://github.com/alfredocarella) made their first contribution in https://github.com/posit-dev/great-tables/pull/401

## v0.10.0

*2024-07-08* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.10.0)

This release adds units notation support in column labels and spanners, a new `opt_table_font()` method, the `.show()` method for interactive display, and several new built-in datasets.

#### New Features

- **Units notation in `cols_label()`** -- Express measurement units directly in column labels using the units notation syntax. ([\#380](https://github.com/posit-dev/great-tables/issues/380))
- **Units notation in `tab_spanner()`** -- Spanner labels can also use units notation for scientific and technical headers. ([\#393](https://github.com/posit-dev/great-tables/issues/393))
- **`opt_table_font()` method** -- Easily set a default font for the entire table. ([\#272](https://github.com/posit-dev/great-tables/issues/272))
- **`.show()` method** -- Display a table interactively in notebooks and other environments. ([\#379](https://github.com/posit-dev/great-tables/issues/379))
- **New datasets** -- Several new built-in datasets added, bringing the total to 16. ([\#382](https://github.com/posit-dev/great-tables/issues/382))

#### Bug Fixes

- Fixed `fmt_percent()` issue with Polars `u64-idx` builds. ([\#388](https://github.com/posit-dev/great-tables/issues/388), [@lostmygithubaccount](https://github.com/lostmygithubaccount))
- Added render target for HTML pages. ([\#377](https://github.com/posit-dev/great-tables/issues/377), [@isabelizimm](https://github.com/isabelizimm))
- `.show()` no longer raises or prints to stderr. ([\#384](https://github.com/posit-dev/great-tables/issues/384))

#### Documentation

- Added absolute URLs to README to improve the PyPI project summary. ([\#373](https://github.com/posit-dev/great-tables/issues/373))

#### New Contributors

- [@isabelizimm](https://github.com/isabelizimm) made their first contribution in https://github.com/posit-dev/great-tables/pull/377
- [@lostmygithubaccount](https://github.com/lostmygithubaccount) made their first contribution in https://github.com/posit-dev/great-tables/pull/388

## v0.9.0

*2024-06-06* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.9.0)

This release adds row subsetting to `data_color()`, allowing color scales to be applied to specific rows.

#### New Features

- **Row selection in `data_color()`** -- A `rows=` argument enables applying color scales to a subset of rows rather than the entire column. ([\#364](https://github.com/posit-dev/great-tables/issues/364), [@jrycw](https://github.com/jrycw))

#### Breaking Changes

- The `rows=` parameter is now the third positional argument in `data_color()`, which may break code that relied on positional argument order.

## v0.8.0

*2024-06-06* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.8.0)

This release adds method equivalents for several constructor options, allowing them to be set in a chained pipeline rather than only at `GT()` instantiation.

#### New Features

- **`GT.tab_stub()`** -- Set `rowname_col=` and `groupname_col=` as a method call instead of only in the `GT()` constructor. ([\#371](https://github.com/posit-dev/great-tables/issues/371))
- **`GT.with_locale()`** -- Set the locale after construction. ([\#371](https://github.com/posit-dev/great-tables/issues/371))
- **`GT.with_id()`** -- Set the table ID after construction. ([\#371](https://github.com/posit-dev/great-tables/issues/371))

## v0.7.0

*2024-06-04* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.7.0)

This release adds the `fmt_units()` method for rendering scientific units and improves Polars selector compatibility.

#### New Features

- **`fmt_units()` method** -- Format measurement units with proper subscripts, superscripts, and symbols for scientific notation. ([\#240](https://github.com/posit-dev/great-tables/issues/240))
- **Non-strict Polars `expand_selector()` support** -- Polars selectors now use non-strict mode, avoiding errors when selectors match no columns. ([\#368](https://github.com/posit-dev/great-tables/issues/368))

#### Bug Fixes

- General enhancements and fixes to several `cols_*()` methods. ([\#366](https://github.com/posit-dev/great-tables/issues/366), [@jrycw](https://github.com/jrycw))
- Better error message when list data is used incorrectly in `fmt_nanoplot()`. ([\#356](https://github.com/posit-dev/great-tables/issues/356), [@marcozzxx810](https://github.com/marcozzxx810))

#### Documentation

- Added an RSS feed to the blog. ([\#367](https://github.com/posit-dev/great-tables/issues/367), [@jrycw](https://github.com/jrycw))

#### Internal

- Refactored `seq_groups()` to accept `Iterable`. ([\#365](https://github.com/posit-dev/great-tables/issues/365), [@jrycw](https://github.com/jrycw))
- Moved `pairwise()`, `seq_groups()`, and `is_equal()` to `_utils.py`. ([\#369](https://github.com/posit-dev/great-tables/issues/369), [@jrycw](https://github.com/jrycw))

## v0.6.1

*2024-05-23* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.6.1)

Great Tables `v0.6.1` is a patch release fixing compatibility with Polars `v0.20.28` and screenshot export for non-PNG formats.

#### Bug Fixes

- Fixed column selections breaking with Polars v0.20.28. ([\#360](https://github.com/posit-dev/great-tables/issues/360), [@jrycw](https://github.com/jrycw))
- Fixed `_save_screenshot()` failing for non-PNG file formats. ([\#352](https://github.com/posit-dev/great-tables/issues/352), [@jrycw](https://github.com/jrycw))

#### Internal

- Enhanced test coverage. ([\#339](https://github.com/posit-dev/great-tables/issues/339), [@jrycw](https://github.com/jrycw))
- Removed unneeded files. ([\#351](https://github.com/posit-dev/great-tables/issues/351))

## v0.6.0

*2024-05-16* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.6.0)

This release introduces multi-level spanners, allowing column spanners to be nested hierarchically. Table export via `.save()` is now more robust.

#### New Features

- **Multi-level spanners** -- Column spanners can now be nested under other spanners to create hierarchical column groupings. ([\#345](https://github.com/posit-dev/great-tables/issues/345), [@timkpaine](https://github.com/timkpaine))

#### Bug Fixes

- `.save()` now always captures the full table when exporting. ([\#344](https://github.com/posit-dev/great-tables/issues/344))

#### Documentation

- Added an example coffee table with nanoplots. ([\#349](https://github.com/posit-dev/great-tables/issues/349))
- Cleaned up minor formatting issues in the docs. ([\#338](https://github.com/posit-dev/great-tables/issues/338), [@jrycw](https://github.com/jrycw))

#### New Contributors

- [@timkpaine](https://github.com/timkpaine) made their first contribution in https://github.com/posit-dev/great-tables/pull/345

## v0.5.2

*2024-05-13* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/0.5.2)

Great Tables `v0.5.2` is a patch release addressing several bugs in borders, image formatting, and nanoplots.

#### Bug Fixes

- `CellStyleBorders` is now properly constructed when `sides` is set to `"all"`. ([\#326](https://github.com/posit-dev/great-tables/issues/326), [@jrycw](https://github.com/jrycw))
- `fmt_image()` no longer errors on missing values. ([\#329](https://github.com/posit-dev/great-tables/issues/329))
- Nanoplots now work with list columns, and Polars list columns no longer raise an error. ([\#330](https://github.com/posit-dev/great-tables/issues/330))
- Nanoplots no longer fail for lists of large integers. ([\#335](https://github.com/posit-dev/great-tables/issues/335))
- `fmt_number()` no longer inserts an improper comma for 3-digit compact, negative numbers. ([\#335](https://github.com/posit-dev/great-tables/issues/335))

#### Documentation

- Added examples to API reference pages. ([\#328](https://github.com/posit-dev/great-tables/issues/328), [@jrycw](https://github.com/jrycw))

#### Internal

- Removed unused `webcolors` library as a required dependency. ([\#336](https://github.com/posit-dev/great-tables/issues/336), [@marcozzxx810](https://github.com/marcozzxx810))

#### New Contributors

- [@marcozzxx810](https://github.com/marcozzxx810) made their first contribution in https://github.com/posit-dev/great-tables/pull/336

## v0.5.1

*2024-05-03* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.5.1)

Great Tables `v0.5.1` is a maintenance release focused on bug fixes, code quality improvements, and documentation. Special thanks to [@jrycw](https://github.com/jrycw) for an incredible number of contributions.

#### Bug Fixes

- `table_font_color=` in `tab_options()` now correctly accepts named colors. ([\#285](https://github.com/posit-dev/great-tables/issues/285), [@jrycw](https://github.com/jrycw))
- Group label rows now produce valid HTML. ([\#308](https://github.com/posit-dev/great-tables/issues/308))
- Fixed Polars selectors error in `cols_hide()`. ([\#316](https://github.com/posit-dev/great-tables/issues/316), [@jrycw](https://github.com/jrycw))
- `fmt_number()` now handles missing values correctly. ([\#317](https://github.com/posit-dev/great-tables/issues/317), [@jrycw](https://github.com/jrycw))
- Fixed display of integer-like values in nanoplots. ([\#319](https://github.com/posit-dev/great-tables/issues/319), [@jrycw](https://github.com/jrycw))

#### Documentation

- Fixed typos throughout the docs. ([\#286](https://github.com/posit-dev/great-tables/issues/286), [@jrycw](https://github.com/jrycw))
- Added a community example from [@chalg](https://github.com/chalg). ([\#323](https://github.com/posit-dev/great-tables/issues/323))

#### Internal

- Cleaned up implementation of `fmt_nanoplot()` and `data_color()`. ([\#294](https://github.com/posit-dev/great-tables/issues/294), [\#295](https://github.com/posit-dev/great-tables/issues/295), [@jrycw](https://github.com/jrycw))
- Refactored `fmt_time()`, `fmt_date()`, and `fmt_datetime()`. ([\#290](https://github.com/posit-dev/great-tables/issues/290), [@jrycw](https://github.com/jrycw))
- Refactored `letters` and `Letters` functions in helpers. ([\#289](https://github.com/posit-dev/great-tables/issues/289), [@jrycw](https://github.com/jrycw))
- Updated type hints and organized imports. ([\#315](https://github.com/posit-dev/great-tables/issues/315), [@jrycw](https://github.com/jrycw))
- Codebase cleanup and minor improvements. ([\#292](https://github.com/posit-dev/great-tables/issues/292), [\#305](https://github.com/posit-dev/great-tables/issues/305), [@jrycw](https://github.com/jrycw))
- Improved test coverage. ([\#311](https://github.com/posit-dev/great-tables/issues/311), [\#325](https://github.com/posit-dev/great-tables/issues/325), [@jrycw](https://github.com/jrycw))
- Added tests for `cols_align()` and extended Polars expression support. ([\#320](https://github.com/posit-dev/great-tables/issues/320), [@jrycw](https://github.com/jrycw))

## v0.5.0

*2024-04-12* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.5.0)

This release significantly reduces the dependency footprint by removing mizani and pandas as required dependencies, adds substitution methods for missing and zero values, and provides webdriver choice in `.save()`.

#### New Features

- **`sub_missing()` and `sub_zero()` methods** -- Substitute missing or zero values with custom text or symbols. ([\#244](https://github.com/posit-dev/great-tables/issues/244))
- **Webdriver selection in `.save()`** -- Choose between different webdrivers (e.g., Chrome, Firefox) when saving tables as images. ([\#262](https://github.com/posit-dev/great-tables/issues/262))

#### Enhancements

- Removed mizani and pandas as required dependencies, making the package lighter and more flexible. ([\#261](https://github.com/posit-dev/great-tables/issues/261), [\#271](https://github.com/posit-dev/great-tables/issues/271))

#### Bug Fixes

- Fixed incorrect passing of nanoplot options to arguments in `_generate_nanoplot()`. ([\#258](https://github.com/posit-dev/great-tables/issues/258))
- Removed uses of `DataFrame.apply` and deprecated `dtype` methods for better compatibility. ([\#277](https://github.com/posit-dev/great-tables/issues/277))
- Closed file handles that were left open. ([\#281](https://github.com/posit-dev/great-tables/issues/281))

#### Documentation

- Added examples for `fmt_nanoplot()`. ([\#245](https://github.com/posit-dev/great-tables/issues/245))
- Added docs site and Codecov badges to the README. ([\#254](https://github.com/posit-dev/great-tables/issues/254))
- Improved examples in the Examples section. ([\#267](https://github.com/posit-dev/great-tables/issues/267))
- Fixed variable names in the Oceania example. ([\#264](https://github.com/posit-dev/great-tables/issues/264))
- Added warning callout for experimental status. ([\#243](https://github.com/posit-dev/great-tables/issues/243))

#### Internal

- Refactored nanoplot internals. ([\#246](https://github.com/posit-dev/great-tables/issues/246))
- Added more tests for formatting methods. ([\#260](https://github.com/posit-dev/great-tables/issues/260))
- Added CodeCov integration to CI. ([\#250](https://github.com/posit-dev/great-tables/issues/250))
- Updated supported Python versions list to match those tested. ([\#269](https://github.com/posit-dev/great-tables/issues/269))

## v0.4.0

*2024-03-15* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.4.0)

This release introduces nanoplots (small inline plots embedded directly in table cells) and adds Polars selector support to all `fmt_*()` methods.

#### New Features

- **Nanoplots** -- Embed small inline plots (sparklines, bar charts, etc.) directly within table cells for at-a-glance data visualization. ([\#219](https://github.com/posit-dev/great-tables/issues/219))
- **Polars selectors in `fmt_*()` methods** -- Use Polars selectors like `cs.starts_with()` to target columns in any formatting method. ([\#217](https://github.com/posit-dev/great-tables/issues/217))

#### Bug Fixes

- Improved HTML representation of tables for better rendering. ([\#233](https://github.com/posit-dev/great-tables/issues/233))
- Header component HTML tags now pass HTML validation. ([\#235](https://github.com/posit-dev/great-tables/issues/235))
- The `'transparent'` color (and other named colors) now works in `tab_options(table_background_color=)`. ([\#242](https://github.com/posit-dev/great-tables/issues/242))
- Fixed a render reorder issue that caused incorrect row groupings. ([\#218](https://github.com/posit-dev/great-tables/issues/218))

#### Documentation

- Fixed the `opt_horizontal_padding()` example. ([\#215](https://github.com/posit-dev/great-tables/issues/215))

## v0.3.1

*2024-02-27* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.3.1)

This release adds table export capabilities with `.save()` and `.as_raw_html()`, plus two new styling convenience methods. Several `data_color()` edge cases are now handled correctly.

#### New Features

- **`.save()` and `.as_raw_html()` methods** -- Export tables to HTML files or retrieve raw HTML strings for embedding. ([\#208](https://github.com/posit-dev/great-tables/issues/208))
- **`opt_stylize()` method** -- Apply one of several pre-built table themes with a single method call. ([\#198](https://github.com/posit-dev/great-tables/issues/198))
- **`opt_table_outline()` method** -- Add or customize the table's outer border. ([\#209](https://github.com/posit-dev/great-tables/issues/209))

#### Bug Fixes

- Fixed row rendering order to iterate over sorted rows. ([\#202](https://github.com/posit-dev/great-tables/issues/202))
- `np.nan` values are now correctly replaced with the `na_color=` value in `data_color()`. ([\#205](https://github.com/posit-dev/great-tables/issues/205))
- `data_color()` now handles edge cases with single-value columns and all-missing columns. ([\#213](https://github.com/posit-dev/great-tables/issues/213))

#### Documentation

- Added the `v0.3.0` release blog post. ([\#200](https://github.com/posit-dev/great-tables/issues/200))
- Added documentation on table themes. ([\#197](https://github.com/posit-dev/great-tables/issues/197))
- Added docs for the `fmt_image()` method. ([\#216](https://github.com/posit-dev/great-tables/issues/216))

#### Internal

- Removed type annotations from docstrings. ([\#207](https://github.com/posit-dev/great-tables/issues/207))

## v0.3.0

*2024-02-16* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.3.0)

This release brings extensive table customization with `tab_options()` for global styling, `cols_width()` for column sizing, `fmt_image()` for embedding images, and several convenience methods for common styling patterns. ColorBrewer palettes are now available in `data_color()`.

#### New Features

- **`tab_options()` method** -- Configure global table styling options including fonts, colors, padding, and borders. ([\#146](https://github.com/posit-dev/great-tables/issues/146))
- **`cols_width()` method** -- Set explicit column widths using absolute or relative values. ([\#143](https://github.com/posit-dev/great-tables/issues/143))
- **`fmt_image()` method** -- Embed images directly in table cells from file paths or URLs. ([\#163](https://github.com/posit-dev/great-tables/issues/163))
- **`opt_align_table_header()` method** -- Quickly align the table header to the left, center, or right. ([\#147](https://github.com/posit-dev/great-tables/issues/147))
- **`opt_all_caps()` method** -- Apply all-caps styling to column labels, spanner labels, or stub text. ([\#150](https://github.com/posit-dev/great-tables/issues/150))
- **Vertical and horizontal padding options** -- New `opt_*` methods for adjusting cell padding. ([\#154](https://github.com/posit-dev/great-tables/issues/154))
- **`system_fonts()` helper** -- Access curated system font stacks for use in table options. ([\#158](https://github.com/posit-dev/great-tables/issues/158))
- **ColorBrewer palettes in `data_color()`** -- Use any ColorBrewer palette for data-driven coloring. ([\#186](https://github.com/posit-dev/great-tables/issues/186))

#### Bug Fixes

- Replaced deprecated `with_row_count` with `with_row_index` for Polars compatibility. ([\#189](https://github.com/posit-dev/great-tables/issues/189), [@jrycw](https://github.com/jrycw))
- Table font names in `tab_options()` now accept both a string and a list. ([\#155](https://github.com/posit-dev/great-tables/issues/155))
- Fixed `FutureWarning` for `DataFrameGroupBy.grouper`. ([\#193](https://github.com/posit-dev/great-tables/issues/193), [@jrycw](https://github.com/jrycw))

#### Enhancements

- Added `py.typed` marker to support PEP 561 type-checking. ([\#139](https://github.com/posit-dev/great-tables/issues/139), [@sugatoray](https://github.com/sugatoray))

#### Documentation

- Added example using `sza` dataset with `data_color()`. ([\#136](https://github.com/posit-dev/great-tables/issues/136))
- Published a Super Bowl blog post. ([\#184](https://github.com/posit-dev/great-tables/issues/184), [\#185](https://github.com/posit-dev/great-tables/issues/185))
- Added sports examples to the docs. ([\#195](https://github.com/posit-dev/great-tables/issues/195))
- Cleaned up examples in the API docs. ([\#191](https://github.com/posit-dev/great-tables/issues/191))
- Fixed a column name in the *Column Labels* documentation. ([\#187](https://github.com/posit-dev/great-tables/issues/187), [@jrycw](https://github.com/jrycw))

#### New Contributors

- [@sugatoray](https://github.com/sugatoray) made their first contribution in https://github.com/posit-dev/great-tables/pull/139
- [@jrycw](https://github.com/jrycw) made their first contribution in https://github.com/posit-dev/great-tables/pull/189

## v0.2.0

*2024-01-24* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.2.0)

This release introduces the `data_color()` method for applying color scales to table data, along with several bug fixes for frame validation and spanner columns.

#### New Features

- **`data_color()` method** -- Apply color scales to columns based on their underlying data values, with support for custom palettes and domains. ([\#109](https://github.com/posit-dev/great-tables/issues/109))

#### Bug Fixes

- Fixed tab spanner column name resolution. ([\#111](https://github.com/posit-dev/great-tables/issues/111), [@atseewal](https://github.com/atseewal))
- Fixed frame validation to handle edge cases. ([\#118](https://github.com/posit-dev/great-tables/issues/118))
- Frame validation now coerces non-string column names. ([\#127](https://github.com/posit-dev/great-tables/issues/127))

#### Enhancements

- Internal use of `to_list()` as a cross-DataFrame solution for better Pandas/Polars compatibility. ([\#128](https://github.com/posit-dev/great-tables/issues/128))

#### Documentation

- Added a guide for `data_color()` and an introductory blog post for the new version. ([\#131](https://github.com/posit-dev/great-tables/issues/131))
- Published a blog post on Polars styling. ([\#113](https://github.com/posit-dev/great-tables/issues/113))

#### New Contributors

- [@atseewal](https://github.com/atseewal) made their first contribution in https://github.com/posit-dev/great-tables/pull/111

## v0.1.5

*2024-01-05* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.5)

This release adds `fmt_datetime()` for date-time formatting and generalizes row selection across all methods that accept a `rows=` argument.

#### New Features

- **`fmt_datetime()` method** -- Format datetime values in the table body with flexible date-time patterns. ([\#101](https://github.com/posit-dev/great-tables/issues/101))
- **Generalized row selectors** -- All `rows=` arguments now accept a function that operates on a DataFrame, making row selection in Pandas much easier. ([\#107](https://github.com/posit-dev/great-tables/issues/107))

#### Documentation

- Published an introductory blog post for Great Tables. ([\#105](https://github.com/posit-dev/great-tables/issues/105))

## v0.1.4

*2023-12-19* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.4)

This release adds data-driven styling via `style.from_column()`, fixes column hiding and style application, and improves the documentation site.

#### New Features

- **`style.from_column()`** -- Apply styles dynamically based on column values, implemented for `loc.body()`. ([\#83](https://github.com/posit-dev/great-tables/issues/83))

#### Enhancements

- `tab_style()` now accepts lists of styles and lists of locations. ([\#87](https://github.com/posit-dev/great-tables/issues/87))
- The compiled CSS ID value is now correctly applied to all rules. ([\#92](https://github.com/posit-dev/great-tables/issues/92))

#### Bug Fixes

- Fixed `cols_hide()` not working correctly. ([\#86](https://github.com/posit-dev/great-tables/issues/86))

#### Documentation

- Examples now display in a single column on narrow screens. ([\#81](https://github.com/posit-dev/great-tables/issues/81))
- Added a *Get Started* page on styling. ([\#88](https://github.com/posit-dev/great-tables/issues/88))
- Added interlinks throughout the documentation site. ([\#97](https://github.com/posit-dev/great-tables/issues/97))

## v0.1.3

*2023-12-12* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.3)

This release introduces the `tab_style()` method for targeted cell styling and includes several fixes to table rendering and source notes.

#### New Features

- **`tab_style()` method** -- Apply custom styles to specific cells, columns, or rows using location selectors. ([\#68](https://github.com/posit-dev/great-tables/issues/68))

#### Enhancements

- `loc.body()` now defaults to all columns and rows when called without arguments. ([\#79](https://github.com/posit-dev/great-tables/issues/79))
- `tab_source_note()` now works correctly with `md()` and `html()` helpers. ([\#77](https://github.com/posit-dev/great-tables/issues/77))

#### Bug Fixes

- Fixed handling of addition operations in the SCSS template. ([\#72](https://github.com/posit-dev/great-tables/issues/72))

#### Documentation

- Added hyperlinks in a table example. ([\#70](https://github.com/posit-dev/great-tables/issues/70), [@kmasiello](https://github.com/kmasiello))

#### Internal

- Added pre-commit checks to CI. ([\#78](https://github.com/posit-dev/great-tables/issues/78))

### New Contributors

- [@kmasiello](https://github.com/kmasiello) made their first contribution in https://github.com/posit-dev/great-tables/pull/70

## v0.1.2

*2023-12-07* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.2)

This release adds Shiny integration for Great Tables, enabling interactive table rendering in Shiny for Python applications (including support for Shinylive).

#### New Features

- **Shiny support** -- A new `great_tables.shiny` module provides `output_gt()` and `render_gt()` for rendering GT tables in Shiny for Python apps. ([\#59](https://github.com/posit-dev/great-tables/issues/59))

#### Enhancements

- Replaced the `libsass` dependency with `webcolors`, enabling Great Tables to run in Shinylive. ([\#61](https://github.com/posit-dev/great-tables/issues/61))

#### Documentation

- Fixed code example in README.md. ([\#62](https://github.com/posit-dev/great-tables/issues/62))

## v0.1.1

*2023-12-06* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.1)

Great Tables v0.1.1 is a maintenance release with bug fixes, improved test coverage, and a reorganization of built-in datasets.

#### Enhancements

- Datasets (except `exibble`) are no longer exported from the top-level module; a `data` submodule is now the access point for all built-in datasets. ([\#57](https://github.com/posit-dev/great-tables/issues/57))

#### Bug Fixes

- Column selections now correctly exclude columns that are in the stub. ([\#49](https://github.com/posit-dev/great-tables/issues/49))
- Several rendering issues were fixed. ([\#58](https://github.com/posit-dev/great-tables/issues/58))

#### Internal

- Dataclasses are now frozen for improved immutability. ([\#50](https://github.com/posit-dev/great-tables/issues/50))
- Added several tests and incorporated `pytest-cov` for coverage reporting. ([\#53](https://github.com/posit-dev/great-tables/issues/53), [\#54](https://github.com/posit-dev/great-tables/issues/54), [\#55](https://github.com/posit-dev/great-tables/issues/55))

## v0.1.0

*2023-12-04* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.0)

This release rounds out the initial API, delivering full table structuring with spanners, row groups, and stub labels. Formatting methods are now complete with locale support, Polars DataFrames and selectors are fully supported, and the new `vals` submodule enables value formatting outside of a table context.

#### New Features

- **Spanners, row groups, and stub labels** -- Tables can now be structured with column spanners, row groups, and stub labels for richer hierarchical layouts.
- **Polars support** -- Polars DataFrames are accepted as input data, and Polars selectors (e.g., `cs.starts_with`) can be used for column targeting.
- **`vals` submodule** -- Format values outside of a table context using the same formatting engine available in `fmt_*()` methods.

#### Enhancements

- Formatting methods are now fully fleshed out with comprehensive locale support for number, currency, and date/time formatting.

#### Documentation

- Added a *Get Started* guide to the documentation site.
- Added many examples throughout the API reference.

## v0.0.2

*2023-11-10* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.0.2)

This release introduces the foundational `GT` object with core table-building capabilities, including value formatting, header content, and annotation methods.

#### New Features

- **`GT` class** -- A top-level table object providing the primary interface for building and customizing tables.
- **`fmt_*()` methods** -- A comprehensive set of formatting methods for transforming cell values in the table body.
- **Title and note methods** -- Methods for adding titles, subtitles, and table notes to provide context and annotations.

#### Internal

- Groundwork for spanners, row columns, and group columns (to be exposed in a future release).

# Changelog

This changelog is generated automatically from [GitHub Releases](https://github.com/posit-dev/great-tables/releases).


# v0.21.0

*2026-03-03* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.21.0)

This release adds [cols_merge()](reference/GT.cols_merge.html#great_tables.GT.cols_merge) for combining cell contents across columns, [cols_label_with()](reference/GT.cols_label_with.html#great_tables.GT.cols_label_with) for function-based relabeling, [fmt_engineering()](reference/GT.fmt_engineering.html#great_tables.GT.fmt_engineering) for engineering notation, and [opt_css()](reference/GT.opt_css.html#great_tables.GT.opt_css) for injecting custom CSS rules.


### Deprecations

- [opt_all_caps()](reference/GT.opt_all_caps.html#great_tables.GT.opt_all_caps) now uses [loc.column_labels](reference/loc.column_labels.html#great_tables.loc.column_labels), [loc.stub](reference/loc.stub.html#great_tables.loc.stub), and [loc.row_groups](reference/loc.row_groups.html#great_tables.loc.row_groups) for the `locations=` argument. String-based locations still work but trigger a deprecation warning. ([\#436](https://github.com/posit-dev/great-tables/issues/436), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


### New Features

- **[cols_merge()](reference/GT.cols_merge.html#great_tables.GT.cols_merge) method** -- Combine cell contents across two or more columns using format patterns. ([\#780](https://github.com/posit-dev/great-tables/issues/780))
- **[cols_label_with()](reference/GT.cols_label_with.html#great_tables.GT.cols_label_with) method** -- Relabel columns using a function (e.g., `str.upper`, `str.replace`). ([\#816](https://github.com/posit-dev/great-tables/issues/816))
- **[fmt_engineering()](reference/GT.fmt_engineering.html#great_tables.GT.fmt_engineering) method** -- Format values in engineering notation (exponents that are multiples of 3). ([\#786](https://github.com/posit-dev/great-tables/issues/786))
- **[opt_css()](reference/GT.opt_css.html#great_tables.GT.opt_css) method** -- Define arbitrary CSS rules for an HTML table. ([\#775](https://github.com/posit-dev/great-tables/issues/775))
- **Container padding in [tab_options()](reference/GT.tab_options.html#great_tables.GT.tab_options)** -- Set padding around the table container element. ([\#802](https://github.com/posit-dev/great-tables/issues/802), [<span class="citation" cites="thriller08">@thriller08</span>](https://github.com/thriller08))


### Bug Fixes

- Refactored internal auto-align code for Pandas 3.0.0 compatibility. ([\#810](https://github.com/posit-dev/great-tables/issues/810))
- Added `int` to the `RowSelectExpr` type definition. ([\#800](https://github.com/posit-dev/great-tables/issues/800), [<span class="citation" cites="tylerriccio33">@tylerriccio33</span>](https://github.com/tylerriccio33))
- Updated the Polars selector type annotation to use `Selector`. ([\#770](https://github.com/posit-dev/great-tables/issues/770), [<span class="citation" cites="schmidma">@schmidma</span>](https://github.com/schmidma))
- Annotated the [pipe()](reference/GT.pipe.html#great_tables.GT.pipe) method's first argument type as [GT](reference/GT.html#great_tables.GT). ([\#757](https://github.com/posit-dev/great-tables/issues/757), [<span class="citation" cites="FBruzzesi">@FBruzzesi</span>](https://github.com/FBruzzesi))
- `interactive_data_values=` is now handled correctly in nanoplots. ([\#792](https://github.com/posit-dev/great-tables/issues/792), [<span class="citation" cites="lorenzo-w">@lorenzo-w</span>](https://github.com/lorenzo-w))
- Group labels are now properly modified when `render_formats()` is called. ([\#769](https://github.com/posit-dev/great-tables/issues/769), [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23))


### Documentation

- Added docs for [val_fmt_engineering()](reference/vals.fmt_engineering.html#great_tables.vals.fmt_engineering). ([\#808](https://github.com/posit-dev/great-tables/issues/808), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Corrected the `fns=` parameter docs in [fmt()](reference/GT.fmt.html#great_tables.GT.fmt). ([\#818](https://github.com/posit-dev/great-tables/issues/818))
- Improved docs for the [from_column()](reference/from_column.html#great_tables.from_column) function. ([\#766](https://github.com/posit-dev/great-tables/issues/766), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Added a gt-extras example to the Examples page. ([\#759](https://github.com/posit-dev/great-tables/issues/759), [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23))
- Added an example demonstrating [define_units()](reference/define_units.html#great_tables.define_units). ([\#446](https://github.com/posit-dev/great-tables/issues/446), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


### Internal

- Updated copyright end year to 2026. ([\#804](https://github.com/posit-dev/great-tables/issues/804))
- Fixed several typos. ([\#798](https://github.com/posit-dev/great-tables/issues/798), [<span class="citation" cites="kianmeng">@kianmeng</span>](https://github.com/kianmeng))
- Added Plausible analytics to the project website. ([\#806](https://github.com/posit-dev/great-tables/issues/806))
- Added tests for [opt_all_caps()](reference/GT.opt_all_caps.html#great_tables.GT.opt_all_caps). ([\#812](https://github.com/posit-dev/great-tables/issues/812))
- Fixed the checkout version tag in CI. ([\#768](https://github.com/posit-dev/great-tables/issues/768), [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23))


### New Contributors

- [<span class="citation" cites="kianmeng">@kianmeng</span>](https://github.com/kianmeng) made their first contribution in https://github.com/posit-dev/great-tables/pull/798
- [<span class="citation" cites="thriller08">@thriller08</span>](https://github.com/thriller08) made their first contribution in https://github.com/posit-dev/great-tables/pull/802
- [<span class="citation" cites="schmidma">@schmidma</span>](https://github.com/schmidma) made their first contribution in https://github.com/posit-dev/great-tables/pull/770
- [<span class="citation" cites="lorenzo-w">@lorenzo-w</span>](https://github.com/lorenzo-w) made their first contribution in https://github.com/posit-dev/great-tables/pull/792


# v0.20.0

*2025-10-31* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.20.0)

This release adds the [grand_summary_rows()](reference/GT.grand_summary_rows.html#great_tables.GT.grand_summary_rows) method for table-wide aggregation rows and Polars expression support in `vals` functions.


### New Features

- **[grand_summary_rows()](reference/GT.grand_summary_rows.html#great_tables.GT.grand_summary_rows) method** -- Add summary rows at the bottom of the entire table for grand totals and other aggregate statistics. ([\#765](https://github.com/posit-dev/great-tables/issues/765), [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23))
- **Polars expressions in `vals` functions** -- The `vals` module now accepts Polars expressions for more flexible value formatting. ([\#793](https://github.com/posit-dev/great-tables/issues/793))


# v0.19.0

*2025-10-07* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.19.0)

This release removes NumPy from the dependencies list, fixes `row_group_as_column` to work as intended, and improves color contrast in [data_color()](reference/GT.data_color.html#great_tables.GT.data_color) and row striping.


### Enhancements

- NumPy has been removed as a dependency; all NumPy usage replaced with standard Python. ([\#749](https://github.com/posit-dev/great-tables/issues/749), [<span class="citation" cites="tylerriccio33">@tylerriccio33</span>](https://github.com/tylerriccio33))
- `row_group_as_column=True` now correctly structures row groups as a column in the stub (previously a no-op). ([\#754](https://github.com/posit-dev/great-tables/issues/754), [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23))
- PyArrow `float64` columns are now right-aligned by default, matching Pandas and Polars behavior. ([\#734](https://github.com/posit-dev/great-tables/issues/734), [<span class="citation" cites="FBruzzesi">@FBruzzesi</span>](https://github.com/FBruzzesi))


### Bug Fixes

- Fixed an error when setting `groupname_col=` without `rowname_col=` in the [GT](reference/GT.html#great_tables.GT) constructor. ([\#756](https://github.com/posit-dev/great-tables/issues/756), [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23))
- [data_color()](reference/GT.data_color.html#great_tables.GT.data_color) now accounts for the alpha value of cell background colors when choosing foreground text color. ([\#747](https://github.com/posit-dev/great-tables/issues/747), [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23))
- Row striping now has better color contrast between text and the cell background. ([\#745](https://github.com/posit-dev/great-tables/issues/745), [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23))
- Column names are now accessed consistently via `get_column_names()` instead of `.columns`. ([\#736](https://github.com/posit-dev/great-tables/issues/736), [<span class="citation" cites="FBruzzesi">@FBruzzesi</span>](https://github.com/FBruzzesi))
- Avoided double use of `clear` internally with Polars DataFrames. ([\#729](https://github.com/posit-dev/great-tables/issues/729), [<span class="citation" cites="FBruzzesi">@FBruzzesi</span>](https://github.com/FBruzzesi))


### Documentation

- Corrected various typos. ([\#730](https://github.com/posit-dev/great-tables/issues/730), [<span class="citation" cites="FBruzzesi">@FBruzzesi</span>](https://github.com/FBruzzesi))
- Added a Posit badge to the project website header. ([\#777](https://github.com/posit-dev/great-tables/issues/777))


### Internal

- Refactored code for better adherence to best practices and improved performance. ([\#731](https://github.com/posit-dev/great-tables/issues/731), [<span class="citation" cites="FBruzzesi">@FBruzzesi</span>](https://github.com/FBruzzesi))


### New Contributors

- [<span class="citation" cites="FBruzzesi">@FBruzzesi</span>](https://github.com/FBruzzesi) made their first contribution in https://github.com/posit-dev/great-tables/pull/731


# v0.18.0

*2025-07-10* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.18.0)

This release introduces [tab_spanner_delim()](reference/GT.tab_spanner_delim.html#great_tables.GT.tab_spanner_delim) for automatic spanner creation from delimited column names, rotatable column labels, boolean formatting with [fmt_tf()](reference/GT.fmt_tf.html#great_tables.GT.fmt_tf), and custom datetime format strings. Tables can now be pickled for serialization.


### New Features

- **[tab_spanner_delim()](reference/GT.tab_spanner_delim.html#great_tables.GT.tab_spanner_delim) method** -- Automatically create column spanners by splitting column names on a delimiter. ([\#647](https://github.com/posit-dev/great-tables/issues/647))
- **[cols_label_rotate()](reference/GT.cols_label_rotate.html#great_tables.GT.cols_label_rotate) method** -- Rotate column label text 90 degrees for compact headers. ([\#696](https://github.com/posit-dev/great-tables/issues/696), [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23))
- **[fmt_tf()](reference/GT.fmt_tf.html#great_tables.GT.fmt_tf) method** -- Format boolean values with customizable true/false representations. ([\#665](https://github.com/posit-dev/great-tables/issues/665), [\#704](https://github.com/posit-dev/great-tables/issues/704))
- **Custom datetime format strings** -- [fmt_datetime()](reference/GT.fmt_datetime.html#great_tables.GT.fmt_datetime) now accepts a `format_str=` parameter for arbitrary datetime formatting. ([\#645](https://github.com/posit-dev/great-tables/issues/645))
- **Pickle support** -- GT tables can now be serialized with `pickle`. ([\#641](https://github.com/posit-dev/great-tables/issues/641), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- **Compact currency formatting** -- [fmt_currency()](reference/GT.fmt_currency.html#great_tables.GT.fmt_currency) gained a `compact=` parameter (e.g., `$13.4M`). ([\#664](https://github.com/posit-dev/great-tables/issues/664))
- **`truncate=` option in [data_color()](reference/GT.data_color.html#great_tables.GT.data_color)** -- Truncate values to the domain bounds instead of erroring on out-of-range data. ([\#673](https://github.com/posit-dev/great-tables/issues/673), [<span class="citation" cites="mahdibaghbanzadeh">@mahdibaghbanzadeh</span>](https://github.com/mahdibaghbanzadeh))


### Enhancements

- Removed the Pandas dependency from [vals.fmt_integer()](reference/vals.fmt_integer.html#great_tables.vals.fmt_integer). ([\#719](https://github.com/posit-dev/great-tables/issues/719))


### Bug Fixes

- Fixed an off-by-one bug in `rescale_factor()` that affected [data_color()](reference/GT.data_color.html#great_tables.GT.data_color) output. ([\#718](https://github.com/posit-dev/great-tables/issues/718), [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23))
- Google Fonts import statements are no longer duplicated in HTML output. ([\#708](https://github.com/posit-dev/great-tables/issues/708))
- Fixed row striping applying to incorrect rows due to an indexing issue. ([\#701](https://github.com/posit-dev/great-tables/issues/701), [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23))
- Spanners can now be correctly styled with [tab_style()](reference/GT.tab_style.html#great_tables.GT.tab_style). ([\#695](https://github.com/posit-dev/great-tables/issues/695), [<span class="citation" cites="ChristopherRussell">@ChristopherRussell</span>](https://github.com/ChristopherRussell))
- Removed unused `sep_mark=` parameter from [fmt_scientific()](reference/GT.fmt_scientific.html#great_tables.GT.fmt_scientific). ([\#642](https://github.com/posit-dev/great-tables/issues/642))


### Documentation

- Added note about using `.show("browser")` in VS Code. ([\#643](https://github.com/posit-dev/great-tables/issues/643))
- Suppressed a [cols_width()](reference/GT.cols_width.html#great_tables.GT.cols_width) warning that appeared in the docs. ([\#659](https://github.com/posit-dev/great-tables/issues/659), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Updated docstrings for date/time formatting methods. ([\#658](https://github.com/posit-dev/great-tables/issues/658))
- Improved interlinking with quartodoc. ([\#697](https://github.com/posit-dev/great-tables/issues/697))
- Added underline to active link in top navigation bar. ([\#706](https://github.com/posit-dev/great-tables/issues/706))
- Improved documentation for [as_raw_html()](reference/GT.as_raw_html.html#great_tables.GT.as_raw_html). ([\#707](https://github.com/posit-dev/great-tables/issues/707))
- Better introduction of the [show()](reference/GT.show.html#great_tables.GT.show) method via a callout. ([\#712](https://github.com/posit-dev/great-tables/issues/712))


### Internal

- Added a no-Pandas dependency test for functions in the `vals` module. ([\#689](https://github.com/posit-dev/great-tables/issues/689))


### New Contributors

- [<span class="citation" cites="dpprdan">@dpprdan</span>](https://github.com/dpprdan) made their first contribution in https://github.com/posit-dev/great-tables/pull/670
- [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23) made their first contribution in https://github.com/posit-dev/great-tables/pull/696
- [<span class="citation" cites="ChristopherRussell">@ChristopherRussell</span>](https://github.com/ChristopherRussell) made their first contribution in https://github.com/posit-dev/great-tables/pull/695
- [<span class="citation" cites="mahdibaghbanzadeh">@mahdibaghbanzadeh</span>](https://github.com/mahdibaghbanzadeh) made their first contribution in https://github.com/posit-dev/great-tables/pull/673


# v0.17.0

*2025-03-11* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.17.0)

This release adds Quarto integration with a table-processing disable option, a new [cols_unhide()](reference/GT.cols_unhide.html#great_tables.GT.cols_unhide) method, and ensures unique HTML ID attributes for tables. The `css-inline` package is now an optional extra.


### Breaking Changes

- HTML ID attributes are now unique per table, which may affect code that relied on the previous static ID. ([\#607](https://github.com/posit-dev/great-tables/issues/607), [<span class="citation" cites="BenGale93">@BenGale93</span>](https://github.com/BenGale93))
- The `css-inline` package has been moved to an extras group (`pip install great_tables[extra]`). ([\#634](https://github.com/posit-dev/great-tables/issues/634))


### New Features

- **Quarto table-processing option** -- Disable Quarto's default table processing and receive a warning on render when needed. ([\#611](https://github.com/posit-dev/great-tables/issues/611))
- **[cols_unhide()](reference/GT.cols_unhide.html#great_tables.GT.cols_unhide) method** -- Reveal previously hidden columns. ([\#629](https://github.com/posit-dev/great-tables/issues/629), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- **`inline_css=` argument** -- Inline CSS directly on table elements for constrained output contexts. ([\#633](https://github.com/posit-dev/great-tables/issues/633), [<span class="citation" cites="tylerriccio33">@tylerriccio33</span>](https://github.com/tylerriccio33))


### Bug Fixes

- Screenshots are no longer always saved as PNG regardless of the specified format. ([\#599](https://github.com/posit-dev/great-tables/issues/599))
- Resolved an encoding issue in `GT.save()`. ([\#609](https://github.com/posit-dev/great-tables/issues/609), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Non-integer values are now correctly passed to nanoplot options. ([\#608](https://github.com/posit-dev/great-tables/issues/608), [<span class="citation" cites="tylerriccio33">@tylerriccio33</span>](https://github.com/tylerriccio33))
- Fixed scientific notation zero padding when `exp_style=` is used (e.g., `"2.3E-03"` was incorrectly displayed as `"2.3E−30"`). ([\#622](https://github.com/posit-dev/great-tables/issues/622))
- Fixed nanoplot code to guard against string values (single string or list containing strings). ([\#623](https://github.com/posit-dev/great-tables/issues/623))


### Documentation

- Updated docs for the `mask=` parameter in [loc.body()](reference/loc.body.html#great_tables.loc.body). ([\#589](https://github.com/posit-dev/great-tables/issues/589), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Updated the preview of the `year` column in the [gtcars](reference/data.gtcars.html#great_tables.data.gtcars) dataset. ([\#587](https://github.com/posit-dev/great-tables/issues/587), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Added examples to the documentation. ([\#618](https://github.com/posit-dev/great-tables/issues/618), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Added [style.css](reference/style.css.html#great_tables.style.css) entry to the API reference. ([\#624](https://github.com/posit-dev/great-tables/issues/624))
- Aligned the *Getting Started* guide with the README. ([\#627](https://github.com/posit-dev/great-tables/issues/627), [<span class="citation" cites="zachvalenta">@zachvalenta</span>](https://github.com/zachvalenta))


### Internal

- Added a `deploy-pypi` environment with deployment protection rules for release workflow review. ([\#590](https://github.com/posit-dev/great-tables/issues/590))


### New Contributors

- [<span class="citation" cites="tylerriccio33">@tylerriccio33</span>](https://github.com/tylerriccio33) made their first contribution in https://github.com/posit-dev/great-tables/pull/608
- [<span class="citation" cites="BenGale93">@BenGale93</span>](https://github.com/BenGale93) made their first contribution in https://github.com/posit-dev/great-tables/pull/607
- [<span class="citation" cites="zachvalenta">@zachvalenta</span>](https://github.com/zachvalenta) made their first contribution in https://github.com/posit-dev/great-tables/pull/627


# v0.16.1

*2025-01-24* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.16.1)

Great Tables `v0.16.1` is a patch release with a single data fix.


### Bug Fixes

- Updated the `year` column dtype in the [gtcars](reference/data.gtcars.html#great_tables.data.gtcars) dataset. ([\#586](https://github.com/posit-dev/great-tables/issues/586))


# v0.16.0

*2025-01-24* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.16.0)

This release introduces the `mask=` argument for enhanced body cell targeting and a [write_raw_html()](reference/GT.write_raw_html.html#great_tables.GT.write_raw_html) helper for convenient HTML file output.


### New Features

- **`mask=` argument in [loc.body()](reference/loc.body.html#great_tables.loc.body)** -- Target specific body cells using a boolean mask for more flexible styling and formatting. ([\#566](https://github.com/posit-dev/great-tables/issues/566), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- **[write_raw_html()](reference/GT.write_raw_html.html#great_tables.GT.write_raw_html) helper** -- Write table HTML output directly to a file without manual string handling. ([\#485](https://github.com/posit-dev/great-tables/issues/485), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


### Bug Fixes

- Fixed a deprecation warning in [as_raw_html()](reference/GT.as_raw_html.html#great_tables.GT.as_raw_html) for Python 3.13. ([\#563](https://github.com/posit-dev/great-tables/issues/563), [<span class="citation" cites="stinodego">@stinodego</span>](https://github.com/stinodego))
- Nanoplots now support the `pl.UInt` type. ([\#577](https://github.com/posit-dev/great-tables/issues/577), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


### Documentation

- Added pyOpenSci and DOI badges to the README to acknowledge successful peer review. ([\#576](https://github.com/posit-dev/great-tables/issues/576))
- Updated images and text for included datasets. ([\#562](https://github.com/posit-dev/great-tables/issues/562))
- Replaced JSON dataset with `.ndjson` file in coffee sales examples to fix a serialization error. ([\#580](https://github.com/posit-dev/great-tables/issues/580))


### New Contributors

- [<span class="citation" cites="stinodego">@stinodego</span>](https://github.com/stinodego) made their first contribution in https://github.com/posit-dev/great-tables/pull/563


# v0.15.0

*2024-12-14* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.15.0)

This release brings several new formatting methods ([fmt_flag()](reference/GT.fmt_flag.html#great_tables.GT.fmt_flag) for country flags, [fmt_icon()](reference/GT.fmt_icon.html#great_tables.GT.fmt_icon) for FontAwesome icons), and accounting notation in numeric formatters. PyArrow tables are now experimentally supported as input, [as_raw_html()](reference/GT.as_raw_html.html#great_tables.GT.as_raw_html) can inline CSS, and the new [pipe()](reference/GT.pipe.html#great_tables.GT.pipe) method enables functional composition in table-building pipelines.


### New Features

- **[fmt_flag()](reference/GT.fmt_flag.html#great_tables.GT.fmt_flag) method** -- Display country flag icons in table cells based on country codes. ([\#523](https://github.com/posit-dev/great-tables/issues/523))
- **[fmt_icon()](reference/GT.fmt_icon.html#great_tables.GT.fmt_icon) method** -- Render FontAwesome icons within table cells. ([\#515](https://github.com/posit-dev/great-tables/issues/515))
- **Accounting notation** -- [fmt_number()](reference/GT.fmt_number.html#great_tables.GT.fmt_number), [fmt_percent()](reference/GT.fmt_percent.html#great_tables.GT.fmt_percent), [fmt_integer()](reference/GT.fmt_integer.html#great_tables.GT.fmt_integer), and [fmt_currency()](reference/GT.fmt_currency.html#great_tables.GT.fmt_currency) now support accounting notation for negative values. ([\#513](https://github.com/posit-dev/great-tables/issues/513))
- **PyArrow table support (experimental)** -- Use a `pyarrow.Table` as input data. ([\#487](https://github.com/posit-dev/great-tables/issues/487), [<span class="citation" cites="amol">@amol</span>](https://github.com/amol)-)
- **Inline CSS in [as_raw_html()](reference/GT.as_raw_html.html#great_tables.GT.as_raw_html)** -- New `inline_css=` argument writes CSS-inlined HTML strings for email and other constrained environments. ([\#557](https://github.com/posit-dev/great-tables/issues/557))
- **[pipe()](reference/GT.pipe.html#great_tables.GT.pipe) method** -- Chain custom functions in a table pipeline, similar to the Pandas and Polars [pipe()](reference/GT.pipe.html#great_tables.GT.pipe) APIs. ([\#363](https://github.com/posit-dev/great-tables/issues/363), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- **Enhanced `save()` method** -- Now supports intermediate saves by returning `self`, enabling chained workflows. ([\#499](https://github.com/posit-dev/great-tables/issues/499), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- **HTTP/HTTPS support in [fmt_image()](reference/GT.fmt_image.html#great_tables.GT.fmt_image)** -- The `columns=` parameter now supports URLs with `http`/`https` schemes. ([\#520](https://github.com/posit-dev/great-tables/issues/520), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


### Bug Fixes

- Hidden columns with column width definitions no longer mangle HTML table output. ([\#509](https://github.com/posit-dev/great-tables/issues/509))
- Improved detection of Polars installation. ([\#505](https://github.com/posit-dev/great-tables/issues/505), [<span class="citation" cites="lukemanley">@lukemanley</span>](https://github.com/lukemanley))
- Fixed missing exception raise in `_val_is_numeric()` and `_val_is_str()`. ([\#510](https://github.com/posit-dev/great-tables/issues/510), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


### Documentation

- Added `CITATION.cff` and citation information to the README. ([\#551](https://github.com/posit-dev/great-tables/issues/551))
- Updated README with conda install instructions and usage environment details. ([\#552](https://github.com/posit-dev/great-tables/issues/552))
- Improved presentation of Contributing Guidelines. ([\#550](https://github.com/posit-dev/great-tables/issues/550))
- Added information about Pandas requirement when using internal datasets. ([\#549](https://github.com/posit-dev/great-tables/issues/549), [\#559](https://github.com/posit-dev/great-tables/issues/559))
- Included [vals.fmt_image()](reference/vals.fmt_image.html#great_tables.vals.fmt_image) in the API reference. ([\#486](https://github.com/posit-dev/great-tables/issues/486), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Fixed spelling in the contributing guide. ([\#516](https://github.com/posit-dev/great-tables/issues/516), [<span class="citation" cites="glemaitre">@glemaitre</span>](https://github.com/glemaitre))


### Internal

- Switched to ruff for linting and formatting, and fixed `mypy` errors. ([\#511](https://github.com/posit-dev/great-tables/issues/511), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Standardized imports by converting to relative imports. ([\#521](https://github.com/posit-dev/great-tables/issues/521), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Added CI build for Python 3.13. ([\#514](https://github.com/posit-dev/great-tables/issues/514), [<span class="citation" cites="glemaitre">@glemaitre</span>](https://github.com/glemaitre))
- Fixed CI README badge to report build status correctly. ([\#553](https://github.com/posit-dev/great-tables/issues/553))
- Excluded `if TYPE_CHECKING:` lines from coverage reports. ([\#556](https://github.com/posit-dev/great-tables/issues/556))


### New Contributors

- [<span class="citation" cites="lukemanley">@lukemanley</span>](https://github.com/lukemanley) made their first contribution in https://github.com/posit-dev/great-tables/pull/505
- [<span class="citation" cites="glemaitre">@glemaitre</span>](https://github.com/glemaitre) made their first contribution in https://github.com/posit-dev/great-tables/pull/514
- [<span class="citation" cites="amol">@amol</span>](https://github.com/amol)- made their first contribution in https://github.com/posit-dev/great-tables/pull/487


# v0.14.0

*2024-11-11* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.14.0)

This release adds experimental LaTeX output support, enabling tables to be rendered as LaTeX code for use in scientific documents and publications.


### New Features

- **`.as_latex()` method (experimental)** -- Render tables as LaTeX code for inclusion in LaTeX documents and PDF pipelines. See the [API reference](https://posit-dev.github.io/great-tables/reference/GT.as_latex.html) for current limitations. ([\#481](https://github.com/posit-dev/great-tables/issues/481))


### Documentation

- Improved API reference layout on lower-width devices. ([\#427](https://github.com/posit-dev/great-tables/issues/427), [\#492](https://github.com/posit-dev/great-tables/issues/492))
- Added preview sections for built-in datasets. ([\#453](https://github.com/posit-dev/great-tables/issues/453), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


# v0.13.0

*2024-10-04* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.13.0)

This release adds granular section restyling via convenience methods, image rendering in non-body components through [val_fmt_image()](reference/vals.fmt_image.html#great_tables.vals.fmt_image), and the ability to pass a webdriver instance directly to `.save()`.


### New Features

- **Granular section restyling** -- Convenience API for restyling individual table sections (header, body, footer, etc.) without touching global options. ([\#341](https://github.com/posit-dev/great-tables/issues/341), [<span class="citation" cites="timkpaine">@timkpaine</span>](https://github.com/timkpaine))
- **[val_fmt_image()](reference/vals.fmt_image.html#great_tables.vals.fmt_image)** -- Render images in table components beyond the body (e.g., column labels, spanners). ([\#451](https://github.com/posit-dev/great-tables/issues/451), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- **Webdriver passthrough in `.save()`** -- Pass an existing webdriver instance to `.save()` for reuse across multiple exports. ([\#478](https://github.com/posit-dev/great-tables/issues/478))


### Bug Fixes

- Global `locale` is now respected in all `fmt_*()` methods. ([\#473](https://github.com/posit-dev/great-tables/issues/473), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Fixed headers causing their CSS classes to be printed in the output. ([\#477](https://github.com/posit-dev/great-tables/issues/477))


### Documentation

- Added [google_font()](reference/google_font.html#great_tables.google_font) helper to the API reference. ([\#464](https://github.com/posit-dev/great-tables/issues/464), [\#471](https://github.com/posit-dev/great-tables/issues/471), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Updated docs and code to support `GoogleFont` in [opt_table_font()](reference/GT.opt_table_font.html#great_tables.GT.opt_table_font). ([\#470](https://github.com/posit-dev/great-tables/issues/470), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Added docstrings for new location methods. ([\#474](https://github.com/posit-dev/great-tables/issues/474), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Fixed deprecated warning for `pl.DataFrame.pivot()`. ([\#472](https://github.com/posit-dev/great-tables/issues/472))
- GT members are no longer documented inline on the reference page. ([\#475](https://github.com/posit-dev/great-tables/issues/475))


# v0.12.0

*2024-09-27* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.12.0)

This release adds Google Fonts integration and row striping support, with [opt_stylize()](reference/GT.opt_stylize.html#great_tables.GT.opt_stylize) now producing striped tables by default.


### Breaking Changes

- [opt_stylize()](reference/GT.opt_stylize.html#great_tables.GT.opt_stylize) now produces row stripes by default. Set `add_row_striping=False` to remove them. ([\#461](https://github.com/posit-dev/great-tables/issues/461))
- [opt_stylize()](reference/GT.opt_stylize.html#great_tables.GT.opt_stylize) now adds borders to certain styles, matching the original design intent. ([\#463](https://github.com/posit-dev/great-tables/issues/463))


### New Features

- **[google_font()](reference/google_font.html#great_tables.google_font) helper** -- Easily use Google Fonts in [opt_table_font()](reference/GT.opt_table_font.html#great_tables.GT.opt_table_font) and [style.text()](reference/style.text.html#great_tables.style.text). ([\#423](https://github.com/posit-dev/great-tables/issues/423))
- **Row striping options** -- Configure row striping behavior through [opt_stylize()](reference/GT.opt_stylize.html#great_tables.GT.opt_stylize) and related options. ([\#461](https://github.com/posit-dev/great-tables/issues/461), [\#463](https://github.com/posit-dev/great-tables/issues/463))


### Bug Fixes

- `.show()` now uses a full HTML page for correct UTF-8 display. ([\#458](https://github.com/posit-dev/great-tables/issues/458))


### Documentation

- Updated the Super Bowl example to align with the latest version of Polars. ([\#460](https://github.com/posit-dev/great-tables/issues/460), [\#462](https://github.com/posit-dev/great-tables/issues/462), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


# v0.11.1

*2024-09-20* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.11.1)


## Fixes

- Do not error when URL string supplied to `path=` argument in [fmt_image()](reference/GT.fmt_image.html#great_tables.GT.fmt_image) by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/444
- Include an `encoding=` arg in `GT.save()` (with default `"utf-8"`) for more dependable saving in Windows by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/454
- Unify the method signatures of [cols_label()](reference/GT.cols_label.html#great_tables.GT.cols_label) and [cols_width()](reference/GT.cols_width.html#great_tables.GT.cols_width) by having them both accept `cases=` and `**kwargs` by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/452


## Chores

- Standardize on the `GTSelf` object in method signatures by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/431
- Consistently use `isinstance()` checks throughout the codebase instead of checking with `hasattr()` by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/434
- Improve test coverage for various `opt_*` methods by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/437
- Consolidate ordered list code using the new `_create_ordered_list()` function by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/407
- Internally use `OrderedSet().as_list()` instead of `list(OrderedSet())` for sake of clarity by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/447
- Refactor import statements throughout the `_formats.py` file by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/450


## Docs

- Update import statement in the [GT.data_color()](reference/GT.data_color.html#great_tables.GT.data_color) example by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/432
- Indicate that [tab_spanner()](reference/GT.tab_spanner.html#great_tables.GT.tab_spanner) allows for use of units notation in its `label=` argument by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/426
- Visually document options for theming table with [opt_stylize()](reference/GT.opt_stylize.html#great_tables.GT.opt_stylize) by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/438
- Provide updates to PyCon- and SciPy-related blog posts by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/445

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.11.0…v0.11.1](https://github.com/posit-dev/great-tables/compare/v0.11.0...v0.11.1)


# v0.11.0

*2024-08-30* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.11.0)

This release restructures the HTML output so that `<thead>` properly encloses both the title/subtitle and column labels, and fixes `.save()` compatibility with the latest version of Google Chrome.


### Breaking Changes

- The `<thead>` element now encloses both title/subtitle and column label rows. This improves semantic correctness but may affect custom CSS targeting the old structure. ([\#421](https://github.com/posit-dev/great-tables/issues/421))


### Bug Fixes

- `.save()` now works with the latest version of Google Chrome. ([\#425](https://github.com/posit-dev/great-tables/issues/425))


### Documentation

- Mentioned Polars support in the *Get Started* section. ([\#408](https://github.com/posit-dev/great-tables/issues/408), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Fixed typos and improved a code example in the "Design Philosophy" doc. ([\#401](https://github.com/posit-dev/great-tables/issues/401), [<span class="citation" cites="alfredocarella">@alfredocarella</span>](https://github.com/alfredocarella))
- Fixed a typo in a blog post. ([\#396](https://github.com/posit-dev/great-tables/issues/396))
- Updated documentation for datasets. ([\#397](https://github.com/posit-dev/great-tables/issues/397), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Updated Polars examples for a deprecated argument. ([\#400](https://github.com/posit-dev/great-tables/issues/400), [<span class="citation" cites="atseewal">@atseewal</span>](https://github.com/atseewal))
- Removed mentions of `accounting` in `force_sign=` argument docs. ([\#422](https://github.com/posit-dev/great-tables/issues/422))


### New Contributors

- [<span class="citation" cites="alfredocarella">@alfredocarella</span>](https://github.com/alfredocarella) made their first contribution in https://github.com/posit-dev/great-tables/pull/401


# v0.10.0

*2024-07-08* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.10.0)

This release adds units notation support in column labels and spanners, a new [opt_table_font()](reference/GT.opt_table_font.html#great_tables.GT.opt_table_font) method, the `.show()` method for interactive display, and several new built-in datasets.


### New Features

- **Units notation in [cols_label()](reference/GT.cols_label.html#great_tables.GT.cols_label)** -- Express measurement units directly in column labels using the units notation syntax. ([\#380](https://github.com/posit-dev/great-tables/issues/380))
- **Units notation in [tab_spanner()](reference/GT.tab_spanner.html#great_tables.GT.tab_spanner)** -- Spanner labels can also use units notation for scientific and technical headers. ([\#393](https://github.com/posit-dev/great-tables/issues/393))
- **[opt_table_font()](reference/GT.opt_table_font.html#great_tables.GT.opt_table_font) method** -- Easily set a default font for the entire table. ([\#272](https://github.com/posit-dev/great-tables/issues/272))
- **`.show()` method** -- Display a table interactively in notebooks and other environments. ([\#379](https://github.com/posit-dev/great-tables/issues/379))
- **New datasets** -- Several new built-in datasets added, bringing the total to 16. ([\#382](https://github.com/posit-dev/great-tables/issues/382))


### Bug Fixes

- Fixed [fmt_percent()](reference/GT.fmt_percent.html#great_tables.GT.fmt_percent) issue with Polars `u64-idx` builds. ([\#388](https://github.com/posit-dev/great-tables/issues/388), [<span class="citation" cites="lostmygithubaccount">@lostmygithubaccount</span>](https://github.com/lostmygithubaccount))
- Added render target for HTML pages. ([\#377](https://github.com/posit-dev/great-tables/issues/377), [<span class="citation" cites="isabelizimm">@isabelizimm</span>](https://github.com/isabelizimm))
- `.show()` no longer raises or prints to stderr. ([\#384](https://github.com/posit-dev/great-tables/issues/384))


### Documentation

- Added absolute URLs to README to improve the PyPI project summary. ([\#373](https://github.com/posit-dev/great-tables/issues/373))


### New Contributors

- [<span class="citation" cites="isabelizimm">@isabelizimm</span>](https://github.com/isabelizimm) made their first contribution in https://github.com/posit-dev/great-tables/pull/377
- [<span class="citation" cites="lostmygithubaccount">@lostmygithubaccount</span>](https://github.com/lostmygithubaccount) made their first contribution in https://github.com/posit-dev/great-tables/pull/388


# v0.9.0

*2024-06-06* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.9.0)


## v0.9.0

This release adds row subsetting to [data_color()](reference/GT.data_color.html#great_tables.GT.data_color), allowing color scales to be applied to specific rows.


### New Features

- **Row selection in [data_color()](reference/GT.data_color.html#great_tables.GT.data_color)** -- A `rows=` argument enables applying color scales to a subset of rows rather than the entire column. ([\#364](https://github.com/posit-dev/great-tables/issues/364), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


### Breaking Changes

- The `rows=` parameter is now the third positional argument in [data_color()](reference/GT.data_color.html#great_tables.GT.data_color), which may break code that relied on positional argument order.


# v0.8.0

*2024-06-06* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.8.0)

This release adds method equivalents for several constructor options, allowing them to be set in a chained pipeline rather than only at [GT()](reference/GT.html#great_tables.GT) instantiation.


### New Features

- **[GT.tab_stub()](reference/GT.tab_stub.html#great_tables.GT.tab_stub)** -- Set `rowname_col=` and `groupname_col=` as a method call instead of only in the [GT()](reference/GT.html#great_tables.GT) constructor. ([\#371](https://github.com/posit-dev/great-tables/issues/371))
- **[GT.with_locale()](reference/GT.with_locale.html#great_tables.GT.with_locale)** -- Set the locale after construction. ([\#371](https://github.com/posit-dev/great-tables/issues/371))
- **[GT.with_id()](reference/GT.with_id.html#great_tables.GT.with_id)** -- Set the table ID after construction. ([\#371](https://github.com/posit-dev/great-tables/issues/371))


# v0.7.0

*2024-06-04* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.7.0)

This release adds the [fmt_units()](reference/GT.fmt_units.html#great_tables.GT.fmt_units) method for rendering scientific units and improves Polars selector compatibility.


### New Features

- **[fmt_units()](reference/GT.fmt_units.html#great_tables.GT.fmt_units) method** -- Format measurement units with proper subscripts, superscripts, and symbols for scientific notation. ([\#240](https://github.com/posit-dev/great-tables/issues/240))
- **Non-strict Polars `expand_selector()` support** -- Polars selectors now use non-strict mode, avoiding errors when selectors match no columns. ([\#368](https://github.com/posit-dev/great-tables/issues/368))


### Bug Fixes

- General enhancements and fixes to several `cols_*()` methods. ([\#366](https://github.com/posit-dev/great-tables/issues/366), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Better error message when list data is used incorrectly in [fmt_nanoplot()](reference/GT.fmt_nanoplot.html#great_tables.GT.fmt_nanoplot). ([\#356](https://github.com/posit-dev/great-tables/issues/356), [<span class="citation" cites="marcozzxx810">@marcozzxx810</span>](https://github.com/marcozzxx810))


### Documentation

- Added an RSS feed to the blog. ([\#367](https://github.com/posit-dev/great-tables/issues/367), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


### Internal

- Refactored `seq_groups()` to accept `Iterable`. ([\#365](https://github.com/posit-dev/great-tables/issues/365), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Moved `pairwise()`, `seq_groups()`, and `is_equal()` to `_utils.py`. ([\#369](https://github.com/posit-dev/great-tables/issues/369), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


# v0.6.1

*2024-05-23* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.6.1)

Great Tables `v0.6.1` is a patch release fixing compatibility with Polars `v0.20.28` and screenshot export for non-PNG formats.


### Bug Fixes

- Fixed column selections breaking with Polars v0.20.28. ([\#360](https://github.com/posit-dev/great-tables/issues/360), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Fixed `_save_screenshot()` failing for non-PNG file formats. ([\#352](https://github.com/posit-dev/great-tables/issues/352), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


### Internal

- Enhanced test coverage. ([\#339](https://github.com/posit-dev/great-tables/issues/339), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Removed unneeded files. ([\#351](https://github.com/posit-dev/great-tables/issues/351))


# v0.6.0

*2024-05-16* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.6.0)

This release introduces multi-level spanners, allowing column spanners to be nested hierarchically. Table export via `.save()` is now more robust.


### New Features

- **Multi-level spanners** -- Column spanners can now be nested under other spanners to create hierarchical column groupings. ([\#345](https://github.com/posit-dev/great-tables/issues/345), [<span class="citation" cites="timkpaine">@timkpaine</span>](https://github.com/timkpaine))


### Bug Fixes

- `.save()` now always captures the full table when exporting. ([\#344](https://github.com/posit-dev/great-tables/issues/344))


### Documentation

- Added an example coffee table with nanoplots. ([\#349](https://github.com/posit-dev/great-tables/issues/349))
- Cleaned up minor formatting issues in the docs. ([\#338](https://github.com/posit-dev/great-tables/issues/338), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


### New Contributors

- [<span class="citation" cites="timkpaine">@timkpaine</span>](https://github.com/timkpaine) made their first contribution in https://github.com/posit-dev/great-tables/pull/345


# v0.5.2

*2024-05-13* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/0.5.2)

Great Tables `v0.5.2` is a patch release addressing several bugs in borders, image formatting, and nanoplots.


### Bug Fixes

- [CellStyleBorders](reference/style.borders.html#great_tables.style.borders) is now properly constructed when [sides](reference/style.borders.html#great_tables.style.borders.sides) is set to `"all"`. ([\#326](https://github.com/posit-dev/great-tables/issues/326), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- [fmt_image()](reference/GT.fmt_image.html#great_tables.GT.fmt_image) no longer errors on missing values. ([\#329](https://github.com/posit-dev/great-tables/issues/329))
- Nanoplots now work with list columns, and Polars list columns no longer raise an error. ([\#330](https://github.com/posit-dev/great-tables/issues/330))
- Nanoplots no longer fail for lists of large integers. ([\#335](https://github.com/posit-dev/great-tables/issues/335))
- [fmt_number()](reference/GT.fmt_number.html#great_tables.GT.fmt_number) no longer inserts an improper comma for 3-digit compact, negative numbers. ([\#335](https://github.com/posit-dev/great-tables/issues/335))


### Documentation

- Added examples to API reference pages. ([\#328](https://github.com/posit-dev/great-tables/issues/328), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


### Internal

- Removed unused `webcolors` library as a required dependency. ([\#336](https://github.com/posit-dev/great-tables/issues/336), [<span class="citation" cites="marcozzxx810">@marcozzxx810</span>](https://github.com/marcozzxx810))


### New Contributors

- [<span class="citation" cites="marcozzxx810">@marcozzxx810</span>](https://github.com/marcozzxx810) made their first contribution in https://github.com/posit-dev/great-tables/pull/336


# v0.5.1

*2024-05-03* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.5.1)

Great Tables `v0.5.1` is a maintenance release focused on bug fixes, code quality improvements, and documentation. Special thanks to [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) for an incredible number of contributions.


### Bug Fixes

- `table_font_color=` in [tab_options()](reference/GT.tab_options.html#great_tables.GT.tab_options) now correctly accepts named colors. ([\#285](https://github.com/posit-dev/great-tables/issues/285), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Group label rows now produce valid HTML. ([\#308](https://github.com/posit-dev/great-tables/issues/308))
- Fixed Polars selectors error in [cols_hide()](reference/GT.cols_hide.html#great_tables.GT.cols_hide). ([\#316](https://github.com/posit-dev/great-tables/issues/316), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- [fmt_number()](reference/GT.fmt_number.html#great_tables.GT.fmt_number) now handles missing values correctly. ([\#317](https://github.com/posit-dev/great-tables/issues/317), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Fixed display of integer-like values in nanoplots. ([\#319](https://github.com/posit-dev/great-tables/issues/319), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


### Documentation

- Fixed typos throughout the docs. ([\#286](https://github.com/posit-dev/great-tables/issues/286), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Added a community example from [<span class="citation" cites="chalg">@chalg</span>](https://github.com/chalg). ([\#323](https://github.com/posit-dev/great-tables/issues/323))


### Internal

- Cleaned up implementation of [fmt_nanoplot()](reference/GT.fmt_nanoplot.html#great_tables.GT.fmt_nanoplot) and [data_color()](reference/GT.data_color.html#great_tables.GT.data_color). ([\#294](https://github.com/posit-dev/great-tables/issues/294), [\#295](https://github.com/posit-dev/great-tables/issues/295), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Refactored [fmt_time()](reference/GT.fmt_time.html#great_tables.GT.fmt_time), [fmt_date()](reference/GT.fmt_date.html#great_tables.GT.fmt_date), and [fmt_datetime()](reference/GT.fmt_datetime.html#great_tables.GT.fmt_datetime). ([\#290](https://github.com/posit-dev/great-tables/issues/290), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Refactored `letters` and `Letters` functions in helpers. ([\#289](https://github.com/posit-dev/great-tables/issues/289), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Updated type hints and organized imports. ([\#315](https://github.com/posit-dev/great-tables/issues/315), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Codebase cleanup and minor improvements. ([\#292](https://github.com/posit-dev/great-tables/issues/292), [\#305](https://github.com/posit-dev/great-tables/issues/305), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Improved test coverage. ([\#311](https://github.com/posit-dev/great-tables/issues/311), [\#325](https://github.com/posit-dev/great-tables/issues/325), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Added tests for [cols_align()](reference/GT.cols_align.html#great_tables.GT.cols_align) and extended Polars expression support. ([\#320](https://github.com/posit-dev/great-tables/issues/320), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


# v0.5.0

*2024-04-12* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.5.0)

This release significantly reduces the dependency footprint by removing mizani and pandas as required dependencies, adds substitution methods for missing and zero values, and provides webdriver choice in `.save()`.


### New Features

- **[sub_missing()](reference/GT.sub_missing.html#great_tables.GT.sub_missing) and [sub_zero()](reference/GT.sub_zero.html#great_tables.GT.sub_zero) methods** -- Substitute missing or zero values with custom text or symbols. ([\#244](https://github.com/posit-dev/great-tables/issues/244))
- **Webdriver selection in `.save()`** -- Choose between different webdrivers (e.g., Chrome, Firefox) when saving tables as images. ([\#262](https://github.com/posit-dev/great-tables/issues/262))


### Enhancements

- Removed mizani and pandas as required dependencies, making the package lighter and more flexible. ([\#261](https://github.com/posit-dev/great-tables/issues/261), [\#271](https://github.com/posit-dev/great-tables/issues/271))


### Bug Fixes

- Fixed incorrect passing of nanoplot options to arguments in `_generate_nanoplot()`. ([\#258](https://github.com/posit-dev/great-tables/issues/258))
- Removed uses of `DataFrame.apply` and deprecated `dtype` methods for better compatibility. ([\#277](https://github.com/posit-dev/great-tables/issues/277))
- Closed file handles that were left open. ([\#281](https://github.com/posit-dev/great-tables/issues/281))


### Documentation

- Added examples for [fmt_nanoplot()](reference/GT.fmt_nanoplot.html#great_tables.GT.fmt_nanoplot). ([\#245](https://github.com/posit-dev/great-tables/issues/245))
- Added docs site and Codecov badges to the README. ([\#254](https://github.com/posit-dev/great-tables/issues/254))
- Improved examples in the Examples section. ([\#267](https://github.com/posit-dev/great-tables/issues/267))
- Fixed variable names in the Oceania example. ([\#264](https://github.com/posit-dev/great-tables/issues/264))
- Added warning callout for experimental status. ([\#243](https://github.com/posit-dev/great-tables/issues/243))


### Internal

- Refactored nanoplot internals. ([\#246](https://github.com/posit-dev/great-tables/issues/246))
- Added more tests for formatting methods. ([\#260](https://github.com/posit-dev/great-tables/issues/260))
- Added CodeCov integration to CI. ([\#250](https://github.com/posit-dev/great-tables/issues/250))
- Updated supported Python versions list to match those tested. ([\#269](https://github.com/posit-dev/great-tables/issues/269))


# v0.4.0

*2024-03-15* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.4.0)

This release introduces nanoplots (small inline plots embedded directly in table cells) and adds Polars selector support to all `fmt_*()` methods.


### New Features

- **Nanoplots** -- Embed small inline plots (sparklines, bar charts, etc.) directly within table cells for at-a-glance data visualization. ([\#219](https://github.com/posit-dev/great-tables/issues/219))
- **Polars selectors in `fmt_*()` methods** -- Use Polars selectors like `cs.starts_with()` to target columns in any formatting method. ([\#217](https://github.com/posit-dev/great-tables/issues/217))


### Bug Fixes

- Improved HTML representation of tables for better rendering. ([\#233](https://github.com/posit-dev/great-tables/issues/233))
- Header component HTML tags now pass HTML validation. ([\#235](https://github.com/posit-dev/great-tables/issues/235))
- The `'transparent'` color (and other named colors) now works in `tab_options(table_background_color=)`. ([\#242](https://github.com/posit-dev/great-tables/issues/242))
- Fixed a render reorder issue that caused incorrect row groupings. ([\#218](https://github.com/posit-dev/great-tables/issues/218))


### Documentation

- Fixed the [opt_horizontal_padding()](reference/GT.opt_horizontal_padding.html#great_tables.GT.opt_horizontal_padding) example. ([\#215](https://github.com/posit-dev/great-tables/issues/215))


# v0.3.1

*2024-02-27* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.3.1)

This release adds table export capabilities with `.save()` and `.as_raw_html()`, plus two new styling convenience methods. Several [data_color()](reference/GT.data_color.html#great_tables.GT.data_color) edge cases are now handled correctly.


### New Features

- **`.save()` and `.as_raw_html()` methods** -- Export tables to HTML files or retrieve raw HTML strings for embedding. ([\#208](https://github.com/posit-dev/great-tables/issues/208))
- **[opt_stylize()](reference/GT.opt_stylize.html#great_tables.GT.opt_stylize) method** -- Apply one of several pre-built table themes with a single method call. ([\#198](https://github.com/posit-dev/great-tables/issues/198))
- **[opt_table_outline()](reference/GT.opt_table_outline.html#great_tables.GT.opt_table_outline) method** -- Add or customize the table's outer border. ([\#209](https://github.com/posit-dev/great-tables/issues/209))


### Bug Fixes

- Fixed row rendering order to iterate over sorted rows. ([\#202](https://github.com/posit-dev/great-tables/issues/202))
- `np.nan` values are now correctly replaced with the `na_color=` value in [data_color()](reference/GT.data_color.html#great_tables.GT.data_color). ([\#205](https://github.com/posit-dev/great-tables/issues/205))
- [data_color()](reference/GT.data_color.html#great_tables.GT.data_color) now handles edge cases with single-value columns and all-missing columns. ([\#213](https://github.com/posit-dev/great-tables/issues/213))


### Documentation

- Added the `v0.3.0` release blog post. ([\#200](https://github.com/posit-dev/great-tables/issues/200))
- Added documentation on table themes. ([\#197](https://github.com/posit-dev/great-tables/issues/197))
- Added docs for the [fmt_image()](reference/GT.fmt_image.html#great_tables.GT.fmt_image) method. ([\#216](https://github.com/posit-dev/great-tables/issues/216))


### Internal

- Removed type annotations from docstrings. ([\#207](https://github.com/posit-dev/great-tables/issues/207))


# v0.3.0

*2024-02-16* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.3.0)

This release brings extensive table customization with [tab_options()](reference/GT.tab_options.html#great_tables.GT.tab_options) for global styling, [cols_width()](reference/GT.cols_width.html#great_tables.GT.cols_width) for column sizing, [fmt_image()](reference/GT.fmt_image.html#great_tables.GT.fmt_image) for embedding images, and several convenience methods for common styling patterns. ColorBrewer palettes are now available in [data_color()](reference/GT.data_color.html#great_tables.GT.data_color).


### New Features

- **[tab_options()](reference/GT.tab_options.html#great_tables.GT.tab_options) method** -- Configure global table styling options including fonts, colors, padding, and borders. ([\#146](https://github.com/posit-dev/great-tables/issues/146))
- **[cols_width()](reference/GT.cols_width.html#great_tables.GT.cols_width) method** -- Set explicit column widths using absolute or relative values. ([\#143](https://github.com/posit-dev/great-tables/issues/143))
- **[fmt_image()](reference/GT.fmt_image.html#great_tables.GT.fmt_image) method** -- Embed images directly in table cells from file paths or URLs. ([\#163](https://github.com/posit-dev/great-tables/issues/163))
- **[opt_align_table_header()](reference/GT.opt_align_table_header.html#great_tables.GT.opt_align_table_header) method** -- Quickly align the table header to the left, center, or right. ([\#147](https://github.com/posit-dev/great-tables/issues/147))
- **[opt_all_caps()](reference/GT.opt_all_caps.html#great_tables.GT.opt_all_caps) method** -- Apply all-caps styling to column labels, spanner labels, or stub text. ([\#150](https://github.com/posit-dev/great-tables/issues/150))
- **Vertical and horizontal padding options** -- New `opt_*` methods for adjusting cell padding. ([\#154](https://github.com/posit-dev/great-tables/issues/154))
- **[system_fonts()](reference/system_fonts.html#great_tables.system_fonts) helper** -- Access curated system font stacks for use in table options. ([\#158](https://github.com/posit-dev/great-tables/issues/158))
- **ColorBrewer palettes in [data_color()](reference/GT.data_color.html#great_tables.GT.data_color)** -- Use any ColorBrewer palette for data-driven coloring. ([\#186](https://github.com/posit-dev/great-tables/issues/186))


### Bug Fixes

- Replaced deprecated `with_row_count` with `with_row_index` for Polars compatibility. ([\#189](https://github.com/posit-dev/great-tables/issues/189), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))
- Table font names in [tab_options()](reference/GT.tab_options.html#great_tables.GT.tab_options) now accept both a string and a list. ([\#155](https://github.com/posit-dev/great-tables/issues/155))
- Fixed `FutureWarning` for `DataFrameGroupBy.grouper`. ([\#193](https://github.com/posit-dev/great-tables/issues/193), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


### Enhancements

- Added `py.typed` marker to support PEP 561 type-checking. ([\#139](https://github.com/posit-dev/great-tables/issues/139), [<span class="citation" cites="sugatoray">@sugatoray</span>](https://github.com/sugatoray))


### Documentation

- Added example using [sza](reference/data.sza.html#great_tables.data.sza) dataset with [data_color()](reference/GT.data_color.html#great_tables.GT.data_color). ([\#136](https://github.com/posit-dev/great-tables/issues/136))
- Published a Super Bowl blog post. ([\#184](https://github.com/posit-dev/great-tables/issues/184), [\#185](https://github.com/posit-dev/great-tables/issues/185))
- Added sports examples to the docs. ([\#195](https://github.com/posit-dev/great-tables/issues/195))
- Cleaned up examples in the API docs. ([\#191](https://github.com/posit-dev/great-tables/issues/191))
- Fixed a column name in the *Column Labels* documentation. ([\#187](https://github.com/posit-dev/great-tables/issues/187), [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw))


### New Contributors

- [<span class="citation" cites="sugatoray">@sugatoray</span>](https://github.com/sugatoray) made their first contribution in https://github.com/posit-dev/great-tables/pull/139
- [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) made their first contribution in https://github.com/posit-dev/great-tables/pull/189


# v0.2.0

*2024-01-24* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.2.0)

This release introduces the [data_color()](reference/GT.data_color.html#great_tables.GT.data_color) method for applying color scales to table data, along with several bug fixes for frame validation and spanner columns.


### New Features

- **[data_color()](reference/GT.data_color.html#great_tables.GT.data_color) method** -- Apply color scales to columns based on their underlying data values, with support for custom palettes and domains. ([\#109](https://github.com/posit-dev/great-tables/issues/109))


### Bug Fixes

- Fixed tab spanner column name resolution. ([\#111](https://github.com/posit-dev/great-tables/issues/111), [<span class="citation" cites="atseewal">@atseewal</span>](https://github.com/atseewal))
- Fixed frame validation to handle edge cases. ([\#118](https://github.com/posit-dev/great-tables/issues/118))
- Frame validation now coerces non-string column names. ([\#127](https://github.com/posit-dev/great-tables/issues/127))


### Enhancements

- Internal use of `to_list()` as a cross-DataFrame solution for better Pandas/Polars compatibility. ([\#128](https://github.com/posit-dev/great-tables/issues/128))


### Documentation

- Added a guide for [data_color()](reference/GT.data_color.html#great_tables.GT.data_color) and an introductory blog post for the new version. ([\#131](https://github.com/posit-dev/great-tables/issues/131))
- Published a blog post on Polars styling. ([\#113](https://github.com/posit-dev/great-tables/issues/113))


### New Contributors

- [<span class="citation" cites="atseewal">@atseewal</span>](https://github.com/atseewal) made their first contribution in https://github.com/posit-dev/great-tables/pull/111


# v0.1.5

*2024-01-05* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.5)

This release adds [fmt_datetime()](reference/GT.fmt_datetime.html#great_tables.GT.fmt_datetime) for date-time formatting and generalizes row selection across all methods that accept a `rows=` argument.


### New Features

- **[fmt_datetime()](reference/GT.fmt_datetime.html#great_tables.GT.fmt_datetime) method** -- Format datetime values in the table body with flexible date-time patterns. ([\#101](https://github.com/posit-dev/great-tables/issues/101))
- **Generalized row selectors** -- All `rows=` arguments now accept a function that operates on a DataFrame, making row selection in Pandas much easier. ([\#107](https://github.com/posit-dev/great-tables/issues/107))


### Documentation

- Published an introductory blog post for Great Tables. ([\#105](https://github.com/posit-dev/great-tables/issues/105))


# v0.1.4

*2023-12-19* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.4)

This release adds data-driven styling via `style.from_column()`, fixes column hiding and style application, and improves the documentation site.


### New Features

- **`style.from_column()`** -- Apply styles dynamically based on column values, implemented for [loc.body()](reference/loc.body.html#great_tables.loc.body). ([\#83](https://github.com/posit-dev/great-tables/issues/83))


### Enhancements

- [tab_style()](reference/GT.tab_style.html#great_tables.GT.tab_style) now accepts lists of styles and lists of locations. ([\#87](https://github.com/posit-dev/great-tables/issues/87))
- The compiled CSS ID value is now correctly applied to all rules. ([\#92](https://github.com/posit-dev/great-tables/issues/92))


### Bug Fixes

- Fixed [cols_hide()](reference/GT.cols_hide.html#great_tables.GT.cols_hide) not working correctly. ([\#86](https://github.com/posit-dev/great-tables/issues/86))


### Documentation

- Examples now display in a single column on narrow screens. ([\#81](https://github.com/posit-dev/great-tables/issues/81))
- Added a *Get Started* page on styling. ([\#88](https://github.com/posit-dev/great-tables/issues/88))
- Added interlinks throughout the documentation site. ([\#97](https://github.com/posit-dev/great-tables/issues/97))


# v0.1.3

*2023-12-12* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.3)

This release introduces the [tab_style()](reference/GT.tab_style.html#great_tables.GT.tab_style) method for targeted cell styling and includes several fixes to table rendering and source notes.


### New Features

- **[tab_style()](reference/GT.tab_style.html#great_tables.GT.tab_style) method** -- Apply custom styles to specific cells, columns, or rows using location selectors. ([\#68](https://github.com/posit-dev/great-tables/issues/68))


### Enhancements

- [loc.body()](reference/loc.body.html#great_tables.loc.body) now defaults to all columns and rows when called without arguments. ([\#79](https://github.com/posit-dev/great-tables/issues/79))
- [tab_source_note()](reference/GT.tab_source_note.html#great_tables.GT.tab_source_note) now works correctly with [md()](reference/md.html#great_tables.md) and [html()](reference/html.html#great_tables.html) helpers. ([\#77](https://github.com/posit-dev/great-tables/issues/77))


### Bug Fixes

- Fixed handling of addition operations in the SCSS template. ([\#72](https://github.com/posit-dev/great-tables/issues/72))


### Documentation

- Added hyperlinks in a table example. ([\#70](https://github.com/posit-dev/great-tables/issues/70), [<span class="citation" cites="kmasiello">@kmasiello</span>](https://github.com/kmasiello))


### Internal

- Added pre-commit checks to CI. ([\#78](https://github.com/posit-dev/great-tables/issues/78))


## New Contributors

- [<span class="citation" cites="kmasiello">@kmasiello</span>](https://github.com/kmasiello) made their first contribution in https://github.com/posit-dev/great-tables/pull/70


# v0.1.2

*2023-12-07* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.2)

This release adds Shiny integration for Great Tables, enabling interactive table rendering in Shiny for Python applications -- including support for Shinylive.


### New Features

- **Shiny support** -- A new `great_tables.shiny` module provides `output_gt()` and `render_gt()` for rendering GT tables in Shiny for Python apps. ([\#59](https://github.com/posit-dev/great-tables/issues/59))


### Enhancements

- Replaced `libsass` dependency with `webcolors`, enabling Great Tables to run in Shinylive. ([\#61](https://github.com/posit-dev/great-tables/issues/61))


### Documentation

- Fixed code example in README.md. ([\#62](https://github.com/posit-dev/great-tables/issues/62))


# v0.1.1

*2023-12-06* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.1)

Great Tables v0.1.1 is a maintenance release with bug fixes, improved test coverage, and a reorganization of built-in datasets.


### Enhancements

- Datasets (except [exibble](reference/data.exibble.html#great_tables.data.exibble)) are no longer exported from the top-level module; a `data` submodule is now the access point for all built-in datasets. ([\#57](https://github.com/posit-dev/great-tables/issues/57))


### Bug Fixes

- Column selections now correctly exclude columns that are in the stub. ([\#49](https://github.com/posit-dev/great-tables/issues/49))
- Several rendering issues were fixed. ([\#58](https://github.com/posit-dev/great-tables/issues/58))


### Internal

- Dataclasses are now frozen for improved immutability. ([\#50](https://github.com/posit-dev/great-tables/issues/50))
- Added several tests and incorporated `pytest-cov` for coverage reporting. ([\#53](https://github.com/posit-dev/great-tables/issues/53), [\#54](https://github.com/posit-dev/great-tables/issues/54), [\#55](https://github.com/posit-dev/great-tables/issues/55))


# v0.1.0

*2023-12-04* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.0)

This release rounds out the initial API, delivering full table structuring with spanners, row groups, and stub labels. Formatting methods are now complete with locale support, Polars DataFrames and selectors are fully supported, and the new `vals` submodule enables value formatting outside of a table context.


### New Features

- **Spanners, row groups, and stub labels** -- Tables can now be structured with column spanners, row groups, and stub labels for richer hierarchical layouts.
- **Polars support** -- Polars DataFrames are accepted as input data, and Polars selectors (e.g., `cs.starts_with`) can be used for column targeting.
- **`vals` submodule** -- Format values outside of a table context using the same formatting engine available in `fmt_*()` methods.


### Enhancements

- Formatting methods are now fully fleshed out with comprehensive locale support for number, currency, and date/time formatting.


### Documentation

- Added a *Get Started* guide to the documentation site.
- Added many examples throughout the API reference.


# v0.0.2

*2023-11-10* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.0.2)

This release introduces the foundational [GT](reference/GT.html#great_tables.GT) object with core table-building capabilities, including value formatting, header content, and annotation methods.


### New Features

- **[GT](reference/GT.html#great_tables.GT) class** -- A top-level table object providing the primary interface for building and customizing tables.
- **`fmt_*()` methods** -- A comprehensive set of formatting methods for transforming cell values in the table body.
- **Title and note methods** -- Methods for adding titles, subtitles, and table notes to provide context and annotations.


### Internal

- Groundwork for spanners, row columns, and group columns (to be exposed in a future release).

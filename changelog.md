# Changelog

This changelog is generated automatically from [GitHub Releases](https://github.com/posit-dev/great-tables/releases).


# v0.21.0: add [cols_merge()](reference/GT.cols_merge.html#great_tables.GT.cols_merge), [cols_label_with()](reference/GT.cols_label_with.html#great_tables.GT.cols_label_with), [opt_css()](reference/GT.opt_css.html#great_tables.GT.opt_css)

*2026-03-03* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.21.0)


## Deprecations

- The [opt_all_caps()](reference/GT.opt_all_caps.html#great_tables.GT.opt_all_caps) method now uses [loc.column_labels](reference/loc.column_labels.html#great_tables.loc.column_labels), [loc.stub](reference/loc.stub.html#great_tables.loc.stub), and [loc.row_groups](reference/loc.row_groups.html#great_tables.loc.row_groups) as arguments to `locations=`; using strings to represent the locations still works but triggers a deprecation warning (https://github.com/posit-dev/great-tables/pull/436)


## Features

- Added the [cols_merge()](reference/GT.cols_merge.html#great_tables.GT.cols_merge) method for combining cell contents across two or more columns by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/780
- Added the [cols_label_with()](reference/GT.cols_label_with.html#great_tables.GT.cols_label_with) method for function-based column relabeling by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/816
- Added the [fmt_engineering()](reference/GT.fmt_engineering.html#great_tables.GT.fmt_engineering) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/786
- The new [opt_css()](reference/GT.opt_css.html#great_tables.GT.opt_css) method lets you define arbitrary CSS rules for an HTML table by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/775
- Added the ability to define container padding in [tab_options()](reference/GT.tab_options.html#great_tables.GT.tab_options) by [<span class="citation" cites="thriller08">@thriller08</span>](https://github.com/thriller08) in https://github.com/posit-dev/great-tables/pull/802


## Fixes

- Refactored internal auto-align code for compatibility with Pandas 3.0.0 by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/810
- Added `int` to the `RowSelectExpr` definition by [<span class="citation" cites="tylerriccio33">@tylerriccio33</span>](https://github.com/tylerriccio33) in https://github.com/posit-dev/great-tables/pull/800
- Updated the Polars selector type annotation to use `Selector` by [<span class="citation" cites="schmidma">@schmidma</span>](https://github.com/schmidma) in https://github.com/posit-dev/great-tables/pull/770
- Annotated the [pipe](reference/GT.pipe.html#great_tables.GT.pipe) method's first argument type as [GT](reference/GT.html#great_tables.GT) by [<span class="citation" cites="FBruzzesi">@FBruzzesi</span>](https://github.com/FBruzzesi) in https://github.com/posit-dev/great-tables/pull/757
- We now correctly handle the `interactive_data_values=` properly in Nanoplots by [<span class="citation" cites="lorenzo-w">@lorenzo-w</span>](https://github.com/lorenzo-w) in https://github.com/posit-dev/great-tables/pull/792
- Group labels are now modified when `render_formats()` is called by [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23) in https://github.com/posit-dev/great-tables/pull/769
- The [opt_all_caps()](reference/GT.opt_all_caps.html#great_tables.GT.opt_all_caps) method has been refactored by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/436


## Docs

- Docs for the [val_fmt_engineering()](reference/vals.fmt_engineering.html#great_tables.vals.fmt_engineering) were added to the project website docs by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/808
- Corrected the `fns=` parameter docs in the [fmt()](reference/GT.fmt.html#great_tables.GT.fmt) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/818
- Improved the docs for the [from_column()](reference/from_column.html#great_tables.from_column) function by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/766
- Added a gt-extras example to the project website's Examples page by [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23) in https://github.com/posit-dev/great-tables/pull/759
- Added an example demonstrating usage of the [define_units()](reference/define_units.html#great_tables.define_units) function by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/446


## Chores

- Updated the copyright end year to 2026 by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/804
- Several typos were fixed by [<span class="citation" cites="kianmeng">@kianmeng</span>](https://github.com/kianmeng) in https://github.com/posit-dev/great-tables/pull/798
- Added Plausible analytics to the project website by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/806
- Added several tests for the [opt_all_caps()](reference/GT.opt_all_caps.html#great_tables.GT.opt_all_caps) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/812
- Fixed the checkout version tag by [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23) in https://github.com/posit-dev/great-tables/pull/768


## New Contributors

- [<span class="citation" cites="kianmeng">@kianmeng</span>](https://github.com/kianmeng) made their first contribution in https://github.com/posit-dev/great-tables/pull/798
- [<span class="citation" cites="thriller08">@thriller08</span>](https://github.com/thriller08) made their first contribution in https://github.com/posit-dev/great-tables/pull/802
- [<span class="citation" cites="schmidma">@schmidma</span>](https://github.com/schmidma) made their first contribution in https://github.com/posit-dev/great-tables/pull/770
- [<span class="citation" cites="lorenzo-w">@lorenzo-w</span>](https://github.com/lorenzo-w) made their first contribution in https://github.com/posit-dev/great-tables/pull/792

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.20.0…v0.21.0](https://github.com/posit-dev/great-tables/compare/v0.20.0...v0.21.0)


# v0.20.0

*2025-10-31* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.20.0)


## Features

- Add [grand_summary_rows()](reference/GT.grand_summary_rows.html#great_tables.GT.grand_summary_rows) method by [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23) in https://github.com/posit-dev/great-tables/pull/765
- Support polars expressions in vals functions by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/793

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.19.0…v0.20.0](https://github.com/posit-dev/great-tables/compare/v0.19.0...v0.20.0)


# v0.19.0

*2025-10-07* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.19.0)


## Fixes

- Code using the NumPy library was replaced with standard Python to enable the removal of NumPy from the dependencies list, by [<span class="citation" cites="tylerriccio33">@tylerriccio33</span>](https://github.com/tylerriccio33) in https://github.com/posit-dev/great-tables/pull/749
- An error when setting `groupname_col=` without `rowname_col=` in the [GT](reference/GT.html#great_tables.GT) constructor has been fixed by [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23) in https://github.com/posit-dev/great-tables/pull/756
- Using `row_group_as_column = True` now structures row groups as a column in the stub (previously, this was a no-op), by [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23) in https://github.com/posit-dev/great-tables/pull/754
- The [data_color()](reference/GT.data_color.html#great_tables.GT.data_color) method now takes the alpha value for the cell background color into account when choosing the foreground text color (fixes the internal `_ideal_fgnd_color()` util function), by [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23) in https://github.com/posit-dev/great-tables/pull/747
- When enabling row striping, there is now better color contrast between the text and the underlying cell background, by [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23) in https://github.com/posit-dev/great-tables/pull/745
- We now internally access column names consistently through `get_column_names()` instead of `.columns`, by [<span class="citation" cites="FBruzzesi">@FBruzzesi</span>](https://github.com/FBruzzesi) in https://github.com/posit-dev/great-tables/pull/736
- Column values with the `pyarrow` `float64` type are now right-aligned to match the default behavior when using Pandas and Polars DFs, by [<span class="citation" cites="FBruzzesi">@FBruzzesi</span>](https://github.com/FBruzzesi) in https://github.com/posit-dev/great-tables/pull/734
- We now avoid the double use of `clear` internally with Polars DFs, by [<span class="citation" cites="FBruzzesi">@FBruzzesi</span>](https://github.com/FBruzzesi) in https://github.com/posit-dev/great-tables/pull/729


## Docs

- Various typos were corrected by [<span class="citation" cites="FBruzzesi">@FBruzzesi</span>](https://github.com/FBruzzesi) in https://github.com/posit-dev/great-tables/pull/730
- We now include a Posit badge in the header of the project website, by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/777


## Chores

- Refactoring was done to better adhere to best practices and to improve code performance, by [<span class="citation" cites="FBruzzesi">@FBruzzesi</span>](https://github.com/FBruzzesi) in https://github.com/posit-dev/great-tables/pull/731


## New Contributors

- [<span class="citation" cites="FBruzzesi">@FBruzzesi</span>](https://github.com/FBruzzesi) made their first contribution in https://github.com/posit-dev/great-tables/pull/731

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.18.0…v0.19.0](https://github.com/posit-dev/great-tables/compare/v0.18.0...v0.19.0)


# v0.18.0

*2025-07-10* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.18.0)


## What's Changed


## Features

- The new [tab_spanner_delim()](reference/GT.tab_spanner_delim.html#great_tables.GT.tab_spanner_delim) method allows for quick creation of spanners through delimited column names, by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/647
- Added the [cols_label_rotate()](reference/GT.cols_label_rotate.html#great_tables.GT.cols_label_rotate) method for rotating column label text 90 degrees, by [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23) in https://github.com/posit-dev/great-tables/pull/696
- We can now easily format boolean values with the new [fmt_tf()](reference/GT.fmt_tf.html#great_tables.GT.fmt_tf) formatting method, by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) (https://github.com/posit-dev/great-tables/pull/665, https://github.com/posit-dev/great-tables/pull/704)
- The [fmt_datetime()](reference/GT.fmt_datetime.html#great_tables.GT.fmt_datetime) method now lets you perform custom datetime formatting with the new `format_str=` parameter, by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/645
- GT tables can now be pickled, by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/641
- The [fmt_currency()](reference/GT.fmt_currency.html#great_tables.GT.fmt_currency) method gained a `compact=` parameter for display of compact currency values (e.g., `$13.4M`), by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/664
- Added the `truncate=` option to [data_color()](reference/GT.data_color.html#great_tables.GT.data_color) by [<span class="citation" cites="mahdibaghbanzadeh">@mahdibaghbanzadeh</span>](https://github.com/mahdibaghbanzadeh) in https://github.com/posit-dev/great-tables/pull/673
- The Pandas dependency in [vals.fmt_integer()](reference/vals.fmt_integer.html#great_tables.vals.fmt_integer) was removed by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/719


## Fixes

- Remove unused `sep_mark=` parameter from the [fmt_scientific()](reference/GT.fmt_scientific.html#great_tables.GT.fmt_scientific) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/642
- Fixed an off-by-one bug in the `rescale_factor()` utility function (which had an adverse effect on [data_color()](reference/GT.data_color.html#great_tables.GT.data_color)), by [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23) in https://github.com/posit-dev/great-tables/pull/718
- When using Google Fonts in an HTML table there will no longer be any duplicated font import statements, by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/708
- An issue with row striping (due to incorrect indexing) was resolved by [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23) in https://github.com/posit-dev/great-tables/pull/701
- Spanners can now be correctly styled with [tab_style()](reference/GT.tab_style.html#great_tables.GT.tab_style), by [<span class="citation" cites="ChristopherRussell">@ChristopherRussell</span>](https://github.com/ChristopherRussell) in https://github.com/posit-dev/great-tables/pull/695


## Docs

- Added note about using `.show("browser")` when in VS Code by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/643
- A warning message from [cols_width()](reference/GT.cols_width.html#great_tables.GT.cols_width) that appeared in the docs is now suppressed, by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/659
- Updated docstrings for date/time formatting methods, by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/658
- We now use improved the interlinking functionality available in quartodoc, by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/697
- In the documentation site, added an underline to active link in top navigation bar by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/706
- Improved the documentation for the [as_raw_html()](reference/GT.as_raw_html.html#great_tables.GT.as_raw_html) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/707
- We now better introduce the use of [show()](reference/GT.show.html#great_tables.GT.show) method in the docs through a callout, by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/712


## Chores

- Added a `no pandas` dependency test of functions in the `vals` module by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/689


## New Contributors

- [<span class="citation" cites="dpprdan">@dpprdan</span>](https://github.com/dpprdan) made their first contribution in https://github.com/posit-dev/great-tables/pull/670
- [<span class="citation" cites="juleswg23">@juleswg23</span>](https://github.com/juleswg23) made their first contribution in https://github.com/posit-dev/great-tables/pull/696
- [<span class="citation" cites="ChristopherRussell">@ChristopherRussell</span>](https://github.com/ChristopherRussell) made their first contribution in https://github.com/posit-dev/great-tables/pull/695
- [<span class="citation" cites="mahdibaghbanzadeh">@mahdibaghbanzadeh</span>](https://github.com/mahdibaghbanzadeh) made their first contribution in https://github.com/posit-dev/great-tables/pull/673

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.17.0…v0.18.0](https://github.com/posit-dev/great-tables/compare/v0.17.0...v0.18.0)


# v0.17.0: unique html IDs, `css-inline` package optional

*2025-03-11* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.17.0)


## Breaking changes

- Ensure HTML ID attributes are unique by [<span class="citation" cites="BenGale93">@BenGale93</span>](https://github.com/BenGale93) in https://github.com/posit-dev/great-tables/pull/607
- Move `css-inline` pkg to extra group by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/634


## Features

- Quarto option to disable table processing, warn on render by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/611
- Add [cols_unhide()](reference/GT.cols_unhide.html#great_tables.GT.cols_unhide) method by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/629
- Add `inline_css=` argument by [<span class="citation" cites="tylerriccio33">@tylerriccio33</span>](https://github.com/tylerriccio33) in https://github.com/posit-dev/great-tables/pull/633


## Fixes

- Ensure HTML ID attributes are unique by [<span class="citation" cites="BenGale93">@BenGale93</span>](https://github.com/BenGale93) in https://github.com/posit-dev/great-tables/pull/607
- Move `css-inline` pkg to extra group by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/634
- Do not always save screenshot as png by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/599
- Resolve encoding issue in `GT.save()` by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/609
- Correctly pass non-ints to nanoplot options by [<span class="citation" cites="tylerriccio33">@tylerriccio33</span>](https://github.com/tylerriccio33) in https://github.com/posit-dev/great-tables/pull/608
- Scientific notation zero padding when `exp_style=` used by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/622
  - e.g. numbers like `"2.3E-03"` were incorrectly displayed as `"2.3E−30"`.
- Update conditional statement in nanoplot code to guard against string values (single string or list containing any strings) by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/623


## Docs

- Update the related docs about `mask=` parameter in [loc.body()](reference/loc.body.html#great_tables.loc.body) by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/589
- Update the preview of `year` col in [gtcars](reference/data.gtcars.html#great_tables.data.gtcars) dataset by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/587
- Add examples to the documentation by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/618
- Add [style.css](reference/style.css.html#great_tables.style.css) entry to API reference docs by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/624
- Align getting started guide with readme by [<span class="citation" cites="zachvalenta">@zachvalenta</span>](https://github.com/zachvalenta) in https://github.com/posit-dev/great-tables/pull/627


## Chores

- Use deploy-pypi environment by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/590
  - Added a environment deployment protection rule. We now have to review the release workflow.


## New Contributors

- [<span class="citation" cites="tylerriccio33">@tylerriccio33</span>](https://github.com/tylerriccio33) made their first contribution in https://github.com/posit-dev/great-tables/pull/608
- [<span class="citation" cites="BenGale93">@BenGale93</span>](https://github.com/BenGale93) made their first contribution in https://github.com/posit-dev/great-tables/pull/607
- [<span class="citation" cites="zachvalenta">@zachvalenta</span>](https://github.com/zachvalenta) made their first contribution in https://github.com/posit-dev/great-tables/pull/627

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.16.1…v0.17.0](https://github.com/posit-dev/great-tables/compare/v0.16.1...v0.17.0)


# v0.16.1

*2025-01-24* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.16.1)


## Fixes

- Update dtype of `year` col in [gtcars](reference/data.gtcars.html#great_tables.data.gtcars) dataset by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/586

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.16.0…v0.16.1](https://github.com/posit-dev/great-tables/compare/v0.16.0...v0.16.1)


# v0.16.0

*2025-01-24* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.16.0)


## Features

- Add the `mask=` argument to [LocBody](reference/loc.body.html#great_tables.loc.body) to enable enhanced body cell targeting by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/566
- Include [write_raw_html()](reference/GT.write_raw_html.html#great_tables.GT.write_raw_html) as a helper function for easier HTML output by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/485


## Fixes

- Fix the deprecation warning in [as_raw_html()](reference/GT.as_raw_html.html#great_tables.GT.as_raw_html) for Python 3.13 by [<span class="citation" cites="stinodego">@stinodego</span>](https://github.com/stinodego) in https://github.com/posit-dev/great-tables/pull/563
- Support the `pl.UInt` type in nanoplots by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/577


## Docs

- Add pyOpenSci and DOI badges to `README.md` to acknowledge the successful peer-review of the package by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/576
- Update images and text around included datasets in the package by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/562
- Replace JSON dataset with .ndjson file in coffee sales examples to sidestep a serialization error by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/580


## New Contributors

- [<span class="citation" cites="stinodego">@stinodego</span>](https://github.com/stinodego) made their first contribution in https://github.com/posit-dev/great-tables/pull/563

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.15.0…v0.16.0](https://github.com/posit-dev/great-tables/compare/v0.15.0...v0.16.0)


# v0.15.0: add Experimental support for using a `pyarrow.Table` as input

*2024-12-14* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.15.0)


## Features

- There is now experimental support for using a `pyarrow.Table` as input by [<span class="citation" cites="amol">@amol</span>](https://github.com/amol)- in https://github.com/posit-dev/great-tables/pull/487
- The [fmt_flag()](reference/GT.fmt_flag.html#great_tables.GT.fmt_flag) method has been added so that you can display flag icons based on country codes by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/523
- With the new [fmt_icon()](reference/GT.fmt_icon.html#great_tables.GT.fmt_icon) method, it's possible to have FontAwesome icons within table cells by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/515
- The [fmt_number()](reference/GT.fmt_number.html#great_tables.GT.fmt_number), [fmt_percent()](reference/GT.fmt_percent.html#great_tables.GT.fmt_percent), [fmt_integer()](reference/GT.fmt_integer.html#great_tables.GT.fmt_integer) and [fmt_currency()](reference/GT.fmt_currency.html#great_tables.GT.fmt_currency) methods can now format values in accounting notation by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/513
- Tables can be written as CSS-inlined HTML strings via [as_raw_html()](reference/GT.as_raw_html.html#great_tables.GT.as_raw_html) with the new `inline_css=` argument by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/557
- The `save()` method has been greatly enhanced and includes the ability to perform intermediate saves (since the method returns itself) by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/499
- Enhance the [fmt_image()](reference/GT.fmt_image.html#great_tables.GT.fmt_image) method to support `http`/`https` schema in the `columns=` parameter by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/520
- The [pipe()](reference/GT.pipe.html#great_tables.GT.pipe) method has been added and it operates similarly to that of the Pandas and Polars APIs, by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/363


## Fixes

- Improve detection of Polars installation by [<span class="citation" cites="lukemanley">@lukemanley</span>](https://github.com/lukemanley) in https://github.com/posit-dev/great-tables/pull/505
- Add CI build for testing Python 3.13 by [<span class="citation" cites="glemaitre">@glemaitre</span>](https://github.com/glemaitre) in https://github.com/posit-dev/great-tables/pull/514
- Having hidden columns along with column width definitions no longer mangles HTML table output by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/509
- Some `mypy` errors were fixed and the project was switched to ruff linting and formatting by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/511
- The CI README badge now properly reports build status by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/553
- Fix missing exception raise in `_val_is_numeric()` and `_val_is_str()` by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/510
- Standardize imports by converting absolute imports to relative imports by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/521
- Exclude `if TYPE_CHECKING:` lines from coverage reports by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/556


## Docs

- Include the [vals.fmt_image()](reference/vals.fmt_image.html#great_tables.vals.fmt_image) function in the API reference by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/486
- Make spelling fixes in the contributing guide by [<span class="citation" cites="glemaitre">@glemaitre</span>](https://github.com/glemaitre) in https://github.com/posit-dev/great-tables/pull/516
- Add information about Pandas requirement when using internal datasets by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) (https://github.com/posit-dev/great-tables/pull/549, https://github.com/posit-dev/great-tables/pull/559)
- Add a `CITATION.cff` file and provide citation information in README by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/551
- Update README with conda install instructions and some clarity on which environments Great Tables can be used in, by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/552
- Improve presentation of Contributing Guidelines by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/550


## New Contributors

- [<span class="citation" cites="lukemanley">@lukemanley</span>](https://github.com/lukemanley) made their first contribution in https://github.com/posit-dev/great-tables/pull/505
- [<span class="citation" cites="glemaitre">@glemaitre</span>](https://github.com/glemaitre) made their first contribution in https://github.com/posit-dev/great-tables/pull/514
- [<span class="citation" cites="amol">@amol</span>](https://github.com/amol)- made their first contribution in https://github.com/posit-dev/great-tables/pull/487

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.14.0…v0.15.0](https://github.com/posit-dev/great-tables/compare/v0.14.0...v0.15.0)


# v0.14.0: add experimental support for LaTeX output

*2024-11-11* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.14.0)


## Features

- Experimental support for LaTeX-table rendering with new `.as_latex()` method (see important information on current limitations in API reference at https://posit-dev.github.io/great-tables/reference/GT.as_latex.html) by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/481


## Docs

- The Reference API docs now have an improved presentation when viewed on lower-width devices by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) (https://github.com/posit-dev/great-tables/pull/427, https://github.com/posit-dev/great-tables/pull/492)
- Preview sections have been added for the built-in datasets by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/453

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.13.0…v0.14.0](https://github.com/posit-dev/great-tables/compare/v0.13.0...v0.14.0)


# v0.13.0: add more location specifiers to `loc`

*2024-10-04* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.13.0)


## Features

- Include [google_font()](reference/google_font.html#great_tables.google_font) helper fn in API reference by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) and [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in ([\#464](https://github.com/posit-dev/great-tables/issues/464), [\#471](https://github.com/posit-dev/great-tables/issues/471))
- Allow for granular section restyling via convenience api by [<span class="citation" cites="timkpaine">@timkpaine</span>](https://github.com/timkpaine) in https://github.com/posit-dev/great-tables/pull/341
- Add [val_fmt_image()](reference/vals.fmt_image.html#great_tables.vals.fmt_image) to enable image rendering in various components by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/451
- Allow passing a webdriver instance to save by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/478


## Fixes

- Resolve global `locale` not being respected in `GT.fmt_*()` functions by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/473


## Docs

- Do not document GT members inline on its reference page by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/475
- Fix deprecated warning for `pl.DataFrame.pivot()` by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/472
- Update docs and code to support `GoogleFont` in [opt_table_font()](reference/GT.opt_table_font.html#great_tables.GT.opt_table_font) and add tests by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/470
- Fix in headers causing their css classes get printed out by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/477
- Add docstrings for new location methods by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/474

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.12.0…v0.13.0](https://github.com/posit-dev/great-tables/compare/v0.12.0...v0.13.0)


# v0.12.0: opt_stylize produces striped rows and borders

*2024-09-27* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.12.0)


## Breaking changes

- [opt_stylize()](reference/GT.opt_stylize.html#great_tables.GT.opt_stylize) now produces stripes by default. Set `add_row_striping=False` to remove. ([\#461](https://github.com/posit-dev/great-tables/issues/461))
- [opt_stylize()](reference/GT.opt_stylize.html#great_tables.GT.opt_stylize) now adds borders to certain styles (which was the original intention; [\#463](https://github.com/posit-dev/great-tables/issues/463))


## Features

- add [google_font()](reference/google_font.html#great_tables.google_font) helper, implement in [opt_table_font()](reference/GT.opt_table_font.html#great_tables.GT.opt_table_font) and [style.text()](reference/style.text.html#great_tables.style.text) by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/423
- implement row striping options by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) ([\#461](https://github.com/posit-dev/great-tables/issues/461), [\#463](https://github.com/posit-dev/great-tables/issues/463))


## Fixes

- use full html page in [show()](reference/GT.show.html#great_tables.GT.show) for correct utf-8 display by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/458


## Docs

- update `superbowl` example to align with the new version of `Polars` by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) ([\#460](https://github.com/posit-dev/great-tables/issues/460), [\#462](https://github.com/posit-dev/great-tables/issues/462))

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.11.1…v0.12.0](https://github.com/posit-dev/great-tables/compare/v0.11.1...v0.12.0)


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


# v0.11.0: include column labels in`<thead>` element

*2024-08-30* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.11.0)

This release contains a breaking change in how HTML output tables are structured (through tag changes). There is also an important fix for saving tables via the `.save()` method using the Google Chrome webdriver.


## Breaking Changes

- We now ensure that the `<thead>` element encloses both title/subtitle and column labels by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/421


## Fixes

- We now ensure that the `<thead>` element encloses both title/subtitle and column labels by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/421
- The `.save` method works with latest version of Google Chrome by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/425


## Docs

- Mention support for `Polars` in the `get-started` section by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/408
- Made tiny typo fixes and improved a code example in the "Design Philosophy" doc by [<span class="citation" cites="alfredocarella">@alfredocarella</span>](https://github.com/alfredocarella) in https://github.com/posit-dev/great-tables/pull/401
- Fix typo in blog post by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/396
- Update documentation for datasets by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/397
- Update polars examples for deprecated arg by [<span class="citation" cites="atseewal">@atseewal</span>](https://github.com/atseewal) in https://github.com/posit-dev/great-tables/pull/400
- Remove mentions of `accounting` in `force_sign=` argument by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/422


## New Contributors

- [<span class="citation" cites="alfredocarella">@alfredocarella</span>](https://github.com/alfredocarella) made their first contribution in https://github.com/posit-dev/great-tables/pull/401

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.10.0…v0.11.0](https://github.com/posit-dev/great-tables/compare/v0.10.0...v0.11.0)


# v0.10.0

*2024-07-08* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.10.0)


## Features

- Add ability to express units in `.cols_label()` by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/380
- Allow spanners to use units notation in `.tab_spanner()` by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/393
- The `.opt_table_font()` method has been added to make it easy to set a default table font; by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/272
- Add the `.show()` method by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/379
- Several new datasets were added (bringing total number up to 16) by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/382


## Fixes

- fix `.fmt_percent()` issue with polars-u64-idx by [<span class="citation" cites="lostmygithubaccount">@lostmygithubaccount</span>](https://github.com/lostmygithubaccount) in https://github.com/posit-dev/great-tables/pull/388
- Add render target for HTML pages by [<span class="citation" cites="isabelizimm">@isabelizimm</span>](https://github.com/isabelizimm) in https://github.com/posit-dev/great-tables/pull/377
- `.show()` no longer raises or prints to stderr by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/384


## Docs

- Add absolute URLs to README to improve PyPI summary by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/373


## New Contributors

- [<span class="citation" cites="isabelizimm">@isabelizimm</span>](https://github.com/isabelizimm) made their first contribution in https://github.com/posit-dev/great-tables/pull/377
- [<span class="citation" cites="lostmygithubaccount">@lostmygithubaccount</span>](https://github.com/lostmygithubaccount) made their first contribution in https://github.com/posit-dev/great-tables/pull/388

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.9.0…v0.10.0](https://github.com/posit-dev/great-tables/compare/v0.9.0...v0.10.0)


# v0.9.0: breaking change, add rows parameter to data_color()

*2024-06-06* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.9.0)


## Features

- **feat!**: support specifying a subset of rows in [GT.data_color()](reference/GT.data_color.html#great_tables.GT.data_color) by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/364
  - Note that `rows=` is now the third argument, which may break earlier code.

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.8.0…v0.9.0](https://github.com/posit-dev/great-tables/compare/v0.8.0...v0.9.0)


# v0.8.0

*2024-06-06* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.8.0)


## Features

- add method equivalents of constructor options by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/371
  - `GT.tab_stub(rowname_col=, groupname_col=)`
  - `GT.with_local()`
  - [GT.with_id()](reference/GT.with_id.html#great_tables.GT.with_id)

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.7.0…v0.8.0](https://github.com/posit-dev/great-tables/compare/v0.7.0...v0.8.0)


# v0.7.0

*2024-06-04* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.7.0)


## What's Changed


## Features

- Add the `.fmt_units()` method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/240
- Support Polars' non-strict `expand_selector()` by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/368


## Fixes

- General enhancements to several `.cols_*()` methods by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/366
- Generate better error message for list data used in `.fmt_nanoplot()` by [<span class="citation" cites="marcozzxx810">@marcozzxx810</span>](https://github.com/marcozzxx810) in https://github.com/posit-dev/great-tables/pull/356


## Docs

- Add RSS feed to blog by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/367


## Chores

- Refactor `seq_groups()` to accept `Iterable` by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/365
- Move `pairwise()`, `seq_groups()`, and `is_equal()` functions to `_utils.py` by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/369

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.6.1…v0.7.0](https://github.com/posit-dev/great-tables/compare/v0.6.1...v0.7.0)


# v0.6.1

*2024-05-23* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.6.1)


## Fixes

- Fix column selections breaking with `Polars` `v0.20.28` by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/360
- Fix `_save_screenshot()` breaking for non-png files by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/352


## Chores

- Enhance the test coverage by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/339
- Remove unneeded files by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/351

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.6.0…v0.6.1](https://github.com/posit-dev/great-tables/compare/v0.6.0...v0.6.1)


# v0.6.0

*2024-05-16* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.6.0)

This release brings support for multi-level spanners (a huge thanks to [<span class="citation" cites="timkpaine">@timkpaine</span>](https://github.com/timkpaine)), and makes saving tables with `GT.save()` a bit more robust.


## Features

- Support multi-level spanners by [<span class="citation" cites="timkpaine">@timkpaine</span>](https://github.com/timkpaine) in https://github.com/posit-dev/great-tables/pull/345


## Fixes

- ensure export() always captures full table by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/344


## Docs

- add example coffee table with nanoplots by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/349
- clean up minor formatting issues in the docs by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/338


## New Contributors

- [<span class="citation" cites="timkpaine">@timkpaine</span>](https://github.com/timkpaine) made their first contribution in https://github.com/posit-dev/great-tables/pull/345

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/0.5.2…v0.6.0](https://github.com/posit-dev/great-tables/compare/0.5.2...v0.6.0)


# 0.5.2

*2024-05-13* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/0.5.2)


## Fixes

- Fix [CellStyleBorders](reference/style.borders.html#great_tables.style.borders) not being properly constructed when [sides](reference/style.borders.html#great_tables.style.borders.sides) is set to "all" by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/326
- Fix [GT.fmt_image()](reference/GT.fmt_image.html#great_tables.GT.fmt_image) erroring on missing values by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/329
- Nanoplots listcols now work, polars list columns no longer raise error by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/330
- Nanoplots no longer fail for lists of large integers by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/335
- [GT.fmt_number()](reference/GT.fmt_number.html#great_tables.GT.fmt_number) no longer puts improper comma for 3-digit compact, negative numbers by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/335


## Docs

- Add examples to reference pages by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/328


## Chores

- Remove unused library webcolors as required dependency by [<span class="citation" cites="marcozzxx810">@marcozzxx810</span>](https://github.com/marcozzxx810) in https://github.com/posit-dev/great-tables/pull/336


## New Contributors

- [<span class="citation" cites="marcozzxx810">@marcozzxx810</span>](https://github.com/marcozzxx810) made their first contribution in https://github.com/posit-dev/great-tables/pull/336

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.5.1…0.5.2](https://github.com/posit-dev/great-tables/compare/v0.5.1...0.5.2)


# v0.5.1

*2024-05-03* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.5.1)

Thanks so much to [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) for an incredible amount of fixes and improvements! This release doesn't have any new features, instead we focused on fixes and documentation.


## Fixes

- Resolve issue with `table_font_color=` not accepting named colors by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/285
- Ensure that group label rows have valid HTML by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/308
- Fix Polars selectors error in [GT.cols_hide()](reference/GT.cols_hide.html#great_tables.GT.cols_hide) by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/316
- Fix missing values not working with [GT.fmt_number()](reference/GT.fmt_number.html#great_tables.GT.fmt_number) by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/317
- Fix display for integerlike values in nanoplots by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/319


## Docs

- Fix typos in docs by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/286
- Add example from [<span class="citation" cites="chalg">@chalg</span>](https://github.com/chalg) by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/323


## Chores

- Clean up implementation of [GT.fmt_nanoplot()](reference/GT.fmt_nanoplot.html#great_tables.GT.fmt_nanoplot) and [GT.data_color()](reference/GT.data_color.html#great_tables.GT.data_color) by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) https://github.com/posit-dev/great-tables/pull/294, https://github.com/posit-dev/great-tables/pull/295
- Refactor [GT.fmt_time()](reference/GT.fmt_time.html#great_tables.GT.fmt_time), [GT.fmt_date()](reference/GT.fmt_date.html#great_tables.GT.fmt_date) and [GT.fmt_datetime()](reference/GT.fmt_datetime.html#great_tables.GT.fmt_datetime) by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/290
- Refactor `letters` and `Letters` functions in `_helpers` by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/289
- Update type hints and organize import modules by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/315
- Codebase cleanup and minor improvements by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/305, https://github.com/posit-dev/great-tables/pull/292
- Improve test coverage by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) https://github.com/posit-dev/great-tables/pull/311, https://github.com/posit-dev/great-tables/pull/325
- Add tests for [GT.cols_align()](reference/GT.cols_align.html#great_tables.GT.cols_align) and extend support for `Polars` expressions by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/320

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.5.0…v0.5.1](https://github.com/posit-dev/great-tables/compare/v0.5.0...v0.5.1)


# v0.5.0

*2024-04-12* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.5.0)


## What's Changed


### Features

- Remove mizani and pandas as dependencies by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) ([\#271](https://github.com/posit-dev/great-tables/issues/271), [\#261](https://github.com/posit-dev/great-tables/issues/261))
- Include choice of webdrivers in the `.save()` method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/262
- Add sub_missing and sub_zero methods by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/244


### Fixes

- Fix error from incorrectly passing nanoplot options to args in `_generate_nanoplot()` by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/258
- Remove uses of DataFrame.apply and dtype methods by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/277
- Close some opened files by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/281


### Docs

- Add warning callout for experimental status by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/243
- Add examples for [fmt_nanoplot()](reference/GT.fmt_nanoplot.html#great_tables.GT.fmt_nanoplot) by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/245
- Add docs site and codecov badges by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/254
- Rename variables on example code for Oceania by [<span class="citation" cites="sergiolaverde0">@sergiolaverde0</span>](https://github.com/sergiolaverde0) in https://github.com/posit-dev/great-tables/pull/264
- Improve two examples in Examples section by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/267


### Chores

- Refactor nanoplots by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/246
- Add more tests for formatting methods by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/260
- ci: workflow pushes to CodeCov by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/250
- Update list of supported Python versions to match those tested by [<span class="citation" cites="discdiver">@discdiver</span>](https://github.com/discdiver) in https://github.com/posit-dev/great-tables/pull/269


## New Contributors

- [<span class="citation" cites="sergiolaverde0">@sergiolaverde0</span>](https://github.com/sergiolaverde0) made their first contribution in https://github.com/posit-dev/great-tables/pull/264
- [<span class="citation" cites="discdiver">@discdiver</span>](https://github.com/discdiver) made their first contribution in https://github.com/posit-dev/great-tables/pull/269

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.4.0…v0.5.0](https://github.com/posit-dev/great-tables/compare/v0.4.0...v0.5.0)


# v0.4.0

*2024-03-15* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.4.0)


## What's Changed


### Features

- Add initial implementation for nanoplots by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/219
- Allow polars selectors in `fmt_*()` methods by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/217


### Fixes

- Improve HTML representation of tables by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/233
- Ensure that header component HTML tags pass HTML validation by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/235
- Allow the 'transparent' color (and others) to be used in `tab_options(table_background_color == <color>)` by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/242
- Fix render reorder causing incorrect groupings by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/218


### Docs

- Fix [opt_horizontal_padding()](reference/GT.opt_horizontal_padding.html#great_tables.GT.opt_horizontal_padding) example by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/215

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.3.1…v0.4.0](https://github.com/posit-dev/great-tables/compare/v0.3.1...v0.4.0)


# v0.3.1

*2024-02-27* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.3.1)


## What's Changed


### Features

- Add the `.save()` and `.as_raw_html()` methods by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/208
- Add the [opt_stylize()](reference/GT.opt_stylize.html#great_tables.GT.opt_stylize) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/198
- Add the [opt_table_outline()](reference/GT.opt_table_outline.html#great_tables.GT.opt_table_outline) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/209


### Fixes

- fix: iterate over sorted rows for rendering by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/202
- Remove type annotations from docstrings by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/207
- Ensure that np.nan values are replaced with `na_color=` vals by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/205
- Handle `.data_color()` edge cases with single val columns / all missing values by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/213


### Docs

- Add the `v0.3.0` release post by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/200
- Docs table themes by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/197
- Add docs to the [fmt_image()](reference/GT.fmt_image.html#great_tables.GT.fmt_image) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/216

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.3.0…v0.3.1](https://github.com/posit-dev/great-tables/compare/v0.3.0...v0.3.1)


# v0.3.0

*2024-02-16* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.3.0)


## What's Changed


### Features

- Add the [cols_width()](reference/GT.cols_width.html#great_tables.GT.cols_width) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/143
- Add the [tab_options()](reference/GT.tab_options.html#great_tables.GT.tab_options) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/146
- Add `opt*` methods for vertical and horizontal padding by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/154
- Add the [opt_align_table_header()](reference/GT.opt_align_table_header.html#great_tables.GT.opt_align_table_header) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/147
- Add the [opt_all_caps()](reference/GT.opt_all_caps.html#great_tables.GT.opt_all_caps) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/150
- Add the [fmt_image()](reference/GT.fmt_image.html#great_tables.GT.fmt_image) method by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/163
- Add the [system_fonts()](reference/system_fonts.html#great_tables.system_fonts) helper function by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/158
- Enable use of ColorBrewer palettes in [data_color()](reference/GT.data_color.html#great_tables.GT.data_color) by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/186


### Fixes

- Replace `with_row_count` by `with_row_index` for `Polars` by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/189
- Add `py.typed` to support PEP-561 (type-hinting) by [<span class="citation" cites="sugatoray">@sugatoray</span>](https://github.com/sugatoray) in https://github.com/posit-dev/great-tables/pull/139
- Ensure table font names (from [tab_options()](reference/GT.tab_options.html#great_tables.GT.tab_options)) is accepted as str or list by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/155
- Fix `FutureWarning` for `DataFrameGroupBy.grouper` by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/193


### Docs

- docs: update one of the column names for `Column Labels` by [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) in https://github.com/posit-dev/great-tables/pull/187
- docs: blog superbowl, add source by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/185
- docs: superbowl blog draft by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/184
- Docs examples sports by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/195
- Add example for sza and [data_color()](reference/GT.data_color.html#great_tables.GT.data_color) by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/136
- Clean up examples in API docs by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/191


### Chores

- Remove unimplemented options from [tab_options()](reference/GT.tab_options.html#great_tables.GT.tab_options) by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/162


## New Contributors

- [<span class="citation" cites="sugatoray">@sugatoray</span>](https://github.com/sugatoray) made their first contribution in https://github.com/posit-dev/great-tables/pull/139
- [<span class="citation" cites="jrycw">@jrycw</span>](https://github.com/jrycw) made their first contribution in https://github.com/posit-dev/great-tables/pull/189

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.2.0…v0.3.0](https://github.com/posit-dev/great-tables/compare/v0.2.0...v0.3.0)


# v0.2.0

*2024-01-24* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.2.0)


## What's Changed

- ci: restore deploy url by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/108
- Fix tab spanner column name by [<span class="citation" cites="atseewal">@atseewal</span>](https://github.com/atseewal) in https://github.com/posit-dev/great-tables/pull/111
- Fix validate frame by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/118
- docs: polars styling blog post by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/113
- Add basic implementation of the [data_color()](reference/GT.data_color.html#great_tables.GT.data_color) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/109
- fix: validate_frame now coerces non string column names by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/127
- Use `to_list()` method as cross-df solution by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/128
- Add guide to [data_color()](reference/GT.data_color.html#great_tables.GT.data_color) and introductory blog post to next version of package by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/131


## New Contributors

- [<span class="citation" cites="atseewal">@atseewal</span>](https://github.com/atseewal) made their first contribution in https://github.com/posit-dev/great-tables/pull/111

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.1.5…v0.2.0](https://github.com/posit-dev/great-tables/compare/v0.1.5...v0.2.0)


# v0.1.5

*2024-01-05* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.5)


## What's Changed

- feat: add the [fmt_datetime()](reference/GT.fmt_datetime.html#great_tables.GT.fmt_datetime) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/101
- feat: generalize row selectors by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/107
  - All `rows=` arguments now can receive a function, that operates on a DataFrame. This makes it easier to select rows in pandas. See the [row selection docs](https://posit-dev.github.io/great-tables/get-started/row-selection.html).
- docs: intro blog post by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/105

**Full Changelog**: [https://github.com/posit-dev/great-tables/compare/v0.1.4…v0.1.5](https://github.com/posit-dev/great-tables/compare/v0.1.4...v0.1.5)


# v0.1.4

*2023-12-19* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.4)


## What's Changed

- docs: single column examples on narrow screens by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/81
- feat: add style.from_column, implement for loc.body by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/83
- fix: cols_hide by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/86
- fix: allow lists of styles and lists of locations by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/87
- docs: get started with styling page by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/88
- Ensure that ID value in compiled CSS is applied to all rules by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/92
- Add interlinks throughout documentation site by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/97


# v0.1.3

*2023-12-12* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.3)

Many small fixes were done in this release, including:

- fix: handle addition in scss template by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/72
- add hyperlinks in table example by [<span class="citation" cites="kmasiello">@kmasiello</span>](https://github.com/kmasiello) in https://github.com/posit-dev/great-tables/pull/70
- Implement the [tab_style()](reference/GT.tab_style.html#great_tables.GT.tab_style) method by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/68
- Ensure that [tab_source_note()](reference/GT.tab_source_note.html#great_tables.GT.tab_source_note) works when using [md()](reference/md.html#great_tables.md) or [html()](reference/html.html#great_tables.html) by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/77
- ci: pre-commit checks by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/78
- Make invocation [loc.body()](reference/loc.body.html#great_tables.loc.body) default to all columns and rows by [<span class="citation" cites="rich-iannone">@rich-iannone</span>](https://github.com/rich-iannone) in https://github.com/posit-dev/great-tables/pull/79


## New Contributors

- [<span class="citation" cites="kmasiello">@kmasiello</span>](https://github.com/kmasiello) made their first contribution in https://github.com/posit-dev/great-tables/pull/70


# v0.1.2

*2023-12-07* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.2)

A few additions were made here:

- **docs**: fix code example in README.md by [<span class="citation" cites="cscheid">@cscheid</span>](https://github.com/cscheid) in https://github.com/posit-dev/great-tables/pull/62
- **feat**: shiny output and renderer for GT by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/59
- **refactor**: replace libsass code with webcolors by [<span class="citation" cites="machow">@machow</span>](https://github.com/machow) in https://github.com/posit-dev/great-tables/pull/61
  - This enables us to use `great_tables` in https://shinylive.io!

Here is an example shiny app:

``` python
from shiny import App, ui

from great_tables import GT, exibble
import great_tables.shiny as gts

app_ui = ui.page_fluid(gts.output_gt("table"))

def server(input, output, session):
    [@output](https://github.com/output)
    [@gts](https://github.com/gts).render_gt
    def table():
        return GT(exibble)

app = App(app_ui, server)
```


# v0.1.1

*2023-12-06* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.1)

- Ensured that column selections exclude columns that are in the stub. (https://github.com/posit-dev/great-tables/pull/49)
- Dataclasses are now frozen. (https://github.com/posit-dev/great-tables/pull/50)
- Added several tests and incorporated `pytest-cov`. (https://github.com/posit-dev/great-tables/pull/53, https://github.com/posit-dev/great-tables/pull/54, https://github.com/posit-dev/great-tables/pull/55)
- Remove datasets from top-level module (except for [exibble](reference/data.exibble.html#great_tables.data.exibble)); added `data` submodule. (https://github.com/posit-dev/great-tables/pull/57)
- Performed several rendering fixes. (https://github.com/posit-dev/great-tables/pull/58)


# v0.1.0

*2023-12-04* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.1.0)

This release rounds out our initial API offering, with:

- structuring of a table with spanners, row groups, and stub labels
- fully fleshed-out formatting methods with locale support
- support for polars and polars selectors (e.g., `cs.starts_with`, etc.)
- addition of the `vals` submodule to enable formatting of values outside of a table context
- a *Get Started* guide on the docs site along with many examples in the API reference


# v0.0.2

*2023-11-10* · [GitHub](https://github.com/posit-dev/great-tables/releases/tag/v0.0.2)

This release contains fairly comprehensive implementations of a top-level [GT](reference/GT.html#great_tables.GT) object, with:

- Reasonably featureful `fmt_()*` methods
- Methods for titles, subtitles, and table notes
- Internal work for implementing spanners, and row and group columns (in a future release).

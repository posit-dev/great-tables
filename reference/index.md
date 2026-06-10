# Reference


## Table Creation


All tables created in Great Tables begin by using `GT()`. With this class, we supply the input data table and some basic options for creating a stub and row groups (with the `rowname_col=` and `groupname_col=` arguments). All GT methods are documented on their own pages.


[GT](GT.md#great_tables.GT)  
Create a **Great Tables** object.


## Major structural table parts


A table can contain a few useful components for conveying additional information. These include a header (with a titles and subtitle), a footer (with source notes), and additional areas for labels (row group labels, column spanner labels, the stubhead label). We can perform styling on targeted table locations with the [`tab_style()`](%60great_tables.GT.tab_style%60) method.


[GT.tab_header()](GT.tab_header.md#great_tables.GT.tab_header)  
Add a table header.

[GT.tab_spanner()](GT.tab_spanner.md#great_tables.GT.tab_spanner)  
Insert a spanner above a selection of column headings.

[GT.tab_spanner_delim()](GT.tab_spanner_delim.md#great_tables.GT.tab_spanner_delim)  
Insert spanners by splitting column names with a delimiter.

[GT.tab_stub()](GT.tab_stub.md#great_tables.GT.tab_stub)  
Add a table stub, to emphasize row and group information.

[GT.tab_stubhead()](GT.tab_stubhead.md#great_tables.GT.tab_stubhead)  
Add label text to the stubhead.

[GT.tab_footnote()](GT.tab_footnote.md#great_tables.GT.tab_footnote)  
Add a table footnote.

[GT.tab_source_note()](GT.tab_source_note.md#great_tables.GT.tab_source_note)  
Add a source note citation.

[GT.tab_style()](GT.tab_style.md#great_tables.GT.tab_style)  
Add custom style to one or more cells

[GT.tab_options()](GT.tab_options.md#great_tables.GT.tab_options)  
Modify the table output options.


## Formatting column data


Columns of data can be formatted with the `fmt_*()` methods. We can specify the rows of these columns quite precisely with the `rows` argument. We get to apply these methods exactly once to each data cell (last call wins). Need to do custom formatting? Use the [`fmt()`](%60great_tables.GT.fmt%60) method and define your own formatter. The `sub_*()` methods allow you to perform substitution operations and `data_color()` provides a lot of power for colorizing body cells based on their data values.


[GT.fmt_number()](GT.fmt_number.md#great_tables.GT.fmt_number)  
Format numeric values.

[GT.fmt_integer()](GT.fmt_integer.md#great_tables.GT.fmt_integer)  
Format values as integers.

[GT.fmt_scientific()](GT.fmt_scientific.md#great_tables.GT.fmt_scientific)  
Format values to scientific notation.

[GT.fmt_engineering()](GT.fmt_engineering.md#great_tables.GT.fmt_engineering)  
Format values to engineering notation.

[GT.fmt_percent()](GT.fmt_percent.md#great_tables.GT.fmt_percent)  
Format values as a percentage.

[GT.fmt_partsper()](GT.fmt_partsper.md#great_tables.GT.fmt_partsper)  
Format values as parts-per quantities.

[GT.fmt_currency()](GT.fmt_currency.md#great_tables.GT.fmt_currency)  
Format values as currencies.

[GT.fmt_roman()](GT.fmt_roman.md#great_tables.GT.fmt_roman)  
Format values as Roman numerals.

[GT.fmt_bytes()](GT.fmt_bytes.md#great_tables.GT.fmt_bytes)  
Format values as bytes.

[GT.fmt_date()](GT.fmt_date.md#great_tables.GT.fmt_date)  
Format values as dates.

[GT.fmt_time()](GT.fmt_time.md#great_tables.GT.fmt_time)  
Format values as times.

[GT.fmt_datetime()](GT.fmt_datetime.md#great_tables.GT.fmt_datetime)  
Format values as datetimes.

[GT.fmt_duration()](GT.fmt_duration.md#great_tables.GT.fmt_duration)  
Format numeric or duration values as styled time duration strings.

[GT.fmt_tf()](GT.fmt_tf.md#great_tables.GT.fmt_tf)  
Format True and False values

[GT.fmt_markdown()](GT.fmt_markdown.md#great_tables.GT.fmt_markdown)  
Format Markdown text.

[GT.fmt_units()](GT.fmt_units.md#great_tables.GT.fmt_units)  
Format measurement units.

[GT.fmt_image()](GT.fmt_image.md#great_tables.GT.fmt_image)  
Format image paths to generate images in cells.

[GT.fmt_flag()](GT.fmt_flag.md#great_tables.GT.fmt_flag)  
Generate flag icons for countries from their country codes.

[GT.fmt_icon()](GT.fmt_icon.md#great_tables.GT.fmt_icon)  
Use icons within a table's body cells.

[GT.fmt_nanoplot()](GT.fmt_nanoplot.md#great_tables.GT.fmt_nanoplot)  
Format data for nanoplot visualizations.

[GT.fmt()](GT.fmt.md#great_tables.GT.fmt)  
Set a column format with a formatter function.

[GT.sub_missing()](GT.sub_missing.md#great_tables.GT.sub_missing)  
Substitute missing values in the table body.

[GT.sub_zero()](GT.sub_zero.md#great_tables.GT.sub_zero)  
Substitute zero values in the table body.

[GT.sub_small_vals()](GT.sub_small_vals.md#great_tables.GT.sub_small_vals)  
Substitute small values in the table body.

[GT.sub_large_vals()](GT.sub_large_vals.md#great_tables.GT.sub_large_vals)  
Substitute large values in the table body.

[GT.sub_values()](GT.sub_values.md#great_tables.GT.sub_values)  
Substitute targeted values in the table body.

[GT.data_color()](GT.data_color.md#great_tables.GT.data_color)  
Perform data cell colorization.


## Text transformation


The text\_\*() method take cell data that are solidified into strings and allow for flexible transformations of those string values. Whereas the `fmt_*()` and `sub_*()` methods are phases 1 and 2 of cell data metamorphoses, the text transformation functions are the final phase, acting on strings generated by formatting and substitution functions with no reference to the source values.


[GT.text_replace()](GT.text_replace.md#great_tables.GT.text_replace)  
Perform targeted text replacement with a regex pattern.

[GT.text_case_when()](GT.text_case_when.md#great_tables.GT.text_case_when)  
Perform text replacements using a case-when approach.

[GT.text_case_match()](GT.text_case_match.md#great_tables.GT.text_case_match)  
Perform text replacements with a switch-like approach.

[GT.text_transform()](GT.text_transform.md#great_tables.GT.text_transform)  
Apply a custom text transformation to cells at specified locations.


## Modifying columns


The `cols_*()` methods allow for modifications that act on entire columns. This includes alignment of the data in columns ([`cols_align()`](%60great_tables.GT.cols_align%60)), hiding columns from view ([`cols_hide()`](%60great_tables.GT.cols_hide%60)), re-labeling the column labels ([`cols_label()`](%60great_tables.GT.cols_label%60)), and moving columns around (with the `cols_move*()` methods).


[GT.cols_align()](GT.cols_align.md#great_tables.GT.cols_align)  
Set the alignment of one or more columns.

[GT.cols_width()](GT.cols_width.md#great_tables.GT.cols_width)  
Set the widths of columns.

[GT.cols_label()](GT.cols_label.md#great_tables.GT.cols_label)  
Relabel one or more columns.

[GT.cols_label_with()](GT.cols_label_with.md#great_tables.GT.cols_label_with)  
Relabel one or more columns using a function.

[GT.cols_label_rotate()](GT.cols_label_rotate.md#great_tables.GT.cols_label_rotate)  
Rotate the column label for one or more columns.

[GT.cols_move()](GT.cols_move.md#great_tables.GT.cols_move)  
Move one or more columns.

[GT.cols_move_to_start()](GT.cols_move_to_start.md#great_tables.GT.cols_move_to_start)  
Move one or more columns to the start.

[GT.cols_move_to_end()](GT.cols_move_to_end.md#great_tables.GT.cols_move_to_end)  
Move one or more columns to the end.

[GT.cols_reorder()](GT.cols_reorder.md#great_tables.GT.cols_reorder)  
Reorder all columns in a specified order.

[GT.cols_hide()](GT.cols_hide.md#great_tables.GT.cols_hide)  
Hide one or more columns.

[GT.cols_unhide()](GT.cols_unhide.md#great_tables.GT.cols_unhide)  
Unhide one or more columns.

[GT.cols_merge()](GT.cols_merge.md#great_tables.GT.cols_merge)  
Merge data from two or more columns into a single column.

[GT.cols_merge_uncert()](GT.cols_merge_uncert.md#great_tables.GT.cols_merge_uncert)  
Merge columns to a value-with-uncertainty column.

[GT.cols_merge_range()](GT.cols_merge_range.md#great_tables.GT.cols_merge_range)  
Merge two columns to a value range column.

[GT.cols_merge_n_pct()](GT.cols_merge_n_pct.md#great_tables.GT.cols_merge_n_pct)  
Merge two columns to combine counts and percentages.


## Adding rows


The [`summary_rows()`](%60great_tables.GT.summary_rows%60) function adds rows to summarize data within each row group, while [`grand_summary_rows()`](%60great_tables.GT.grand_summary_rows%60) summarizes across the entire table.


[GT.summary_rows()](GT.summary_rows.md#great_tables.GT.summary_rows)  
Add group-wise summary rows to the table.

[GT.grand_summary_rows()](GT.grand_summary_rows.md#great_tables.GT.grand_summary_rows)  
Add grand summary rows to the table.


## Location Targeting and Styling Classes


Location targeting is a powerful feature of Great Tables. It allows for the precise selection of table locations for styling (using the `tab_style()` method). The styling classes allow for the specification of the styling properties to be applied to the targeted locations.


[loc.header](loc.header.md#great_tables.loc.header)  
Target the table header (title and subtitle).

[loc.title](loc.title.md#great_tables.loc.title)  
Target the table title.

[loc.subtitle](loc.subtitle.md#great_tables.loc.subtitle)  
Target the table subtitle.

[loc.stubhead](loc.stubhead.md#great_tables.loc.stubhead)  
Target the stubhead.

[loc.column_header](loc.column_header.md#great_tables.loc.column_header)  
Target column spanners and column labels.

[loc.spanner_labels](loc.spanner_labels.md#great_tables.loc.spanner_labels)  
Target spanner labels.

[loc.column_labels](loc.column_labels.md#great_tables.loc.column_labels)  
Target column labels.

[loc.grand_summary_stub](loc.grand_summary_stub.md#great_tables.loc.grand_summary_stub)  
Target the grand summary stub.

[loc.stub](loc.stub.md#great_tables.loc.stub)  
Target the table stub.

[loc.row_groups](loc.row_groups.md#great_tables.loc.row_groups)  
Target row groups.

[loc.grand_summary](loc.grand_summary.md#great_tables.loc.grand_summary)  
Target the data cells in grand summary rows.

[loc.body](loc.body.md#great_tables.loc.body)  
Target data cells in the table body.

[loc.footer](loc.footer.md#great_tables.loc.footer)  
Target the table footer.

[loc.source_notes](loc.source_notes.md#great_tables.loc.source_notes)  
Target the source notes.

[style.fill](style.fill.md#great_tables.style.fill)  
A style specification for the background fill of targeted cells.

[style.text](style.text.md#great_tables.style.text)  
A style specification for cell text.

[style.borders](style.borders.md#great_tables.style.borders)  
A style specification for cell borders.

[style.css](style.css.md#great_tables.style.css)  
A style specification for custom CSS rules.


## Helper Functions


An assortment of helper functions is available in the Great Tables package. The `md()` and `html()` helper functions can be used during label creation with the `tab_header()`, `tab_spanner()`, `tab_stubhead()`, and `tab_source_note()` methods.


[GT.with_id()](GT.with_id.md#great_tables.GT.with_id)  
Set the id for this table.

[GT.with_locale()](GT.with_locale.md#great_tables.GT.with_locale)  
Set a column to be the default locale.

[md()](md.md#great_tables.md)  
Interpret input text as Markdown-formatted text.

[html()](html.md#great_tables.html)  
Interpret input text as HTML-formatted text.

[from_column](from_column.md#great_tables.from_column)  
Specify that a style value should be fetched from a column in the data.

[google_font()](google_font.md#great_tables.google_font)  
Specify a font from the *Google Fonts* service.

[system_fonts()](system_fonts.md#great_tables.system_fonts)  
Get a themed font stack that works well across systems.

[define_units()](define_units.md#great_tables.define_units)  
With `define_units()` you can work with a specially-crafted units notation string and emit the

[nanoplot_options()](nanoplot_options.md#great_tables.nanoplot_options)  
Helper for setting the options for a nanoplot.


## Table options


With the `opt_*()` functions, we have an easy way to set commonly-used table options without having to use `tab_options()` directly.


[GT.opt_stylize()](GT.opt_stylize.md#great_tables.GT.opt_stylize)  
Stylize your table with a colorful look.

[GT.opt_footnote_marks()](GT.opt_footnote_marks.md#great_tables.GT.opt_footnote_marks)  
Option to modify the set of footnote marks.

[GT.opt_row_striping()](GT.opt_row_striping.md#great_tables.GT.opt_row_striping)  
Option to add or remove row striping.

[GT.opt_align_table_header()](GT.opt_align_table_header.md#great_tables.GT.opt_align_table_header)  
Option to align the table header.

[GT.opt_vertical_padding()](GT.opt_vertical_padding.md#great_tables.GT.opt_vertical_padding)  
Option to scale the vertical padding of the table.

[GT.opt_horizontal_padding()](GT.opt_horizontal_padding.md#great_tables.GT.opt_horizontal_padding)  
Option to scale the horizontal padding of the table.

[GT.opt_all_caps()](GT.opt_all_caps.md#great_tables.GT.opt_all_caps)  
Option to use all caps in select table locations.

[GT.opt_table_outline()](GT.opt_table_outline.md#great_tables.GT.opt_table_outline)  
Option to wrap an outline around the entire table.

[GT.opt_table_font()](GT.opt_table_font.md#great_tables.GT.opt_table_font)  
Options to define font choices for the entire table.

[GT.opt_css()](GT.opt_css.md#great_tables.GT.opt_css)  
Option to add custom CSS for the table.


## Export


There may come a day when you need to export a table to some specific format. A great method for that is `gtsave()`, which allows us to save the table as a standalone image file or PDF. You can also get the table code as an HTML fragment with the `*_raw_html()` methods.


[GT.gtsave()](GT.gtsave.md#great_tables.GT.gtsave)  
Save a GT table to a file (PNG, JPEG, WebP, or PDF).

[GT.show()](GT.show.md#great_tables.GT.show)  
Display the table in a notebook or a web browser.

[GT.as_raw_html()](GT.as_raw_html.md#great_tables.GT.as_raw_html)  
Get the HTML content of a GT object.

[GT.write_raw_html()](GT.write_raw_html.md#great_tables.GT.write_raw_html)  
Write the table to an HTML file.

[GT.as_latex()](GT.as_latex.md#great_tables.GT.as_latex)  
Output a GT object as LaTeX


## Pipeline


Sometimes, you might want to programmatically manipulate the table while still benefiting from the chained API that **Great Tables** offers. `pipe()` is designed to tackle this issue.


[GT.pipe()](GT.pipe.md#great_tables.GT.pipe)  
Provide a structured way to chain a function for a GT object.


## Value Formatting Functions


If you have single values (or lists of them) in need of formatting, we have a set of `val_fmt_*()` functions that have been adapted from the corresponding `fmt_*()` methods.


[vals.fmt_number()](vals.fmt_number.md#great_tables.vals.fmt_number)  
Format numeric values.

[vals.fmt_integer()](vals.fmt_integer.md#great_tables.vals.fmt_integer)  
Format values as integers.

[vals.fmt_scientific()](vals.fmt_scientific.md#great_tables.vals.fmt_scientific)  
Format values to scientific notation.

[vals.fmt_engineering()](vals.fmt_engineering.md#great_tables.vals.fmt_engineering)  
Format values to engineering notation.

[vals.fmt_percent()](vals.fmt_percent.md#great_tables.vals.fmt_percent)  
Format values as a percentage.

[vals.fmt_partsper()](vals.fmt_partsper.md#great_tables.vals.fmt_partsper)  
Format values as parts-per quantities.

[vals.fmt_currency()](vals.fmt_currency.md#great_tables.vals.fmt_currency)  
Format values as currencies.

[vals.fmt_roman()](vals.fmt_roman.md#great_tables.vals.fmt_roman)  
Format values as Roman numerals.

[vals.fmt_bytes()](vals.fmt_bytes.md#great_tables.vals.fmt_bytes)  
Format values as bytes.

[vals.fmt_duration()](vals.fmt_duration.md#great_tables.vals.fmt_duration)  
Format values as time duration strings.

[vals.fmt_date()](vals.fmt_date.md#great_tables.vals.fmt_date)  
Format values as dates.

[vals.fmt_time()](vals.fmt_time.md#great_tables.vals.fmt_time)  
Format values as times.

[vals.fmt_duration()](vals.fmt_duration.md#great_tables.vals.fmt_duration)  
Format values as time duration strings.

[vals.fmt_markdown()](vals.fmt_markdown.md#great_tables.vals.fmt_markdown)  
Format Markdown text.

[vals.fmt_image()](vals.fmt_image.md#great_tables.vals.fmt_image)  
Format image paths to generate images in cells.


## Built-in Datasets


The Great Tables package is equipped with sixteen datasets that come in all shapes and sizes. Many examples throughout the help docs use these datasets to quickly demonstrate the features of the package.


[data.countrypops](data.countrypops.md#great_tables.data.countrypops)  
Yearly populations of countries from 1960 to 2022.

[data.sza](data.sza.md#great_tables.data.sza)  
Twice hourly solar zenith angles by month & latitude.

[data.gtcars](data.gtcars.md#great_tables.data.gtcars)  
Deluxe automobiles from the 2014-2017 period.

[data.sp500](data.sp500.md#great_tables.data.sp500)  
Daily S&P 500 Index data from 1950 to 2015.

[data.pizzaplace](data.pizzaplace.md#great_tables.data.pizzaplace)  
A year of pizza sales from a pizza place.

[data.exibble](data.exibble.md#great_tables.data.exibble)  
A toy example table for testing with great_tables: exibble.

[data.towny](data.towny.md#great_tables.data.towny)  
Populations of all municipalities in Ontario from 1996 to 2021.

[data.peeps](data.peeps.md#great_tables.data.peeps)  
A table of personal information for people all over the world.

[data.films](data.films.md#great_tables.data.films)  
Feature films in competition at the Cannes Film Festival.

[data.metro](data.metro.md#great_tables.data.metro)  
The stations of the Paris Metro.

[data.gibraltar](data.gibraltar.md#great_tables.data.gibraltar)  
Weather conditions in Gibraltar, May 2023.

[data.constants](data.constants.md#great_tables.data.constants)  
The fundamental physical constants.

[data.illness](data.illness.md#great_tables.data.illness)  
Lab tests for one suffering from an illness.

[data.reactions](data.reactions.md#great_tables.data.reactions)  
Reaction rates for gas-phase atmospheric reactions of organic compounds.

[data.photolysis](data.photolysis.md#great_tables.data.photolysis)  
Data on photolysis rates for gas-phase organic compounds.

[data.nuclides](data.nuclides.md#great_tables.data.nuclides)  
Nuclide data.

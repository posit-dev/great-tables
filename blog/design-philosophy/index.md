# The Design Philosophy of Great Tables

We've spent a lot of time thinking about tables. Tables--like plots--are crucial as a last step toward presenting information. There is surprising sophistication and nuance in designing effective tables. Over the past 5,000 years, they've evolved from simple grids to highly structured displays of data. Although we argue that the mid-1900s served as a high point, the popularization and wider accessibility of computing seemingly brought us back to the simple, ancient times.

Okay, it's not all *that bad* but the workers of data are today confronted with an all-too-familiar dilemma: copy your data into a tool like Excel to make the table, or, display an otherwise unpolished table. Through the exploration of the qualities that make tables shine, the backstory of tables as a display of data, and the issues faced today, it's clear how we can solve the **great table dilemma** with [**Great Tables**](https://github.com/posit-dev/great-tables).

<img src="./computer_tables.png" class="img-fluid" />

Tables made with computers (left to right): (1) a DataFrame printed at the console, (2) an Excel table, and (3) a **Great Tables** table.


## What is a table, really?

Before getting to what makes tables *shine* we should first define what a table is. This is surprisingly hard! But I believe it can be boiled down to two basic rules:

- the data is represented as columns and rows
- the data is primarily text

Let's look at an example of a simple table with actual data to tie this theory to practice.


| Name | Address | City | Postcode | DOB | Height | Weight |
|----|----|----|----|----|----|----|
| Dustin B. Roach | 1183 Columbia Road | Holly Oak, DE | 19809 | 1970-09-16 | 5' 9" | 202.5 |
| Iwona Adamczyk | ul. Zabłudowska 133 | Warszawa | 04-788 | 1976-01-03 | 5' 5" | 123.7 |
| Geneviève Massé | 1415 rue Principale | Amos, QC | J9T 1E4 | 1967-12-08 | 5' 3" | 136.3 |
| João Souza Lima | Rua Cosmorama, 538 | São Paulo-SP | 04648-080 | 2001-04-21 | 6' 2" | 231.0 |
| Maddison McCabe | 149 Raymond Street | Strathern | Invercargill 9812 | 1982-03-05 | 5' 8" | 146.1 |


A table of named individuals along with a select set of characteristics.

This table arranges records containing personal characteristics as columns and rows. Each person is a row, and each characteristic makes up a different column. The characteristics use different types of data, like dates, numbers, and text. This arrangement makes it easy to look up individual values or make comparisons across the different rows or columns.

Note that there are horizontal lines separating the rows. This aesthetic touch, while not strictly required for a table, serves as a visual reinforcement for separating the individual rows.

The order of the columns matters, and that we start with the `Name` column here is no accident. If that column were the last (i.e., furthest to the right), it would be slightly more confusing for the reader since the subject for the record isn't immediate. In addition to order, column labels play an important role for indicating what data is in each column. They're not always necessary but in most cases they remove the guesswork for what type of data is contained within each column.

We'll go into some detail later about how [**Great Tables**](https://github.com/posit-dev/great-tables) provides affordances for structuring information for better legibility and how the package can be used to adorn the table with other structural elements. For now, our conception of a table can be summarized in this schematic.

<img src="./a_simple_table.png" class="img-fluid" />

A simple table has: (1) cells containing data, (2) an arrangement of columns and rows, and (3) column labels to describe the type data in each column.

Now, let's go back: way back. In examining where tables came from, we might better understand the great story of tables.


## The early history of tables

Tables emerged from square grids. When grids are made like this, you invariably generate containers that may hold some sort of information. The earliest known examples of grids go very far back in human history. Twenty-five thousand year old representations of the grid are found on the walls of the Lascaux and Niaux caves in France[^1].

<img src="./cave_grids.png" class="img-fluid" />

Reproductions of early grids found on cave walls.

In the second century BC, the Greek astronomer Hipparchus used latitude and longitude to locate celestial and terrestrial positions[^2]. At around AD 150, Ptolmey published *Geographia*, which contains 25 geographical maps accompanied by methodologies for their construction using grids[^3]. The Romans employed a grid system called *centuriation*, which can be described as land measurement (using surveyors' instruments) to realize the formation of square grids using roads, canals, or agricultural plots[^4].

When agriculture became more widespread (ca. 10,000 years ago), there was the need to document and manage economic transactions to do with farming, livestock, and the division of labor. In the fourth millennium BC, Mesopotamian cities that traded with far way kingdoms needed to keep such records. Clay tablets recovered from the ancient Sumerian city of Uruk show early yet sophisticated tables. Here is a drawing of one of the recovered tablets, which contains an accounting of deliveries of barley and malt from two individuals for the production of beer[^5].

<img src="./uruk_tablet_with_annotations.png" class="img-fluid" />

Drawing of clay tablet from Sumerian city of Uruk, circa 3200-3000 BC. Uruk III Tablet (MSVO 3, 51, Louvre Museum, Paris, France). Annotated with the meanings of the columns, rows, and cells.

Note that the recovered tablet is meant to be read from right to left. Inside each box is an ideogram (a symbol that represented a word or idea) and a numerical value representing a quantity.

Its structure is where things get super interesting:

- Rows: there are roughly two rows, each corresponding to an individual.
- Columns: the first two columns from the right contain counts of malt (rightmost column) and barley (second rightmost column).
- Subtotals: the third column from the right sums barley and malt within each individual, and the left-most column displays the grand total.

As a bonus, the table has a footer, since the bottom row contains the name of the official in charge.

Zooming ahead about a thousand years, you start to see more systematically structured tables. Here's a photo of a cuneiform tablet that was originally from Mesopotamia (from the Temple of Enlil at Nippur, ca. 1850 BC)[^6], containing sources of revenue and monthly disbursements for 50 temple personnel.

<img src="./nippur_cuneiform_tablet.png" class="img-fluid" />

Cuneiform tablet, temple of Enlil at Nippur, (CBS 3323, University of Pennsylvania).

You can see right away that there is a more regular grid and, if you probe deeper, there are more similarities than differerences with the tables of today. While difficult to pick them out, the following table elements are present[^7]:

- column headings (month names) and row titles (names/professions of individuals).
- cells with no information (look at the blank or smooth cells along rows)
- numerical values in the cells
- subtotals for each individual every six months
- grand totals
- annotations with explanatory notes

Later on, tables were less inscribed on clay and more on wax tablets, papyrus, and paper. The media have changed, writing technologies have changed, and the design and presentation of tables also went through changes.


## Midcentury modern tables

Perhaps the best period for tables was around the middle of the 20th century. Technologies for table (and surrounding document) preparation included the offset printer, the typewriter, and varitype[^8] (my favorite). The technologies were sufficiently advanced as to allow the precise typesetting of table elements. While of course constrained by the limited space available on pages, tabular design at this point had many workable solutions for fitting tables into single pages or dispersing the tabular content across multiple pages. The combination of advanced printing technology with advanced knowledge of tabular design resulted in *beautiful tables*.

There's no greater embodiment of that pairing of technology and design than the [*Manual of Tabular Presentation*](https://www2.census.gov/library/publications/1949/general/tabular-presentation.pdf)[^9], written and published by the United States Bureau of the Census. It is truly a remarkable work which goes into great detail on how the department imagines the ideal designs of information-rich tables. The work articulates the different parts of a table (and each part is given a descriptive name), sparing no detail when describing those different table parts in rigorous detail. Throughout its hundreds of pages, the authors make strong recommendations on what to do (and what *not* to do) for many tabulation scenarios. When poring over the tables visually depicted in the book, you can't help but see that tables can both look really good *and* contain a density of information. The promise and the result is a balance of form and function.

We at [**Great Tables**](https://github.com/posit-dev/great-tables) borrow liberally from this work because many of its tabular design principles are just as good now as they were back then (and we'll talk about what we took from that work in the next section). We'll end this brief section with a visual montage of snippets from the *Census Manual*, which provides a glimpse of the sound advice on offer.

<img src="./snippets_from_manual_tablular_presentation.png" class="img-fluid" />

Little nuggets of wisdom from the *Census Manual*. This may very well be the ultimate book on tabular design.


## The late history of tables

With computing technologies becoming more accessible by the 1970s and 1980s, people were able to generate tables in both electronic and print form. The democratization of computational tables arguably began with VisiCalc in 1979, a massive success that initiated the computing category of spreadsheeting software. There's an undeniable advantage to having data analyzed and transformed in computing environments, but, this comes at a cost. This is what it looked like:

<img src="./visicalc.png" class="img-fluid" />

This is a table in VisiCalc (earliest example of a table in a spreadsheet application). It's pretty crude compared to the tables in print but the advantage here is that you can calculate values quickly.

The grid cells couldn't be styled with borders for presentation purposes, the values couldn't be formatted, and the tables couldn't even be printed. I mean, [try it out](https://www.pcjs.org/software/pcx86/app/other/visicalc/1981/) and you'll see that this is quite limited in more than a few ways.

Over time, and this took about 10-15 years, tables-within-spreadsheets got a little easier on the eyes. By the early 1990s, Excel could paint borders on your tables, better typographical support was available, and the formatting of values was fully-featured (though, [wonky](https://www.cnet.com/tech/computing/prevent-excel-from-reformatting-two-numbers-to-a-date-and-month/)). Great! Problem solved, right? Not really.

While Excel tables from the last three decades looked much better than 1980s-spreadsheet-borne tables, they could never hold a candle to what was shown in the *Census Manual* (no matter how much of an Excel expert you became). Further to this, data analysis started to became a thing accomplished outside of Excel. One example of that is Python and its use inside Jupyter notebooks. We now have a bag of problematic scenarios

- all Python: analyze data and generate tables all in Python (bad tables)
- all Excel: analyze data and make tables in Excel (less flexible analysis)
- split-brained: analyze data in Python, copy over to Excel to make tables (not reproducible)

All of these are suboptimal solutions. We propose that it is far better to do everything in Python: the data ingestion, the data analysis, and the data visualization. The visualization step is what's done for plots and other types of graphics composed from data, it shouldn't be any different when it comes to generating summary tables.


## Approach to tables taken by **Great Tables**

[**Great Tables**](https://github.com/posit-dev/great-tables) restores the elegance of midcentury tables with the power of a coding interface. With [**Great Tables**](https://github.com/posit-dev/great-tables) anyone can make beautiful tables in Python. Our framework expresses a table as a combination of six independent components. With this framework, you can structure the table, format the values, and style the table. We firmly believe that the methods offered in the package enable people to construct a wide variety of useful tables that work across many disciplines.

You build with [**Great Tables**](https://github.com/posit-dev/great-tables) iteratively, starting off with your table body from code, adding styling, formatting and other components. Here is a schematic that outlines our terminology and depicts how the different table components are related to each other:

<img src="./composition_of_a_table_in_GT.png" class="img-fluid" />

A schematic with the complete set of table components that can be utilized in **Great Tables**.

Note the following six component pieces:

- **Table Header**: a place for a title and subtitle, where you can succinctly describe the table content
- **Column Labels**: the column labels define the content of each column, and spanners are headings over groups of columns
- **Stub Head**: the 'top-left' location, where a label could be used in a variety of ways
- **Row Stub**: for row information, including row grouping labels
- **Table Body**: contains cells and so it's where the data lives
- **Table Footer**: a place for additional information pertaining to the table content

Here's a table that takes advantage of the different components available in [**Great Tables**](https://github.com/posit-dev/great-tables). It contains the names and addresses of people.


Show the code

``` python
from great_tables import GT, md, system_fonts

(
    GT(simple_table, rowname_col="Name")
    .tab_header(title="Names, Addresses, and Characteristics of Remote Correspondents")
    .tab_stubhead(label=md("*Name*"))
    .tab_spanner(label="Location", columns=["Address", "City", "Postcode"])
    .tab_spanner(label="Personal Characteristics", columns=["DOB", "Height", "Weight"])
    .tab_source_note(source_note=md("**Data last updated**: December 18, 2022."))
    .fmt_date(columns="DOB", date_style="m_day_year")
    .fmt_integer(columns="Weight", pattern="{x} lbs")
    .opt_stylize()
    .opt_align_table_header(align="left")
    .opt_vertical_padding(scale=0.75)
    .tab_options(
        table_font_names=system_fonts(name="rounded-sans"),
        table_font_size="14px",
    )
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal">Names, Addresses, and Characteristics of Remote Correspondents</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="<em>Name</em>" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"><em>Name</em></th>
<th colspan="3" id="Location" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Location</th>
<th colspan="3" id="Personal-Characteristics" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Personal Characteristics</th>
</tr>
<tr class="gt_col_headings">
<th id="Address" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Address</th>
<th id="City" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">City</th>
<th id="Postcode" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Postcode</th>
<th id="DOB" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">DOB</th>
<th id="Height" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Height</th>
<th id="Weight" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Weight</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">Dustin B. Roach</th>
<td class="gt_row gt_left">1183 Columbia Road</td>
<td class="gt_row gt_left">Holly Oak, DE</td>
<td class="gt_row gt_left">19809</td>
<td class="gt_row gt_left">Sep 16, 1970</td>
<td class="gt_row gt_left">5' 9"</td>
<td class="gt_row gt_right">202 lbs</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Iwona Adamczyk</th>
<td class="gt_row gt_left gt_striped">ul. Zabłudowska 133</td>
<td class="gt_row gt_left gt_striped">Warszawa</td>
<td class="gt_row gt_left gt_striped">04-788</td>
<td class="gt_row gt_left gt_striped">Jan 3, 1976</td>
<td class="gt_row gt_left gt_striped">5' 5"</td>
<td class="gt_row gt_right gt_striped">124 lbs</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Geneviève Massé</th>
<td class="gt_row gt_left">1415 rue Principale</td>
<td class="gt_row gt_left">Amos, QC</td>
<td class="gt_row gt_left">J9T 1E4</td>
<td class="gt_row gt_left">Dec 8, 1967</td>
<td class="gt_row gt_left">5' 3"</td>
<td class="gt_row gt_right">136 lbs</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">João Souza Lima</th>
<td class="gt_row gt_left gt_striped">Rua Cosmorama, 538</td>
<td class="gt_row gt_left gt_striped">São Paulo-SP</td>
<td class="gt_row gt_left gt_striped">04648-080</td>
<td class="gt_row gt_left gt_striped">Apr 21, 2001</td>
<td class="gt_row gt_left gt_striped">6' 2"</td>
<td class="gt_row gt_right gt_striped">231 lbs</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Maddison McCabe</th>
<td class="gt_row gt_left">149 Raymond Street</td>
<td class="gt_row gt_left">Strathern</td>
<td class="gt_row gt_left">Invercargill 9812</td>
<td class="gt_row gt_left">Mar 5, 1982</td>
<td class="gt_row gt_left">5' 8"</td>
<td class="gt_row gt_right">146 lbs</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="7" class="gt_sourcenote"><strong>Data last updated</strong>: December 18, 2022.</td>
</tr>
</tfoot>

</table>


A table of named individuals redone, **Great Tables** style!

Notice that there is a blue row stub component that makes the row labels distinct from the body of the table. This is important because each person described forms a unique observation and we want to highlight the subject of each row. The heading provides context on what's contained within the table. The two column spanners arrange the columns into sensible groupings (e.g., 'Location'). The consistent use of blue lines and cell backgrounds gives the table a professional look.

If you look at the table code above you'll see that every method for modifying the table starts with `tab_`. These particular methods are concerned with adding a table component (e.g., [tab_header()](../../reference/GT.tab_header.md#great_tables.GT.tab_header) creates a **Table Header**) and they're designed to be easy and straightforward to use.


### Formatting

Table structuring is important, but not the only thing. Tables in different disciplines have a certain set of display requirements specific for any values shown. Even something as simple as a number can be formatted in many different ways depending on a community's norms and expectations. This extends to a very wide area when we consider that dates, times, and currencies also need to be formatted.

Depending on your display requirements, a raw value like 134,000 could presented as:

- scientific notation ([fmt_scientific()](../../reference/GT.fmt_scientific.md#great_tables.GT.fmt_scientific)): 1.34 × 10<sup>5</sup>
- a number in the German locale ([fmt_number()](../../reference/GT.fmt_number.md#great_tables.GT.fmt_number)): 134.000,00
- a compact integer value ([fmt_integer()](../../reference/GT.fmt_integer.md#great_tables.GT.fmt_integer)): 134K

The problem grows worse when values need to be conveyed as images or plots. If you're a medical analyst, for example, you might need to effectively convey whether test results for a patient are improving or worsening over time. Reading such data as a sequence of numbers across a row can slow interpretation. But by using *nanoplots*, available as the [fmt_nanoplot()](../../reference/GT.fmt_nanoplot.md#great_tables.GT.fmt_nanoplot) formatting method, readers can spot trends right away. Here's an example that provides test results over a series of days.


Show the code

``` python
from great_tables import GT, md
from great_tables.data import illness
import polars as pl
from polars import selectors as cs

illness_mini = (
    pl.from_pandas(illness)
    .head(10)
    .select(
        "test", values=pl.concat_str(cs.starts_with("day"), separator=" ", ignore_nulls=True)
    )
    .slice(1, 9)
)

(
    GT(illness_mini, rowname_col="test")
    .fmt_nanoplot(columns="values")
    .tab_header(md("Partial summary of daily tests<br>performed on YF patient"))
    .tab_stubhead(label=md("**Test**"))
    .cols_label(values=md("*Progression*"))
    .cols_align(align="center", columns="values")
    .tab_source_note(source_note="Measurements from Day 3 through Day 9.")
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="gt_heading">
<th colspan="2" class="gt_heading gt_title gt_font_normal">Partial summary of daily tests<br />
performed on YF patient</th>
</tr>
<tr class="gt_col_headings">
<th id="<strong>Test</strong>" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"><strong>Test</strong></th>
<th id="values" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col"><em>Progression</em></th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">WBC</th>
<td class="gt_row gt_center"><div>
<img src="data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdib3g9IjAgMCA0NTAgMTMwIiBzdHlsZT0iaGVpZ2h0OiAyZW07IG1hcmdpbi1sZWZ0OiBhdXRvOyBtYXJnaW4tcmlnaHQ6IGF1dG87IGZvbnQtc2l6ZTogaW5oZXJpdDsgb3ZlcmZsb3c6IHZpc2libGU7IHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7IHBvc2l0aW9uOnJlbGF0aXZlOyI+PGRlZnM+PHBhdHRlcm4gaWQ9ImFyZWFfcGF0dGVybiIgd2lkdGg9IjgiIGhlaWdodD0iOCIgcGF0dGVybnVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggY2xhc3M9InBhdHRlcm4tbGluZSIgZD0iTSAwLDggbCA4LC04IE0gLTEsMSBsIDQsLTQgTSA2LDEwIGwgNCwtNCIgc3Ryb2tlPSIjRkYwMDAwIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiIgLz48L3BhdHRlcm4+PC9kZWZzPjxzdHlsZT4gdGV4dCB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsICdDYXNjYWRpYSBDb2RlJywgJ1NvdXJjZSBDb2RlIFBybycsIE1lbmxvLCBDb25zb2xhcywgJ0RlamFWdSBTYW5zIE1vbm8nLCBtb25vc3BhY2U7IHN0cm9rZS13aWR0aDogMC4xNWVtOyBwYWludC1vcmRlcjogc3Ryb2tlOyBzdHJva2UtbGluZWpvaW46IHJvdW5kOyBjdXJzb3I6IGRlZmF1bHQ7IH0gLnZlcnQtbGluZTpob3ZlciByZWN0IHsgZmlsbDogIzkxMUVCNDsgZmlsbC1vcGFjaXR5OiA0MCU7IHN0cm9rZTogI0ZGRkZGRjYwOyBjb2xvcjogcmVkOyB9IC52ZXJ0LWxpbmU6aG92ZXIgdGV4dCB7IHN0cm9rZTogd2hpdGU7IGZpbGw6ICMyMTI0Mjc7IH0gLmhvcml6b250YWwtbGluZTpob3ZlciB0ZXh0IHtzdHJva2U6IHdoaXRlOyBmaWxsOiAjMjEyNDI3OyB9IC5yZWYtbGluZTpob3ZlciByZWN0IHsgc3Ryb2tlOiAjRkZGRkZGNjA7IH0gLnJlZi1saW5lOmhvdmVyIGxpbmUgeyBzdHJva2U6ICNGRjAwMDA7IH0gLnJlZi1saW5lOmhvdmVyIHRleHQgeyBzdHJva2U6IHdoaXRlOyBmaWxsOiAjMjEyNDI3OyB9IC55LWF4aXMtbGluZTpob3ZlciByZWN0IHsgZmlsbDogI0VERURFRDsgZmlsbC1vcGFjaXR5OiA2MCU7IHN0cm9rZTogI0ZGRkZGRjYwOyBjb2xvcjogcmVkOyB9IC55LWF4aXMtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgc3Ryb2tlLXdpZHRoOiAwLjIwZW07IGZpbGw6ICMxQTFDMUY7IH0gPC9zdHlsZT48cGF0aCBjbGFzcz0iYXJlYS1jbG9zZWQiIGQ9Ik0gNTAuMCwxMTEuMTUzODQ2MTUzODQ2MTYgMTA4LjMzMzMzMzMzMzMzMzMzLDExNS4wIDE2Ni42NjY2NjY2NjY2NjY2Niw5My4yMzA3NjkyMzA3NjkyNCAyMjUuMCw5MS4wMzg0NjE1Mzg0NjE1NSAyODMuMzMzMzMzMzMzMzMzMywzNi4xMTUzODQ2MTUzODQ2MyAzNDEuNjY2NjY2NjY2NjY2NywxNS4wIDQwMC4wLDU4LjE5MjMwNzY5MjMwNzY4NiA0MDAuMCwxMjUgNTAuMCwxMjUgWiIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJ1cmwoI2FyZWFfcGF0dGVybikiIGZpbGwtb3BhY2l0eT0iMC43IiAvPjxwYXRoIGQ9Ik0gNTAuMCwxMTEuMTUzODQ2MTUzODQ2MTYgQyA3NS4wLDExMS4xNTM4NDYxNTM4NDYxNiA4My4zMzMzMzMzMzMzMzMzMywxMTUuMCAxMDguMzMzMzMzMzMzMzMzMzMsMTE1LjAgQyAxMzMuMzMzMzMzMzMzMzMzMzEsMTE1LjAgMTQxLjY2NjY2NjY2NjY2NjY2LDkzLjIzMDc2OTIzMDc2OTI0IDE2Ni42NjY2NjY2NjY2NjY2Niw5My4yMzA3NjkyMzA3NjkyNCBDIDE5MS42NjY2NjY2NjY2NjY2Niw5My4yMzA3NjkyMzA3NjkyNCAyMDAuMCw5MS4wMzg0NjE1Mzg0NjE1NSAyMjUuMCw5MS4wMzg0NjE1Mzg0NjE1NSBDIDI1MC4wLDkxLjAzODQ2MTUzODQ2MTU1IDI1OC4zMzMzMzMzMzMzMzMzLDM2LjExNTM4NDYxNTM4NDYzIDI4My4zMzMzMzMzMzMzMzMzLDM2LjExNTM4NDYxNTM4NDYzIEMgMzA4LjMzMzMzMzMzMzMzMzMsMzYuMTE1Mzg0NjE1Mzg0NjMgMzE2LjY2NjY2NjY2NjY2NjcsMTUuMCAzNDEuNjY2NjY2NjY2NjY2NywxNS4wIEMgMzY2LjY2NjY2NjY2NjY2NjcsMTUuMCAzNzUuMCw1OC4xOTIzMDc2OTIzMDc2ODYgNDAwLjAsNTguMTkyMzA3NjkyMzA3Njg2IiBzdHJva2U9IiM0NjgyQjQiIHN0cm9rZS13aWR0aD0iOCIgZmlsbD0ibm9uZSIgLz48Y2lyY2xlIGN4PSI1MC4wIiBjeT0iMTExLjE1Mzg0NjE1Mzg0NjE2IiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjEwOC4zMzMzMzMzMzMzMzMzMyIgY3k9IjExNS4wIiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjE2Ni42NjY2NjY2NjY2NjY2NiIgY3k9IjkzLjIzMDc2OTIzMDc2OTI0IiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjIyNS4wIiBjeT0iOTEuMDM4NDYxNTM4NDYxNTUiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMjgzLjMzMzMzMzMzMzMzMzMiIGN5PSIzNi4xMTUzODQ2MTUzODQ2MyIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIzNDEuNjY2NjY2NjY2NjY2NyIgY3k9IjE1LjAiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iNDAwLjAiIGN5PSI1OC4xOTIzMDc2OTIzMDc2ODYiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGcgY2xhc3M9InktYXhpcy1saW5lIj48cmVjdCB4PSIwIiB5PSIwIiB3aWR0aD0iNjUiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjAiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjAiIHk9IjE5LjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjI1Ij4zMC4zPC90ZXh0Pjx0ZXh0IHg9IjAiIHk9IjEyNi4wIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIyNSI+NC4yNjwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iNDAuMCIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iNjAuMCIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjUuMjY8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9Ijk4LjMzMzMzMzMzMzMzMzMzIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIxMTguMzMzMzMzMzMzMzMzMzMiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij40LjI2PC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIxNTYuNjY2NjY2NjY2NjY2NjYiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjE3Ni42NjY2NjY2NjY2NjY2NiIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjkuOTI8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjIxNS4wIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIyMzUuMCIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjEwLjU8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjI3My4zMzMzMzMzMzMzMzMzIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIyOTMuMzMzMzMzMzMzMzMzMyIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjI0Ljg8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjMzMS42NjY2NjY2NjY2NjY3IiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIzNTEuNjY2NjY2NjY2NjY2NyIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjMwLjM8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjM5MC4wIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSI0MTAuMCIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjE5LjA8L3RleHQ+PC9nPjwvc3ZnPg==" />
</div></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Neutrophils</th>
<td class="gt_row gt_center"><div>
<img src="data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdib3g9IjAgMCA0NTAgMTMwIiBzdHlsZT0iaGVpZ2h0OiAyZW07IG1hcmdpbi1sZWZ0OiBhdXRvOyBtYXJnaW4tcmlnaHQ6IGF1dG87IGZvbnQtc2l6ZTogaW5oZXJpdDsgb3ZlcmZsb3c6IHZpc2libGU7IHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7IHBvc2l0aW9uOnJlbGF0aXZlOyI+PGRlZnM+PHBhdHRlcm4gaWQ9ImFyZWFfcGF0dGVybiIgd2lkdGg9IjgiIGhlaWdodD0iOCIgcGF0dGVybnVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggY2xhc3M9InBhdHRlcm4tbGluZSIgZD0iTSAwLDggbCA4LC04IE0gLTEsMSBsIDQsLTQgTSA2LDEwIGwgNCwtNCIgc3Ryb2tlPSIjRkYwMDAwIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiIgLz48L3BhdHRlcm4+PC9kZWZzPjxzdHlsZT4gdGV4dCB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsICdDYXNjYWRpYSBDb2RlJywgJ1NvdXJjZSBDb2RlIFBybycsIE1lbmxvLCBDb25zb2xhcywgJ0RlamFWdSBTYW5zIE1vbm8nLCBtb25vc3BhY2U7IHN0cm9rZS13aWR0aDogMC4xNWVtOyBwYWludC1vcmRlcjogc3Ryb2tlOyBzdHJva2UtbGluZWpvaW46IHJvdW5kOyBjdXJzb3I6IGRlZmF1bHQ7IH0gLnZlcnQtbGluZTpob3ZlciByZWN0IHsgZmlsbDogIzkxMUVCNDsgZmlsbC1vcGFjaXR5OiA0MCU7IHN0cm9rZTogI0ZGRkZGRjYwOyBjb2xvcjogcmVkOyB9IC52ZXJ0LWxpbmU6aG92ZXIgdGV4dCB7IHN0cm9rZTogd2hpdGU7IGZpbGw6ICMyMTI0Mjc7IH0gLmhvcml6b250YWwtbGluZTpob3ZlciB0ZXh0IHtzdHJva2U6IHdoaXRlOyBmaWxsOiAjMjEyNDI3OyB9IC5yZWYtbGluZTpob3ZlciByZWN0IHsgc3Ryb2tlOiAjRkZGRkZGNjA7IH0gLnJlZi1saW5lOmhvdmVyIGxpbmUgeyBzdHJva2U6ICNGRjAwMDA7IH0gLnJlZi1saW5lOmhvdmVyIHRleHQgeyBzdHJva2U6IHdoaXRlOyBmaWxsOiAjMjEyNDI3OyB9IC55LWF4aXMtbGluZTpob3ZlciByZWN0IHsgZmlsbDogI0VERURFRDsgZmlsbC1vcGFjaXR5OiA2MCU7IHN0cm9rZTogI0ZGRkZGRjYwOyBjb2xvcjogcmVkOyB9IC55LWF4aXMtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgc3Ryb2tlLXdpZHRoOiAwLjIwZW07IGZpbGw6ICMxQTFDMUY7IH0gPC9zdHlsZT48cGF0aCBjbGFzcz0iYXJlYS1jbG9zZWQiIGQ9Ik0gNTAuMCwxMTQuMzMxODQ4NTUyMzM4NTMgMTA4LjMzMzMzMzMzMzMzMzMzLDExNS4wIDE2Ni42NjY2NjY2NjY2NjY2NiwxMDAuNzQ2MTAyNDQ5ODg4NjQgMjI1LjAsNTQuOTEwOTEzMTQwMzExOCAyODMuMzMzMzMzMzMzMzMzMywzNy42NzI2MDU3OTA2NDU4OTYgMzQxLjY2NjY2NjY2NjY2NjcsMTUuMCA0MDAuMCw2Mi4xMjY5NDg3NzUwNTU2OCA0MDAuMCwxMjUgNTAuMCwxMjUgWiIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJ1cmwoI2FyZWFfcGF0dGVybikiIGZpbGwtb3BhY2l0eT0iMC43IiAvPjxwYXRoIGQ9Ik0gNTAuMCwxMTQuMzMxODQ4NTUyMzM4NTMgQyA3NS4wLDExNC4zMzE4NDg1NTIzMzg1MyA4My4zMzMzMzMzMzMzMzMzMywxMTUuMCAxMDguMzMzMzMzMzMzMzMzMzMsMTE1LjAgQyAxMzMuMzMzMzMzMzMzMzMzMzEsMTE1LjAgMTQxLjY2NjY2NjY2NjY2NjY2LDEwMC43NDYxMDI0NDk4ODg2NCAxNjYuNjY2NjY2NjY2NjY2NjYsMTAwLjc0NjEwMjQ0OTg4ODY0IEMgMTkxLjY2NjY2NjY2NjY2NjY2LDEwMC43NDYxMDI0NDk4ODg2NCAyMDAuMCw1NC45MTA5MTMxNDAzMTE4IDIyNS4wLDU0LjkxMDkxMzE0MDMxMTggQyAyNTAuMCw1NC45MTA5MTMxNDAzMTE4IDI1OC4zMzMzMzMzMzMzMzMzLDM3LjY3MjYwNTc5MDY0NTg5NiAyODMuMzMzMzMzMzMzMzMzMywzNy42NzI2MDU3OTA2NDU4OTYgQyAzMDguMzMzMzMzMzMzMzMzMywzNy42NzI2MDU3OTA2NDU4OTYgMzE2LjY2NjY2NjY2NjY2NjcsMTUuMCAzNDEuNjY2NjY2NjY2NjY2NywxNS4wIEMgMzY2LjY2NjY2NjY2NjY2NjcsMTUuMCAzNzUuMCw2Mi4xMjY5NDg3NzUwNTU2OCA0MDAuMCw2Mi4xMjY5NDg3NzUwNTU2OCIgc3Ryb2tlPSIjNDY4MkI0IiBzdHJva2Utd2lkdGg9IjgiIGZpbGw9Im5vbmUiIC8+PGNpcmNsZSBjeD0iNTAuMCIgY3k9IjExNC4zMzE4NDg1NTIzMzg1MyIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIxMDguMzMzMzMzMzMzMzMzMzMiIGN5PSIxMTUuMCIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIxNjYuNjY2NjY2NjY2NjY2NjYiIGN5PSIxMDAuNzQ2MTAyNDQ5ODg4NjQiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMjI1LjAiIGN5PSI1NC45MTA5MTMxNDAzMTE4IiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjI4My4zMzMzMzMzMzMzMzMzIiBjeT0iMzcuNjcyNjA1NzkwNjQ1ODk2IiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjM0MS42NjY2NjY2NjY2NjY3IiBjeT0iMTUuMCIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSI0MDAuMCIgY3k9IjYyLjEyNjk0ODc3NTA1NTY4IiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxnIGNsYXNzPSJ5LWF4aXMtbGluZSI+PHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjY1IiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIwIiB5PSIxOS4wIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIyNSI+MjcuMjwvdGV4dD48dGV4dCB4PSIwIiB5PSIxMjYuMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMjUiPjQuNzI8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjQwLjAiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjYwLjAiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij40Ljg3PC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSI5OC4zMzMzMzMzMzMzMzMzMyIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMTE4LjMzMzMzMzMzMzMzMzMzIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+NC43MjwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMTU2LjY2NjY2NjY2NjY2NjY2IiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIxNzYuNjY2NjY2NjY2NjY2NjYiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij43LjkyPC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIyMTUuMCIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMjM1LjAiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij4xOC4yPC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIyNzMuMzMzMzMzMzMzMzMzMyIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMjkzLjMzMzMzMzMzMzMzMzMiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij4yMi4xPC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIzMzEuNjY2NjY2NjY2NjY2NyIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMzUxLjY2NjY2NjY2NjY2NjciIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij4yNy4yPC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIzOTAuMCIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iNDEwLjAiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij4xNi42PC90ZXh0PjwvZz48L3N2Zz4=" />
</div></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">RBC</th>
<td class="gt_row gt_center"><div>
<img src="data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdib3g9IjAgMCA0NTAgMTMwIiBzdHlsZT0iaGVpZ2h0OiAyZW07IG1hcmdpbi1sZWZ0OiBhdXRvOyBtYXJnaW4tcmlnaHQ6IGF1dG87IGZvbnQtc2l6ZTogaW5oZXJpdDsgb3ZlcmZsb3c6IHZpc2libGU7IHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7IHBvc2l0aW9uOnJlbGF0aXZlOyI+PGRlZnM+PHBhdHRlcm4gaWQ9ImFyZWFfcGF0dGVybiIgd2lkdGg9IjgiIGhlaWdodD0iOCIgcGF0dGVybnVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggY2xhc3M9InBhdHRlcm4tbGluZSIgZD0iTSAwLDggbCA4LC04IE0gLTEsMSBsIDQsLTQgTSA2LDEwIGwgNCwtNCIgc3Ryb2tlPSIjRkYwMDAwIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiIgLz48L3BhdHRlcm4+PC9kZWZzPjxzdHlsZT4gdGV4dCB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsICdDYXNjYWRpYSBDb2RlJywgJ1NvdXJjZSBDb2RlIFBybycsIE1lbmxvLCBDb25zb2xhcywgJ0RlamFWdSBTYW5zIE1vbm8nLCBtb25vc3BhY2U7IHN0cm9rZS13aWR0aDogMC4xNWVtOyBwYWludC1vcmRlcjogc3Ryb2tlOyBzdHJva2UtbGluZWpvaW46IHJvdW5kOyBjdXJzb3I6IGRlZmF1bHQ7IH0gLnZlcnQtbGluZTpob3ZlciByZWN0IHsgZmlsbDogIzkxMUVCNDsgZmlsbC1vcGFjaXR5OiA0MCU7IHN0cm9rZTogI0ZGRkZGRjYwOyBjb2xvcjogcmVkOyB9IC52ZXJ0LWxpbmU6aG92ZXIgdGV4dCB7IHN0cm9rZTogd2hpdGU7IGZpbGw6ICMyMTI0Mjc7IH0gLmhvcml6b250YWwtbGluZTpob3ZlciB0ZXh0IHtzdHJva2U6IHdoaXRlOyBmaWxsOiAjMjEyNDI3OyB9IC5yZWYtbGluZTpob3ZlciByZWN0IHsgc3Ryb2tlOiAjRkZGRkZGNjA7IH0gLnJlZi1saW5lOmhvdmVyIGxpbmUgeyBzdHJva2U6ICNGRjAwMDA7IH0gLnJlZi1saW5lOmhvdmVyIHRleHQgeyBzdHJva2U6IHdoaXRlOyBmaWxsOiAjMjEyNDI3OyB9IC55LWF4aXMtbGluZTpob3ZlciByZWN0IHsgZmlsbDogI0VERURFRDsgZmlsbC1vcGFjaXR5OiA2MCU7IHN0cm9rZTogI0ZGRkZGRjYwOyBjb2xvcjogcmVkOyB9IC55LWF4aXMtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgc3Ryb2tlLXdpZHRoOiAwLjIwZW07IGZpbGw6ICMxQTFDMUY7IH0gPC9zdHlsZT48cGF0aCBjbGFzcz0iYXJlYS1jbG9zZWQiIGQ9Ik0gNTAuMCwyMi44Nzg3ODc4Nzg3ODc4OTcgMTA4LjMzMzMzMzMzMzMzMzMzLDE1LjAgMTY2LjY2NjY2NjY2NjY2NjY2LDY4LjAzMDMwMzAzMDMwMzAzIDIyNS4wLDQ5Ljg0ODQ4NDg0ODQ4NDg2IDI4My4zMzMzMzMzMzMzMzMzLDcxLjM2MzYzNjM2MzYzNjM3IDM0MS42NjY2NjY2NjY2NjY3LDExNS4wIDQwMC4wLDk1LjYwNjA2MDYwNjA2MDYxIDQwMC4wLDEyNSA1MC4wLDEyNSBaIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjIiIGZpbGw9InVybCgjYXJlYV9wYXR0ZXJuKSIgZmlsbC1vcGFjaXR5PSIwLjciIC8+PHBhdGggZD0iTSA1MC4wLDIyLjg3ODc4Nzg3ODc4Nzg5NyBDIDc1LjAsMjIuODc4Nzg3ODc4Nzg3ODk3IDgzLjMzMzMzMzMzMzMzMzMzLDE1LjAgMTA4LjMzMzMzMzMzMzMzMzMzLDE1LjAgQyAxMzMuMzMzMzMzMzMzMzMzMzEsMTUuMCAxNDEuNjY2NjY2NjY2NjY2NjYsNjguMDMwMzAzMDMwMzAzMDMgMTY2LjY2NjY2NjY2NjY2NjY2LDY4LjAzMDMwMzAzMDMwMzAzIEMgMTkxLjY2NjY2NjY2NjY2NjY2LDY4LjAzMDMwMzAzMDMwMzAzIDIwMC4wLDQ5Ljg0ODQ4NDg0ODQ4NDg2IDIyNS4wLDQ5Ljg0ODQ4NDg0ODQ4NDg2IEMgMjUwLjAsNDkuODQ4NDg0ODQ4NDg0ODYgMjU4LjMzMzMzMzMzMzMzMzMsNzEuMzYzNjM2MzYzNjM2MzcgMjgzLjMzMzMzMzMzMzMzMzMsNzEuMzYzNjM2MzYzNjM2MzcgQyAzMDguMzMzMzMzMzMzMzMzMyw3MS4zNjM2MzYzNjM2MzYzNyAzMTYuNjY2NjY2NjY2NjY2NywxMTUuMCAzNDEuNjY2NjY2NjY2NjY2NywxMTUuMCBDIDM2Ni42NjY2NjY2NjY2NjY3LDExNS4wIDM3NS4wLDk1LjYwNjA2MDYwNjA2MDYxIDQwMC4wLDk1LjYwNjA2MDYwNjA2MDYxIiBzdHJva2U9IiM0NjgyQjQiIHN0cm9rZS13aWR0aD0iOCIgZmlsbD0ibm9uZSIgLz48Y2lyY2xlIGN4PSI1MC4wIiBjeT0iMjIuODc4Nzg3ODc4Nzg3ODk3IiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjEwOC4zMzMzMzMzMzMzMzMzMyIgY3k9IjE1LjAiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMTY2LjY2NjY2NjY2NjY2NjY2IiBjeT0iNjguMDMwMzAzMDMwMzAzMDMiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMjI1LjAiIGN5PSI0OS44NDg0ODQ4NDg0ODQ4NiIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIyODMuMzMzMzMzMzMzMzMzMyIgY3k9IjcxLjM2MzYzNjM2MzYzNjM3IiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjM0MS42NjY2NjY2NjY2NjY3IiBjeT0iMTE1LjAiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iNDAwLjAiIGN5PSI5NS42MDYwNjA2MDYwNjA2MSIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48ZyBjbGFzcz0ieS1heGlzLWxpbmUiPjxyZWN0IHg9IjAiIHk9IjAiIHdpZHRoPSI2NSIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMCIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMCIgeT0iMTkuMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMjUiPjUuOTg8L3RleHQ+PHRleHQgeD0iMCIgeT0iMTI2LjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjI1Ij4yLjY4PC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSI0MC4wIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSI2MC4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+NS43MjwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iOTguMzMzMzMzMzMzMzMzMzMiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjExOC4zMzMzMzMzMzMzMzMzMyIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjUuOTg8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjE1Ni42NjY2NjY2NjY2NjY2NiIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMTc2LjY2NjY2NjY2NjY2NjY2IiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+NC4yMzwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMjE1LjAiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjIzNS4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+NC44MzwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMjczLjMzMzMzMzMzMzMzMzMiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjI5My4zMzMzMzMzMzMzMzMzIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+NC4xMjwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMzMxLjY2NjY2NjY2NjY2NjciIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjM1MS42NjY2NjY2NjY2NjY3IiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+Mi42ODwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMzkwLjAiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjQxMC4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+My4zMjwvdGV4dD48L2c+PC9zdmc+" />
</div></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Hb</th>
<td class="gt_row gt_center"><div>
<img src="data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdib3g9IjAgMCA0NTAgMTMwIiBzdHlsZT0iaGVpZ2h0OiAyZW07IG1hcmdpbi1sZWZ0OiBhdXRvOyBtYXJnaW4tcmlnaHQ6IGF1dG87IGZvbnQtc2l6ZTogaW5oZXJpdDsgb3ZlcmZsb3c6IHZpc2libGU7IHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7IHBvc2l0aW9uOnJlbGF0aXZlOyI+PGRlZnM+PHBhdHRlcm4gaWQ9ImFyZWFfcGF0dGVybiIgd2lkdGg9IjgiIGhlaWdodD0iOCIgcGF0dGVybnVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggY2xhc3M9InBhdHRlcm4tbGluZSIgZD0iTSAwLDggbCA4LC04IE0gLTEsMSBsIDQsLTQgTSA2LDEwIGwgNCwtNCIgc3Ryb2tlPSIjRkYwMDAwIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiIgLz48L3BhdHRlcm4+PC9kZWZzPjxzdHlsZT4gdGV4dCB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsICdDYXNjYWRpYSBDb2RlJywgJ1NvdXJjZSBDb2RlIFBybycsIE1lbmxvLCBDb25zb2xhcywgJ0RlamFWdSBTYW5zIE1vbm8nLCBtb25vc3BhY2U7IHN0cm9rZS13aWR0aDogMC4xNWVtOyBwYWludC1vcmRlcjogc3Ryb2tlOyBzdHJva2UtbGluZWpvaW46IHJvdW5kOyBjdXJzb3I6IGRlZmF1bHQ7IH0gLnZlcnQtbGluZTpob3ZlciByZWN0IHsgZmlsbDogIzkxMUVCNDsgZmlsbC1vcGFjaXR5OiA0MCU7IHN0cm9rZTogI0ZGRkZGRjYwOyBjb2xvcjogcmVkOyB9IC52ZXJ0LWxpbmU6aG92ZXIgdGV4dCB7IHN0cm9rZTogd2hpdGU7IGZpbGw6ICMyMTI0Mjc7IH0gLmhvcml6b250YWwtbGluZTpob3ZlciB0ZXh0IHtzdHJva2U6IHdoaXRlOyBmaWxsOiAjMjEyNDI3OyB9IC5yZWYtbGluZTpob3ZlciByZWN0IHsgc3Ryb2tlOiAjRkZGRkZGNjA7IH0gLnJlZi1saW5lOmhvdmVyIGxpbmUgeyBzdHJva2U6ICNGRjAwMDA7IH0gLnJlZi1saW5lOmhvdmVyIHRleHQgeyBzdHJva2U6IHdoaXRlOyBmaWxsOiAjMjEyNDI3OyB9IC55LWF4aXMtbGluZTpob3ZlciByZWN0IHsgZmlsbDogI0VERURFRDsgZmlsbC1vcGFjaXR5OiA2MCU7IHN0cm9rZTogI0ZGRkZGRjYwOyBjb2xvcjogcmVkOyB9IC55LWF4aXMtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgc3Ryb2tlLXdpZHRoOiAwLjIwZW07IGZpbGw6ICMxQTFDMUY7IH0gPC9zdHlsZT48cGF0aCBjbGFzcz0iYXJlYS1jbG9zZWQiIGQ9Ik0gNTAuMCwxNS4wIDEwOC4zMzMzMzMzMzMzMzMzMywzOC4wNzY5MjMwNzY5MjMwNyAxNjYuNjY2NjY2NjY2NjY2NjYsNDkuNjE1Mzg0NjE1Mzg0NjEgMjI1LjAsNjMuNzE3OTQ4NzE3OTQ4NzIgMjgzLjMzMzMzMzMzMzMzMzMsMTE1LjAgMzQxLjY2NjY2NjY2NjY2NjcsOTkuNjE1Mzg0NjE1Mzg0NjEgNDAwLjAsODkuMzU4OTc0MzU4OTc0MzYgNDAwLjAsMTI1IDUwLjAsMTI1IFoiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMiIgZmlsbD0idXJsKCNhcmVhX3BhdHRlcm4pIiBmaWxsLW9wYWNpdHk9IjAuNyIgLz48cGF0aCBkPSJNIDUwLjAsMTUuMCBDIDc1LjAsMTUuMCA4My4zMzMzMzMzMzMzMzMzMywzOC4wNzY5MjMwNzY5MjMwNyAxMDguMzMzMzMzMzMzMzMzMzMsMzguMDc2OTIzMDc2OTIzMDcgQyAxMzMuMzMzMzMzMzMzMzMzMzEsMzguMDc2OTIzMDc2OTIzMDcgMTQxLjY2NjY2NjY2NjY2NjY2LDQ5LjYxNTM4NDYxNTM4NDYxIDE2Ni42NjY2NjY2NjY2NjY2Niw0OS42MTUzODQ2MTUzODQ2MSBDIDE5MS42NjY2NjY2NjY2NjY2Niw0OS42MTUzODQ2MTUzODQ2MSAyMDAuMCw2My43MTc5NDg3MTc5NDg3MiAyMjUuMCw2My43MTc5NDg3MTc5NDg3MiBDIDI1MC4wLDYzLjcxNzk0ODcxNzk0ODcyIDI1OC4zMzMzMzMzMzMzMzMzLDExNS4wIDI4My4zMzMzMzMzMzMzMzMzLDExNS4wIEMgMzA4LjMzMzMzMzMzMzMzMzMsMTE1LjAgMzE2LjY2NjY2NjY2NjY2NjcsOTkuNjE1Mzg0NjE1Mzg0NjEgMzQxLjY2NjY2NjY2NjY2NjcsOTkuNjE1Mzg0NjE1Mzg0NjEgQyAzNjYuNjY2NjY2NjY2NjY2Nyw5OS42MTUzODQ2MTUzODQ2MSAzNzUuMCw4OS4zNTg5NzQzNTg5NzQzNiA0MDAuMCw4OS4zNTg5NzQzNTg5NzQzNiIgc3Ryb2tlPSIjNDY4MkI0IiBzdHJva2Utd2lkdGg9IjgiIGZpbGw9Im5vbmUiIC8+PGNpcmNsZSBjeD0iNTAuMCIgY3k9IjE1LjAiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMTA4LjMzMzMzMzMzMzMzMzMzIiBjeT0iMzguMDc2OTIzMDc2OTIzMDciIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMTY2LjY2NjY2NjY2NjY2NjY2IiBjeT0iNDkuNjE1Mzg0NjE1Mzg0NjEiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMjI1LjAiIGN5PSI2My43MTc5NDg3MTc5NDg3MiIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIyODMuMzMzMzMzMzMzMzMzMyIgY3k9IjExNS4wIiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjM0MS42NjY2NjY2NjY2NjY3IiBjeT0iOTkuNjE1Mzg0NjE1Mzg0NjEiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iNDAwLjAiIGN5PSI4OS4zNTg5NzQzNTg5NzQzNiIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48ZyBjbGFzcz0ieS1heGlzLWxpbmUiPjxyZWN0IHg9IjAiIHk9IjAiIHdpZHRoPSI2NSIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMCIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMCIgeT0iMTkuMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMjUiPjE1MzwvdGV4dD48dGV4dCB4PSIwIiB5PSIxMjYuMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMjUiPjc1PC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSI0MC4wIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSI2MC4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MTUzPC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSI5OC4zMzMzMzMzMzMzMzMzMyIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMTE4LjMzMzMzMzMzMzMzMzMzIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MTM1PC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIxNTYuNjY2NjY2NjY2NjY2NjYiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjE3Ni42NjY2NjY2NjY2NjY2NiIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjEyNjwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMjE1LjAiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjIzNS4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MTE1PC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIyNzMuMzMzMzMzMzMzMzMzMyIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMjkzLjMzMzMzMzMzMzMzMzMiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij43NTwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMzMxLjY2NjY2NjY2NjY2NjciIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjM1MS42NjY2NjY2NjY2NjY3IiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+ODc8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjM5MC4wIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSI0MTAuMCIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjk1PC90ZXh0PjwvZz48L3N2Zz4=" />
</div></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">PLT</th>
<td class="gt_row gt_center"><div>
<img src="data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdib3g9IjAgMCA0NTAgMTMwIiBzdHlsZT0iaGVpZ2h0OiAyZW07IG1hcmdpbi1sZWZ0OiBhdXRvOyBtYXJnaW4tcmlnaHQ6IGF1dG87IGZvbnQtc2l6ZTogaW5oZXJpdDsgb3ZlcmZsb3c6IHZpc2libGU7IHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7IHBvc2l0aW9uOnJlbGF0aXZlOyI+PGRlZnM+PHBhdHRlcm4gaWQ9ImFyZWFfcGF0dGVybiIgd2lkdGg9IjgiIGhlaWdodD0iOCIgcGF0dGVybnVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggY2xhc3M9InBhdHRlcm4tbGluZSIgZD0iTSAwLDggbCA4LC04IE0gLTEsMSBsIDQsLTQgTSA2LDEwIGwgNCwtNCIgc3Ryb2tlPSIjRkYwMDAwIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiIgLz48L3BhdHRlcm4+PC9kZWZzPjxzdHlsZT4gdGV4dCB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsICdDYXNjYWRpYSBDb2RlJywgJ1NvdXJjZSBDb2RlIFBybycsIE1lbmxvLCBDb25zb2xhcywgJ0RlamFWdSBTYW5zIE1vbm8nLCBtb25vc3BhY2U7IHN0cm9rZS13aWR0aDogMC4xNWVtOyBwYWludC1vcmRlcjogc3Ryb2tlOyBzdHJva2UtbGluZWpvaW46IHJvdW5kOyBjdXJzb3I6IGRlZmF1bHQ7IH0gLnZlcnQtbGluZTpob3ZlciByZWN0IHsgZmlsbDogIzkxMUVCNDsgZmlsbC1vcGFjaXR5OiA0MCU7IHN0cm9rZTogI0ZGRkZGRjYwOyBjb2xvcjogcmVkOyB9IC52ZXJ0LWxpbmU6aG92ZXIgdGV4dCB7IHN0cm9rZTogd2hpdGU7IGZpbGw6ICMyMTI0Mjc7IH0gLmhvcml6b250YWwtbGluZTpob3ZlciB0ZXh0IHtzdHJva2U6IHdoaXRlOyBmaWxsOiAjMjEyNDI3OyB9IC5yZWYtbGluZTpob3ZlciByZWN0IHsgc3Ryb2tlOiAjRkZGRkZGNjA7IH0gLnJlZi1saW5lOmhvdmVyIGxpbmUgeyBzdHJva2U6ICNGRjAwMDA7IH0gLnJlZi1saW5lOmhvdmVyIHRleHQgeyBzdHJva2U6IHdoaXRlOyBmaWxsOiAjMjEyNDI3OyB9IC55LWF4aXMtbGluZTpob3ZlciByZWN0IHsgZmlsbDogI0VERURFRDsgZmlsbC1vcGFjaXR5OiA2MCU7IHN0cm9rZTogI0ZGRkZGRjYwOyBjb2xvcjogcmVkOyB9IC55LWF4aXMtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgc3Ryb2tlLXdpZHRoOiAwLjIwZW07IGZpbGw6ICMxQTFDMUY7IH0gPC9zdHlsZT48cGF0aCBjbGFzcz0iYXJlYS1jbG9zZWQiIGQ9Ik0gNTAuMCwyOS42MzkxNzUyNTc3MzE5NSAxMDguMzMzMzMzMzMzMzMzMzMsODguMTk1ODc2Mjg4NjU5NzkgMTY2LjY2NjY2NjY2NjY2NjY2LDExMS4yODg2NTk3OTM4MTQ0MyAyMjUuMCwxMTMuNzYyODg2NTk3OTM4MTUgMjgzLjMzMzMzMzMzMzMzMzMsMTUuMCAzNDEuNjY2NjY2NjY2NjY2Nyw5My4xNDQzMjk4OTY5MDcyMSA0MDAuMCwxMTUuMCA0MDAuMCwxMjUgNTAuMCwxMjUgWiIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJ1cmwoI2FyZWFfcGF0dGVybikiIGZpbGwtb3BhY2l0eT0iMC43IiAvPjxwYXRoIGQ9Ik0gNTAuMCwyOS42MzkxNzUyNTc3MzE5NSBDIDc1LjAsMjkuNjM5MTc1MjU3NzMxOTUgODMuMzMzMzMzMzMzMzMzMzMsODguMTk1ODc2Mjg4NjU5NzkgMTA4LjMzMzMzMzMzMzMzMzMzLDg4LjE5NTg3NjI4ODY1OTc5IEMgMTMzLjMzMzMzMzMzMzMzMzMxLDg4LjE5NTg3NjI4ODY1OTc5IDE0MS42NjY2NjY2NjY2NjY2NiwxMTEuMjg4NjU5NzkzODE0NDMgMTY2LjY2NjY2NjY2NjY2NjY2LDExMS4yODg2NTk3OTM4MTQ0MyBDIDE5MS42NjY2NjY2NjY2NjY2NiwxMTEuMjg4NjU5NzkzODE0NDMgMjAwLjAsMTEzLjc2Mjg4NjU5NzkzODE1IDIyNS4wLDExMy43NjI4ODY1OTc5MzgxNSBDIDI1MC4wLDExMy43NjI4ODY1OTc5MzgxNSAyNTguMzMzMzMzMzMzMzMzMywxNS4wIDI4My4zMzMzMzMzMzMzMzMzLDE1LjAgQyAzMDguMzMzMzMzMzMzMzMzMywxNS4wIDMxNi42NjY2NjY2NjY2NjY3LDkzLjE0NDMyOTg5NjkwNzIxIDM0MS42NjY2NjY2NjY2NjY3LDkzLjE0NDMyOTg5NjkwNzIxIEMgMzY2LjY2NjY2NjY2NjY2NjcsOTMuMTQ0MzI5ODk2OTA3MjEgMzc1LjAsMTE1LjAgNDAwLjAsMTE1LjAiIHN0cm9rZT0iIzQ2ODJCNCIgc3Ryb2tlLXdpZHRoPSI4IiBmaWxsPSJub25lIiAvPjxjaXJjbGUgY3g9IjUwLjAiIGN5PSIyOS42MzkxNzUyNTc3MzE5NSIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIxMDguMzMzMzMzMzMzMzMzMzMiIGN5PSI4OC4xOTU4NzYyODg2NTk3OSIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIxNjYuNjY2NjY2NjY2NjY2NjYiIGN5PSIxMTEuMjg4NjU5NzkzODE0NDMiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMjI1LjAiIGN5PSIxMTMuNzYyODg2NTk3OTM4MTUiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMjgzLjMzMzMzMzMzMzMzMzMiIGN5PSIxNS4wIiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjM0MS42NjY2NjY2NjY2NjY3IiBjeT0iOTMuMTQ0MzI5ODk2OTA3MjEiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iNDAwLjAiIGN5PSIxMTUuMCIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48ZyBjbGFzcz0ieS1heGlzLWxpbmUiPjxyZWN0IHg9IjAiIHk9IjAiIHdpZHRoPSI2NSIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMCIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMCIgeT0iMTkuMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMjUiPjc0LjE8L3RleHQ+PHRleHQgeD0iMCIgeT0iMTI2LjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjI1Ij4yNS42PC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSI0MC4wIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSI2MC4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+NjcuMDwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iOTguMzMzMzMzMzMzMzMzMzMiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjExOC4zMzMzMzMzMzMzMzMzMyIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjM4LjY8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjE1Ni42NjY2NjY2NjY2NjY2NiIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMTc2LjY2NjY2NjY2NjY2NjY2IiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MjcuNDwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMjE1LjAiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjIzNS4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MjYuMjwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMjczLjMzMzMzMzMzMzMzMzMiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjI5My4zMzMzMzMzMzMzMzMzIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+NzQuMTwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMzMxLjY2NjY2NjY2NjY2NjciIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjM1MS42NjY2NjY2NjY2NjY3IiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MzYuMjwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMzkwLjAiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjQxMC4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MjUuNjwvdGV4dD48L2c+PC9zdmc+" />
</div></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">ALT</th>
<td class="gt_row gt_center"><div>
<img src="data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdib3g9IjAgMCA0NTAgMTMwIiBzdHlsZT0iaGVpZ2h0OiAyZW07IG1hcmdpbi1sZWZ0OiBhdXRvOyBtYXJnaW4tcmlnaHQ6IGF1dG87IGZvbnQtc2l6ZTogaW5oZXJpdDsgb3ZlcmZsb3c6IHZpc2libGU7IHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7IHBvc2l0aW9uOnJlbGF0aXZlOyI+PGRlZnM+PHBhdHRlcm4gaWQ9ImFyZWFfcGF0dGVybiIgd2lkdGg9IjgiIGhlaWdodD0iOCIgcGF0dGVybnVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggY2xhc3M9InBhdHRlcm4tbGluZSIgZD0iTSAwLDggbCA4LC04IE0gLTEsMSBsIDQsLTQgTSA2LDEwIGwgNCwtNCIgc3Ryb2tlPSIjRkYwMDAwIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiIgLz48L3BhdHRlcm4+PC9kZWZzPjxzdHlsZT4gdGV4dCB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsICdDYXNjYWRpYSBDb2RlJywgJ1NvdXJjZSBDb2RlIFBybycsIE1lbmxvLCBDb25zb2xhcywgJ0RlamFWdSBTYW5zIE1vbm8nLCBtb25vc3BhY2U7IHN0cm9rZS13aWR0aDogMC4xNWVtOyBwYWludC1vcmRlcjogc3Ryb2tlOyBzdHJva2UtbGluZWpvaW46IHJvdW5kOyBjdXJzb3I6IGRlZmF1bHQ7IH0gLnZlcnQtbGluZTpob3ZlciByZWN0IHsgZmlsbDogIzkxMUVCNDsgZmlsbC1vcGFjaXR5OiA0MCU7IHN0cm9rZTogI0ZGRkZGRjYwOyBjb2xvcjogcmVkOyB9IC52ZXJ0LWxpbmU6aG92ZXIgdGV4dCB7IHN0cm9rZTogd2hpdGU7IGZpbGw6ICMyMTI0Mjc7IH0gLmhvcml6b250YWwtbGluZTpob3ZlciB0ZXh0IHtzdHJva2U6IHdoaXRlOyBmaWxsOiAjMjEyNDI3OyB9IC5yZWYtbGluZTpob3ZlciByZWN0IHsgc3Ryb2tlOiAjRkZGRkZGNjA7IH0gLnJlZi1saW5lOmhvdmVyIGxpbmUgeyBzdHJva2U6ICNGRjAwMDA7IH0gLnJlZi1saW5lOmhvdmVyIHRleHQgeyBzdHJva2U6IHdoaXRlOyBmaWxsOiAjMjEyNDI3OyB9IC55LWF4aXMtbGluZTpob3ZlciByZWN0IHsgZmlsbDogI0VERURFRDsgZmlsbC1vcGFjaXR5OiA2MCU7IHN0cm9rZTogI0ZGRkZGRjYwOyBjb2xvcjogcmVkOyB9IC55LWF4aXMtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgc3Ryb2tlLXdpZHRoOiAwLjIwZW07IGZpbGw6ICMxQTFDMUY7IH0gPC9zdHlsZT48cGF0aCBjbGFzcz0iYXJlYS1jbG9zZWQiIGQ9Ik0gNTAuMCwxNS4wIDEwOC4zMzMzMzMzMzMzMzMzMywxNi42NDczNzk2MTE0NDU2MzMgMTY2LjY2NjY2NjY2NjY2NjY2LDY3LjAwNDQ0NzExMzQzMzg2IDIyNS4wLDg0LjU2MjQzMDAwNjY1NDQ0IDI4My4zMzMzMzMzMzMzMzMzLDEwNS45ODE2MTEwMjM2NDc2IDM0MS42NjY2NjY2NjY2NjY3LDExMy42OTk5NDk2ODU5NDI5IDQwMC4wLDExNS4wIDQwMC4wLDEyNSA1MC4wLDEyNSBaIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjIiIGZpbGw9InVybCgjYXJlYV9wYXR0ZXJuKSIgZmlsbC1vcGFjaXR5PSIwLjciIC8+PHBhdGggZD0iTSA1MC4wLDE1LjAgQyA3NS4wLDE1LjAgODMuMzMzMzMzMzMzMzMzMzMsMTYuNjQ3Mzc5NjExNDQ1NjMzIDEwOC4zMzMzMzMzMzMzMzMzMywxNi42NDczNzk2MTE0NDU2MzMgQyAxMzMuMzMzMzMzMzMzMzMzMzEsMTYuNjQ3Mzc5NjExNDQ1NjMzIDE0MS42NjY2NjY2NjY2NjY2Niw2Ny4wMDQ0NDcxMTM0MzM4NiAxNjYuNjY2NjY2NjY2NjY2NjYsNjcuMDA0NDQ3MTEzNDMzODYgQyAxOTEuNjY2NjY2NjY2NjY2NjYsNjcuMDA0NDQ3MTEzNDMzODYgMjAwLjAsODQuNTYyNDMwMDA2NjU0NDQgMjI1LjAsODQuNTYyNDMwMDA2NjU0NDQgQyAyNTAuMCw4NC41NjI0MzAwMDY2NTQ0NCAyNTguMzMzMzMzMzMzMzMzMywxMDUuOTgxNjExMDIzNjQ3NiAyODMuMzMzMzMzMzMzMzMzMywxMDUuOTgxNjExMDIzNjQ3NiBDIDMwOC4zMzMzMzMzMzMzMzMzLDEwNS45ODE2MTEwMjM2NDc2IDMxNi42NjY2NjY2NjY2NjY3LDExMy42OTk5NDk2ODU5NDI5IDM0MS42NjY2NjY2NjY2NjY3LDExMy42OTk5NDk2ODU5NDI5IEMgMzY2LjY2NjY2NjY2NjY2NjcsMTEzLjY5OTk0OTY4NTk0MjkgMzc1LjAsMTE1LjAgNDAwLjAsMTE1LjAiIHN0cm9rZT0iIzQ2ODJCNCIgc3Ryb2tlLXdpZHRoPSI4IiBmaWxsPSJub25lIiAvPjxjaXJjbGUgY3g9IjUwLjAiIGN5PSIxNS4wIiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjEwOC4zMzMzMzMzMzMzMzMzMyIgY3k9IjE2LjY0NzM3OTYxMTQ0NTYzMyIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIxNjYuNjY2NjY2NjY2NjY2NjYiIGN5PSI2Ny4wMDQ0NDcxMTM0MzM4NiIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIyMjUuMCIgY3k9Ijg0LjU2MjQzMDAwNjY1NDQ0IiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjI4My4zMzMzMzMzMzMzMzMzIiBjeT0iMTA1Ljk4MTYxMTAyMzY0NzYiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMzQxLjY2NjY2NjY2NjY2NjciIGN5PSIxMTMuNjk5OTQ5Njg1OTQyOSIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSI0MDAuMCIgY3k9IjExNS4wIiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxnIGNsYXNzPSJ5LWF4aXMtbGluZSI+PHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjY1IiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIwIiB5PSIxOS4wIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIyNSI+MTIuOEs8L3RleHQ+PHRleHQgeD0iMCIgeT0iMTI2LjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjI1Ij41MTI8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjQwLjAiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjYwLjAiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij4xMi44SzwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iOTguMzMzMzMzMzMzMzMzMzMiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjExOC4zMzMzMzMzMzMzMzMzMyIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjEyLjZLPC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIxNTYuNjY2NjY2NjY2NjY2NjYiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjE3Ni42NjY2NjY2NjY2NjY2NiIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjYuNDNLPC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIyMTUuMCIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMjM1LjAiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij40LjI2SzwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMjczLjMzMzMzMzMzMzMzMzMiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjI5My4zMzMzMzMzMzMzMzMzIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MS42Mks8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjMzMS42NjY2NjY2NjY2NjY3IiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIzNTEuNjY2NjY2NjY2NjY2NyIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjY3MzwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMzkwLjAiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjQxMC4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+NTEyPC90ZXh0PjwvZz48L3N2Zz4=" />
</div></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">AST</th>
<td class="gt_row gt_center"><div>
yYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjM1MS42NjY2NjY2NjY2NjY3IiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MS4xNEs8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjM5MC4wIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSI0MTAuMCIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjc4MjwvdGV4dD48L2c+PC9zdmc+" />
</div></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">TBIL</th>
<td class="gt_row gt_center"><div>
<img src="data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdib3g9IjAgMCA0NTAgMTMwIiBzdHlsZT0iaGVpZ2h0OiAyZW07IG1hcmdpbi1sZWZ0OiBhdXRvOyBtYXJnaW4tcmlnaHQ6IGF1dG87IGZvbnQtc2l6ZTogaW5oZXJpdDsgb3ZlcmZsb3c6IHZpc2libGU7IHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7IHBvc2l0aW9uOnJlbGF0aXZlOyI+PGRlZnM+PHBhdHRlcm4gaWQ9ImFyZWFfcGF0dGVybiIgd2lkdGg9IjgiIGhlaWdodD0iOCIgcGF0dGVybnVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggY2xhc3M9InBhdHRlcm4tbGluZSIgZD0iTSAwLDggbCA4LC04IE0gLTEsMSBsIDQsLTQgTSA2LDEwIGwgNCwtNCIgc3Ryb2tlPSIjRkYwMDAwIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiIgLz48L3BhdHRlcm4+PC9kZWZzPjxzdHlsZT4gdGV4dCB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsICdDYXNjYWRpYSBDb2RlJywgJ1NvdXJjZSBDb2RlIFBybycsIE1lbmxvLCBDb25zb2xhcywgJ0RlamFWdSBTYW5zIE1vbm8nLCBtb25vc3BhY2U7IHN0cm9rZS13aWR0aDogMC4xNWVtOyBwYWludC1vcmRlcjogc3Ryb2tlOyBzdHJva2UtbGluZWpvaW46IHJvdW5kOyBjdXJzb3I6IGRlZmF1bHQ7IH0gLnZlcnQtbGluZTpob3ZlciByZWN0IHsgZmlsbDogIzkxMUVCNDsgZmlsbC1vcGFjaXR5OiA0MCU7IHN0cm9rZTogI0ZGRkZGRjYwOyBjb2xvcjogcmVkOyB9IC52ZXJ0LWxpbmU6aG92ZXIgdGV4dCB7IHN0cm9rZTogd2hpdGU7IGZpbGw6ICMyMTI0Mjc7IH0gLmhvcml6b250YWwtbGluZTpob3ZlciB0ZXh0IHtzdHJva2U6IHdoaXRlOyBmaWxsOiAjMjEyNDI3OyB9IC5yZWYtbGluZTpob3ZlciByZWN0IHsgc3Ryb2tlOiAjRkZGRkZGNjA7IH0gLnJlZi1saW5lOmhvdmVyIGxpbmUgeyBzdHJva2U6ICNGRjAwMDA7IH0gLnJlZi1saW5lOmhvdmVyIHRleHQgeyBzdHJva2U6IHdoaXRlOyBmaWxsOiAjMjEyNDI3OyB9IC55LWF4aXMtbGluZTpob3ZlciByZWN0IHsgZmlsbDogI0VERURFRDsgZmlsbC1vcGFjaXR5OiA2MCU7IHN0cm9rZTogI0ZGRkZGRjYwOyBjb2xvcjogcmVkOyB9IC55LWF4aXMtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgc3Ryb2tlLXdpZHRoOiAwLjIwZW07IGZpbGw6ICMxQTFDMUY7IH0gPC9zdHlsZT48cGF0aCBjbGFzcz0iYXJlYS1jbG9zZWQiIGQ9Ik0gNTAuMCw5NC4xNzM4MzgyMDk5ODI3OCAxMDguMzMzMzMzMzMzMzMzMzMsNDguMzkwNzA1Njc5ODYyMjggMTY2LjY2NjY2NjY2NjY2NjY2LDU5Ljc1MDQzMDI5MjU5ODk4IDIyNS4wLDIzLjc3Nzk2OTAxODkzMjg2NSAyODMuMzMzMzMzMzMzMzMzMyw3Ni43OTAwMTcyMTE3MDM5NSAzNDEuNjY2NjY2NjY2NjY2NywxMTUuMCA0MDAuMCwxNS4wIDQwMC4wLDEyNSA1MC4wLDEyNSBaIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjIiIGZpbGw9InVybCgjYXJlYV9wYXR0ZXJuKSIgZmlsbC1vcGFjaXR5PSIwLjciIC8+PHBhdGggZD0iTSA1MC4wLDk0LjE3MzgzODIwOTk4Mjc4IEMgNzUuMCw5NC4xNzM4MzgyMDk5ODI3OCA4My4zMzMzMzMzMzMzMzMzMyw0OC4zOTA3MDU2Nzk4NjIyOCAxMDguMzMzMzMzMzMzMzMzMzMsNDguMzkwNzA1Njc5ODYyMjggQyAxMzMuMzMzMzMzMzMzMzMzMzEsNDguMzkwNzA1Njc5ODYyMjggMTQxLjY2NjY2NjY2NjY2NjY2LDU5Ljc1MDQzMDI5MjU5ODk4IDE2Ni42NjY2NjY2NjY2NjY2Niw1OS43NTA0MzAyOTI1OTg5OCBDIDE5MS42NjY2NjY2NjY2NjY2Niw1OS43NTA0MzAyOTI1OTg5OCAyMDAuMCwyMy43Nzc5NjkwMTg5MzI4NjUgMjI1LjAsMjMuNzc3OTY5MDE4OTMyODY1IEMgMjUwLjAsMjMuNzc3OTY5MDE4OTMyODY1IDI1OC4zMzMzMzMzMzMzMzMzLDc2Ljc5MDAxNzIxMTcwMzk1IDI4My4zMzMzMzMzMzMzMzMzLDc2Ljc5MDAxNzIxMTcwMzk1IEMgMzA4LjMzMzMzMzMzMzMzMzMsNzYuNzkwMDE3MjExNzAzOTUgMzE2LjY2NjY2NjY2NjY2NjcsMTE1LjAgMzQxLjY2NjY2NjY2NjY2NjcsMTE1LjAgQyAzNjYuNjY2NjY2NjY2NjY2NywxMTUuMCAzNzUuMCwxNS4wIDQwMC4wLDE1LjAiIHN0cm9rZT0iIzQ2ODJCNCIgc3Ryb2tlLXdpZHRoPSI4IiBmaWxsPSJub25lIiAvPjxjaXJjbGUgY3g9IjUwLjAiIGN5PSI5NC4xNzM4MzgyMDk5ODI3OCIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIxMDguMzMzMzMzMzMzMzMzMzMiIGN5PSI0OC4zOTA3MDU2Nzk4NjIyOCIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIxNjYuNjY2NjY2NjY2NjY2NjYiIGN5PSI1OS43NTA0MzAyOTI1OTg5OCIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIyMjUuMCIgY3k9IjIzLjc3Nzk2OTAxODkzMjg2NSIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIyODMuMzMzMzMzMzMzMzMzMyIgY3k9Ijc2Ljc5MDAxNzIxMTcwMzk1IiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjM0MS42NjY2NjY2NjY2NjY3IiBjeT0iMTE1LjAiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iNDAwLjAiIGN5PSIxNS4wIiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxnIGNsYXNzPSJ5LWF4aXMtbGluZSI+PHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjY1IiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIwIiB5PSIxOS4wIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIyNSI+MTYzPC90ZXh0Pjx0ZXh0IHg9IjAiIHk9IjEyNi4wIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIyNSI+MTA1PC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSI0MC4wIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSI2MC4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MTE3PC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSI5OC4zMzMzMzMzMzMzMzMzMyIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMTE4LjMzMzMzMzMzMzMzMzMzIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MTQ0PC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIxNTYuNjY2NjY2NjY2NjY2NjYiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjE3Ni42NjY2NjY2NjY2NjY2NiIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjEzNzwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMjE1LjAiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjIzNS4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MTU4PC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIyNzMuMzMzMzMzMzMzMzMzMyIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMjkzLjMzMzMzMzMzMzMzMzMiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij4xMjc8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjMzMS42NjY2NjY2NjY2NjY3IiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIzNTEuNjY2NjY2NjY2NjY2NyIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjEwNTwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMzkwLjAiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjQxMC4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MTYzPC90ZXh0PjwvZz48L3N2Zz4=" />
</div></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">DBIL</th>
<td class="gt_row gt_center"><div>
MzMzMzMzMzMzMzMzMzIiBjeT0iNjkuMjA2ODk2NTUxNzI0MTYiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMTY2LjY2NjY2NjY2NjY2NjY2IiBjeT0iODMuMDAwMDAwMDAwMDAwMDEiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMjI1LjAiIGN5PSIxNS4wIiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjI4My4zMzMzMzMzMzMzMzMzIiBjeT0iNTEuMDAwMDAwMDAwMDAwMDEiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMzQxLjY2NjY2NjY2NjY2NjciIGN5PSI5OC4xNzI0MTM3OTMxMDM0NiIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSI0MDAuMCIgY3k9IjM5LjI3NTg2MjA2ODk2NTUyIiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxnIGNsYXNzPSJ5LWF4aXMtbGluZSI+PHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjY1IiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIwIiB5PSIxOS4wIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIyNSI+MTQ0PC90ZXh0Pjx0ZXh0IHg9IjAiIHk9IjEyNi4wIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIyNSI+NzEuNDwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iNDAuMCIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iNjAuMCIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjcxLjQ8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9Ijk4LjMzMzMzMzMzMzMzMzMzIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIxMTguMzMzMzMzMzMzMzMzMzMiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij4xMDU8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjE1Ni42NjY2NjY2NjY2NjY2NiIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMTc2LjY2NjY2NjY2NjY2NjY2IiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+OTQuNjwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMjE1LjAiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjIzNS4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MTQ0PC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIyNzMuMzMzMzMzMzMzMzMzMyIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMjkzLjMzMzMzMzMzMzMzMzMiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij4xMTg8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjMzMS42NjY2NjY2NjY2NjY3IiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIzNTEuNjY2NjY2NjY2NjY2NyIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjgzLjY8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjM5MC4wIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSI0MTAuMCIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjEyNjwvdGV4dD48L2c+PC9zdmc+" />
</div></td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="2" class="gt_sourcenote">Measurements from Day 3 through Day 9.</td>
</tr>
</tfoot>

</table>


Notice that if you hover over the data points, you still get values for each of the days. We designed nanoplots to be stripped down plotting visualizations that balance the quick visual interpretation of a plot against the compactness of a table.

[**Great Tables**](https://github.com/posit-dev/great-tables) contains a lot of functionality for formatting. If you peeked at the code in the above table displays you might have noticed there are methods beginning with `fmt_` (i.e., [fmt_date()](../../reference/GT.fmt_date.md#great_tables.GT.fmt_date), [fmt_integer()](../../reference/GT.fmt_integer.md#great_tables.GT.fmt_integer), [fmt_nanoplot()](../../reference/GT.fmt_nanoplot.md#great_tables.GT.fmt_nanoplot)). We want to make many formatting methods available to serve different users' needs. We also want them to be easy to use, but with many useful options to provide flexibility for all your formatting tasks.


### Great Tables is focused on display

There are myriad ways that people interact with tables. [**Great Tables**](https://github.com/posit-dev/great-tables) is focused on the display of tables for publication and presentation. If you're analyzing data in a database, you might want a simple table display that offers controls to navigate and filter hundreds, thousands, maybe even more records. And that is great for those situations.

The publication of results is a entirely different task, and the emphasis here is on structuring, formatting, and styling. We believe that beautiful table displays should do the following:

- make information easier to digest
- provide extra context wherever needed
- adhere to the style of the document or of the organization

We wanted to help the type of user that wanted to present data in this way. This is typically what you see in journal articles, in books, and in reports. We think the area of static summary tables deserves it's own focus. This class of tables can look *great* and we offer various `opt_*()` methods in the [**Great Tables**](https://github.com/posit-dev/great-tables) API so it's that much easier to provide a great table to your readers.


## In conclusion

Tables have come a long way and we've learned a lot from our continued research in tabular design. We hope to make the [**Great Tables**](https://github.com/posit-dev/great-tables) package useful for your generation of summary tables. Given there's ample room for innovation in this area, we'll keep plugging away at doing that work to improve the API. We measure success by the quality of the tables the package is able to produce and we always keep that goal top of mind.

We're very excited about where things are going with [**Great Tables**](https://github.com/posit-dev/great-tables) and we genuinely appreciate community feedback. If ever you want to talk tables with us, you're always welcome to jump into our [Discord Server](https://discord.com/invite/Ux7nrcXHVV) and drop us a line!

Many thanks to Curtis Kephart and [Anthony Baker](https://anthonywbaker.com) for providing helpful advice when writing this article.


## Footnotes


[^1]: Taylor, B. (2021). Lunar timekeeping in Upper Paleolithic Cave Art. *PRAEHISTORIA New Series*, *3*(13), 215-232.

[^2]: Duke, D. W. (2002). Hipparchus' Coordinate System. *Archive for History of Exact Sciences*, *56*(5), 427-433.

[^3]: <https://en.wikipedia.org/wiki/Geography_(Ptolemy)>

[^4]: Palet, J. M. and Orengo, H. A., The Roman Centuriated Landscape: Conception, Genesis, and Development as Inferred from the Ager Tarraconensis Case. *American Journal of Archaeology*, *115*(3), 383-402.

[^5]: Marchese, F. T., Exploring the Origins of Tables for Information Visualization. *Proceedings of the 2011 15th International Conference on Information Visualisation*, 13-15 July 2011, doi:10.1109/IV.2011.36.

[^6]: M. W. Green, The construction and implementation of the cuneiform writing system, *Visible Writing*, *15*, 1981, 345-72.

[^7]: Robson, E., "Tables and tabular formatting in Sumer, Babylonia, and Assyria, 2500-50 BCE" in M. Campbell-Kelly, M. Croarken, R.G. Flood, and E. Robson (eds.), *The History of Mathematical Tables from Sumer to Spreadsheets*. Oxford: Oxford University Press, 2003, 18-47.

[^8]: <https://site.xavier.edu/polt/typewriters/varityper.html>

[^9]: Manual of Tabular Presentation: An Outline of Theory and Practice in the Presentation of Statistical Data in Tables for Publication. United States. Bureau of the Census. U.S. Government Printing Office, 1949. Resource available at: <https://www2.census.gov/library/publications/1949/general/tabular-presentation.pdf>.

# GT.fmt_email()


Format values as email links.


Usage

``` python
GT.fmt_email(
    columns=None,
    rows=None,
    display_name=None,
    as_button=False,
    color="auto",
    show_underline="auto",
    button_fill="auto",
    button_width=None,
    button_outline=None,
    target="_blank",
)
```


The `fmt_email()` method transforms email addresses in the table body into clickable `mailto:` links. Like `fmt_url()`, the links can be styled as buttons or as plain underlined text, with customizable colors.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`display_name: str | Callable[[str], str] | None = None`  
An optional display name to use instead of the raw email address. If a string is provided, it will be used as the visible text for all links. If a callable is provided, it will be called with the email address and should return the display text.

`as_button: bool = ``False`  
Should the link be styled as a button? By default this is `False`.

`color: str = ``"auto"`  
The color of the link text. The default `"auto"` uses `"#008B8B"` (dark cyan) for regular links and `"#FFFFFF"` (white) for buttons. Any CSS color name or hex value can be used.

`show_underline: str | bool = ``"auto"`  
Should the link be underlined? The default `"auto"` uses `True` for regular links and `False` for buttons. Set explicitly to `True` or `False` to override.

`button_fill: str = ``"auto"`  
The background color for button-style links. The default `"auto"` uses `"#4682B4"` (steel blue). Only used when `as_button=True`.

`button_width: str | None = None`  
The width of the button. Should be a CSS width string (e.g., `"150px"`). By default buttons size to their content.

`button_outline: str | None = None`  
The CSS outline for the button (e.g., `"2px solid #ccc"`). By default, a light gray outline is automatically added when the button fill color is very light, and hidden otherwise.

`target: str | None = ``"_blank"`  
The `target` attribute for the anchor element. Defaults to `"_blank"` to open links in a new tab. Set to `None` to open in the same tab.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using a subset of the [peeps](data.peeps.md#great_tables.data.peeps) dataset filtered to contacts in Australia, let's format the `email_addr` column as email links.


``` python
import polars as pl
from great_tables import GT, md, data

peeps_aus = (
    data.pl.peeps
    .filter(pl.col("country") == "AUS")
    .select(
        "name_given", "name_family", "address", "city",
        "state_prov", "postcode", "country", "email_addr",
    )
)

(
    GT(peeps_aus, rowname_col="name_family")
    .tab_header(title="Our Contacts in Australia")
    .fmt_email(columns="email_addr")
    .cols_label(
        name_given="First Name",
        address="Address",
        city="City",
        state_prov="State",
        postcode="Postcode",
        country="Country",
        email_addr="Email",
    )
)
```


<style>
#kvqmnalelw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kvqmnalelw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kvqmnalelw p { margin: 0; padding: 0; }
 #kvqmnalelw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kvqmnalelw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kvqmnalelw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kvqmnalelw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kvqmnalelw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kvqmnalelw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kvqmnalelw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kvqmnalelw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kvqmnalelw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kvqmnalelw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kvqmnalelw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kvqmnalelw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kvqmnalelw .gt_spanner_row { border-bottom-style: hidden; }
 #kvqmnalelw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kvqmnalelw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kvqmnalelw .gt_from_md> :first-child { margin-top: 0; }
 #kvqmnalelw .gt_from_md> :last-child { margin-bottom: 0; }
 #kvqmnalelw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kvqmnalelw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kvqmnalelw .gt_indent_1 { text-indent: 5px; }
 #kvqmnalelw .gt_indent_2 { text-indent: calc(5px * 2); }
 #kvqmnalelw .gt_indent_3 { text-indent: calc(5px * 3); }
 #kvqmnalelw .gt_indent_4 { text-indent: calc(5px * 4); }
 #kvqmnalelw .gt_indent_5 { text-indent: calc(5px * 5); }
 #kvqmnalelw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kvqmnalelw .gt_row_group_first td { border-top-width: 2px; }
 #kvqmnalelw .gt_row_group_first th { border-top-width: 2px; }
 #kvqmnalelw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kvqmnalelw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kvqmnalelw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kvqmnalelw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kvqmnalelw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kvqmnalelw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kvqmnalelw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kvqmnalelw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kvqmnalelw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kvqmnalelw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kvqmnalelw .gt_left { text-align: left; }
 #kvqmnalelw .gt_center { text-align: center; }
 #kvqmnalelw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kvqmnalelw .gt_font_normal { font-weight: normal; }
 #kvqmnalelw .gt_font_bold { font-weight: bold; }
 #kvqmnalelw .gt_font_italic { font-style: italic; }
 #kvqmnalelw .gt_super { font-size: 65%; }
 #kvqmnalelw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kvqmnalelw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kvqmnalelw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kvqmnalelw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kvqmnalelw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kvqmnalelw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_title gt_font_normal">Our Contacts in Australia</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="name_given" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">First Name</th>
<th id="address" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Address</th>
<th id="city" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">City</th>
<th id="state_prov" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">State</th>
<th id="postcode" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Postcode</th>
<th id="country" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Country</th>
<th id="email_addr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Email</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">Christison</th>
<td class="gt_row gt_left">Milla</td>
<td class="gt_row gt_left">34 McGregor Street</td>
<td class="gt_row gt_left">Kinalung</td>
<td class="gt_row gt_left">NSW</td>
<td class="gt_row gt_left">2880</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[milla_c@example.com](mailto:milla_c@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Stead</th>
<td class="gt_row gt_left">Alannah</td>
<td class="gt_row gt_left">44 Mt Berryman Road</td>
<td class="gt_row gt_left">Ropeley</td>
<td class="gt_row gt_left">QLD</td>
<td class="gt_row gt_left">4343</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[alannahstead@example.com](mailto:alannahstead@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Fitzhardinge</th>
<td class="gt_row gt_left">Lucas</td>
<td class="gt_row gt_left">88 Dossiter Street</td>
<td class="gt_row gt_left">Waterloo</td>
<td class="gt_row gt_left">TAS</td>
<td class="gt_row gt_left">7109</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[lucas_fitz@example.com](mailto:lucas_fitz@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Goldhar</th>
<td class="gt_row gt_left">Lucinda</td>
<td class="gt_row gt_left">24 Settlement Road</td>
<td class="gt_row gt_left">Dargo</td>
<td class="gt_row gt_left">VIC</td>
<td class="gt_row gt_left">3862</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[lucinda_g@example.com](mailto:lucinda_g@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Dearth</th>
<td class="gt_row gt_left">Alexis</td>
<td class="gt_row gt_left">60 Sunnyside Road</td>
<td class="gt_row gt_left">Taylorville</td>
<td class="gt_row gt_left">SA</td>
<td class="gt_row gt_left">5330</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[alexisdearth@example.com](mailto:alexisdearth@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Hansen</th>
<td class="gt_row gt_left">Christopher</td>
<td class="gt_row gt_left">99 Weemala Avenue</td>
<td class="gt_row gt_left">Gooloogong</td>
<td class="gt_row gt_left">NSW</td>
<td class="gt_row gt_left">2805</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[chrishansen85@example.com](mailto:chrishansen85@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Kaczmarek</th>
<td class="gt_row gt_left">Scott</td>
<td class="gt_row gt_left">94 Peninsula Drive</td>
<td class="gt_row gt_left">Illawong</td>
<td class="gt_row gt_left">NSW</td>
<td class="gt_row gt_left">2234</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[scott_kaczmarek@example.com](mailto:scott_kaczmarek@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Pugliesi</th>
<td class="gt_row gt_left">Brandon</td>
<td class="gt_row gt_left">83 McDowall Street</td>
<td class="gt_row gt_left">Balmoral Ridge</td>
<td class="gt_row gt_left">QLD</td>
<td class="gt_row gt_left">4552</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[brandon_pugliesi@example.com](mailto:brandon_pugliesi@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Bremer</th>
<td class="gt_row gt_left">Rachel</td>
<td class="gt_row gt_left">80 Argyle Street</td>
<td class="gt_row gt_left">Stratford</td>
<td class="gt_row gt_left">NSW</td>
<td class="gt_row gt_left">2422</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[rachel_bremer@example.com](mailto:rachel_bremer@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Kerferd</th>
<td class="gt_row gt_left">Kaitlyn</td>
<td class="gt_row gt_left">15 Souttar Terrace</td>
<td class="gt_row gt_left">Kingsley</td>
<td class="gt_row gt_left">WA</td>
<td class="gt_row gt_left">6026</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[kaitlyn_kerferd@example.com](mailto:kaitlyn_kerferd@example.com)</span></td>
</tr>
</tbody>
</table>


We can use `display_name=` with a callable to show just the local part of the email address before the `@` sign.


``` python
(
    GT(peeps_aus, rowname_col="name_family")
    .tab_header(title="Our Contacts in Australia")
    .fmt_email(
        columns="email_addr",
        display_name=lambda x: x.split("@")[0],
        color="gray25",
    )
    .cols_label(
        name_given="First Name",
        address="Address",
        city="City",
        state_prov="State",
        postcode="Postcode",
        country="Country",
        email_addr="Email",
    )
)
```


<style>
#iucjrhxttp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iucjrhxttp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iucjrhxttp p { margin: 0; padding: 0; }
 #iucjrhxttp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #iucjrhxttp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iucjrhxttp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iucjrhxttp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iucjrhxttp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iucjrhxttp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iucjrhxttp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iucjrhxttp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iucjrhxttp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iucjrhxttp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iucjrhxttp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iucjrhxttp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iucjrhxttp .gt_spanner_row { border-bottom-style: hidden; }
 #iucjrhxttp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iucjrhxttp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #iucjrhxttp .gt_from_md> :first-child { margin-top: 0; }
 #iucjrhxttp .gt_from_md> :last-child { margin-bottom: 0; }
 #iucjrhxttp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #iucjrhxttp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #iucjrhxttp .gt_indent_1 { text-indent: 5px; }
 #iucjrhxttp .gt_indent_2 { text-indent: calc(5px * 2); }
 #iucjrhxttp .gt_indent_3 { text-indent: calc(5px * 3); }
 #iucjrhxttp .gt_indent_4 { text-indent: calc(5px * 4); }
 #iucjrhxttp .gt_indent_5 { text-indent: calc(5px * 5); }
 #iucjrhxttp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iucjrhxttp .gt_row_group_first td { border-top-width: 2px; }
 #iucjrhxttp .gt_row_group_first th { border-top-width: 2px; }
 #iucjrhxttp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #iucjrhxttp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iucjrhxttp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iucjrhxttp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #iucjrhxttp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iucjrhxttp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iucjrhxttp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iucjrhxttp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iucjrhxttp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iucjrhxttp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iucjrhxttp .gt_left { text-align: left; }
 #iucjrhxttp .gt_center { text-align: center; }
 #iucjrhxttp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iucjrhxttp .gt_font_normal { font-weight: normal; }
 #iucjrhxttp .gt_font_bold { font-weight: bold; }
 #iucjrhxttp .gt_font_italic { font-style: italic; }
 #iucjrhxttp .gt_super { font-size: 65%; }
 #iucjrhxttp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iucjrhxttp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #iucjrhxttp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iucjrhxttp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iucjrhxttp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iucjrhxttp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_title gt_font_normal">Our Contacts in Australia</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="name_given" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">First Name</th>
<th id="address" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Address</th>
<th id="city" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">City</th>
<th id="state_prov" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">State</th>
<th id="postcode" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Postcode</th>
<th id="country" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Country</th>
<th id="email_addr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Email</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">Christison</th>
<td class="gt_row gt_left">Milla</td>
<td class="gt_row gt_left">34 McGregor Street</td>
<td class="gt_row gt_left">Kinalung</td>
<td class="gt_row gt_left">NSW</td>
<td class="gt_row gt_left">2880</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[milla_c](mailto:milla_c@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Stead</th>
<td class="gt_row gt_left">Alannah</td>
<td class="gt_row gt_left">44 Mt Berryman Road</td>
<td class="gt_row gt_left">Ropeley</td>
<td class="gt_row gt_left">QLD</td>
<td class="gt_row gt_left">4343</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[alannahstead](mailto:alannahstead@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Fitzhardinge</th>
<td class="gt_row gt_left">Lucas</td>
<td class="gt_row gt_left">88 Dossiter Street</td>
<td class="gt_row gt_left">Waterloo</td>
<td class="gt_row gt_left">TAS</td>
<td class="gt_row gt_left">7109</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[lucas_fitz](mailto:lucas_fitz@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Goldhar</th>
<td class="gt_row gt_left">Lucinda</td>
<td class="gt_row gt_left">24 Settlement Road</td>
<td class="gt_row gt_left">Dargo</td>
<td class="gt_row gt_left">VIC</td>
<td class="gt_row gt_left">3862</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[lucinda_g](mailto:lucinda_g@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Dearth</th>
<td class="gt_row gt_left">Alexis</td>
<td class="gt_row gt_left">60 Sunnyside Road</td>
<td class="gt_row gt_left">Taylorville</td>
<td class="gt_row gt_left">SA</td>
<td class="gt_row gt_left">5330</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[alexisdearth](mailto:alexisdearth@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Hansen</th>
<td class="gt_row gt_left">Christopher</td>
<td class="gt_row gt_left">99 Weemala Avenue</td>
<td class="gt_row gt_left">Gooloogong</td>
<td class="gt_row gt_left">NSW</td>
<td class="gt_row gt_left">2805</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[chrishansen85](mailto:chrishansen85@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Kaczmarek</th>
<td class="gt_row gt_left">Scott</td>
<td class="gt_row gt_left">94 Peninsula Drive</td>
<td class="gt_row gt_left">Illawong</td>
<td class="gt_row gt_left">NSW</td>
<td class="gt_row gt_left">2234</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[scott_kaczmarek](mailto:scott_kaczmarek@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Pugliesi</th>
<td class="gt_row gt_left">Brandon</td>
<td class="gt_row gt_left">83 McDowall Street</td>
<td class="gt_row gt_left">Balmoral Ridge</td>
<td class="gt_row gt_left">QLD</td>
<td class="gt_row gt_left">4552</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[brandon_pugliesi](mailto:brandon_pugliesi@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Bremer</th>
<td class="gt_row gt_left">Rachel</td>
<td class="gt_row gt_left">80 Argyle Street</td>
<td class="gt_row gt_left">Stratford</td>
<td class="gt_row gt_left">NSW</td>
<td class="gt_row gt_left">2422</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[rachel_bremer](mailto:rachel_bremer@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Kerferd</th>
<td class="gt_row gt_left">Kaitlyn</td>
<td class="gt_row gt_left">15 Souttar Terrace</td>
<td class="gt_row gt_left">Kingsley</td>
<td class="gt_row gt_left">WA</td>
<td class="gt_row gt_left">6026</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[kaitlyn_kerferd](mailto:kaitlyn_kerferd@example.com)</span></td>
</tr>
</tbody>
</table>


Button-styled email links are also supported.


``` python
(
    GT(peeps_aus.head(5), rowname_col="name_family")
    .tab_header(title="Contact Us")
    .fmt_email(
        columns="email_addr",
        display_name="Send Email",
        as_button=True,
        button_fill="#228B22",
    )
    .cols_label(
        name_given="First Name",
        address="Address",
        city="City",
        state_prov="State",
        postcode="Postcode",
        country="Country",
        email_addr="Email",
    )
)
```


<style>
#gpqzqefzav table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gpqzqefzav thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gpqzqefzav p { margin: 0; padding: 0; }
 #gpqzqefzav .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gpqzqefzav .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gpqzqefzav .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gpqzqefzav .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gpqzqefzav .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gpqzqefzav .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gpqzqefzav .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gpqzqefzav .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gpqzqefzav .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gpqzqefzav .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gpqzqefzav .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gpqzqefzav .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gpqzqefzav .gt_spanner_row { border-bottom-style: hidden; }
 #gpqzqefzav .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gpqzqefzav .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gpqzqefzav .gt_from_md> :first-child { margin-top: 0; }
 #gpqzqefzav .gt_from_md> :last-child { margin-bottom: 0; }
 #gpqzqefzav .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gpqzqefzav .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gpqzqefzav .gt_indent_1 { text-indent: 5px; }
 #gpqzqefzav .gt_indent_2 { text-indent: calc(5px * 2); }
 #gpqzqefzav .gt_indent_3 { text-indent: calc(5px * 3); }
 #gpqzqefzav .gt_indent_4 { text-indent: calc(5px * 4); }
 #gpqzqefzav .gt_indent_5 { text-indent: calc(5px * 5); }
 #gpqzqefzav .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gpqzqefzav .gt_row_group_first td { border-top-width: 2px; }
 #gpqzqefzav .gt_row_group_first th { border-top-width: 2px; }
 #gpqzqefzav .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gpqzqefzav .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gpqzqefzav .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gpqzqefzav .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gpqzqefzav .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gpqzqefzav .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gpqzqefzav .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gpqzqefzav .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gpqzqefzav .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gpqzqefzav .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gpqzqefzav .gt_left { text-align: left; }
 #gpqzqefzav .gt_center { text-align: center; }
 #gpqzqefzav .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gpqzqefzav .gt_font_normal { font-weight: normal; }
 #gpqzqefzav .gt_font_bold { font-weight: bold; }
 #gpqzqefzav .gt_font_italic { font-style: italic; }
 #gpqzqefzav .gt_super { font-size: 65%; }
 #gpqzqefzav .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gpqzqefzav .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gpqzqefzav .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gpqzqefzav .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gpqzqefzav .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gpqzqefzav .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_title gt_font_normal">Contact Us</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="name_given" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">First Name</th>
<th id="address" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Address</th>
<th id="city" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">City</th>
<th id="state_prov" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">State</th>
<th id="postcode" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Postcode</th>
<th id="country" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Country</th>
<th id="email_addr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Email</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">Christison</th>
<td class="gt_row gt_left">Milla</td>
<td class="gt_row gt_left">34 McGregor Street</td>
<td class="gt_row gt_left">Kinalung</td>
<td class="gt_row gt_left">NSW</td>
<td class="gt_row gt_left">2880</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[Send Email](mailto:milla_c@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Stead</th>
<td class="gt_row gt_left">Alannah</td>
<td class="gt_row gt_left">44 Mt Berryman Road</td>
<td class="gt_row gt_left">Ropeley</td>
<td class="gt_row gt_left">QLD</td>
<td class="gt_row gt_left">4343</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[Send Email](mailto:alannahstead@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Fitzhardinge</th>
<td class="gt_row gt_left">Lucas</td>
<td class="gt_row gt_left">88 Dossiter Street</td>
<td class="gt_row gt_left">Waterloo</td>
<td class="gt_row gt_left">TAS</td>
<td class="gt_row gt_left">7109</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[Send Email](mailto:lucas_fitz@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Goldhar</th>
<td class="gt_row gt_left">Lucinda</td>
<td class="gt_row gt_left">24 Settlement Road</td>
<td class="gt_row gt_left">Dargo</td>
<td class="gt_row gt_left">VIC</td>
<td class="gt_row gt_left">3862</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[Send Email](mailto:lucinda_g@example.com)</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Dearth</th>
<td class="gt_row gt_left">Alexis</td>
<td class="gt_row gt_left">60 Sunnyside Road</td>
<td class="gt_row gt_left">Taylorville</td>
<td class="gt_row gt_left">SA</td>
<td class="gt_row gt_left">5330</td>
<td class="gt_row gt_left">AUS</td>
<td class="gt_row gt_left"><span style="white-space:pre;">[Send Email](mailto:alexisdearth@example.com)</span></td>
</tr>
</tbody>
</table>

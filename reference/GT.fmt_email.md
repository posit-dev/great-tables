# GT.fmt_email()

Format values as email links.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_formats.py#L3956-L4162)

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

The [`fmt_email()`](../reference/GT.fmt_email.md#great_tables.GT.fmt_email) method transforms email addresses in the table body into clickable `mailto:` links. Like [`fmt_url()`](../reference/GT.fmt_url.md#great_tables.GT.fmt_url), the links can be styled as buttons or as plain underlined text, with customizable colors.

In LaTeX output, the links are written with the `href` command (so the **hyperref** package needs to be loaded) and the styling options only apply to HTML output.

## Parameters

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`display_name: str | Callable[[str], str] | None = None`  
An optional display name to use instead of the raw email address. If a string is provided, it will be used as the visible text for all links. If a callable is provided, it will be called with the email address and should return the display text.

`as_button: bool = False`  
Should the link be styled as a button? By default this is `False`.

`color: str = "auto"`  
The color of the link text. The default `"auto"` uses `"#008B8B"` (dark cyan) for regular links and `"#FFFFFF"` (white) for buttons. Any CSS color name or hex value can be used.

`show_underline: str | bool = "auto"`  
Should the link be underlined? The default `"auto"` uses `True` for regular links and `False` for buttons. Set explicitly to `True` or `False` to override.

`button_fill: str = "auto"`  
The background color for button-style links. The default `"auto"` uses `"#4682B4"` (steel blue). Only used when `as_button=True`.

`button_width: str | None = None`  
The width of the button. Should be a CSS width string (e.g., `"150px"`). By default buttons size to their content.

`button_outline: str | None = None`  
The CSS outline for the button (e.g., `"2px solid #ccc"`). By default, a light gray outline is automatically added when the button fill color is very light, and hidden otherwise.

`target: str | None = "_blank"`  
The `target` attribute for the anchor element. Defaults to `"_blank"` to open links in a new tab. Set to `None` to open in the same tab.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Using a subset of the [peeps](../reference/data.peeps.md#great_tables.data.peeps) dataset filtered to contacts in Australia, let's format the `email_addr` column as email links.

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

| Our Contacts in Australia |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
|  | First Name | Address | City | State | Postcode | Country | Email |
| Christison | Milla | 34 McGregor Street | Kinalung | NSW | 2880 | AUS | <milla_c@example.com> |
| Stead | Alannah | 44 Mt Berryman Road | Ropeley | QLD | 4343 | AUS | <alannahstead@example.com> |
| Fitzhardinge | Lucas | 88 Dossiter Street | Waterloo | TAS | 7109 | AUS | <lucas_fitz@example.com> |
| Goldhar | Lucinda | 24 Settlement Road | Dargo | VIC | 3862 | AUS | <lucinda_g@example.com> |
| Dearth | Alexis | 60 Sunnyside Road | Taylorville | SA | 5330 | AUS | <alexisdearth@example.com> |
| Hansen | Christopher | 99 Weemala Avenue | Gooloogong | NSW | 2805 | AUS | <chrishansen85@example.com> |
| Kaczmarek | Scott | 94 Peninsula Drive | Illawong | NSW | 2234 | AUS | <scott_kaczmarek@example.com> |
| Pugliesi | Brandon | 83 McDowall Street | Balmoral Ridge | QLD | 4552 | AUS | <brandon_pugliesi@example.com> |
| Bremer | Rachel | 80 Argyle Street | Stratford | NSW | 2422 | AUS | <rachel_bremer@example.com> |
| Kerferd | Kaitlyn | 15 Souttar Terrace | Kingsley | WA | 6026 | AUS | <kaitlyn_kerferd@example.com> |

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

| Our Contacts in Australia |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
|  | First Name | Address | City | State | Postcode | Country | Email |
| Christison | Milla | 34 McGregor Street | Kinalung | NSW | 2880 | AUS | [milla_c](mailto:milla_c@example.com) |
| Stead | Alannah | 44 Mt Berryman Road | Ropeley | QLD | 4343 | AUS | [alannahstead](mailto:alannahstead@example.com) |
| Fitzhardinge | Lucas | 88 Dossiter Street | Waterloo | TAS | 7109 | AUS | [lucas_fitz](mailto:lucas_fitz@example.com) |
| Goldhar | Lucinda | 24 Settlement Road | Dargo | VIC | 3862 | AUS | [lucinda_g](mailto:lucinda_g@example.com) |
| Dearth | Alexis | 60 Sunnyside Road | Taylorville | SA | 5330 | AUS | [alexisdearth](mailto:alexisdearth@example.com) |
| Hansen | Christopher | 99 Weemala Avenue | Gooloogong | NSW | 2805 | AUS | [chrishansen85](mailto:chrishansen85@example.com) |
| Kaczmarek | Scott | 94 Peninsula Drive | Illawong | NSW | 2234 | AUS | [scott_kaczmarek](mailto:scott_kaczmarek@example.com) |
| Pugliesi | Brandon | 83 McDowall Street | Balmoral Ridge | QLD | 4552 | AUS | [brandon_pugliesi](mailto:brandon_pugliesi@example.com) |
| Bremer | Rachel | 80 Argyle Street | Stratford | NSW | 2422 | AUS | [rachel_bremer](mailto:rachel_bremer@example.com) |
| Kerferd | Kaitlyn | 15 Souttar Terrace | Kingsley | WA | 6026 | AUS | [kaitlyn_kerferd](mailto:kaitlyn_kerferd@example.com) |

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

| Contact Us |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
|  | First Name | Address | City | State | Postcode | Country | Email |
| Christison | Milla | 34 McGregor Street | Kinalung | NSW | 2880 | AUS | [Send Email](mailto:milla_c@example.com) |
| Stead | Alannah | 44 Mt Berryman Road | Ropeley | QLD | 4343 | AUS | [Send Email](mailto:alannahstead@example.com) |
| Fitzhardinge | Lucas | 88 Dossiter Street | Waterloo | TAS | 7109 | AUS | [Send Email](mailto:lucas_fitz@example.com) |
| Goldhar | Lucinda | 24 Settlement Road | Dargo | VIC | 3862 | AUS | [Send Email](mailto:lucinda_g@example.com) |
| Dearth | Alexis | 60 Sunnyside Road | Taylorville | SA | 5330 | AUS | [Send Email](mailto:alexisdearth@example.com) |

# Recreating Septa Transit Timetables in Python

Recently, Rich and I were poking around transit data, and we were struck by the amount of structuring that goes into transit timetables.

For example, consider this weekend rail schedule table from SEPTA, Philadelphia's transit agency.

<img src="./example-timetable.png" class="img-fluid" style="max-width: 700px; display: block; margin-left: auto; margin-right: auto;" />

Notice these big pieces:

- The vertical text on the left indicating trains are traveling "TO CENTER CITY".
- The blue header, and spanner columns ("Services" and "Train Number") grouping related columns.
- The striped background for easier reading. Also the black background indicating stations in Center City (the urban core).

Tables like this often have to be created in tools like Illustrator, and updated by hand. At the same time, when agencies automate table creation, they often sacrifice a lot of the assistive features and helpful affordances of the table.

We set out to recreate this table in Great Tables (and by we I mean 99% Rich). In this post, I'll walk quickly through how we recreated it, and share some other examples of transit timetables in the wild. For the theory behind why tables like this are useful, see [The Design Philosophy of Great Tables](../../blog/design-philosophy/index.md).


# The final result

Here's a look at our quick version in Great Tables. In this post we'll walk through quickly how we created it, but wanted to treat you to the final result up front! Note that the table is fully in HTML for accessibility.


Code

``` python
from great_tables import GT, html, style, loc, google_font
import polars as pl
import polars.selectors as cs

stops = pl.read_csv("chw-stops.csv")
times = pl.read_csv("times.csv")

stop_times = times.join(other=stops, on="stop_name", maintain_order="left").select(
    pl.lit("To Center City").alias("direction"), pl.col("*")
)


def h_m_p(s):
    h, m, _ = [int(part) for part in s.split(":")]
    ap = "a"

    if h > 12:
        h -= 12
        ap = "p"
    return f"{h}:{m:02d}{ap}"


def tick(b):
    return "✓" if b else ""


transit_table = (
    GT(stop_times)
    .tab_stub(groupname_col="direction")
    .tab_header("Saturdays, Sundays, and Major Holidays")
    .cols_hide(columns=["stop_url", "zone_id", "stop_desc", "stop_lat", "stop_lon", "stop_id"])
    .fmt(h_m_p, columns=cs.matches(r"^[0-9]{4}$"))
    .fmt(tick, columns=cs.starts_with("service_"))
    .cols_label(
        stop_name="Stations",
        service_access="A",
        service_cash="C",
        service_park="P",
        fare_zone=html("Fare<br>Zone"),
    )
    .tab_spanner(label="Services", columns=cs.starts_with("service_"))
    .tab_spanner(label="Train Number", columns=cs.matches(r"^[0-9]{4}$"))
    .cols_move_to_start("fare_zone")
    .cols_move_to_start(cs.starts_with("service_"))
    .cols_width(cases={c: "20px" for c in stop_times.columns if c.startswith("service_")})
    .cols_width(cases={c: "60px" for c in stop_times.columns if c.startswith("8")})
    .opt_row_striping(row_striping=True)
    .cols_align(align="center", columns="fare_zone")
    .cols_align(align="right", columns=cs.matches(r"^[0-9]{4}$"))
    # style header
    .tab_style(
        locations=loc.header(),
        style=style.css(
            "background-color: rgb(66, 99, 128) !important; color: white !important; font-size: 24px !important; font-weight: bold !important; border-width: 0px !important;",
        ),
    )
    # style vertical text on left
    .tab_style(
        locations=loc.row_groups(),
        # TODO: rotate text vertically
        style=style.css(
            "writing-mode: sideways-lr; padding-bottom: 25% !important; font-size: 24px !important; font-weight: bold !important; text-transform: uppercase !important;"
        ),
    )
    .tab_style(
        style=style.css(
            "background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important;"
        ),
        locations=loc.body(columns=None, rows=list(range(-4, -1))),
    )
    .tab_style(
        style=style.css(
            """
                border-top: none !important;
                border-bottom: none !important;
                border-right: solid white 2px !important;
                color: white !important;
            """
        ),
        locations=loc.body(columns=~cs.matches(r"^[0-9]{4}$"), rows=list(range(-4, -1))),
    )
    .tab_style(
        style=style.css("border-right: solid black 2px !important;"),
        locations=loc.body(columns=~cs.matches(r"^[0-9]{4}$"), rows=list(range(0, 10)) + [13]),
    )
    .tab_options(
        row_striping_background_color="#A9A9A9",
        row_group_as_column=True,
    )
    .opt_table_outline()
    .opt_table_font(font=google_font("IBM Plex Sans"))
)

transit_table
```


    /home/runner/work/great-tables/great-tables/great_tables/_render_checks.py:37: RenderWarning: Rendering table with .cols_width() in Quarto may result in unexpected behavior. This is because Quarto performs custom table processing. Either use all percentage widths, or set .tab_options(quarto_disable_processing=True) to disable Quarto table processing.
      warnings.warn(


<table class="gt_table" style="table-layout: fixed;" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="14" class="gt_heading gt_title gt_font_normal" style="background-color: rgb(66, 99, 128) !important; color: white !important; font-size: 24px !important; font-weight: bold !important; border-width: 0px !important">Saturdays, Sundays, and Major Holidays</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th colspan="3" id="Services" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Services</th>
<th rowspan="2" id="fare_zone" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">Fare<br />
Zone</th>
<th rowspan="2" id="stop_name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Stations</th>
<th colspan="8" id="Train-Number" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Train Number</th>
</tr>
<tr class="gt_col_headings">
<th id="service_access" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">A</th>
<th id="service_cash" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">C</th>
<th id="service_park" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">P</th>
<th id="8210" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8210</th>
<th id="8716" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8716</th>
<th id="8318" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8318</th>
<th id="8322" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8322</th>
<th id="8338" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8338</th>
<th id="8242" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8242</th>
<th id="8750" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8750</th>
<th id="8756" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8756</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_row_group_first">
<th rowspan="14" class="gt_row gt_left gt_stub_row_group" style="writing-mode: sideways-lr; padding-bottom: 25% !important; font-size: 24px !important; font-weight: bold !important; text-transform: uppercase !important">To Center City</th>
<td class="gt_row gt_right" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_center" style="border-right: solid black 2px !important">2</td>
<td class="gt_row gt_left" style="border-right: solid black 2px !important">Chestnut Hill West</td>
<td class="gt_row gt_right">6:51a</td>
<td class="gt_row gt_right">8:08a</td>
<td class="gt_row gt_right">8:49a</td>
<td class="gt_row gt_right">9:49a</td>
<td class="gt_row gt_right">1:52p</td>
<td class="gt_row gt_right">2:49p</td>
<td class="gt_row gt_right">4:48p</td>
<td class="gt_row gt_right">6:20p</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_center gt_striped" style="border-right: solid black 2px !important">2</td>
<td class="gt_row gt_left gt_striped" style="border-right: solid black 2px !important">Highland</td>
<td class="gt_row gt_right gt_striped">6:52a</td>
<td class="gt_row gt_right gt_striped">8:09a</td>
<td class="gt_row gt_right gt_striped">8:50a</td>
<td class="gt_row gt_right gt_striped">9:50a</td>
<td class="gt_row gt_right gt_striped">1:53p</td>
<td class="gt_row gt_right gt_striped">2:50p</td>
<td class="gt_row gt_right gt_striped">4:49p</td>
<td class="gt_row gt_right gt_striped">6:21p</td>
</tr>
<tr>
<td class="gt_row gt_right" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_center" style="border-right: solid black 2px !important">1</td>
<td class="gt_row gt_left" style="border-right: solid black 2px !important">St. Martins</td>
<td class="gt_row gt_right">6:54a</td>
<td class="gt_row gt_right">8:11a</td>
<td class="gt_row gt_right">8:52a</td>
<td class="gt_row gt_right">9:52a</td>
<td class="gt_row gt_right">1:55p</td>
<td class="gt_row gt_right">2:52p</td>
<td class="gt_row gt_right">4:51p</td>
<td class="gt_row gt_right">6:23p</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_center gt_striped" style="border-right: solid black 2px !important">1</td>
<td class="gt_row gt_left gt_striped" style="border-right: solid black 2px !important">Richard Allen Lane</td>
<td class="gt_row gt_right gt_striped">6:56a</td>
<td class="gt_row gt_right gt_striped">8:13a</td>
<td class="gt_row gt_right gt_striped">8:54a</td>
<td class="gt_row gt_right gt_striped">9:54a</td>
<td class="gt_row gt_right gt_striped">1:57p</td>
<td class="gt_row gt_right gt_striped">2:54p</td>
<td class="gt_row gt_right gt_striped">4:53p</td>
<td class="gt_row gt_right gt_striped">6:25p</td>
</tr>
<tr>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_center" style="border-right: solid black 2px !important">1</td>
<td class="gt_row gt_left" style="border-right: solid black 2px !important">Carpenter</td>
<td class="gt_row gt_right">6:58a</td>
<td class="gt_row gt_right">8:15a</td>
<td class="gt_row gt_right">8:56a</td>
<td class="gt_row gt_right">9:56a</td>
<td class="gt_row gt_right">1:59p</td>
<td class="gt_row gt_right">2:56p</td>
<td class="gt_row gt_right">4:55p</td>
<td class="gt_row gt_right">6:27p</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_center gt_striped" style="border-right: solid black 2px !important">1</td>
<td class="gt_row gt_left gt_striped" style="border-right: solid black 2px !important">Upsal</td>
<td class="gt_row gt_right gt_striped">7:00a</td>
<td class="gt_row gt_right gt_striped">8:17a</td>
<td class="gt_row gt_right gt_striped">8:58a</td>
<td class="gt_row gt_right gt_striped">9:58a</td>
<td class="gt_row gt_right gt_striped">2:01p</td>
<td class="gt_row gt_right gt_striped">2:58p</td>
<td class="gt_row gt_right gt_striped">4:57p</td>
<td class="gt_row gt_right gt_striped">6:29p</td>
</tr>
<tr>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_center" style="border-right: solid black 2px !important">C</td>
<td class="gt_row gt_left" style="border-right: solid black 2px !important">Tulpehocken</td>
<td class="gt_row gt_right">7:02a</td>
<td class="gt_row gt_right">8:19a</td>
<td class="gt_row gt_right">9:00a</td>
<td class="gt_row gt_right">10:00a</td>
<td class="gt_row gt_right">2:03p</td>
<td class="gt_row gt_right">3:00p</td>
<td class="gt_row gt_right">4:59p</td>
<td class="gt_row gt_right">6:31p</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_center gt_striped" style="border-right: solid black 2px !important">C</td>
<td class="gt_row gt_left gt_striped" style="border-right: solid black 2px !important">Chelten Avenue</td>
<td class="gt_row gt_right gt_striped">7:04a</td>
<td class="gt_row gt_right gt_striped">8:21a</td>
<td class="gt_row gt_right gt_striped">9:02a</td>
<td class="gt_row gt_right gt_striped">10:02a</td>
<td class="gt_row gt_right gt_striped">2:05p</td>
<td class="gt_row gt_right gt_striped">3:02p</td>
<td class="gt_row gt_right gt_striped">5:01p</td>
<td class="gt_row gt_right gt_striped">6:33p</td>
</tr>
<tr>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_center" style="border-right: solid black 2px !important">C</td>
<td class="gt_row gt_left" style="border-right: solid black 2px !important">Queen Lane</td>
<td class="gt_row gt_right">7:06a</td>
<td class="gt_row gt_right">8:23a</td>
<td class="gt_row gt_right">9:04a</td>
<td class="gt_row gt_right">10:04a</td>
<td class="gt_row gt_right">2:07p</td>
<td class="gt_row gt_right">3:04p</td>
<td class="gt_row gt_right">5:03p</td>
<td class="gt_row gt_right">6:35p</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_center gt_striped" style="border-right: solid black 2px !important">C</td>
<td class="gt_row gt_left gt_striped" style="border-right: solid black 2px !important">North Philadelphia</td>
<td class="gt_row gt_right gt_striped">7:12a</td>
<td class="gt_row gt_right gt_striped">8:29a</td>
<td class="gt_row gt_right gt_striped">9:12a</td>
<td class="gt_row gt_right gt_striped">10:12a</td>
<td class="gt_row gt_right gt_striped">2:15p</td>
<td class="gt_row gt_right gt_striped">3:12p</td>
<td class="gt_row gt_right gt_striped">5:09p</td>
<td class="gt_row gt_right gt_striped">6:41p</td>
</tr>
<tr>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">✓</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important"></td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">✓</td>
<td class="gt_row gt_center" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">2</td>
<td class="gt_row gt_left" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">Gray 30th Street</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">7:23a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">8:42a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">9:23a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">10:23a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">2:26p</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">3:23p</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">5:20p</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">6:54p</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important"></td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important"></td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">✓</td>
<td class="gt_row gt_center gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">2</td>
<td class="gt_row gt_left gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">Suburban Station</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">7:28a</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">8:47a</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">9:28a</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">10:28a</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">2:31p</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">3:28p</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">5:25p</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">6:59p</td>
</tr>
<tr>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important"></td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important"></td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">✓</td>
<td class="gt_row gt_center" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">2</td>
<td class="gt_row gt_left" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">Jefferson Station</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">7:33a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">8:52a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">9:33a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">10:33a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">2:36p</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">3:33p</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">5:30p</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">7:04p</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_center gt_striped" style="border-right: solid black 2px !important">2</td>
<td class="gt_row gt_left gt_striped" style="border-right: solid black 2px !important">Temple University</td>
<td class="gt_row gt_right gt_striped">7:37a</td>
<td class="gt_row gt_right gt_striped">8:57a</td>
<td class="gt_row gt_right gt_striped">9:37a</td>
<td class="gt_row gt_right gt_striped">10:37a</td>
<td class="gt_row gt_right gt_striped">2:40p</td>
<td class="gt_row gt_right gt_striped">3:37p</td>
<td class="gt_row gt_right gt_striped">5:35p</td>
<td class="gt_row gt_right gt_striped">7:08p</td>
</tr>
</tbody>
</table>


# Reading in stops and times

For this example, I simplified SEPTA's transit data down to two pieces:

- `chw-stops.csv` - detailed information about each stop location.
- `times.csv` - when a train arrives at a stop on the Chesnut Hill West line. Each row is a stop location, and each column is a trip (e.g. the 6:51am train).

To make the final table we joined these two together, to get the trips and stop information together.


``` python
import polars as pl

stops = pl.read_csv("chw-stops.csv")
times = pl.read_csv("times.csv")
```


Here's a quick preview of stops.


``` python
stops.select("stop_name", "service_access", "service_cash").head()
```


shape: (5, 3)

| stop_name            | service_access | service_cash |
|----------------------|----------------|--------------|
| str                  | i64            | i64          |
| "Gray 30th Street"   | 1              | 0            |
| "Suburban Station"   | 0              | 0            |
| "Jefferson Station"  | 0              | 0            |
| "Temple University"  | 1              | 0            |
| "Chestnut Hill West" | 0              | 0            |


Notice that the table above has the name of each stop, and a 1 or 0 in the `service_access` column to indicate whether the stop is wheelchair accessible. Note that a big challenge for this specific route is that sometimes boarding the train requires using steps, and sometimes the station requires using steps. For example, Chelton Ave (not shown) does not require steps to board the train, but the station itself is not wheelchair accessible because of steps to get to the platform.

Here's a quick preview of the times.


``` python
times.head(3)
```


shape: (3, 9)

| stop_name | 8210 | 8716 | 8318 | 8322 | 8338 | 8242 | 8750 | 8756 |
|----|----|----|----|----|----|----|----|----|
| str | str | str | str | str | str | str | str | str |
| "Chestnut Hill West" | "06:51:00" | "08:08:00" | "08:49:00" | "09:49:00" | "13:52:00" | "14:49:00" | "16:48:00" | "18:20:00" |
| "Highland" | "06:52:00" | "08:09:00" | "08:50:00" | "09:50:00" | "13:53:00" | "14:50:00" | "16:49:00" | "18:21:00" |
| "St. Martins" | "06:54:00" | "08:11:00" | "08:52:00" | "09:52:00" | "13:55:00" | "14:52:00" | "16:51:00" | "18:23:00" |


Notice that each trip is a column (i.e. a train leaving from Chesnut Hill West at a specific time), and each row is a stop. For example, the 8210 train is the 6:51am train. (Note that schedules and train numbers can change, so this data may be out of date).

Joining these together gives us `stop_times`, with trips and stop information on the columns.


``` python
stop_times = times.join(other=stops, on="stop_name", maintain_order="left").select(
    pl.lit("To Center City").alias("direction"), pl.col("*")
)

stop_times.head(3)
```


shape: (3, 20)

| direction | stop_name | 8210 | 8716 | 8318 | 8322 | 8338 | 8242 | 8750 | 8756 | service_access | service_cash | service_park | fare_zone | stop_id | stop_desc | stop_lat | stop_lon | zone_id | stop_url |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| str | str | str | str | str | str | str | str | str | str | i64 | i64 | i64 | str | i64 | str | f64 | f64 | str | str |
| "To Center City" | "Chestnut Hill West" | "06:51:00" | "08:08:00" | "08:49:00" | "09:49:00" | "13:52:00" | "14:49:00" | "16:48:00" | "18:20:00" | 0 | 0 | 1 | "2" | 90801 | null | 40.076389 | -75.208333 | "2S" | null |
| "To Center City" | "Highland" | "06:52:00" | "08:09:00" | "08:50:00" | "09:50:00" | "13:53:00" | "14:50:00" | "16:49:00" | "18:21:00" | 0 | 0 | 1 | "2" | 90802 | null | 40.070556 | -75.211111 | "2S" | null |
| "To Center City" | "St. Martins" | "06:54:00" | "08:11:00" | "08:52:00" | "09:52:00" | "13:55:00" | "14:52:00" | "16:51:00" | "18:23:00" | 0 | 0 | 1 | "1" | 90803 | null | 40.065833 | -75.204444 | "2S" | null |


Notice that in the table above, the first row tells us when each train leaves Chesnut Hill West, and information about the Chesnut Hill West stop.


# Creating the table

Below is the code for the table, with 5 key activities marked with comments. For example, the first is creating high level structure, like the header and the left-hand "To Center City" stub. Others include formatting in checkmarks, customizing columns (e.g. their width), and styling (e.g. setting background colors and fonts).

It's a lot to take in, but worth it!:


``` python
from great_tables import GT, html, style, loc, google_font
import polars as pl
import polars.selectors as cs


def h_m_p(s):
    h, m, _ = [int(part) for part in s.split(":")]
    ap = "a"

    if h > 12:
        h -= 12
        ap = "p"
    return f"{h}:{m:02d}{ap}"


def tick(b):
    return "✓" if b else ""


transit_table = (
    GT(stop_times)

    # Create left-hand stub, top header, and hide extra cols --------
    .tab_stub(groupname_col="direction")
    .tab_header("Saturdays, Sundays, and Major Holidays")
    .cols_hide(
        columns=["stop_url", "zone_id", "stop_desc", "stop_lat", "stop_lon", "stop_id"]
    )

    # custom functions for checkmarks and time formatting -----------
    .fmt(h_m_p, columns=cs.matches(r"^[0-9]{4}$"))
    .fmt(tick, columns=cs.starts_with("service_"))

    # relabel columns and add spanners (labels over columns) --------
    .cols_label(
        stop_name="Stations",
        service_access="A",
        service_cash="C",
        service_park="P",
        fare_zone=html("Fare<br>Zone"),
    )
    .tab_spanner(label="Services", columns=cs.starts_with("service_"))
    .tab_spanner(label="Train Number", columns=cs.matches(r"^[0-9]{4}$"))

    # move columns around and setting their width and alignment -----
    .cols_move_to_start("fare_zone")
    .cols_move_to_start(cs.starts_with("service_"))
    .cols_width(
        cases={c: "18px" for c in stop_times.columns if c.startswith("service_")}
    )
    .cols_width(cases={c: "60px" for c in stop_times.columns if c.startswith("8")})
    .cols_align(align="center", columns="fare_zone")
    .cols_align(align="right", columns=cs.matches(r"^[0-9]{4}$"))

    # styles: striping, vertical text, background colors, fonts -----
    # style header
    .tab_style(
        locations=loc.header(),
        style=style.css(
            "background-color: rgb(66, 99, 128) !important; color: white !important; font-size: 24px !important; font-weight: bold !important; border-width: 0px !important;",
        ),
    )
    # style vertical text on left
    .tab_style(
        locations=loc.row_groups(),
        style=style.css(
            "writing-mode: sideways-lr; padding-bottom: 25% !important; font-size: 24px !important; font-weight: bold !important; text-transform: uppercase !important;"
        ),
    )
    .tab_style(
        style=style.css(
            "background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important;"
        ),
        locations=loc.body(columns=None, rows=list(range(-4, -1))),
    )
    .tab_style(
        style=style.css(
            """
                border-top: none !important;
                border-bottom: none !important;
                border-right: solid white 2px !important;
                color: white !important;
            """
        ),
        locations=loc.body(
            columns=~cs.matches(r"^[0-9]{4}$"), rows=list(range(-4, -1))
        ),
    )
    .tab_style(
        style=style.css("border-right: solid black 2px !important;"),
        locations=loc.body(
            columns=~cs.matches(r"^[0-9]{4}$"), rows=list(range(0, 10)) + [13]
        ),
    )
    .tab_options(
        row_striping_background_color="#A9A9A9",
        row_group_as_column=True,
    )
    .opt_row_striping(row_striping=True)
    .opt_table_outline()
    .opt_table_font(font=google_font("IBM Plex Sans"))
)

transit_table
```


<table class="gt_table" style="table-layout: fixed;" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="14" class="gt_heading gt_title gt_font_normal" style="background-color: rgb(66, 99, 128) !important; color: white !important; font-size: 24px !important; font-weight: bold !important; border-width: 0px !important">Saturdays, Sundays, and Major Holidays</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th colspan="3" id="Services" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Services</th>
<th rowspan="2" id="fare_zone" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">Fare<br />
Zone</th>
<th rowspan="2" id="stop_name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Stations</th>
<th colspan="8" id="Train-Number" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Train Number</th>
</tr>
<tr class="gt_col_headings">
<th id="service_access" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">A</th>
<th id="service_cash" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">C</th>
<th id="service_park" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">P</th>
<th id="8210" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8210</th>
<th id="8716" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8716</th>
<th id="8318" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8318</th>
<th id="8322" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8322</th>
<th id="8338" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8338</th>
<th id="8242" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8242</th>
<th id="8750" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8750</th>
<th id="8756" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8756</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_row_group_first">
<th rowspan="14" class="gt_row gt_left gt_stub_row_group" style="writing-mode: sideways-lr; padding-bottom: 25% !important; font-size: 24px !important; font-weight: bold !important; text-transform: uppercase !important">To Center City</th>
<td class="gt_row gt_right" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_center" style="border-right: solid black 2px !important">2</td>
<td class="gt_row gt_left" style="border-right: solid black 2px !important">Chestnut Hill West</td>
<td class="gt_row gt_right">6:51a</td>
<td class="gt_row gt_right">8:08a</td>
<td class="gt_row gt_right">8:49a</td>
<td class="gt_row gt_right">9:49a</td>
<td class="gt_row gt_right">1:52p</td>
<td class="gt_row gt_right">2:49p</td>
<td class="gt_row gt_right">4:48p</td>
<td class="gt_row gt_right">6:20p</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_center gt_striped" style="border-right: solid black 2px !important">2</td>
<td class="gt_row gt_left gt_striped" style="border-right: solid black 2px !important">Highland</td>
<td class="gt_row gt_right gt_striped">6:52a</td>
<td class="gt_row gt_right gt_striped">8:09a</td>
<td class="gt_row gt_right gt_striped">8:50a</td>
<td class="gt_row gt_right gt_striped">9:50a</td>
<td class="gt_row gt_right gt_striped">1:53p</td>
<td class="gt_row gt_right gt_striped">2:50p</td>
<td class="gt_row gt_right gt_striped">4:49p</td>
<td class="gt_row gt_right gt_striped">6:21p</td>
</tr>
<tr>
<td class="gt_row gt_right" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_center" style="border-right: solid black 2px !important">1</td>
<td class="gt_row gt_left" style="border-right: solid black 2px !important">St. Martins</td>
<td class="gt_row gt_right">6:54a</td>
<td class="gt_row gt_right">8:11a</td>
<td class="gt_row gt_right">8:52a</td>
<td class="gt_row gt_right">9:52a</td>
<td class="gt_row gt_right">1:55p</td>
<td class="gt_row gt_right">2:52p</td>
<td class="gt_row gt_right">4:51p</td>
<td class="gt_row gt_right">6:23p</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_center gt_striped" style="border-right: solid black 2px !important">1</td>
<td class="gt_row gt_left gt_striped" style="border-right: solid black 2px !important">Richard Allen Lane</td>
<td class="gt_row gt_right gt_striped">6:56a</td>
<td class="gt_row gt_right gt_striped">8:13a</td>
<td class="gt_row gt_right gt_striped">8:54a</td>
<td class="gt_row gt_right gt_striped">9:54a</td>
<td class="gt_row gt_right gt_striped">1:57p</td>
<td class="gt_row gt_right gt_striped">2:54p</td>
<td class="gt_row gt_right gt_striped">4:53p</td>
<td class="gt_row gt_right gt_striped">6:25p</td>
</tr>
<tr>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_center" style="border-right: solid black 2px !important">1</td>
<td class="gt_row gt_left" style="border-right: solid black 2px !important">Carpenter</td>
<td class="gt_row gt_right">6:58a</td>
<td class="gt_row gt_right">8:15a</td>
<td class="gt_row gt_right">8:56a</td>
<td class="gt_row gt_right">9:56a</td>
<td class="gt_row gt_right">1:59p</td>
<td class="gt_row gt_right">2:56p</td>
<td class="gt_row gt_right">4:55p</td>
<td class="gt_row gt_right">6:27p</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_center gt_striped" style="border-right: solid black 2px !important">1</td>
<td class="gt_row gt_left gt_striped" style="border-right: solid black 2px !important">Upsal</td>
<td class="gt_row gt_right gt_striped">7:00a</td>
<td class="gt_row gt_right gt_striped">8:17a</td>
<td class="gt_row gt_right gt_striped">8:58a</td>
<td class="gt_row gt_right gt_striped">9:58a</td>
<td class="gt_row gt_right gt_striped">2:01p</td>
<td class="gt_row gt_right gt_striped">2:58p</td>
<td class="gt_row gt_right gt_striped">4:57p</td>
<td class="gt_row gt_right gt_striped">6:29p</td>
</tr>
<tr>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_center" style="border-right: solid black 2px !important">C</td>
<td class="gt_row gt_left" style="border-right: solid black 2px !important">Tulpehocken</td>
<td class="gt_row gt_right">7:02a</td>
<td class="gt_row gt_right">8:19a</td>
<td class="gt_row gt_right">9:00a</td>
<td class="gt_row gt_right">10:00a</td>
<td class="gt_row gt_right">2:03p</td>
<td class="gt_row gt_right">3:00p</td>
<td class="gt_row gt_right">4:59p</td>
<td class="gt_row gt_right">6:31p</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_center gt_striped" style="border-right: solid black 2px !important">C</td>
<td class="gt_row gt_left gt_striped" style="border-right: solid black 2px !important">Chelten Avenue</td>
<td class="gt_row gt_right gt_striped">7:04a</td>
<td class="gt_row gt_right gt_striped">8:21a</td>
<td class="gt_row gt_right gt_striped">9:02a</td>
<td class="gt_row gt_right gt_striped">10:02a</td>
<td class="gt_row gt_right gt_striped">2:05p</td>
<td class="gt_row gt_right gt_striped">3:02p</td>
<td class="gt_row gt_right gt_striped">5:01p</td>
<td class="gt_row gt_right gt_striped">6:33p</td>
</tr>
<tr>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_center" style="border-right: solid black 2px !important">C</td>
<td class="gt_row gt_left" style="border-right: solid black 2px !important">Queen Lane</td>
<td class="gt_row gt_right">7:06a</td>
<td class="gt_row gt_right">8:23a</td>
<td class="gt_row gt_right">9:04a</td>
<td class="gt_row gt_right">10:04a</td>
<td class="gt_row gt_right">2:07p</td>
<td class="gt_row gt_right">3:04p</td>
<td class="gt_row gt_right">5:03p</td>
<td class="gt_row gt_right">6:35p</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_center gt_striped" style="border-right: solid black 2px !important">C</td>
<td class="gt_row gt_left gt_striped" style="border-right: solid black 2px !important">North Philadelphia</td>
<td class="gt_row gt_right gt_striped">7:12a</td>
<td class="gt_row gt_right gt_striped">8:29a</td>
<td class="gt_row gt_right gt_striped">9:12a</td>
<td class="gt_row gt_right gt_striped">10:12a</td>
<td class="gt_row gt_right gt_striped">2:15p</td>
<td class="gt_row gt_right gt_striped">3:12p</td>
<td class="gt_row gt_right gt_striped">5:09p</td>
<td class="gt_row gt_right gt_striped">6:41p</td>
</tr>
<tr>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">✓</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important"></td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">✓</td>
<td class="gt_row gt_center" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">2</td>
<td class="gt_row gt_left" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">Gray 30th Street</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">7:23a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">8:42a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">9:23a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">10:23a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">2:26p</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">3:23p</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">5:20p</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">6:54p</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important"></td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important"></td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">✓</td>
<td class="gt_row gt_center gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">2</td>
<td class="gt_row gt_left gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">Suburban Station</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">7:28a</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">8:47a</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">9:28a</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">10:28a</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">2:31p</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">3:28p</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">5:25p</td>
<td class="gt_row gt_right gt_striped" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">6:59p</td>
</tr>
<tr>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important"></td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important"></td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">✓</td>
<td class="gt_row gt_center" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">2</td>
<td class="gt_row gt_left" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important; border-top: none !important; border-bottom: none !important; border-right: solid white 2px !important; color: white !important">Jefferson Station</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">7:33a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">8:52a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">9:33a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">10:33a</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">2:36p</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">3:33p</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">5:30p</td>
<td class="gt_row gt_right" style="background-color: black !important; color: white !important; border-top: none !important; border-bottom: none !important">7:04p</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important"></td>
<td class="gt_row gt_right gt_striped" style="border-right: solid black 2px !important">✓</td>
<td class="gt_row gt_center gt_striped" style="border-right: solid black 2px !important">2</td>
<td class="gt_row gt_left gt_striped" style="border-right: solid black 2px !important">Temple University</td>
<td class="gt_row gt_right gt_striped">7:37a</td>
<td class="gt_row gt_right gt_striped">8:57a</td>
<td class="gt_row gt_right gt_striped">9:37a</td>
<td class="gt_row gt_right gt_striped">10:37a</td>
<td class="gt_row gt_right gt_striped">2:40p</td>
<td class="gt_row gt_right gt_striped">3:37p</td>
<td class="gt_row gt_right gt_striped">5:35p</td>
<td class="gt_row gt_right gt_striped">7:08p</td>
</tr>
</tbody>
</table>


# Other schedules in the wild

MetroTransit in Minneapolis uses a transposed format, with stops as columns and trips as rows. Here's an example from their [Route 2 bus timetable](https://www.metrotransit.org/route/2):

<img src="./metrotransit-route2.png" class="img-fluid" style="max-width: 600px; display: block; margin-left: auto; margin-right: auto;" />

This is useful when there a lot of trips, because with trips on the rows readers can scroll down (versus needing to scroll sideways).

The MTA in New York City is similar. Here's an example of their [bx1 bus route timetable](https://www.mta.info/schedules/bus/bx1):

<img src="./mta-route-bx1.png" class="img-fluid" style="max-width: 600px; display: block; margin-left: auto; margin-right: auto;" />

What I like about all these tables is they highlight the structure behind bus and train routes. Sometimes they skip certain stops. But realistically, what makes them a route is that trips tend to make the same stops over and over.

A common alternative to using these tables is to do routing from a set start to end point. For example, below is a form for selecting a start and end point on SEPTA's website, with a resulting table of departure and arrival times.

<img src="./septa-routing.png" class="img-fluid" style="max-width: 600px; display: block; margin-left: auto; margin-right: auto;" />

Notice that the table has removed a lot of information about intermediate stops people might not care about.


# In conclusion

Transit tables are richly structured displays of information. They take advantage often of the fact that a train route like Chesnut Hill West is a fixed set of stops-so that stops can be on the rows, and arrival times for trips throughout the day can be on the columns.

This is intuitive to people reading transit timetables, but can get tricky to display on the web. Timetables are a core part of navigating transit networks, so it was a fun experiment to try replicating one of Septa's timetables in Great Tables!

# GT.fmt_image()


Format image paths to generate images in cells.


Usage

``` python
GT.fmt_image(
    columns=None,
    rows=None,
    height=None,
    width=None,
    sep=" ",
    path=None,
    file_pattern="{}",
    encode=True
)
```


To more easily insert graphics into body cells, we can use the [fmt_image()](GT.fmt_image.md#great_tables.GT.fmt_image) method. This allows for one or more images to be placed in the targeted cells. The cells need to contain some reference to an image file, either: (1) local paths to the files; (2) complete http/https to the files; (3) the file names, where a common path can be provided via `path=`; or (4) a fragment of the file name, where the `file_pattern=` argument helps to compose the entire file name and `path=` provides the path information. This should be expressly used on columns that contain *only* references to image files (i.e., no image references as part of a larger block of text). Multiple images can be included per cell by separating image references by commas. The `sep=` argument allows for a common separator to be applied between images.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`height: str | int | None = None`  
The height of the rendered images.

`width: str | int | None = None`  
The width of the rendered images.

`sep: str = ``" "`  
In the output of images within a body cell, `sep=` provides the separator between each image.

`path: str | Path | None = None`  
An optional path to local image files or an HTTP/HTTPS URL. This is combined with the filenames to form the complete image paths.

`file_pattern: str = ``"{}"`  
The pattern to use for mapping input values in the body cells to the names of the graphics files. The string supplied should use `"{}"` in the pattern to map filename fragments to input strings.

`encode: bool = ``True`  
The option to always use Base64 encoding for image paths that are determined to be local. By default, this is `True`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using a small portion of [metro](data.metro.md#great_tables.data.metro) dataset, let's create a new table. We will only include a few columns and rows from that table. The `lines` column has comma-separated listings of numbers corresponding to lines served at each station. We have a directory of SVG graphics for all of these lines in the package (the path for the image directory can be accessed via `files("great_tables") / "data/metro_images"`, using the `importlib_resources` package). The filenames roughly corresponds to the data in the `lines` column. The [fmt_image()](GT.fmt_image.md#great_tables.GT.fmt_image) method can be used with these inputs since the `path=` and `file_pattern=` arguments allow us to compose complete and valid file locations. What you get from this are sequences of images in the table cells, taken from the referenced graphics files on disk.


``` python
from great_tables import GT
from great_tables.data import metro
from importlib_resources import files

img_paths = files("great_tables") / "data/metro_images"

metro_mini = metro[["name", "lines", "passengers"]].head(5)

(
    GT(metro_mini)
    .fmt_image(
        columns="lines",
        path=img_paths,
        file_pattern="metro_{}.svg"
    )
    .fmt_integer(columns="passengers")
)
```


<style>
#mewiuxvgpa table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mewiuxvgpa thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mewiuxvgpa p { margin: 0; padding: 0; }
 #mewiuxvgpa .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mewiuxvgpa .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mewiuxvgpa .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mewiuxvgpa .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mewiuxvgpa .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mewiuxvgpa .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mewiuxvgpa .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mewiuxvgpa .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mewiuxvgpa .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mewiuxvgpa .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mewiuxvgpa .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mewiuxvgpa .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mewiuxvgpa .gt_spanner_row { border-bottom-style: hidden; }
 #mewiuxvgpa .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mewiuxvgpa .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mewiuxvgpa .gt_from_md> :first-child { margin-top: 0; }
 #mewiuxvgpa .gt_from_md> :last-child { margin-bottom: 0; }
 #mewiuxvgpa .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mewiuxvgpa .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mewiuxvgpa .gt_indent_1 { text-indent: 5px; }
 #mewiuxvgpa .gt_indent_2 { text-indent: calc(5px * 2); }
 #mewiuxvgpa .gt_indent_3 { text-indent: calc(5px * 3); }
 #mewiuxvgpa .gt_indent_4 { text-indent: calc(5px * 4); }
 #mewiuxvgpa .gt_indent_5 { text-indent: calc(5px * 5); }
 #mewiuxvgpa .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mewiuxvgpa .gt_row_group_first td { border-top-width: 2px; }
 #mewiuxvgpa .gt_row_group_first th { border-top-width: 2px; }
 #mewiuxvgpa .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mewiuxvgpa .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mewiuxvgpa .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mewiuxvgpa .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mewiuxvgpa .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mewiuxvgpa .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mewiuxvgpa .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mewiuxvgpa .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mewiuxvgpa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mewiuxvgpa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mewiuxvgpa .gt_left { text-align: left; }
 #mewiuxvgpa .gt_center { text-align: center; }
 #mewiuxvgpa .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mewiuxvgpa .gt_font_normal { font-weight: normal; }
 #mewiuxvgpa .gt_font_bold { font-weight: bold; }
 #mewiuxvgpa .gt_font_italic { font-style: italic; }
 #mewiuxvgpa .gt_super { font-size: 65%; }
 #mewiuxvgpa .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mewiuxvgpa .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mewiuxvgpa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mewiuxvgpa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mewiuxvgpa .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mewiuxvgpa .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| name | lines | passengers |
|----|----|----|
| Argentine | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0ZFQ0UwMCIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIyMUUyMCIgZD0iTTU3Ny4wMjYgNzYzLjk4N1YyMzQuMDIyaC05Mi4zNTJjLTIzLjkzOCAxOC43MTQtODEuMDE3IDU0LjAyNi0xNDIuNTY1IDgzLjI2NWwtMzIuMjg3IDE1LjE0NyAzNi4wMTQgODEuMDQyIDI3Ljk0Ni0xNC4zOGMxOS4zNzgtOS42MTEgNzIuNjE3LTM3LjM1NyA5MC42OC01MS43djQxNi41OTFoMTEyLjU2NCIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /></span> | 2,079,212 |
| Bastille | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0ZFQ0UwMCIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIyMUUyMCIgZD0iTTU3Ny4wMjYgNzYzLjk4N1YyMzQuMDIyaC05Mi4zNTJjLTIzLjkzOCAxOC43MTQtODEuMDE3IDU0LjAyNi0xNDIuNTY1IDgzLjI2NWwtMzIuMjg3IDE1LjE0NyAzNi4wMTQgODEuMDQyIDI3Ljk0Ni0xNC4zOGMxOS4zNzgtOS42MTEgNzIuNjE3LTM3LjM1NyA5MC42OC01MS43djQxNi41OTFoMTEyLjU2NCIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0YxOTA0MyIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIzMUYyMCIgZD0iTTY3OS43MSA1OTIuNzVjMC03OS40ODYtNTguNDItMTU5LjY4LTIwMy4yNy0xNjcuMjVsLTE1LjEzMy0uNzEyIDcuNDE4LTEwMS4zNTFoMTkwLjc4di04Ny45MTNoLTI3OC41MmwtMjEuMDM2IDI3NS40OSA4Mi41NDIuNzEyYzk3LjYxMy45NzkgMTIyLjk3OSA1My4zMTcgMTIyLjk3OSA5MS42NSAwIDYyLjE2LTUxLjYyNyA4NS42MjktOTIuODY2IDg1LjYyOS00NS4xODggMC03NS4wMzctMTYuNjE1LTEwMC42MS0zMy45MTJsLTM4Ljg5NyA4Mi42OWM0MS4wOTMgMjMuMTcyIDg5LjI3NyAzOC4zMzMgMTQ1LjUgMzguMzMzIDEyMC43NzEtLjA0IDIwMS4xMi04Mi4wOCAyMDEuMTItMTgzLjM3Ii8+PC9zdmc+" style="height: 2em;vertical-align: middle;" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0NEQUNDRiIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIzMUYyMCIgZD0iTTY4OS4yMSA2MTQuOTJjMC02OS42MTctNDIuNzQyLTExMS44MS05MS41NzMtMTM0Ljg1IDQ5LjU2OC0zMC4xNzUgNzUuMjA2LTY4LjQ1NCA3NS4yMDYtMTE3LjkgMC05MC45ODYtNzcuMzc4LTEzNi44My0xNzAuNDYtMTM2LjgzLTkwLjg3NyAwLTE3MC40MSA2MC45My0xNzAuNDEgMTQ4LjY2IDAgNTQuODAxIDI4LjU0NSA4Ny4wMzEgNzQuMjM1IDExNS41NC01MS4wMjMgMjYuMjk2LTkwLjc3OSA2Ny43MTYtOTAuNzc5IDEzOC4xNSAwIDgwLjM5NyA2Ni42OTMgMTUwLjkwOSAxODQuNTggMTUwLjkwOSAxMDguODYtLjAyIDE4OS4xOS02Mi45NiAxODkuMTktMTYzLjY4TTU3MS40MDkgMzY4LjgzYzAgMzMuMTItMzAuMDIxIDYzLjY4Mi01Ny44MTIgNzYuNTU5LTMzLjcwNS0xNC4yNzItNzcuMzAyLTM3LjYyLTc3LjMwMi04MS4wNTkgMC0zNi42ODkgMjYuMjIxLTYyLjI4NiA2Ny41MjctNjIuMjg2IDQzLjUyOS4wMSA2Ny41OCAyOS45MSA2Ny41OCA2Ni43OWwuMDA3LS4wMDR6bTguMjIgMjU0LjQyYzAgNDIuMDQyLTI3Ljc3IDc3LjM3My03OC4wOTUgNzcuMzczLTUxLjEwMyAwLTc5LjU1LTQxLjQ1OS03OS41NS04NC44OTYgMC00MS4xODggMzQuNTM5LTc1LjcwNSA2OS4wNTgtODkuMzE4IDQ0Ljk5IDIyLjU0IDg4LjU5IDQ4LjggODguNTkgOTYuODVsLS4wMDMtLjAwOXoiLz48L3N2Zz4=" style="height: 2em;vertical-align: middle;" /></span> | 8,069,243 |
| Bérault | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0ZFQ0UwMCIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIyMUUyMCIgZD0iTTU3Ny4wMjYgNzYzLjk4N1YyMzQuMDIyaC05Mi4zNTJjLTIzLjkzOCAxOC43MTQtODEuMDE3IDU0LjAyNi0xNDIuNTY1IDgzLjI2NWwtMzIuMjg3IDE1LjE0NyAzNi4wMTQgODEuMDQyIDI3Ljk0Ni0xNC4zOGMxOS4zNzgtOS42MTEgNzIuNjE3LTM3LjM1NyA5MC42OC01MS43djQxNi41OTFoMTEyLjU2NCIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /></span> | 2,106,827 |
| Champs-Élysées--Clemenceau | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0ZFQ0UwMCIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIyMUUyMCIgZD0iTTU3Ny4wMjYgNzYzLjk4N1YyMzQuMDIyaC05Mi4zNTJjLTIzLjkzOCAxOC43MTQtODEuMDE3IDU0LjAyNi0xNDIuNTY1IDgzLjI2NWwtMzIuMjg3IDE1LjE0NyAzNi4wMTQgODEuMDQyIDI3Ljk0Ni0xNC4zOGMxOS4zNzgtOS42MTEgNzIuNjE3LTM3LjM1NyA5MC42OC01MS43djQxNi41OTFoMTEyLjU2NCIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iIzk5RDRERSIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIzMUYyMCIgZD0iTTM4Ny41IDc2NC4xMVYyMzQuMDNoLTkyLjM2MWMtMjQuMDkyIDE4LjY5NS04MS4xODkgNTMuODcxLTE0Mi43MyA4My4xMDVsLTMyLjI5MiAxNC45NzQgMzYuMDk2IDgxLjYgMjcuNzc2LTE0LjI2YzE5LjQ1Ni05Ljc0NSA3Mi44MjgtMzcuNDM1IDkwLjc3Ny01MS42MTN2NDE2LjI4aDExMi43Mk04MjEuMjIgNjA2LjkzYzAtNzQuMTUxLTQ0LjI5Ny0xMTcuNTY5LTEwMi44NTktMTI4Ljg1OXYtMS40NjVjNTYuMjY2LTIwLjk5NCA4NS40MjgtNjIuODYzIDg1LjQyOC0xMTcuNTcgMC03MS4xNDMtNjEuNDk1LTEzNC4wNC0xNjkuNTEtMTM0LjA0LTYyLjQ0NyAwLTExMy4zOCAxNy4yNy0xNTkuMTUgNDcuMjE3bDM2LjcxMSA3Ny44NzdjMTcuMjM2LTE0LjIyMSA0OS40NS0zOC4xODYgOTguMzQ2LTM4LjE4NiA1NS41OTMgMCA4MS4wMjkgMjkuOTg1IDgxLjAyOSA2My42OTQgMCA0MC4zMjQtMzIuMjEzIDY1Ljg3NS04NC4xMjEgNjUuODc1SDU1MS41OHY4Ny41OGg1NC44MDFjNTQuMjAzIDAgMTAwLjY0IDE5LjQ0OSAxMDAuNjQgODAuMDk3IDAgNDQuOTItMzguMTk3IDc4LjY3LTk5LjkzMiA3OC42Ny00NC43NzQgMC04MS42MDQtMTcuMjcxLTEwNC4xNy0zNC40NjRsLTQwLjU5NiA4MS42MDFjNDIuNzk0IDIzLjkyNiA4NC4wNjIgMzkuNjEzIDE1Mi4zNyAzOS42MTMgMTIzLjE0OS0uMDExIDIwNi41Mi03NC44ODEgMjA2LjUyLTE2Ny42NWwuMDA3LjAxeiIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /></span> | 1,909,005 |
| Charles de Gaulle--Étoile | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0ZFQ0UwMCIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIyMUUyMCIgZD0iTTU3Ny4wMjYgNzYzLjk4N1YyMzQuMDIyaC05Mi4zNTJjLTIzLjkzOCAxOC43MTQtODEuMDE3IDU0LjAyNi0xNDIuNTY1IDgzLjI2NWwtMzIuMjg3IDE1LjE0NyAzNi4wMTQgODEuMDQyIDI3Ljk0Ni0xNC4zOGMxOS4zNzgtOS42MTEgNzIuNjE3LTM3LjM1NyA5MC42OC01MS43djQxNi41OTFoMTEyLjU2NCIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iIzAwNjVBRSIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTY3Ni40NCA3NDAuOTV2LTg4LjcwOUg0NTcuNzZjNi44ODgtMzAuNzEzIDYwLjEzMy03NS4wMzUgODcuMDg0LTk5Ljc1IDYzLjg1NS01Ny45OTcgMTIxLjYyLTk5LjE4OCAxMjEuNjItMTkwLjAxIDAtMTA4LjA1LTg3LjY3OC0xNjAuNjEtMTgwLjc2LTE2MC42MS03MS4zNjYgMC0xMTguNjIgMjAuOTkxLTE2OS43MiA2NS4zNzlsNTUuNzE3IDczLjU4NWMxMi42NTItMTQuMzM1IDQ0Ljk3NS00OC4xMTIgOTEuNDM0LTQ4LjExMiA1Ny43NiAwIDg3Ljc0MiAzNi43NzYgODcuNzQyIDgyLjQ4MiAwIDUxLjIwOS0zOC4wMjMgODcuODU0LTczLjM0NCAxMTguNjMtNzAuNzA5IDYxLjU5LTEzMS40NyAxMTUuNTctMTQ0Ljk0IDE3Ny4yOXY2OS44NjFoMzQzLjg1MSIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iIzg0QzI4RSIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIzMUYyMCIgZD0iTTY3Mi4xNiA1NzAuNTZjMC05OS4zMDUtNzAuNTE5LTE1Ny4wMS0xNTcuMTEtMTU3LjAxLTU1Ljk0NyAwLTg5Ljg4NyAyMC4yODctMTA3Ljc5IDM2LjA2OCA2LjY5OS0xMDYuNTIxIDYxLjQzOC0xNTkuODcgMTM0LjQxLTE1OS44NyAyOS43NjggMCA1Ni45NzMgNi43MDEgNzEuMDMxIDEyLjg5MWwxNi42Ni05MC4xMTVjLTIxLjcxMy01LjQxNy00OC45MTYtOC45MzQtNzguODMtOC45MzQtMTY2LjU5IDAtMjUxLjM2IDEyNS44OTEtMjUxLjM2IDMwOS44OTEgMCAxNDAuMzUgNTAuODk1IDI0MC4zMSAxOTMuNTggMjQwLjMxIDEwOC44OS0uMDAxIDE3OS40MS03Ny41NjEgMTc5LjQwOS0xODMuMjMxbS0xMDUuODA5IDExLjI4YzAgNDUuNjI1LTI2LjI1NCA4OC40My03Ny40MDEgODguNDMtNTIuNTc4IDAtODAuOTUzLTQ4Ljc3Mi04MC45NTMtOTkuMTIgMC0xNS42MzggMC0zNS45NTkgNi4wMDQtNDQuOTY4IDEwLjQ3MS0xNi41ODYgMzYuNzk3LTI5LjE4NCA2OS4wNTUtMjkuMTg0IDUwLjkyIDAgODMuMjkgMzUuMTkgODMuMjkgODQuODRsLjAwNS4wMDJ6Ii8+PC9zdmc+" style="height: 2em;vertical-align: middle;" /></span> | 4,291,663 |

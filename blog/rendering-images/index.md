# Rendering images anywhere in Great Tables

Rendering images in Great Tables is straightforward with [GT.fmt_image()](../../reference/GT.fmt_image.md#great_tables.GT.fmt_image) and [vals.fmt_image()](../../reference/vals.fmt_image.md#great_tables.vals.fmt_image). In this post, we'll explore three key topics:

- Four examples demonstrating how to render images within the body using [GT.fmt_image()](../../reference/GT.fmt_image.md#great_tables.GT.fmt_image).
- How to render images anywhere using [vals.fmt_image()](../../reference/vals.fmt_image.md#great_tables.vals.fmt_image) and [html()](../../reference/html.md#great_tables.html).
- How to manually render images anywhere using [html()](../../reference/html.md#great_tables.html).


# Rendering Images in the Body

[GT.fmt_image()](https://posit-dev.github.io/great-tables/reference/GT.fmt_image.html#great_tables.GT.fmt_image) is the go-to tool for rendering images within the body of a table. Below, we'll present four examples corresponding to the cases outlined in the documentation:

- **Case 1**: Local file paths.
- **Case 2**: Full HTTP/HTTPS URLs.
- **Case 3**: Image names with the `path=` argument.
- **Case 4**: Image names using both the `path=` and `file_pattern=` arguments.

> **Tip: Finding the Right Case for Your Needs**
>
> - **Case 1** and **Case 2** work best for data sourced directly from a database.
> - **Case 3** is ideal for users dealing with image names relative to a base directory or URL (e.g., `/path/to/images`).
> - **Case 4** is tailored for users working with patterned image names (e.g., `metro_{}.svg`).


## Preparations

For this demonstration, we'll use the first five rows of the built-in [metro](https://posit-dev.github.io/great-tables/reference/data.metro.html#great_tables.data.metro) dataset, specifically the `name` and `lines` columns.

To ensure a smooth walkthrough, we'll manipulate the `data` (a Python dictionary) directly. However, in real-world applications, such operations are more likely performed at the DataFrame level to leverage the benefits of vectorized operations.


Show the Code

``` python
import pandas as pd
from great_tables import GT, vals, html
from importlib_resources import files

pd.set_option('display.max_colwidth', 150)

data = {
    "name": [
        "Argentine",
        "Bastille",
        "Bérault",
        "Champs-Élysées--Clemenceau",
        "Charles de Gaulle--Étoile",
    ],
    "lines": ["1", "1, 5, 8", "1", "1, 13", "1, 2, 6"],
}

print("""\
data = {
    "name": [
        "Argentine",
        "Bastille",
        "Bérault",
        "Champs-Élysées--Clemenceau",
        "Charles de Gaulle--Étoile",
    ],
    "lines": ["1", "1, 5, 8", "1", "1, 13", "1, 2, 6"],
}\
""")
```


    data = {
        "name": [
            "Argentine",
            "Bastille",
            "Bérault",
            "Champs-Élysées--Clemenceau",
            "Charles de Gaulle--Étoile",
        ],
        "lines": ["1", "1, 5, 8", "1", "1, 13", "1, 2, 6"],
    }


Attentive readers may have noticed that the values for the key `lines` are lists of strings, each containing one or more numbers separated by commas. [GT.fmt_image()](../../reference/GT.fmt_image.md#great_tables.GT.fmt_image) is specifically designed to handle such cases, allowing users to render multiple images in a single row.


## Case 1: Local File Paths

**Case 1** demonstrates how to simulate a column containing strings representing local file paths. We'll use images stored in the `data/metro_images` directory of Great Tables:


``` python
1img_local_paths = files("great_tables") / "data/metro_images"
```


1  
<span code-cell="annotated-cell-2" code-lines="1" code-annotation="1">These image files follow a patterned naming convention, such as `metro_1.svg`, `metro_2.svg`, and so on.</span>


Below is a `Pandas` DataFrame called `metro_mini1`, where the `case1` column contains local file paths that we want to render as images.


Show the Code

``` python
metro_mini1 = pd.DataFrame(
    {
        **data,
        "case1": [
            ", ".join(
                str((img_local_paths / f"metro_{item}").with_suffix(".svg"))
                for item in row.split(", ")
            )
            for row in data["lines"]
        ],
    }
)
metro_mini1
```


|  | name | lines | case1 |
|----|----|----|----|
| 0 | Argentine | 1 | /home/runner/work/great-tables/great-tables/great_tables/data/metro_images/metro_1.svg |
| 1 | Bastille | 1, 5, 8 | /home/runner/work/great-tables/great-tables/great_tables/data/metro_images/metro_1.svg, /home/runner/work/great-tables/great-tables/great_tables/d... |
| 2 | Bérault | 1 | /home/runner/work/great-tables/great-tables/great_tables/data/metro_images/metro_1.svg |
| 3 | Champs-Élysées--Clemenceau | 1, 13 | /home/runner/work/great-tables/great-tables/great_tables/data/metro_images/metro_1.svg, /home/runner/work/great-tables/great-tables/great_tables/d... |
| 4 | Charles de Gaulle--Étoile | 1, 2, 6 | /home/runner/work/great-tables/great-tables/great_tables/data/metro_images/metro_1.svg, /home/runner/work/great-tables/great-tables/great_tables/d... |


> **Tip: Use the `pathlib` Module to Construct Paths**
>
> Local file paths can vary depending on the operating system, which makes it easy to accidentally construct invalid paths. A good practice to mitigate this is to use Python's built-in [pathlib](https://docs.python.org/3/library/pathlib.html) module to construct paths first and then convert them to strings. In this example, `img_local_paths` is actually an instance of `pathlib.Path`.
>
> <div id="2cb45818" class="cell" execution_count="4">
>
> ``` python
> from pathlib import Path
>
> isinstance(img_local_paths, Path)  # True
> ```
>
> The `case1` column is quite lengthy due to the inclusion of `img_local_paths`. In **Case 3**, we'll share a useful trick to avoid repeating the directory name each time--stay tuned!
>
> For now, let's use [GT.fmt_image()](../../reference/GT.fmt_image.md#great_tables.GT.fmt_image) to render images by passing `"case1"` as the first argument:
>
> <div id="e53a348c" class="cell" execution_count="5">
>
> ``` python
> GT(metro_mini1).fmt_image("case1").cols_align(align="right", columns="case1")
> ```
>
> <div class="cell-output cell-output-display" execution_count="4">
>
> <div id="kowbdyjkbi" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
>
> | name | lines | case1 |
> |----|----|----|
> | Argentine | 1 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0ZFQ0UwMCIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIyMUUyMCIgZD0iTTU3Ny4wMjYgNzYzLjk4N1YyMzQuMDIyaC05Mi4zNTJjLTIzLjkzOCAxOC43MTQtODEuMDE3IDU0LjAyNi0xNDIuNTY1IDgzLjI2NWwtMzIuMjg3IDE1LjE0NyAzNi4wMTQgODEuMDQyIDI3Ljk0Ni0xNC4zOGMxOS4zNzgtOS42MTEgNzIuNjE3LTM3LjM1NyA5MC42OC01MS43djQxNi41OTFoMTEyLjU2NCIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /></span> |
hdGggZmlsbD0iIzIzMUYyMCIgZD0iTTY4OS4yMSA2MTQuOTJjMC02OS42MTctNDIuNzQyLTExMS44MS05MS41NzMtMTM0Ljg1IDQ5LjU2OC0zMC4xNzUgNzUuMjA2LTY4LjQ1NCA3NS4yMDYtMTE3LjkgMC05MC45ODYtNzcuMzc4LTEzNi44My0xNzAuNDYtMTM2LjgzLTkwLjg3NyAwLTE3MC40MSA2MC45My0xNzAuNDEgMTQ4LjY2IDAgNTQuODAxIDI4LjU0NSA4Ny4wMzEgNzQuMjM1IDExNS41NC01MS4wMjMgMjYuMjk2LTkwLjc3OSA2Ny43MTYtOTAuNzc5IDEzOC4xNSAwIDgwLjM5NyA2Ni42OTMgMTUwLjkwOSAxODQuNTggMTUwLjkwOSAxMDguODYtLjAyIDE4OS4xOS02Mi45NiAxODkuMTktMTYzLjY4TTU3MS40MDkgMzY4LjgzYzAgMzMuMTItMzAuMDIxIDYzLjY4Mi01Ny44MTIgNzYuNTU5LTMzLjcwNS0xNC4yNzItNzcuMzAyLTM3LjYyLTc3LjMwMi04MS4wNTkgMC0zNi42ODkgMjYuMjIxLTYyLjI4NiA2Ny41MjctNjIuMjg2IDQzLjUyOS4wMSA2Ny41OCAyOS45MSA2Ny41OCA2Ni43OWwuMDA3LS4wMDR6bTguMjIgMjU0LjQyYzAgNDIuMDQyLTI3Ljc3IDc3LjM3My03OC4wOTUgNzcuMzczLTUxLjEwMyAwLTc5LjU1LTQxLjQ1OS03OS41NS04NC44OTYgMC00MS4xODggMzQuNTM5LTc1LjcwNSA2OS4wNTgtODkuMzE4IDQ0Ljk5IDIyLjU0IDg4LjU5IDQ4LjggODguNTkgOTYuODVsLS4wMDMtLjAwOXoiLz48L3N2Zz4=" style="height: 2em;vertical-align: middle;" /></span> |
> | Bérault | 1 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0ZFQ0UwMCIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIyMUUyMCIgZD0iTTU3Ny4wMjYgNzYzLjk4N1YyMzQuMDIyaC05Mi4zNTJjLTIzLjkzOCAxOC43MTQtODEuMDE3IDU0LjAyNi0xNDIuNTY1IDgzLjI2NWwtMzIuMjg3IDE1LjE0NyAzNi4wMTQgODEuMDQyIDI3Ljk0Ni0xNC4zOGMxOS4zNzgtOS42MTEgNzIuNjE3LTM3LjM1NyA5MC42OC01MS43djQxNi41OTFoMTEyLjU2NCIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /></span> |
> | Champs-Élysées--Clemenceau | 1, 13 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0ZFQ0UwMCIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIyMUUyMCIgZD0iTTU3Ny4wMjYgNzYzLjk4N1YyMzQuMDIyaC05Mi4zNTJjLTIzLjkzOCAxOC43MTQtODEuMDE3IDU0LjAyNi0xNDIuNTY1IDgzLjI2NWwtMzIuMjg3IDE1LjE0NyAzNi4wMTQgODEuMDQyIDI3Ljk0Ni0xNC4zOGMxOS4zNzgtOS42MTEgNzIuNjE3LTM3LjM1NyA5MC42OC01MS43djQxNi41OTFoMTEyLjU2NCIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iIzk5RDRERSIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIzMUYyMCIgZD0iTTM4Ny41IDc2NC4xMVYyMzQuMDNoLTkyLjM2MWMtMjQuMDkyIDE4LjY5NS04MS4xODkgNTMuODcxLTE0Mi43MyA4My4xMDVsLTMyLjI5MiAxNC45NzQgMzYuMDk2IDgxLjYgMjcuNzc2LTE0LjI2YzE5LjQ1Ni05Ljc0NSA3Mi44MjgtMzcuNDM1IDkwLjc3Ny01MS42MTN2NDE2LjI4aDExMi43Mk04MjEuMjIgNjA2LjkzYzAtNzQuMTUxLTQ0LjI5Ny0xMTcuNTY5LTEwMi44NTktMTI4Ljg1OXYtMS40NjVjNTYuMjY2LTIwLjk5NCA4NS40MjgtNjIuODYzIDg1LjQyOC0xMTcuNTcgMC03MS4xNDMtNjEuNDk1LTEzNC4wNC0xNjkuNTEtMTM0LjA0LTYyLjQ0NyAwLTExMy4zOCAxNy4yNy0xNTkuMTUgNDcuMjE3bDM2LjcxMSA3Ny44NzdjMTcuMjM2LTE0LjIyMSA0OS40NS0zOC4xODYgOTguMzQ2LTM4LjE4NiA1NS41OTMgMCA4MS4wMjkgMjkuOTg1IDgxLjAyOSA2My42OTQgMCA0MC4zMjQtMzIuMjEzIDY1Ljg3NS04NC4xMjEgNjUuODc1SDU1MS41OHY4Ny41OGg1NC44MDFjNTQuMjAzIDAgMTAwLjY0IDE5LjQ0OSAxMDAuNjQgODAuMDk3IDAgNDQuOTItMzguMTk3IDc4LjY3LTk5LjkzMiA3OC42Ny00NC43NzQgMC04MS42MDQtMTcuMjcxLTEwNC4xNy0zNC40NjRsLTQwLjU5NiA4MS42MDFjNDIuNzk0IDIzLjkyNiA4NC4wNjIgMzkuNjEzIDE1Mi4zNyAzOS42MTMgMTIzLjE0OS0uMDExIDIwNi41Mi03NC44ODEgMjA2LjUyLTE2Ny42NWwuMDA3LjAxeiIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /></span> |
> | Charles de Gaulle--Étoile | 1, 2, 6 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0ZFQ0UwMCIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIyMUUyMCIgZD0iTTU3Ny4wMjYgNzYzLjk4N1YyMzQuMDIyaC05Mi4zNTJjLTIzLjkzOCAxOC43MTQtODEuMDE3IDU0LjAyNi0xNDIuNTY1IDgzLjI2NWwtMzIuMjg3IDE1LjE0NyAzNi4wMTQgODEuMDQyIDI3Ljk0Ni0xNC4zOGMxOS4zNzgtOS42MTEgNzIuNjE3LTM3LjM1NyA5MC42OC01MS43djQxNi41OTFoMTEyLjU2NCIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iIzAwNjVBRSIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTY3Ni40NCA3NDAuOTV2LTg4LjcwOUg0NTcuNzZjNi44ODgtMzAuNzEzIDYwLjEzMy03NS4wMzUgODcuMDg0LTk5Ljc1IDYzLjg1NS01Ny45OTcgMTIxLjYyLTk5LjE4OCAxMjEuNjItMTkwLjAxIDAtMTA4LjA1LTg3LjY3OC0xNjAuNjEtMTgwLjc2LTE2MC42MS03MS4zNjYgMC0xMTguNjIgMjAuOTkxLTE2OS43MiA2NS4zNzlsNTUuNzE3IDczLjU4NWMxMi42NTItMTQuMzM1IDQ0Ljk3NS00OC4xMTIgOTEuNDM0LTQ4LjExMiA1Ny43NiAwIDg3Ljc0MiAzNi43NzYgODcuNzQyIDgyLjQ4MiAwIDUxLjIwOS0zOC4wMjMgODcuODU0LTczLjM0NCAxMTguNjMtNzAuNzA5IDYxLjU5LTEzMS40NyAxMTUuNTctMTQ0Ljk0IDE3Ny4yOXY2OS44NjFoMzQzLjg1MSIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iIzg0QzI4RSIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIzMUYyMCIgZD0iTTY3Mi4xNiA1NzAuNTZjMC05OS4zMDUtNzAuNTE5LTE1Ny4wMS0xNTcuMTEtMTU3LjAxLTU1Ljk0NyAwLTg5Ljg4NyAyMC4yODctMTA3Ljc5IDM2LjA2OCA2LjY5OS0xMDYuNTIxIDYxLjQzOC0xNTkuODcgMTM0LjQxLTE1OS44NyAyOS43NjggMCA1Ni45NzMgNi43MDEgNzEuMDMxIDEyLjg5MWwxNi42Ni05MC4xMTVjLTIxLjcxMy01LjQxNy00OC45MTYtOC45MzQtNzguODMtOC45MzQtMTY2LjU5IDAtMjUxLjM2IDEyNS44OTEtMjUxLjM2IDMwOS44OTEgMCAxNDAuMzUgNTAuODk1IDI0MC4zMSAxOTMuNTggMjQwLjMxIDEwOC44OS0uMDAxIDE3OS40MS03Ny41NjEgMTc5LjQwOS0xODMuMjMxbS0xMDUuODA5IDExLjI4YzAgNDUuNjI1LTI2LjI1NCA4OC40My03Ny40MDEgODguNDMtNTIuNTc4IDAtODAuOTUzLTQ4Ljc3Mi04MC45NTMtOTkuMTIgMC0xNS42MzggMC0zNS45NTkgNi4wMDQtNDQuOTY4IDEwLjQ3MS0xNi41ODYgMzYuNzk3LTI5LjE4NCA2OS4wNTUtMjkuMTg0IDUwLjkyIDAgODMuMjkgMzUuMTkgODMuMjkgODQuODRsLjAwNS4wMDJ6Ii8+PC9zdmc+" style="height: 2em;vertical-align: middle;" /></span> |
>
> </div>
>
> </div>
>
> </div>
>
> <div id="case-2-full-httphttps-urls" class="section level2">
>
> ## Case 2: Full HTTP/HTTPS URLs
>
> **Case 2** demonstrates how to simulate a column containing strings representing HTTP/HTTPS URLs. We'll use the same images as in **Case 1**, but this time, retrieve them from the Great Tables GitHub repository:
>
> <div id="f4069850" class="cell" execution_count="6">
>
> ``` python
> img_url_paths = "https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images"
> ```
>
> </div>
>
> Below is a `Pandas` DataFrame called `metro_mini2`, where the `case2` column contains full HTTP/HTTPS URLs that we aim to render as images.
>
> <div id="fb19e8fe" class="cell" execution_count="7">
>
> Show the Code
>
> ``` python
> metro_mini2 = pd.DataFrame(
>     {
>         **data,
>         "case2": [
>             ", ".join(f"{img_url_paths}/metro_{item}.svg" for item in row.split(", "))
>             for row in data["lines"]
>         ],
>     }
> )
> metro_mini2
> ```
>
> <div class="cell-output cell-output-display" execution_count="6">
>
> <div>
>
> |  | name | lines | case2 |
> |----|----|----|----|
> | 0 | Argentine | 1 | https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg |
> | 1 | Bastille | 1, 5, 8 | https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg, https://raw.githubusercontent... |
> | 2 | Bérault | 1 | https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg |
> | 3 | Champs-Élysées--Clemenceau | 1, 13 | https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg, https://raw.githubusercontent... |
> | 4 | Charles de Gaulle--Étoile | 1, 2, 6 | https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg, https://raw.githubusercontent... |
>
> </div>
>
> </div>
>
> </div>
>
> The lengthy `case2` column issue can also be addressed using the trick shared in **Case 3**.
>
> Similarly, we can use [GT.fmt_image()](../../reference/GT.fmt_image.md#great_tables.GT.fmt_image) to render images by passing `"case2"` as the first argument:
>
> <div id="d2261923" class="cell" execution_count="8">
>
> ``` python
> GT(metro_mini2).fmt_image("case2").cols_align(align="right", columns="case2")
> ```
>
> <div class="cell-output cell-output-display" execution_count="7">
>
> <div id="kjqkqdycij" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
>
> | name | lines | case2 |
> |----|----|----|
> | Argentine | 1 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /></span> |
> | Bastille | 1, 5, 8 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_5.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_8.svg" style="height: 2em;vertical-align: middle;" /></span> |
> | Bérault | 1 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /></span> |
> | Champs-Élysées--Clemenceau | 1, 13 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_13.svg" style="height: 2em;vertical-align: middle;" /></span> |
> | Charles de Gaulle--Étoile | 1, 2, 6 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_2.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_6.svg" style="height: 2em;vertical-align: middle;" /></span> |
>
> </div>
>
> </div>
>
> </div>
>
> <div id="case-3-image-names-with-the-path-argument" class="section level2">
>
> ## Case 3: Image Names with the `path=` Argument
>
> **Case 3** demonstrates how to use the `path=` argument to specify images relative to a base directory or URL. This approach eliminates much of the repetition in file names, offering a solution to the issues in **Case 1** and **Case 2**.
>
> Below is a `Pandas` DataFrame called `metro_mini3`, where the `case3` column contains file names that we aim to render as images.
>
> <div id="dc157577" class="cell" execution_count="9">
>
> Show the Code
>
> ``` python
> metro_mini3 = pd.DataFrame(
>     {
>         **data,
>         "case3": [
>             ", ".join(f"metro_{item}.svg" for item in row.split(", ")) for row in data["lines"]
>         ],
>     }
> )
> metro_mini3
> ```
>
> <div class="cell-output cell-output-display" execution_count="8">
>
> <div>
>
> |     | name                      | lines   | case3                                 |
> |-----|---------------------------|---------|---------------------------------------|
> | 0   | Argentine                 | 1       | metro_1.svg                           |
> | 1   | Bastille                  | 1, 5, 8 | metro_1.svg, metro_5.svg, metro_8.svg |
> | 2   | Bérault                   | 1       | metro_1.svg                           |
> | 3   | Champs-Élysées--Clemenceau | 1, 13   | metro_1.svg, metro_13.svg             |
> | 4   | Charles de Gaulle--Étoile  | 1, 2, 6 | metro_1.svg, metro_2.svg, metro_6.svg |
>
> </div>
>
> </div>
>
> </div>
>
> Now we can use [GT.fmt_image()](../../reference/GT.fmt_image.md#great_tables.GT.fmt_image) to render the images by passing `"case3"` as the first argument and specifying either `img_local_paths` or `img_url_paths` as the `path=` argument:
>
> <div id="c54d80d3" class="cell" execution_count="10">
>
> ``` python
> # equivalent to `Case 1`
> (
>     GT(metro_mini3)
>     .fmt_image("case3", path=img_local_paths)
>     .cols_align(align="right", columns="case3")
> )
>
> # equivalent to `Case 2`
> (
>     GT(metro_mini3)
>     .fmt_image("case3", path=img_url_paths)
>     .cols_align(align="right", columns="case3")
> )
> ```
>
> <div class="cell-output cell-output-display" execution_count="9">
>
> <div id="hqgggwxopa" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
>
> | name | lines | case3 |
> |----|----|----|
> | Argentine | 1 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /></span> |
> | Bastille | 1, 5, 8 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_5.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_8.svg" style="height: 2em;vertical-align: middle;" /></span> |
> | Bérault | 1 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /></span> |
> | Champs-Élysées--Clemenceau | 1, 13 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_13.svg" style="height: 2em;vertical-align: middle;" /></span> |
> | Charles de Gaulle--Étoile | 1, 2, 6 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_2.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_6.svg" style="height: 2em;vertical-align: middle;" /></span> |
>
> </div>
>
> </div>
>
> </div>
>
> After exploring **Case 1** and **Case 2**, you'll likely appreciate the functionality of the `path=` argument. However, manually constructing file names can still be a bit tedious. If your file names follow a consistent pattern, the `file_pattern=` argument can simplify the process. Let's see how this works in **Case 4** below.
>
> <div id="case-4-image-names-using-both-the-path-and-file_pattern-arguments" class="section level2">
>
> ## Case 4: Image Names Using Both the `path=` and `file_pattern=` Arguments
>
> **Case 4** demonstrates how to use `path=` and `file_pattern=` to specify images with names following a common pattern. For example, you could use `file_pattern="metro_{}.svg"` to reference images like `metro_1.svg`, `metro_2.svg`, and so on.
>
> Below is a `Pandas` DataFrame called `metro_mini4`, where the `case4` column contains a copy of `data["lines"]`, which we aim to render as images.
>
> <div id="1e5b3500" class="cell" execution_count="11">
>
> Show the Code
>
> ``` python
> metro_mini4 = pd.DataFrame({**data, "case4": data["lines"]})
> metro_mini4
> ```
>
> <div class="cell-output cell-output-display" execution_count="10">
>
> <div>
>
> |     | name                      | lines   | case4   |
> |-----|---------------------------|---------|---------|
> | 0   | Argentine                 | 1       | 1       |
> | 1   | Bastille                  | 1, 5, 8 | 1, 5, 8 |
> | 2   | Bérault                   | 1       | 1       |
> | 3   | Champs-Élysées--Clemenceau | 1, 13   | 1, 13   |
> | 4   | Charles de Gaulle--Étoile  | 1, 2, 6 | 1, 2, 6 |
>
> </div>
>
> </div>
>
> </div>
>
> First, define a string pattern to illustrate the file naming convention, using `{}` to indicate the variable portion:
>
> <div id="0c186417" class="cell" execution_count="12">
>
> ``` python
> file_pattern = "metro_{}.svg"
> ```
>
> </div>
>
> Next, pass `"case4"` as the first argument, along with `img_local_paths` or `img_url_paths` as the `path=` argument, and `file_pattern` as the `file_pattern=` argument. This allows [GT.fmt_image()](../../reference/GT.fmt_image.md#great_tables.GT.fmt_image) to render the images:
>
> <div id="8b01a1bd" class="cell" execution_count="13">
>
> ``` python
> # equivalent to `Case 1`
> (
>     GT(metro_mini4)
>     .fmt_image("case4", path=img_local_paths, file_pattern=file_pattern)
>     .cols_align(align="right", columns="case4")
> )
>
> # equivalent to `Case 2`
> (
>     GT(metro_mini4)
>     .fmt_image("case4", path=img_url_paths, file_pattern=file_pattern)
>     .cols_align(align="right", columns="case4")
> )
> ```
>
> <div class="cell-output cell-output-display" execution_count="12">
>
> <div id="pterkevrfm" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
>
> | name | lines | case4 |
> |----|----|----|
> | Argentine | 1 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /></span> |
> | Bastille | 1, 5, 8 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_5.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_8.svg" style="height: 2em;vertical-align: middle;" /></span> |
> | Bérault | 1 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /></span> |
> | Champs-Élysées--Clemenceau | 1, 13 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_13.svg" style="height: 2em;vertical-align: middle;" /></span> |
> | Charles de Gaulle--Étoile | 1, 2, 6 | <span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_2.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_6.svg" style="height: 2em;vertical-align: middle;" /></span> |
>
> </div>
>
> </div>
>
> </div>
>
> > **Warning: Using `file_pattern=` Independently**
> >
> > The `file_pattern=` argument is typically used in conjunction with the `path=` argument, but this is not a strict rule. If your local file paths or HTTP/HTTPS URLs follow a pattern, you can use `file_pattern=` alone without `path=`. This allows you to include the shared portion of the file paths or URLs directly in `file_pattern`, as shown below:
> >
> > <div id="abfbecd8" class="cell" execution_count="14">
> >
> > ``` python
> > file_pattern = str(img_local_paths / "metro_{}.svg")
> > (
> >     GT(metro_mini4)
> >     .fmt_image("case4", file_pattern=file_pattern)
> >     .cols_align(align="right", columns="case4")
> > )
> > ```
> >
> > <div class="cell-output cell-output-display" execution_count="13">
> >
> > <div id="erwsmojuqo" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
> >
> > | name | lines | case4 |
> > |----|----|----|
> > | Argentine | 1 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0ZFQ0UwMCIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIyMUUyMCIgZD0iTTU3Ny4wMjYgNzYzLjk4N1YyMzQuMDIyaC05Mi4zNTJjLTIzLjkzOCAxOC43MTQtODEuMDE3IDU0LjAyNi0xNDIuNTY1IDgzLjI2NWwtMzIuMjg3IDE1LjE0NyAzNi4wMTQgODEuMDQyIDI3Ljk0Ni0xNC4zOGMxOS4zNzgtOS42MTEgNzIuNjE3LTM3LjM1NyA5MC42OC01MS43djQxNi41OTFoMTEyLjU2NCIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /></span> |
> > | Bastille | 1, 5, 8 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0ZFQ0UwMCIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIyMUUyMCIgZD0iTTU3Ny4wMjYgNzYzLjk4N1YyMzQuMDIyaC05Mi4zNTJjLTIzLjkzOCAxOC43MTQtODEuMDE3IDU0LjAyNi0xNDIuNTY1IDgzLjI2NWwtMzIuMjg3IDE1LjE0NyAzNi4wMTQgODEuMDQyIDI3Ljk0Ni0xNC4zOGMxOS4zNzgtOS42MTEgNzIuNjE3LTM3LjM1NyA5MC42OC01MS43djQxNi41OTFoMTEyLjU2NCIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0YxOTA0MyIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIzMUYyMCIgZD0iTTY3OS43MSA1OTIuNzVjMC03OS40ODYtNTguNDItMTU5LjY4LTIwMy4yNy0xNjcuMjVsLTE1LjEzMy0uNzEyIDcuNDE4LTEwMS4zNTFoMTkwLjc4di04Ny45MTNoLTI3OC41MmwtMjEuMDM2IDI3NS40OSA4Mi41NDIuNzEyYzk3LjYxMy45NzkgMTIyLjk3OSA1My4zMTcgMTIyLjk3OSA5MS42NSAwIDYyLjE2LTUxLjYyNyA4NS42MjktOTIuODY2IDg1LjYyOS00NS4xODggMC03NS4wMzctMTYuNjE1LTEwMC42MS0zMy45MTJsLTM4Ljg5NyA4Mi42OWM0MS4wOTMgMjMuMTcyIDg5LjI3NyAzOC4zMzMgMTQ1LjUgMzguMzMzIDEyMC43NzEtLjA0IDIwMS4xMi04Mi4wOCAyMDEuMTItMTgzLjM3Ii8+PC9zdmc+" style="height: 2em;vertical-align: middle;" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0NEQUNDRiIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIzMUYyMCIgZD0iTTY4OS4yMSA2MTQuOTJjMC02OS42MTctNDIuNzQyLTExMS44MS05MS41NzMtMTM0Ljg1IDQ5LjU2OC0zMC4xNzUgNzUuMjA2LTY4LjQ1NCA3NS4yMDYtMTE3LjkgMC05MC45ODYtNzcuMzc4LTEzNi44My0xNzAuNDYtMTM2LjgzLTkwLjg3NyAwLTE3MC40MSA2MC45My0xNzAuNDEgMTQ4LjY2IDAgNTQuODAxIDI4LjU0NSA4Ny4wMzEgNzQuMjM1IDExNS41NC01MS4wMjMgMjYuMjk2LTkwLjc3OSA2Ny43MTYtOTAuNzc5IDEzOC4xNSAwIDgwLjM5NyA2Ni42OTMgMTUwLjkwOSAxODQuNTggMTUwLjkwOSAxMDguODYtLjAyIDE4OS4xOS02Mi45NiAxODkuMTktMTYzLjY4TTU3MS40MDkgMzY4LjgzYzAgMzMuMTItMzAuMDIxIDYzLjY4Mi01Ny44MTIgNzYuNTU5LTMzLjcwNS0xNC4yNzItNzcuMzAyLTM3LjYyLTc3LjMwMi04MS4wNTkgMC0zNi42ODkgMjYuMjIxLTYyLjI4NiA2Ny41MjctNjIuMjg2IDQzLjUyOS4wMSA2Ny41OCAyOS45MSA2Ny41OCA2Ni43OWwuMDA3LS4wMDR6bTguMjIgMjU0LjQyYzAgNDIuMDQyLTI3Ljc3IDc3LjM3My03OC4wOTUgNzcuMzczLTUxLjEwMyAwLTc5LjU1LTQxLjQ1OS03OS41NS04NC44OTYgMC00MS4xODggMzQuNTM5LTc1LjcwNSA2OS4wNTgtODkuMzE4IDQ0Ljk5IDIyLjU0IDg4LjU5IDQ4LjggODguNTkgOTYuODVsLS4wMDMtLjAwOXoiLz48L3N2Zz4=" style="height: 2em;vertical-align: middle;" /></span> |
> > | Bérault | 1 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0ZFQ0UwMCIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIyMUUyMCIgZD0iTTU3Ny4wMjYgNzYzLjk4N1YyMzQuMDIyaC05Mi4zNTJjLTIzLjkzOCAxOC43MTQtODEuMDE3IDU0LjAyNi0xNDIuNTY1IDgzLjI2NWwtMzIuMjg3IDE1LjE0NyAzNi4wMTQgODEuMDQyIDI3Ljk0Ni0xNC4zOGMxOS4zNzgtOS42MTEgNzIuNjE3LTM3LjM1NyA5MC42OC01MS43djQxNi41OTFoMTEyLjU2NCIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /></span> |
> > | Champs-Élysées--Clemenceau | 1, 13 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0ZFQ0UwMCIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIyMUUyMCIgZD0iTTU3Ny4wMjYgNzYzLjk4N1YyMzQuMDIyaC05Mi4zNTJjLTIzLjkzOCAxOC43MTQtODEuMDE3IDU0LjAyNi0xNDIuNTY1IDgzLjI2NWwtMzIuMjg3IDE1LjE0NyAzNi4wMTQgODEuMDQyIDI3Ljk0Ni0xNC4zOGMxOS4zNzgtOS42MTEgNzIuNjE3LTM3LjM1NyA5MC42OC01MS43djQxNi41OTFoMTEyLjU2NCIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iIzk5RDRERSIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIzMUYyMCIgZD0iTTM4Ny41IDc2NC4xMVYyMzQuMDNoLTkyLjM2MWMtMjQuMDkyIDE4LjY5NS04MS4xODkgNTMuODcxLTE0Mi43MyA4My4xMDVsLTMyLjI5MiAxNC45NzQgMzYuMDk2IDgxLjYgMjcuNzc2LTE0LjI2YzE5LjQ1Ni05Ljc0NSA3Mi44MjgtMzcuNDM1IDkwLjc3Ny01MS42MTN2NDE2LjI4aDExMi43Mk04MjEuMjIgNjA2LjkzYzAtNzQuMTUxLTQ0LjI5Ny0xMTcuNTY5LTEwMi44NTktMTI4Ljg1OXYtMS40NjVjNTYuMjY2LTIwLjk5NCA4NS40MjgtNjIuODYzIDg1LjQyOC0xMTcuNTcgMC03MS4xNDMtNjEuNDk1LTEzNC4wNC0xNjkuNTEtMTM0LjA0LTYyLjQ0NyAwLTExMy4zOCAxNy4yNy0xNTkuMTUgNDcuMjE3bDM2LjcxMSA3Ny44NzdjMTcuMjM2LTE0LjIyMSA0OS40NS0zOC4xODYgOTguMzQ2LTM4LjE4NiA1NS41OTMgMCA4MS4wMjkgMjkuOTg1IDgxLjAyOSA2My42OTQgMCA0MC4zMjQtMzIuMjEzIDY1Ljg3NS04NC4xMjEgNjUuODc1SDU1MS41OHY4Ny41OGg1NC44MDFjNTQuMjAzIDAgMTAwLjY0IDE5LjQ0OSAxMDAuNjQgODAuMDk3IDAgNDQuOTItMzguMTk3IDc4LjY3LTk5LjkzMiA3OC42Ny00NC43NzQgMC04MS42MDQtMTcuMjcxLTEwNC4xNy0zNC40NjRsLTQwLjU5NiA4MS42MDFjNDIuNzk0IDIzLjkyNiA4NC4wNjIgMzkuNjEzIDE1Mi4zNyAzOS42MTMgMTIzLjE0OS0uMDExIDIwNi41Mi03NC44ODEgMjA2LjUyLTE2Ny42NWwuMDA3LjAxeiIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /></span> |
> > | Charles de Gaulle--Étoile | 1, 2, 6 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iI0ZFQ0UwMCIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIyMUUyMCIgZD0iTTU3Ny4wMjYgNzYzLjk4N1YyMzQuMDIyaC05Mi4zNTJjLTIzLjkzOCAxOC43MTQtODEuMDE3IDU0LjAyNi0xNDIuNTY1IDgzLjI2NWwtMzIuMjg3IDE1LjE0NyAzNi4wMTQgODEuMDQyIDI3Ljk0Ni0xNC4zOGMxOS4zNzgtOS42MTEgNzIuNjE3LTM3LjM1NyA5MC42OC01MS43djQxNi41OTFoMTEyLjU2NCIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iIzAwNjVBRSIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTY3Ni40NCA3NDAuOTV2LTg4LjcwOUg0NTcuNzZjNi44ODgtMzAuNzEzIDYwLjEzMy03NS4wMzUgODcuMDg0LTk5Ljc1IDYzLjg1NS01Ny45OTcgMTIxLjYyLTk5LjE4OCAxMjEuNjItMTkwLjAxIDAtMTA4LjA1LTg3LjY3OC0xNjAuNjEtMTgwLjc2LTE2MC42MS03MS4zNjYgMC0xMTguNjIgMjAuOTkxLTE2OS43MiA2NS4zNzlsNTUuNzE3IDczLjU4NWMxMi42NTItMTQuMzM1IDQ0Ljk3NS00OC4xMTIgOTEuNDM0LTQ4LjExMiA1Ny43NiAwIDg3Ljc0MiAzNi43NzYgODcuNzQyIDgyLjQ4MiAwIDUxLjIwOS0zOC4wMjMgODcuODU0LTczLjM0NCAxMTguNjMtNzAuNzA5IDYxLjU5LTEzMS40NyAxMTUuNTctMTQ0Ljk0IDE3Ny4yOXY2OS44NjFoMzQzLjg1MSIvPjwvc3ZnPg==" style="height: 2em;vertical-align: middle;" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld0JveD0iMCAwIDEwNTAgMTA1MCIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MS4xM2VtO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OmF1dG87Zm9udC1zaXplOmluaGVyaXQ7b3ZlcmZsb3c6dmlzaWJsZTtwb3NpdGlvbjpyZWxhdGl2ZTsiPjxjaXJjbGUgZmlsbD0iIzg0QzI4RSIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIi8+PHBhdGggZmlsbD0iIzIzMUYyMCIgZD0iTTY3Mi4xNiA1NzAuNTZjMC05OS4zMDUtNzAuNTE5LTE1Ny4wMS0xNTcuMTEtMTU3LjAxLTU1Ljk0NyAwLTg5Ljg4NyAyMC4yODctMTA3Ljc5IDM2LjA2OCA2LjY5OS0xMDYuNTIxIDYxLjQzOC0xNTkuODcgMTM0LjQxLTE1OS44NyAyOS43NjggMCA1Ni45NzMgNi43MDEgNzEuMDMxIDEyLjg5MWwxNi42Ni05MC4xMTVjLTIxLjcxMy01LjQxNy00OC45MTYtOC45MzQtNzguODMtOC45MzQtMTY2LjU5IDAtMjUxLjM2IDEyNS44OTEtMjUxLjM2IDMwOS44OTEgMCAxNDAuMzUgNTAuODk1IDI0MC4zMSAxOTMuNTggMjQwLjMxIDEwOC44OS0uMDAxIDE3OS40MS03Ny41NjEgMTc5LjQwOS0xODMuMjMxbS0xMDUuODA5IDExLjI4YzAgNDUuNjI1LTI2LjI1NCA4OC40My03Ny40MDEgODguNDMtNTIuNTc4IDAtODAuOTUzLTQ4Ljc3Mi04MC45NTMtOTkuMTIgMC0xNS42MzggMC0zNS45NTkgNi4wMDQtNDQuOTY4IDEwLjQ3MS0xNi41ODYgMzYuNzk3LTI5LjE4NCA2OS4wNTUtMjkuMTg0IDUwLjkyIDAgODMuMjkgMzUuMTkgODMuMjkgODQuODRsLjAwNS4wMDJ6Ii8+PC9zdmc+" style="height: 2em;vertical-align: middle;" /></span> |
> >
> > **Case 4** is undoubtedly one of the most powerful features of Great Tables. While mastering it may take some practice, we hope this example helps you render images effortlessly and effectively.
> >
> > <div id="rendering-images-anywhere" class="section level1">
> >
> > # Rendering Images Anywhere
> >
> > While [GT.fmt_image()](../../reference/GT.fmt_image.md#great_tables.GT.fmt_image) is primarily designed for rendering images in the table body, what if you need to display images in other locations, such as the header? In such cases, you can turn to the versatile [vals.fmt_image()](https://posit-dev.github.io/great-tables/reference/vals.fmt_image.html#great_tables.vals.fmt_image).
> >
> > [vals.fmt_image()](../../reference/vals.fmt_image.md#great_tables.vals.fmt_image) is a hidden gem in Great Tables. Its usage is similar to [GT.fmt_image()](../../reference/GT.fmt_image.md#great_tables.GT.fmt_image), but instead of working directly with DataFrame columns, it lets you pass a string or a list of strings as the first argument, returning a list of strings, each representing an image. You can then wrap these strings with [html()](https://posit-dev.github.io/great-tables/reference/html.html#great_tables.html), allowing Great Tables to render the images anywhere in the table.
> >
> > <div id="preparations-1" class="section level2">
> >
> > ## Preparations
> >
> > We will create a `Pandas` DataFrame named `metro_mini` using the `data` dictionary. This will be used for demonstration in the following examples:
> >
> > <div id="f334ca16" class="cell" execution_count="15">
> >
> > Show the Code
> >
> > ``` python
> > metro_mini = pd.DataFrame(data)
> > metro_mini
> > ```
> >
> > <div class="cell-output cell-output-display" execution_count="14">
> >
> > <div>
> >
> > |     | name                      | lines   |
> > |-----|---------------------------|---------|
> > | 0   | Argentine                 | 1       |
> > | 1   | Bastille                  | 1, 5, 8 |
> > | 2   | Bérault                   | 1       |
> > | 3   | Champs-Élysées--Clemenceau | 1, 13   |
> > | 4   | Charles de Gaulle--Étoile  | 1, 2, 6 |
> >
> > </div>
> >
> > </div>
> >
> > </div>
> >
> > <div id="single-image" class="section level2">
> >
> > ## Single Image
> >
> > This example shows how to render a valid URL as an image in the title of the table header:
> >
> > <div id="22385dd1" class="cell" execution_count="16">
> >
> > ``` python
> > gt_logo_url = "https://posit-dev.github.io/great-tables/assets/GT_logo.svg"
> >
> > 1_gt_logo, *_ = vals.fmt_image(gt_logo_url, height=100)
> > gt_logo = html(_gt_logo)
> >
> > (
> >     GT(metro_mini)
> >     .fmt_image("lines", path=img_url_paths, file_pattern="metro_{}.svg")
> >     .tab_header(title=gt_logo)
> >     .cols_align(align="right", columns="lines")
> >     .opt_stylize(style=4, color="gray")
> > )
> > ```
> >
> > <div class="cell-annotation">
> >
> > 1  
> > <span code-cell="annotated-cell-14" code-lines="3" code-annotation="1">[vals.fmt_image()](../../reference/vals.fmt_image.md#great_tables.vals.fmt_image) returns a list of strings. Here, we use tuple unpacking to extract the first item from the list.</span>
> >
> > </div>
> >
> > <div class="cell-output cell-output-display" execution_count="15">
> >
> > <div id="epbojcspmz" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
> >
> > <table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
> > <thead>
> > <tr class="gt_heading">
> > <th colspan="2" class="gt_heading gt_title gt_font_normal"><span style="white-space:nowrap;"><img src="https://posit-dev.github.io/great-tables/assets/GT_logo.svg" style="height: 100px;vertical-align: middle;" /></span></th>
> > </tr>
> > <tr class="gt_col_headings">
> > <th id="name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">name</th>
> > <th id="lines" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">lines</th>
> > </tr>
> > </thead>
> > <tbody class="gt_table_body">
> > <tr>
> > <td class="gt_row gt_left">Argentine</td>
> > <td class="gt_row gt_right"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /></span></td>
> > </tr>
> > <tr>
> > <td class="gt_row gt_left gt_striped">Bastille</td>
> > <td class="gt_row gt_right gt_striped"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_5.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_8.svg" style="height: 2em;vertical-align: middle;" /></span></td>
> > </tr>
> > <tr>
> > <td class="gt_row gt_left">Bérault</td>
> > <td class="gt_row gt_right"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /></span></td>
> > </tr>
> > <tr>
> > <td class="gt_row gt_left gt_striped">Champs-Élysées--Clemenceau</td>
> > <td class="gt_row gt_right gt_striped"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_13.svg" style="height: 2em;vertical-align: middle;" /></span></td>
> > </tr>
> > <tr>
> > <td class="gt_row gt_left">Charles de Gaulle--Étoile</td>
> > <td class="gt_row gt_right"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_2.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_6.svg" style="height: 2em;vertical-align: middle;" /></span></td>
> > </tr>
> > </tbody>
> > </table>
> >
> > </div>
> >
> > </div>
> >
> > </div>
> >
> > <div id="multiple-images" class="section level2">
> >
> > ## Multiple Images
> >
> > This example demonstrates how to render two valid URLs as images in the title and subtitle of the table header:
> >
> > <div id="9dbf549e" class="cell" execution_count="17">
> >
> > ``` python
> > metro_logo_url = "https://raw.githubusercontent.com/rstudio/gt/master/images/dataset_metro.svg"
> > logo_urls = [gt_logo_url, metro_logo_url]
> >
> > 1_gt_logo, _metro_logo = vals.fmt_image(logo_urls, height=100)
> > gt_logo, metro_logo = html(_gt_logo), html(_metro_logo)
> >
> > (
> >     GT(metro_mini)
> >     .fmt_image("lines", path=img_url_paths, file_pattern="metro_{}.svg")
> >     .tab_header(title=gt_logo, subtitle=metro_logo)
> >     .cols_align(align="right", columns="lines")
> >     .opt_stylize(style=4, color="gray")
> > )
> > ```
> >
> > <div class="cell-annotation">
> >
> > 1  
> > <span code-cell="annotated-cell-15" code-lines="4" code-annotation="1">Note that if you need to render images with different `height` or `width`, you might need to make two separate calls to [vals.fmt_image()](../../reference/vals.fmt_image.md#great_tables.vals.fmt_image).</span>
> >
> > </div>
> >
> > <div class="cell-output cell-output-display" execution_count="16">
> >
> > <div id="ljnsvbhaua" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
> >
> > <table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
> > <thead>
> > <tr class="gt_heading">
> > <th colspan="2" class="gt_heading gt_title gt_font_normal"><span style="white-space:nowrap;"><img src="https://posit-dev.github.io/great-tables/assets/GT_logo.svg" style="height: 100px;vertical-align: middle;" /></span></th>
> > </tr>
> > <tr class="gt_heading">
> > <th colspan="2" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/rstudio/gt/master/images/dataset_metro.svg" style="height: 100px;vertical-align: middle;" /></span></th>
> > </tr>
> > <tr class="gt_col_headings">
> > <th id="name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">name</th>
> > <th id="lines" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">lines</th>
> > </tr>
> > </thead>
> > <tbody class="gt_table_body">
> > <tr>
> > <td class="gt_row gt_left">Argentine</td>
> > <td class="gt_row gt_right"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /></span></td>
> > </tr>
> > <tr>
> > <td class="gt_row gt_left gt_striped">Bastille</td>
> > <td class="gt_row gt_right gt_striped"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_5.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_8.svg" style="height: 2em;vertical-align: middle;" /></span></td>
> > </tr>
> > <tr>
> > <td class="gt_row gt_left">Bérault</td>
> > <td class="gt_row gt_right"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /></span></td>
> > </tr>
> > <tr>
> > <td class="gt_row gt_left gt_striped">Champs-Élysées--Clemenceau</td>
> > <td class="gt_row gt_right gt_striped"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_13.svg" style="height: 2em;vertical-align: middle;" /></span></td>
> > </tr>
> > <tr>
> > <td class="gt_row gt_left">Charles de Gaulle--Étoile</td>
> > <td class="gt_row gt_right"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_1.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_2.svg" style="height: 2em;vertical-align: middle;" /> <img src="https://raw.githubusercontent.com/posit-dev/great-tables/refs/heads/main/great_tables/data/metro_images/metro_6.svg" style="height: 2em;vertical-align: middle;" /></span></td>
> > </tr>
> > </tbody>
> > </table>
> >
> > </div>
> >
> > </div>
> >
> > </div>
> >
> > <div id="manually-rendering-images-anywhere" class="section level1">
> >
> > # Manually Rendering Images Anywhere
> >
> > Remember, you can always use [html()](../../reference/html.md#great_tables.html) to manually construct your desired output. For example, the previous table can be created without relying on [vals.fmt_image()](../../reference/vals.fmt_image.md#great_tables.vals.fmt_image) like this:
> >
> > <div id="27936321" class="cell" execution_count="18">
> >
> > ``` python
> > (
> >     GT(metro_mini)
> >     .fmt_image("lines", path=img_url_paths, file_pattern="metro_{}.svg")
> >     .tab_header(
> >         title=html(f'<img src="{gt_logo_url}" height="100">'),
> >         subtitle=html(f'<img src="{metro_logo_url}" height="100">'),
> >     )
> >     .cols_align(align="right", columns="lines")
> >     .opt_stylize(style=4, color="gray")
> > )
> > ```
> >
> > </div>
> >
> > Alternatively, you can manually encode the image using Python's built-in [base64](https://docs.python.org/3/library/base64.html) module, specify the appropriate MIME type and HTML attributes, and then wrap it in [html()](../../reference/html.md#great_tables.html) to display the table.
> >
> > <div id="final-words" class="section level1">
> >
> > # Final Words
> >
> > In this post, we focused on the most common use cases for rendering images in Great Tables, deliberately avoiding excessive DataFrame operations. Including such details could have overwhelmed the post with examples of string manipulations and the complexities of working with various DataFrame libraries.
> >
> > We hope you found this guide helpful and enjoyed the structured approach. Until next time, happy table creation with Great Tables!
> >
> > > **Note: Appendix: Related PRs**
> > >
> > > If you're interested in the recent enhancements we've made to image rendering, be sure to check out [\#444](https://github.com/posit-dev/great-tables/pull/444), [\#451](https://github.com/posit-dev/great-tables/pull/451) and [\#520](https://github.com/posit-dev/great-tables/pull/520) for all the details.
> >
> > </div>
> >
> > </div>
> >
> > </div>
> >
> > </div>
> >
> > </div>
> >
> > </div>
> >
> > </div>
> >
> > </div>
> >
> > </div>
>
> </div>
>
> </div>
>
> </div>
>
> </div>

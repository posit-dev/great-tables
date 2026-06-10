## vals.fmt_image()


Format image paths to generate images in cells.


Usage

``` python
vals.fmt_image(
    x,
    height=None,
    width=None,
    sep=" ",
    path=None,
    file_pattern="{}",
    encode=True
)
```


To more easily insert graphics into body cells, we can use the [fmt_image()](GT.fmt_image.md#great_tables.GT.fmt_image) method. This allows for one or more images to be placed in the targeted cells. The cells need to contain some reference to an image file, either: (1) complete http/https or local paths to the files; (2) the file names, where a common path can be provided via `path=`; or (3) a fragment of the file name, where the `file_pattern=` argument helps to compose the entire file name and `path=` provides the path information. This should be expressly used on columns that contain *only* references to image files (i.e., no image references as part of a larger block of text). Multiple images can be included per cell by separating image references by commas. The `sep=` argument allows for a common separator to be applied between images.


## Parameters


`x: X`  
A list of values to be formatted.

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


`list[str]`  
A list of formatted values is returned.

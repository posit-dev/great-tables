## system_fonts()


Get a themed font stack that works well across systems.


Usage

``` python
system_fonts(name="system-ui")
```


A font stack can be obtained from [system_fonts()](system_fonts.md#great_tables.system_fonts) using one of various keywords such as `"system-ui"`, `"old-style"`, and `"humanist"` (there are 15 in total) representing a themed set of fonts. These sets comprise a font family that has been tested to work across a wide range of computer systems.


## Parameters


`name: FontStackName = ``"system-ui"`  
The name of a font stack. Must be drawn from the set of `"system-ui"` (the default), `"transitional"`, `"old-style"`, `"humanist"`, `"geometric-humanist"`, `"classical-humanist"`, `"neo-grotesque"`, `"monospace-slab-serif"`, `"monospace-code"`, `"industrial"`, `"rounded-sans"`, `"slab-serif"`, `"antique"`, `"didone"`, and `"handwritten"`.


## Returns


`list[str]`  
A list of font names that make up the font stack.


## The Font Stacks And The Individual Fonts Used By Platform


#### System UI (`"system-ui"`)

``` css
font-family: system-ui, sans-serif;
```

The operating system interface's default typefaces are known as system UI fonts. They contain a variety of font weights, are quite readable at small sizes, and are perfect for UI elements. These typefaces serve as a great starting point for text in data tables and so this font stack is the default for **Great Tables**.

------------------------------------------------------------------------


#### Transitional (`"transitional"`)

``` css
font-family: Charter, 'Bitstream Charter', 'Sitka Text', Cambria, serif;
```

The Enlightenment saw the development of transitional typefaces, which combine Old Style and Modern typefaces. *Times New Roman*, a transitional typeface created for the Times of London newspaper, is among the most well-known instances of this style.

------------------------------------------------------------------------


#### Old Style (`"old-style"`)

``` css
font-family: 'Iowan Old Style', 'Palatino Linotype', 'URW Palladio L', P052, serif;
```

Old style typefaces were created during the Renaissance and are distinguished by diagonal stress, a lack of contrast between thick and thin strokes, and rounded serifs. *Garamond* is among the most well-known instances of an antique typeface.

------------------------------------------------------------------------


#### Humanist (`"humanist"`)

``` css
font-family: Seravek, 'Gill Sans Nova', Ubuntu, Calibri, 'DejaVu Sans', source-sans-pro, sans-serif;
```

Low contrast between thick and thin strokes and organic, calligraphic forms are traits of humanist typefaces. These typefaces, which draw their inspiration from Renaissance calligraphy, are frequently regarded as being more readable and easier to read than other sans serif typefaces.

------------------------------------------------------------------------


#### Geometric Humanist (`"geometric-humanist"`)

``` css
font-family: Avenir, Montserrat, Corbel, 'URW Gothic', source-sans-pro, sans-serif;
```

Clean, geometric forms and consistent stroke widths are characteristics of geometric humanist typefaces. These typefaces, which are frequently used for headlines and other display purposes, are frequently thought to be contemporary and slick in appearance. A well-known example of this classification is *Futura*.

------------------------------------------------------------------------


#### Classical Humanist (`"classical-humanist"`)

``` css
font-family: Optima, Candara, 'Noto Sans', source-sans-pro, sans-serif;
```

The way the strokes gradually widen as they approach the stroke terminals without ending in a serif is what distinguishes classical humanist typefaces. The stone carving on Renaissance-era tombstones and classical Roman capitals served as inspiration for these typefaces.

------------------------------------------------------------------------


#### Neo-Grotesque (`"neo-grotesque"`)

``` css
font-family: Inter, Roboto, 'Helvetica Neue', 'Arial Nova', 'Nimbus Sans', Arial, sans-serif;
```

Neo-grotesque typefaces are a form of sans serif that originated in the late 19th and early 20th centuries. They are distinguished by their crisp, geometric shapes and regular stroke widths. *Helvetica* is among the most well-known examples of a Neo-grotesque typeface.

------------------------------------------------------------------------


#### Monospace Slab Serif (`"monospace-slab-serif"`)

``` css
font-family: 'Nimbus Mono PS', 'Courier New', monospace;
```

Monospace slab serif typefaces are distinguished by their fixed-width letters, which are the same width irrespective of their shape, and their straightforward, geometric forms. For reports, tabular work, and technical documentation, this technique is used to simulate typewriter output.

------------------------------------------------------------------------


#### Monospace Code (`"monospace-code"`)

``` css
font-family: ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, 'DejaVu Sans Mono', monospace;
```

Specifically created for use in programming and other technical applications, monospace code typefaces are used in these fields. These typefaces are distinguished by their clear, readable forms and monospaced design, which ensures that all letters and characters are the same width.

------------------------------------------------------------------------


#### Industrial (`"industrial"`)

``` css
font-family: Bahnschrift, 'DIN Alternate', 'Franklin Gothic Medium', 'Nimbus Sans Narrow', sans-serif-condensed, sans-serif;
```

The development of industrial typefaces began in the late 19th century and was greatly influenced by the industrial and technological advancements of the time. Industrial typefaces are distinguished by their strong sans serif letterforms, straightforward appearance, and use of geometric shapes and straight lines.

------------------------------------------------------------------------


#### Rounded Sans (`"rounded-sans"`)

``` css
font-family: ui-rounded, 'Hiragino Maru Gothic ProN', Quicksand, Comfortaa, Manjari, 'Arial Rounded MT', 'Arial Rounded MT Bold', Calibri, source-sans-pro, sans-serif;
```

The rounded, curved letterforms that define rounded typefaces give them a softer, friendlier appearance. The typeface's rounded edges give it a more natural and playful feel, making it appropriate for use in casual or kid-friendly designs. Since the 1950s, the rounded sans-serif design has gained popularity and is still frequently used in branding, graphic design, and other fields.

------------------------------------------------------------------------


#### Slab Serif (`"slab-serif"`)

``` css
font-family: Rockwell, 'Rockwell Nova', 'Roboto Slab', 'DejaVu Serif', 'Sitka Small', serif;
```

Slab Serif typefaces are distinguished by the thick, block-like serifs that appear at the ends of each letterform. Typically, these serifs are unbracketed, which means that they do not have any curved or tapered transitions to the letter's main stroke.

------------------------------------------------------------------------


#### Antique (`"antique"`)

``` css
font-family: Superclarendon, 'Bookman Old Style', 'URW Bookman', 'URW Bookman L', 'Georgia Pro', Georgia, serif;
```

Serif typefaces that were popular in the 19th century include antique typefaces, also referred to as Egyptians. They are distinguished by their thick, uniform stroke weight and block-like serifs. The typeface *Clarendon* is a highly regarded example of this style and *Superclarendon* is a modern take on that revered typeface.

------------------------------------------------------------------------


#### Didone (`"didone"`)

``` css
font-family: Didot, 'Bodoni MT', 'Noto Serif Display', 'URW Palladio L', P052, Sylfaen, serif;
```

Didone typefaces, also referred to as Modern typefaces, are distinguished by their vertical stress, sharp contrast between thick and thin strokes, and hairline serifs without bracketing. The Didone style first appeared in the late 18th century and became well-known in the early 19th century. *Bodoni* and *Didot* are two of the most well-known typefaces in this category.

------------------------------------------------------------------------


#### Handwritten (`"handwritten"`)

``` css
font-family: 'Segoe Print', 'Bradley Hand', Chilanka, TSCu_Comic, casual, cursive;
```

The appearance and feel of handwriting are replicated by handwritten typefaces. Although there are a wide variety of handwriting styles, this font stack tends to use a more casual and commonplace style. In regards to these types of fonts in tables, one can say that any table having a handwritten font will evoke a feeling of gleefulness.


## Examples

Using select columns from the [exibble](data.exibble.md#great_tables.data.exibble) dataset, let's create a table with a number of components added. Following that, we'll set a font for the entire table using the [tab_options()](GT.tab_options.md#great_tables.GT.tab_options) method with the `table_font_names` parameter. Instead of passing a list of font names, we'll use the [system_fonts()](system_fonts.md#great_tables.system_fonts) helper function to get a font stack. In this case, we'll use the `"industrial"` font stack.


``` python
from great_tables import GT, exibble, md, system_fonts

(
  GT(
    exibble[["num", "char", "currency", "row", "group"]],
    rowname_col="row",
    groupname_col="group"
  )
  .tab_header(
    title=md("Data listing from **exibble**"),
    subtitle=md("`exibble` is a **Great Tables** dataset.")
  )
  .fmt_number(columns="num")
  .fmt_currency(columns="currency")
  .tab_source_note(source_note="This is only a subset of the dataset.")
  .opt_align_table_header(align="left")
  .tab_options(table_font_names=system_fonts("industrial"))
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">[exibble](data.exibble.md#great_tables.data.exibble) is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">$49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_right">$1,325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">$13.26</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777,000.00</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right"></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right">8,880,000.00</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">$0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This is only a subset of the dataset.</td>
</tr>
</tfoot>

</table>


Invoking the [system_fonts()](system_fonts.md#great_tables.system_fonts) helper function with the `"industrial"` argument will return a list of font names that make up the font stack. This is exactly the type of input that the `table_font_names` parameter requires.

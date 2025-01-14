<div align="center">

<a href="https://posit-dev.github.io/great-tables/"><img src="https://posit-dev.github.io/great-tables/assets/GT_logo.svg" width="350px"/></a>

_Absolutely Delightful Table-making in Python_

[![Python Versions](https://img.shields.io/pypi/pyversions/great_tables.svg)](https://pypi.python.org/pypi/great_tables)
[![PyPI](https://img.shields.io/pypi/v/great_tables)](https://pypi.org/project/great-tables/#history)
[![PyPI Downloads](https://img.shields.io/pypi/dm/great-tables)](https://pypistats.org/packages/great-tables)
[![License](https://img.shields.io/github/license/posit-dev/great-tables)](https://img.shields.io/github/license/posit-dev/great-tables)

[![CI Build](https://github.com/posit-dev/great-tables/actions/workflows/ci-tests.yaml/badge.svg)](https://github.com/posit-dev/great-tables/actions/workflows/ci-tests.yaml)
[![Codecov branch](https://img.shields.io/codecov/c/github/posit-dev/great-tables/main.svg)](https://codecov.io/gh/posit-dev/great-tables)
[![Repo Status](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![Documentation](https://img.shields.io/badge/docs-project_website-blue.svg)](https://posit-dev.github.io/great-tables/)

[![Contributors](https://img.shields.io/github/contributors/posit-dev/great-tables)](https://github.com/posit-dev/great-tables/graphs/contributors)
[![Discord](https://img.shields.io/discord/1086103944280952992?color=%237289da&label=Discord)](https://discord.com/invite/Ux7nrcXHVV)
[![pyOpenSci Peer-Reviewed](https://pyopensci.org/badges/peer-reviewed.svg)](https://github.com/pyOpenSci/software-review/issues/202)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14618357.svg)](https://doi.org/10.5281/zenodo.14618357)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.1%20adopted-ff69b4.svg)](https://www.contributor-covenant.org/version/2/1/code_of_conduct.html)

</div>

With **Great Tables** anyone can make wonderful-looking tables in Python. The philosophy here is that we can construct a wide variety of useful tables by working with a cohesive set of table components. You can mix and match things like a _header_ and _footer_, attach a _stub_ (which contains row labels), arrange _spanner labels_ over top of the _column labels_, and much more. Not only that, but you can format the cell values in a variety of awesome ways.

<div align="center">
<img src="https://posit-dev.github.io/great-tables/assets/the_components_of_a_table.svg" width="800px">
</div>

It all begins with **table data** in the form of a Pandas or Polars DataFrame. You then decide how to compose your output table with the elements and formatting you need for the task at hand. Finally, the table is rendered to HTML (the default option) or to an image file.

The **Great Tables** package is designed to be both straightforward yet powerful. The emphasis is on simple methods for the everyday display table needs (but power when you need it). Here is a brief example of how to use **Great Tables** to create a table from the included `sp500` dataset:

```python
from great_tables import GT
from great_tables.data import sp500

# Define the start and end dates for the data range
start_date = "2010-06-07"
end_date = "2010-06-14"

# Filter sp500 using Pandas to dates between `start_date` and `end_date`
sp500_mini = sp500[(sp500["date"] >= start_date) & (sp500["date"] <= end_date)]

# Create a display table based on the `sp500_mini` table data
(
    GT(sp500_mini)
    .tab_header(title="S&P 500", subtitle=f"{start_date} to {end_date}")
    .fmt_currency(columns=["open", "high", "low", "close"])
    .fmt_date(columns="date", date_style="wd_m_day_year")
    .fmt_number(columns="volume", compact=True)
    .cols_hide(columns="adj_close")
)
```

<div align="center">
<img src="https://posit-dev.github.io/great-tables/assets/gt_sp500_table.svg" width="800px">
</div>

Typically we use Great Tables in an notebook environment or within a [**Quarto**](https://quarto.org) document. Tables won't print to the console, but using the [`show()` method](https://posit-dev.github.io/great-tables/reference/GT.show.html#great_tables.GT.show) on a table object while in the console will open the HTML table in your default browser.

There are 16 datasets provided by **Great Tables**: `countrypops`, `sza`, `gtcars`, `sp500`, `pizzaplace`, `exibble`, `towny`, `peeps`, `films`, `metro`, `gibraltar`, `constants`, `illness`, `reactions`, `photolysis`, and `nuclides`.

<div align="center" style="padding-top:20px">
<img src="https://posit-dev.github.io/great-tables/assets/datasets.png" style="width:100%;">
</div>

All of this tabular data is great for experimenting with the functionality available inside **Great Tables** and we make extensive use of these datasets in our documentation.

Beyond the methods shown in the simple `sp500`-based example, there are many possible ways to create super-customized tables. Check out the [documentation website](https://posit-dev.github.io/great-tables/) to get started via introductory articles for making **Great Tables**. There's a handy _Reference_ section that has detailed help for every method and function in the package.

[![Documentation Site](https://img.shields.io/badge/Project%20Website-Documentation%20and%20Reference-blue?style=social)](https://posit-dev.github.io/great-tables/)

Let's talk about how to make **Great Tables**! There are a few locations where there is much potential for discussion.

One such place is in [_GitHub Discussions_](https://github.com/posit-dev/great-tables/discussions). This discussion board is especially great for Q&A, and many people have had their problems solved in there.

[![GitHub Discussions](https://img.shields.io/badge/GitHub%20Discussions-Ask%20about%20anything-blue?style=social&logo=github&logoColor=gray)](https://github.com/posit-dev/great-tables/discussions)

Another fine venue for discussion is in our [_Discord server_](https://discord.com/invite/Ux7nrcXHVV). This is a good option for asking about the development of **Great Tables**, pitching ideas that may become features, and sharing your table creations!

[![Discord Server](https://img.shields.io/badge/Discord-Chat%20with%20us-blue?style=social&logo=discord&logoColor=purple)](https://discord.com/invite/Ux7nrcXHVV)

Finally, there is the [_X account_](https://twitter.com/gt_package). There you'll find posts about **Great Tables** (including sneak previews about in-development features) and other table-generation packages.

[![X Follow](https://img.shields.io/twitter/follow/gt_package?style=social)](https://twitter.com/gt_package)

These are all great places to ask questions about how to use the package, discuss some ideas, engage with others, and much more!

## INSTALLATION

The **Great Tables** package can be installed from **PyPI** with:

```bash
$ pip install great_tables
```

You can also install [Great Tables from Conda-Forge](https://anaconda.org/conda-forge/great_tables) by using:

```bash
conda install conda-forge::great_tables
```

If you encounter a bug, have usage questions, or want to share ideas to make this package better, please feel free to file an [issue](https://github.com/posit-dev/great-tables/issues).

## Code of Conduct

Please note that the **Great Tables** project is released with a [contributor code of conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).<br>By participating in this project you agree to abide by its terms.

## Contributing to **Great Tables**

There are many ways to contribute to the ongoing development of the **Great Tables** package. Some contributions can be simple (like fixing typos, improving documentation, filing issues for feature requests or problems, etc.) and others might take more time and care (like answering questions and submitting PRs with code changes). Just know that anything you can do to help would be very much appreciated!

Please read over the [contributing guidelines](https://github.com/posit-dev/great-tables/blob/main/CONTRIBUTING.md) for information on how to get started.

## 📄 License

**Great Tables** is licensed under the MIT license.

© Posit Software, PBC.

## Citation

If you use **Great Tables** in your research/project/product, we would appreciate a citation to the package. You can cite the package using the following BibTeX entry:

```bibtex
@software{Iannone_great_tables,
author = {Iannone, Richard and Chow, Michael},
license = {MIT},
title = {{great-tables: Make awesome display tables using Python.}},
url = {https://github.com/posit-dev/great-tables},
version = {0.14.0}
}
```

## 🏛️ Governance

This project is primarily maintained by [Rich Iannone](https://twitter.com/riannone) and [Michael Chow](https://twitter.com/chowthedog).
Other authors may occasionally assist with some of these duties.

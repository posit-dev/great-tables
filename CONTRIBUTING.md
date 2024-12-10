# Contributing Guidelines

There are many ways to contribute to the ongoing development of the Great Tables package. Some contributions can be rather easy to do (e.g., fixing typos, improving documentation, filing issues for feature requests or problems, etc.) whereas other contributions can require more time and patience (like answering questions and submitting pull requests with code changes). Just know that that help provided in any capacity is very much appreciated. :)

## Filing Issues

If you believe you found a bug, minimal reproducible example (MRE) for your posting to the [Great Tables issue tracker](https://github.com/posit-dev/great-tables/issues). Try not to include anything unnecessary, just the minimal amount of code that constitutes the reproducible bug. For useful guidelines on how to create an MRE, take a look at [this guide on Stack Overflow](https://stackoverflow.com/help/minimal-reproducible-example). We will try to verify the bug by running the code in the provided MRE. The quality of the MRE will reduce the amount of back-and-forth communication in trying to understand how to execute the code on our systems.

## Answering questions

One way to help is by simply answering questions. It's amazing how a little conversation could lead to better insights on a problem. Don't quite know the answer? That's okay too. We're all in this together.

Where might you answer user questions? Some of the forums for Q&A on Great Tables include the _Issues_ and _Discussion_ pages in the repo. Good etiquette is key during these interactions: be a good person to all who ask questions.

### Making Pull Requests

Should you consider making a pull request (PR), please file an issue first and explain the problem in some detail. If the PR is an enhancement, detail how the change would make things better for package users. Bugfix PRs also require some explanation about the bug and how the proposed fix will remove that bug. A great way to illustrate the bug is to include an MRE. While all this upfront work prior to preparing a PR can be time-consuming it opens a line of communication with the package authors and the community, perhaps leading to a better enhancement or more effective fixes!

Once there is consensus that a PR based on the issue would be helpful, adhering to the following process will make things proceed more quickly:

- Create a separate Git branch for each PR
- Look at the build status badges before and after making changes; these badges are available in the package [README](https://github.com/posit-dev/great-tables)
- The Great Tables package follows the [Style Guide for Python Code](https://peps.python.org/pep-0008/) so please adopt those guidelines in your submitted code as best as possible
- Comment your code, particularly in those hard-to-understand areas
- Add test cases that cover the changes made in the PR; having tests for any new codepaths will help guard against regressions

### Setting Up Your Development Environment

To set up your development environment, you can follow these steps:

- Clone the posit-dev/great-tables repository
- Create a virtual environment for the folder
- Install the package in editable mode with `pip install -e .` from the root of the project folder
- Install the development dependencies with `pip install .[dev]` (have a look at the `pyproject.toml` file for the list of development dependencies)

Our documentation use `quartodoc` which in turn requires a local install of the Quarto CLI. To install Quarto, go to <https://quarto.org/docs/get-started/> to get the latest build for your platform.

We also use `ruff` for linting and formatting (this is part of our development dependencies). If using VS Code as your editor, it may be useful to install the `Ruff` extension. This will make it so any commits will pass the `pre-commit` checks. You can verify that any changes pass all pre-commit checks by running `pre-commit run --all-files`.

If you are planning to investigate or submit a PR concerning the generation of table images, you need to install additional dependencies (`selenium`and`Pillow`) and this can be done by using `pip install .[all]`.

### Building the Documentation Locally

Building the documentation can be done with `make docs-build` from the root of the project folder. Locally building the documentation site is useful when you want to see how your changes will look during iteration. The site will be built in the `docs/_site` folder.

### Running Tests Locally

The tests are located in the `tests` folder and we use `pytest` for running them. To run all of the tests, use `make test`. If you want to run a specific test file, you can use `pytest tests/test_file.py`.

If you create new tests involving snapshots, please ensure that the resulting snapshots are relatively small. After adding snapshots, use `make test-update` (this runs `pytest --snapshot-update`). A subsequent use of `make test` should pass without any issues.

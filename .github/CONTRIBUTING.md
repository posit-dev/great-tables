# Information and Guidelines for Contributing to **great_tables**

There are many ways to contribute to the ongoing development of the **great_tables** package. Some contributions can be rather easy to do (e.g., fixing typos, improving documentation, filing issues for feature requests or problems, etc.) whereas other contributions can require more time and patience (like answering questions and submitting pull requests with code changes). Just know that that help provided in any capacity is very much appreciated. :)

## Filing Issues

If you believe you found a bug, minimal reproducible example (MRE) for your posting to the [**great_tables** issue tracker](https://github.com/posit-dev/great-tables/issues). Try not to include anything unnecessary, just the minimal amount of code that constitutes the reproducible bug. We will try to verify the bug by running the code in the MRE provided. The quality of the MRE will reduce the amount of back-and-forth communication in trying to understand how to execute the code on our systems.

## Answering questions

A great way to help is by simply answering questions. It's amazing how a little conversation could lead to better insights on a problem. Don't quite know the answer? That's okay too. We're all in this together.

Where might you answer user questions? Some of the forums for Q&A on **great_tables** include the _Issues_ and _Discussion_ pages in the repo. Good etiquette is key during these interactions: be a good person to all who ask questions.

### Making Pull Requests

Should you consider making a pull request (PR), please file an issue first and explain the problem in some detail. If the PR is an enhancement, detail how the change would make things better for package users. Bugfix PRs also requre some explanation about the bug and how the proposed fix will remove that bug. A great way to illustrate the bug is to include an MRE. While all this upfront work prior to preparing a PR can be time-consuming it opens a line of communication with the package authors and the community, perhaps leading to a better enhancement or more effective fixes!

Once there is consensus that a PR based on the issue would be helpful, adhering to the following process will make things proceed more quickly:

- Create a separate Git branch for each PR.
- Look at the build status badges before and after making changes; these badges are available in the package [README](https://github.com/posit-dev/great-tables).
- The **great_tables** package follows the [Style Guide for Python Code](https://peps.python.org/pep-0008/) so please adopt those guidelines in your submitted code as best as possible.
- Comment your code, particularly in those hard-to-understand areas.
- We use **pytest** for code coverage; those contributions with test cases included are helpful and easier to accept.

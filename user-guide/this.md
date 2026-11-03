# The Zen of Great Tables

Python has a well-known easter egg: `import this` prints *The Zen of Python* ([PEP 20](https://peps.python.org/pep-0020/)). **Great Tables** took inspiration from *this* and wrote its own Zen. And since it's a Zen about tables, importing it in a notebook shows a great table:

``` python
import great_tables.this
```

[TABLE]

At the console, the import prints the aphorisms as plain text instead, just like `import this` does. To see the table from there, open it in your browser:

``` python
from great_tables.this import table

table().show()
```

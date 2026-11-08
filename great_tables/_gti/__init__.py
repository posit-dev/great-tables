"""GTI: the interactive table renderer, built on the `<gt-table>` element (packages/gti).

`GTI` tables render through it (see `great_tables/gti.py`), and so do `GT` tables made
interactive with `opt_interactive()`.
"""

from ._render import page_html, render_gti_html, spec_to_script_json
from ._spec import SPEC_VERSION, Spec, build_spec

__all__ = [
    "SPEC_VERSION",
    "Spec",
    "build_spec",
    "page_html",
    "render_gti_html",
    "spec_to_script_json",
]

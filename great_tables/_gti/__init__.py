"""GTI: the interactive table renderer, built on the `<gt-table>` element (packages/gti).

`GTI` tables render through it (see `great_tables/gti.py`); `opt_interactive()` will too.
"""

from ._render import render_gti_html, spec_to_script_json
from ._spec import SPEC_VERSION, Spec, build_spec

__all__ = ["SPEC_VERSION", "Spec", "build_spec", "render_gti_html", "spec_to_script_json"]

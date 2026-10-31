"""GTI: the interactive table renderer, built on the `<gt-table>` element (packages/gti).

Internal for now; `GTI()` and `opt_interactive()` will render through it.
"""

from ._render import render_gti_html, spec_to_script_json
from ._spec import SPEC_VERSION, Spec, build_spec

__all__ = ["SPEC_VERSION", "Spec", "build_spec", "render_gti_html", "spec_to_script_json"]

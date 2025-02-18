import warnings

from ._gt_data import GTData
from ._render import infer_render_env


class RenderWarning(Warning):
    """Base warning for render checks."""


def _render_check(data: GTData):
    if infer_render_env() == "quarto":
        _render_check(data)


def _render_check_quarto(data: GTData):
    """Check for rendering issues in Quarto.

    * Quarto uses Pandoc internally to handle tables, and Pandoc tables do not support pixel widths.
      As a result, when cols_width is used in a Quarto environment, widths need to be converted to
      percentages.
    * Alternatively, users may set the option quarto_disable_processing to True.
    * Disabling table processing also helps with pieces like table striping, but means Quarto will
      not process cross-references, etc..
    """

    # quarto_disable_processing is set, no need to warn ----
    if data._options["quarto_disable_processing"]:
        return

    # cols_widths set ----
    if any([col.column_width is not None for col in data._boxhead]):
        warnings.warn(
            "Rendering table with .col_widths() in Quarto may result in unexpected behavior."
            " This is because Quarto performs custom table processing."
            " Set .tab_options(quarto_disable_processing=True) to disable Quarto table processing.",
            RenderWarning,
        )

from ._gt_data import GTData
from great_tables.gt import _get_column_of_values, GT
from great_tables import GT
from typing import List, Any, Union, Optional


def _make_one_col_table(vals: Union[Any, List[Any]]) -> GTData:
    """
    Create a one-column table from a list of values.

    Args:
        val_list (Union[Any, List[Any]]): The list of values to be converted into a table.

    Returns:
        GTData: The GTData object representing the one-column table.
    """

    import pandas as pd

    # Upgrade a single value to a list
    if type(vals) != list:
        vals = [vals]

    # Convert the list to a Pandas DataFrame and then to a GTData object
    gt_obj = GT(pd.DataFrame({"x": vals}), auto_align=False)
    return gt_obj


def vals_fmt_number(
    vals: Union[Any, List[Any]],
    decimals: int = 2,
    n_sigfig: Optional[int] = None,
    drop_trailing_zeros: bool = False,
    drop_trailing_dec_mark: bool = True,
    use_seps: bool = True,
    scale_by: float = 1,
    pattern: str = "{x}",
    sep_mark: str = ",",
    dec_mark: str = ".",
    force_sign: bool = False,
    locale: Union[str, None] = None,
) -> List[str]:
    """
    Format numeric values.

    With numeric values in a list, we can perform number-based formatting so that the values are
    rendered with some level of precision. The following major options are available:

    - decimals: choice of the number of decimal places, option to drop trailing zeros, and a choice
    of the decimal symbol
    - digit grouping separators: options to enable/disable digit separators and provide a choice of
    separator symbol
    - scaling: we can choose to scale targeted values by a multiplier value
    - large-number suffixing: larger figures (thousands, millions, etc.) can be autoscaled and
    decorated with the appropriate suffixes
    - pattern: option to use a text pattern for decoration of the formatted values
    - locale-based formatting: providing a locale ID will result in number formatting specific to
    the chosen locale

    Parameters
    ----------
    decimals : int
        The `decimals` values corresponds to the exact number of decimal places to use. A value such
        as `2.34` can, for example, be formatted with `0` decimal places and it would result in
        `"2"`. With `4` decimal places, the formatted value becomes `"2.3400"`. The trailing zeros
        can be removed with `drop_trailing_zeros=True`. If you always need `decimals = 0`, the
        `fmt_integer()` method should be considered.
    n_sigfig : Optional[int]
        A option to format numbers to *n* significant figures. By default, this is `None` and thus
        number values will be formatted according to the number of decimal places set via
        `decimals`. If opting to format according to the rules of significant figures, `n_sigfig`
        must be a number greater than or equal to `1`. Any values passed to the `decimals` and
        `drop_trailing_zeros` arguments will be ignored.
    drop_trailing_zeros : bool
        A boolean value that allows for removal of trailing zeros (those redundant zeros after the
        decimal mark).
    drop_trailing_dec_mark : bool
        A boolean value that determines whether decimal marks should always appear even if there are
        no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By
        default trailing decimal marks are not shown.
    use_seps : bool
        The `use_seps` option allows for the use of digit group separators. The type of digit group
        separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This
        setting is `True` by default.
    scale_by : float
        All numeric values will be multiplied by the `scale_by` value before undergoing formatting.
        Since the `default` value is `1`, no values will be changed unless a different multiplier
        value is supplied.
    pattern : str
        A formatting pattern that allows for decoration of the formatted value. The formatted value
        is represented by the `{x}` (which can be used multiple times, if needed) and all other
        characters will be interpreted as string literals.
    sep_mark : str
        The string to use as a separator between groups of digits. For example, using `sep_mark=","`
        with a value of `1000` would result in a formatted value of `"1,000"`. This argument is
        ignored if a `locale` is supplied (i.e., is not `None`).
    dec_mark : str
        The string to be used as the decimal mark. For example, using `dec_mark=","` with the value
        `0.152` would result in a formatted value of `"0,152"`). This argument is ignored if a
        `locale` is supplied (i.e., is not `None`).
    force_sign : bool
        Should the positive sign be shown for positive values (effectively showing a sign for all
        values except zero)? If so, use `True` for this option. The default is `False`, where only
        negative numbers will display a minus sign. This option is disregarded when using accounting
        notation with `accounting = True`.
    locale : str
        An optional locale identifier that can be used for formatting values according the locale's
        rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).

    Returns
    -------
    GTData
        The GTData object is returned.
    """

    gt_obj: GTData = _make_one_col_table(vals=vals)

    gt_obj_fmt = gt_obj.fmt_number(
        columns="x",
        decimals=decimals,
        n_sigfig=n_sigfig,
        drop_trailing_zeros=drop_trailing_zeros,
        drop_trailing_dec_mark=drop_trailing_dec_mark,
        use_seps=use_seps,
        scale_by=scale_by,
        pattern=pattern,
        sep_mark=sep_mark,
        dec_mark=dec_mark,
        force_sign=force_sign,
        locale=locale,
    )

    vals_fmt = _get_column_of_values(gt=gt_obj_fmt, column_name="x", context="html")

    return vals_fmt

from typing import Optional, List
from dataclasses import dataclass
import re


def _generate_tokens_list(units_notation: str) -> List[str]:

    # Remove any surrounding double braces before splitting the string into a list of tokens
    tokens_list = re.split(r"\s+", re.sub(r"^\{\{\s*|\s*\}\}$", "", units_notation))

    # Remove any empty tokens (i.e., `None` or `""`)
    tokens_list = [token for token in tokens_list if token != "" and token is not None]

    # Replace any instances of `/<text>` with `<text>^-1`
    tokens_list = [
        re.sub(r"^/", "", x) + "^-1" if re.match(r"^/", x) and len(x) > 1 else x
        for x in tokens_list
    ]

    return tokens_list


@dataclass
class UnitDefinition:
    token: str
    unit: str
    unit_subscript: Optional[str] = None
    exponent: Optional[str] = None
    sub_super_overstrike: bool = False
    chemical_formula: bool = False


    def __repr__(self) -> str:
        return f"UnitDefinition({self.__dict__})"


def define_units(units_notation: str) -> List[UnitDefinition]:

    # Get a list of raw tokens
    tokens_list = _generate_tokens_list(units_notation=units_notation)

    # Initialize a list to store the units
    units_list = []

    for i in range(len(tokens_list)):

        tokens_list_i = tokens_list[i]

        unit_subscript = None
        sub_super_overstrike = False
        chemical_formula = False
        exponent = None

        if re.match(r"^%.*%$", tokens_list_i) and len(tokens_list_i) > 2:
            # Case where the unit is marked as a chemical formula

            chemical_formula = True

            # Extract the formula w/o the surrounding `%` signs
            unit = re.sub(r"^%|%$", "", tokens_list_i)

        elif re.search(r".+?\[_.+?\^.+?\]", tokens_list_i):
            # Case where both a subscript and exponent are present and
            # an overstrike arrangement is necessary

            sub_super_overstrike = True

            # Extract the unit w/o subscript from the string
            unit = re.sub(r"(.+?)\[_.+?\^.+?\]", r"\1", tokens_list_i)

            # Obtain only the subscript/exponent of the string
            sub_exponent = re.sub(r".+?\[(_.+?\^.+?)\]", r"\1", tokens_list_i)

            # Extract the content after the underscore but terminate
            # before any `^`; this is the subscript
            unit_subscript = re.sub(r"^_(.+?)(\^.+?)$", r"\1", sub_exponent)

            # Extract the content after the caret but terminate before
            # any `_`; this is the exponent
            exponent = re.sub(r"_.+?\^(.+?)", r"\1", sub_exponent)

        elif re.search(r".+?_.+?\^.+?", tokens_list_i):
            # Case where both a subscript and exponent are present and
            # the subscript is set before the exponent

            # Extract the unit w/o subscript from the string
            unit = re.sub(r"^(.+?)_.+?\^.+?$", r"\1", tokens_list_i)

            # Obtain only the subscript/exponent portion of the string
            sub_exponent = re.sub(r".+?(_.+?\^.+?)$", r"\1", tokens_list_i)

            # Extract the content after the underscore but terminate
            # before any `^`; this is the subscript
            unit_subscript = re.sub(r"^_(.+?)\^.+?$", r"\1", sub_exponent)

            # Extract the content after the caret but terminate before
            # any `_`; this is the exponent
            exponent = re.sub(r"^_.+?\^(.+?)$", r"\1", sub_exponent)

        elif re.search(r"\^", tokens_list_i):
            # Case where only an exponent is present

            # Extract the unit w/o exponent from the string
            unit = re.sub(r"^(.+?)\^.+?$", r"\1", tokens_list_i)

            # Obtain only the exponent/subscript portion of the string
            exponent = re.sub(r"^.+?\^(.+?)$", r"\1", tokens_list_i)

        elif re.search(r"_", tokens_list_i):
            # Case where only a subscript is present

            # Extract the unit w/o exponent from the string
            unit = re.sub(r"^(.+?)_.+?$", r"\1", tokens_list_i)

            # Obtain only the exponent/subscript portion of the string
            unit_subscript = re.sub(r"^.+?_(.+?)$", r"\1", tokens_list_i)
        else:
            unit = tokens_list_i

        # Create a new unit definition
        unit_definition = UnitDefinition(
            token=tokens_list_i,
            unit=unit,
            unit_subscript=unit_subscript,
            exponent=exponent,
            sub_super_overstrike=sub_super_overstrike,
            chemical_formula=chemical_formula,
        )

        # Append the unit definition to the list of units
        units_list.append(unit_definition)

    return units_list

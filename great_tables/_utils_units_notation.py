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
    built: Optional[str] = None


class UnitDefinitionList:
    def __init__(self, units_list: List[UnitDefinition]):
        self.units_list = units_list

    def __repr__(self) -> str:
        return f"UnitDefinitionList({self.__dict__})"

    def __len__(self) -> int:
        return len(self.units_list)

    def __getitem__(self, index: int) -> UnitDefinition:
        return self.units_list[index]

    def to_html(self) -> str:

        from great_tables._text import _md_html

        for i in range(len(self)):

            units_str_i = ""

            units_object_i = self[i]
            unit = units_object_i.unit
            unit_subscript = units_object_i.unit_subscript
            exponent = units_object_i.exponent
            sub_super_overstrike = units_object_i.sub_super_overstrike
            chemical_formula = units_object_i.chemical_formula

            if "x10" in unit and not chemical_formula:
                unit = unit.replace("x", "&times;")

            unit = _units_symbol_replacements(text=unit)

            if len(unit) > 2 and "*" in unit:

                unit = _md_html(unit)

            if unit_subscript is not None and len(unit_subscript) > 2 and "*" in unit_subscript:

                unit_subscript = _units_symbol_replacements(text=unit_subscript)
                unit_subscript = _md_html(unit_subscript)

            if exponent is not None and len(exponent) > 2 and "*" in exponent:

                exponent = _units_symbol_replacements(text=exponent)
                exponent = _md_html(exponent)

            units_str_i += unit

            if sub_super_overstrike and unit_subscript is not None and exponent is not None:

                exponent = exponent.replace("-", "&minus;")

                units_str_i += _units_html_sub_super(
                    content_sub=unit_subscript, content_sup=exponent
                )

            elif chemical_formula:

                units_str_i = re.sub(
                    "(\\d+)",
                    '<span style="white-space:nowrap;"><sub>\\1</sub></span>',
                    units_str_i,
                )

            else:

                if unit_subscript is not None:

                    unit_subscript = _units_to_subscript(content=unit_subscript)
                    units_str_i += unit_subscript

                if exponent is not None:

                    exponent = exponent.replace("-", "&minus;")

                    exponent = _units_to_superscript(content=exponent)
                    units_str_i += exponent

            self[i].built = units_str_i

        units_str = ""

        units_object = self.units_list

        for i in range(len(units_object)):

            unit_add = units_object[i].built

            if re.search("\\($|\\[$", units_str) or re.search("^\\)|^\\]", unit_add):
                spacer = ""
            else:
                spacer = " "

            if len(units_object) == 3 and units_object[1].unit == "/":
                spacer = ""

            units_str += f"{spacer}{unit_add}"

        units_str = re.sub("^\\s+|\\s+$", "", units_str)

        return units_str


def _units_to_subscript(content: str) -> str:
    return '<span style="white-space:nowrap;"><sub>' + content + "</sub></span>"


def _units_to_superscript(content: str) -> str:
    return '<span style="white-space:nowrap;"><sup>' + content + "</sup></span>"


def _units_html_sub_super(content_sub: str, content_sup: str) -> str:
    return (
        '<span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">'
        + content_sup
        + "<br>"
        + content_sub
        + "</span>"
    )


def _replace_units_symbol(text: str, detect: str, pattern: str, replace: str) -> str:

    if re.search(detect, text):
        text = re.sub(pattern, replace, text)

    return text


def _units_symbol_replacements(text: str) -> str:

    # Replace certain units symbols with HTML entities; these are cases where the parsed
    # text should be at the beginning of a string (or should be the entire string)
    text = _replace_units_symbol(text, "^-", "^-", "&minus;")
    text = _replace_units_symbol(text, "^um$", "um", "&micro;m")
    text = _replace_units_symbol(text, "^uL$", "uL", "&micro;L")
    text = _replace_units_symbol(text, "^umol", "^umol", "&micro;mol")
    text = _replace_units_symbol(text, "^ug$", "ug", "&micro;g")
    text = _replace_units_symbol(text, "^ohm$", "ohm", "&#8486;")

    # Loop through the dictionary of units symbols and replace them with their HTML entities
    for key, value in UNITS_SYMBOLS_HTML.items():
        text = _replace_units_symbol(text, key, key, value)

    return text


UNITS_SYMBOLS_HTML = {
    "degC": "&deg;C",
    "degF": "&deg;F",
    ":pm:": "&plusmn;",
    ":mp:": "&mnplus;",
    ":lt:": "&lt;",
    ":gt:": "&gt;",
    ":le:": "&le;",
    ":ge:": "&ge;",
    ":cdot:": "&sdot;",
    ":times:": "&times;",
    ":div:": "&divide;",
    ":ne:": "&ne;",
    ":prime:": "&prime;",
    ":rightarrow:": "&rarr;",
    ":leftarrow:": "&larr;",
    ":micro:": "&micro;",
    ":ohm:": "&#8486;",
    ":angstrom:": "&#8491;",
    ":times:": "&times;",
    ":plusminus:": "&plusmn;",
    ":permil:": "&permil;",
    ":permille:": "&permil;",
    ":degree:": "&deg;",
    ":degrees:": "&deg;",
    ":space:": "&nbsp;",
    ":Alpha:": "&Alpha;",
    ":alpha:": "&alpha;",
    ":Beta:": "&Beta;",
    ":beta:": "&beta;",
    ":Gamma:": "&Gamma;",
    ":gamma:": "&gamma;",
    ":Delta:": "&Delta;",
    ":delta:": "&delta;",
    ":Epsilon:": "&Epsilon;",
    ":epsilon:": "&epsilon;",
    ":varepsilon:": "&varepsilon;",
    ":Zeta:": "&Zeta;",
    ":zeta:": "&zeta;",
    ":Eta:": "&Eta;",
    ":eta:": "&eta;",
    ":Theta:": "&Theta;",
    ":theta:": "&theta;",
    ":vartheta:": "&vartheta;",
    ":Iota:": "&Iota;",
    ":iota:": "&iota;",
    ":Kappa:": "&Kappa;",
    ":kappa:": "&kappa;",
    ":Lambda:": "&Lambda;",
    ":lambda:": "&lambda;",
    ":Mu:": "&Mu;",
    ":mu:": "&mu;",
    ":Nu:": "&Nu;",
    ":nu:": "&nu;",
    ":Xi:": "&Xi;",
    ":xi:": "&xi;",
    ":Omicron:": "&Omicron;",
    ":omicron:": "&omicron;",
    ":Pi:": "&Pi;",
    ":pi:": "&pi;",
    ":Rho:": "&Rho;",
    ":rho:": "&rho;",
    ":Sigma:": "&Sigma;",
    ":sigma:": "&sigma;",
    ":sigmaf:": "&sigmaf;",
    ":varsigma:": "&varsigma;",
    ":Tau:": "&Tau;",
    ":tau:": "&tau;",
    ":Upsilon:": "&Upsilon;",
    ":upsilon:": "&upsilon;",
    ":Phi:": "&Phi;",
    ":phi:": "&phi;",
    ":Chi:": "&Chi;",
    ":chi:": "&chi;",
    ":Psi:": "&Psi;",
    ":psi:": "&psi;",
    ":Omega:": "&Omega;",
    ":omega:": "&omega;",
}


def define_units(units_notation: str) -> UnitDefinitionList:

    # Get a list of raw tokens
    tokens_list = _generate_tokens_list(units_notation=units_notation)

    # Initialize a list to store the units
    units_list = []

    if len(tokens_list) == 0:
        return UnitDefinitionList(units_list=[])

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

    return UnitDefinitionList(units_list=units_list)

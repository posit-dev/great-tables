import re


def generate_tokens_list(units_notation: str) -> List[str]:

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

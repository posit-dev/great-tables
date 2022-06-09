from typing import Optional


def heading_has_title(title: Optional[str]) -> bool:
    if title is None:
        return False
    else:
        return True


def heading_has_subtitle(subtitle: Optional[str]) -> bool:
    if subtitle is None:
        return False
    else:
        return True


class Heading:
    title: Optional[str] = None
    subtitle: Optional[str] = None
    preheader: Optional[str] = None

    def __init__(self):
        pass

    def create_heading_component(self) -> str:

        # If there is no title or heading component, then return an empty string
        if heading_has_title(title=self.title) is False:
            return ""

        title = self.title
        subtitle_defined = heading_has_subtitle(subtitle=self.subtitle)

        # TODO: Get effective number of columns
        # This cannot yet be done but we need a way to effectively count the
        # number of columns that will finally be rendered
        # e.g., n_cols_total = self._get_effective_number_of_columns(data=data)
        n_cols_total = 2

        heading_rows = f"""  <tr>
    <th colspan="{n_cols_total}" class="gt_heading gt_title gt_font_normal">{title}
  </tr>"""

        if subtitle_defined:

            subtitle = self.subtitle

            subtitle_row = f"""  <tr>
    <th colspan="{n_cols_total}" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">{subtitle}
  </tr>"""
            heading_rows = f"""{heading_rows}\n{subtitle_row}"""

        heading_component = f"""<thead class=\"gt_header\">{heading_rows}</thead>"""

        return heading_component


class HeadingAPI:
    _heading: Heading

    def __init__(self):
        self._heading = Heading()

    def tab_header(
        self,
        title: str,
        subtitle: Optional[str] = None,
        preheader: Optional[str] = None,
    ):
        self._heading.title = title
        self._heading.subtitle = subtitle
        self._heading.preheader = preheader

        return self

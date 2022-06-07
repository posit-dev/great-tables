from typing import Optional


class Heading:
    title: Optional[str] = None
    subtitle: Optional[str] = None
    preheader: Optional[str] = None

    def __init__(self):
        pass

    def create_heading_component(self):

        # If there is no title or heading component, then return an empty string
        if self.title is None:
            return ""

        # TODO: Get effective number of columns
        # This cannot yet be done but we need a way to effectively count the
        # number of columns that will finally be rendered
        # e.g., n_cols_total = self._get_effective_number_of_columns(data=data)
        n_cols_total = 2

        title_row = f"""  <tr>
    <th colspan=\"{n_cols_total}\">{self.title}
  </tr>"""

        heading_component = f"""<thead class=\"gt_header\">{title_row}</thead>"""

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

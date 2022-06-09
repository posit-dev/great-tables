from typing import List


class SourceNotes:
    source_notes: List[str] = []

    def __init__(self):
        pass

    def create_source_notes_component(self) -> str:

        source_notes = self.source_notes

        # If there are no source notes, then return an empty string
        if source_notes == []:
            return ""

        # TODO: Obtain the `multiline` option from `_options`
        multiline = True

        # TODO: Obtain the `separator` option from `_options`
        separator = " "

        # TODO: Get effective number of columns
        # This cannot yet be done but we need a way to effectively count the
        # number of columns that will finally be rendered
        # e.g., n_cols_total = self._get_effective_number_of_columns(data=data)
        n_cols_total = 2

        # Handle the multiline source notes case (each footnote takes up one line)
        if multiline:

            # Create the source notes component as a series of `<tr><td>` (one per
            # source note) inside of a `<tfoot>`

            source_notes_tr: List[str] = []

            for note in source_notes:
                source_notes_tr.append(
                    f"""
  <tr>
    <td class="gt_sourcenote" colspan="{n_cols_total}">{note}</td>
  </tr>
"""
                )

            source_notes_joined = "\n".join(source_notes_tr)

            source_notes_component = f"""  <tfoot class="gt_sourcenotes">
  {source_notes_joined}
</tfoot>"""

            return source_notes_component

        # TODO: Perform HTML escaping on the separator text and
        # transform space characters to non-breaking spaces

        # Create the source notes component as a single `<tr><td>` inside
        # of a `<tfoot>`

        source_notes_str_joined = separator.join(source_notes)

        source_notes_component = f"""<tfoot>
  <tr class="gt_sourcenotes">
    <td class="gt_sourcenote" colspan="{n_cols_total}">
      <div style="padding-bottom:2px;">{source_notes_str_joined}</div>
    </td>
  </tr>
</tfoot>
        """

        return source_notes_component


class SourceNotesAPI:
    _source_notes: SourceNotes

    def __init__(self):
        self._source_notes = SourceNotes()

    def tab_source_note(self, source_note: str):

        if self._source_notes.source_notes == []:
            self._source_notes.source_notes = [source_note]
        elif type(self._source_notes.source_notes) is list:
            self._source_notes.source_notes.append(source_note)

        return self

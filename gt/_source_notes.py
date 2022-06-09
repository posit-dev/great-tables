from typing import Optional, List


class SourceNotes:
    source_notes: Optional[List[str]] = []

    def __init__(self):
        pass


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

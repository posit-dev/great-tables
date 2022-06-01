from typing import Optional, List


class SourceNotes:
    source_notes: Optional[List[str]]

    def __init__(self):
        pass


class SourceNotesAPI:
    _source_notes: SourceNotes

    def __init__(self):
        self._source_notes = SourceNotes()

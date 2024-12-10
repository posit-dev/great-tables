from __future__ import annotations

from ._locations import (
    #
    # Body ----
    LocBody as body,
)
from ._locations import (
    #
    # Column Labels ----
    LocColumnHeader as column_header,
)
from ._locations import (
    LocColumnLabels as column_labels,
)
from ._locations import (
    #
    # Footer ----
    LocFooter as footer,
)
from ._locations import (
    # Header ----
    LocHeader as header,
)
from ._locations import (
    LocRowGroups as row_groups,
)
from ._locations import (
    LocSourceNotes as source_notes,
)
from ._locations import (
    LocSpannerLabels as spanner_labels,
)
from ._locations import (
    #
    # Stub ----
    LocStub as stub,
)
from ._locations import (
    #
    # Stubhead ----
    LocStubhead as stubhead,
)
from ._locations import (
    LocSubTitle as subtitle,
)
from ._locations import (
    LocTitle as title,
)

__all__ = (
    "header",
    "title",
    "subtitle",
    "stubhead",
    "column_header",
    "spanner_labels",
    "column_labels",
    "stub",
    "row_groups",
    "body",
    "footer",
    "source_notes",
)

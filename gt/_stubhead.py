from typing import Optional


class Stubhead:
    stubhead: Optional[str]

    def __init__(self):
        pass


class StubheadAPI:
    _stubhead: Stubhead

    def __init__(self):
        self._stubhead = Stubhead()

    # TODO: create the `tab_stubhead()` function

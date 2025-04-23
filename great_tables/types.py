from typing import Literal

from typing_extensions import TypeAlias


ColumnAlignment: TypeAlias = Literal["left", "center", "right", "justify"]

RenderTargets: TypeAlias = Literal["auto", "notebook", "browser"]

RenderEnvs: TypeAlias = Literal[
    "quarto", "databricks", "ipython_terminal", "vscode", "positron", "default"
]

WebDrivers: TypeAlias = Literal["chrome", "firefox", "safari", "edge"]

HTMLContext: TypeAlias = Literal["html"]

DebugDumpOptions: TypeAlias = Literal["zoom", "width_resize", "final_resize"]

PlacementOptions: TypeAlias = Literal["auto", "left", "right"]

NullMeans = Literal["everything", "nothing"]

RowNameAttrs = Literal["rowname", "group_id"]

FontStackName: TypeAlias = Literal[
    "system-ui",
    "transitional",
    "old-style",
    "humanist",
    "geometric-humanist",
    "classical-humanist",
    "neo-grotesque",
    "monospace-slab-serif",
    "monospace-code",
    "industrial",
    "rounded-sans",
    "slab-serif",
    "antique",
    "didone",
    "handwritten",
]

DateStyle: TypeAlias = Literal[
    "iso",
    "wday_month_day_year",
    "wd_m_day_year",
    "wday_day_month_year",
    "month_day_year",
    "m_day_year",
    "day_m_year",
    "day_month_year",
    "day_month",
    "day_m",
    "year",
    "month",
    "day",
    "year.mn.day",
    "y.mn.day",
    "year_week",
    "year_quarter",
]

TimeStyle: TypeAlias = Literal[
    "iso",
    "iso-short",
    "h_m_s_p",
    "h_m_p",
    "h_p",
]

PlotType: TypeAlias = Literal[
    "line",
    "bar",
]

MissingVals: TypeAlias = Literal[
    "marker",
    "gap",
    "zero",
    "remove",
]

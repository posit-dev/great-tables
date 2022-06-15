import pandas as pd
import gt
from IPython.display import display, HTML

pd_data = pd.DataFrame([{"a": 5, "b": 15}, {"a": 15, "b": 2000}])

# gt_tbl = gt.GT(pd_data)
# gt_tbl = gt.GT(pd_data).tab_header(title="Title of Table")
gt_tbl = (
    gt.GT(pd_data)
    .tab_header(title="Title", subtitle="Subtitle")
    .tab_source_note("Source Note 1")
    .tab_source_note("Source Note 2")
    .tab_options(table_width="720px", table_font_size="16px")
    .opt_row_striping(row_striping=True)
)

print(gt_tbl.render())

display(HTML(gt_tbl.render()))

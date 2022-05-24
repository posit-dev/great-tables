import gt

data = [{"a": 5, "b": 10}, {"a": 15, "b": 20}]

gt_tbl = gt.GT(data).tab_header(title="Title of Table")

print(gt_tbl.render())

# print(GT(data))
# print(GT(data)._data)
# print(GT(data)._has_built)
# print(GT(data)._locale)
# print(GT(data)._heading)

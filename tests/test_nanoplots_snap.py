from great_tables._utils_nanoplots import _generate_nanoplot


# ---------------------------------------------------------------------------
# Test data
# ---------------------------------------------------------------------------

# Simple gap in the middle
Y_MIDDLE_GAP = [
    1.0,
    2.0,
    3.0,
    4.0,
    float("nan"),
    float("nan"),
    float("nan"),
    8.0,
    9.0,
    10.0,
    11.0,
    12.0,
]

# Gap at the start
Y_START_GAP = [float("nan"), float("nan"), 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]

# Gap at the end
Y_END_GAP = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, float("nan"), float("nan")]

# Multiple gaps
Y_MULTI_GAP = [
    1.0,
    2.0,
    float("nan"),
    4.0,
    5.0,
    float("nan"),
    float("nan"),
    8.0,
    9.0,
    float("nan"),
    11.0,
    12.0,
]

# Alternating values and gaps
Y_ALTERNATING = [
    1.0,
    float("nan"),
    3.0,
    float("nan"),
    5.0,
    float("nan"),
    7.0,
    float("nan"),
    9.0,
    float("nan"),
    11.0,
    float("nan"),
]

# Negative values with gaps
Y_NEGATIVE_GAP = [-3.0, -1.0, float("nan"), 2.0, 4.0, float("nan"), -2.0, 1.0, 3.0, 5.0]


# ---------------------------------------------------------------------------
# Line plot snapshots — curved
# ---------------------------------------------------------------------------


def test_snap_line_gap_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, missing_vals="gap")
    assert snapshot == result


def test_snap_line_gap_start(snapshot):
    result = _generate_nanoplot(y_vals=Y_START_GAP, missing_vals="gap")
    assert snapshot == result


def test_snap_line_gap_end(snapshot):
    result = _generate_nanoplot(y_vals=Y_END_GAP, missing_vals="gap")
    assert snapshot == result


def test_snap_line_gap_multiple(snapshot):
    result = _generate_nanoplot(y_vals=Y_MULTI_GAP, missing_vals="gap")
    assert snapshot == result


def test_snap_line_gap_alternating(snapshot):
    result = _generate_nanoplot(y_vals=Y_ALTERNATING, missing_vals="gap")
    assert snapshot == result


def test_snap_line_gap_negative(snapshot):
    result = _generate_nanoplot(y_vals=Y_NEGATIVE_GAP, missing_vals="gap")
    assert snapshot == result


# ---------------------------------------------------------------------------
# Line plot snapshots — straight
# ---------------------------------------------------------------------------


def test_snap_line_straight_gap_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, missing_vals="gap", data_line_type="straight")
    assert snapshot == result


def test_snap_line_straight_gap_multiple(snapshot):
    result = _generate_nanoplot(y_vals=Y_MULTI_GAP, missing_vals="gap", data_line_type="straight")
    assert snapshot == result


# ---------------------------------------------------------------------------
# Line plot snapshots — marker
# ---------------------------------------------------------------------------


def test_snap_line_marker_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, missing_vals="marker")
    assert snapshot == result


def test_snap_line_marker_alternating(snapshot):
    result = _generate_nanoplot(y_vals=Y_ALTERNATING, missing_vals="marker")
    assert snapshot == result


# ---------------------------------------------------------------------------
# Line plot snapshots — zero
# ---------------------------------------------------------------------------


def test_snap_line_zero_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, missing_vals="zero")
    assert snapshot == result


# ---------------------------------------------------------------------------
# Line plot snapshots — remove
# ---------------------------------------------------------------------------


def test_snap_line_remove_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, missing_vals="remove")
    assert snapshot == result


# ---------------------------------------------------------------------------
# Bar plot snapshots
# ---------------------------------------------------------------------------


def test_snap_bar_gap_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, plot_type="bar", missing_vals="gap")
    assert snapshot == result


def test_snap_bar_gap_multiple(snapshot):
    result = _generate_nanoplot(y_vals=Y_MULTI_GAP, plot_type="bar", missing_vals="gap")
    assert snapshot == result


def test_snap_bar_gap_alternating(snapshot):
    result = _generate_nanoplot(y_vals=Y_ALTERNATING, plot_type="bar", missing_vals="gap")
    assert snapshot == result


def test_snap_bar_gap_negative(snapshot):
    result = _generate_nanoplot(y_vals=Y_NEGATIVE_GAP, plot_type="bar", missing_vals="gap")
    assert snapshot == result


def test_snap_bar_marker_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, plot_type="bar", missing_vals="marker")
    assert snapshot == result


def test_snap_bar_zero_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, plot_type="bar", missing_vals="zero")
    assert snapshot == result


def test_snap_bar_remove_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, plot_type="bar", missing_vals="remove")
    assert snapshot == result

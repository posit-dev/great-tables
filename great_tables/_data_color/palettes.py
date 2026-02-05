"""Palette classes for translating data to color values.

Note that this code is largely a pure python port of the mizani gradient_n_pal code.
"""

from __future__ import annotations

from bisect import bisect
from math import isinf, isnan
from typing import TypedDict

from great_tables._utils import pairwise

from .base import RGBColor, _hex_to_rgb, _html_color


def rgb_to_hex(rgb: RGBColor) -> str:
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


# data ---------------------------------------------------------------------------------------------


class GradientCoefficients(TypedDict):
    """Coefficients for a gradient color map.

    Parameters
    ----------
    starting:
        The value at which these coefficients start to apply.
    intercept:
        The outcome when the value is equal to starting.
    scalar:
        The rate at which the outcome changes as the value increases.
    """

    starting: float
    intercept: int
    scalar: float


# coefficient lookup classes -----------------------------------------------------------------------


class CoeffSequence:
    """Return the coefficients for transforming an input to RGB."""

    coeffs: list[GradientCoefficients]

    def __init__(self, coeffs: list[GradientCoefficients]):
        self.coeffs = coeffs

    def lookup(self, x: float) -> GradientCoefficients:
        for coeff in reversed(self.coeffs):
            if x >= coeff["starting"]:
                return coeff

        raise ValueError("No coefficients found for this value.")


class CoeffSequenceBisector(CoeffSequence):
    """Use a bisect search to find coefficients."""

    starting: list[float]
    coeffs: list[GradientCoefficients]

    def __init__(self, coeffs: list[GradientCoefficients]):
        self.starting = [coeff["starting"] for coeff in coeffs]
        self.coeffs = coeffs

    def lookup(self, x: float) -> GradientCoefficients:
        idx = bisect(self.starting, x) - 1
        return self.coeffs[idx]


# palettes -----------------------------------------------------------------------------------------


class GradientPalette:
    """A palette that interpolates between colors using a linear gradient on RBG channels.

    Parameters
    ----------
    colors:
        The colors to interpolate between, as hex strings.
    values:
        The value cutoffs for switching between colors. By default these are evenly spaced.
    """

    colors: list[RGBColor]
    values: list[float]

    def __init__(
        self,
        colors: list[str],
        values: "list[float] | None" = None,
        cls_coeff_sequence: "type[CoeffSequence]" = CoeffSequenceBisector,
    ):
        if len(colors) < 2:
            raise ValueError(
                f"Palette requires at least 2 colors, but only {len(colors)} provided."
            )

        if values is None:
            values = self._linspace_to_one(len(colors))
        elif len(values) < 2 or values[0] != 0 or values[-1] != 1:
            raise ValueError("Values must be at least length 2, start with 0, and end with 1.")

        if len(values) != len(colors):
            raise ValueError(
                "Values and colors must be the same length. "
                f"Received {len(values)} values and {len(colors)} colors."
            )

        # colors can be rgb tuples or hex strings
        if isinstance(colors[0], str):
            rgb_colors: "list[RGBColor]" = [_hex_to_rgb(color) for color in _html_color(colors)]
        else:
            raise NotImplementedError("Currently, rgb tuples can't be passed directly.")

        self.colors = rgb_colors
        self.values = values
        self.cls_coeff_sequence = cls_coeff_sequence
        self._r_coeffs = self._create_coefficients(values, [x[0] for x in rgb_colors])
        self._g_coeffs = self._create_coefficients(values, [x[1] for x in rgb_colors])
        self._b_coeffs = self._create_coefficients(values, [x[2] for x in rgb_colors])

    def __call__(self, data: list[float]) -> "list[str | None]":
        """Return data transformed to hex color values."""

        rgb = self.vals_to_rgb(data)
        return [rgb_to_hex(x) if x is not None else None for x in rgb]

    def vals_to_rgb(self, data: list[float | None]) -> "list[RGBColor | None]":
        """Return data transformed to RGB values."""

        out: "list[RGBColor | None]" = []
        for ii, x in enumerate(data):
            if x is None:
                out.append(None)
                continue

            if isinf(x) or isnan(x):
                out.append(None)
                continue

            if x < 0 or x > 1:
                raise ValueError(f"Element {ii} is outside the range [0, 1]. Value: {x}.")

            r = self._interpolate(x, self._r_coeffs)
            g = self._interpolate(x, self._g_coeffs)
            b = self._interpolate(x, self._b_coeffs)
            out.append((round(r), round(g), round(b)))

        return out

    @staticmethod
    def _linspace_to_one(n_steps: int) -> list[float]:
        # equivalent to np.linspace(0, 1, n_steps)
        increment = 1 / (n_steps - 1)
        return [x * increment for x in range(n_steps)]

    def _create_coefficients(self, cutoffs: list[float], channel: list[int]) -> CoeffSequence:
        """Return coefficients for interpolating between cutoffs on a color channel."""

        coeffs: list[GradientCoefficients] = []
        for (prev_cutoff, crnt_cutoff), (prev_color, crnt_color) in zip(
            pairwise(cutoffs), pairwise(channel)
        ):
            cutoff_diff = crnt_cutoff - prev_cutoff
            color_scalar = (crnt_color - prev_color) / cutoff_diff

            coeffs.append(
                {"scalar": color_scalar, "intercept": prev_color, "starting": prev_cutoff}
            )

        return self.cls_coeff_sequence(coeffs)

    @staticmethod
    def _interpolate(x: float, coeffs: CoeffSequence) -> float:
        coeff = coeffs.lookup(x)
        return coeff["scalar"] * (x - coeff["starting"]) + coeff["intercept"]

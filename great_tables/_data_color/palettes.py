"""Palette classes for translating data to color values.

Note that this code is largely a pure python port of the mizani gradient_n_pal code, interpolating
in CIELAB as R's `scales::colour_ramp()` (used by R gt's `data_color()`) does.
"""

from __future__ import annotations

from bisect import bisect
from math import isinf, isnan
from typing import TypedDict

from great_tables._utils import pairwise

from .base import RGBColor, _hex_to_rgb, _html_color


def rgb_to_hex(rgb: RGBColor) -> str:
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


# CIELAB conversions -------------------------------------------------------------------------------
#
# These follow the conversions of the `farver` R package (used by `scales::colour_ramp()`), so that
# interpolated colors match R gt's exactly: sRGB companding, the sRGB/XYZ matrices, and a D65 white
# reference.

LabColor = tuple[float, float, float]

_D65_WHITE = (95.047, 100.0, 108.883)


def _rgb_to_lab(rgb: RGBColor) -> LabColor:
    def linearize(channel: int) -> float:
        c = channel / 255
        return (((c + 0.055) / 1.055) ** 2.4 if c > 0.04045 else c / 12.92) * 100

    r, g, b = (linearize(channel) for channel in rgb)
    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041

    def f(t: float) -> float:
        return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116

    fx, fy, fz = f(x / _D65_WHITE[0]), f(y / _D65_WHITE[1]), f(z / _D65_WHITE[2])

    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def _lab_to_rgb(lab: LabColor) -> RGBColor:
    lightness, a, b = lab
    fy = (lightness + 16) / 116
    fx = a / 500 + fy
    fz = fy - b / 200

    def f_inv(t: float) -> float:
        t3 = t**3
        return t3 if t3 > 0.008856 else (t - 16 / 116) / 7.787

    x = f_inv(fx) * _D65_WHITE[0] / 100
    y = f_inv(fy) * _D65_WHITE[1] / 100
    z = f_inv(fz) * _D65_WHITE[2] / 100

    linear = (
        x * 3.2404542 + y * -1.5371385 + z * -0.4985314,
        x * -0.9692660 + y * 1.8760108 + z * 0.0415560,
        x * 0.0556434 + y * -0.2040259 + z * 1.0572252,
    )

    def compand(c: float) -> int:
        c = 1.055 * c ** (1 / 2.4) - 0.055 if c > 0.0031308 else 12.92 * c
        return min(255, max(0, round(c * 255)))

    r, g, b = (compand(c) for c in linear)
    return r, g, b


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
    intercept: float
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
    """A palette that interpolates between colors using a linear gradient in CIELAB.

    Interpolating in CIELAB (rather than on RGB channels) gives perceptually even gradients and the
    same colors as R gt (via `scales::colour_ramp()`).

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

        lab_colors = [_rgb_to_lab(color) for color in rgb_colors]
        self._l_coeffs = self._create_coefficients(values, [x[0] for x in lab_colors])
        self._a_coeffs = self._create_coefficients(values, [x[1] for x in lab_colors])
        self._b_coeffs = self._create_coefficients(values, [x[2] for x in lab_colors])

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

            lab = (
                self._interpolate(x, self._l_coeffs),
                self._interpolate(x, self._a_coeffs),
                self._interpolate(x, self._b_coeffs),
            )
            out.append(_lab_to_rgb(lab))

        return out

    @staticmethod
    def _linspace_to_one(n_steps: int) -> list[float]:
        # equivalent to np.linspace(0, 1, n_steps)
        increment = 1 / (n_steps - 1)
        return [x * increment for x in range(n_steps)]

    def _create_coefficients(self, cutoffs: list[float], channel: list[float]) -> CoeffSequence:
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

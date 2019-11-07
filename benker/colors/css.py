# coding: utf-8
"""
CSS Colors names
================
"""
from __future__ import print_function

import re

from benker.colors.const import CMYK_SCALE
from benker.colors.const import CSS_COLOR_NAMES
from benker.colors.const import HUE_SCALE
from benker.colors.const import RGB_SCALE
from benker.colors.rgb import rgba_to_cmyka
from benker.colors.rgb import rgba_to_hsla

_COLOR_NAME_REGEX = "|".join(sorted(CSS_COLOR_NAMES, key=lambda n: -len(n)))

_match_css_name = re.compile(r"^{}$".format(_COLOR_NAME_REGEX), flags=re.I).match
_match_percent_name = re.compile(r"^(P<percent>.+?)%(P<name>{})$".format(_COLOR_NAME_REGEX), flags=re.I).match


def parse_css_name(text):
    # type: (str) -> (str, float)
    mo = _match_css_name(text)
    if mo:
        color_name = mo.group()
        return color_name, 1
    if "%" in text:
        percent, text = text.split("%", 1)
        color_name = parse_css_name(text)[0]
        percent = float(percent) / 100
        if 0 <= percent <= 1:
            return color_name, percent
    raise ValueError(text)


def css_name_to_rgba(text, rgb_scale=RGB_SCALE):
    color_name, percent = parse_css_name(text)
    r, g, b = CSS_COLOR_NAMES[color_name.lower()]
    z = rgb_scale / RGB_SCALE
    r *= z * percent
    g *= z * percent
    b *= z * percent
    return r, g, b, None


def css_name_to_hsla(text, hue_scale=HUE_SCALE):
    color_name, percent = parse_css_name(text)
    r, g, b = CSS_COLOR_NAMES[color_name.lower()]
    h, s, l, a = rgba_to_hsla(r * percent, g * percent, b * percent, hue_scale=hue_scale)
    return h, s, l, a


def css_name_to_cmyka(text, cmyk_scale=CMYK_SCALE):
    color_name, percent = parse_css_name(text)
    r, g, b = CSS_COLOR_NAMES[color_name.lower()]
    c, m, y, k, a = rgba_to_cmyka(r * percent, g * percent, b * percent, cmyk_scale=cmyk_scale)
    return c, m, y, k, a

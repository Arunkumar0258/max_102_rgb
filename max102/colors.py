# src/max102/colors.py

from enum import IntEnum


class Color(IntEnum):
    RED = 0
    YELLOW = 43
    GREEN = 85
    BLUE = 170
    PURPLE = 213


def volume_to_hue(value: float):

    if value < 0.05:
        return Color.RED

    if value < 0.10:
        return Color.YELLOW

    if value < 0.20:
        return Color.GREEN

    if value < 0.35:
        return Color.BLUE

    return Color.PURPLE

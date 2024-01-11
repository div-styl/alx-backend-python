#!/usr/bin/env python3
"""
function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that returns a new function that multiplier float by multiplier
    :param multiplier:
    :return: function mf
    """

    def mf(num: float) -> float:
        return float(num * multiplier)

    return mf

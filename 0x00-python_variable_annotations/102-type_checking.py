#!/usr/bin/env python3
"""REFORM THE CODE TYPING"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Generates a zoomed-in version of the given list by
    repeating each item a specified number of times.

    Parameters:
    - lst (Tuple): The list to be zoomed in.
    - factor (int): The number of times each item in
    the list should be repeated. Default is 2.

    Returns:
    - zoomed_in (List): The zoomed-in version of the list
    with each item repeated according to the factor.

    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

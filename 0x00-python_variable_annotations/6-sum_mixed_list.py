#!/usr/bin/env python3
"""
sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum_mixed_list which takes a list mxd_lst
    of integers and floats and returns their sum as a float.
    """
    return sum(mxd_lst)

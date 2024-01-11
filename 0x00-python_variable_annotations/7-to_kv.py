#!/usr/bin/env python3
"""
 function to_kv that takes a string k
 and an int OR float v as arguments
 and returns a tuple. The first element of the
 tuple is the string k. The second element is the square
 of the int/float v and should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Generates a tuple where the first element is
    the given key and the second element is the square of the given value.

    Args:
        k (str): The key.
        v (Union[int, float]): The value, which
        can be either an int or a float.

    Returns:
        Tuple[str, float]: A tuple containing the key
        and the square of the value.
    """
    return k, v ** 2

#!/usr/bin/env python3
"""reform the code typing"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of
    the given list if it is not empty.
    Otherwise, return None.
    :param lst: A sequence of any type.
    :return: The first element of the list if it is not empty,
    otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None

#!/usr/bin/env python3
"""
Here's what the mappings should look like
dct: typing.Mapping
key: typing.Any
default: typing.Union[~T, NoneType]
return: typing.Union[typing.Any, ~T]
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary based on a given key.
    Args:
        dct (Mapping): The dictionary from which to retrieve the value.
        key (Any): The key to lookup in the dictionary.
        default (Union[T, None], optional): The default value to
        return if the key is not found. Defaults to None.
    Returns:
        Union[Any, T]: The value associated with the key if it exists in
        the dictionary, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

#!/usr/bin/env python3
""" Module for testing the utils """
from typing import Mapping, Sequence, Dict, Any
from utils import access_nested_map, get_json, memoize
from unittest import TestCase
import requests
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """class for testing access nested map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ):
        """The test method for returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), "a"),
            ({{"a": 1}}, ("a", "b"), "b"),
        ]
    )
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence
    ):
        """test that keyerror is raised for the input"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class for testing the json resp"""
    @parameterized(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    def test_get_json(
        self,
        url: str,
        test_payload: Dict
    ):
        """Test the get json function by mocking the request"""
        mock_resp = Mock()
        mock_resp.json.return_value = test_payload
        with patch('request.get', return_value=mock_resp) as mocked_get:
            output = get_json(url)
        mocked_get.assert_called_once_with(url)
        self.assertEqual(output, test_payload)

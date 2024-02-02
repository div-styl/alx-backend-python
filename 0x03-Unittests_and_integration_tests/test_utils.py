#!/usr/bin/env python3
""" Module for testing the utils """
from typing import Mapping, Sequence, Dict, Any
from utils import access_nested_map, get_json, memoize
from unittest import TestCase
import requests
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(TestCase):
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
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence
    ):
        """test that keyerror is raised for the input"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """class for testing the json resp"""
    @parameterized.expand(
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


class TestMemoize(TestCase):
    """Test case for memoriz decor"""
    def test_memoize(self):
        """test memoize decor on prop mocking method"""
        class TestCase:
            """dummy class for testing """
            def a_method(self) -> int:
                """mocked method for testing"""
                return 42

            @memoize
            def a_property(self) -> int:
                """prop under testing using memoize decor"""
                return self.a_method()

        with patch.object(TestCase, 'a_method') as mock_meth:
            mock_meth.return_value = 42
            dmmy = TestCase()
            res1 = dmmy.a_property
            res2 = dmmy.a_property

        dmmy = TestCase()
        res1 = dmmy.a_property
        res2 = dmmy.a_property

        mocked_method.assert_called_once()
        self.assertEqual(res1, 42)
        self.assertEqual(res1, 42)

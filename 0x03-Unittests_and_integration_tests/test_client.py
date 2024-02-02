#!/usr/bin/env python3
"""test case for the client module"""

from unittest import TestCase
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, MagicMock


class TestGithubOrgClient(TestCase):
    """test case for testing github client"""

    @parameterized.expand(["google", "abc"])
    @patch("client.get_json")
    def test_org(self, org_name: str, mocked_get_json: MagicMock):
        """test func that tests the org method of git hub client"""
        GithubOrgClient(org_name).org
        mocked_get_json.assert_called_once_with(
            "https://api.github.com/orgs/" + org_name
        )

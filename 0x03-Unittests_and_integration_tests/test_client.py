#!/usr/bin/env python3
"""test case for the client module"""

from unittest import TestCase
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, MagicMock, PropertyMock, Mock
from fixtures import TEST_PAYLOAD


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

    @patch('client.GithubOrgClient.org', return_value={"repos_url": 'url'})
    def test_public_repos_url(self, mocked_org):
        """Test the public repo"""
        client = GithubOrgClient('random org url')
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_prop:
            mocked_prop.return_value = mocked_org.return_value["repos_url"]
            rp_url = client._public_repos_url
        self.assertEqual('url', rp_url)

    @patch("client.get_json")
    def test_public_repos(self, mocked_get_json):
        """test public repo method"""
        test_payload = [
            {'name': 'name1'},
            {'name': 'name2'}
        ]
        mocked_get_json.return_value = test_payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_prop:
            mocked_prop.return_value = 'za url'
            name_lt = GithubOrgClient('random name').public_repos()
        self.assertEqual(['name1', 'name2'], name_lt)
        mocked_get_json.assert_called_once_with('za url')

    @parameterized.expand([
        ({"name": "repo1", "license": {"key": "my_license"}},
         "my_license", True),
        ({"name": "repo2", "license": {"key": "other_license"}},
         "my_license", False)
    ])
    def test_has_license(self, repo, licence, expected):
        """Test the licence static method of githuborgclient"""
        self.assertEqual(GithubOrgClient.has_license(repo, licence), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(TestCase):
    """integration test cases for the githubclient"""
    @classmethod
    def setUpClass(cls):
        """set up the class for integration test"""
        def side(url):
            """side eff fuc for requests get"""
            repo = []
            mock_resp = Mock()
            for payload in TEST_PAYLOAD:
                if url == payload[0]["repos_url"]:
                    repo = payload[1]
                    break
            mock_resp.json.return_value = repo
            return mock_resp
            cls.get_patcher = patch('requests.get', side_effect=side)
            cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """tear down the class"""
        cls.get_patcher.stop()

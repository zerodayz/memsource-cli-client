# coding: utf-8

"""
    Memsource REST API

    Welcome to Memsource's API documentation. To view our legacy APIs please [visit our documentation](https://wiki.memsource.com/wiki/Memsource_API) and for more information about our new APIs, [visit our blog](https://www.memsource.com/blog/2017/10/24/introducing-rest-apis-qa-with-the-memsource-api-team/).    If you have any questions, please contact [Memsource Support](<mailto:support@memsource.com>).  # noqa: E501

    OpenAPI spec version: Latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import memsource_cli
from memsource_cli.api.provider_api import ProviderApi  # noqa: E501
from memsource_cli.rest import ApiException


class TestProviderApi(unittest.TestCase):
    """ProviderApi unit test stubs"""

    def setUp(self):
        self.api = memsource_cli.api.provider_api.ProviderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_project_assignments(self):
        """Test case for get_project_assignments

        List project providers  # noqa: E501
        """
        pass

    def test_list_providers(self):
        """Test case for list_providers

        Get suggested providers  # noqa: E501
        """
        pass

    def test_list_providers1(self):
        """Test case for list_providers1

        Get suggested providers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

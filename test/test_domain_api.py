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
from memsource_cli.api.domain_api import DomainApi  # noqa: E501
from memsource_cli.rest import ApiException


class TestDomainApi(unittest.TestCase):
    """DomainApi unit test stubs"""

    def setUp(self):
        self.api = memsource_cli.api.domain_api.DomainApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_domain(self):
        """Test case for create_domain

        Create domain  # noqa: E501
        """
        pass

    def test_delete_domain(self):
        """Test case for delete_domain

        Delete domain  # noqa: E501
        """
        pass

    def test_get_domain(self):
        """Test case for get_domain

        Get domain  # noqa: E501
        """
        pass

    def test_list_domains(self):
        """Test case for list_domains

        List of domains  # noqa: E501
        """
        pass

    def test_update_domain(self):
        """Test case for update_domain

        Edit domain  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

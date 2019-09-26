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
from memsource_cli.api.connector_api import ConnectorApi  # noqa: E501
from memsource_cli.rest import ApiException


class TestConnectorApi(unittest.TestCase):
    """ConnectorApi unit test stubs"""

    def setUp(self):
        self.api = memsource_cli.api.connector_api.ConnectorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_connector(self):
        """Test case for get_connector

        Get a connector  # noqa: E501
        """
        pass

    def test_get_connector_list(self):
        """Test case for get_connector_list

        List connectors  # noqa: E501
        """
        pass

    def test_get_file(self):
        """Test case for get_file

        Download file  # noqa: E501
        """
        pass

    def test_get_folder(self):
        """Test case for get_folder

        List files in a subfolder  # noqa: E501
        """
        pass

    def test_get_root_folder(self):
        """Test case for get_root_folder

        List files in root  # noqa: E501
        """
        pass

    def test_upload_file(self):
        """Test case for upload_file

        Upload a file to a subfolder of the selected connector  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
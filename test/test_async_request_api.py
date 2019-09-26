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
from memsource_cli.api.async_request_api import AsyncRequestApi  # noqa: E501
from memsource_cli.rest import ApiException


class TestAsyncRequestApi(unittest.TestCase):
    """AsyncRequestApi unit test stubs"""

    def setUp(self):
        self.api = memsource_cli.api.async_request_api.AsyncRequestApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_async_request(self):
        """Test case for get_async_request

        Get asynchronous request  # noqa: E501
        """
        pass

    def test_list_pending_requests(self):
        """Test case for list_pending_requests

        List pending requests  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

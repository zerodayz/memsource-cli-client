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
from memsource_cli.api.workflow_changes_api import WorkflowChangesApi  # noqa: E501
from memsource_cli.rest import ApiException


class TestWorkflowChangesApi(unittest.TestCase):
    """WorkflowChangesApi unit test stubs"""

    def setUp(self):
        self.api = memsource_cli.api.workflow_changes_api.WorkflowChangesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_download_workflow_changes(self):
        """Test case for download_workflow_changes

        Download workflow changes report  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

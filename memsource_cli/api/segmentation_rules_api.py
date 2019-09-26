# coding: utf-8

"""
    Memsource REST API

    Welcome to Memsource's API documentation. To view our legacy APIs please [visit our documentation](https://wiki.memsource.com/wiki/Memsource_API) and for more information about our new APIs, [visit our blog](https://www.memsource.com/blog/2017/10/24/introducing-rest-apis-qa-with-the-memsource-api-team/).    If you have any questions, please contact [Memsource Support](<mailto:support@memsource.com>).  # noqa: E501

    OpenAPI spec version: Latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from memsource_cli.api_client import ApiClient


class SegmentationRulesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_segmentation_rule(self, body, seg_rule, **kwargs):  # noqa: E501
        """Create segmentation rule  # noqa: E501

        Creates new Segmentation Rule with file and segRule JSON Object as header parameter. The same object is used for GET action.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_segmentation_rule(body, seg_rule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InputStream body: streamed file (required)
        :param str seg_rule: (required)
        :return: SegmentationRuleDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_segmentation_rule_with_http_info(body, seg_rule, **kwargs)  # noqa: E501
        else:
            (data) = self.create_segmentation_rule_with_http_info(body, seg_rule, **kwargs)  # noqa: E501
            return data

    def create_segmentation_rule_with_http_info(self, body, seg_rule, **kwargs):  # noqa: E501
        """Create segmentation rule  # noqa: E501

        Creates new Segmentation Rule with file and segRule JSON Object as header parameter. The same object is used for GET action.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_segmentation_rule_with_http_info(body, seg_rule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InputStream body: streamed file (required)
        :param str seg_rule: (required)
        :return: SegmentationRuleDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'seg_rule']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_segmentation_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_segmentation_rule`")  # noqa: E501
        # verify the required parameter 'seg_rule' is set
        if ('seg_rule' not in params or
                params['seg_rule'] is None):
            raise ValueError("Missing the required parameter `seg_rule` when calling `create_segmentation_rule`")  # noqa: E501

        if ('seg_rule' in params and
                len(params['seg_rule']) > 255):
            raise ValueError("Invalid value for parameter `seg_rule` when calling `create_segmentation_rule`, length must be less than or equal to `255`")  # noqa: E501
        if ('seg_rule' in params and
                len(params['seg_rule']) < 0):
            raise ValueError("Invalid value for parameter `seg_rule` when calling `create_segmentation_rule`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'seg_rule' in params:
            header_params['segRule'] = params['seg_rule']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api2/v1/segmentationRules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SegmentationRuleDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def deletes_segmentation_rule(self, seg_rule_id, **kwargs):  # noqa: E501
        """Delete segmentation rule  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletes_segmentation_rule(seg_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int seg_rule_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletes_segmentation_rule_with_http_info(seg_rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.deletes_segmentation_rule_with_http_info(seg_rule_id, **kwargs)  # noqa: E501
            return data

    def deletes_segmentation_rule_with_http_info(self, seg_rule_id, **kwargs):  # noqa: E501
        """Delete segmentation rule  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletes_segmentation_rule_with_http_info(seg_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int seg_rule_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['seg_rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deletes_segmentation_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'seg_rule_id' is set
        if ('seg_rule_id' not in params or
                params['seg_rule_id'] is None):
            raise ValueError("Missing the required parameter `seg_rule_id` when calling `deletes_segmentation_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'seg_rule_id' in params:
            path_params['segRuleId'] = params['seg_rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api2/v1/segmentationRules/{segRuleId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_list_of_segmentation_rules(self, **kwargs):  # noqa: E501
        """List segmentation rules  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_of_segmentation_rules(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number: Page number, starting with 0, default 0
        :param int page_size: Page size, accepts values between 1 and 50, default 50
        :return: PageDtoSegmentationRuleReference
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_list_of_segmentation_rules_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_list_of_segmentation_rules_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_list_of_segmentation_rules_with_http_info(self, **kwargs):  # noqa: E501
        """List segmentation rules  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_of_segmentation_rules_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number: Page number, starting with 0, default 0
        :param int page_size: Page size, accepts values between 1 and 50, default 50
        :return: PageDtoSegmentationRuleReference
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_list_of_segmentation_rules" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_number' in params and params['page_number'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_number` when calling `get_list_of_segmentation_rules`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page_size' in params and params['page_size'] > 50:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_list_of_segmentation_rules`, must be a value less than or equal to `50`")  # noqa: E501
        if 'page_size' in params and params['page_size'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_list_of_segmentation_rules`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api2/v1/segmentationRules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDtoSegmentationRuleReference',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_segmentation_rule(self, seg_rule_id, **kwargs):  # noqa: E501
        """Get segmentation rule  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_segmentation_rule(seg_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int seg_rule_id: (required)
        :return: SegmentationRuleDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_segmentation_rule_with_http_info(seg_rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_segmentation_rule_with_http_info(seg_rule_id, **kwargs)  # noqa: E501
            return data

    def get_segmentation_rule_with_http_info(self, seg_rule_id, **kwargs):  # noqa: E501
        """Get segmentation rule  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_segmentation_rule_with_http_info(seg_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int seg_rule_id: (required)
        :return: SegmentationRuleDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['seg_rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_segmentation_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'seg_rule_id' is set
        if ('seg_rule_id' not in params or
                params['seg_rule_id'] is None):
            raise ValueError("Missing the required parameter `seg_rule_id` when calling `get_segmentation_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'seg_rule_id' in params:
            path_params['segRuleId'] = params['seg_rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api2/v1/segmentationRules/{segRuleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SegmentationRuleDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def updates_segmentation_rule(self, seg_rule_id, **kwargs):  # noqa: E501
        """Edit segmentation rule  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.updates_segmentation_rule(seg_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int seg_rule_id: (required)
        :param EditSegmentationRuleDto body:
        :return: SegmentationRuleDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.updates_segmentation_rule_with_http_info(seg_rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.updates_segmentation_rule_with_http_info(seg_rule_id, **kwargs)  # noqa: E501
            return data

    def updates_segmentation_rule_with_http_info(self, seg_rule_id, **kwargs):  # noqa: E501
        """Edit segmentation rule  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.updates_segmentation_rule_with_http_info(seg_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int seg_rule_id: (required)
        :param EditSegmentationRuleDto body:
        :return: SegmentationRuleDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['seg_rule_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method updates_segmentation_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'seg_rule_id' is set
        if ('seg_rule_id' not in params or
                params['seg_rule_id'] is None):
            raise ValueError("Missing the required parameter `seg_rule_id` when calling `updates_segmentation_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'seg_rule_id' in params:
            path_params['segRuleId'] = params['seg_rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api2/v1/segmentationRules/{segRuleId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SegmentationRuleDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
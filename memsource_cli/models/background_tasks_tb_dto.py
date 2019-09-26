# coding: utf-8

"""
    Memsource REST API

    Welcome to Memsource's API documentation. To view our legacy APIs please [visit our documentation](https://wiki.memsource.com/wiki/Memsource_API) and for more information about our new APIs, [visit our blog](https://www.memsource.com/blog/2017/10/24/introducing-rest-apis-qa-with-the-memsource-api-team/).    If you have any questions, please contact [Memsource Support](<mailto:support@memsource.com>).  # noqa: E501

    OpenAPI spec version: Latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from memsource_cli.models.async_request_dto import AsyncRequestDto  # noqa: F401,E501
from memsource_cli.models.metadata_response import MetadataResponse  # noqa: F401,E501


class BackgroundTasksTbDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'status': 'str',
        'finished_data_text': 'str',
        'async_request': 'AsyncRequestDto',
        'last_task_string': 'str',
        'metadata': 'MetadataResponse',
        'last_task_ok': 'str',
        'last_task_error': 'str',
        'last_task_error_html': 'str'
    }

    attribute_map = {
        'status': 'status',
        'finished_data_text': 'finishedDataText',
        'async_request': 'asyncRequest',
        'last_task_string': 'lastTaskString',
        'metadata': 'metadata',
        'last_task_ok': 'lastTaskOk',
        'last_task_error': 'lastTaskError',
        'last_task_error_html': 'lastTaskErrorHtml'
    }

    def __init__(self, status=None, finished_data_text=None, async_request=None, last_task_string=None, metadata=None, last_task_ok=None, last_task_error=None, last_task_error_html=None):  # noqa: E501
        """BackgroundTasksTbDto - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._finished_data_text = None
        self._async_request = None
        self._last_task_string = None
        self._metadata = None
        self._last_task_ok = None
        self._last_task_error = None
        self._last_task_error_html = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if finished_data_text is not None:
            self.finished_data_text = finished_data_text
        if async_request is not None:
            self.async_request = async_request
        if last_task_string is not None:
            self.last_task_string = last_task_string
        if metadata is not None:
            self.metadata = metadata
        if last_task_ok is not None:
            self.last_task_ok = last_task_ok
        if last_task_error is not None:
            self.last_task_error = last_task_error
        if last_task_error_html is not None:
            self.last_task_error_html = last_task_error_html

    @property
    def status(self):
        """Gets the status of this BackgroundTasksTbDto.  # noqa: E501


        :return: The status of this BackgroundTasksTbDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BackgroundTasksTbDto.


        :param status: The status of this BackgroundTasksTbDto.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def finished_data_text(self):
        """Gets the finished_data_text of this BackgroundTasksTbDto.  # noqa: E501


        :return: The finished_data_text of this BackgroundTasksTbDto.  # noqa: E501
        :rtype: str
        """
        return self._finished_data_text

    @finished_data_text.setter
    def finished_data_text(self, finished_data_text):
        """Sets the finished_data_text of this BackgroundTasksTbDto.


        :param finished_data_text: The finished_data_text of this BackgroundTasksTbDto.  # noqa: E501
        :type: str
        """

        self._finished_data_text = finished_data_text

    @property
    def async_request(self):
        """Gets the async_request of this BackgroundTasksTbDto.  # noqa: E501


        :return: The async_request of this BackgroundTasksTbDto.  # noqa: E501
        :rtype: AsyncRequestDto
        """
        return self._async_request

    @async_request.setter
    def async_request(self, async_request):
        """Sets the async_request of this BackgroundTasksTbDto.


        :param async_request: The async_request of this BackgroundTasksTbDto.  # noqa: E501
        :type: AsyncRequestDto
        """

        self._async_request = async_request

    @property
    def last_task_string(self):
        """Gets the last_task_string of this BackgroundTasksTbDto.  # noqa: E501


        :return: The last_task_string of this BackgroundTasksTbDto.  # noqa: E501
        :rtype: str
        """
        return self._last_task_string

    @last_task_string.setter
    def last_task_string(self, last_task_string):
        """Sets the last_task_string of this BackgroundTasksTbDto.


        :param last_task_string: The last_task_string of this BackgroundTasksTbDto.  # noqa: E501
        :type: str
        """

        self._last_task_string = last_task_string

    @property
    def metadata(self):
        """Gets the metadata of this BackgroundTasksTbDto.  # noqa: E501


        :return: The metadata of this BackgroundTasksTbDto.  # noqa: E501
        :rtype: MetadataResponse
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this BackgroundTasksTbDto.


        :param metadata: The metadata of this BackgroundTasksTbDto.  # noqa: E501
        :type: MetadataResponse
        """

        self._metadata = metadata

    @property
    def last_task_ok(self):
        """Gets the last_task_ok of this BackgroundTasksTbDto.  # noqa: E501


        :return: The last_task_ok of this BackgroundTasksTbDto.  # noqa: E501
        :rtype: str
        """
        return self._last_task_ok

    @last_task_ok.setter
    def last_task_ok(self, last_task_ok):
        """Sets the last_task_ok of this BackgroundTasksTbDto.


        :param last_task_ok: The last_task_ok of this BackgroundTasksTbDto.  # noqa: E501
        :type: str
        """

        self._last_task_ok = last_task_ok

    @property
    def last_task_error(self):
        """Gets the last_task_error of this BackgroundTasksTbDto.  # noqa: E501


        :return: The last_task_error of this BackgroundTasksTbDto.  # noqa: E501
        :rtype: str
        """
        return self._last_task_error

    @last_task_error.setter
    def last_task_error(self, last_task_error):
        """Sets the last_task_error of this BackgroundTasksTbDto.


        :param last_task_error: The last_task_error of this BackgroundTasksTbDto.  # noqa: E501
        :type: str
        """

        self._last_task_error = last_task_error

    @property
    def last_task_error_html(self):
        """Gets the last_task_error_html of this BackgroundTasksTbDto.  # noqa: E501


        :return: The last_task_error_html of this BackgroundTasksTbDto.  # noqa: E501
        :rtype: str
        """
        return self._last_task_error_html

    @last_task_error_html.setter
    def last_task_error_html(self, last_task_error_html):
        """Sets the last_task_error_html of this BackgroundTasksTbDto.


        :param last_task_error_html: The last_task_error_html of this BackgroundTasksTbDto.  # noqa: E501
        :type: str
        """

        self._last_task_error_html = last_task_error_html

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BackgroundTasksTbDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BackgroundTasksTbDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

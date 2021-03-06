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

from memsource_cli.models.error_detail_dto import ErrorDetailDto  # noqa: F401,E501


class AsyncResponseDto(object):
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
        'date_created': 'datetime',
        'error_code': 'str',
        'error_desc': 'str',
        'error_details': 'list[ErrorDetailDto]',
        'warnings': 'list[ErrorDetailDto]'
    }

    attribute_map = {
        'date_created': 'dateCreated',
        'error_code': 'errorCode',
        'error_desc': 'errorDesc',
        'error_details': 'errorDetails',
        'warnings': 'warnings'
    }

    def __init__(self, date_created=None, error_code=None, error_desc=None, error_details=None, warnings=None):  # noqa: E501
        """AsyncResponseDto - a model defined in Swagger"""  # noqa: E501

        self._date_created = None
        self._error_code = None
        self._error_desc = None
        self._error_details = None
        self._warnings = None
        self.discriminator = None

        if date_created is not None:
            self.date_created = date_created
        if error_code is not None:
            self.error_code = error_code
        if error_desc is not None:
            self.error_desc = error_desc
        if error_details is not None:
            self.error_details = error_details
        if warnings is not None:
            self.warnings = warnings

    @property
    def date_created(self):
        """Gets the date_created of this AsyncResponseDto.  # noqa: E501


        :return: The date_created of this AsyncResponseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this AsyncResponseDto.


        :param date_created: The date_created of this AsyncResponseDto.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def error_code(self):
        """Gets the error_code of this AsyncResponseDto.  # noqa: E501


        :return: The error_code of this AsyncResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this AsyncResponseDto.


        :param error_code: The error_code of this AsyncResponseDto.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_desc(self):
        """Gets the error_desc of this AsyncResponseDto.  # noqa: E501


        :return: The error_desc of this AsyncResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._error_desc

    @error_desc.setter
    def error_desc(self, error_desc):
        """Sets the error_desc of this AsyncResponseDto.


        :param error_desc: The error_desc of this AsyncResponseDto.  # noqa: E501
        :type: str
        """

        self._error_desc = error_desc

    @property
    def error_details(self):
        """Gets the error_details of this AsyncResponseDto.  # noqa: E501


        :return: The error_details of this AsyncResponseDto.  # noqa: E501
        :rtype: list[ErrorDetailDto]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this AsyncResponseDto.


        :param error_details: The error_details of this AsyncResponseDto.  # noqa: E501
        :type: list[ErrorDetailDto]
        """

        self._error_details = error_details

    @property
    def warnings(self):
        """Gets the warnings of this AsyncResponseDto.  # noqa: E501


        :return: The warnings of this AsyncResponseDto.  # noqa: E501
        :rtype: list[ErrorDetailDto]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this AsyncResponseDto.


        :param warnings: The warnings of this AsyncResponseDto.  # noqa: E501
        :type: list[ErrorDetailDto]
        """

        self._warnings = warnings

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
        if issubclass(AsyncResponseDto, dict):
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
        if not isinstance(other, AsyncResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

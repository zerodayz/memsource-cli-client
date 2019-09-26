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


class SearchTbByJobRequestDto(object):
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
        'query': 'str',
        'count': 'int',
        'offset': 'int',
        'reverse': 'bool'
    }

    attribute_map = {
        'query': 'query',
        'count': 'count',
        'offset': 'offset',
        'reverse': 'reverse'
    }

    def __init__(self, query=None, count=None, offset=None, reverse=None):  # noqa: E501
        """SearchTbByJobRequestDto - a model defined in Swagger"""  # noqa: E501

        self._query = None
        self._count = None
        self._offset = None
        self._reverse = None
        self.discriminator = None

        self.query = query
        if count is not None:
            self.count = count
        if offset is not None:
            self.offset = offset
        if reverse is not None:
            self.reverse = reverse

    @property
    def query(self):
        """Gets the query of this SearchTbByJobRequestDto.  # noqa: E501


        :return: The query of this SearchTbByJobRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SearchTbByJobRequestDto.


        :param query: The query of this SearchTbByJobRequestDto.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def count(self):
        """Gets the count of this SearchTbByJobRequestDto.  # noqa: E501

        Default: 15  # noqa: E501

        :return: The count of this SearchTbByJobRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SearchTbByJobRequestDto.

        Default: 15  # noqa: E501

        :param count: The count of this SearchTbByJobRequestDto.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def offset(self):
        """Gets the offset of this SearchTbByJobRequestDto.  # noqa: E501

        Default: 0  # noqa: E501

        :return: The offset of this SearchTbByJobRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchTbByJobRequestDto.

        Default: 0  # noqa: E501

        :param offset: The offset of this SearchTbByJobRequestDto.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def reverse(self):
        """Gets the reverse of this SearchTbByJobRequestDto.  # noqa: E501

        Default: false  # noqa: E501

        :return: The reverse of this SearchTbByJobRequestDto.  # noqa: E501
        :rtype: bool
        """
        return self._reverse

    @reverse.setter
    def reverse(self, reverse):
        """Sets the reverse of this SearchTbByJobRequestDto.

        Default: false  # noqa: E501

        :param reverse: The reverse of this SearchTbByJobRequestDto.  # noqa: E501
        :type: bool
        """

        self._reverse = reverse

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
        if issubclass(SearchTbByJobRequestDto, dict):
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
        if not isinstance(other, SearchTbByJobRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
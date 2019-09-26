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

from memsource_cli.models.segment_warning import SegmentWarning  # noqa: F401,E501


class ForbiddenStringWarningDto(SegmentWarning):
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
        'forbidden_string': 'str'
    }

    attribute_map = {
        'forbidden_string': 'forbiddenString'
    }

    def __init__(self, forbidden_string=None):  # noqa: E501
        """ForbiddenStringWarningDto - a model defined in Swagger"""  # noqa: E501

        self._forbidden_string = None
        self.discriminator = None

        if forbidden_string is not None:
            self.forbidden_string = forbidden_string

    @property
    def forbidden_string(self):
        """Gets the forbidden_string of this ForbiddenStringWarningDto.  # noqa: E501


        :return: The forbidden_string of this ForbiddenStringWarningDto.  # noqa: E501
        :rtype: str
        """
        return self._forbidden_string

    @forbidden_string.setter
    def forbidden_string(self, forbidden_string):
        """Sets the forbidden_string of this ForbiddenStringWarningDto.


        :param forbidden_string: The forbidden_string of this ForbiddenStringWarningDto.  # noqa: E501
        :type: str
        """

        self._forbidden_string = forbidden_string

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
        if issubclass(ForbiddenStringWarningDto, dict):
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
        if not isinstance(other, ForbiddenStringWarningDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

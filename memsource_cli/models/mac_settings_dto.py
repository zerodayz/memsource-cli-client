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


class MacSettingsDto(object):
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
        'html_subfilter': 'bool',
        'tag_regexp': 'str'
    }

    attribute_map = {
        'html_subfilter': 'htmlSubfilter',
        'tag_regexp': 'tagRegexp'
    }

    def __init__(self, html_subfilter=None, tag_regexp=None):  # noqa: E501
        """MacSettingsDto - a model defined in Swagger"""  # noqa: E501

        self._html_subfilter = None
        self._tag_regexp = None
        self.discriminator = None

        if html_subfilter is not None:
            self.html_subfilter = html_subfilter
        if tag_regexp is not None:
            self.tag_regexp = tag_regexp

    @property
    def html_subfilter(self):
        """Gets the html_subfilter of this MacSettingsDto.  # noqa: E501

        Default: false  # noqa: E501

        :return: The html_subfilter of this MacSettingsDto.  # noqa: E501
        :rtype: bool
        """
        return self._html_subfilter

    @html_subfilter.setter
    def html_subfilter(self, html_subfilter):
        """Sets the html_subfilter of this MacSettingsDto.

        Default: false  # noqa: E501

        :param html_subfilter: The html_subfilter of this MacSettingsDto.  # noqa: E501
        :type: bool
        """

        self._html_subfilter = html_subfilter

    @property
    def tag_regexp(self):
        """Gets the tag_regexp of this MacSettingsDto.  # noqa: E501


        :return: The tag_regexp of this MacSettingsDto.  # noqa: E501
        :rtype: str
        """
        return self._tag_regexp

    @tag_regexp.setter
    def tag_regexp(self, tag_regexp):
        """Sets the tag_regexp of this MacSettingsDto.


        :param tag_regexp: The tag_regexp of this MacSettingsDto.  # noqa: E501
        :type: str
        """

        self._tag_regexp = tag_regexp

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
        if issubclass(MacSettingsDto, dict):
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
        if not isinstance(other, MacSettingsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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


class JoinTagsWarningDto(SegmentWarning):
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
        'source_tags_count': 'int',
        'translation_tags_count': 'int'
    }

    attribute_map = {
        'source_tags_count': 'sourceTagsCount',
        'translation_tags_count': 'translationTagsCount'
    }

    def __init__(self, source_tags_count=None, translation_tags_count=None):  # noqa: E501
        """JoinTagsWarningDto - a model defined in Swagger"""  # noqa: E501

        self._source_tags_count = None
        self._translation_tags_count = None
        self.discriminator = None

        if source_tags_count is not None:
            self.source_tags_count = source_tags_count
        if translation_tags_count is not None:
            self.translation_tags_count = translation_tags_count

    @property
    def source_tags_count(self):
        """Gets the source_tags_count of this JoinTagsWarningDto.  # noqa: E501


        :return: The source_tags_count of this JoinTagsWarningDto.  # noqa: E501
        :rtype: int
        """
        return self._source_tags_count

    @source_tags_count.setter
    def source_tags_count(self, source_tags_count):
        """Sets the source_tags_count of this JoinTagsWarningDto.


        :param source_tags_count: The source_tags_count of this JoinTagsWarningDto.  # noqa: E501
        :type: int
        """

        self._source_tags_count = source_tags_count

    @property
    def translation_tags_count(self):
        """Gets the translation_tags_count of this JoinTagsWarningDto.  # noqa: E501


        :return: The translation_tags_count of this JoinTagsWarningDto.  # noqa: E501
        :rtype: int
        """
        return self._translation_tags_count

    @translation_tags_count.setter
    def translation_tags_count(self, translation_tags_count):
        """Sets the translation_tags_count of this JoinTagsWarningDto.


        :param translation_tags_count: The translation_tags_count of this JoinTagsWarningDto.  # noqa: E501
        :type: int
        """

        self._translation_tags_count = translation_tags_count

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
        if issubclass(JoinTagsWarningDto, dict):
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
        if not isinstance(other, JoinTagsWarningDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

from memsource_cli.models.language_metadata1 import LanguageMetadata1  # noqa: F401,E501


class MetadataResponse(object):
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
        'segments_count': 'int',
        'deduplicated_segments_count': 'int',
        'metadata_by_language': 'dict(str, LanguageMetadata1)'
    }

    attribute_map = {
        'segments_count': 'segmentsCount',
        'deduplicated_segments_count': 'deduplicatedSegmentsCount',
        'metadata_by_language': 'metadataByLanguage'
    }

    def __init__(self, segments_count=None, deduplicated_segments_count=None, metadata_by_language=None):  # noqa: E501
        """MetadataResponse - a model defined in Swagger"""  # noqa: E501

        self._segments_count = None
        self._deduplicated_segments_count = None
        self._metadata_by_language = None
        self.discriminator = None

        if segments_count is not None:
            self.segments_count = segments_count
        if deduplicated_segments_count is not None:
            self.deduplicated_segments_count = deduplicated_segments_count
        if metadata_by_language is not None:
            self.metadata_by_language = metadata_by_language

    @property
    def segments_count(self):
        """Gets the segments_count of this MetadataResponse.  # noqa: E501


        :return: The segments_count of this MetadataResponse.  # noqa: E501
        :rtype: int
        """
        return self._segments_count

    @segments_count.setter
    def segments_count(self, segments_count):
        """Sets the segments_count of this MetadataResponse.


        :param segments_count: The segments_count of this MetadataResponse.  # noqa: E501
        :type: int
        """

        self._segments_count = segments_count

    @property
    def deduplicated_segments_count(self):
        """Gets the deduplicated_segments_count of this MetadataResponse.  # noqa: E501


        :return: The deduplicated_segments_count of this MetadataResponse.  # noqa: E501
        :rtype: int
        """
        return self._deduplicated_segments_count

    @deduplicated_segments_count.setter
    def deduplicated_segments_count(self, deduplicated_segments_count):
        """Sets the deduplicated_segments_count of this MetadataResponse.


        :param deduplicated_segments_count: The deduplicated_segments_count of this MetadataResponse.  # noqa: E501
        :type: int
        """

        self._deduplicated_segments_count = deduplicated_segments_count

    @property
    def metadata_by_language(self):
        """Gets the metadata_by_language of this MetadataResponse.  # noqa: E501


        :return: The metadata_by_language of this MetadataResponse.  # noqa: E501
        :rtype: dict(str, LanguageMetadata1)
        """
        return self._metadata_by_language

    @metadata_by_language.setter
    def metadata_by_language(self, metadata_by_language):
        """Sets the metadata_by_language of this MetadataResponse.


        :param metadata_by_language: The metadata_by_language of this MetadataResponse.  # noqa: E501
        :type: dict(str, LanguageMetadata1)
        """

        self._metadata_by_language = metadata_by_language

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
        if issubclass(MetadataResponse, dict):
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
        if not isinstance(other, MetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

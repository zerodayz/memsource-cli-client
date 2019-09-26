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

from memsource_cli.models.id_reference import IdReference  # noqa: F401,E501


class BulkEditAnalyseDto(object):
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
        'analyses': 'list[IdReference]',
        'name': 'str',
        'linguist': 'IdReference'
    }

    attribute_map = {
        'analyses': 'analyses',
        'name': 'name',
        'linguist': 'linguist'
    }

    def __init__(self, analyses=None, name=None, linguist=None):  # noqa: E501
        """BulkEditAnalyseDto - a model defined in Swagger"""  # noqa: E501

        self._analyses = None
        self._name = None
        self._linguist = None
        self.discriminator = None

        self.analyses = analyses
        if name is not None:
            self.name = name
        if linguist is not None:
            self.linguist = linguist

    @property
    def analyses(self):
        """Gets the analyses of this BulkEditAnalyseDto.  # noqa: E501


        :return: The analyses of this BulkEditAnalyseDto.  # noqa: E501
        :rtype: list[IdReference]
        """
        return self._analyses

    @analyses.setter
    def analyses(self, analyses):
        """Sets the analyses of this BulkEditAnalyseDto.


        :param analyses: The analyses of this BulkEditAnalyseDto.  # noqa: E501
        :type: list[IdReference]
        """
        if analyses is None:
            raise ValueError("Invalid value for `analyses`, must not be `None`")  # noqa: E501

        self._analyses = analyses

    @property
    def name(self):
        """Gets the name of this BulkEditAnalyseDto.  # noqa: E501


        :return: The name of this BulkEditAnalyseDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BulkEditAnalyseDto.


        :param name: The name of this BulkEditAnalyseDto.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def linguist(self):
        """Gets the linguist of this BulkEditAnalyseDto.  # noqa: E501


        :return: The linguist of this BulkEditAnalyseDto.  # noqa: E501
        :rtype: IdReference
        """
        return self._linguist

    @linguist.setter
    def linguist(self, linguist):
        """Sets the linguist of this BulkEditAnalyseDto.


        :param linguist: The linguist of this BulkEditAnalyseDto.  # noqa: E501
        :type: IdReference
        """

        self._linguist = linguist

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
        if issubclass(BulkEditAnalyseDto, dict):
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
        if not isinstance(other, BulkEditAnalyseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

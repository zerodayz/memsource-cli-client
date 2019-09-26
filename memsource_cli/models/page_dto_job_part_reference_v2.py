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

from memsource_cli.models.job_part_reference_v2 import JobPartReferenceV2  # noqa: F401,E501


class PageDtoJobPartReferenceV2(object):
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
        'total_elements': 'int',
        'total_pages': 'int',
        'page_size': 'int',
        'page_number': 'int',
        'number_of_elements': 'int',
        'content': 'list[JobPartReferenceV2]'
    }

    attribute_map = {
        'total_elements': 'totalElements',
        'total_pages': 'totalPages',
        'page_size': 'pageSize',
        'page_number': 'pageNumber',
        'number_of_elements': 'numberOfElements',
        'content': 'content'
    }

    def __init__(self, total_elements=None, total_pages=None, page_size=None, page_number=None, number_of_elements=None, content=None):  # noqa: E501
        """PageDtoJobPartReferenceV2 - a model defined in Swagger"""  # noqa: E501

        self._total_elements = None
        self._total_pages = None
        self._page_size = None
        self._page_number = None
        self._number_of_elements = None
        self._content = None
        self.discriminator = None

        if total_elements is not None:
            self.total_elements = total_elements
        if total_pages is not None:
            self.total_pages = total_pages
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if number_of_elements is not None:
            self.number_of_elements = number_of_elements
        if content is not None:
            self.content = content

    @property
    def total_elements(self):
        """Gets the total_elements of this PageDtoJobPartReferenceV2.  # noqa: E501


        :return: The total_elements of this PageDtoJobPartReferenceV2.  # noqa: E501
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        """Sets the total_elements of this PageDtoJobPartReferenceV2.


        :param total_elements: The total_elements of this PageDtoJobPartReferenceV2.  # noqa: E501
        :type: int
        """

        self._total_elements = total_elements

    @property
    def total_pages(self):
        """Gets the total_pages of this PageDtoJobPartReferenceV2.  # noqa: E501


        :return: The total_pages of this PageDtoJobPartReferenceV2.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this PageDtoJobPartReferenceV2.


        :param total_pages: The total_pages of this PageDtoJobPartReferenceV2.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def page_size(self):
        """Gets the page_size of this PageDtoJobPartReferenceV2.  # noqa: E501


        :return: The page_size of this PageDtoJobPartReferenceV2.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this PageDtoJobPartReferenceV2.


        :param page_size: The page_size of this PageDtoJobPartReferenceV2.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this PageDtoJobPartReferenceV2.  # noqa: E501


        :return: The page_number of this PageDtoJobPartReferenceV2.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this PageDtoJobPartReferenceV2.


        :param page_number: The page_number of this PageDtoJobPartReferenceV2.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def number_of_elements(self):
        """Gets the number_of_elements of this PageDtoJobPartReferenceV2.  # noqa: E501


        :return: The number_of_elements of this PageDtoJobPartReferenceV2.  # noqa: E501
        :rtype: int
        """
        return self._number_of_elements

    @number_of_elements.setter
    def number_of_elements(self, number_of_elements):
        """Sets the number_of_elements of this PageDtoJobPartReferenceV2.


        :param number_of_elements: The number_of_elements of this PageDtoJobPartReferenceV2.  # noqa: E501
        :type: int
        """

        self._number_of_elements = number_of_elements

    @property
    def content(self):
        """Gets the content of this PageDtoJobPartReferenceV2.  # noqa: E501


        :return: The content of this PageDtoJobPartReferenceV2.  # noqa: E501
        :rtype: list[JobPartReferenceV2]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this PageDtoJobPartReferenceV2.


        :param content: The content of this PageDtoJobPartReferenceV2.  # noqa: E501
        :type: list[JobPartReferenceV2]
        """

        self._content = content

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
        if issubclass(PageDtoJobPartReferenceV2, dict):
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
        if not isinstance(other, PageDtoJobPartReferenceV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

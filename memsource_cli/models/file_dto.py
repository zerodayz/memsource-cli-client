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

from memsource_cli.models.error_dto import ErrorDto  # noqa: F401,E501


class FileDto(object):
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
        'id': 'str',
        'name': 'str',
        'encoded_name': 'str',
        'content_type': 'str',
        'size': 'int',
        'directory': 'bool',
        'last_modified': 'datetime',
        'selected': 'bool',
        'error': 'ErrorDto',
        'escaped_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'encoded_name': 'encodedName',
        'content_type': 'contentType',
        'size': 'size',
        'directory': 'directory',
        'last_modified': 'lastModified',
        'selected': 'selected',
        'error': 'error',
        'escaped_name': 'escapedName'
    }

    def __init__(self, id=None, name=None, encoded_name=None, content_type=None, size=None, directory=None, last_modified=None, selected=None, error=None, escaped_name=None):  # noqa: E501
        """FileDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._encoded_name = None
        self._content_type = None
        self._size = None
        self._directory = None
        self._last_modified = None
        self._selected = None
        self._error = None
        self._escaped_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if encoded_name is not None:
            self.encoded_name = encoded_name
        if content_type is not None:
            self.content_type = content_type
        if size is not None:
            self.size = size
        if directory is not None:
            self.directory = directory
        if last_modified is not None:
            self.last_modified = last_modified
        if selected is not None:
            self.selected = selected
        if error is not None:
            self.error = error
        if escaped_name is not None:
            self.escaped_name = escaped_name

    @property
    def id(self):
        """Gets the id of this FileDto.  # noqa: E501


        :return: The id of this FileDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileDto.


        :param id: The id of this FileDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FileDto.  # noqa: E501


        :return: The name of this FileDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileDto.


        :param name: The name of this FileDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def encoded_name(self):
        """Gets the encoded_name of this FileDto.  # noqa: E501


        :return: The encoded_name of this FileDto.  # noqa: E501
        :rtype: str
        """
        return self._encoded_name

    @encoded_name.setter
    def encoded_name(self, encoded_name):
        """Sets the encoded_name of this FileDto.


        :param encoded_name: The encoded_name of this FileDto.  # noqa: E501
        :type: str
        """

        self._encoded_name = encoded_name

    @property
    def content_type(self):
        """Gets the content_type of this FileDto.  # noqa: E501


        :return: The content_type of this FileDto.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this FileDto.


        :param content_type: The content_type of this FileDto.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def size(self):
        """Gets the size of this FileDto.  # noqa: E501


        :return: The size of this FileDto.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileDto.


        :param size: The size of this FileDto.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def directory(self):
        """Gets the directory of this FileDto.  # noqa: E501


        :return: The directory of this FileDto.  # noqa: E501
        :rtype: bool
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this FileDto.


        :param directory: The directory of this FileDto.  # noqa: E501
        :type: bool
        """

        self._directory = directory

    @property
    def last_modified(self):
        """Gets the last_modified of this FileDto.  # noqa: E501


        :return: The last_modified of this FileDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this FileDto.


        :param last_modified: The last_modified of this FileDto.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def selected(self):
        """Gets the selected of this FileDto.  # noqa: E501


        :return: The selected of this FileDto.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this FileDto.


        :param selected: The selected of this FileDto.  # noqa: E501
        :type: bool
        """

        self._selected = selected

    @property
    def error(self):
        """Gets the error of this FileDto.  # noqa: E501


        :return: The error of this FileDto.  # noqa: E501
        :rtype: ErrorDto
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this FileDto.


        :param error: The error of this FileDto.  # noqa: E501
        :type: ErrorDto
        """

        self._error = error

    @property
    def escaped_name(self):
        """Gets the escaped_name of this FileDto.  # noqa: E501


        :return: The escaped_name of this FileDto.  # noqa: E501
        :rtype: str
        """
        return self._escaped_name

    @escaped_name.setter
    def escaped_name(self, escaped_name):
        """Sets the escaped_name of this FileDto.


        :param escaped_name: The escaped_name of this FileDto.  # noqa: E501
        :type: str
        """

        self._escaped_name = escaped_name

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
        if issubclass(FileDto, dict):
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
        if not isinstance(other, FileDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

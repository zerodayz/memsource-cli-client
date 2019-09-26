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

from memsource_cli.models.comment_dto import CommentDto  # noqa: F401,E501
from memsource_cli.models.status_dto import StatusDto  # noqa: F401,E501


class CommonConversationDto(object):
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
        'date_created': 'datetime',
        'date_modified': 'datetime',
        'comments': 'list[CommentDto]',
        'status': 'StatusDto',
        'deleted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'date_created': 'dateCreated',
        'date_modified': 'dateModified',
        'comments': 'comments',
        'status': 'status',
        'deleted': 'deleted'
    }

    discriminator_value_class_map = {
        'SEGMENT_TARGET': 'SEGMENTTARGET',
        'LQA': 'LQA'
    }

    def __init__(self, id=None, date_created=None, date_modified=None, comments=None, status=None, deleted=None):  # noqa: E501
        """CommonConversationDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._date_created = None
        self._date_modified = None
        self._comments = None
        self._status = None
        self._deleted = None
        self.discriminator = 'type'

        if id is not None:
            self.id = id
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified
        if comments is not None:
            self.comments = comments
        if status is not None:
            self.status = status
        if deleted is not None:
            self.deleted = deleted

    @property
    def id(self):
        """Gets the id of this CommonConversationDto.  # noqa: E501


        :return: The id of this CommonConversationDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommonConversationDto.


        :param id: The id of this CommonConversationDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this CommonConversationDto.  # noqa: E501


        :return: The date_created of this CommonConversationDto.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this CommonConversationDto.


        :param date_created: The date_created of this CommonConversationDto.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this CommonConversationDto.  # noqa: E501


        :return: The date_modified of this CommonConversationDto.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this CommonConversationDto.


        :param date_modified: The date_modified of this CommonConversationDto.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def comments(self):
        """Gets the comments of this CommonConversationDto.  # noqa: E501


        :return: The comments of this CommonConversationDto.  # noqa: E501
        :rtype: list[CommentDto]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this CommonConversationDto.


        :param comments: The comments of this CommonConversationDto.  # noqa: E501
        :type: list[CommentDto]
        """

        self._comments = comments

    @property
    def status(self):
        """Gets the status of this CommonConversationDto.  # noqa: E501


        :return: The status of this CommonConversationDto.  # noqa: E501
        :rtype: StatusDto
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CommonConversationDto.


        :param status: The status of this CommonConversationDto.  # noqa: E501
        :type: StatusDto
        """

        self._status = status

    @property
    def deleted(self):
        """Gets the deleted of this CommonConversationDto.  # noqa: E501


        :return: The deleted of this CommonConversationDto.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this CommonConversationDto.


        :param deleted: The deleted of this CommonConversationDto.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(CommonConversationDto, dict):
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
        if not isinstance(other, CommonConversationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
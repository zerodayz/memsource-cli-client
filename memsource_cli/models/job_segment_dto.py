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

from memsource_cli.models.user_reference import UserReference  # noqa: F401,E501
from memsource_cli.models.workflow_step_dto import WorkflowStepDto  # noqa: F401,E501


class JobSegmentDto(object):
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
        'source': 'str',
        'translation': 'str',
        'created_at': 'int',
        'modified_at': 'int',
        'created_by': 'UserReference',
        'modified_by': 'UserReference',
        'workflow_level': 'int',
        'workflow_step': 'WorkflowStepDto'
    }

    attribute_map = {
        'id': 'id',
        'source': 'source',
        'translation': 'translation',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt',
        'created_by': 'createdBy',
        'modified_by': 'modifiedBy',
        'workflow_level': 'workflowLevel',
        'workflow_step': 'workflowStep'
    }

    def __init__(self, id=None, source=None, translation=None, created_at=None, modified_at=None, created_by=None, modified_by=None, workflow_level=None, workflow_step=None):  # noqa: E501
        """JobSegmentDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._source = None
        self._translation = None
        self._created_at = None
        self._modified_at = None
        self._created_by = None
        self._modified_by = None
        self._workflow_level = None
        self._workflow_step = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if source is not None:
            self.source = source
        if translation is not None:
            self.translation = translation
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if workflow_level is not None:
            self.workflow_level = workflow_level
        if workflow_step is not None:
            self.workflow_step = workflow_step

    @property
    def id(self):
        """Gets the id of this JobSegmentDto.  # noqa: E501


        :return: The id of this JobSegmentDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobSegmentDto.


        :param id: The id of this JobSegmentDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def source(self):
        """Gets the source of this JobSegmentDto.  # noqa: E501


        :return: The source of this JobSegmentDto.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this JobSegmentDto.


        :param source: The source of this JobSegmentDto.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def translation(self):
        """Gets the translation of this JobSegmentDto.  # noqa: E501


        :return: The translation of this JobSegmentDto.  # noqa: E501
        :rtype: str
        """
        return self._translation

    @translation.setter
    def translation(self, translation):
        """Sets the translation of this JobSegmentDto.


        :param translation: The translation of this JobSegmentDto.  # noqa: E501
        :type: str
        """

        self._translation = translation

    @property
    def created_at(self):
        """Gets the created_at of this JobSegmentDto.  # noqa: E501


        :return: The created_at of this JobSegmentDto.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this JobSegmentDto.


        :param created_at: The created_at of this JobSegmentDto.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this JobSegmentDto.  # noqa: E501


        :return: The modified_at of this JobSegmentDto.  # noqa: E501
        :rtype: int
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this JobSegmentDto.


        :param modified_at: The modified_at of this JobSegmentDto.  # noqa: E501
        :type: int
        """

        self._modified_at = modified_at

    @property
    def created_by(self):
        """Gets the created_by of this JobSegmentDto.  # noqa: E501


        :return: The created_by of this JobSegmentDto.  # noqa: E501
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this JobSegmentDto.


        :param created_by: The created_by of this JobSegmentDto.  # noqa: E501
        :type: UserReference
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this JobSegmentDto.  # noqa: E501


        :return: The modified_by of this JobSegmentDto.  # noqa: E501
        :rtype: UserReference
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this JobSegmentDto.


        :param modified_by: The modified_by of this JobSegmentDto.  # noqa: E501
        :type: UserReference
        """

        self._modified_by = modified_by

    @property
    def workflow_level(self):
        """Gets the workflow_level of this JobSegmentDto.  # noqa: E501


        :return: The workflow_level of this JobSegmentDto.  # noqa: E501
        :rtype: int
        """
        return self._workflow_level

    @workflow_level.setter
    def workflow_level(self, workflow_level):
        """Sets the workflow_level of this JobSegmentDto.


        :param workflow_level: The workflow_level of this JobSegmentDto.  # noqa: E501
        :type: int
        """

        self._workflow_level = workflow_level

    @property
    def workflow_step(self):
        """Gets the workflow_step of this JobSegmentDto.  # noqa: E501


        :return: The workflow_step of this JobSegmentDto.  # noqa: E501
        :rtype: WorkflowStepDto
        """
        return self._workflow_step

    @workflow_step.setter
    def workflow_step(self, workflow_step):
        """Sets the workflow_step of this JobSegmentDto.


        :param workflow_step: The workflow_step of this JobSegmentDto.  # noqa: E501
        :type: WorkflowStepDto
        """

        self._workflow_step = workflow_step

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
        if issubclass(JobSegmentDto, dict):
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
        if not isinstance(other, JobSegmentDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

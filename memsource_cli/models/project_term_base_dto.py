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

from memsource_cli.models.term_base_dto import TermBaseDto  # noqa: F401,E501
from memsource_cli.models.workflow_step_reference import WorkflowStepReference  # noqa: F401,E501


class ProjectTermBaseDto(object):
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
        'target_locale': 'str',
        'workflow_step': 'WorkflowStepReference',
        'read_mode': 'bool',
        'write_mode': 'bool',
        'term_base': 'TermBaseDto',
        'quality_assurance': 'bool'
    }

    attribute_map = {
        'target_locale': 'targetLocale',
        'workflow_step': 'workflowStep',
        'read_mode': 'readMode',
        'write_mode': 'writeMode',
        'term_base': 'termBase',
        'quality_assurance': 'qualityAssurance'
    }

    def __init__(self, target_locale=None, workflow_step=None, read_mode=None, write_mode=None, term_base=None, quality_assurance=None):  # noqa: E501
        """ProjectTermBaseDto - a model defined in Swagger"""  # noqa: E501

        self._target_locale = None
        self._workflow_step = None
        self._read_mode = None
        self._write_mode = None
        self._term_base = None
        self._quality_assurance = None
        self.discriminator = None

        if target_locale is not None:
            self.target_locale = target_locale
        if workflow_step is not None:
            self.workflow_step = workflow_step
        if read_mode is not None:
            self.read_mode = read_mode
        if write_mode is not None:
            self.write_mode = write_mode
        if term_base is not None:
            self.term_base = term_base
        if quality_assurance is not None:
            self.quality_assurance = quality_assurance

    @property
    def target_locale(self):
        """Gets the target_locale of this ProjectTermBaseDto.  # noqa: E501


        :return: The target_locale of this ProjectTermBaseDto.  # noqa: E501
        :rtype: str
        """
        return self._target_locale

    @target_locale.setter
    def target_locale(self, target_locale):
        """Sets the target_locale of this ProjectTermBaseDto.


        :param target_locale: The target_locale of this ProjectTermBaseDto.  # noqa: E501
        :type: str
        """

        self._target_locale = target_locale

    @property
    def workflow_step(self):
        """Gets the workflow_step of this ProjectTermBaseDto.  # noqa: E501


        :return: The workflow_step of this ProjectTermBaseDto.  # noqa: E501
        :rtype: WorkflowStepReference
        """
        return self._workflow_step

    @workflow_step.setter
    def workflow_step(self, workflow_step):
        """Sets the workflow_step of this ProjectTermBaseDto.


        :param workflow_step: The workflow_step of this ProjectTermBaseDto.  # noqa: E501
        :type: WorkflowStepReference
        """

        self._workflow_step = workflow_step

    @property
    def read_mode(self):
        """Gets the read_mode of this ProjectTermBaseDto.  # noqa: E501


        :return: The read_mode of this ProjectTermBaseDto.  # noqa: E501
        :rtype: bool
        """
        return self._read_mode

    @read_mode.setter
    def read_mode(self, read_mode):
        """Sets the read_mode of this ProjectTermBaseDto.


        :param read_mode: The read_mode of this ProjectTermBaseDto.  # noqa: E501
        :type: bool
        """

        self._read_mode = read_mode

    @property
    def write_mode(self):
        """Gets the write_mode of this ProjectTermBaseDto.  # noqa: E501


        :return: The write_mode of this ProjectTermBaseDto.  # noqa: E501
        :rtype: bool
        """
        return self._write_mode

    @write_mode.setter
    def write_mode(self, write_mode):
        """Sets the write_mode of this ProjectTermBaseDto.


        :param write_mode: The write_mode of this ProjectTermBaseDto.  # noqa: E501
        :type: bool
        """

        self._write_mode = write_mode

    @property
    def term_base(self):
        """Gets the term_base of this ProjectTermBaseDto.  # noqa: E501


        :return: The term_base of this ProjectTermBaseDto.  # noqa: E501
        :rtype: TermBaseDto
        """
        return self._term_base

    @term_base.setter
    def term_base(self, term_base):
        """Sets the term_base of this ProjectTermBaseDto.


        :param term_base: The term_base of this ProjectTermBaseDto.  # noqa: E501
        :type: TermBaseDto
        """

        self._term_base = term_base

    @property
    def quality_assurance(self):
        """Gets the quality_assurance of this ProjectTermBaseDto.  # noqa: E501


        :return: The quality_assurance of this ProjectTermBaseDto.  # noqa: E501
        :rtype: bool
        """
        return self._quality_assurance

    @quality_assurance.setter
    def quality_assurance(self, quality_assurance):
        """Sets the quality_assurance of this ProjectTermBaseDto.


        :param quality_assurance: The quality_assurance of this ProjectTermBaseDto.  # noqa: E501
        :type: bool
        """

        self._quality_assurance = quality_assurance

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
        if issubclass(ProjectTermBaseDto, dict):
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
        if not isinstance(other, ProjectTermBaseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

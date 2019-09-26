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
from memsource_cli.models.project_template_notify_provider_dto import ProjectTemplateNotifyProviderDto  # noqa: F401,E501
from memsource_cli.models.project_template_workflow_settings_assigned_to_dto import ProjectTemplateWorkflowSettingsAssignedToDto  # noqa: F401,E501


class WorkflowStepSettingsEditDto(object):
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
        'workflow_step': 'IdReference',
        'assigned_to': 'list[ProjectTemplateWorkflowSettingsAssignedToDto]',
        'notify_provider': 'ProjectTemplateNotifyProviderDto'
    }

    attribute_map = {
        'workflow_step': 'workflowStep',
        'assigned_to': 'assignedTo',
        'notify_provider': 'notifyProvider'
    }

    def __init__(self, workflow_step=None, assigned_to=None, notify_provider=None):  # noqa: E501
        """WorkflowStepSettingsEditDto - a model defined in Swagger"""  # noqa: E501

        self._workflow_step = None
        self._assigned_to = None
        self._notify_provider = None
        self.discriminator = None

        if workflow_step is not None:
            self.workflow_step = workflow_step
        if assigned_to is not None:
            self.assigned_to = assigned_to
        if notify_provider is not None:
            self.notify_provider = notify_provider

    @property
    def workflow_step(self):
        """Gets the workflow_step of this WorkflowStepSettingsEditDto.  # noqa: E501


        :return: The workflow_step of this WorkflowStepSettingsEditDto.  # noqa: E501
        :rtype: IdReference
        """
        return self._workflow_step

    @workflow_step.setter
    def workflow_step(self, workflow_step):
        """Sets the workflow_step of this WorkflowStepSettingsEditDto.


        :param workflow_step: The workflow_step of this WorkflowStepSettingsEditDto.  # noqa: E501
        :type: IdReference
        """

        self._workflow_step = workflow_step

    @property
    def assigned_to(self):
        """Gets the assigned_to of this WorkflowStepSettingsEditDto.  # noqa: E501


        :return: The assigned_to of this WorkflowStepSettingsEditDto.  # noqa: E501
        :rtype: list[ProjectTemplateWorkflowSettingsAssignedToDto]
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this WorkflowStepSettingsEditDto.


        :param assigned_to: The assigned_to of this WorkflowStepSettingsEditDto.  # noqa: E501
        :type: list[ProjectTemplateWorkflowSettingsAssignedToDto]
        """

        self._assigned_to = assigned_to

    @property
    def notify_provider(self):
        """Gets the notify_provider of this WorkflowStepSettingsEditDto.  # noqa: E501


        :return: The notify_provider of this WorkflowStepSettingsEditDto.  # noqa: E501
        :rtype: ProjectTemplateNotifyProviderDto
        """
        return self._notify_provider

    @notify_provider.setter
    def notify_provider(self, notify_provider):
        """Sets the notify_provider of this WorkflowStepSettingsEditDto.


        :param notify_provider: The notify_provider of this WorkflowStepSettingsEditDto.  # noqa: E501
        :type: ProjectTemplateNotifyProviderDto
        """

        self._notify_provider = notify_provider

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
        if issubclass(WorkflowStepSettingsEditDto, dict):
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
        if not isinstance(other, WorkflowStepSettingsEditDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

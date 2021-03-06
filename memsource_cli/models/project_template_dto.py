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

from memsource_cli.models.assignment_per_target_lang_dto import AssignmentPerTargetLangDto  # noqa: F401,E501
from memsource_cli.models.business_unit_reference import BusinessUnitReference  # noqa: F401,E501
from memsource_cli.models.client_reference import ClientReference  # noqa: F401,E501
from memsource_cli.models.domain_reference import DomainReference  # noqa: F401,E501
from memsource_cli.models.project_template_notify_provider_dto import ProjectTemplateNotifyProviderDto  # noqa: F401,E501
from memsource_cli.models.sub_domain_reference import SubDomainReference  # noqa: F401,E501
from memsource_cli.models.user_reference import UserReference  # noqa: F401,E501
from memsource_cli.models.workflow_step_dto import WorkflowStepDto  # noqa: F401,E501
from memsource_cli.models.workflow_step_settings_dto import WorkflowStepSettingsDto  # noqa: F401,E501


class ProjectTemplateDto(object):
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
        'template_name': 'str',
        'name': 'str',
        'source_lang': 'str',
        'target_langs': 'list[str]',
        'note': 'str',
        'owner': 'UserReference',
        'client': 'ClientReference',
        'domain': 'DomainReference',
        'sub_domain': 'SubDomainReference',
        'created_by': 'UserReference',
        'date_created': 'datetime',
        'workflow_steps': 'list[WorkflowStepDto]',
        'workflow_settings': 'list[WorkflowStepSettingsDto]',
        'business_unit': 'BusinessUnitReference',
        'notify_providers': 'ProjectTemplateNotifyProviderDto',
        'assigned_to': 'list[AssignmentPerTargetLangDto]'
    }

    attribute_map = {
        'id': 'id',
        'template_name': 'templateName',
        'name': 'name',
        'source_lang': 'sourceLang',
        'target_langs': 'targetLangs',
        'note': 'note',
        'owner': 'owner',
        'client': 'client',
        'domain': 'domain',
        'sub_domain': 'subDomain',
        'created_by': 'createdBy',
        'date_created': 'dateCreated',
        'workflow_steps': 'workflowSteps',
        'workflow_settings': 'workflowSettings',
        'business_unit': 'businessUnit',
        'notify_providers': 'notifyProviders',
        'assigned_to': 'assignedTo'
    }

    def __init__(self, id=None, template_name=None, name=None, source_lang=None, target_langs=None, note=None, owner=None, client=None, domain=None, sub_domain=None, created_by=None, date_created=None, workflow_steps=None, workflow_settings=None, business_unit=None, notify_providers=None, assigned_to=None):  # noqa: E501
        """ProjectTemplateDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._template_name = None
        self._name = None
        self._source_lang = None
        self._target_langs = None
        self._note = None
        self._owner = None
        self._client = None
        self._domain = None
        self._sub_domain = None
        self._created_by = None
        self._date_created = None
        self._workflow_steps = None
        self._workflow_settings = None
        self._business_unit = None
        self._notify_providers = None
        self._assigned_to = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if template_name is not None:
            self.template_name = template_name
        if name is not None:
            self.name = name
        if source_lang is not None:
            self.source_lang = source_lang
        if target_langs is not None:
            self.target_langs = target_langs
        if note is not None:
            self.note = note
        if owner is not None:
            self.owner = owner
        if client is not None:
            self.client = client
        if domain is not None:
            self.domain = domain
        if sub_domain is not None:
            self.sub_domain = sub_domain
        if created_by is not None:
            self.created_by = created_by
        if date_created is not None:
            self.date_created = date_created
        if workflow_steps is not None:
            self.workflow_steps = workflow_steps
        if workflow_settings is not None:
            self.workflow_settings = workflow_settings
        if business_unit is not None:
            self.business_unit = business_unit
        if notify_providers is not None:
            self.notify_providers = notify_providers
        if assigned_to is not None:
            self.assigned_to = assigned_to

    @property
    def id(self):
        """Gets the id of this ProjectTemplateDto.  # noqa: E501


        :return: The id of this ProjectTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectTemplateDto.


        :param id: The id of this ProjectTemplateDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def template_name(self):
        """Gets the template_name of this ProjectTemplateDto.  # noqa: E501


        :return: The template_name of this ProjectTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this ProjectTemplateDto.


        :param template_name: The template_name of this ProjectTemplateDto.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

    @property
    def name(self):
        """Gets the name of this ProjectTemplateDto.  # noqa: E501


        :return: The name of this ProjectTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectTemplateDto.


        :param name: The name of this ProjectTemplateDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def source_lang(self):
        """Gets the source_lang of this ProjectTemplateDto.  # noqa: E501


        :return: The source_lang of this ProjectTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._source_lang

    @source_lang.setter
    def source_lang(self, source_lang):
        """Sets the source_lang of this ProjectTemplateDto.


        :param source_lang: The source_lang of this ProjectTemplateDto.  # noqa: E501
        :type: str
        """

        self._source_lang = source_lang

    @property
    def target_langs(self):
        """Gets the target_langs of this ProjectTemplateDto.  # noqa: E501


        :return: The target_langs of this ProjectTemplateDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_langs

    @target_langs.setter
    def target_langs(self, target_langs):
        """Sets the target_langs of this ProjectTemplateDto.


        :param target_langs: The target_langs of this ProjectTemplateDto.  # noqa: E501
        :type: list[str]
        """

        self._target_langs = target_langs

    @property
    def note(self):
        """Gets the note of this ProjectTemplateDto.  # noqa: E501


        :return: The note of this ProjectTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ProjectTemplateDto.


        :param note: The note of this ProjectTemplateDto.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def owner(self):
        """Gets the owner of this ProjectTemplateDto.  # noqa: E501


        :return: The owner of this ProjectTemplateDto.  # noqa: E501
        :rtype: UserReference
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ProjectTemplateDto.


        :param owner: The owner of this ProjectTemplateDto.  # noqa: E501
        :type: UserReference
        """

        self._owner = owner

    @property
    def client(self):
        """Gets the client of this ProjectTemplateDto.  # noqa: E501


        :return: The client of this ProjectTemplateDto.  # noqa: E501
        :rtype: ClientReference
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this ProjectTemplateDto.


        :param client: The client of this ProjectTemplateDto.  # noqa: E501
        :type: ClientReference
        """

        self._client = client

    @property
    def domain(self):
        """Gets the domain of this ProjectTemplateDto.  # noqa: E501


        :return: The domain of this ProjectTemplateDto.  # noqa: E501
        :rtype: DomainReference
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ProjectTemplateDto.


        :param domain: The domain of this ProjectTemplateDto.  # noqa: E501
        :type: DomainReference
        """

        self._domain = domain

    @property
    def sub_domain(self):
        """Gets the sub_domain of this ProjectTemplateDto.  # noqa: E501


        :return: The sub_domain of this ProjectTemplateDto.  # noqa: E501
        :rtype: SubDomainReference
        """
        return self._sub_domain

    @sub_domain.setter
    def sub_domain(self, sub_domain):
        """Sets the sub_domain of this ProjectTemplateDto.


        :param sub_domain: The sub_domain of this ProjectTemplateDto.  # noqa: E501
        :type: SubDomainReference
        """

        self._sub_domain = sub_domain

    @property
    def created_by(self):
        """Gets the created_by of this ProjectTemplateDto.  # noqa: E501


        :return: The created_by of this ProjectTemplateDto.  # noqa: E501
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ProjectTemplateDto.


        :param created_by: The created_by of this ProjectTemplateDto.  # noqa: E501
        :type: UserReference
        """

        self._created_by = created_by

    @property
    def date_created(self):
        """Gets the date_created of this ProjectTemplateDto.  # noqa: E501


        :return: The date_created of this ProjectTemplateDto.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this ProjectTemplateDto.


        :param date_created: The date_created of this ProjectTemplateDto.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def workflow_steps(self):
        """Gets the workflow_steps of this ProjectTemplateDto.  # noqa: E501


        :return: The workflow_steps of this ProjectTemplateDto.  # noqa: E501
        :rtype: list[WorkflowStepDto]
        """
        return self._workflow_steps

    @workflow_steps.setter
    def workflow_steps(self, workflow_steps):
        """Sets the workflow_steps of this ProjectTemplateDto.


        :param workflow_steps: The workflow_steps of this ProjectTemplateDto.  # noqa: E501
        :type: list[WorkflowStepDto]
        """

        self._workflow_steps = workflow_steps

    @property
    def workflow_settings(self):
        """Gets the workflow_settings of this ProjectTemplateDto.  # noqa: E501


        :return: The workflow_settings of this ProjectTemplateDto.  # noqa: E501
        :rtype: list[WorkflowStepSettingsDto]
        """
        return self._workflow_settings

    @workflow_settings.setter
    def workflow_settings(self, workflow_settings):
        """Sets the workflow_settings of this ProjectTemplateDto.


        :param workflow_settings: The workflow_settings of this ProjectTemplateDto.  # noqa: E501
        :type: list[WorkflowStepSettingsDto]
        """

        self._workflow_settings = workflow_settings

    @property
    def business_unit(self):
        """Gets the business_unit of this ProjectTemplateDto.  # noqa: E501


        :return: The business_unit of this ProjectTemplateDto.  # noqa: E501
        :rtype: BusinessUnitReference
        """
        return self._business_unit

    @business_unit.setter
    def business_unit(self, business_unit):
        """Sets the business_unit of this ProjectTemplateDto.


        :param business_unit: The business_unit of this ProjectTemplateDto.  # noqa: E501
        :type: BusinessUnitReference
        """

        self._business_unit = business_unit

    @property
    def notify_providers(self):
        """Gets the notify_providers of this ProjectTemplateDto.  # noqa: E501


        :return: The notify_providers of this ProjectTemplateDto.  # noqa: E501
        :rtype: ProjectTemplateNotifyProviderDto
        """
        return self._notify_providers

    @notify_providers.setter
    def notify_providers(self, notify_providers):
        """Sets the notify_providers of this ProjectTemplateDto.


        :param notify_providers: The notify_providers of this ProjectTemplateDto.  # noqa: E501
        :type: ProjectTemplateNotifyProviderDto
        """

        self._notify_providers = notify_providers

    @property
    def assigned_to(self):
        """Gets the assigned_to of this ProjectTemplateDto.  # noqa: E501


        :return: The assigned_to of this ProjectTemplateDto.  # noqa: E501
        :rtype: list[AssignmentPerTargetLangDto]
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this ProjectTemplateDto.


        :param assigned_to: The assigned_to of this ProjectTemplateDto.  # noqa: E501
        :type: list[AssignmentPerTargetLangDto]
        """

        self._assigned_to = assigned_to

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
        if issubclass(ProjectTemplateDto, dict):
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
        if not isinstance(other, ProjectTemplateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

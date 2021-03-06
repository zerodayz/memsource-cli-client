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


class UserEditDtoV2(object):
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
        'user_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'role': 'str',
        'timezone': 'str',
        'note': 'str',
        'may_edit_approved_terms': 'bool',
        'may_reject_jobs': 'bool',
        'editor_machine_translate_enabled': 'bool',
        'receive_newsletter': 'bool',
        'may_edit_translation_memory': 'bool',
        'source_langs': 'list[str]',
        'target_langs': 'list[str]',
        'active': 'bool',
        'workflow_steps': 'list[IdReference]',
        'clients': 'list[IdReference]',
        'domains': 'list[IdReference]',
        'sub_domains': 'list[IdReference]',
        'project_business_units': 'list[IdReference]'
    }

    attribute_map = {
        'user_name': 'userName',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'role': 'role',
        'timezone': 'timezone',
        'note': 'note',
        'may_edit_approved_terms': 'mayEditApprovedTerms',
        'may_reject_jobs': 'mayRejectJobs',
        'editor_machine_translate_enabled': 'editorMachineTranslateEnabled',
        'receive_newsletter': 'receiveNewsletter',
        'may_edit_translation_memory': 'mayEditTranslationMemory',
        'source_langs': 'sourceLangs',
        'target_langs': 'targetLangs',
        'active': 'active',
        'workflow_steps': 'workflowSteps',
        'clients': 'clients',
        'domains': 'domains',
        'sub_domains': 'subDomains',
        'project_business_units': 'projectBusinessUnits'
    }

    def __init__(self, user_name=None, first_name=None, last_name=None, email=None, role=None, timezone=None, note=None, may_edit_approved_terms=None, may_reject_jobs=None, editor_machine_translate_enabled=None, receive_newsletter=None, may_edit_translation_memory=None, source_langs=None, target_langs=None, active=None, workflow_steps=None, clients=None, domains=None, sub_domains=None, project_business_units=None):  # noqa: E501
        """UserEditDtoV2 - a model defined in Swagger"""  # noqa: E501

        self._user_name = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._role = None
        self._timezone = None
        self._note = None
        self._may_edit_approved_terms = None
        self._may_reject_jobs = None
        self._editor_machine_translate_enabled = None
        self._receive_newsletter = None
        self._may_edit_translation_memory = None
        self._source_langs = None
        self._target_langs = None
        self._active = None
        self._workflow_steps = None
        self._clients = None
        self._domains = None
        self._sub_domains = None
        self._project_business_units = None
        self.discriminator = None

        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role = role
        self.timezone = timezone
        if note is not None:
            self.note = note
        if may_edit_approved_terms is not None:
            self.may_edit_approved_terms = may_edit_approved_terms
        if may_reject_jobs is not None:
            self.may_reject_jobs = may_reject_jobs
        if editor_machine_translate_enabled is not None:
            self.editor_machine_translate_enabled = editor_machine_translate_enabled
        if receive_newsletter is not None:
            self.receive_newsletter = receive_newsletter
        if may_edit_translation_memory is not None:
            self.may_edit_translation_memory = may_edit_translation_memory
        if source_langs is not None:
            self.source_langs = source_langs
        if target_langs is not None:
            self.target_langs = target_langs
        if active is not None:
            self.active = active
        if workflow_steps is not None:
            self.workflow_steps = workflow_steps
        if clients is not None:
            self.clients = clients
        if domains is not None:
            self.domains = domains
        if sub_domains is not None:
            self.sub_domains = sub_domains
        if project_business_units is not None:
            self.project_business_units = project_business_units

    @property
    def user_name(self):
        """Gets the user_name of this UserEditDtoV2.  # noqa: E501


        :return: The user_name of this UserEditDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserEditDtoV2.


        :param user_name: The user_name of this UserEditDtoV2.  # noqa: E501
        :type: str
        """
        if user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501
        if user_name is not None and len(user_name) > 255:
            raise ValueError("Invalid value for `user_name`, length must be less than or equal to `255`")  # noqa: E501
        if user_name is not None and len(user_name) < 0:
            raise ValueError("Invalid value for `user_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._user_name = user_name

    @property
    def first_name(self):
        """Gets the first_name of this UserEditDtoV2.  # noqa: E501


        :return: The first_name of this UserEditDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserEditDtoV2.


        :param first_name: The first_name of this UserEditDtoV2.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if first_name is not None and len(first_name) > 255:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `255`")  # noqa: E501
        if first_name is not None and len(first_name) < 0:
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserEditDtoV2.  # noqa: E501


        :return: The last_name of this UserEditDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserEditDtoV2.


        :param last_name: The last_name of this UserEditDtoV2.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501
        if last_name is not None and len(last_name) > 255:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `255`")  # noqa: E501
        if last_name is not None and len(last_name) < 0:
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this UserEditDtoV2.  # noqa: E501


        :return: The email of this UserEditDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserEditDtoV2.


        :param email: The email of this UserEditDtoV2.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if email is not None and len(email) > 255:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `255`")  # noqa: E501
        if email is not None and len(email) < 0:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `0`")  # noqa: E501

        self._email = email

    @property
    def role(self):
        """Gets the role of this UserEditDtoV2.  # noqa: E501


        :return: The role of this UserEditDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserEditDtoV2.


        :param role: The role of this UserEditDtoV2.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["ADMIN", "PROJECT_MANAGER", "LINGUIST", "GUEST", "SUBMITTER"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def timezone(self):
        """Gets the timezone of this UserEditDtoV2.  # noqa: E501


        :return: The timezone of this UserEditDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this UserEditDtoV2.


        :param timezone: The timezone of this UserEditDtoV2.  # noqa: E501
        :type: str
        """
        if timezone is None:
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501
        if timezone is not None and len(timezone) > 255:
            raise ValueError("Invalid value for `timezone`, length must be less than or equal to `255`")  # noqa: E501
        if timezone is not None and len(timezone) < 0:
            raise ValueError("Invalid value for `timezone`, length must be greater than or equal to `0`")  # noqa: E501

        self._timezone = timezone

    @property
    def note(self):
        """Gets the note of this UserEditDtoV2.  # noqa: E501


        :return: The note of this UserEditDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this UserEditDtoV2.


        :param note: The note of this UserEditDtoV2.  # noqa: E501
        :type: str
        """
        if note is not None and len(note) > 4096:
            raise ValueError("Invalid value for `note`, length must be less than or equal to `4096`")  # noqa: E501
        if note is not None and len(note) < 0:
            raise ValueError("Invalid value for `note`, length must be greater than or equal to `0`")  # noqa: E501

        self._note = note

    @property
    def may_edit_approved_terms(self):
        """Gets the may_edit_approved_terms of this UserEditDtoV2.  # noqa: E501

        In previous version as terminologist. Default: false  # noqa: E501

        :return: The may_edit_approved_terms of this UserEditDtoV2.  # noqa: E501
        :rtype: bool
        """
        return self._may_edit_approved_terms

    @may_edit_approved_terms.setter
    def may_edit_approved_terms(self, may_edit_approved_terms):
        """Sets the may_edit_approved_terms of this UserEditDtoV2.

        In previous version as terminologist. Default: false  # noqa: E501

        :param may_edit_approved_terms: The may_edit_approved_terms of this UserEditDtoV2.  # noqa: E501
        :type: bool
        """

        self._may_edit_approved_terms = may_edit_approved_terms

    @property
    def may_reject_jobs(self):
        """Gets the may_reject_jobs of this UserEditDtoV2.  # noqa: E501

        Default: false  # noqa: E501

        :return: The may_reject_jobs of this UserEditDtoV2.  # noqa: E501
        :rtype: bool
        """
        return self._may_reject_jobs

    @may_reject_jobs.setter
    def may_reject_jobs(self, may_reject_jobs):
        """Sets the may_reject_jobs of this UserEditDtoV2.

        Default: false  # noqa: E501

        :param may_reject_jobs: The may_reject_jobs of this UserEditDtoV2.  # noqa: E501
        :type: bool
        """

        self._may_reject_jobs = may_reject_jobs

    @property
    def editor_machine_translate_enabled(self):
        """Gets the editor_machine_translate_enabled of this UserEditDtoV2.  # noqa: E501

        Applies only to Linguist or Guest. Default: true  # noqa: E501

        :return: The editor_machine_translate_enabled of this UserEditDtoV2.  # noqa: E501
        :rtype: bool
        """
        return self._editor_machine_translate_enabled

    @editor_machine_translate_enabled.setter
    def editor_machine_translate_enabled(self, editor_machine_translate_enabled):
        """Sets the editor_machine_translate_enabled of this UserEditDtoV2.

        Applies only to Linguist or Guest. Default: true  # noqa: E501

        :param editor_machine_translate_enabled: The editor_machine_translate_enabled of this UserEditDtoV2.  # noqa: E501
        :type: bool
        """

        self._editor_machine_translate_enabled = editor_machine_translate_enabled

    @property
    def receive_newsletter(self):
        """Gets the receive_newsletter of this UserEditDtoV2.  # noqa: E501

        Default: true  # noqa: E501

        :return: The receive_newsletter of this UserEditDtoV2.  # noqa: E501
        :rtype: bool
        """
        return self._receive_newsletter

    @receive_newsletter.setter
    def receive_newsletter(self, receive_newsletter):
        """Sets the receive_newsletter of this UserEditDtoV2.

        Default: true  # noqa: E501

        :param receive_newsletter: The receive_newsletter of this UserEditDtoV2.  # noqa: E501
        :type: bool
        """

        self._receive_newsletter = receive_newsletter

    @property
    def may_edit_translation_memory(self):
        """Gets the may_edit_translation_memory of this UserEditDtoV2.  # noqa: E501

        Default: false  # noqa: E501

        :return: The may_edit_translation_memory of this UserEditDtoV2.  # noqa: E501
        :rtype: bool
        """
        return self._may_edit_translation_memory

    @may_edit_translation_memory.setter
    def may_edit_translation_memory(self, may_edit_translation_memory):
        """Sets the may_edit_translation_memory of this UserEditDtoV2.

        Default: false  # noqa: E501

        :param may_edit_translation_memory: The may_edit_translation_memory of this UserEditDtoV2.  # noqa: E501
        :type: bool
        """

        self._may_edit_translation_memory = may_edit_translation_memory

    @property
    def source_langs(self):
        """Gets the source_langs of this UserEditDtoV2.  # noqa: E501


        :return: The source_langs of this UserEditDtoV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_langs

    @source_langs.setter
    def source_langs(self, source_langs):
        """Sets the source_langs of this UserEditDtoV2.


        :param source_langs: The source_langs of this UserEditDtoV2.  # noqa: E501
        :type: list[str]
        """

        self._source_langs = source_langs

    @property
    def target_langs(self):
        """Gets the target_langs of this UserEditDtoV2.  # noqa: E501


        :return: The target_langs of this UserEditDtoV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_langs

    @target_langs.setter
    def target_langs(self, target_langs):
        """Sets the target_langs of this UserEditDtoV2.


        :param target_langs: The target_langs of this UserEditDtoV2.  # noqa: E501
        :type: list[str]
        """

        self._target_langs = target_langs

    @property
    def active(self):
        """Gets the active of this UserEditDtoV2.  # noqa: E501

        Default: true  # noqa: E501

        :return: The active of this UserEditDtoV2.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this UserEditDtoV2.

        Default: true  # noqa: E501

        :param active: The active of this UserEditDtoV2.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def workflow_steps(self):
        """Gets the workflow_steps of this UserEditDtoV2.  # noqa: E501


        :return: The workflow_steps of this UserEditDtoV2.  # noqa: E501
        :rtype: list[IdReference]
        """
        return self._workflow_steps

    @workflow_steps.setter
    def workflow_steps(self, workflow_steps):
        """Sets the workflow_steps of this UserEditDtoV2.


        :param workflow_steps: The workflow_steps of this UserEditDtoV2.  # noqa: E501
        :type: list[IdReference]
        """

        self._workflow_steps = workflow_steps

    @property
    def clients(self):
        """Gets the clients of this UserEditDtoV2.  # noqa: E501


        :return: The clients of this UserEditDtoV2.  # noqa: E501
        :rtype: list[IdReference]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this UserEditDtoV2.


        :param clients: The clients of this UserEditDtoV2.  # noqa: E501
        :type: list[IdReference]
        """

        self._clients = clients

    @property
    def domains(self):
        """Gets the domains of this UserEditDtoV2.  # noqa: E501


        :return: The domains of this UserEditDtoV2.  # noqa: E501
        :rtype: list[IdReference]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this UserEditDtoV2.


        :param domains: The domains of this UserEditDtoV2.  # noqa: E501
        :type: list[IdReference]
        """

        self._domains = domains

    @property
    def sub_domains(self):
        """Gets the sub_domains of this UserEditDtoV2.  # noqa: E501


        :return: The sub_domains of this UserEditDtoV2.  # noqa: E501
        :rtype: list[IdReference]
        """
        return self._sub_domains

    @sub_domains.setter
    def sub_domains(self, sub_domains):
        """Sets the sub_domains of this UserEditDtoV2.


        :param sub_domains: The sub_domains of this UserEditDtoV2.  # noqa: E501
        :type: list[IdReference]
        """

        self._sub_domains = sub_domains

    @property
    def project_business_units(self):
        """Gets the project_business_units of this UserEditDtoV2.  # noqa: E501


        :return: The project_business_units of this UserEditDtoV2.  # noqa: E501
        :rtype: list[IdReference]
        """
        return self._project_business_units

    @project_business_units.setter
    def project_business_units(self, project_business_units):
        """Sets the project_business_units of this UserEditDtoV2.


        :param project_business_units: The project_business_units of this UserEditDtoV2.  # noqa: E501
        :type: list[IdReference]
        """

        self._project_business_units = project_business_units

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
        if issubclass(UserEditDtoV2, dict):
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
        if not isinstance(other, UserEditDtoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

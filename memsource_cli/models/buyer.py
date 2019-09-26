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

from memsource_cli.models.abstract_project_dto import AbstractProjectDto  # noqa: F401,E501
from memsource_cli.models.business_unit_reference import BusinessUnitReference  # noqa: F401,E501
from memsource_cli.models.client_reference import ClientReference  # noqa: F401,E501
from memsource_cli.models.cost_center_reference import CostCenterReference  # noqa: F401,E501
from memsource_cli.models.domain_reference import DomainReference  # noqa: F401,E501
from memsource_cli.models.id_reference import IdReference  # noqa: F401,E501
from memsource_cli.models.mt_settings_per_language_reference import MTSettingsPerLanguageReference  # noqa: F401,E501
from memsource_cli.models.progress_dto import ProgressDto  # noqa: F401,E501
from memsource_cli.models.project_workflow_step_dto import ProjectWorkflowStepDto  # noqa: F401,E501
from memsource_cli.models.reference_file_reference import ReferenceFileReference  # noqa: F401,E501
from memsource_cli.models.sub_domain_reference import SubDomainReference  # noqa: F401,E501
from memsource_cli.models.user import USER  # noqa: F401,E501
from memsource_cli.models.user_reference import UserReference  # noqa: F401,E501
from memsource_cli.models.vendor_reference import VendorReference  # noqa: F401,E501


class Buyer(AbstractProjectDto):
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
        'shared': 'bool',
        'progress': 'ProgressDto',
        'client': 'ClientReference',
        'cost_center': 'CostCenterReference',
        'business_unit': 'BusinessUnitReference',
        'date_due': 'datetime',
        'status': 'str',
        'purchase_order': 'str',
        'is_published_on_job_board': 'bool',
        'note': 'str',
        'created_by': 'UserReference',
        'quality_assurance_settings': 'IdReference',
        'workflow_steps': 'list[ProjectWorkflowStepDto]',
        'analyse_settings': 'IdReference',
        'access_settings': 'IdReference',
        'financial_settings': 'IdReference',
        'mt_settings_per_language_list': 'list[MTSettingsPerLanguageReference]',
        'vendor_owner': 'USER',
        'vendor': 'VendorReference'
    }

    attribute_map = {
        'shared': 'shared',
        'progress': 'progress',
        'client': 'client',
        'cost_center': 'costCenter',
        'business_unit': 'businessUnit',
        'date_due': 'dateDue',
        'status': 'status',
        'purchase_order': 'purchaseOrder',
        'is_published_on_job_board': 'isPublishedOnJobBoard',
        'note': 'note',
        'created_by': 'createdBy',
        'quality_assurance_settings': 'qualityAssuranceSettings',
        'workflow_steps': 'workflowSteps',
        'analyse_settings': 'analyseSettings',
        'access_settings': 'accessSettings',
        'financial_settings': 'financialSettings',
        'mt_settings_per_language_list': 'mtSettingsPerLanguageList',
        'vendor_owner': 'vendorOwner',
        'vendor': 'vendor'
    }

    def __init__(self, shared=None, progress=None, client=None, cost_center=None, business_unit=None, date_due=None, status=None, purchase_order=None, is_published_on_job_board=None, note=None, created_by=None, quality_assurance_settings=None, workflow_steps=None, analyse_settings=None, access_settings=None, financial_settings=None, mt_settings_per_language_list=None, vendor_owner=None, vendor=None):  # noqa: E501
        """Buyer - a model defined in Swagger"""  # noqa: E501

        self._shared = None
        self._progress = None
        self._client = None
        self._cost_center = None
        self._business_unit = None
        self._date_due = None
        self._status = None
        self._purchase_order = None
        self._is_published_on_job_board = None
        self._note = None
        self._created_by = None
        self._quality_assurance_settings = None
        self._workflow_steps = None
        self._analyse_settings = None
        self._access_settings = None
        self._financial_settings = None
        self._mt_settings_per_language_list = None
        self._vendor_owner = None
        self._vendor = None
        self.discriminator = None

        if shared is not None:
            self.shared = shared
        if progress is not None:
            self.progress = progress
        if client is not None:
            self.client = client
        if cost_center is not None:
            self.cost_center = cost_center
        if business_unit is not None:
            self.business_unit = business_unit
        if date_due is not None:
            self.date_due = date_due
        if status is not None:
            self.status = status
        if purchase_order is not None:
            self.purchase_order = purchase_order
        if is_published_on_job_board is not None:
            self.is_published_on_job_board = is_published_on_job_board
        if note is not None:
            self.note = note
        if created_by is not None:
            self.created_by = created_by
        if quality_assurance_settings is not None:
            self.quality_assurance_settings = quality_assurance_settings
        if workflow_steps is not None:
            self.workflow_steps = workflow_steps
        if analyse_settings is not None:
            self.analyse_settings = analyse_settings
        if access_settings is not None:
            self.access_settings = access_settings
        if financial_settings is not None:
            self.financial_settings = financial_settings
        if mt_settings_per_language_list is not None:
            self.mt_settings_per_language_list = mt_settings_per_language_list
        if vendor_owner is not None:
            self.vendor_owner = vendor_owner
        if vendor is not None:
            self.vendor = vendor

    @property
    def shared(self):
        """Gets the shared of this Buyer.  # noqa: E501

        Default: false  # noqa: E501

        :return: The shared of this Buyer.  # noqa: E501
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this Buyer.

        Default: false  # noqa: E501

        :param shared: The shared of this Buyer.  # noqa: E501
        :type: bool
        """

        self._shared = shared

    @property
    def progress(self):
        """Gets the progress of this Buyer.  # noqa: E501


        :return: The progress of this Buyer.  # noqa: E501
        :rtype: ProgressDto
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this Buyer.


        :param progress: The progress of this Buyer.  # noqa: E501
        :type: ProgressDto
        """

        self._progress = progress

    @property
    def client(self):
        """Gets the client of this Buyer.  # noqa: E501


        :return: The client of this Buyer.  # noqa: E501
        :rtype: ClientReference
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this Buyer.


        :param client: The client of this Buyer.  # noqa: E501
        :type: ClientReference
        """

        self._client = client

    @property
    def cost_center(self):
        """Gets the cost_center of this Buyer.  # noqa: E501


        :return: The cost_center of this Buyer.  # noqa: E501
        :rtype: CostCenterReference
        """
        return self._cost_center

    @cost_center.setter
    def cost_center(self, cost_center):
        """Sets the cost_center of this Buyer.


        :param cost_center: The cost_center of this Buyer.  # noqa: E501
        :type: CostCenterReference
        """

        self._cost_center = cost_center

    @property
    def business_unit(self):
        """Gets the business_unit of this Buyer.  # noqa: E501


        :return: The business_unit of this Buyer.  # noqa: E501
        :rtype: BusinessUnitReference
        """
        return self._business_unit

    @business_unit.setter
    def business_unit(self, business_unit):
        """Sets the business_unit of this Buyer.


        :param business_unit: The business_unit of this Buyer.  # noqa: E501
        :type: BusinessUnitReference
        """

        self._business_unit = business_unit

    @property
    def date_due(self):
        """Gets the date_due of this Buyer.  # noqa: E501


        :return: The date_due of this Buyer.  # noqa: E501
        :rtype: datetime
        """
        return self._date_due

    @date_due.setter
    def date_due(self, date_due):
        """Sets the date_due of this Buyer.


        :param date_due: The date_due of this Buyer.  # noqa: E501
        :type: datetime
        """

        self._date_due = date_due

    @property
    def status(self):
        """Gets the status of this Buyer.  # noqa: E501


        :return: The status of this Buyer.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Buyer.


        :param status: The status of this Buyer.  # noqa: E501
        :type: str
        """
        allowed_values = ["NEW", "ASSIGNED", "COMPLETED", "ACCEPTED_BY_VENDOR", "DECLINED_BY_VENDOR", "COMPLETED_BY_VENDOR", "CANCELLED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def purchase_order(self):
        """Gets the purchase_order of this Buyer.  # noqa: E501


        :return: The purchase_order of this Buyer.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order

    @purchase_order.setter
    def purchase_order(self, purchase_order):
        """Sets the purchase_order of this Buyer.


        :param purchase_order: The purchase_order of this Buyer.  # noqa: E501
        :type: str
        """

        self._purchase_order = purchase_order

    @property
    def is_published_on_job_board(self):
        """Gets the is_published_on_job_board of this Buyer.  # noqa: E501

        Default: false  # noqa: E501

        :return: The is_published_on_job_board of this Buyer.  # noqa: E501
        :rtype: bool
        """
        return self._is_published_on_job_board

    @is_published_on_job_board.setter
    def is_published_on_job_board(self, is_published_on_job_board):
        """Sets the is_published_on_job_board of this Buyer.

        Default: false  # noqa: E501

        :param is_published_on_job_board: The is_published_on_job_board of this Buyer.  # noqa: E501
        :type: bool
        """

        self._is_published_on_job_board = is_published_on_job_board

    @property
    def note(self):
        """Gets the note of this Buyer.  # noqa: E501


        :return: The note of this Buyer.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Buyer.


        :param note: The note of this Buyer.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def created_by(self):
        """Gets the created_by of this Buyer.  # noqa: E501


        :return: The created_by of this Buyer.  # noqa: E501
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Buyer.


        :param created_by: The created_by of this Buyer.  # noqa: E501
        :type: UserReference
        """

        self._created_by = created_by

    @property
    def quality_assurance_settings(self):
        """Gets the quality_assurance_settings of this Buyer.  # noqa: E501


        :return: The quality_assurance_settings of this Buyer.  # noqa: E501
        :rtype: IdReference
        """
        return self._quality_assurance_settings

    @quality_assurance_settings.setter
    def quality_assurance_settings(self, quality_assurance_settings):
        """Sets the quality_assurance_settings of this Buyer.


        :param quality_assurance_settings: The quality_assurance_settings of this Buyer.  # noqa: E501
        :type: IdReference
        """

        self._quality_assurance_settings = quality_assurance_settings

    @property
    def workflow_steps(self):
        """Gets the workflow_steps of this Buyer.  # noqa: E501


        :return: The workflow_steps of this Buyer.  # noqa: E501
        :rtype: list[ProjectWorkflowStepDto]
        """
        return self._workflow_steps

    @workflow_steps.setter
    def workflow_steps(self, workflow_steps):
        """Sets the workflow_steps of this Buyer.


        :param workflow_steps: The workflow_steps of this Buyer.  # noqa: E501
        :type: list[ProjectWorkflowStepDto]
        """

        self._workflow_steps = workflow_steps

    @property
    def analyse_settings(self):
        """Gets the analyse_settings of this Buyer.  # noqa: E501


        :return: The analyse_settings of this Buyer.  # noqa: E501
        :rtype: IdReference
        """
        return self._analyse_settings

    @analyse_settings.setter
    def analyse_settings(self, analyse_settings):
        """Sets the analyse_settings of this Buyer.


        :param analyse_settings: The analyse_settings of this Buyer.  # noqa: E501
        :type: IdReference
        """

        self._analyse_settings = analyse_settings

    @property
    def access_settings(self):
        """Gets the access_settings of this Buyer.  # noqa: E501


        :return: The access_settings of this Buyer.  # noqa: E501
        :rtype: IdReference
        """
        return self._access_settings

    @access_settings.setter
    def access_settings(self, access_settings):
        """Sets the access_settings of this Buyer.


        :param access_settings: The access_settings of this Buyer.  # noqa: E501
        :type: IdReference
        """

        self._access_settings = access_settings

    @property
    def financial_settings(self):
        """Gets the financial_settings of this Buyer.  # noqa: E501


        :return: The financial_settings of this Buyer.  # noqa: E501
        :rtype: IdReference
        """
        return self._financial_settings

    @financial_settings.setter
    def financial_settings(self, financial_settings):
        """Sets the financial_settings of this Buyer.


        :param financial_settings: The financial_settings of this Buyer.  # noqa: E501
        :type: IdReference
        """

        self._financial_settings = financial_settings

    @property
    def mt_settings_per_language_list(self):
        """Gets the mt_settings_per_language_list of this Buyer.  # noqa: E501


        :return: The mt_settings_per_language_list of this Buyer.  # noqa: E501
        :rtype: list[MTSettingsPerLanguageReference]
        """
        return self._mt_settings_per_language_list

    @mt_settings_per_language_list.setter
    def mt_settings_per_language_list(self, mt_settings_per_language_list):
        """Sets the mt_settings_per_language_list of this Buyer.


        :param mt_settings_per_language_list: The mt_settings_per_language_list of this Buyer.  # noqa: E501
        :type: list[MTSettingsPerLanguageReference]
        """

        self._mt_settings_per_language_list = mt_settings_per_language_list

    @property
    def vendor_owner(self):
        """Gets the vendor_owner of this Buyer.  # noqa: E501


        :return: The vendor_owner of this Buyer.  # noqa: E501
        :rtype: USER
        """
        return self._vendor_owner

    @vendor_owner.setter
    def vendor_owner(self, vendor_owner):
        """Sets the vendor_owner of this Buyer.


        :param vendor_owner: The vendor_owner of this Buyer.  # noqa: E501
        :type: USER
        """

        self._vendor_owner = vendor_owner

    @property
    def vendor(self):
        """Gets the vendor of this Buyer.  # noqa: E501


        :return: The vendor of this Buyer.  # noqa: E501
        :rtype: VendorReference
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this Buyer.


        :param vendor: The vendor of this Buyer.  # noqa: E501
        :type: VendorReference
        """

        self._vendor = vendor

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
        if issubclass(Buyer, dict):
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
        if not isinstance(other, Buyer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

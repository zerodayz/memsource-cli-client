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


class EditProjectDto(object):
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
        'name': 'str',
        'status': 'str',
        'client': 'IdReference',
        'business_unit': 'IdReference',
        'domain': 'IdReference',
        'sub_domain': 'IdReference',
        'owner': 'IdReference',
        'purchase_order': 'str',
        'date_due': 'datetime',
        'note': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'client': 'client',
        'business_unit': 'businessUnit',
        'domain': 'domain',
        'sub_domain': 'subDomain',
        'owner': 'owner',
        'purchase_order': 'purchaseOrder',
        'date_due': 'dateDue',
        'note': 'note'
    }

    def __init__(self, name=None, status=None, client=None, business_unit=None, domain=None, sub_domain=None, owner=None, purchase_order=None, date_due=None, note=None):  # noqa: E501
        """EditProjectDto - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._status = None
        self._client = None
        self._business_unit = None
        self._domain = None
        self._sub_domain = None
        self._owner = None
        self._purchase_order = None
        self._date_due = None
        self._note = None
        self.discriminator = None

        self.name = name
        if status is not None:
            self.status = status
        if client is not None:
            self.client = client
        if business_unit is not None:
            self.business_unit = business_unit
        if domain is not None:
            self.domain = domain
        if sub_domain is not None:
            self.sub_domain = sub_domain
        if owner is not None:
            self.owner = owner
        if purchase_order is not None:
            self.purchase_order = purchase_order
        if date_due is not None:
            self.date_due = date_due
        if note is not None:
            self.note = note

    @property
    def name(self):
        """Gets the name of this EditProjectDto.  # noqa: E501


        :return: The name of this EditProjectDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EditProjectDto.


        :param name: The name of this EditProjectDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this EditProjectDto.  # noqa: E501


        :return: The status of this EditProjectDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EditProjectDto.


        :param status: The status of this EditProjectDto.  # noqa: E501
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
    def client(self):
        """Gets the client of this EditProjectDto.  # noqa: E501


        :return: The client of this EditProjectDto.  # noqa: E501
        :rtype: IdReference
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this EditProjectDto.


        :param client: The client of this EditProjectDto.  # noqa: E501
        :type: IdReference
        """

        self._client = client

    @property
    def business_unit(self):
        """Gets the business_unit of this EditProjectDto.  # noqa: E501


        :return: The business_unit of this EditProjectDto.  # noqa: E501
        :rtype: IdReference
        """
        return self._business_unit

    @business_unit.setter
    def business_unit(self, business_unit):
        """Sets the business_unit of this EditProjectDto.


        :param business_unit: The business_unit of this EditProjectDto.  # noqa: E501
        :type: IdReference
        """

        self._business_unit = business_unit

    @property
    def domain(self):
        """Gets the domain of this EditProjectDto.  # noqa: E501


        :return: The domain of this EditProjectDto.  # noqa: E501
        :rtype: IdReference
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this EditProjectDto.


        :param domain: The domain of this EditProjectDto.  # noqa: E501
        :type: IdReference
        """

        self._domain = domain

    @property
    def sub_domain(self):
        """Gets the sub_domain of this EditProjectDto.  # noqa: E501


        :return: The sub_domain of this EditProjectDto.  # noqa: E501
        :rtype: IdReference
        """
        return self._sub_domain

    @sub_domain.setter
    def sub_domain(self, sub_domain):
        """Sets the sub_domain of this EditProjectDto.


        :param sub_domain: The sub_domain of this EditProjectDto.  # noqa: E501
        :type: IdReference
        """

        self._sub_domain = sub_domain

    @property
    def owner(self):
        """Gets the owner of this EditProjectDto.  # noqa: E501


        :return: The owner of this EditProjectDto.  # noqa: E501
        :rtype: IdReference
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this EditProjectDto.


        :param owner: The owner of this EditProjectDto.  # noqa: E501
        :type: IdReference
        """

        self._owner = owner

    @property
    def purchase_order(self):
        """Gets the purchase_order of this EditProjectDto.  # noqa: E501


        :return: The purchase_order of this EditProjectDto.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order

    @purchase_order.setter
    def purchase_order(self, purchase_order):
        """Sets the purchase_order of this EditProjectDto.


        :param purchase_order: The purchase_order of this EditProjectDto.  # noqa: E501
        :type: str
        """
        if purchase_order is not None and len(purchase_order) > 255:
            raise ValueError("Invalid value for `purchase_order`, length must be less than or equal to `255`")  # noqa: E501
        if purchase_order is not None and len(purchase_order) < 0:
            raise ValueError("Invalid value for `purchase_order`, length must be greater than or equal to `0`")  # noqa: E501

        self._purchase_order = purchase_order

    @property
    def date_due(self):
        """Gets the date_due of this EditProjectDto.  # noqa: E501


        :return: The date_due of this EditProjectDto.  # noqa: E501
        :rtype: datetime
        """
        return self._date_due

    @date_due.setter
    def date_due(self, date_due):
        """Sets the date_due of this EditProjectDto.


        :param date_due: The date_due of this EditProjectDto.  # noqa: E501
        :type: datetime
        """

        self._date_due = date_due

    @property
    def note(self):
        """Gets the note of this EditProjectDto.  # noqa: E501


        :return: The note of this EditProjectDto.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this EditProjectDto.


        :param note: The note of this EditProjectDto.  # noqa: E501
        :type: str
        """
        if note is not None and len(note) > 4096:
            raise ValueError("Invalid value for `note`, length must be less than or equal to `4096`")  # noqa: E501
        if note is not None and len(note) < 0:
            raise ValueError("Invalid value for `note`, length must be greater than or equal to `0`")  # noqa: E501

        self._note = note

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
        if issubclass(EditProjectDto, dict):
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
        if not isinstance(other, EditProjectDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
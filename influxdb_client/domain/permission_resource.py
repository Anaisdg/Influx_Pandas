# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PermissionResource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'id': 'str',
        'name': 'str',
        'org_id': 'str',
        'org': 'str'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'org_id': 'orgID',
        'org': 'org'
    }

    def __init__(self, type=None, id=None, name=None, org_id=None, org=None):  # noqa: E501
        """PermissionResource - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._id = None
        self._name = None
        self._org_id = None
        self._org = None
        self.discriminator = None

        self.type = type
        self.id = id
        self.name = name
        self.org_id = org_id
        self.org = org

    @property
    def type(self):
        """Gets the type of this PermissionResource.  # noqa: E501


        :return: The type of this PermissionResource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PermissionResource.


        :param type: The type of this PermissionResource.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def id(self):
        """Gets the id of this PermissionResource.  # noqa: E501

        If ID is set that is a permission for a specific resource. if it is not set it is a permission for all resources of that resource type.  # noqa: E501

        :return: The id of this PermissionResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PermissionResource.

        If ID is set that is a permission for a specific resource. if it is not set it is a permission for all resources of that resource type.  # noqa: E501

        :param id: The id of this PermissionResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PermissionResource.  # noqa: E501

        Optional name of the resource if the resource has a name field.  # noqa: E501

        :return: The name of this PermissionResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PermissionResource.

        Optional name of the resource if the resource has a name field.  # noqa: E501

        :param name: The name of this PermissionResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this PermissionResource.  # noqa: E501

        If orgID is set that is a permission for all resources owned my that org. if it is not set it is a permission for all resources of that resource type.  # noqa: E501

        :return: The org_id of this PermissionResource.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this PermissionResource.

        If orgID is set that is a permission for all resources owned my that org. if it is not set it is a permission for all resources of that resource type.  # noqa: E501

        :param org_id: The org_id of this PermissionResource.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def org(self):
        """Gets the org of this PermissionResource.  # noqa: E501

        Optional name of the organization of the organization with orgID.  # noqa: E501

        :return: The org of this PermissionResource.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this PermissionResource.

        Optional name of the organization of the organization with orgID.  # noqa: E501

        :param org: The org of this PermissionResource.  # noqa: E501
        :type: str
        """

        self._org = org

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PermissionResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
